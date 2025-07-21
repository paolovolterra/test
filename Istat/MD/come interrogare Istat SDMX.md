---
title: come interrogare Istat SDMX
authors:
  - Paolo Volterra
url:
tags:
  - io
  - Istat
  - SDMX
  - guida
  - howto
  - importanti
  - top
created: 2025-07-15 21:29
---
## 1. trova il dataset che ti interessa 

http://sdmx.istat.it/SDMXWS/rest/dataflow


## 2. cerca il blocco XML che ti interessa

 un abstract [qui](https://github.com/ondata/guida-api-istat/blob/master/processing/dataflow.csv) 

contiene:
- il nome del dataset
- il codice della struttura dati associata (DataStructureDefinition); in questo caso **DCIS_POPRES1** necessario per conoscere **le dimensioni del dataset**
- la versione (in questo caso **1.5**)

```
<structure:Dataflow id="22_289" urn="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IT1:22_289(1.5)" agencyID="IT1" version="1.5" isFinal="false">
<common:Name xml:lang="it">Popolazione residente al 1° gennaio</common:Name>
<common:Name xml:lang="en">Resident population on 1st January</common:Name>
<structure:Structure>
<Ref id="DCIS_POPRES1" version="1.5" agencyID="IT1" package="datastructure" class="DataStructure"/>
</structure:Structure>
</structure:Dataflow>
```

 - **22_289** versione 1.5 (Popolazione residente al 1° gennaio), struttura  **DCIS_POPRES1**
 - **139_176** versione 1.0 (Importazioni ed esportazioni per paese e merce Ateco 2007), **DCSP_COEIMPEX1**

## 3. Recupera la struttura dati

necessario per conoscere le dimensioni
- http://sdmx.istat.it/SDMXWS/rest/datastructure/IT1/DCIS_POPRES1/1.5  (FREQ CL_FREQ,  ETA CL_ETA1, ...)
-  http://sdmx.istat.it/SDMXWS/rest/datastructure/IT1/DCSP_COEIMPEX1/1.0

## 4.   analizza le codelist (valori validi)
sono però valori teorici. Per sapere quelli effettivamente utilizzati meglio interrogare così https://sdmx.istat.it/SDMXWS/rest/data/139_176/all?detail=serieskeysonly

## 5. costruisci il link filtrato

---
## ESEMPI

### Popolazione residente al 1° gennaio

- **22_289(1.5)** https://sdmx.istat.it/SDMXWS/rest/data/22_289 oppure `curl -kL "http://sdmx.istat.it/SDMXWS/rest/data/22_289" >./22_289.xml` (oltre 3Gbyte !)
- **DCIS_POPRES1 (1.5)** http://sdmx.istat.it/SDMXWS/rest/datastructure/IT1/DCIS_POPRES1/1.5 

| ID dimensione | Descrizione                             | Codelist associata   | Versione codelist |                                                                   |
| ------------- | --------------------------------------- | -------------------- | ----------------- | ----------------------------------------------------------------- |
| `FREQ`        | Frequenza (annuale, trimestrale…)       | `CL_FREQ`            | `1.0`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_FREQ/1.0        |
| `ETA`         | Età                                     | `CL_ETA1`            | `2.5`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_ETA1/2.5        |
| `ITTER107`    | Territorio (regioni, province…)         | `CL_ITTER107`        | `5.4`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_ITTER107/5.4    |
| `SESSO`       | Sesso                                   | `CL_SEXISTAT1`       | `2.0`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_SEXISTAT1/2.0   |
| `STACIVX`     | Stato civile                            | `CL_STATCIV2`        | `4.3`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_STATCIV2/4.3    |
| `TIPO_INDDEM` | Tipo indicatore demografico             | `CL_TIPO_DATO15`     | `4.0`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_TIPO_DATO15/4.0 |
| `TIME_PERIOD` | Periodo temporale (anno di rilevazione) | _(nessuna codelist)_ | _(formato SDMX)_  |                                                                   |

### Incidenti, morti e feriti - comuni 
- dataset **41_983** https://sdmx.istat.it/SDMXWS/rest/data/41_983 oppure `curl -kL "http://sdmx.istat.it/SDMXWS/rest/data/41_983" >./41_983.xml`
- struttura **DCIS_INCIDMORFER_COM**  versione 1.1 http://sdmx.istat.it/SDMXWS/rest/datastructure/IT1/DCIS_INCIDMORFER_COM/1.1 


### Importazioni ed esportazioni per paese e merce Ateco 2007
- dataflow **139_176** https://sdmx.istat.it/SDMXWS/rest/data/139_176  oppure `curl -kL "http://sdmx.istat.it/SDMXWS/rest/data/139_176" >./139_176.xml` (1.5Mbyte)
- struttura **DCSP_COEIMPEX1** versione 1.5 http://sdmx.istat.it/SDMXWS/rest/datastructure/IT1/DCSP_COEIMPEX1/1.5 

| ID dimensione      | Descrizione                                                 | Codelist associata           | Versione codelist |                                                                        |                                                        |
| ------------------ | ----------------------------------------------------------- | ---------------------------- | ----------------- | ---------------------------------------------------------------------- | ------------------------------------------------------ |
| `FREQ`             | Frequenza temporale (es. annuale, trimestrale)              | `CL_FREQ`                    | `1.0`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_FREQ/1.0             | M,Q                                                    |
| `MERCE_ATECO_2007` | Prodotto (classificazione ATECO 2007)                       | `CL_ATECO_2007_MERCE`        | `1.0`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_ATECO_2007_MERCE/1.0 | solo 0010                                              |
| `PAESE_PARTNER`    | Paese partner commerciale (es. USA, DE, CN…)                | `CL_ISO`                     | `1.5`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_ISO/1.5              | EU, EXT_EU, WORLD                                      |
| `ITTER107`         | Territorio italiano (es. IT, ITF4, ITC1…)                   | `CL_ITTER107`                | `1.2`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_ITTER107/1.2         | ITTOT,ITC,ITC1,ITC2,ITC3,ITC4, ITD,ITD1,ITD2,ITD3,ITD4 |
| `TIPO_DATO`        | Tipologia dato (es. valore economico, quantità, variazioni) | `CL_TIPO_DATO12`             | `1.1`             | https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_TIPO_DATO12/1.1      | ESAV, EV,ISAV,IV,TBSAV,TBV                             |
| `TIME_PERIOD`      | Periodo di osservazione (es. `2023-Q1`, `2022`)             | _(no codelist, è temporale)_ | _(ISO 8601)_      |                                                                        |                                                        |
- i mensili sono per nazione=ITTOT,  MERCE_ATECO_2007 =0010 e  PAESE_PARTNER=EU/EXT_EU/WORLD
- i trimestrali sono per provincia, MERCE_ATECO_2007 =0010  e PAESE_PARTNER=WORLD

link validi
- https://sdmx.istat.it/SDMXWS/rest/data/139_176
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/all?detail=serieskeysonly

- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010...EV
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.WORLD..EV
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/Q.0010.WORLD.ITE2.EV
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/Q.0010.WORLD.ITE2+ITG2.EV
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITTOT.ESAV?startPeriod=2022-01&endPeriod=2024-12
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITTOT.ESAV?startPeriod=2020-01
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITTOT.ESAV?lastNObservations=12
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITTOT.ESAV?startPeriod=2024-05&endPeriod=2024-05


curl -kL -H "Accept: text/csv" "https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITTOT.ESAV?lastNObservations=24" -o export_C10_EU.csv


---
## Valore aggiunto per branca di attività 

### CONTI E AGGREGATI ECONOMICI NAZIONALI TRIMESTRALI

- DATAWAREHOUSE,1.0/UP_ACC_TRIMES/IT1,163_1226_DF_DCCN_QNA1_1,1.0
- **163_1226**
- trimestrale
- struttura
	- https://esploradati.istat.it/SDMXWS/rest/dataflow/IT1/163_1226_DF_DCCN_QNA1_1/1.0/?detail=Full&references=Descendants
- Query del dato 
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,163_1226_DF_DCCN_QNA1_1,1.0
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,163_1226_DF_DCCN_QNA1_1,1.0/Q........./
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,163_1226_DF_DCCN_QNA1_1,1.0/Q.IT.B1G_B_W2_S1.C.Z.Z.L_2020.N.B.2024M12/
- col browser
	- https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TRIMES/IT1,163_1226_DF_DCCN_QNA1_1,1.0)
- `curl -kL "https://esploradati.istat.it/SDMXWS/rest/data/IT1,163_1226_DF_DCCN_QNA1_1,1.0" >./163_1226_DF_DCCN_QNA1_1.xml`
- 10 dimensioni (dentro l'SDMX )
	1.   1   FREQ: Q
	2.   1   REF_AREA: IT
	3.   1   DATA_TYPE_AGGR: B1G_B_W2_S1
	4. 24   BRKDW_INDUSTRY_NACE_REV2:  \_T, A, B, BTE, BTF, C, C10T12, C13T18, C19T21, C22T25, C26T28, C29_30, C31T33, D_E, F, GTI, GTU, J, K, L, M_N, NMKT, OTQ, RTU
	5.        NONFIN_ASSETS: Z
	6.        EXPEND_PURPOSE_COICOPCOFOG: Z
	7.   3   VALUATION: L_2020, V, Y
	8.   3   ADJUSTMENT:	N, W, Y
	9.   1   PRICE: B
	10. 4   EDITION: 2024M10, 2024M12, 2025M3, 2025M5


```
https://esploradati.istat.it/   SDMXWS/rest/data/                                                    IT1,163_1226_DF_DCCN_QNA1_1,1.0/Q.IT.B1G_B_W2_S1.C.Z.Z.L_2020.N.B.2024M12/
https://esploradati.istat.it/   databrowser/#/it/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TRIMES/  IT1,163_1226_DF_DCCN_QNA1_1,1.0
```


### CONTI E AGGREGATI ECONOMICI TERRITORIALI

- DATAWAREHOUSE,1.0/UP_ACC_TERRIT/IT1,93_1227_DF_DCCN_TNA1_1,1.0
- **93_1227**
- annuale
- struttura
	- https://esploradati.istat.it/SDMXWS/rest/dataflow/IT1/93_1227_DF_DCCN_TNA1_1/1.0/?detail=Full&references=Descendants
- Query del dato
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_1,1.0/
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_1,1.0/A.ITC12.B1G_B_W2_S1.C.Z.Z.V.N.B.2025M6
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_1,1.0/A.ITC12.B1G_B_W2_S1.C.Z.Z.V.N.B.2025M6?startPeriod=2014&endPeriod=2014
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_1,1.0/A.ITC12+ITC11.B1G_B_W2_S1.C.Z.Z.V.N.B.2025M6?startPeriod=2014&endPeriod=2014
	- https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_1,1.0/A........./ALL/?detail=full&startPeriod=2014-01-01&endPeriod=2023-12-31&dimensionAtObservation=TIME_PERIOD
- col browser
	- https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TERRIT/IT1,93_1227_DF_DCCN_TNA1_1,1.0
- `curl -kl "https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_1,1.0/" > butta.xml`
- dimensioni
	1.  FREQ: "A"
	2.  REF_AREA: "IT"
	3.  DATA_TYPE_AGGR: "B1G_B_W2_S1"
	4.  BRKDW_INDUSTRY_NACE_REV2: "\_T"
	5.  NONFIN_ASSETS: "Z"
	6.  EXPEND_PURPOSE_COICOPCOFOG: "Z"
	7.  VALUATION: "L_2020"
	8.  ADJUSTMENT: "N"
	9.  PRICE: "B"
	10. EDITION: "2025M6"

---
## Valori pro capite

https://esploradati.istat.it/SDMXWS/rest/data/IT1,93_1227_DF_DCCN_TNA1_6,1.0/A.ITC12........?startPeriod=2014&endPeriod=2014


- dimensioni
	1. <generic:Value id="FREQ" value="A"/>
	2. <generic:Value id="REF_AREA" value="ITC12"/>
	3. <generic:Value id="DATA_TYPE_AGGR" value="B1G_B_W2_S1_R_POP"/>
	4. <generic:Value id="BRKDW_INDUSTRY_NACE_REV2" value="Z"/>
	5. <generic:Value id="NONFIN_ASSETS" value="Z"/>
	6. <generic:Value id="EXPEND_PURPOSE_COICOPCOFOG" value="Z"/>
	7. <generic:Value id="VALUATION" value="V"/>
	8. <generic:Value id="ADJUSTMENT" value="N"/>
	9. <generic:Value id="PRICE" value="Z"/>
	10. <generic:Value id="EDITION" value="2025M6"/>