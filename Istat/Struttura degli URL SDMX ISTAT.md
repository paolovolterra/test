# Struttura degli URL SDMX ISTAT


l’API SDMX di ISTAT (esposta su `https://esploradati.istat.it/SDMXWS/rest`) **funziona come quella di Eurostat** per quanto riguarda la personalizzazione degli URL
Puoi infatti costruire **URL SDMX completi o parziali** a seconda di quante dimensioni vuoi specificare.

- L’**ordine delle dimensioni è vincolato** a quello nel DSD (`DCSP_COEIMPEX1`) → se sbagli anche una sola posizione, ottieni `404`.
- Il **nome dei codici** deve essere esatto: ad esempio `"IMP_VAL"` vs `"VAL_IMP"` fa la differenza.
- Non puoi omettere una dimensione intermedia: se metti `A.IT...C10...` ma lasci uno spazio vuoto al centro, otterrai errore.

### 🧪 Esempi pratici (ISTAT)

il **Dataflow `139_176`** richiede **5 dimensioni obbligatorie**, in questo ordine:

`1. FREQ   2. REF_AREA   3. DATA_TYPE   4. CPA_ATECO2007_COE   5. PARTNER_COUNTRY`

#### 1. ✅ **Tutto il dataset**

```text
https://esploradati.istat.it/SDMXWS/rest/data/139_176

```

| Dimensione          | Descrizione                           | Codelist                                     |
| ------------------- | ------------------------------------- | -------------------------------------------- |
| `FREQ`              | Frequenza (es. annuale, trimestrale)  | `CL_FREQ`                                    |
| `REF_AREA`          | Area di riferimento (es. IT, regioni) | `CL_COEWEB_ITTER107`                         |
| `DATA_TYPE`         | Tipo di dato (valori, indici, ecc.)   | `CL_COEWEB_TIPO_DATO_COEIMPEX`               |
| `CPA_ATECO2007_COE` | Codice merceologico Ateco 2007        | `CL_COEWEB_ATECO_2007_MERCE`                 |
| `PARTNER_COUNTRY`   | Paese partner                         | `CL_COEWEB_GEONOM`                           |
| `TIME_PERIOD`       | Periodo temporale                     | — *(gestito con `startPeriod`, `endPeriod`)* |

|Dimensione|Codice|Significato (probabile)|
|---|---|---|
|`FREQ`|`M`|Mensile|
|`MERCE_ATECO_2007`|`0010`|Codice merceologico Ateco 2007 (es. C10)|
|`PAESE_PARTNER`|`EU`|Partner commerciale (Unione Europea)|
|`ITTER107`|`ITTOT`|Italia totale (area geografica)|
|`TIPO_DATO`|`ESAV`|Tipo di dato (es. valore export, ecc.)|

### PAESE_PARTNER

|     | values_ids | values_description         |
| --: | :--------- | :------------------------- |
|   0 | EU         | European union             |
|   1 | WORLD      | All countries of the world |
|   2 | EXT_EU     | Extra-EU                   |
### TIPO_DATO

|    | values_ids   | values_description                                                               |
|---:|:-------------|:---------------------------------------------------------------------------------|
|  0 | EV           | export - value (euro)                                                            |
|  1 | TBV          | trade balance - value (euro)                                                     |
|  2 | ISAV         | import - seasonally adjusted value - world based model (millions of euro)        |
|  3 | ESAV         | export - seasonally adjusted value - world based model (millions of euro)        |
|  4 | TBSAV        | trade balance - seasonally adjusted value  -world based model (millions of euro) |
|  5 | IV           | import - value (euro)                                                            |

## Funzionano

```

- https://esploradati.istat.it/SDMXWS/rest/data/139_176/M.ITTOT.ESAV.0010.EU?lastNObservations=5
- https://esploradati.istat.it/SDMXWS/rest/data/139_176/M.ITTOT.ESAV.0010.EU?detail=full&dimensionAtObservation=TIME_PERIOD
- https://esploradati.istat.it/SDMXWS/rest/data/139_176/M.ITTOT.ESAV.0010.EU?lastNObservations=1&dimensionAtObservation=TIME_PERIOD
- https://esploradati.istat.it/SDMXWS/rest/dataflow/IT1/94_1063/1.0/?detail=Full&references=Descendants
- https://esploradati.istat.it/SDMXWS/rest/dataflow/IT1/139_176/1.0/?detail=Full&references=Descendants
- https://esploradati.istat.it/SDMXWS/rest/datastructure/IT1/DCIS_MIGRAZIONI/
- https://esploradati.istat.it/SDMXWS/rest/data/139_176/M....
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.....
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010...
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU..ESAV
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITH.ESAV
- https://sdmx.istat.it/SDMXWS/rest/data/139_176/M.0010.EU.ITTOT.ESAV?lastNObservations=12&dimensionAtObservation=TIME_PERIOD
  
  
  
- https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_FREQ
- https://sdmx.istat.it/SDMXWS/rest/codelist/IT1/CL_ITTER107


```
