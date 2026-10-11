"""
Simulacion VOX - todas las propuestas economicas a la vez
Baseline INE CNA2025 + AEAT 2024 + BdE + IGAE + Seg.Social + EPA/EAES
Uso: python vox_simulacion.py
"""
BASELINE = {
    "PIB_2025_M": 1690012 / 1000,  # M€
    "PIB_per_capita_2025": 34365,
    "crec_2023": 2.4, "crec_2024": 3.7, "crec_2025": 2.6,
    "deuda_pct_2025": 100.7, "deficit_pct_base": 2.39, "deficit_abs_base_M": 40330 / 1000,
    "AEAT_total_2024_M": 294734 / 1000,
    "IRPF_2024_M": 129408 / 1000, "IVA_2024_M": 90541 / 1000,
    "SOC_2024_M": 39096 / 1000, "ESP_2024_M": 22128 / 1000,
    "COTIZ_2024_M": 199595 / 1000, "GASTO_2024_M": 725001 / 1000,
    "PENSIONES_2025_M": 189600 / 1000, "SMI_2025": 16576, "SMI_2026": 17094,
    "SALARIO_MEDIO_2024": 29540.26, "PARO_Q4_24": 10.61, "IPC_2024": 2.8,
    "fuentes": "INE CNA2025 https://www.ine.es/dyngs/Prensa/CNA2025.htm, EAES https://www.ine.es/dyngs/Prensa/EAES2024.htm, EPA https://www.ine.es/dyngs/Prensa/es/EPA4T24.htm, AEAT Informe 2024, BdE deuda, Hacienda deficit, Seg.Social pensiones"
}
PIB = BASELINE["PIB_2025_M"]  # 1690.012 B = M€ en miles? Ojo: valores en M€/1000 = B€
# En este script todo en B€ (miles de M€). PIB=1690.012 B€? No: 1.690.012 M€ = 1690.012 B€? 1B=1000M, asi PIB=1690.012 B€? Correcto 1690 B€.
# Para evitar confusion: PIB_B = 1690.012
PIB_B = 1690.012
def pp(x_B): return x_B / PIB_B * 100

COSTES = {
    "irpf_2tramos_exento22k_menos4pp_hijo": 40.0,
    "iva_21a18_general": 9.05,   # 70% base *3/21 sobre 90.541
    "iva_10a8_reducido": 4.525,  # 25% base *2/10
    "iva_0_alimentos": 2.5,
    "iva_4_energia_sin_IIEE": 2.0,
    "soc_25a15": 12.0,  # estatico 15.6, VOX dice 10, central 12
    "patrimonio": 1.4, "sucesiones": 3.2, "plusvalia_IIVTNU": 1.5, "itp_ajd_rebaja": 4.5,
    "exencion_irpf_pensiones": 13.0,
    "cuota_autonomos_menorSMI": 6.25,
    "bonif_SS_nuevos_indefinidos": 3.2,
}
COSTES["iva_total"] = COSTES["iva_21a18_general"] + COSTES["iva_10a8_reducido"] + COSTES["iva_0_alimentos"] + COSTES["iva_4_energia_sin_IIEE"]
COSTES["impuestos_suprimidos"] = COSTES["patrimonio"] + COSTES["sucesiones"] + COSTES["plusvalia_IIVTNU"] + COSTES["itp_ajd_rebaja"]
merma_bruta = sum([COSTES["irpf_2tramos_exento22k_menos4pp_hijo"], COSTES["iva_total"], COSTES["soc_25a15"], COSTES["impuestos_suprimidos"], COSTES["exencion_irpf_pensiones"], COSTES["cuota_autonomos_menorSMI"], COSTES["bonif_SS_nuevos_indefinidos"]])
ahorro = 40.0
neto_estatico = merma_bruta - ahorro
# Dinamico: recupera 18% merma, ahorro pierde 15% por menor PIB
recup = merma_bruta * 0.18
ahorro_efectivo = ahorro * 0.85
neto_dinamico = merma_bruta - recup - ahorro_efectivo
impulso_pib = (merma_bruta * 0.5 - ahorro * 0.7) / PIB_B * 100

print("=== VOX SIMULACION ===")
print(f"Baseline PIB {PIB_B:.3f} B€, deficit {BASELINE['deficit_pct_base']}%, deuda {BASELINE['deuda_pct_2025']}%")
print("-- detalle (no sumar totales parciales) --")
for k in ["irpf_2tramos_exento22k_menos4pp_hijo","iva_21a18_general","iva_10a8_reducido","iva_0_alimentos","iva_4_energia_sin_IIEE","soc_25a15","patrimonio","sucesiones","plusvalia_IIVTNU","itp_ajd_rebaja","exencion_irpf_pensiones","cuota_autonomos_menorSMI","bonif_SS_nuevos_indefinidos"]:
    print(f"  {k}: {COSTES[k]:.2f} B€ ({pp(COSTES[k]):.2f}% PIB)")
print(f"-- subtotales -- iva_total {COSTES['iva_total']:.2f}B, impuestos_suprimidos {COSTES['impuestos_suprimidos']:.2f}B")
print(f"Merma bruta {merma_bruta:.2f} B€ = {pp(merma_bruta):.2f}% PIB (rango 90-103 con solape IRPF/pensiones)")
print(f"Ahorro prometido {ahorro:.2f} B€")
print(f"Neto estatico {neto_estatico:.2f} B€ = +{pp(neto_estatico):.2f}pp -> deficit {BASELINE['deficit_pct_base']+pp(neto_estatico):.2f}%")
print(f"Dinamico: recupera {recup:.1f}B, ahorro efectivo {ahorro_efectivo:.1f}B, neto {neto_dinamico:.1f}B = +{pp(neto_dinamico):.2f}pp -> deficit {BASELINE['deficit_pct_base']+pp(neto_dinamico):.2f}%")
print(f"Impulso PIB corto +{impulso_pib:.2f}pp antes de financiacion (tipos/EDP lo recortan en 12-18m)")
print(f"Pension +exencion: +1200-2000 eur/año pensionista medio; SMI<22k exento IRPF; cesta -2.5-4% por IVA")
print("Riesgo: sin ahorro 100% realista (solo 12-18B año1), deficit 7%+, deuda 107-110% en 2 años.")
