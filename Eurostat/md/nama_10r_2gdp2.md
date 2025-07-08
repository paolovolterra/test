# [nama_10r_2gdp](https://ec.europa.eu/eurostat/en/web/main/search/-/search/dataset?text=nama_10r_2gdp)

#PIL #NUTS2

_Gross domestic product (GDP) at current market prices by NUTS 2 region_


Il dataset **`nama_10r_2gdp`** di Eurostat corrisponde ai dati sul **Prodotto Interno Lordo (PIL)** a prezzi correnti, analizzato per **regioni NUTS 2**, ovvero le macro-regioni statistiche a livello intermedio (ad esempio, Piemonte, Lombardia, Catalunya, etc.) ([ec.europa.eu](https://ec.europa.eu/eurostat/databrowser/product/view/nama_10r_2gdp?utm_source=chatgpt.com "Gross domestic product (GDP) at current market prices by NUTS 2 ...")).

### Cosa contiene

- **PIL a prezzi correnti**: esprime il valore totale dei beni e servizi prodotti, valutati ai prezzi del periodo di riferimento.
    
- **Unità di misura**: solitamente in milioni di euro, con periodicità annuale.
    
- **Livello territoriale**: regione NUTS 2, utile per confronti territoriali all’interno della UE  

###  Frequenza e aggiornamento

- I dati sono aggiornati con cadenza annuale: l’ultimo aggiornamento disponibile risale al **18 marzo 2025**, con valori “p” (provisional, provvisori) per il 2022 e il 2023 .
    
- Questo consente di analizzare trend di crescita economica, confronti tra regioni e contributi al PIL nazionale.

### Perché è utile

1. **Analisi regionale**: confrontare la performance economica tra regioni, come crescita, dimensione e peso sul totale nazionale.
    
2. **Pianificazione territoriale**: strumento per policy-maker, investitori e amministrazioni locali.
    
3. **Confronti europei**: consente di posizionare le regioni italiane nel contesto europeo.
    

## 4 Dimensioni

esempio https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_2gdp?geo=IT&time=2025-04

## unit

#HAB 

1. "MIO_EUR": "Million euro",
2. "EUR_HAB": "Euro per inhabitant",
3. "EUR_HAB_EU27_2020": "Euro per inhabitant in percentage of the EU27 (from 2020) average",
4. "MIO_NAC": "Million units of national currency",
5. "MIO_PPS_EU27_2020": "Million purchasing power standards (PPS, EU27 from 2020)",
6. "PPS_EU27_2020_HAB": "Purchasing power standard (PPS, EU27 from 2020), per inhabitant",
7. "PPS_HAB_EU27_2020": "Purchasing power standard (PPS, EU27 from 2020), per inhabitant in percentage of the EU27 (from 2020) average"


si tratta di **unità di misura diverse** usate nei dataset Eurostat, in particolare nei conti nazionali regionali (`nama_10r_2gdp`, `nama_10r_3gdp`, ecc.). 
###  1. `"MIO_EUR"` – _Million euro_

- **Definizione**: PIL o altra variabile espresso in **milioni di euro correnti**.
    
- **Uso**: confronti assoluti tra regioni o paesi in termini monetari.
    
- **Limite**: non tiene conto delle dimensioni della popolazione né del potere d’acquisto.
    

### 2. `"EUR_HAB"` – _Euro per inhabitant_

- **Definizione**: valore per abitante in **euro correnti**.
    
- **Uso**: confronti tra regioni normalizzati per popolazione.
    
- **Limite**: non tiene conto del costo della vita (es. 10.000 €/hab in Bulgaria ≠ in Francia).
    


### 3. `"EUR_HAB_EU27_2020"` – _Euro per inhabitant in % of EU27 (2020) average_

- **Definizione**: PIL pro capite in euro espresso come **% rispetto alla media UE27 (base 100)**.
    
- **Uso**: misura relativa del benessere monetario rispetto alla media UE.
    
- **Esempio**: 120 = 20% sopra la media UE27.
    

### 4. `"MIO_NAC"` – _Million units of national currency_

- **Definizione**: valori espressi in **milioni della valuta nazionale** (es. zloty in Polonia).
    
- **Uso**: solo per paesi **non euro**.
    
- **Nota**: per i paesi euro equivale a `MIO_EUR`.
    

### 5. `"MIO_PPS_EU27_2020"` – _Million PPS (EU27 from 2020)_

- **Definizione**: valori espressi in **milioni di standard di potere d’acquisto** (PPS), base UE27 2020.
    
- **Uso**: consente confronti tra regioni tenendo conto dei diversi livelli di prezzo.
    
- **PPS** ≈ euro "corretti" per il costo della vita.
    

### 6. `"PPS_EU27_2020_HAB"` – _PPS per inhabitant_

- **Definizione**: **PIL pro capite in PPS**, utile per confronti di benessere economico reale.
    
- **Uso**: confronto diretto della ricchezza/potere d’acquisto tra regioni.
    

### 7. `"PPS_HAB_EU27_2020"` – _PPS per inhabitant in % of EU27 (2020) average_

- **Definizione**: PIL pro capite in PPS come **% della media UE27 (2020)**.
    
- **Uso**: indicatore chiave di convergenza regionale (es. in coesione UE).
    
- **Esempio**: 65 = il potere d’acquisto pro capite è il 65% della media UE.
    

### Confronto sintetico:

| Codice              | Valuta  | Per capita? | Prezzi comparabili? | In % UE27 |
| ------------------- | ------- | :---------: | :-----------------: | :-------: |
| `MIO_EUR`           | €       | ❌           | ❌                   | ❌         |
| `EUR_HAB`           | €       | ✅           | ❌                   | ❌         |
| `EUR_HAB_EU27_2020` | €       | ✅           | ❌                   | ✅         |
| `MIO_NAC`           | val.naz | ❌           | ❌                   | ❌         |
| `MIO_PPS_EU27_2020` | PPS     | ❌           | ✅                   | ❌         |
| `PPS_EU27_2020_HAB` | PPS     | ✅           | ✅                   | ❌         |
| `PPS_HAB_EU27_2020` | PPS     | ✅           | ✅                   | ✅         |

---

Hai bisogno di un grafico comparativo (es. PPS per abitante per tutte le regioni italiane)? Posso generarlo direttamente.

### geo

- "EU27_2020": "European Union - 27 countries (from 2020)",
- ...
- "IT": "Italy",
- "ITC": "Nord-Ovest",
- "ITC1": "Piemonte",
- "ITC2": "Valle d’Aosta/Vallée d’Aoste",
- "ITC3": "Liguria",
- "ITC4": "Lombardia",
- "ITF": "Sud",
- "ITF1": "Abruzzo",
- "ITF2": "Molise",
- "ITF3": "Campania",
- "ITF4": "Puglia",
- "ITF5": "Basilicata",
- "ITF6": "Calabria",
- "ITG": "Isole",
- "ITG1": "Sicilia",
- "ITG2": "Sardegna",
- "ITH": "Nord-Est",
- "ITH1": "Provincia Autonoma di Bolzano/Bozen",
- "ITH2": "Provincia Autonoma di Trento",
- "ITH3": "Veneto",
- "ITH4": "Friuli-Venezia Giulia",
- "ITH5": "Emilia-Romagna",
- "ITI": "Centro (IT)",
- "ITI1": "Toscana",
- "ITI2": "Umbria",
- "ITI3": "Marche",
- "ITI4": "Lazio",
- "ITZ": "Extra-Regio NUTS 1",
- "ITZZ": "Extra-Regio NUTS 2",
- ...


## estrazione 


```Python


```