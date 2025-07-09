# Nama VS Namq

https://ec.europa.eu/eurostat/databrowser/explore/all/economy?lang=en


![](Pasted%20image%2020250708134149.png)

I dataset  [[nama]] (annuali) e [[namq]] (trimestrali) di [[Eurostat]] condividono la logica economica e molte dimensioni
ma hanno strutture tecniche leggermente diverse
pensate per usi distinti.


## 1. Differenze principali tra `nama` e `namq`

|Caratteristica|`nama_` (annuale)|`namq_` (trimestrale)|
|---|---|---|
|Frequenza|Annuale (`A`)|Trimestrale (`Q`)|
|Dimensione `s_adj` (stagionalità)|❌ Non presente|✅ Presente: `SCA`
`SA`
`NSA`
`WDA`|
|Copertura temporale|1995–ultimo anno|1995Q1–ultimo trimestre|
|Dettaglio geografico|Nazioni (EU
EA
Paesi membri)|Nazioni|
|Dettaglio NACE/COFOG|Disponibile in alcuni sotto-dataset|Limitato o assente|
|Dataset tipico|`nama_10_gdp`
`nama_10r_2gfcf`|`namq_10_gdp`
`namq_10_a10`|
|Variabili (`na_item`)|Piena copertura: `B1GQ`
`P3`
`P51G`
...|Più limitata (focalizzata sul PIL e pochi altri)|

## 2. Dimensioni comuni (in entrambi)

Sia `nama` che `namq` possono includere:

- `na_item`: voce contabile (es. PIL
investimenti)
    
- `unit`: unità di misura (`CLV_I10`
`MIO_EUR`
ecc.)
    
- `geo`: paese
    
- `time`: anno o trimestre
    

## Esempio pratico

|Dataset|Frequenza|Voce contabile (na_item)|Unità|Stagionalità|
|---|---|---|---|---|
|`nama_10_gdp`|Annuale|`P51G`
`P3`
`B1GQ`
...|`CLV_I10`|❌ no|
|`namq_10_gdp`|Trimestrale|`B1GQ`
`P3`
`P6`
...|`CLV_I10`
`CP_MEUR`|✅ sì (SA
NSA...)|

## In sintesi

- ✅ Struttura simile
ma:
    
    - `namq_` ha stagionalità (`s_adj`) e frequenza trimestrale
        
    - `nama_` ha più voci disponibili
ma solo annuali
        
- 📈 Usa `namq_` per analisi di breve periodo
cicli e trend infra-annuali
    
- 🧮 Usa `nama_` per confronti strutturali
tendenze di lungo periodo
PIL potenziale
etc.
    
- 
- https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_2gfcf?geo=ITH4

|annuale        |trimestrale   |  territoriale  |  titolo                                                                                                 |
|---------------|--------------|----------------|---------------------------------------------------------------------------------------------------------|
|nama_10_a10    |namq_10_a10   |                |Valore aggiunto lordo e reddito per branca di attività economica principale (NACE Rev.2)                 |
|nama_10_a10_e  |namq_10_a10_e |                |Occupazione per settore principale (NACE Rev.2) - conti nazionali                                        |
|nama_10_a64    |              |                |Valore aggiunto lordo e reddito per settore di attività economica (NACE Rev.2)                           |
|nama_10_a64_e  |              |                |Occupazione per settore di attività economica (NACE Rev.2) - conti nazionali                             |
|nama_10_a64_p5 |              |                |                                                                                                         |
|nama_10_an6    |namq_10_an6   |                |                                                                                                         |
|nama_10_co3_p3 |              |                |                                                                                                         |
|nama_10_cp18   |              |                |                                                                                                         |
|nama_10_cp_a21 |              |                |                                                                                                         |
|nama_10_e_p    |namq_10_e_p   |                |                                                                                                         |
|nama_10_exi    |namq_10_exi   |                |                                                                                                         |
|nama_10_fcs    |namq_10_fcs   |                |                                                                                                         |
|nama_10_fte    |              |                |                                                                                                         |
|nama_10_gdp    |namq_10_gdp   |                |Prodotto interno lordo (PIL) e principali componenti (produzione, spesa e reddito)                       |
|nama_10_hfc    |              |                |                                                                                                         |
|nama_10r_lp    |              |                |                                                                                                         |
|nama_10_lp_a21 |              |                |                                                                                                         |
|nama_10_lp_ulc |namq_10_lp_ulc|                |Produttività del lavoro e costi unitari del lavoro                                                       |
|nama_10_lpc    |              |                |                                                                                                         |
|               |namq_10_lp_cf |                |                                                                                                         |
|nama_10_nfa    |              |                |                                                                                                         |
|nama_10_nfa_bs |              |                |                                                                                                         |
|nama_10_nfa_st |              |                |                                                                                                         |
|nama_10_pc     |namq_10_pc    |                |Prodotto interno lordo (PIL) e principali componenti pro capite                                          |
|nama_10_pe     |namq_10_pe    |                |Popolazione e occupazione - conti nazionali                                                              |
|nama_10_pp     |              |                |Reddito nazionale lordo (RNL) pro capite                                                                 |
|nama_10r_2coe  |              |                |Retribuzione dei dipendenti per regione NUTS                                                             |
|nama_10r_2emhrw|              |                |Occupazione (migliaia di ore lavorate) per regione NUTS                                                  |
|nama_10r_2gdp  |              |nama_10r_3gdp   |Prodotto interno lordo (PIL) ai prezzi correnti di mercato per regione NUTS                              |
|nama_10r_2gfcf |              |                |Formazione lorda di capitale fisso per regione NUTS 2 per l'economia totale e la pubblica amministrazione|
|nama_10r_2gvagr|              |                |Prodotto interno lordo (PIL) e valore aggiunto lordo (VAL) in volume per regione NUTS                    |
|nama_10r_2hhinc|              |                |                                                                                                         |
|nama_10r_2lp10 |              |                |                                                                                                         |
|nama_10r_2nlp  |              |                |Produttività nominale del lavoro per regione NUTS 2                                                      |
|nama_10r_2rlp  |              |                |Produttività reale del lavoro per regione NUTS 2                                                         |
|               |              |nama_10r_3empers|Occupazione (migliaia di persone) per regione NUTS 3                                                     |
|               |              |nama_10r_3gva   |Valore aggiunto lordo ai prezzi base per regione NUTS 3                                                  |
|               |              |nama_10r_3nlp   |Produttività nominale del lavoro per regione NUTS 3                                                      |
|               |              |nama_10r_3popgdp|Popolazione media annua per calcolare i dati del PIL regionale (migliaia di persone) per regione NUTS 3  |
















