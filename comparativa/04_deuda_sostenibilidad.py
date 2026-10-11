"""
Sostenibilidad de deuda 2026-2030 — simulacion consistente stock-flujo
No predice quiebra ni fechas. Estima deficit, deuda % PIB y ajuste necesario
bajo escenarios alternativos de ahorro, crecimiento e intereses.

Ley: D_t = D_{t-1} + Def_t ; Y_t = Y_{t-1}*(1+g_t) ; b_t = D_t/Y_t
Def_t = base_t + neto_partido_t + extra_intereses_t
extra_intereses por spread con pass-through gradual (solo nueva emision y rollover ~20%/ano).

Baseline 2025 verificado: Y=1690.012B (INE CNA), b=100.7% => D=1702.04B, deficit 2.39%.
Hipotesis base 2026-30 sin medidas: deficit 2.2% constante, g nominal 4.5% (2.2 real +2.3 deflactor),
i implicito 3.0% (intereses ~3% PIB, primario superavit ~0.8%). SFA 0.
Uso: python 04_deuda_sostenibilidad.py
"""
Y2025 = 1690.012
B2025 = 100.7
D2025 = Y2025 * B2025 / 100
G0 = 0.045
I0 = 0.030
DEF_BASE = 0.022

PARTIDOS = {
    # merma/gasto bruto permanente, recuperacion base, ahorros por escenario, impulso PIB, spread bp
    "VOX":  {"bruta": 96.5, "recup_rate": 0.15, "ahorro": {"pes": 12.0, "cen": 25.0, "opt": 40.0}, "impulso": [0.012, 0.006, 0.0, 0.0, 0.0], "spread_bp": {"pes": 150, "cen": 110, "opt": 60}, "drag_confianza": {"pes": -0.008, "cen": -0.004, "opt": 0.0}},
    "PP":   {"bruta": 27.0, "recup_rate": 0.15, "ahorro": {"pes": 4.0, "cen": 7.0, "opt": 10.0},  "impulso": [0.006, 0.004, 0.002, 0.002, 0.002], "spread_bp": {"pes": 40, "cen": 30, "opt": 15}, "drag_confianza": {"pes": 0.0, "cen": 0.0, "opt": 0.0}},
    "PSOE": {"bruta": 0.0,  "recup_rate": 0.0,  "ahorro": {"pes": 0.0, "cen": 0.0, "opt": 0.0},   "impulso": [0.0]*5, "spread_bp": {"pes": 10, "cen": 0, "opt": 0}, "drag_confianza": {"pes": 0.0, "cen": 0.0, "opt": 0.0}, "neto_fijo": {"pes": 4.0, "cen": 3.0, "opt": 1.5}},
    "SUMAR":{"bruta": 41.5, "recup_rate": 0.0,  "ahorro_ing": {"pes": 17.0, "cen": 20.0, "opt": 24.8}, "impulso": [0.004, -0.005, -0.006, -0.006, -0.006], "spread_bp": {"pes": 80, "cen": 55, "opt": 30}, "drag_confianza": {"pes": -0.004, "cen": -0.002, "opt": 0.0}},
}

def simular(partido, escenario):
    P = PARTIDOS[partido]
    Y, D = Y2025, D2025
    rows = []
    for t in range(5):
        year = 2026 + t
        # crecimiento: base + impulso + drag confianza desde t>=1 si deficit alto (simplificado: siempre aplica drag)
        g = G0 + P["impulso"][t] + (P["drag_confianza"][escenario] if t >= 1 else 0.0)
        # deficit base
        Y_prev = Y
        Y = Y_prev * (1 + g)
        def_base = DEF_BASE * Y
        # neto partido (en B corrientes, escala con Y nominal para permanencia en % PIB)
        scale = Y / Y2025
        if partido == "PSOE":
            neto = P["neto_fijo"][escenario] * scale
        elif partido == "SUMAR":
            neto = (P["bruta"] * scale - P["ahorro_ing"][escenario] * scale)
        else:
            bruto_ef = P["bruta"] * (1 - P["recup_rate"]) * scale
            neto = bruto_ef - P["ahorro"][escenario] * scale
        # extra intereses: spread * D_{t-1} * pass-through (20% ano1 -> 60% ano5)
        passthrough = 0.20 + 0.10 * t
        spread = P["spread_bp"][escenario] / 10000
        extra_int = D * spread * passthrough
        deft = def_base + neto + extra_int
        D = D + deft
        b = D / Y * 100
        # primario aprox y ajuste para estabilizar en b actual: pb* = b*(i-g)/(1+g)
        i_eff = I0 + spread * passthrough
        pb_star = b * (i_eff - g) / (1 + g)  # negativo = superavit necesario? signo: si i<g, pb* negativo (puede haber deficit primario)
        rows.append({"year": year, "g_pct": g*100, "i_eff_pct": i_eff*100, "def_B": deft, "def_pct": deft/Y*100, "neto_B": neto, "extra_int_B": extra_int, "deuda_pct": b, "pb_star_pct": pb_star})
    return rows

if __name__ == "__main__":
    for p in ["VOX", "PP", "PSOE", "SUMAR"]:
        print(f"\n=== {p} ===")
        for esc in ["pes", "cen", "opt"]:
            rows = simular(p, esc)
            d2030 = rows[-1]["deuda_pct"]
            def2030 = rows[-1]["def_pct"]
            print(f" -- {esc}: deficit 2030 {def2030:.2f}% | deuda 2030 {d2030:.1f}%")
            for r in rows:
                print(f"    {r['year']} g={r['g_pct']:.2f}% i={r['i_eff_pct']:.2f}% def={r['def_B']:.1f}B ({r['def_pct']:.2f}%) neto={r['neto_B']:.1f}B extra_int={r['extra_int_B']:.1f}B deuda={r['deuda_pct']:.1f}% (pb*={r['pb_star_pct']:.2f}%)")
    print("\nLectura: no es prevision de impago. Si deficit >3% persistente, la UE exige correccion (EDP) y el Tesoro paga mas intereses. pb* indica el saldo primario que estabilizaria la deuda con ese i,g.")
