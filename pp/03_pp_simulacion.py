"""
Simulacion PP - rebaja media + desregulacion
Baseline INE + AEAT
Uso: python pp_simulacion.py
"""
PIB_B = 1690.012
BASE_DEF = 2.39
def pp(x): return x / PIB_B * 100

COSTES = {
    "deflactar_IRPF_menor40k": 6.0,
    "duplicar_minimos_hijos": 5.0,  # +5100 base*30%*3.5M fam
    "iva_0_alimentos": 3.0,
    "iva_energia_21a10": 4.5,
    "exencion_iva_autonomos_85k": 1.0,
    "grandes_fortunas": 0.6, "patrimonio_CCAA": 1.4, "sucesiones_rebaja": 2.0, "itp_ajd_iva_joven": 3.5,
}
bruta = sum(COSTES.values())
ahorro = 7.0
neto = bruta - ahorro
recup = bruta * 0.18
neto_din = bruta - recup - ahorro * 0.85

print("=== PP SIMULACION ===")
for k, v in COSTES.items(): print(f"  {k}: {v:.2f}B ({pp(v):.2f}% PIB)")
print(f"Bruta {bruta:.2f}B = {pp(bruta):.2f}% PIB")
print(f"Ahorro burocracia {ahorro:.2f}B -> Neto estatico {neto:.2f}B = +{pp(neto):.2f}pp -> deficit {BASE_DEF+pp(neto):.2f}%")
print(f"Neto dinamico {neto_din:.2f}B = +{pp(neto_din):.2f}pp -> deficit {BASE_DEF+pp(neto_din):.2f}%")
print("Hogar 30k 2 hijos: +400 ago-dic (~1000 año) +deflact 400 +IVA 500 = +1500-2000/año")
print("Vivienda joven: IVA 4%+AJD 0.4%+ITP 4%+aval 95% = entrada -40-50%; oferta 140-170k real vs 250k promesa")
print("Empleo: +350-450k, paro a 8.8-9.0%; nuclear+sin imp generacion = pool -10-15 eur/MWh")
