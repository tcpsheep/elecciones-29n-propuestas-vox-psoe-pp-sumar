# VOX — Simulación: qué pasa si se aplican TODAS sus propuestas a la vez

> Baseline: PIB 1.690.012 M€ (INE CNA2025), déficit 2,39% (40,33B con DANA), deuda 100,7%, AEAT 294,734B (IRPF 129,4B, IVA 90,5B, Soc 39,1B), cotizaciones 199,6B, gasto 725B, pensiones 189,6B. Ver `../comparativa/00_baseline_INE.md`. Cálculos verificados con Python (ver abajo).

## 1. Merma estática (año 1, sin comportamiento)

| Bloque | Hipótesis | Coste año 1 |
|---|---|---|
| IRPF 2 tramos + exento 22k + -4pp/hijo | **Hacienda 13-10-2026: 85B = 61% recaudación IRPF (~140B)**. VOX decía 40B (solo tramo estatal, sin autonómico). SMI=0€ ahorro, 100k=18.935€, 1M=212.333€ | **85,0 B (5,03% PIB)** |
| IVA 21→18 + 10→8 | 70% base al general (-14,3%) +25% al reducido (-20%) sobre 90,5B = 13,6B | **13,6 B** |
| IVA 0% alimentos + 4% energía + quitar IIEE | Alimentos ~2,5B, energía/IIEE ~2,0B | **4,5 B** |
| IVA total |  | **18,1 B (1,07% PIB)** |
| Sociedades 25→15% | Estático sería 15,6B; VOX dice 10B por modulación empleo/relocalización. Central **12,0 B** | **12,0 B (0,71%)** |
| Patrimonio+Sucesiones+Plusvalía+ITP/AJD | 1,4+3,2+1,5+4,5 | **10,6 B (0,63%)** |
| Exención IRPF pensiones contributivas | Solo tributan los pensionistas con pensión >15.876 €/año (umbral exento de retenciones, Gestha); obligación de declarar = 22.000 € (1 pagador). El 63% no presenta declaración (Gestha). AEAT 2024: retenciones pensiones públicas = 14.317 M€ sobre masa 159.743 M€. Solapa parcial con reforma IRPF, se suma porque VOX la lista aparte | **14,3 B (0,85%)** |
| Cuota autónomos <SMI bonif 100% | Cifra VOX (>50% RETA 11.655M) | **6,25 B (0,37%)** |
| Bonif 100%/50% SS nuevos indefinidos | ~400k empleos × ~8k cotización | **3,2 B (0,19%)** |
| **TOTAL merma bruta** |  | **~149,4 B = 8,84% PIB** |

Solape IRPF pensiones/reforma: si se corrige 100% el solape (exención 14,3B ya incluida en reforma IRPF), el total baja a ~135B (8,0% PIB). Se mantiene rango **135-149B**.

## 2. Ahorro gasto prometido
- VOX: **40,0 B/año (2,37% PIB)** eliminando ministerios (22→12), subvenciones partidos/sindicatos/patronal, ODS/Agenda 2030, observatorios, cooperación, TVs autonómicas, duplicidades, presupuestos base cero.
- Realismo: el gasto político directo (ministerios, subvenciones, cooperación, observatorios) suma ~8-12B en PGE. Llegar a 40B exige recortar transferencias a CCAA, personal o inversión, o devolver competencias (Educación/Sanidad = ~120B autonómico) con fricción constitucional y transición de años. **Año 1 factible: 12-18B; 40B solo a medio plazo y con conflicto autonómico.**
- Escenario central aquí: se concede el 100% (40B) para no infravalorar VOX, y se advierte del riesgo.

## 3. Déficit y deuda resultantes

- Neto estático con ahorro 100%: **149,4 − 40,0 = 109,4 B = +6,48 pp → déficit 2,39% → ~8,9% PIB**.
- Con solape corregido (~135B): neto ~95B → **déficit ~8,0%**.
- Dinámico (recuperación 18% merma ≈26,9B por mayor consumo/empleo, ahorro efectivo 34B tras restar -15% por menor PIB del recorte): **neto ~88,5B = +5,24 pp → déficit ~7,6%**.
- **Rango final año 1-2: déficit 7,6-8,9% PIB, deuda 108-113% y subiendo ~4 pp/año si no hay ajuste adicional.**
- Sin el ahorro completo (solo 15B realista año 1): déficit **10%+**, deuda rumbo a 110-115% en 2 años. Procedimiento de déficit excesivo UE casi seguro, prima de riesgo al alza.

Verificación:
```
VOX merma bruta 149.43B = 8.84% PIB (IRPF corregido 85B Hacienda 13-10-2026)
VOX neto tras ahorro 40B: 109.43B = 6.47pp deficit -> 8.86% PIB
Dinamico: recupera 26.9B, ahorro efectivo 34.0B, neto 88.5B = 5.24pp
Impulso PIB corto +2.76pp antes de financiación
```

## 4. Efectos por canal (España si se aplica todo)

**Hogares / poder adquisitivo (corto: muy positivo, medio: condicionado a financiar el agujero)**
- Exento 22k + 15% deja sin IRPF a ~40-50% de asalariados mileuristas/SMI (SMI 16.576 € <22k). Ahorro tipo: quien pagaba 25-30% pasa a 15%: +1.500-3.000 €/año en 25-40k; con 2 hijos (-8pp) el ahorro se duplica.
- IVA -3pp/-2pp + 0% alimentos + 4% energía: cesta -2,5-4% precio efectivo. IPC -0,8-1,2 pp año 1. Poder adquisitivo +4-6% para rentas bajas-medias año 1.
- Pensiones sin IRPF: la media aritmética por pensionista (14.317M AEAT / 9,3M = ~1.540 €/año) cae en el rango +1.200-2.000, **pero es engañosa**: el 63% no presenta declaración (Gestha) y muchos no notan ningún cambio (blog Desmontando VOX). El umbral exento de retenciones es 15.876 €/año (Gestha); el pensionista medio (pensión media del sistema 1.262 €/mes × 14 pagas = 17.668 €/año, 65+) está entre 15.876 y 22.000 € y paga **~1.100€/año IRPF** (con reducción por trabajo umbral 16.825€ neto + mínimo personal 65+ de 6.700€; sin la deducción del SMI, que solo es para asalariados — sueldovox.es metodología; Santander blog: retención 2-3% media tramo 12-18k). El ahorro real se concentra en el ~37% con pensión >22.000 € (~4.160 €/año de media). Consumo jubilados medio sube +1-3%, no +8-10%.

**Empleo / empresas**
- Soc 15% + bonif SS + cuota 0 autónomos: coste laboral -6-9% para nuevas contrataciones, margen empresarial +3-4 pp. Impulso contratación indefinida +300-500k año 1-2, paro -1,5-2 pp (hacia 8-8,5%) si no lo frena la incertidumbre fiscal/deuda.
- Riesgo: si el déficit dispara tipos de interés (+80-150 pb), el crédito a pymes encarece y anula parte del estímulo en 12-18 meses.

**Vivienda**
- Fin IVA + ITP/AJD ~0 + deducción IRPF: compra primera vivienda -15-22% coste fiscal (≈20-30k en piso 200k). Demanda +15-25%, precio al alza +5-8% si no se liberaliza suelo a la vez. Alquiler: derogar Ley Vivienda + desalojo 24h eleva oferta en tensión, pero sin límite de precios sube rentabilidad propietaria.

**Pensiones / Estado bienestar**
- Exención IRPF pensiones + capitalización sueca: los pensionistas que ya tributan (>15.876 €/año, ~37% sobre todo >22.000 €) ganan hoy, pero el sistema pierde 14,3B/año de IRPF (AEAT 2024) + cotizaciones bonificadas 9,4B. Sin subir cotizaciones, el agujero SS (+23,7B) debe cubrirse con deuda/transferencia. Capitalización a 20-30 años vista no resuelve año 1-5. Riesgo recorte futuro o deuda.

**Autonomías / energía / inmigración**
- Devolver Educación/Sanidad y suprimir duplicidades: ahorro potencial grande pero coste transición y litigiosidad 2-4 años, parálisis inversora autonómica.
- Nuclear + fin ecotasas: luz -15-25% factura (IVA 4% + sin IVPE + nuclear amortizada), industria electrointensiva + competitividad. Choque con UE (Pacto Verde, fondos) que puede congelar PRTR (77.000 M ya recibidos, 76% MRR).
- Prioridad nacional 10/5 años + excluir no contributivas: ahorro 3-6B según VOX (no verificado INE), pero coste administrativo, judicial (UE/derechos) y caída de cotizantes extranjeros (afiliación extranjera ~2,8M) que reduce ingresos SS 4-6B. Neto incierto, posiblemente negativo.

## 5. Ganadores / perdedores / riesgos
- Ganan a corto: rentas bajas-medias con hijos, pensionistas, autónomos <SMI, empresas que contraten/inviertan, compradores primera vivienda, industria energética.
- Pierden: perceptores ayudas no contributivas sin arraigo, empleados sector público superfluo/subvencionado, CCAA (financiación), contribuyentes futuros si la deuda obliga a subir impuestos o recortar sanidad/educación.
- Riesgo macro central: **estímulo privado fuerte + agujero público insostenible**. Sin credibilidad del ahorro 40B, España entra en EDP, pierde margen contra recesión y depende de BCE. Con ahorro creíble y liberalización suelo/nuclear ejecutada, el +1,4 pp de impulso PIB puede consolidar +0,6-0,8 pp estructural y paro <9%, pero a costa de mayor desigualdad inicial y tensión territorial/UE.

## 6. Qué vigilar con INE para saber si funciona
- IPC e IPC subyacente (¿baja 1 pp por IVA?), EPA paro/ocupados, EAES salarios reales, CNA consumo hogares + FBCF, IGAE déficit/deuda trimestral, AEAT recaudación por figuras (¿cae 135B o recupera 27B?).
