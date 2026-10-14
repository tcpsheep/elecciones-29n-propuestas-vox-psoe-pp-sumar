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
- **Deuda/déficit:** déficit nuevo = 2,39% + neto/PIB. Deuda +1 año ≈ 100,7% + neto/PIB (sin contar crecimiento denominador; con PIB nominal +5% la deuda baja ~4pp a igualdad de todo lo demás — se advierte en cada ficha).
- **Empleo/precios:** elasticidades BdE (jornada -0,3-0,6% empleo, SMI +518 €×2,5M=1,29B masa), IPC por IVA (1pp IVA ≈ 0,3-0,4pp IPC).
- Cálculos reproducibles: bloques Python ejecutados en sesión (mermas, dinámicos, pensiones 189,6×2,7%=5,12B, herencia 450k×20k=9B, crianza 6,5M×2.400=15,6B).

## 3. Límites honestos
- No es modelo DSGE ni microsimulación AEAT con microdatos IRPF/IVA. Son órdenes de magnitud (±20-30%) para comparar, no previsión oficial.
- Solapes (ej. VOX IRPF 85B Hacienda + exención pensiones 14,3B) se presentan en rango 135-149B.
- Ahorros VOX 40B y gastos SUMAR 1% PIB son promesas sin desglose PGE línea a línea; se conceden al 100% y se advierte factibilidad.
- Comportamiento (fuga, deslocalización, tipos interés, UE) es la mayor incertidumbre: se da rango, no punto.
- Fondos UE (77.000M, 76% MRR) y BCE se mantienen constantes en central; ruptura verde VOX o EDP cambiarían el escenario a peor.

## 4. Qué actualizar con INE cada trimestre
- CNA (PIB), EPA (paro/ocupados), IPC (alimentos/energía/alquiler), EAES/EACL (salarios/coste hora), IGAE (déficit/deuda), AEAT (IRPF/IVA/Soc), ECV (Gini/AROPE), MIVAU visados (vivienda).
- Si la recaudación cae 135B (VOX) o sube 20B (SUMAR) o el paro no baja a 8-9% (PP/PSOE), revisar hipótesis.

## 5. Estructura carpetas
```
politica/
  README.md
  vox/01_propuestas_vox.md / 02_simulacion_vox.md / 03_vox_simulacion.py
  psoe/01_propuestas_psoe.md / 02_simulacion_psoe.md / 03_psoe_simulacion.py
  pp/01_propuestas_pp.md / 02_simulacion_pp.md / 03_pp_simulacion.py
  sumar/01_propuestas_sumar.md / 02_simulacion_sumar.md / 03_sumar_simulacion.py
  comparativa/00_baseline_INE.md / 01_comparativa_global.md / 02_metodologia_y_fuentes.md
  comparativa/03_sostenibilidad_deuda.md / 04_deuda_sostenibilidad.py
  comparativa/05_montecarlo.py / 05_montecarlo_resultados.md
```

## 6. Fuentes verificadas y anti-desinformación

### Organismos oficiales (datos baseline)
| Fuente | Dato clave | URL |
|---|---|---|
| **INE** | PIB 1.690.012 M€ (CNA2025), salario medio 29.540,26 € (EAES2024), paro 10,61%/9,93% (EPA) | https://www.ine.es/dyngs/Prensa/CNA2025.htm |
| **AEAT** | Recaudación 2024: total 294.734 M€, IRPF 129.408 M€, IVA 90.541 M€, Soc 39.096 M€; retenciones pensiones públicas 14.317 M€ (Nota3) | https://sede.agenciatributaria.gob.es |
| **Banco de España** | Deuda pública 100,7% PIB (~1.702 mm) | https://www.bde.es |
| **IGAE/Hacienda** | Déficit 2,39% (40.330 M con DANA) | https://www.igae.pap.hacienda.gob.es |
| **Ministerio de Hacienda** | Coste IRPF VOX = **85.000 M€** (61% recaudación). Ministro Arcadi España, Consejo de Ministros 13-10-2026 | Infobae/El Independiente/EFE 13-10-2026 |
| **La Moncloa** | Pensiones +2,7% general, +7% mínimas, +11,4% cónyuge (10-02-2026). SMI 17.094 € (2026) | https://www.lamoncloa.gob.es |
| **BOE** | RDL 4/2024, Ley 7/2024, RD SMI/pensiones/subsidio/vivienda | https://www.boe.es |
| **Seguridad Social** | Pensiones: 10,28 M, media 1.261,9 €/mes, gasto ~189.600 M | https://www.seg-social.es |

### Verificación y anti-desinformación
| Fuente | Dato verificado | URL |
|---|---|---|
| **Gestha** (Técnicos Hacienda) | 63% pensionistas no presenta IRPF; umbral exento retenciones 15.876 €; obligación declarar 22.000 € | https://www.gestha.es |
| **demon.code.blog** | "Desmontando a VOX: pensiones" — aclaró que la mayoría de pensionistas no notaría cambio: "la mayoría de la gente no va a notar ningún cambio". Clave para corregir el claim VOX "+1.200-2.000€/año sin IRPF" | https://demon.code.blog/2020/05/07/pensiones/ |
| **Newtral** | VOX 2019: "15% Sociedades solo PYMES"; fact-checking propuestas | https://www.newtral.es |
| **SmartVote** | VOX = "mayor fábrica de bulos" entre partidos políticos españoles | smartvote.es |
| **Institut Ostrom** (think tank *liberal*) | Cuentas VOX "tramposas": "Bajar impuestos puede ser buena política. Pero prometer que lo pagarán las subvenciones es tramposo" (oct-2026) | ostrom.cat |
| **Alex Wong** | IRPF+IVA VOX ~118B (vs 64-70B declarado); solo ~15.227 M€ recortes identificados; infografía VOX muestra IRPF 85B | alexpwong.substack.com |
| **sueldovox.es** | Calculadora oficial de VOX (programa junio 2025). Confirma SMI = 0€ ahorro IRPF (ya exento). Metodología transparente con reducciones/mínimos/deducciones actuales vs VOX | sueldovox.es |
| **Cinco Días/El País** | Propuesta IRPF VOX "hundiría la recaudación en un 50%" (~65B) (21-07-2023) | cincodias.elpais.com |
| **Herqles** | VOX estima 64B (IRPF 40+IVA 14+Soc 10); confirma Sociedades 15% general (10-10-2026) | herqles.com |

### Prensa usada (solo doble/triple fuente, marcada como tal)
- **Infobae, El Independiente, EFE** (13-10-2026) — Hacienda cifra IRPF VOX en 85B.
- **El País, El Economista, Europa Press, Infobae, La Voz de Galicia, El Mundo** — Gravamen 3% >50M Sumar (~4.200 M).
- **EFE** (29-06-2025) — VOX "rebajas masivas al Impuesto de Sociedades".
- **VOX YouTube** (02-10-2025) — "Sociedades al quince por ciento".
- PP IVA 4% vivienda joven + IRPF jóvenes: pp.es + Congreso moción + 6+ periódicos de todo el espectro.

### Programas electorales (PDF oficiales)
- VOX: `votaabascal.es/assets/pdf/Programa-VOX-2023.pdf` + `voxespana.es/wp-content/uploads/2025/10/Programa-WEB-021025.pdf`
- PSOE: `psoe.es/media-content/2023/07/PROGRAMA_ELECTORAL-GENERALES-2023.pdf`
- PP: `pp.es/wp-content/uploads/2023/07/programa_electoral_pp_23j_feijoo_2023.pdf` + `pp.es/wp-content/uploads/2025/07/POLITICA_PARTIDOPOPULAR_2025.pdf`
- Sumar: `movimientosumar.es/wp-content/uploads/2023/07/Un-Programa-para-ti.pdf` + BOCG `congreso.es/public_oficiales/L15/CONG/BOCG/B/BOCG-15-B-335-1.PDF`

**Principio**: INE/AEAT/BdE primero. Prensa solo cuando doble/triple fuente y sin sesgo ideológico evidente. Para VOX: verificación extra (right-wing media tiende a omitir/distorsionar). demon.code.blog usado solo para el claim de pensiones; todo lo demás con fuentes oficiales.
