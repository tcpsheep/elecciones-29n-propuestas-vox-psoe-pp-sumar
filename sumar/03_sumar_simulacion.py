"""
Simulacion SUMAR - maxima redistribucion, maximo Estado
Teorico +26.803B +4.2B gravamen 50M vs comportamental -35% erosion
Gasto: vivienda 1% PIB + herencia 20k + crianza 200/mes
Uso: python sumar_simulacion.py
"""
PIB_B = 1690.012
BASE_DEF = 2.39
def pp(x): return x / PIB_B * 100

ING_TEO = {"sociedades": 13.0, "irpf_ahorro_herencias": 2.5, "iva_privada": 2.695, "ambiental_lujo": 1.5, "resto_paquete": 7.108, "gravamen_50M": 4.2}
teo_total = sum(ING_TEO.values())  # 31.003
# Erosion por bloque
ING_NETO = {"sociedades": 13.0*0.65, "irpf_ahorro_herencias": 2.5*0.8, "iva_privada": 2.695*0.85, "ambiental_lujo": 1.5*0.8, "resto_paquete": 7.108*0.7, "gravamen_50M": 4.2*0.7}
neto_ing = sum(ING_NETO.values())

GASTO = {"vivienda_1pct_PIB": PIB_B*0.01, "herencia_20k_450k": 450000*20000/1e9, "crianza_200mes_6_5M": 6.5*2.4, "pensiones_minimas_extra": 1.75, "banco_publico_provision": 1.0}
gasto_total_sin_banco = GASTO["vivienda_1pct_PIB"] + GASTO["herencia_20k_450k"] + GASTO["crianza_200mes_6_5M"]
gasto_central = 41.5  # informe (vivienda+herencia+crianza)
neto_estatico = gasto_central - teo_total
neto_real = gasto_central - neto_ing
retorno_gasto = gasto_central * 0.25
neto_din = (gasto_central - retorno_gasto) - neto_ing

print("=== SUMAR SIMULACION ===")
print(f"Ing teorico {teo_total:.2f}B = {pp(teo_total):.2f}% PIB")
for k, v in ING_TEO.items(): print(f"  {k} teorico {v:.3f}B -> neto {ING_NETO[k]:.3f}B")
print(f"Ing neto comportamental {neto_ing:.2f}B = {pp(neto_ing):.2f}% PIB")
print(f"Gasto: vivienda {GASTO['vivienda_1pct_PIB']:.2f}B + herencia {GASTO['herencia_20k_450k']:.2f}B + crianza {GASTO['crianza_200mes_6_5M']:.2f}B = {gasto_total_sin_banco:.2f}B (central informe {gasto_central:.2f}B)")
print(f"Neto estatico {neto_estatico:.2f}B = +{pp(neto_estatico):.2f}pp -> deficit {BASE_DEF+pp(neto_estatico):.2f}%")
print(f"Neto real {neto_real:.2f}B = +{pp(neto_real):.2f}pp -> deficit {BASE_DEF+pp(neto_real):.2f}%")
print(f"Dinamico (retorno 25% gasto) neto {neto_din:.2f}B = +{pp(neto_din):.2f}pp, pero PIB -0.5-1pp por inversion -8%")
print("Gravamen 50M cubre 17% del nuevo gasto social (4.2 vs 24.6 herencia+crianza). Sin means-test, estructural 4%+.")
print("Desigualdad: Gini -2-3pp, pobreza infantil -6-9pp. Empleo pymes -0.5-1pp paro hacia 10.5-11%.")
