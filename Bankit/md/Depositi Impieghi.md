# Prestiti e Depositi
Bankit - STAFINFRA Banche e istituzioni finanziarie: finanziamenti e raccolta per settori e territori
https://www.bancaditalia.it/pubblicazioni/finanziamenti-raccolta

## dati al 31-12-2023 Società non finanziarie e famiglie produttrici
- Prestiti  688.958
- Depositi  506.604


## legenda

### ENTE_SEGN	Ente segnalante

Codice	Descrizione
- 1070001	Banche e Cassa depositi e prestiti
- 1100010	Banche

### ATECO_CTP	Attività economica della controparte (ateco 2007)
- Codice	Descrizione
- 000000	Informazione non prevista o non applicabile
- **1004999	Totale ateco al netto della sez. U**
- 1005001	Attività industriali
- 1005003	Servizi
- 1005009	Totale ateco al netto della sez. U comprese le attività non produttive
- F	Costruzioni

### LOC_CTP	Localizzazione della controparte
https://en.wikipedia.org/wiki/NUTS_statistical_regions_of_Italy

- Codice	Descrizione
- IT	Italia
- ITC	Italia nord-occidentale
- ITC1	Piemonte
- ITC2	Valle d'Aosta/Vallée d'Aoste
- ITC3	Liguria
- ITC4	Lombardia

### SET_CTP	Settore istituzionale della controparte
- Codice	Descrizione
- 600	    Famiglie consumatrici
- S11	    Società non finanziarie
- S12BI7	Società finanziarie diverse da istituzioni finanziarie monetarie
- S13	    Amministrazioni pubbliche
- S14BI2	Famiglie produttrici (fino a 5 addetti)
- **SBI25	Società non finanziarie e famiglie produttrici**
- SBI33	    Società di persone, semplici, di fatto e ditte individuali con meno di 20 addetti
- SBI42   	Totale residenti al netto delle Istituzioni finanziarie monetarie (TOTALONE)


## Prestiti


### TFR20232 Prestiti per regione, settore e attività economica della clientela  
- LOC_CTP   IT
- ENTE_SEGN 1070001
- FENEC     52000700

| ATECO_CTP | SET_CTP | VALORE       |
| --------- | ------- | -----------: |
| 1005009   | SBI42   | 1710491022   |
| 1004999   | SBI25   | **689081386**| *************************************************
| 1004999   | S11     | 617890251    |
| 0         | 600     | 591775862    |
| 1005003   | SBI25   | 371922627    |
| 1005003   | S11     | 330486503    |
| 0         | S13     | 247159024    |
| 1005001   | SBI25   | 218031728    |
| 1005001   | S11     | 213691371    |
| 0         | S12BI7  | 175006323    |
| 1004999   | SBI33   | 111845973    |
| 1004999   | S14BI2  | 71191134     |
| F         | SBI25   | 59706516     |
| F         | S11     | 54515210     |

- TOTALE                                                               1710491022  SBI42
  - Amministrazioni pubbliche                                           247159024  S13
  - Società finanziarie (escluse le  Istituzioni finanziarie monetarie) 175006323  S12BI7
  - Società non finanziarie e  famiglie produttrici                     689081386  SBI25
    - Industria                                                         218031728  SBI25 1005001
    - Edilizia                                                           59706516  SBI25 F
    - Servizi                                                           371922627  SBI25 1005003
  - Famiglie consumatrici                                               591775862  600


### TFR20255 Prestiti per area geografica e attività economica della clientela
- ENTE_SEGN 1070001
- FENEC 52000700
- SET_CTP SBI25

| ATECO_CTP | VALORE        |
| --------- | ------------: |
| 1004999   | **689081386** |   *******************************************************
| C         | 188774671     |
| G         | 121514060     |
| F         | 59706516      |
| M         | 57664826      |
| L         | 57261630      |
| A         | 39420514      |
| 1000061   | 33507229      |
| I         | 32742248      |
| H         | 31536300      |
| 1000074   | 25667021      |
| 25        | 25344205      |
| 28        | 21161581      |
| J         | 20521135      |
| D         | 18838975      |
| N         | 18500199      |
| 1000062   | 15836751      |
| 1000055   | 14848524      |
| 1000065   | 12433322      |
| 1000060   | 11035739      |
| 24        | 10815171      |
| 22        | 9902976       |
| 61        | 9225949       |
| E         | 8663970       |
| 23        | 8036507       |
| 1000063   | 6606504       |
| K         | 6515209       |
| 27        | 6269743       |
| 26        | 5051370       |
| 31        | 4689652       |
| 19        | 3235396       |
| B         | 1754113       |



### TDB10226 Prestiti (esclusi PCT e sofferenze) per provincia e settore della clientela

DATA_OSS	ENTE_SEGN	FENEC	LOC_CTP	SET_CTP	VALORE
2023-12-31 00:00:00.000000	1070001	52000139	IT	SBI42	1642167419
2023-12-31 00:00:00.000000	1070001	52000139	IT	SBI33	108022985
2023-12-31 00:00:00.000000	1070001	52000139	IT	S11BI13	556896011
2023-12-31 00:00:00.000000	1070001	52000139	IT	SBI25	664918996   ***************************
2023-12-31 00:00:00.000000	1070001	52000139	IT	SBI28	590271509



### TFR10194 Prestiti (esclusi PCT), Depositi (esclusi PCT) e Sportelli							
_distribuzione per comune degli sportelli_

DATA_OSS	DIVISA1	DURORI	ENTE_SEGN	FENEC	LOC_SPORT	PRV_SPORT	RESIDENZA1	VALORE	STATUS
2023-12-31 00:00:00.000000	1000	9	1100010	1077778	9999997	IT	IT	1429501870	
2023-12-31 00:00:00.000000	1000	9	1100010	1041810	9999997	IT	IT	1546906651	
2023-12-31 00:00:00.000000	1000	9	1100010	30990009	9999997	IT	IT	20158	


## Depositi

### TDB20290 Depositi per provincia, settore e sottosettore della clientela
* SBI25 = S11 + S14BI2

| DATA_OSS   | ENTE_SEGN | FENEC    | LOC_CTP | SET_CTP | VALORE     |
| ---------- | --------- | -------- | ------- | ------- | ---------: |
| 31/12/2023 | 1070001   | 52000100 | IT      | SBI59   | 2041514321 |
| 31/12/2023 | 1070001   | 52000100 | IT      | S14     | 1206160106 |
| 31/12/2023 | 1070001   | 52000100 | IT      | 600     | 1123575292 |
| 31/12/2023 | 1070001   | 52000100 | IT      | S11     | 423988885  | *
| 31/12/2023 | 1070001   | 52000100 | IT      | S11BI32 | 369343251  |
| 31/12/2023 | 1070001   | 52000100 | IT      | S12BI7  | 316584500  |
| 31/12/2023 | 1070001   | 52000100 | IT      | S12BI66 | 239752388  |
| 31/12/2023 | 1070001   | 52000100 | IT      | S14BI2  | 82584814   | *
| 31/12/2023 | 1070001   | 52000100 | IT      | S13     | 52677186   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S15     | 35562957   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S1311   | 28513478   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S11001  | 23317873   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S126    | 21546672   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S124    | 21397417   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S11BI8  | 20191728   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S1313   | 17141056   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S127    | 13655207   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S128    | 13558125   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S11BI7  | 10207822   |
| 31/12/2023 | 1070001   | 52000100 | IT      | S1314   | 7022651    |
| 31/12/2023 | 1070001   | 52000100 | IT      | S129    | 6674690    |
| 31/12/2023 | 1070001   | 52000100 | IT      | SBI9    | 6534201    |
| 31/12/2023 | 1070001   | 52000100 | IT      | 450     | 928211     |