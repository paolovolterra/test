---
title:
authors:
  - 
url:
tags:
  - PIL
  - Eurostat
  - Prometeia
  - grafici
  - Python
created: 2025-06-16 20:53
---
## Dimensioni
### freq: 1 items
- Q: Quarterly

### unit: 1 items
- CLV10_MEUR: Chain linked volumes (2010), million euro

### s_adj: 1 items
- Seasonally and calendar adjusted data

### geo: 

### time: 

### na_item: 39 items

Il dataset Eurostat `namq_10_gdp` ha **39 voci** nella dimensione `na_item`, ciascuna rappresentante un **aggregato contabile nazionale** secondo il sistema ESA 2010 (European System of Accounts):

  - B11: External balance of goods and services
  - B111: External balance - goods
  - B112: External balance - services
  - **B1G: Value added, gross**
  - B1GQ: Gross domestic product at market prices
  - B2A3G: Operating surplus and mixed income, gross
  - D1: Compensation of employees
  - D11: Wages and salaries
  - D12: Employers' social contributions
  - D2: Taxes on production and imports
  - D21: Taxes on products
  - D21X31: Taxes less subsidies on products
  - D2X3: Taxes on production and imports less subsidies
  - D3: Subsidies
  - D31: Subsidies on products
  - P3: Final consumption expenditure
  - P31_S13: Individual consumption expenditure of general government
  - P31_S14: Final consumption expenditure of households
  - P31_S14_S15: Household and NPISH final consumption expenditure
  - P31_S15: Final consumption expenditure of NPISH
  - P32_S13: Collective consumption expenditure of general government
  - P3_P5: Final consumption expenditure and gross capital formation
  - P3_P6: Final consumption expenditure, gross capital formation and exports of goods and services
  - P3_S13: Final consumption expenditure of general government
  - P41: Actual individual consumption
  - P51G: Gross fixed capital formation
  - P52: Changes in inventories
  - P52_P53: Changes in inventories and acquisitions less disposals of valuables
  - P53: Acquisitions less disposals of valuables
  - P5G: Gross capital formation
  - P6: Exports of goods and services
  - P61: Exports of goods
  - P62: Exports of services
  - P7: Imports of goods and services
  - P71: Imports of goods
  - P72: Imports of services
  - YA0: Statistical discrepancy (expenditure approach)
  - YA1: Statistical discrepancy (production approach)
  - YA2: Statistical discrepancy (income approach)

 Tra queste, la voce più comunemente usata per rappresentare il **PIL** è: `B1GQ` – _Gross Domestic Product at market prices_


### Perché si usa `B1GQ` per il PIL?

- **È il PIL nella sua definizione ufficiale** secondo l'ESA 2010.
    
- È il risultato dell'identità contabile:
    
    ```
    PIL = Consumi finali + Investimenti + (Esportazioni - Importazioni)
        = Valore aggiunto lordo + Imposte sui prodotti - Sussidi sui prodotti
    ```
    
- È la voce sintetica più rappresentativa per confronti internazionali e temporali.
    

### Quando si usano gli altri 38 `na_item`?

Servono per **analisi più dettagliate** del PIL o della contabilità nazionale. Alcuni esempi:

|Codice|Descrizione sintetica|Uso tipico|
|---|---|---|
|**B1G**|Valore aggiunto lordo a prezzi base|Analisi produttività|
|**D1**|Retribuzioni dei dipendenti|Mercato del lavoro|
|**P3**|Spesa per consumi finali|Consumi privati e pubblici|
|**P5G**|Formazione lorda di capitale (investimenti)|Cicli economici|
|**P6**|Esportazioni di beni e servizi|Commercio estero|
|**P7**|Importazioni di beni e servizi|Commercio estero|
|**B9**|Saldo economico netto (risparmio nazionale)|Risparmio/investimenti|
|**B2A3G**|Risultato operativo lordo (gross operating surplus)|Profitti imprese|

### Quando usarli nei grafici?

- **Analisi settoriale o funzionale**: per esempio, confrontare `P3` (consumi) e `P5G` (investimenti).
    
- **Studio della domanda aggregata**: `P3 + P5G + (P6 - P7)` deve uguagliare `B1GQ`.
    
- **Analisi del reddito primario**: `D1`, `B2A3G`, ecc.
    
- **Per derivare il PIL via produzione, spesa o reddito**, si usano combinazioni specifiche di `na_item`.
    

### Risorse utili

- [Eurostat Metadata - ESA 2010 aggregates](https://ec.europa.eu/eurostat/cache/metadata/en/nama_10_gdp_esms.htm)
- [Manuale ESA 2010](https://ec.europa.eu/eurostat/documents/3859598/5925693/KS-02-13-269-EN.PDF)



## Le pià usate

Le voci `na_item` più comunemente utilizzate nei grafici e nelle analisi macroeconomiche (oltre a `B1GQ`) sono quelle che compongono o spiegano le principali **identità contabili** della contabilità nazionale: **produzione, reddito, spesa**. 
Ecco una selezione delle più rilevanti e frequentemente utilizzate:

### **Contabilità della produzione**

|Codice|Descrizione|Uso comune|
|---|---|---|
|`B1GQ`|Gross domestic product at market prices (PIL)|Principale misura dell’attività economica|
|`B1G`|Value added, gross|Valore aggiunto lordo (PIL a prezzi base)|
|`D2`|Taxes on production and imports|Per ricostruire il passaggio da VA a PIL|
|`D3`|Subsidies|Idem, con segno opposto alle imposte|


### **Contabilità della spesa (domanda aggregata)**

|Codice|Descrizione|Uso comune|
|---|---|---|
|`P3`|Final consumption expenditure|Consumi totali|
|`P31S14`|Final consumption expenditure of households|Consumi privati|
|`P31S13`|Final consumption expenditure of general government|Consumi pubblici|
|`P5G`|Gross capital formation|Investimenti|
|`P6`|Exports of goods and services|Esportazioni|
|`P7`|Imports of goods and services|Importazioni|


### **Contabilità del reddito**

|Codice|Descrizione|Uso comune|
|---|---|---|
|`D1`|Compensation of employees|Occupazione e redditi|
|`D11`|Wages and salaries|Salari|
|`D12`|Employers' social contributions|Contributi sociali|
|`B2A3G`|Gross operating surplus and mixed income|Profitti lordi (imprese e autonomi)|
|`B5G`|Gross national income|Reddito nazionale lordo|
|`B6G`|Gross disposable income|Reddito disponibile lordo|


### In sintesi

|Tipo Analisi|Voci chiave|
|---|---|
|PIL aggregato|`B1GQ`|
|Pil lato offerta|`B1G`, `D2`, `D3`|
|Pil lato spesa|`P3`, `P5G`, `P6`, `P7`|
|Pil lato reddito|`D1`, `B2A3G`, `B5G`, `B6G`|
|Famiglie|`P31S14`, `D11`, `B6G`|
|Governo|`P31S13`, `D12`, `D2`, `D5`|
