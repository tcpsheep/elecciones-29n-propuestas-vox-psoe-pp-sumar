# Sostenibilidad de deuda 2026-2030 — simulación consistente y escenarios

> No predice quiebra ni fechas. Cuantifica déficit, deuda % PIB y corrección necesaria bajo hipótesis alternativas de ahorro, crecimiento e intereses. Si el déficit queda >3% persistente, la conclusión sólida es que haría falta corregir (vía menos gasto, más ingresos o más crecimiento), no un impago en un año concreto.
> Script reproducible: `04_deuda_sostenibilidad.py` (`python comparativa/04_deuda_sostenibilidad.py`).

## 1. Método stock-flujo

- `D_t = D_{t-1} + Def_t` ; `Y_t = Y_{t-1}*(1+g_t)` ; `b_t = D_t/Y_t`
- `Def_t = base_t + neto_partido_t + extra_intereses_t`
- Base 2025: Y=1.690,012B (INE CNA), b=100,7% => D=1.702,04B, déficit 2,39%.
- Sin medidas 2026-30: déficit base 2,2%, g nominal 4,5% (2,2 real +2,3 deflactor), i implícito 3,0%, SFA 0. Con i<g la deuda tiende a bajar si el déficit no se dispara.
- Neto partido permanente (escala con Y nominal):
  - VOX: bruta 142,0B (punto medio 135-149 por solape IRPF/pensiones, IRPF corregido a 85B Hacienda 13-10-2026) con 15% recuperación base menos ahorro 12/25/40B según pes/cen/opt.
  - PP: bruta 27B con 15% recuperación menos ahorro 4/7/10B.
  - PSOE: neto fijo 4,0/3,0/1,5B (gasto menos ingresos).
  - SUMAR: gasto 41,5B menos ingresos 17,0/20,0/24,8B según erosión.
- Intereses extra: spread × D_{t-1} × pass-through 20% año1 → 60% año5 (solo nueva emisión/rollover). Spreads: VOX 150/110/60 pb, PP 40/30/15, PSOE 10/0/0, SUMAR 80/55/30.
- Crecimiento: base + impulso (VOX +2,8/+1,4/0, PP +0,6/+0,4/+0,2, SUMAR +0,4/-0,5/-0,6) + drag confianza desde año2 (VOX -0,8/-0,4/0, SUMAR -0,4/-0,2/0).

## 2. Resultados 2030 (ver salida completa del script)

| Partido / escenario | Déficit 2030 | Deuda 2030 | Lectura |
|---|---|---|---|
| VOX pes (ahorro 12B, spread 150, g bajo) | 9,65% | 123,2% | Déficit casi triplica el 3%. Corrección necesaria ~6,5pp. EDP seguro, prima alta, bola intereses visible (+22B extra en 2030). |
| VOX cen (25B, 110 pb) | 8,58% | 117,2% | Aun con ahorro intermedio, déficit triplica el límite. Necesita ~5,5pp de ajuste o revertir parte de la rebaja. |
| VOX opt (40B, 60 pb) | 7,35% | 110,7% | Incluso si el ahorro 40B fuese íntegro y el crecimiento alto, el déficit sigue >7%. Insostenible sin revertir parte de la rebaja IRPF. |
| PP pes (4B, 40 pb) | 3,54% | 95,5% | Ligeramente sobre 3%. Corrección pequeña (~0,5pp) o un año más de crecimiento lo encauza. Deuda baja por denominador. |
| PP cen (7B, 30 pb) | 3,31% | 94,5% | En el borde. Senda creíble a <3% en 1-2 años evita EDP duro. |
| PP opt (10B, 15 pb) | 3,05% | 93,4% | Prácticamente estabilizado. |
| PSOE pes | 2,49% | 92,2% | Estable, deuda a la baja. |
| PSOE cen | 2,38% | 91,7% | Compatible con objetivo 1,8% en 2027-28 con PIB nominal. |
| PSOE opt | 2,29% | 91,3% | Margen conservado. |
| SUMAR pes (ing 17B, 80 pb) | 4,12% | 102,1% | Estructural >4%. Requiere focalizar crianza/herencia o aceptar presión 40%+ para corregir ~1pp. |
| SUMAR cen (20B, 55 pb) | 3,79% | 100,1% | Sobre 3% persistente. Corrección ~0,8pp. |
| SUMAR opt (24,8B, 30 pb) | 3,36% | 97,6% | Aun con recaudación alta, queda sobre 3%. Deuda contenida solo si el crecimiento no cae. |

Detalle año a año en la salida del script (g, i efectiva, def B y %, neto, extra intereses, deuda, pb* para estabilizar).

## 3. Qué es sólido y qué no

- Sólido: **sin ahorro real equivalente, las rebajas generan un déficit mucho mayor desde el año 1** (VOX +87-117B año1 según escenario, SUMAR +57-67B, PP +53-60B, PSOE +40-43B) y la deuda deja de bajar. Con déficit >3% varios años la UE abre/exige corrección y el Tesoro paga más por el spread, lo que agranda el agujero (efecto bola: VOX +8-22B extra en 2030, SUMAR +3-10B).
- No sólido: fechar quiebra o impago. España emite en euros, con vencimiento ~8 años, base inversora amplia y BCE (TPI) desde 2022. El modelo no incluye compras BCE, rating, colchón de caja ni shocks (tipos, petróleo, DANA). Para hablar de estrés grave haría falta añadir esos bloques, no basta este script.
- Sensibilidad: 1pp menos de g nominal durante 5 años suma ~4-5pp a la deuda con el mismo déficit. 100 pb de spread sostenido suman ~3-5B/año extra al final. 10B permanentes de ahorro/ingreso restan ~0,5pp al déficit y ~2-3pp a la deuda en 2030.

## 4. Cómo usarlo

- Si defiendes rebajas: muestra en qué línea PGE están los 12/25/40B y en qué año, o qué parte reviertes si no llegan.
- Si defiendes gasto permanente (crianza/herencia/vivienda 1% PIB): muestra base imponible que lo sostiene con erosión 20-45%, o focalización (means-test ahorra 8-10B).
- Para EDP: compara tu déficit 2027-28 con 3% y tu ajuste estructural anual con 0,5pp que pide la UE.

## 5. Reproducir y actualizar

```
python comparativa/04_deuda_sostenibilidad.py
```

Cambia `G0, I0, DEF_BASE, bruta, ahorro, spread_bp, impulso` arriba del script para tus hipótesis y vuelve a ejecutar. Actualiza Y2025/b con la próxima CNA del INE y el cierre IGAE.
