"""
Monte Carlo: 10.000 iteraciones por partido.
Proyecta déficit (% PIB), deuda (% PIB), PIB nominal y paro a 1, 2, 3 y 4 años.

Baseline 2025 (fuentes oficiales):
  PIB 1.690.012 M (INE CNA 2025)
  Deuda 100,7% PIB (Banco de España)
  Déficit estructural 2,2% (IGAE, sin DANA)
  Paro 9,93% (INE EPA Q4-2025)

Modelo: stock-flujo consistente.
  D(t) = D(t-1) + Def(t)
  Y(t) = Y(t-1) * (1 + g(t))
  b(t) = D(t) / Y(t) * 100
  Def(t) = def_base * Y(t) + neto_partido(t) + extra_intereses(t)
  extra_intereses = D(t-1) * spread * passthrough(t)

Incertidumbre: distribuciones triangulares (min, moda, max) en:
  - merma/gasto bruto
  - ahorro/ingresos compensatorios
  - tasa de recuperación (multiplicador)
  - impulso PIB corto plazo
  - spread de riesgo (prima)
  - drag por confianza/incertidumbre

Solo librería estándar. Semilla 42 para reproducibilidad.
Uso: python 05_montecarlo.py
"""
import random

random.seed(42)
N = 10000
YEARS = 4

# === Baseline (fuentes oficiales) ===
PIB0 = 1690.012        # B (INE CNA 2025)
DEUDA0_PCT = 100.7     # % PIB (Banco de España)
D0 = PIB0 * DEUDA0_PCT / 100
DEF_BASE = 0.022       # 2,2% déficit estructural (IGAE)
G_NOM_BASE = 0.045     # 4,5% crecimiento nominal (2,2% real + 2,3% deflactor)
PARO0 = 9.93           # % (INE EPA Q4-2025)
G_POT = 0.022          # crecimiento potencial para ley de Okun
INFLA_BASE = 0.023     # 2,3% deflactor base

# === Parámetros por partido ===
# Formato: (min, moda, max) para distribución triangular
# Saldos en B, tasas en fraccion decimal

PARTIDOS = {
    "VOX": {
        "tipo": "merma_ahorro",
        "desc": "IRPF 85B (Hacienda 13-10-2026) 2 tramos 15/25% exento 22k | IVA 21->18 10->8 0% alimentos 4% energía | Soc 25->15% | Suprimir Patrimonio/Sucesiones/Plusvalía | Exención IRPF pensiones (14,3B AEAT) | Cuota autónomos 0 <SMI | Bonif SS nuevos indefinidos | Ahorro 40B prometido",
        # Merma bruta: 135-149B (IRPF corregido a 85B, Hacienda 13-10-2026)
        # VOX decía 40B (solo tramo estatal); Hacienda confirma 85B = 61% recaudación IRPF
        "merma": (125, 149, 175),
        # Ahorro: 8B realista año 1 -> 40B prometido
        "ahorro": (8, 22, 40),
        # Recuperación vía mayor consumo/empleo: 10-25%
        "recup_rate": (0.10, 0.18, 0.25),
        # Eficacia del ahorro (no todo se materializa): 65-95%
        "ahorro_ef": (0.65, 0.85, 0.95),
        # Impulso PIB año 1: +0,5 a +4,0pp (repo central +2,8pp con IRPF 85B)
        "impulso": (0.005, 0.028, 0.040),
        # Spread prima de riesgo: 40-220bp (repo 80-150bp)
        "spread": (0.004, 0.011, 0.022),
        # Drag confianza año 2+: -2pp (conflictos UE/CCAA) a 0
        "drag": (-0.020, -0.004, 0.0),
    },
    "PP": {
        "tipo": "merma_ahorro",
        "desc": "Deflactar IRPF <40k | Duplicar mínimos por hijo | IVA 0% básicos vivienda joven | Bajada tipos autónomos | 1M viviendas",
        "merma": (22, 27, 35),
        "ahorro": (2, 7, 12),
        "recup_rate": (0.10, 0.18, 0.25),
        "ahorro_ef": (0.75, 0.90, 1.0),
        "impulso": (0.002, 0.007, 0.013),
        "spread": (0.001, 0.003, 0.007),
        "drag": (-0.005, 0.0, 0.003),
    },
    "PSOE": {
        "tipo": "neto_fijo",
        "desc": "SMI 1.221x14 | Pensiones +2,7% (+mínimas +7-11,4%) | Jornada 36h antes 2030 | PRTR 77B | MEI 0,9%",
        # Gasto neto pequeño: SMI, pensiones, PRTR vs MEI/cuotas
        "neto": (1.0, 3.0, 6.0),
        "impulso": (-0.002, 0.005, 0.012),
        "spread": (0.0, 0.0005, 0.0025),
        "drag": (-0.003, 0.0, 0.0),
    },
    "SUMAR": {
        "tipo": "gasto_ingresos",
        "desc": "Crianza 200/mes | Herencia 20k a los 23 | IRPF 52% desde 300k | Gravamen 3% >50M | Vivienda 1% PIB | 30h semanales",
        # Gasto: crianza + herencia + vivienda + impuestos
        "gasto": (32, 41.5, 55),
        # Ingresos: IRPF 52% + gravamen 50M + sociedades
        "ingresos": (12, 20, 30),
        # Retorno del gasto social via consumo: 0-25%
        "recup_rate": (0.0, 0.10, 0.25),
        "impulso": (-0.015, -0.002, 0.008),
        "spread": (0.0015, 0.0055, 0.012),
        "drag": (-0.010, -0.002, 0.0),
    },
}


def pctile(data, p):
    """Percentil p (0-100) de datos ya ordenados."""
    k = (len(data) - 1) * p / 100.0
    f = int(k)
    c = k - f
    if f + 1 < len(data):
        return data[f] + c * (data[f + 1] - data[f])
    return data[f]


def simulate(params, n_iter, is_base=False):
    """Ejecuta n_iter iteraciones de 4 años."""
    res = {y: {"def": [], "deuda": [], "pib": [], "paro": []}
           for y in range(1, YEARS + 1)}

    for _ in range(n_iter):
        if is_base:
            neto_base = 0.0
            impulso = random.gauss(0, 0.003)
            spread = 0.0
            drag = 0.0
        else:
            tp = params["tipo"]
            if tp == "merma_ahorro":
                merma = random.triangular(*params["merma"])
                ahorro = random.triangular(*params["ahorro"])
                recup = random.triangular(*params["recup_rate"])
                aef = random.triangular(*params["ahorro_ef"])
                neto_base = merma * (1 - recup) - ahorro * aef
            elif tp == "neto_fijo":
                neto_base = random.triangular(*params["neto"])
            elif tp == "gasto_ingresos":
                gasto = random.triangular(*params["gasto"])
                ing = random.triangular(*params["ingresos"])
                recup = random.triangular(*params["recup_rate"])
                neto_base = gasto * (1 - recup) - ing

            impulso = random.triangular(*params["impulso"])
            spread = random.triangular(*params["spread"])
            drag = random.triangular(*params["drag"])

        Y = PIB0
        D = D0
        paro = PARO0

        for t in range(YEARS):
            # Crecimiento nominal
            imp_t = impulso * max(0, 1 - t * 0.3)
            drag_t = drag if t >= 1 else 0.0
            g = G_NOM_BASE + imp_t + drag_t + random.gauss(0, 0.003)

            Y_prev = Y
            Y = Y_prev * (1 + g)
            scale = Y / PIB0

            # Impacto fiscal neto (escala con PIB)
            neto = neto_base * scale

            # Intereses extra por spread
            passthru = 0.20 + 0.10 * t
            extra_int = D * spread * passthru

            # Déficit total
            def_base = DEF_BASE * Y
            def_tot = def_base + neto + extra_int

            # Deuda
            D = D + def_tot

            # Ratios
            dp = def_tot / Y * 100
            bp = D / Y * 100

            # Paro (Okun simplificado)
            g_real = g - INFLA_BASE
            paro = paro - 0.5 * (g_real - G_POT) * 100
            paro = max(3.0, min(25.0, paro))

            yk = t + 1
            res[yk]["def"].append(dp)
            res[yk]["deuda"].append(bp)
            res[yk]["pib"].append(Y)
            res[yk]["paro"].append(paro)

    return res


def show(name, res):
    print(f"\n{'='*95}")
    print(f"=== {name} ===")
    hdr = (f"{'Año':<6} {'Déficit %PIB':>28} {'Deuda %PIB':>22} "
           f"{'PIB acum':>9} {'Paro %':>7} {'P(EDP)':>7} {'P(>110%)':>8} {'P(>5%)':>7}")
    print(hdr)
    print("-" * 95)

    for y in range(1, YEARS + 1):
        d = res[y]
        defs = sorted(d["def"])
        debts = sorted(d["deuda"])
        pibs = sorted(d["pib"])
        paros = sorted(d["paro"])
        n = len(defs)

        dm = sum(defs) / n
        dmed = pctile(defs, 50)
        d5 = pctile(defs, 5)
        d95 = pctile(defs, 95)

        bm = sum(debts) / n
        b5 = pctile(debts, 5)
        b95 = pctile(debts, 95)

        pm = sum(pibs) / n
        pg = (pm / PIB0 - 1) * 100

        prm = sum(paros) / n

        pe = sum(1 for x in defs if x > 3.0) / n * 100
        pd = sum(1 for x in debts if x > 110) / n * 100
        p5 = sum(1 for x in defs if x > 5.0) / n * 100

        yr = 2025 + y
        line = (f"{yr:<6} {dm:>5.1f} (med {dmed:>4.1f}) [{d5:>4.1f}-{d95:>4.1f}] "
                f"{bm:>5.1f} [{b5:>4.1f}-{b95:>4.1f}] "
                f"{pg:>7.1f}% {prm:>5.1f} {pe:>5.0f}% {pd:>6.0f}% {p5:>5.0f}%")
        print(line)


# === Ejecucion ===
print("=" * 95)
print("SIMULACIÓN MONTE CARLO -- 10.000 iteraciones por partido")
print("Baseline 2025: PIB 1.690 B (INE), deuda 100,7% (BdE), déficit 2,2% (IGAE), paro 9,93% (INE EPA)")
print("Modelo stock-flujo: D(t)=D(t-1)+Def(t), Y(t)=Y(t-1)*(1+g), b=D/Y")
print("Incertidumbre triangular en merma, ahorro, multiplicadores, spread, crecimiento")
print(f"Semilla: 42 | Iteraciones: {N} | Horizonte: {YEARS} años (2026-2029)")
print("=" * 95)

all_res = {}
all_res["BASE"] = simulate(None, N, is_base=True)
for name, params in PARTIDOS.items():
    all_res[name] = simulate(params, N)

for name in ["BASE", "PSOE", "PP", "SUMAR", "VOX"]:
    show(name, all_res[name])

# === Resumen comparativo ===
print(f"\n{'='*95}")
print(f"RESUMEN COMPARATIVO -- Año 4 (2029)")
print(f"{'='*95}")
hdr = (f"{'Partido':<12} {'Def.medio':>10} {'P(EDP>3%)':>10} {'P(Def>5%)':>10} "
       f"{'Deuda media':>12} {'P(>110%)':>9} {'PIB acum':>9} {'Paro':>6}")
print(hdr)
print("-" * 95)

for name in ["BASE", "PSOE", "PP", "SUMAR", "VOX"]:
    d4 = all_res[name][YEARS]
    defs = sorted(d4["def"])
    debts = sorted(d4["deuda"])
    pibs = sorted(d4["pib"])
    paros = sorted(d4["paro"])
    n = len(defs)

    dm = sum(defs) / n
    bm = sum(debts) / n
    pg = (sum(pibs) / n / PIB0 - 1) * 100
    prm = sum(paros) / n
    pe = sum(1 for x in defs if x > 3.0) / n * 100
    p5 = sum(1 for x in defs if x > 5.0) / n * 100
    pd = sum(1 for x in debts if x > 110) / n * 100

    print(f"{name:<12} {dm:>7.1f}% {pe:>8.0f}% {p5:>8.0f}% "
          f"{bm:>10.1f}% {pd:>7.0f}% {pg:>7.1f}% {prm:>5.1f}%")

# === Markdown para repo ===
md = []
md.append("# Simulación Monte Carlo (10.000 iteraciones)\n\n")
md.append("Baseline 2025: PIB 1.690 B (INE CNA), deuda 100,7% (Banco de España), ")
md.append("déficit 2,2% estructural (IGAE), paro 9,93% (INE EPA Q4-2025).\n\n")
md.append("Modelo stock-flujo con incertidumbre triangular en merma, ahorro, multiplicadores, ")
md.append("spread y crecimiento. Semilla 42 para reproducibilidad. Solo librería estándar.\n\n")

md.append("## Parámetros por partido\n\n")
for name, p in PARTIDOS.items():
    md.append(f"### {name}\n")
    md.append(f"**Propuestas**: {p['desc']}\n\n")
    if p["tipo"] == "merma_ahorro":
        md.append(f"| Parámetro | Min | Moda | Max | Unidad |\n|---|---|---|---|---|\n")
        md.append(f"| Merma bruta | {p['merma'][0]} | {p['merma'][1]} | {p['merma'][2]} | B |\n")
        md.append(f"| Ahorro | {p['ahorro'][0]} | {p['ahorro'][1]} | {p['ahorro'][2]} | B |\n")
        md.append(f"| Recuperación | {p['recup_rate'][0]*100:.0f} | {p['recup_rate'][1]*100:.0f} | {p['recup_rate'][2]*100:.0f} | % |\n")
        md.append(f"| Eficacia ahorro | {p['ahorro_ef'][0]*100:.0f} | {p['ahorro_ef'][1]*100:.0f} | {p['ahorro_ef'][2]*100:.0f} | % |\n")
        md.append(f"| Impulso PIB | {p['impulso'][0]*100:.1f} | {p['impulso'][1]*100:.1f} | {p['impulso'][2]*100:.1f} | pp |\n")
        md.append(f"| Spread | {p['spread'][0]*10000:.0f} | {p['spread'][1]*10000:.0f} | {p['spread'][2]*10000:.0f} | pb |\n")
        md.append(f"| Drag confianza | {p['drag'][0]*100:.1f} | {p['drag'][1]*100:.1f} | {p['drag'][2]*100:.1f} | pp |\n\n")
    elif p["tipo"] == "neto_fijo":
        md.append(f"| Parámetro | Min | Moda | Max | Unidad |\n|---|---|---|---|---|\n")
        md.append(f"| Neto fiscal | {p['neto'][0]} | {p['neto'][1]} | {p['neto'][2]} | B |\n")
        md.append(f"| Impulso PIB | {p['impulso'][0]*100:.1f} | {p['impulso'][1]*100:.1f} | {p['impulso'][2]*100:.1f} | pp |\n")
        md.append(f"| Spread | {p['spread'][0]*10000:.0f} | {p['spread'][1]*10000:.0f} | {p['spread'][2]*10000:.0f} | pb |\n")
        md.append(f"| Drag confianza | {p['drag'][0]*100:.1f} | {p['drag'][1]*100:.1f} | {p['drag'][2]*100:.1f} | pp |\n\n")
    elif p["tipo"] == "gasto_ingresos":
        md.append(f"| Parámetro | Min | Moda | Max | Unidad |\n|---|---|---|---|---|\n")
        md.append(f"| Gasto | {p['gasto'][0]} | {p['gasto'][1]} | {p['gasto'][2]} | B |\n")
        md.append(f"| Ingresos | {p['ingresos'][0]} | {p['ingresos'][1]} | {p['ingresos'][2]} | B |\n")
        md.append(f"| Recuperación | {p['recup_rate'][0]*100:.0f} | {p['recup_rate'][1]*100:.0f} | {p['recup_rate'][2]*100:.0f} | % |\n")
        md.append(f"| Impulso PIB | {p['impulso'][0]*100:.1f} | {p['impulso'][1]*100:.1f} | {p['impulso'][2]*100:.1f} | pp |\n")
        md.append(f"| Spread | {p['spread'][0]*10000:.0f} | {p['spread'][1]*10000:.0f} | {p['spread'][2]*10000:.0f} | pb |\n")
        md.append(f"| Drag confianza | {p['drag'][0]*100:.1f} | {p['drag'][1]*100:.1f} | {p['drag'][2]*100:.1f} | pp |\n\n")

md.append("## Resultados por partido\n\n")
for name in ["BASE", "PSOE", "PP", "SUMAR", "VOX"]:
    if name == "BASE":
        md.append(f"### BASE (sin medidas de partido)\n\n")
    else:
        md.append(f"### {name}\n")
        md.append(f"**Propuestas**: {PARTIDOS[name]['desc']}\n\n")

    md.append(f"| Año | Déficit % (mediana) [P5-P95] | Deuda % [P5-P95] | PIB acum | Paro % | P(EDP>3%) | P(Deuda>110%) | P(Def>5%) |\n")
    md.append(f"|---|---|---|---|---|---|---|---|\n")

    for y in range(1, YEARS + 1):
        d = all_res[name][y]
        defs = sorted(d["def"])
        debts = sorted(d["deuda"])
        pibs = sorted(d["pib"])
        paros = sorted(d["paro"])
        n = len(defs)

        dm = sum(defs) / n
        dmed = pctile(defs, 50)
        d5 = pctile(defs, 5)
        d95 = pctile(defs, 95)
        bm = sum(debts) / n
        b5 = pctile(debts, 5)
        b95 = pctile(debts, 95)
        pg = (sum(pibs) / n / PIB0 - 1) * 100
        prm = sum(paros) / n
        pe = sum(1 for x in defs if x > 3.0) / n * 100
        pd = sum(1 for x in debts if x > 110) / n * 100
        p5 = sum(1 for x in defs if x > 5.0) / n * 100

        yr = 2025 + y
        md.append(f"| {yr} | {dm:.1f} ({dmed:.1f}) [{d5:.1f}-{d95:.1f}] | "
                  f"{bm:.1f} [{b5:.1f}-{b95:.1f}] | {pg:.1f}% | {prm:.1f} | "
                  f"{pe:.0f}% | {pd:.0f}% | {p5:.0f}% |\n")

    md.append("\n")

md.append("## Resumen comparativo (Año 4 - 2029)\n\n")
md.append("| Partido | Déficit medio | P(EDP>3%) | P(Def>5%) | Deuda media | P(>110%) | PIB acum | Paro medio |\n")
md.append("|---|---|---|---|---|---|---|---|\n")
for name in ["BASE", "PSOE", "PP", "SUMAR", "VOX"]:
    d4 = all_res[name][YEARS]
    defs = sorted(d4["def"])
    debts = sorted(d4["deuda"])
    pibs = sorted(d4["pib"])
    paros = sorted(d4["paro"])
    n = len(defs)

    dm = sum(defs) / n
    bm = sum(debts) / n
    pg = (sum(pibs) / n / PIB0 - 1) * 100
    prm = sum(paros) / n
    pe = sum(1 for x in defs if x > 3.0) / n * 100
    p5 = sum(1 for x in defs if x > 5.0) / n * 100
    pd = sum(1 for x in debts if x > 110) / n * 100

    md.append(f"| {name} | {dm:.1f}% | {pe:.0f}% | {p5:.0f}% | {bm:.1f}% | {pd:.0f}% | {pg:.1f}% | {prm:.1f}% |\n")

md.append("\n## Metodología\n\n")
md.append("- **Modelo**: stock-flujo consistente. D(t)=D(t-1)+Def(t), Y(t)=Y(t-1)*(1+g(t)), b(t)=D(t)/Y(t).\n")
md.append("- **Def(t)** = déficit base (2,2% PIB) + impacto fiscal neto del partido + intereses extra por prima de riesgo.\n")
md.append("- **Impacto neto**: merma*(1-recuperación) - ahorro*eficacia (VOX/PP); gasto neto (PSOE); gasto*(1-recup) - ingresos (SUMAR).\n")
md.append("- **Passthrough del spread**: gradual (20% año 1, +10pp/año) sobre el stock de deuda.\n")
md.append("- **Impulso PIB**: decae 30%/año desde año 1.\n")
md.append("- **Drag confianza**: activo desde año 2.\n")
md.append("- **Paro**: ley de Okun simplificada (delta_paro = -0,5*(g_real - g_potencial)).\n")
md.append("- **Distribuciones**: triangulares (min, moda, max) calibradas con datos del repo y fuentes oficiales.\n")
md.append("- **Ruido**: gauss(0, 0,3%) añadido al crecimiento para variabilidad no explicada.\n")
md.append("- **Fuentes**: INE (PIB CNA, EPA, EAES), Banco de España (deuda), IGAE (déficit), AEAT (recaudación IRPF/IVA/pensiones), La Moncloa/BOE (SMI, pensiones).\n")
md.append("- **Limitaciones**: parámetros muestreados independientemente (sin correlación entre merma y spread); el impulso fiscal no distingue oferta/demanda; el paro usa Okun simplificado.\n")

with open("comparativa/05_montecarlo_resultados.md", "w", encoding="utf-8") as f:
    f.writelines(md)

print(f"\nResultados guardados en comparativa/05_montecarlo_resultados.md")
