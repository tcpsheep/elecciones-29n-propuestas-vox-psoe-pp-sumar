# Simulacion Monte Carlo (10.000 iteraciones)

Baseline 2025: PIB 1.690 B (INE CNA), deuda 100,7% (Banco de Espana), deficit 2,2% estructural (IGAE), paro 9,93% (INE EPA Q4-2025).

Modelo stock-flujo con incertidumbre triangular en merma, ahorro, multiplicadores, spread y crecimiento. Semilla 42 para reproducibilidad. Solo libreria estandar.

## Parametros por partido

### VOX
**Propuestas**: IRPF 85B (Hacienda 13-10-2026) 2 tramos 15/25% exento 22k | IVA 21->18 10->8 0% alimentos 4% energia | Soc 25->15% | Suprimir Patrimonio/Sucesiones/Plusvalia | Exencion IRPF pensiones (14,3B AEAT) | Cuota autonomos 0 <SMI | Bonif SS nuevos indefinidos | Ahorro 40B prometido

| Parametro | Min | Moda | Max | Unidad |
|---|---|---|---|---|
| Merma bruta | 125 | 149 | 175 | B |
| Ahorro | 8 | 22 | 40 | B |
| Recuperacion | 10 | 18 | 25 | % |
| Eficacia ahorro | 65 | 85 | 95 | % |
| Impulso PIB | 0.5 | 2.8 | 4.0 | pp |
| Spread | 40 | 110 | 220 | pb |
| Drag confianza | -2.0 | -0.4 | 0.0 | pp |

### PP
**Propuestas**: Deflactar IRPF <40k | Duplicar minimos hijos | IVA 0% basicos vivienda joven | Bajada tipos autonomos | 1M viviendas

| Parametro | Min | Moda | Max | Unidad |
|---|---|---|---|---|
| Merma bruta | 22 | 27 | 35 | B |
| Ahorro | 2 | 7 | 12 | B |
| Recuperacion | 10 | 18 | 25 | % |
| Eficacia ahorro | 75 | 90 | 100 | % |
| Impulso PIB | 0.2 | 0.7 | 1.3 | pp |
| Spread | 10 | 30 | 70 | pb |
| Drag confianza | -0.5 | 0.0 | 0.3 | pp |

### PSOE
**Propuestas**: SMI 1.221x14 | Pensiones +2,7% (+miminas +7-11,4%) | Jornada 37,5h | PRTR 77B | MEI 0,9%

| Parametro | Min | Moda | Max | Unidad |
|---|---|---|---|---|
| Neto fiscal | 1.0 | 3.0 | 6.0 | B |
| Impulso PIB | -0.2 | 0.5 | 1.2 | pp |
| Spread | 0 | 5 | 25 | pb |
| Drag confianza | -0.3 | 0.0 | 0.0 | pp |

### SUMAR
**Propuestas**: Crianza 200/mes | Herencia 20k a los 23 | IRPF 52% desde 300k | Gravamen 3% >50M | Vivienda 1% PIB | 30h semana

| Parametro | Min | Moda | Max | Unidad |
|---|---|---|---|---|
| Gasto | 32 | 41.5 | 55 | B |
| Ingresos | 12 | 20 | 30 | B |
| Recuperacion | 0 | 10 | 25 | % |
| Impulso PIB | -1.5 | -0.2 | 0.8 | pp |
| Spread | 15 | 55 | 120 | pb |
| Drag confianza | -1.0 | -0.2 | 0.0 | pp |

## Resultados por partido

### BASE (sin medidas de partido)

| Ano | Deficit % (mediana) [P5-P95] | Deuda % [P5-P95] | PIB acum | Paro % | P(EDP>3%) | P(Deuda>110%) | P(Def>5%) |
|---|---|---|---|---|---|---|---|
| 2026 | 2.2 (2.2) [2.2-2.2] | 98.6 [97.9-99.2] | 4.5% | 9.9 | 0% | 0% | 0% |
| 2027 | 2.2 (2.2) [2.2-2.2] | 96.5 [95.6-97.5] | 9.2% | 9.9 | 0% | 0% | 0% |
| 2028 | 2.2 (2.2) [2.2-2.2] | 94.6 [93.4-95.7] | 14.1% | 9.9 | 0% | 0% | 0% |
| 2029 | 2.2 (2.2) [2.2-2.2] | 92.7 [91.5-93.9] | 19.3% | 9.9 | 0% | 0% | 0% |

### PSOE
**Propuestas**: SMI 1.221x14 | Pensiones +2,7% (+miminas +7-11,4%) | Jornada 37,5h | PRTR 77B | MEI 0,9%

| Ano | Deficit % (mediana) [P5-P95] | Deuda % [P5-P95] | PIB acum | Paro % | P(EDP>3%) | P(Deuda>110%) | P(Def>5%) |
|---|---|---|---|---|---|---|---|
| 2026 | 2.4 (2.4) [2.3-2.5] | 98.3 [97.8-98.9] | 5.0% | 9.7 | 0% | 0% | 0% |
| 2027 | 2.4 (2.4) [2.3-2.5] | 96.3 [95.5-97.2] | 9.9% | 9.6 | 0% | 0% | 0% |
| 2028 | 2.4 (2.4) [2.3-2.5] | 94.5 [93.5-95.6] | 14.9% | 9.6 | 0% | 0% | 0% |
| 2029 | 2.4 (2.4) [2.3-2.5] | 92.9 [91.8-94.1] | 20.1% | 9.6 | 0% | 0% | 0% |

### PP
**Propuestas**: Deflactar IRPF <40k | Duplicar minimos hijos | IVA 0% basicos vivienda joven | Bajada tipos autonomos | 1M viviendas

| Ano | Deficit % (mediana) [P5-P95] | Deuda % [P5-P95] | PIB acum | Paro % | P(EDP>3%) | P(Deuda>110%) | P(Def>5%) |
|---|---|---|---|---|---|---|---|
| 2026 | 3.3 (3.3) [3.0-3.5] | 99.0 [98.4-99.6] | 5.2% | 9.6 | 97% | 0% | 0% |
| 2027 | 3.3 (3.3) [3.1-3.5] | 97.6 [96.8-98.6] | 10.4% | 9.4 | 98% | 0% | 0% |
| 2028 | 3.3 (3.3) [3.1-3.5] | 96.6 [95.4-97.8] | 15.5% | 9.3 | 99% | 0% | 0% |
| 2029 | 3.3 (3.3) [3.1-3.6] | 95.8 [94.3-97.2] | 20.7% | 9.3 | 99% | 0% | 0% |

### SUMAR
**Propuestas**: Crianza 200/mes | Herencia 20k a los 23 | IRPF 52% desde 300k | Gravamen 3% >50M | Vivienda 1% PIB | 30h semana

| Ano | Deficit % (mediana) [P5-P95] | Deuda % [P5-P95] | PIB acum | Paro % | P(EDP>3%) | P(Deuda>110%) | P(Def>5%) |
|---|---|---|---|---|---|---|---|
| 2026 | 3.3 (3.3) [2.9-3.8] | 100.0 [99.2-101.0] | 4.2% | 10.1 | 89% | 0% | 0% |
| 2027 | 3.4 (3.4) [3.0-3.8] | 99.7 [98.3-101.3] | 8.2% | 10.4 | 92% | 0% | 0% |
| 2028 | 3.5 (3.4) [3.0-3.9] | 99.4 [97.4-101.5] | 12.4% | 10.7 | 95% | 0% | 0% |
| 2029 | 3.5 (3.5) [3.1-4.0] | 99.0 [96.6-101.5] | 17.0% | 10.9 | 97% | 0% | 0% |

### VOX
**Propuestas**: IRPF 85B (Hacienda 13-10-2026) 2 tramos 15/25% exento 22k | IVA 21->18 10->8 0% alimentos 4% energia | Soc 25->15% | Suprimir Patrimonio/Sucesiones/Plusvalia | Exencion IRPF pensiones (14,3B AEAT) | Cuota autonomos 0 <SMI | Bonif SS nuevos indefinidos | Ahorro 40B prometido

| Ano | Deficit % (mediana) [P5-P95] | Deuda % [P5-P95] | PIB acum | Paro % | P(EDP>3%) | P(Deuda>110%) | P(Def>5%) |
|---|---|---|---|---|---|---|---|
| 2026 | 8.6 (8.6) [7.7-9.5] | 102.8 [101.5-104.2] | 6.9% | 8.7 | 100% | 0% | 100% |
| 2027 | 8.7 (8.7) [7.8-9.6] | 106.3 [103.8-108.9] | 12.6% | 8.3 | 100% | 1% | 100% |
| 2028 | 8.9 (8.9) [7.9-9.7] | 110.4 [106.9-114.0] | 17.9% | 8.2 | 100% | 57% | 100% |
| 2029 | 9.0 (9.0) [8.1-9.9] | 115.3 [110.8-119.8] | 22.5% | 8.5 | 100% | 98% | 100% |

## Resumen comparativo (Ano 4 - 2029)

| Partido | Deficit medio | P(EDP>3%) | P(Def>5%) | Deuda media | P(>110%) | PIB acum | Paro medio |
|---|---|---|---|---|---|---|---|
| BASE | 2.2% | 0% | 0% | 92.7% | 0% | 19.3% | 9.9% |
| PSOE | 2.4% | 0% | 0% | 92.9% | 0% | 20.1% | 9.6% |
| PP | 3.3% | 99% | 0% | 95.8% | 0% | 20.7% | 9.3% |
| SUMAR | 3.5% | 97% | 0% | 99.0% | 0% | 17.0% | 10.9% |
| VOX | 9.0% | 100% | 100% | 115.3% | 98% | 22.5% | 8.5% |

## Metodologia

- **Modelo**: stock-flujo consistente. D(t)=D(t-1)+Def(t), Y(t)=Y(t-1)*(1+g(t)), b(t)=D(t)/Y(t).
- **Def(t)** = deficit base (2,2% PIB) + impacto fiscal neto del partido + intereses extra por prima de riesgo.
- **Impacto neto**: merma*(1-recuperacion) - ahorro*eficacia (VOX/PP); gasto neto (PSOE); gasto*(1-recup) - ingresos (SUMAR).
- **Passthrough del spread**: gradual (20% ano 1, +10pp/ano) sobre el stock de deuda.
- **Impulso PIB**: decae 30%/ano desde ano 1.
- **Drag confianza**: activo desde ano 2.
- **Paro**: ley de Okun simplificada (delta_paro = -0,5*(g_real - g_potencial)).
- **Distribuciones**: triangulares (min, moda, max) calibradas con datos del repo y fuentes oficiales.
- **Ruido**: gauss(0, 0,3%) anadido al crecimiento para variabilidad no explicada.
- **Fuentes**: INE (PIB CNA, EPA, EAES), Banco de Espana (deuda), IGAE (deficit), AEAT (recaudacion IRPF/IVA/pensiones), La Moncloa/BOE (SMI, pensiones).
- **Limitaciones**: parametros muestreados independientemente (sin correlacion entre merma y spread); el impulso fiscal no distingue oferta/demanda; el paro usa Okun simplificado.
