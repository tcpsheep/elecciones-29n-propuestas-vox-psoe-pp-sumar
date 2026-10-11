# Metodología y fuentes — cómo se ha hecho y límites

## 1. Principio pedido: INE primero, prensa mínima y verificada
- **INE verificado directo (webfetch 11/10/2026):** CNA2025 (PIB 1.690.012M, +2,6% 2025, +3,7% 2024, +2,4% 2023), EAES2024 (salario medio 29.540,26 €), EPA4T24 (ocupados 21.857.900, paro 10,61%).
  - https://www.ine.es/dyngs/Prensa/CNA2025.htm
  - https://www.ine.es/dyngs/Prensa/EAES2024.htm
  - https://www.ine.es/dyngs/Prensa/es/EPA4T24.htm
- Resto baseline: BdE deuda, IGAE/Hacienda déficit, AEAT recaudación, Seg. Social pensiones, BOE SMI — todos organismos oficiales, no prensa.
- Propuestas: **programas PDF oficiales + BOE + La Moncloa + Congreso/BOCG**. Prensa solo si doble/triple y marcada como tal (PP jóvenes/Hucha, Sumar gravamen 50M, PP deflactación cuantificada). Cada `01_propuestas_*` lista su fuente madre para re-verificar.

## 2. Método simulación
- **Estático año 1:** tipo × base (ej. IVA 3pp/21 sobre 70% de 90,5B = 9,05B). Sin comportamiento.
- **Dinámico 1-3 años:** multiplicadores AIReF/BdE (impuestos 0,4-0,6, gasto 0,6-1,0), recuperación Laffer 15-20% merma, erosión base capital 30-40%, retorno gasto social 25%.
- **Deuda/déficit:** déficit nuevo = 2,39% + neto/PIB. Deuda +1 año ≈ 100,7% + neto/PIB (sin contar crecimiento denominador; con PIB nominal +5% la deuda baja ~4pp todo else equal — se advierte en cada ficha).
- **Empleo/precios:** elasticidades BdE (jornada -0,3-0,6% empleo, SMI +518 €×2,5M=1,29B masa), IPC por IVA (1pp IVA ≈ 0,3-0,4pp IPC).
- Cálculos reproducibles: bloques Python ejecutados en sesión (mermas, dinámicos, pensiones 189,6×2,7%=5,12B, herencia 450k×20k=9B, crianza 6,5M×2.400=15,6B).

## 3. Límites honestos
- No es modelo DSGE ni microsimulación AEAT con microdatos IRPF/IVA. Son órdenes de magnitud (±20-30%) para comparar, no previsión oficial.
- Solapes (ej. VOX IRPF + exención pensiones) se presentan en rango 90-103B.
- Ahorros VOX 40B y gastos SUMAR 1% PIB son promesas sin desglose PGE línea a línea; se conceden al 100% y se advierte factibilidad.
- Comportamiento (fuga, deslocalización, tipos interés, UE) es la mayor incertidumbre: se da rango, no punto.
- Fondos UE (77.000M, 76% MRR) y BCE se mantienen constantes en central; ruptura verde VOX o EDP cambiarían el escenario a peor.

## 4. Qué actualizar con INE cada trimestre
- CNA (PIB), EPA (paro/ocupados), IPC (alimentos/energía/alquiler), EAES/EACL (salarios/coste hora), IGAE (déficit/deuda), AEAT (IRPF/IVA/Soc), ECV (Gini/arope), MIVAU visados (vivienda).
- Si la recaudación cae 90B (VOX) o sube 20B (SUMAR) o el paro no baja a 8-9% (PP/PSOE), revisar hipótesis.

## 5. Estructura carpetas
```
politica/
  README.md
  vox/01_propuestas_vox.md / 02_simulacion_vox.md
  psoe/01_propuestas_psoe.md / 02_simulacion_psoe.md
  pp/01_propuestas_pp.md / 02_simulacion_pp.md
  sumar/01_propuestas_sumar.md / 02_simulacion_sumar.md
  comparativa/00_baseline_INE.md / 01_comparativa_global.md / 02_metodologia_y_fuentes.md
```
