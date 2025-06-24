# Costruiamo il link



![](https://ec.europa.eu/eurostat/o/estat-theme-ecl/images/header/estat-logo-horizontal.svg?browserId=other&minifierType=js&languageId=en_GB&t=1749220086000)

_capire le dimensioni che compongono i dataset di Eurostat_


Eurostat pubblica diversi [dataset paralleli o derivati](https://ec.europa.eu/eurostat/en/web/main/search/-/search/dataset?_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_pageNumber=1&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_pageSize=11&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_text=nama_10_gdp&p_auth=tvLAcqGs&text=) che riguardano il PIL o aggregati simili. Ecco una panoramica organizzata per **tematica**:
### Contabilità nazionale – PIL e componenti

| Codice dataset    | Frequenza   | Descrizione sintetica                                 | Note                                 |
| ----------------- | ----------- | ----------------------------------------------------- | ------------------------------------ |
| **namq_10_gdp**   | Trimestrale | Contabilità nazionale trimestrale - PIL               | Principale per analisi congiunturale |
| **nama_10_gdp**   | Annuale     | Contabilità nazionale annuale - PIL                   | Principale per analisi strutturale   |
| **nama_10_pc**    | Annuale     | PIL pro capite                                        | In euro, SPA, PPS                    |
| **nama_10r_3gdp** | Annuale     | PIL regionale a prezzi di mercato                     | Disponibile per NUTS2                |
| **nama_10r_2gdp** | Annuale     | PIL regionale per abitante                            | Complemento di `nama_10r_3gdp`       |
| **namq_10_sa**    | Trimestrale | PIL e componenti, destagionalizzati                   | Include consumi, investimenti, ecc.  |
| **nama_10_f**     | Annuale     | PIL per branca di attività                            | Settori ATECO/NACE                   |
| **nama_10_an6**   | Annuale     | PIL e occupazione per attività                        | Più dettagliato                      |
| **nama_10_c**     | Annuale     | PIL per tipo di spesa (final consumption, GFCF, ecc.) | Domanda aggregata                    |

### Indicatori derivati e confronti internazionali

| Codice dataset      | Frequenza | Descrizione                          | Note                                  |
| ------------------- | --------- | ------------------------------------ | ------------------------------------- |
| **tec00115**        | Annuale   | PIL reale per abitante               | Dataset semplificato                  |
| **nama_10_lp_ulc**  | Annuale   | Produttività e costo del lavoro      | Include PIL per ora lavorata          |
| **nama_10_exi**     | Annuale   | PIL e saldo estero                   | Esportazioni, importazioni, ecc.      |
| **nama_10_gdpdefl** | Annuale   | Deflatore del PIL                    | Utile per passare da nominale a reale |
| **sdg_08_10**       | Annuale   | SDG: crescita PIL reale per abitante | Sustainable Development Goal 8        |

### Serie internazionali (PPS, SPA, Eurostat-OECD)

|Codice dataset|Frequenza|Descrizione|
|---|---|---|
|**prc_ppp_ind**|Annuale|PIL in standard di potere d’acquisto (PPS)|
|**nama_aux_gph**|Annuale|Gross domestic product per hour worked (OCSE-Eurostat)|


Puoi cercarli via [Eurostat Data Browser](https://ec.europa.eu/eurostat/databrowser/)
    
## [namq_10_gdp](https://ec.europa.eu/eurostat/en/web/main/search/-/search/dataset?text=namq_10_gdp)

- Trimestrale
- Contabilità nazionale trimestrale - PIL
- Principale per analisi 

![](Github/Eurostat/media/Pasted%20image%2020250622114356.png)

Usiamo come esempio il dataset `nama_10_gdp`  "**Gross domestic product (GDP) and main components (output, expenditure and income)**"  
voglio sapere quali sono le dimensioni di questo dataset  
purtroppo la query qui appresso scaricherà tutto il dataset

```python
# tutto il dataset
url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp"
response = requests.get(url)
data = response.json()
print("📐 Dimensioni disponibili:", data["dimension"].keys())
print("🔢 Numero di valori:", len(data["value"]))
```

    📐 Dimensioni disponibili: dict_keys(['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'])
    🔢 Numero di valori: 7881265

filtriamo ora in sequenza le varie dimensioni ['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'] dopo averle interrogate una per volta 


### filtro su unit

```python
data["dimension"]["unit"]["category"]["label"]
```

    {'CLV_I20': 'Chain linked volumes, index 2020=100',
     'CLV_I15': 'Chain linked volumes, index 2015=100',
     'CLV_I10': 'Chain linked volumes, index 2010=100',
     'CLV_I05': 'Chain linked volumes, index 2005=100',
     'PC_GDP': 'Percentage of gross domestic product (GDP)',
     'CP_MEUR': 'Current prices, million euro',
     'CP_MNAC': 'Current prices, million units of national currency',
     'CLV20_MEUR': 'Chain linked volumes (2020), million euro',
     'CLV15_MEUR': 'Chain linked volumes (2015), million euro',
     'CLV10_MEUR': 'Chain linked volumes (2010), million euro',
     'CLV05_MEUR': 'Chain linked volumes (2005), million euro',
     'CLV20_MNAC': 'Chain linked volumes (2020), million units of national currency',
     'CLV15_MNAC': 'Chain linked volumes (2015), million units of national currency',
     'CLV10_MNAC': 'Chain linked volumes (2010), million units of national currency',
     'CLV05_MNAC': 'Chain linked volumes (2005), million units of national currency',
     'CLV_PCH_PRE': 'Chain linked volumes, percentage change on previous period',
     'CLV_PCH_SM': 'Chain linked volumes, percentage change compared to same period in previous year',
     'CLV_PCH_ANN': 'Chain linked volumes, annualized percentage change on previous period',
     'PYP_MEUR': 'Previous year prices, million euro',
     'PYP_MNAC': 'Previous year prices, million units of national currency',
     'CON_PPCH_PRE': 'Contribution to GDP growth, percentage point change on previous period',
     'CON_PPCH_SM': 'Contribution to GDP growth, percentage point change compared to same period in previous year',
     'PD20_EUR': 'Price index (implicit deflator), 2020=100, euro',
     'PD15_EUR': 'Price index (implicit deflator), 2015=100, euro',
     'PD10_EUR': 'Price index (implicit deflator), 2010=100, euro',
     'PD05_EUR': 'Price index (implicit deflator), 2005=100, euro',
     'PD20_NAC': 'Price index (implicit deflator), 2020=100, national currency',
     'PD15_NAC': 'Price index (implicit deflator), 2015=100, national currency',
     'PD10_NAC': 'Price index (implicit deflator), 2010=100, national currency',
     'PD05_NAC': 'Price index (implicit deflator), 2005=100, national currency',
     'PD_PCH_PRE_EUR': 'Price index (implicit deflator), percentage change on previous period, euro',
     'PD_PCH_PRE_NAC': 'Price index (implicit deflator), percentage change on previous period, national currency',
     'PD_PCH_SM_EUR': 'Price index (implicit deflator), percentage change compared to same period in previous year, euro',
     'PD_PCH_SM_NAC': 'Price index (implicit deflator), percentage change compared to same period in previous year, national currency'}

```python
# filtro sulla dimensione unit
url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?unit=CLV_I20"
response = requests.get(url)
data = response.json()
print("📐 Dimensioni disponibili:", data["dimension"].keys())
print("🔢 Numero di valori:", len(data["value"]))
```

    📐 Dimensioni disponibili: dict_keys(['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'])
    🔢 Numero di valori: 245663

### filtro su s_adj

```python
data["dimension"]["s_adj"]["category"]["label"]
```

    {'NSA': 'Unadjusted data (i.e. neither seasonally adjusted nor calendar adjusted data)',
     'SA': 'Seasonally adjusted data, not calendar adjusted data',
     'CA': 'Calendar adjusted data, not seasonally adjusted data',
     'SCA': 'Seasonally and calendar adjusted data'}

```python
# filtro sulla dimensione na_item
url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?unit=CLV_I20&s_adj=SCA"
response = requests.get(url)
data = response.json()
print("📐 Dimensioni disponibili:", data["dimension"].keys())
print("🔢 Numero di valori:", len(data["value"]))
```

    📐 Dimensioni disponibili: dict_keys(['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'])
    🔢 Numero di valori: 105015

### filtro su na_item

```python
data["dimension"]["na_item"]["category"]["label"]
```

    {'B1GQ': 'Gross domestic product at market prices',
     'B1G': 'Value added, gross',
     'P3': 'Final consumption expenditure',
     'P3_S13': 'Final consumption expenditure of general government',
     'P31_S13': 'Individual consumption expenditure of general government',
     'P32_S13': 'Collective consumption expenditure of general government',
     'P31_S14_S15': 'Household and NPISH final consumption expenditure',
     'P31_S14': 'Final consumption expenditure of households',
     'P31_S15': 'Final consumption expenditure of NPISH',
     'P41': 'Actual individual consumption',
     'P5G': 'Gross capital formation',
     'P51G': 'Gross fixed capital formation',
     'P52_P53': 'Changes in inventories and acquisitions less disposals of valuables',
     'P52': 'Changes in inventories',
     'P53': 'Acquisitions less disposals of valuables',
     'P6': 'Exports of goods and services',
     'P61': 'Exports of goods',
     'P62': 'Exports of services',
     'P7': 'Imports of goods and services',
     'P71': 'Imports of goods',
     'P72': 'Imports of services',
     'B11': 'External balance of goods and services',
     'B111': 'External balance - goods',
     'B112': 'External balance - services',
     'D1': 'Compensation of employees',
     'D11': 'Wages and salaries',
     'D12': "Employers' social contributions",
     'B2A3G': 'Operating surplus and mixed income, gross',
     'D2X3': 'Taxes on production and imports less subsidies',
     'D2': 'Taxes on production and imports',
     'D3': 'Subsidies',
     'D21X31': 'Taxes less subsidies on products',
     'D21': 'Taxes on products',
     'D31': 'Subsidies on products',
     'YA1': 'Statistical discrepancy (production approach)',
     'YA0': 'Statistical discrepancy (expenditure approach)',
     'YA2': 'Statistical discrepancy (income approach)',
     'P3_P5': 'Final consumption expenditure and gross capital formation',
     'P3_P6': 'Final consumption expenditure, gross capital formation and exports of goods and services'}


```python
# filtro sulla nazione
url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?unit=CLV_I20&s_adj=SCA&na_item=B1G"
response = requests.get(url)
data = response.json()
print("📐 Dimensioni disponibili:", data["dimension"].keys())
print("🔢 Numero di valori:", len(data["value"]))
```

    📐 Dimensioni disponibili: dict_keys(['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'])
    🔢 Numero di valori: 4721

### filtro su nazione

```python
data["dimension"]["geo"]["category"]["label"]
```

    {'EU27_2020': 'European Union - 27 countries (from 2020)',
     'EA': 'Euro area (EA11-1999, EA12-2001, EA13-2007, EA15-2008, EA16-2009, EA17-2011, EA18-2014, EA19-2015, EA20-2023)',
     'EA20': 'Euro area – 20 countries (from 2023)',
     'EA19': 'Euro area - 19 countries  (2015-2022)',
     'EA12': 'Euro area - 12 countries (2001-2006)',
     'BE': 'Belgium',
     'BG': 'Bulgaria',
     'CZ': 'Czechia',
     'DK': 'Denmark',
     'DE': 'Germany',
     'EE': 'Estonia',
     'IE': 'Ireland',
     'EL': 'Greece',
     'ES': 'Spain',
     'FR': 'France',
     'HR': 'Croatia',
     'IT': 'Italy',
     'CY': 'Cyprus',
     'LV': 'Latvia',
     'LT': 'Lithuania',
     'LU': 'Luxembourg',
     'HU': 'Hungary',
     'MT': 'Malta',
     'NL': 'Netherlands',
     'AT': 'Austria',
     'PL': 'Poland',
     'PT': 'Portugal',
     'RO': 'Romania',
     'SI': 'Slovenia',
     'SK': 'Slovakia',
     'FI': 'Finland',
     'SE': 'Sweden',
     'IS': 'Iceland',
     'NO': 'Norway',
     'CH': 'Switzerland',
     'UK': 'United Kingdom',
     'BA': 'Bosnia and Herzegovina',
     'ME': 'Montenegro',
     'MK': 'North Macedonia',
     'AL': 'Albania',
     'RS': 'Serbia',
     'TR': 'Türkiye',
     'XK': 'Kosovo*'}

```python
# filtro sulla nazione
url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?unit=CLV_I20&s_adj=SCA&na_item=B1G&geo=IT"
response = requests.get(url)
data = response.json()
print("📐 Dimensioni disponibili:", data["dimension"].keys())
print("🔢 Numero di valori:", len(data["value"]))
```

    📐 Dimensioni disponibili: dict_keys(['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'])
    🔢 Numero di valori: 117

### filtro su time

```python
data["dimension"]["time"]["category"]["label"]
```

    {'1975-Q1': '1975-Q1',
    ...
     '2024-Q4': '2024-Q4',
     '2025-Q1': '2025-Q1'}

```python
# filtro sulla dimensione na_item
url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?unit=CLV_I20&s_adj=SCA&na_item=B1G&geo=IT&time=2023-Q1"
response = requests.get(url)
data = response.json()
print("📐 Dimensioni disponibili:", data["dimension"].keys())
print("🔢 Numero di valori:", len(data["value"]))
```

    📐 Dimensioni disponibili: dict_keys(['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'])
    🔢 Numero di valori: 1

## nama_10_gdp

- Gross domestic product (GDP) and main components (output, expenditure and income)
- annuale
- Contabilità nazionale annuale
- Principale per analisi strutturale

Oltre a [namq_10_gdp](https://ec.europa.eu/eurostat/en/web/main/search/-/search/dataset?_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_pageNumber=1&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_pageSize=11&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_text=tec00115&p_auth=tvLAcqGs&text=namq_10_gdp), stessa cosa possiamo ottenerla da [nama_10_gdp](https://ec.europa.eu/eurostat/en/web/main/search/-/search/dataset?_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_pageNumber=1&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_pageSize=11&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_text=namq_10_gdp&p_auth=tvLAcqGs&text=nama_10_gdp) - **Gross domestic product (GDP) and main components (output, expenditure and income)**

vediamo come la serie di filtri hanno ridotto i dati sa estrarre: 

| dimensione | filtro                                            | namq_10_gdp | nama_10_gdp |
| ---------- | ------------------------------------------------- | ----------: | ----------: |
|            |                                                   |   7.881.265 |   1.049.888 |
| unit       | 'CLV_I20': 'Chain linked volumes, index 2020=100' |     245.663 |      29.825 |
| s_adj      | 'SCA': 'Seasonally and calendar adjusted data'    |     105.015 |             |
| na_item    | 'B1GQ': 'Gross domestic product at market prices' |       4.721 |       1.313 |
| geo        | 'IT': 'Italy'                                     |         117 |          30 |
| time       | '2023-Q1' / '2023'                                |           1 |           1 |


questo è il [link](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?unit=CLV_I20&s_adj=SCA&na_item=B1G&geo=IT&time=2025-Q1) per avere il valore puntuale 

```python
data
```

    {'version': '2.0',
     'class': 'dataset',
     'label': 'Gross domestic product (GDP) and main components (output, expenditure and income)',
     'source': 'ESTAT',
     'updated': '2025-06-19T23:00:00+0200',
     'value': {'0': 116.239},
     'id': ['freq', 'unit', 's_adj', 'na_item', 'geo', 'time'],
     'size': [1, 1, 1, 1, 1, 1],
     'dimension': {'freq': {'label': 'Time frequency',
       'category': {'index': {'Q': 0}, 'label': {'Q': 'Quarterly'}}},
      'unit': {'label': 'Unit of measure',
       'category': {'index': {'CLV_I20': 0},
        'label': {'CLV_I20': 'Chain linked volumes, index 2020=100'}}},
      's_adj': {'label': 'Seasonal adjustment',
       'category': {'index': {'SCA': 0},
        'label': {'SCA': 'Seasonally and calendar adjusted data'}}},
      'na_item': {'label': 'National accounts indicator (ESA 2010)',
       'category': {'index': {'B1G': 0}, 'label': {'B1G': 'Value added, gross'}}},
      'geo': {'label': 'Geopolitical entity (reporting)',
       'category': {'index': {'IT': 0}, 'label': {'IT': 'Italy'}}},
      'time': {'label': 'Time',
       'category': {'index': {'2025-Q1': 0}, 'label': {'2025-Q1': '2025-Q1'}}}},
     'extension': {'lang': 'EN',
      'id': 'NAMQ_10_GDP',
      'agencyId': 'ESTAT',
      'version': '1.0',
      'datastructure': {'id': 'NAMQ_10_GDP',
       'agencyId': 'ESTAT',
       'version': '128.0'},
      'annotation': [{'type': 'CREATED', 'date': '2014-09-04T14:58:29+0200'},
       {'type': 'DISSEMINATION_DOI_XML',
        'title': '<adms:identifier xmlns:adms="http://www.w3.org/ns/adms#" xmlns:skos="http://www.w3.org/2004/02/skos/core.html" xmlns:dct="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><adms:Identifier rdf:about="https://doi.org/10.2908/NAMQ_10_GDP"><skos:notation rdf:datatype="http://purl.org/spar/datacite/doi">10.2908/NAMQ_10_GDP</skos:notation><dct:creator rdf:resource="http://publications.europa.eu/resource/authority/corporate-body/ESTAT"/><dct:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2023-01-23</dct:issued></adms:Identifier></adms:identifier>'},
       {'type': 'DISSEMINATION_OBJECT_TYPE', 'title': 'DATASET'},
       {'type': 'DISSEMINATION_TIMESTAMP_DATA',
        'date': '2025-06-19T23:00:00+0200'},
       {'type': 'DISSEMINATION_TIMESTAMP_GLOBAL',
        'date': '2025-06-19T23:00:00+0200'},
       {'type': 'DISSEMINATION_TIMESTAMP_PLANNED',
        'date': '2025-06-19T23:00:00+0200'},
       {'type': 'ESMS_HTML',
        'title': 'Explanatory texts (metadata)',
        'href': 'https://ec.europa.eu/eurostat/cache/metadata/en/namq_10_gdp_esms.htm'},
       {'type': 'ESMS_SDMX',
        'title': 'Explanatory texts (metadata)',
        'href': 'https://ec.europa.eu/eurostat/api/dissemination/files?file=metadata/namq_10_gdp_esms.sdmx.zip'},
       {'type': 'FOOTNOTE',
        'title': 'Footnote (metadata)',
        'href': 'https://ec.europa.eu/eurostat/cache/metadata/Annexes/namq_10_gdp_esms_an_namq_10_gdp.xlsx'},
       {'type': 'OBS_COUNT', 'title': '7881265'},
       {'type': 'OBS_PERIOD_OVERALL_LATEST', 'title': '2025-Q1'},
       {'type': 'OBS_PERIOD_OVERALL_OLDEST', 'title': '1975-Q1'},
       {'type': 'SOURCE_INSTITUTIONS', 'text': 'Eurostat'},
       {'type': 'UPDATE_DATA', 'date': '2025-06-19T23:00:00+0200'},
       {'type': 'UPDATE_FOOTNOTES', 'date': '2025-06-18T13:30:02Z'},
       {'type': 'UPDATE_STRUCTURE', 'date': '2025-04-29T23:00:00+0200'}],
      'positions-with-no-data': {'freq': [],
       'unit': [],
       's_adj': [],
       'na_item': [],
       'geo': [],
       'time': []}}}

### Una sorpresa 

nel json ci sono anche 3 indirizzi molto interessanti che non occorre spiegare:
- https://ec.europa.eu/eurostat/cache/metadata/en/namq_10_gdp_esms.htm
- https://ec.europa.eu/eurostat/api/dissemination/files?file=metadata/namq_10_gdp_esms.sdmx.zip
- https://ec.europa.eu/eurostat/cache/metadata/Annexes/namq_10_gdp_esms_an_namq_10_gdp.xlsx

## costruiamo il filtro 

siamo ora pronti per interrogare l'API con una query puntuale in modo da scaricare solo i dati necessari  
la query ci permetterà di costruire l'url corretto, inserendo tutti i parametri che ci interessano  
se non valorizziamo una delle dimensioni previste nel dataset, questa verrà scaricata integralmente  

```python
def eurostat_url(dataset, filters: dict, fmt="JSON"):
    # Costruisce i parametri con chiavi ripetute per ogni valore
    param_list = []
    for key, val in filters.items():
        values = val if isinstance(val, list) else [val]
        for v in values:
            param_list.append(f"{key}={v}")
    params = "&".join(param_list)
    return f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{dataset}?{params}&format={fmt}"
```

```python
url = eurostat_url(
    dataset="namq_10_gdp",
    filters={
        'freq': ["Q"], 
        'unit': ["CLV_I20"],
        's_adj':["SCA"],
        'na_item':["B1GQ"],
        'geo': ['IT', 'DE'],
#        'time': ['2024-Q4','2025-Q1']
    }
)
print(url)
```

https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?freq=Q&unit=CLV_I20&s_adj=SCA&na_item=B1GQ&geo=IT&geo=DE&format=JSON
    
A questo punto diventa fondamentale conoscere tutti i valori che possono assumere tutte le dimensioni presenti negli oltre 9.300 dataset Eurostat.
Un giochetto ! ;-)



## namq_10_gdp VS nama_10_gdp

le differenze tra `**namq_10_gdp**` e `**nama_10_gdp**` si riducono principalmente alla **frequenza temporale**:

|Dataset|Frequenza|Nome completo|Note principali|
|---|---|---|---|
|`namq_10_gdp`|**Trimestrale**|**National accounts - quarterly data (ESA 2010)**|Dati a frequenza **Q** (Quarterly)|
|`nama_10_gdp`|**Annuale**|**National accounts - annual data (ESA 2010)**|Dati a frequenza **A** (Annual)|

### Ulteriori differenze:

Entrambi i dataset contengono voci come:

- `na_item = B1GQ` (PIL ai prezzi di mercato)
    
- `unit = CLV_I10` o `CLV_I20` (prezzi concatenati, base 2010 o 2020)
    
- `s_adj = SCA` (dati destagionalizzati e corretti per effetti di calendario)
    
- `geo = ...` (paesi UE, EA19, ecc.)
    

### Compatibilità delle dimensioni:

- Le dimensioni (`na_item`, `unit`, `geo`, ecc.) sono **quasi identiche**.
    
- La dimensione `freq` non è presente come filtro esplicito perché **è fissa per ciascun dataset** (`A` o `Q`).
    

Se vuoi confrontare **PIL annuale vs trimestrale**, puoi:

- Usare `nama_10_gdp` per un **long-term trend**.
    
- Usare `namq_10_gdp` per analisi **cicliche o a breve termine**.



## nama_10r_3gdp

## altri dataset simili

