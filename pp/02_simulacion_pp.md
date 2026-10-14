# PP — Simulación: qué pasa si se aplican TODAS sus propuestas

> Baseline PIB 1.690B, déficit 2,39%, AEAT 294,7B. Ver `../comparativa/00_baseline_INE.md`. Enfoque: rebaja media-alta + desregulación, sin cifra SMI propia.

## 1. Merma estática

| Bloque | Hipótesis | Coste |
|---|---|---|
| Deflactar IRPF <40k (3 tramos) | ~60% declarantes, -5,3% cuota media. IRPF 129B × ~8% tramo bajo | **6,0 B** |
| Duplicar mínimos hijos | +5.100 € base familia 2 hijos × ~30% tipo × ~3,5M familias | **5,0 B** |
| IVA 0% alimentos básicos | De 4% a 0% en cesta básica (~75B base) | **3,0 B** |
| IVA energía 21→10% | Hogares+empresas (~40B base) | **4,5 B** |
| Exención IVA autónomos <85k | ~300k autónomos × ~3k cuota media | **1,0 B** |
| Patrimonio+Grandes Fortunas+Sucesiones+ITP/AJD/IVA joven | 0,6+1,4+2,0+3,5 (ITP 4%, AJD 0,4%, IVA 4% joven) | **7,5 B** |
| **TOTAL bruto** |  | **27,0 B = 1,60% PIB** |
| Ahorro burocracia (ministerios, 1×3, central compras) | Realista año 1-2 | **-7,0 B** |
| **NETO estático** |  | **20,0 B = 1,18 pp → déficit 3,57%** |
| Neto dinámico (recupera 18% ≈4,9B) |  | **16,2 B = 0,96 pp → déficit ~3,35%** |

Verificación Python: bruta 27B=1,60%, neta 20B=1,18pp, dinámica 16,2B=0,96pp.

## 2. Efectos por canal

**Hogares**
- Familia con 2 hijos y 30k: +400 € ago-dic (≈+1.000 €/año completo) + deflactación +300-500 € + IVA de alimentos/energía +400-600 €. Total **+1.500-2.000 €/año (+5-7% renta disponible)**. Mejor focalizado en clase media-baja con hijos que VOX (menos radical) y que PSOE (más IRPF que transferencias).
- Jóvenes compra: IVA 4% + AJD 0,4% + ITP 4% + aval 95-100% + Hucha 20%: entrada -40-50% (de 50k a 25-30k en piso 250k). Demanda joven +20-30%.

**Empresas / empleo**
- IS pymes simplificado + libertad amortización + no subir impuestos (garantía Empresa Familiar): inversión +4-6%, sobre todo pymes 50-250 (umbral 250=nuevos 50 elimina salto). Tarifa 0 autónomos + menos declaraciones: altas +80-120k/año, pero exención IVA <85k puede fragmentar facturación (riesgo de fraude por fraccionamiento).
- SMI sin cifra + bancos horas + control absentismo (1,2M): coste laboral contenido vs PSOE/Sumar. Paro **-0,8-1,2 pp hacia 8,8-9,0%**, ocupados +350-450k, sin el freno jornada.
- Absentismo: si baja 10-15%, PIB +0,2-0,3 pp.

**Vivienda**
- 250k/año ×4 = 1M: hoy se visan ~110-130k + se terminan ~90k. Multiplicar ×2,5 exige suelo + mano de obra + financiación que no existe en el año 1. Factible **140-170k/año** con reforma (silencio positivo, suelo público, seguridad jurídica antiokupa). Precio modera +1-2% vs +5% inercial, alquiler + oferta +8-12% en tensión por seguridad jurídica (derogar topes atrae propietarios que PSOE expulsa).
- Riesgo: derogar Ley Vivienda sin alternativa para las tensionadas genera choque con CCAA/ayuntamientos durante 12-18 meses.

**Energía / industria**
- Nuclear prorrogada + quitar impuesto generación: pool -10-15 €/MWh, factura -8-12%. Industria electrointensiva + competitividad, inversión +2-3B. Compatible con renovables (desbloqueo red) a diferencia de VOX (ruptura verde). Menos choque UE, PRTR se mantiene.

**Fiscal / deuda**
- Déficit 3,3-3,6% año 1-2: incumple 3% pero evita EDP dura si hay senda creíble a 2,5% con crecimiento +2,5-2,8% (multiplicador rebaja 0,5 + desregulación). Deuda **101-102% estable** por denominador.
- Si no se recorta burocracia (ahorro 0): déficit 4,0%, deuda al alza. Clave: presupuestos base cero light + AIReF reforzada.

## 3. Ganadores / perdedores
- Ganan: familias con hijos, jóvenes compradores, autónomos/pymes, propietarios en alquiler, industria.
- Pierden: recaudación autonómica (ITP/AJD/Patrimonio) si no se compensa vía financiación; inquilinos vulnerables sin tope (subida inicial +3-5% antes de más oferta).
- Balance: **estímulo medio, déficit medio, riesgo bajo-medio**. Es el programa menos disruptivo con VOX en rebajas pero sin su agujero, y más pro-oferta que PSOE.

## 4. Qué vigilar (INE)
- AEAT IRPF por tramos (<40k), IVA alimentos/energía, EPA autónomos/ocupados, EACL coste, visados vivienda (MIVAU + INE), pool eléctrico (REE, no INE) cruzado con IPC energía.
