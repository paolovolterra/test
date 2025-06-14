
# IPCA – Indice dei Prezzi al Consumo Armonizzato

- **Definizione:** Misura l'inflazione al consumo secondo criteri armonizzati a livello europeo (Eurostat).
    
- **Copertura geografica:** Uniforme per tutti i Paesi UE.
    
- **Uso principale:** Confrontabilità tra paesi dell'UE. È l'indicatore ufficiale per la **BCE** (Banca Centrale Europea) per monitorare la **stabilità dei prezzi**.
    
- **Caratteristiche:**
    
    - Esclude la **spesa per abitazione di proprietà** (spesa stimata e non affitto reale).
        
    - Include la spesa di **tutte le famiglie** e **turisti stranieri** in Italia.
        
- **Fonte:** Istat, con standard Eurostat.



## definizioni e del confronto tra **IPCA**, **NIC**, **FOI**, e **FOB**

### NIC – Indice dei Prezzi al Consumo per l'intera collettività

- **Definizione:** Misura l’inflazione percepita dalle **famiglie residenti in Italia**, su tutto il territorio nazionale.
    
- **Uso principale:** Analisi **interna** del potere d’acquisto e contrattazione salariale.
    
- **Caratteristiche:**
    
    - Include sia famiglie proprietarie sia affittuarie.
        
    - Non considera spese sostenute da **non residenti**.
        
- **Fonte:** Istat.
    


### FOI – Indice dei Prezzi al Consumo per le famiglie di operai e impiegati**

- **Definizione:** Derivato dal NIC, ma limitato alle **famiglie di operai e impiegati** (escluse quelle con solo pensionati o imprenditori).
    
- **Uso principale:** Riferimento per **rivalutazioni monetarie**, come **canoni di affitto**, **assegni**, ecc.
    
- **Caratteristiche:**
    
    - È il più “tradizionale” degli indici.
        
    - Non include le spese per **tabacchi**.
        
- **Fonte:** Istat.
    



### FOB – Free On Board (Prezzi all’Export)

- **Definizione:** Non è un indice dei prezzi al consumo, ma una **condizione di consegna** nel commercio estero: il prezzo di un bene **alla frontiera del paese esportatore**, senza includere trasporto o assicurazione internazionale.
    
- **Uso principale:** Commercio estero, **bilancia commerciale**.
    
- **Differenza chiave:** Si riferisce ai **prezzi all’esportazione**, **non all’inflazione interna**.
    



### CONFRONTO SINTETICO

|Sigla|Nome|Copertura|Uso principale|Esclude / Include|
|---|---|---|---|---|
|IPCA|Indice armonizzato|UE|Politica monetaria BCE|Include turisti, esclude proprietà|
|NIC|Collettività nazionale|Italia (residenti)|Analisi inflazione interna|Include tutti i residenti|
|FOI|Famiglie operai/impiegati|Italia (subset NIC)|Rivalutazioni monetarie|Esclude tabacchi, include solo alcune famiglie|
|FOB|Free On Board (export)|Internazionale|Prezzo export alla frontiera|Non è un indice dei prezzi al consumo|


### In breve:

- **IPCA** → confronto europeo, senza spesa abitativa.
- **NIC** → misura ufficiale dell’inflazione in Italia.
- **FOI** → usato per rivalutazioni, è una versione ristretta del NIC.   
- **FOB** → prezzo doganale all’esportazione, non è un indice di inflazione.
    
Se vuoi posso anche prepararti un grafico comparativo con i trend storici dei tre indici italiani (IPCA, NIC, FOI). Vuoi procedere?


# IPCA - approfondimenti


L'indice è stato sviluppato per assicurare una misura dell'inflazione che fosse comparabile a livello europeo; l'indice, riferito alla stessa popolazione ed allo stesso territorio dell'indice dei prezzi al consumo per l'intera collettività, è però calcolato in relazione ad un paniere di beni e servizi costruito tenendo conto sia delle particolarità di ogni paese sia di regole comuni per la ponderazione dei beni che compongono tale paniere (ad esempio il paniere considerato esclude, sulla base di un accordo comunitario, le [lotterie](https://it.wikipedia.org/wiki/Lotteria "Lotteria"), il [lotto](https://it.wikipedia.org/wiki/Lotto "Lotto") e i concorsi pronostici); l'IPCA è stato assunto come indicatore di verifica della convergenza delle economie dei paesi membri dell'UE al fine dell'accesso all'[Unione monetaria](https://it.wikipedia.org/wiki/Unione_economica_e_monetaria "Unione economica e monetaria") e della permanenza nella stessa dei paesi aderenti [^1].

- **CP00** è il codice standard Eurostat per **"All-items HICP"**, ovvero l’indice generale (non solo un sottoinsieme di beni/servizi).    
- **IPCA** è la traduzione italiana del termine **HICP**, usato da **ISTAT** e **Banca d’Italia** per indicare l’indice armonizzato europeo.
- Questo indice viene utilizzato, ad esempio, dalla BCE per valutare la stabilità dei prezzi.
- In Italia si chiama IPCA Indice dei Prezzi al Consumo Armonizzato; all'estero HICP (Harmonised Index of Consumer Prices, HICP)
- **l’Indice NIC**: sarebbe un’altra dimensione (`CP00_IT`, a volte codificato diversamente).
- **Confronto tra IPCA e NIC**: l’IPCA è armonizzato a livello europeo, il NIC è pensato per il solo contesto nazionale.
- Germania, Francia e Spagna hanno [oggi](2025-06-13.md) comunicato i rispettivi **IPCA**
- Ieri [12 giugno](2025-06-12.md) [Istat](Istat) ha comunicato quelli relativi all'[Italia](https://www.istat.it/comunicato-stampa/comunicazione-ipca-anni-2021-2024/)
- **l’HICP non contiene prezzi assoluti** (es. 1 litro di latte = 1,30€). Eurostat fornisce **solo indici sintetici**, non il prezzo effettivo di ogni bene
- i dati IPCA Italia sono disponibili sul sito [Istat]() , Bankit e [CCIAA di Macerata](https://opendata.marche.camcom.it/focus.htm?theme=prezzi-consumo)
- si tratta di oltre 3M3 di dati (non cliccare sui link: le estrazioni sono pesanti) che vengono forniti in 
	- [JSON](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr)
	- [SDMX](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/prc_hicp_manr?format=SDMX-CSV&compressed=true)
	- [TSV](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/prc_hicp_manr?format=TSV&compressed=true)

- l'API che rende disponibile i dati è customizzabile per estrarre un subset: qui ad esempio estraggo CP00 Italia 

```
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?coicop=CP00&geo=IT
```



### livello dell'indice dei prezzi
(es. HICP = 105,3, base 2015=100): sono nel dataset `prc_hicp_midx` (HICP - monthly data, index).

Esempio:

```
Date       | HICP (midx, CP00, IT)
-----------|----------------------
2020-01    | 104.3
2020-02    | 104.5
...
```

Questi sono **indici sintetici**.  
Se HICP = 104,3 nel 2020-01, significa che i prezzi sono cresciuti del 4,3% rispetto al valore medio del **2015** (che vale 100, perché è l'anno base dell’indice).


## Definizioni

- **IPCA**: indice armonizzato dei prezzi al consumo per i Paesi dell’Unione europea. 
- **IPCA-AS**: indici armonizzati dei prezzi al consumo per aggregati speciali sono indicatori costruiti secondo uno schema classificatorio diverso dalla ECOICOP-IPCA e da quello utilizzato per gli indici NIC per tipologia di prodotto. La struttura di classificazione e le procedure di calcolo sono comuni a quelle utilizzate da Eurostat e ne condividono le innovazioni di carattere metodologico. In particolare, dalla diffusione degli indici definitivi di gennaio 2019 cambia il metodo di calcolo degli aggregati speciali dell’IPCA che sono ottenuti aggregando gli indici delle sottoclassi della ECOICOP (in precedenza, per il computo di questi indicatori erano utilizzati gli indici delle classi). Per una migliore fruibilità dei nuovi indicatori, le serie degli aggregati speciali, secondo il nuovo schema, sono state ricostruite per il periodo gennaio 2017 - dicembre 2018 e sostituiscono, per l’intervallo temporale in questione, quelle precedentemente diffuse, basate sulla vecchia metodologia di calcolo. 
- **IPCA-TC**: indice armonizzato dei prezzi al consumo a tassazione costante per i Paesi dell’Unione europea


### prezzi assoluti (in euro)

- **OCSE** (solo alcune voci)
- **istat.it** → microdati IPCA su prodotti singoli,
- **Scanner data / database Nielsen / GfK** (a pagamento).

./
## IPCA e Istat

### Prezzi al consumo armonizzati per i paesi dell'Unione europea (Ipca)

- 168_6 IPCA – Pesi dal 2001
- 168_756 IPCA a tassazione costante - Dati mensili dal 2002 (base 2015=100)
- 168_757 IPCA a tassazione costante - Medie annue dal 2002 (base 2015=100)
- 168_758 Ipca - medie annue dal 2001 (base 2015)
- 168_760 Ipca - mensili dal 2001 (base 2015)

### Prezzi al consumo armonizzati per i paesi dell'Unione europea (Ipca) - Basi precedenti (Ipca)

- 168_2 IPCA – Dati mensili dal 2001 (base 2005=100)
- 168_5 IPCA – Medie annue dal 2001 (base 2005=100)
- 168_261 IPCA a tassazione costante – Medie annue dal 2002 (base 2005=100)
- 168_306 IPCA a tassazione costante – Dati mensili dal 2002 (base 2005=100)

![Pasted image 20250613121026](./media/Pasted%20image%2020250613121026.png)

![Pasted image 20250613120925](./media/Pasted%20image%2020250613120925.png)

![Pasted image 20250613120839](./media/Pasted%20image%2020250613120839.png)

![Pasted image 20250613120819](./media/Pasted%20image%2020250613120819.png)


![Pasted image 20250613120406](./media/Pasted%20image%2020250613120406.png)



## ICPA e Banca d'Italia

### [Banca d’Italia. (2025). _EIB-L’economia italiana in breve](https://www.bancaditalia.it/pubblicazioni/economia-italiana-in-breve/index.html)


![Pasted image 20250613115258](./media/Pasted%20image%2020250613115258.png)

![Pasted image 20250613115309](./media/Pasted%20image%2020250613115309.png)


### [Banca d’Italia. (2025). Proiezioni macroeconomiche per l’Italia](https://www.bancaditalia.it/pubblicazioni/proiezioni-macroeconomiche/)

![Pasted image 20250613115744](./media/Pasted%20image%2020250613115744.png)
  
_(Banca d'Italia, 2025, p. 2) Proiezioni macroeconomiche per l’economia italiana (variazioni percentuali sull’anno precedente, salvo diversa indicazione). Fonte: elaborazioni su dati Banca d’Italia e Istat. Quadro previsivo per l'Italia basato sulle informazioni disponibili al 28 marzo (per la formulazione delle ipotesi tecniche) e al 2 aprile (per i dati congiunturali). (1) Per il PIL e le sue componenti, variazioni stimate su dati trimestrali destagionalizzati e corretti per il numero di giornate lavorative. Senza tale correzione il PIL crescerebbe dello 0,5 per cento nel 2025, dello 0,9 nel 2026 e dello 0,7 nel 2027. – (2) In percentuale del PIL. – (3) Medie annue, valori percentuali._


## Ufficio Parlamentare di Bilancio. (2025). Nota sulla congiuntura
[https://www.upbilancio.it](https://www.upbilancio.it)

![Pasted image 20250613121656](./media/Pasted%20image%2020250613121656.png)


## Banca Intesa

![Pasted image 20250613123229](./media/Pasted%20image%2020250613123229.png)


## teicp000

**versione “light”** dell’HICP
- **Codice Eurostat**: `TEICP000`
- **Titolo completo**: _Harmonised Index of Consumer Prices (HICP) - All-items - Annual rate of change (%)_
- **Fonte**: dataset _short-term indicators_ (tematico, non dettagliato)
- **Copertura**: solo **CP00** (indice generale), **senza dettagli per COICOP**, **senza frequenza mensile**, solo **variazione % annuale**.
- **Uso tipico**: panoramiche economiche rapide, confronti cross-country a colpo d'occhio.


### Quando usare `teicp000`

- Per **grafici semplici** che confrontano paesi su base **annua**;
- In **dashboard** o **slide** con indicatori chiave;
- Quando non servono breakdown per categorie di consumo.
 

## Dataset analitici

La tabella appresso rappresenta le principali **serie Eurostat sull'HICP**, ciascuna con un focus diverso sulla dinamica dei prezzi:

| **Sigla**        | **Descrizione**                                                                       | **Uso tipico**                                                    |
| ---------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `prc_hicp_manr`  | HICP – **monthly data**, **annual rate of change** (tasso t/t-12)                     | Misura l’inflazione annua – **indice principale usato dalla BCE** |
| `prc_hicp_midx`  | HICP – **monthly data**, **index** (livello dell’indice, base variabile es: 2015=100) | Analisi di lungo periodo e confronti tra paesi                    |
| `prc_hicp_mmor`  | HICP – **monthly data**, **monthly rate of change** (var. % sul mese precedente)      | Per valutare shock di breve periodo (es. rincari energetici)      |
| `prc_hicp_mv12r` | HICP – **monthly data**, **12-month moving average** (media mobile dei tassi annui)   | Indicatore smussato, usato per monitoraggio macro più stabile     |



| Dataset          | Contiene valori assoluti in €? | Contiene un indice? | Contiene variazioni %? |
| ---------------- | ------------------------------ | ------------------- | ---------------------- |
| `prc_hicp_midx`  | ❌ No                           | ✅ Sì                | ❌ No                   |
| `prc_hicp_manr`  | ❌ No                           | ❌ No                | ✅ Sì (annuo)           |
| `prc_hicp_mmor`  | ❌ No                           | ❌ No                | ✅ Sì (mensile)         |
| `prc_hicp_mv12r` | ❌ No                           | ❌ No                | ✅ Sì (media 12 mesi)   |


### Quale scegliere

- Per **l’inflazione "ufficiale"** → `prc_hicp_manr`
- Per **analisi stagionali e dinamiche brevi** → `prc_hicp_mmor` 
- Per **confronti storici o tra paesi (a parità di base)** → `prc_hicp_midx`
- Per **trend macroeconomici filtrati dalla volatilità** → `prc_hicp_mv12r`

I 4 dataset (`prc_hicp_manr`, `prc_hicp_midx`, `prc_hicp_mmor`, `prc_hicp_mv12r`) contengono **gli stessi punti osservati**, ovvero:

- **Stesso asse temporale** (ad esempio tutti i mesi dal 1996 a oggi),
- **Stessa classificazione COICOP** (es. `CP00` per All-items, `CP01` per Food, ecc.),
- **Stessa area geografica** (`geo=IT`, `FR`, `EU`, ecc.),
- **Stesse dimensioni di aggregazione** (come `unit=PC_CHG`, ecc. se presenti),
    
ma ognuno **trasforma il dato base** (l’indice dei prezzi) in una **vista diversa**:
- Livello indice → `midx`
- Var. % annuale → `manr`
- Var. % mensile → `mmor`
- Media mobile → `mv12r`

È come osservare **la stessa curva dei prezzi**, ma attraverso **4 lenti diverse**:
- **`midx`** ti mostra la curva assoluta;
- **`manr`** ti dice quanto è cambiata rispetto all'anno scorso;
- **`mmor`** rispetto al mese scorso;
- **`mv12r`** ti fa vedere una versione "smussata" della `manr`.



### Differenza tra `TEICP000` e `prc_hicp_manr`

|Caratteristica|`TEICP000`|`prc_hicp_manr`|
|---|---|---|
|Dettaglio COICOP|❌ Solo `CP00`|✅ Tutte le voci (es. `CP01`, `CP02`, …)|
|Frequenza|✅ Annual rate (%)|✅ Annual rate (%)|
|Periodicità|✅ Mensile|✅ Mensile|
|Livello di dettaglio|❌ Ridotto (overview)|✅ Completo (dati granulari)|
|URL API|`/data/teicp000`|`/data/prc_hicp_manr`|


### Analisi prc_hicp_manr
- Chiavi: dict_keys(['version', 'class', 'label', 'source', 'updated', 'value', 'status', 'id', 'size', 'dimension', 'extension']) 
- Dimensioni disponibili: dict_keys(['freq', 'unit', 'coicop', 'geo', 'time'])
- Numero di valori: 3.381.206
- freq (1):   M: Monthly
- unit (1):  RCH_A: Annual rate of change
- coicop (467):  AP: Administered prices | APF: Fully administered prices | APM: Mainly administered prices | AP_NNRG: Administered prices, non-energy | AP_NRG: Administered prices, energy | CP00: All-items HICP | CP01: Food and non-alcoholic beverages | CP011: Food | CP0111: Bread and cereals | CP01111: Rice | CP01112: Flours and other cereals | CP01113: Bread | CP01114: Other bakery products | CP01115: Pizza and quiche | CP01116: Pasta products and couscous | CP01117: Breakfast cereals | ......
  AL: Albania | AT: Austria | BE: Belgium | BG: Bulgaria | CH: Switzerland |...
- time (341): mensilmente, dal  1997-01 al 2025-05

per l'elenco completo di **geo** e **coicop** vedi csv 


### Analisi prc_hicp_midx

- freq: 1 items 
- unit: 3 items 
- coicop: 468 items 
- geo: 45 items
- time: 353 items
- I05: Index, 2005=100
- I15: Index, 2015=100
- I96: Index, 1996=100

#### esempio



## [DB Nomics - Prices](https://db.nomics.world/Eurostat)


- [[PRC_​HICP_​APC] HICP - administered prices (composition)](https://db.nomics.world/Eurostat/PRC_HICP_APC)
    - [[PRC_​HICP_​CANN] HICP at constant tax rates - monthly data (annual rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_CANN)
    - [[PRC_​HICP_​CIND] HICP at constant tax rates - monthly data (index)](https://db.nomics.world/Eurostat/PRC_HICP_CIND)
    - [[PRC_​HICP_​CMON] HICP at constant tax rates - monthly data (monthly rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_CMON)
- [prc_hicp__] -----
    - [[PRC_​HICP_​COW] HICP - country weights](https://db.nomics.world/Eurostat/PRC_HICP_COW)
    - [[PRC_​HICP_​INW] HICP - item weights](https://db.nomics.world/Eurostat/PRC_HICP_INW)
- [[PRC_​HICP_​AIND] HICP - annual data (average index and rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_AIND)
- [[PRC_​HICP_​CTRB] HICP - contributions to EA annual inflation (in percentage points)](https://db.nomics.world/Eurostat/PRC_HICP_CTRB)
- [[PRC_​HICP_​FP] HICP - first published data (monthly index and annual rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_FP)
- [[PRC_​HICP_​MANR] HICP - monthly data (annual rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_MANR)
- [[PRC_​HICP_​MIDX] HICP - monthly data (index)](https://db.nomics.world/Eurostat/PRC_HICP_MIDX)
- [[PRC_​HICP_​MMOR] HICP - monthly data (monthly rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_MMOR)
- [[PRC_​HICP_​MV12R] HICP - monthly data (12-month average rate of change)](https://db.nomics.world/Eurostat/PRC_HICP_MV12R)

![Pasted image 20250613122728](./media/Pasted%20image%2020250613122728.png)

./

## Riferimenti

- [Prezzi al consumo armonizzati per i paesi dell'Unione europea](Github/README.md)
- [IPCA](Github/README.md)
- [Eurostat - IPCA - tutti gli articoli](https://ec.europa.eu/eurostat/databrowser/product/page/teicp000)

[^1]: https://it.wikipedia.org/wiki/Indice_dei_prezzi_al_consumo
