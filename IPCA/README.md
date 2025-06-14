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

Questi sono **indici sintetici**: se HICP = 104,3 nel 2020-01, significa che i prezzi sono cresciuti del 4,3% rispetto al valore medio del **2015** (che vale 100, perché è l'anno base dell’indice).


## Definizioni

- IPCA: indice armonizzato dei prezzi al consumo per i Paesi dell’Unione europea. 
- IPCA-AS: indici armonizzati dei prezzi al consumo per aggregati speciali sono indicatori costruiti secondo uno schema classificatorio diverso dalla ECOICOP-IPCA e da quello utilizzato per gli indici NIC per tipologia di prodotto. La struttura di classificazione e le procedure di calcolo sono comuni a quelle utilizzate da Eurostat e ne condividono le innovazioni di carattere metodologico. In particolare, dalla diffusione degli indici definitivi di gennaio 2019 cambia il metodo di calcolo degli aggregati speciali dell’IPCA che sono ottenuti aggregando gli indici delle sottoclassi della ECOICOP (in precedenza, per il computo di questi indicatori erano utilizzati gli indici delle classi). Per una migliore fruibilità dei nuovi indicatori, le serie degli aggregati speciali, secondo il nuovo schema, sono state ricostruite per il periodo gennaio 2017 - dicembre 2018 e sostituiscono, per l’intervallo temporale in questione, quelle precedentemente diffuse, basate sulla vecchia metodologia di calcolo. 
- IPCA-TC: indice armonizzato dei prezzi al consumo a tassazione costante per i Paesi dell’Unione europea


### prezzi assoluti (in euro)

- **OCSE** (solo alcune voci)
- **istat.it** → microdati IPCA su prodotti singoli,
- **Scanner data / database Nielsen / GfK** (a pagamento).


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

![Pasted image 20250613121026](media/Pasted%20image%2020250613121026.png)

![Pasted image 20250613120925](media/Pasted%20image%2020250613120925.png)

![Pasted image 20250613120839](media/Pasted%20image%2020250613120839.png)

![Pasted image 20250613120819](media/Pasted%20image%2020250613120819.png)


![Pasted image 20250613120406](media/Pasted%20image%2020250613120406.png)


## ICPA e Banca d'Italia

### [Banca d’Italia. (2025). _EIB-L’economia italiana in breve](https://www.bancaditalia.it/pubblicazioni/economia-italiana-in-breve/index.html)


![Pasted image 20250613115258](media/Pasted%20image%2020250613115258.png)

![Pasted image 20250613115309](media/Pasted%20image%2020250613115309.png)


### [Banca d’Italia. (2025). Proiezioni macroeconomiche per l’Italia](https://www.bancaditalia.it/pubblicazioni/proiezioni-macroeconomiche/)

![Pasted image 20250613115744](media/Pasted%20image%2020250613115744.png)
  
_(Banca d'Italia, 2025, p. 2) Proiezioni macroeconomiche per l’economia italiana (variazioni percentuali sull’anno precedente, salvo diversa indicazione). Fonte: elaborazioni su dati Banca d’Italia e Istat. Quadro previsivo per l'Italia basato sulle informazioni disponibili al 28 marzo (per la formulazione delle ipotesi tecniche) e al 2 aprile (per i dati congiunturali). (1) Per il PIL e le sue componenti, variazioni stimate su dati trimestrali destagionalizzati e corretti per il numero di giornate lavorative. Senza tale correzione il PIL crescerebbe dello 0,5 per cento nel 2025, dello 0,9 nel 2026 e dello 0,7 nel 2027. – (2) In percentuale del PIL. – (3) Medie annue, valori percentuali._


## Ufficio Parlamentare di Bilancio. (2025). Nota sulla congiuntura
[https://www.upbilancio.it](https://www.upbilancio.it)

![Pasted image 20250613121656](media/Pasted%20image%2020250613121656.png)


## Banca Intesa

![Pasted image 20250613123229](media/Pasted%20image%2020250613123229.png)


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

|**Sigla**|**Descrizione**|**Uso tipico**|
|---|---|---|
|`prc_hicp_manr`|HICP – **monthly data**, **annual rate of change** (tasso t/t-12)|Misura l’inflazione annua – **indice principale usato dalla BCE**|
|`prc_hicp_midx`|HICP – **monthly data**, **index** (livello dell’indice, base variabile es: 2015=100)|Analisi di lungo periodo e confronti tra paesi|
|`prc_hicp_mmor`|HICP – **monthly data**, **monthly rate of change** (var. % sul mese precedente)|Per valutare shock di breve periodo (es. rincari energetici)|
|`prc_hicp_mv12r`|HICP – **monthly data**, **12-month moving average** (media mobile dei tassi annui)|Indicatore smussato, usato per monitoraggio macro più stabile|



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
- coicop (467):
  AP: Administered prices | APF: Fully administered prices | APM: Mainly administered prices | AP_NNRG: Administered prices, non-energy | AP_NRG: Administered prices, energy | CP00: All-items HICP | CP01: Food and non-alcoholic beverages | CP011: Food | CP0111: Bread and cereals | CP01111: Rice | CP01112: Flours and other cereals | CP01113: Bread | CP01114: Other bakery products | CP01115: Pizza and quiche | CP01116: Pasta products and couscous | CP01117: Breakfast cereals | CP01118: Other cereal products | CP0112: Meat | CP01121: Beef and veal | CP01122: Pork | CP01123: Lamb and goat | CP01124: Poultry | CP01125: Other meats | CP01126: Edible offal | CP01127: Dried, salted or smoked meat | CP01128: Other meat preparations | CP0113: Fish and seafood | CP01131: Fresh or chilled fish | CP01132: Frozen fish | CP01133: Fresh or chilled seafood | CP01134: Frozen seafood | CP01135: Dried, smoked or salted fish and seafood | CP01136: Other preserved or processed fish and seafood and fish and seafood preparations | CP0114: Milk, cheese and eggs | CP01141: Fresh whole milk | CP01142: Fresh low fat milk | CP01143: Preserved milk | CP01144: Yoghurt | CP01145: Cheese and curd | CP01146: Other milk products | CP01147: Eggs | CP0115: Oils and fats | CP01151: Butter | CP01152: Margarine and other vegetable fats | CP01153: Olive oil | CP01154: Other edible oils | CP01155: Other edible animal fats | CP0116: Fruit | CP01161: Fresh or chilled fruit | CP01162: Frozen fruit | CP01163: Dried fruit and nuts | CP01164: Preserved fruit and fruit-based products | CP0117: Vegetables | CP01171: Fresh or chilled vegetables other than potatoes and other tubers | CP01172: Frozen vegetables other than potatoes and other tubers | CP01173: Dried vegetables, other preserved or processed vegetables | CP01174: Potatoes | CP01175: Crisps | CP01176: Other tubers and products of tuber vegetables | CP0118: Sugar, jam, honey, chocolate and confectionery | CP01181: Sugar | CP01182: Jams, marmalades and honey | CP01183: Chocolate | CP01184: Confectionery products | CP01185: Edible ices and ice cream | CP01186: Artificial sugar substitutes | CP0119: Food products n.e.c. | CP01191: Sauces, condiments | CP01192: Salt, spices and culinary herbs | CP01193: Baby food | CP01194: Ready-made meals | CP01199: Other food products n.e.c. | CP012: Non-alcoholic beverages | CP0121: Coffee, tea and cocoa | CP01211: Coffee | CP01212: Tea | CP01213: Cocoa and powdered chocolate | CP0122: Mineral waters, soft drinks, fruit and vegetable juices | CP01221: Mineral or spring waters | CP01222: Soft drinks | CP01223: Fruit and vegetables juices | CP02: Alcoholic beverages, tobacco and narcotics | CP021: Alcoholic beverages | CP0211: Spirits | CP02111: Spirits and liqueurs | CP02112: Alcoholic soft drinks | CP0212: Wine | CP02121: Wine from grapes | CP02122: Wine from other fruits | CP02123: Fortified wines | CP02124: Wine-based drinks | CP0213: Beer | CP02131: Lager beer | CP02132: Other alcoholic beer | CP02133: Low and non-alcoholic beer | CP02134: Beer-based drinks | CP022: Tobacco | CP02201: Cigarettes | CP02202: Cigars | CP02203: Other tobacco products | CP03: Clothing and footwear | CP031: Clothing | CP0311: Clothing materials | CP0312: Garments | CP03121: Garments for men | CP03122: Garments for women | CP03123: Garments for infants (0 to 2 years) and children (3 to 13 years) | CP0313: Other articles of clothing and clothing accessories | CP03131: Other articles of clothing | CP03132: Clothing accessories | CP0314: Cleaning, repair and hire of clothing | CP03141: Cleaning of clothing | CP03142: Repair and hire of clothing | CP032: Footwear | CP0321: Shoes and other footwear | CP03211: Footwear for men | CP03212: Footwear for women | CP03213: Footwear for infants and children | CP0322: Repair and hire of footwear | CP04: Housing, water, electricity, gas and other fuels | CP041: Actual rentals for housing | CP0411: Actual rentals paid by tenants | CP0412: Other actual rentals | CP04121: Actual rentals paid by tenants for secondary residences | CP04122: Garage rentals and other rentals paid by tenants | CP043: Maintenance and repair of the dwelling | CP0431: Materials for the maintenance and repair of the dwelling | CP0432: Services for the maintenance and repair of the dwelling | CP04321: Services of plumbers | CP04322: Services of electricians | CP04323: Maintenance services for heating systems | CP04324: Services of painters | CP04325: Services of carpenters | CP04329: Other services for maintenance and repair of the dwelling | CP044: Water supply and miscellaneous services relating to the dwelling | CP0441: Water supply | CP0442: Refuse collection | CP0443: Sewerage collection | CP0444: Other services relating to the dwelling n.e.c. | CP04441: Maintenance charges in multi-occupied buildings | CP04442: Security services | CP04449: Other services related to dwelling | CP045: Electricity, gas and other fuels | CP0451: Electricity | CP0452: Gas | CP04521: Natural gas and town gas | CP04522: Liquefied hydrocarbons (butane, propane, etc.) | CP0453: Liquid fuels | CP0454: Solid fuels | CP04541: Coal | CP04549: Other solid fuels | CP0455: Heat energy | CP05: Furnishings, household equipment and routine household maintenance | CP051: Furniture and furnishings, carpets and other floor coverings | CP0511: Furniture and furnishings | CP05111: Household furniture | CP05112: Garden furniture | CP05113: Lighting equipment | CP05119: Other furniture and furnishings | CP0512: Carpets and other floor coverings | CP05121: Carpet and rugs | CP05122: Other floor coverings | CP05123: Services of laying of fitted carpets and floor coverings | CP0513: Repair of furniture, furnishings and floor coverings | CP052: Household textiles | CP05201: Furnishings fabrics and curtains | CP05202: Bed linen | CP05203: Table linen and bathroom linen | CP05204: Repair of household textiles | CP05209: Other household textiles | CP053: Household appliances | CP0531: Major household appliances whether electric or not | CP05311: Refrigerators, freezers and fridge-freezers | CP05312: Clothes washing machines, clothes drying machines and dish washing machines | CP05313: Cookers | CP05314: Heaters, air conditioners | CP05315: Cleaning equipment | CP05319: Other major household appliances | CP0531_0532: Major household appliances whether electric or not and small electric household appliances | CP0532: Small electric household appliances | CP05321: Food processing appliances | CP05322: Coffee machines, tea-makers and similar appliances | CP05323: Irons | CP05324: Toasters and grills | CP05329: Other small electric household appliances | CP0533: Repair of household appliances | CP054: Glassware, tableware and household utensils | CP05401: Glassware, crystal-ware, ceramic ware and chinaware | CP05402: Cutlery, flatware and silverware | CP05403: Non-electric kitchen utensils and articles | CP05404: Repair of glassware, tableware and household utensils | CP055: Tools and equipment for house and garden | CP0551: Major tools and equipment | CP05511: Motorized major tools and equipment | CP05512: Repair, leasing and rental of major tools and equipment | CP0552: Small tools and miscellaneous accessories | CP05521: Non-motorised small tools | CP05522: Miscellaneous small tool accessories | CP05523: Repair of non-motorised small tools and miscellaneous accessories | CP056: Goods and services for routine household maintenance | CP0561: Non-durable household goods | CP05611: Cleaning and maintenance products | CP05612: Other non-durable small household articles | CP0562: Domestic services and household services | CP05621: Domestic services by paid staff | CP05622: Cleaning services | CP05623: Hire of furniture and furnishings | CP05629: Other domestic services and household services | CP06: Health | CP061: Medical products, appliances and equipment | CP0611: Pharmaceutical products | CP0612: Other medical products | CP06121: Pregnancy tests and mechanical contraceptive devices | CP06129: Other medical products n.e.c. | CP0612_0613: Other medical products, therapeutic appliances and equipment | CP0613: Therapeutic appliances and equipment | CP06131: Corrective eye-glasses and contact lenses | CP06132: Hearing aids | CP06133: Repair of therapeutic appliances and equipment | CP06139: Other therapeutic appliances and equipment | CP062: Out-patient services | CP0621: Medical services | CP06211: General practice | CP06212: Specialist practice | CP0621_0623: Medical services and paramedical services | CP0622: Dental services | CP0623: Paramedical services | CP06231: Services of medical analysis laboratories and X-ray centres | CP06232: Thermal-baths, corrective-gymnastic therapy, ambulance and hire of therapeutic equipment | CP06239: Other paramedical services | CP063: Hospital services | CP07: Transport | CP071: Purchase of vehicles | CP0711: Motor cars | CP07111: New motor cars | CP07112: Second-hand motor cars | CP0712: Motor cycles | CP0712-0714: Motor cycles, bicycles and animal drawn vehicles | CP0713: Bicycles | CP072: Operation of personal transport equipment | CP0721: Spare parts and accessories for personal transport equipment | CP07211: Tyres | CP07212: Spare parts for personal transport equipment | CP07213: Accessories for personal transport equipment | CP0722: Fuels and lubricants for personal transport equipment | CP07221: Diesel | CP07222: Petrol | CP07223: Other fuels for personal transport equipment | CP07224: Lubricants | CP0723: Maintenance and repair of personal transport equipment | CP0724: Other services in respect of personal transport equipment | CP07241: Hire of garages, parking spaces and personal transport equipment | CP07242: Toll facilities and parking meters | CP07243: Driving lessons, tests, licences and road worthiness tests | CP073: Transport services | CP0731: Passenger transport by railway | CP07311: Passenger transport by train | CP07312: Passenger transport by underground and tram | CP0732: Passenger transport by road | CP07321: Passenger transport by bus and coach | CP07322: Passenger transport by taxi and hired car with driver | CP0733: Passenger transport by air | CP07331: Domestic flights | CP07332: International flights | CP0734: Passenger transport by sea and inland waterway | CP07341: Passenger transport by sea | CP07342: Passenger transport by inland waterway | CP0735: Combined passenger transport | CP0736: Other purchased transport services | CP07361: Funicular, cable-car and chair-lift transport | CP07362: Removal and storage services | CP07369: Other purchased transport services n.e.c. | CP08: Communications | CP081: Postal services | CP08101: Letter handling services | CP08109: Other postal services | CP0820: Telephone and telefax equipment | CP08201: Fixed telephone equipment | CP08202: Mobile telephone equipment | CP08203: Other equipment of telephone and telefax equipment | CP08204: Repair of telephone or telefax equipment | CP082_083: Telephone and telefax equipment and services | CP0830: Telephone and telefax services | CP08301: Wired telephone services | CP08302: Wireless telephone services | CP08303: Internet access provision services | CP08304: Bundled telecommunication services | CP08305: Other information transmission services | CP09: Recreation and culture | CP091: Audio-visual, photographic and information processing equipment | CP0911: Equipment for the reception, recording and reproduction of sound and picture | CP09111: Equipment for the reception, recording and reproduction of sound | CP09112: Equipment for the reception, recording and reproduction of sound and vision | CP09113: Portable sound and vision devices | CP09119: Other equipment for the reception, recording and reproduction of sound and picture | CP0912: Photographic and cinematographic equipment and optical instruments | CP09121: Cameras | CP09122: Accessories for photographic and cinematographic equipment | CP09123: Optical instruments | CP0913: Information processing equipment | CP09131: Personal computers | CP09132: Accessories for information processing equipment | CP09133: Software | CP09134: Calculators and other information processing equipment | CP0914: Recording media | CP09141: Pre-recorded recording media | CP09142: Unrecorded recording media | CP09149: Other recording media | CP0915: Repair of audio-visual, photographic and information processing equipment | CP092: Other major durables for recreation and culture | CP0921: Major durables for outdoor recreation | CP09211: Camper vans, caravans and trailers | CP09212: Aeroplanes, microlight aircraft, gliders, hang-gliders and hot-air balloons | CP09213: Boats, outboard motors and fitting out of boats | CP09214: Horses, ponies and accessories | CP09215: Major items for games and sport | CP0921_0922: Major durables for indoor and outdoor recreation including musical instruments | CP0922: Musical instruments and major durables for indoor recreation | CP09221: Musical instruments | CP09222: Major durables for indoor recreation | CP0923: Maintenance and repair of other major durables for recreation and culture | CP093: Other recreational items and equipment, gardens and pets | CP0931: Games, toys and hobbies | CP09311: Games and hobbies | CP09312: Toys and celebration articles | CP0932: Equipment for sport, camping and open-air recreation | CP09321: Equipment for sport | CP09322: Equipment for camping and open-air recreation | CP09323: Repair of equipment for sport, camping and open-air recreation | CP0933: Gardens, plants and flowers | CP09331: Garden products | CP09332: Plants and flowers | CP0934: Pets and related products | CP09341: Purchase of pets | CP09342: Products for pets | CP0934_0935: Pets and related products; veterinary and other services for pets | CP0935: Veterinary and other services for pets | CP094: Recreational and cultural services | CP0941: Recreational and sporting services | CP09411: Recreational and sporting services - attendance | CP09412: Recreational and sporting services - participation | CP0942: Cultural services | CP09421: Cinemas, theatres, concerts | CP09422: Museums, libraries, zoological gardens | CP09423: Television and radio licence fees, subscriptions | CP09424: Hire of equipment and accessories for culture | CP09425: Photographic services | CP09429: Other cultural services | CP095: Newspapers, books and stationery | CP0951: Books | CP09511: Fiction books | CP09512: Educational text books | CP09513: Other non-fiction books | CP09514: Binding services and E-book downloads | CP0952: Newspapers and periodicals | CP09521: Newspapers | CP09522: Magazines and periodicals | CP0953: Miscellaneous printed matter | CP0953_0954: Miscellaneous printed matter; stationery and drawing materials | CP0954: Stationery and drawing materials | CP09541: Paper products | CP09549: Other stationery and drawing materials | CP096: Package holidays | CP09601: Package domestic holidays | CP09602: Package international holidays | CP10: Education | CP101: Pre-primary and primary education | CP10101: Pre-primary education | CP10102: Primary education | CP102: Secondary education | CP103: Post-secondary non-tertiary education | CP104: Tertiary education | CP105: Education not definable by level | CP11: Restaurants and hotels | CP111: Catering services | CP1111: Restaurants, cafés and the like | CP11111: Restaurants, cafés and dancing establishments | CP11112: Fast food and take away food services | CP1112: Canteens | CP112: Accommodation services | CP11201: Hotels, motels, inns and similar accommodation services | CP11202: Holiday centres, camping sites, youth hostels and similar accommodation services | CP11203: Accommodation services of other establishments | CP12: Miscellaneous goods and services | CP121: Personal care | CP1211: Hairdressing salons and personal grooming establishments | CP12111: Hairdressing for men and children | CP12112: Hairdressing for women | CP12113: Personal grooming treatments | CP1212: Electrical appliances for personal care | CP12121: Electric appliances for personal care | CP12122: Repair of electric appliances for personal care | CP1212_1213: Electrical appliances for personal care; other appliances, articles and products for personal care | CP1213: Other appliances, articles and products for personal care | CP12131: Non-electrical appliances | CP12132: Articles for personal hygiene and wellness, esoteric products and beauty products | CP123: Personal effects n.e.c. | CP1231: Jewellery, clocks and watches | CP12311: Jewellery | CP12312: Clocks and watches | CP12313: Repair of jewellery, clocks and watches | CP1232: Other personal effects | CP12321: Travel goods | CP12322: Articles for babies | CP12323: Repair of other personal effects | CP12329: Other personal effects n.e.c. | CP124: Social protection | CP12401: Child care services | CP12402: Retirement homes for elderly persons and residences for disabled persons | CP12403: Services to maintain people in their private homes | CP12404: Counselling | CP125: Insurance | CP1252: Insurance connected with the dwelling | CP1253: Insurance connected with health | CP12532: Private insurance connected with health | CP1254: Insurance connected with transport | CP12541: Motor vehicle insurance | CP12542: Travel insurance | CP1255: Other insurance | CP126: Financial services n.e.c. | CP12621: Charges by banks and post offices | CP12622: Fees and service charges of brokers, investment counsellors | CP127: Other services n.e.c. | CP12701: Administrative fees | CP12702: Legal services and accountancy | CP12703: Funeral services | CP12704: Other fees and services | EDUC_HLTH_SPR: Education, health and social protection | ELC_GAS: Electricity, gas, solid fuels and heat energy | FOOD: Food including alcohol and tobacco | FOOD_NP: Unprocessed food | FOOD_P: Processed food including alcohol and tobacco | FOOD_P_X_ALC_TBC: Processed food excluding alcohol and tobacco | FOOD_S: Seasonal food | FROOPP: Frequent out-of-pocket purchases | FUEL: Liquid fuels and fuels and lubricants for personal transport equipment | GD: Goods (overall index excluding services) | IGD: Industrial goods | IGD_NNRG: Non-energy industrial goods | IGD_NNRG_D: Non-energy industrial goods, durables only | IGD_NNRG_ND: Non-energy industrial goods, non-durables only | IGD_NNRG_SD: Non-energy industrial goods, semi-durables only | NRG: Energy | NRG_FOOD_NP: Energy and unprocessed food | NRG_FOOD_S: Energy and seasonal food | SERV: Services (overall index excluding goods) | SERV_COM: Services related to communication | SERV_HOUS: Services related to housing | SERV_MSC: Services - miscellaneous | SERV_REC: Services related to recreation, including repairs and personal care | SERV_REC_HOA: Services related to package holidays and accommodation | SERV_REC_X_HOA: Services related to recreation and personal care, excluding package holidays and accommodation | SERV_TRA: Services related to transport | TOT_X_ALC_TBC: Overall index excluding alcohol and tobacco | TOT_X_AP: Overall index excluding administered prices | TOT_X_APF: Overall index excluding fully administered prices | TOT_X_APM: Overall index excluding mainly administered prices | TOT_X_EDUC_HLTH_SPR: Overall index excluding education, health and social protection | TOT_X_FOOD_S: Overall index excluding seasonal food | TOT_X_FROOPP: Overall index excluding frequent out-of-pocket purchases | TOT_X_FUEL: Overall index excluding liquid fuels and lubricants for personal transport equipment | TOT_X_HOUS: Overall index excluding housing, water, electricity, gas and other fuels | TOT_X_NRG: Overall index excluding energy | TOT_X_NRG_FOOD: Overall index excluding energy, food, alcohol and tobacco | TOT_X_NRG_FOOD_NP: Overall index excluding energy and unprocessed food | TOT_X_NRG_FOOD_S: Overall index excluding energy and seasonal food | TOT_X_TBC: Overall index excluding tobacco
- geo (45):
  AL: Albania | AT: Austria | BE: Belgium | BG: Bulgaria | CH: Switzerland | CY: Cyprus | CZ: Czechia | DE: Germany | DK: Denmark | EA: Euro area (EA11-1999, EA12-2001, EA13-2007, EA15-2008, EA16-2009, EA17-2011, EA18-2014, EA19-2015, EA20-2023) | EA19: Euro area - 19 countries  (2015-2022) | EA20: Euro area – 20 countries (from 2023) | EE: Estonia | EEA: European Economic Area (EEA18-1995, EEA28-2004, EEA30-2007, EEA31-2013, EEA30-2020) | EL: Greece | ES: Spain | EU: European Union (EU6-1958, EU9-1973, EU10-1981, EU12-1986, EU15-1995, EU25-2004, EU27-2007, EU28-2013, EU27-2020) | EU27_2020: European Union - 27 countries (from 2020) | EU28: European Union - 28 countries (2013-2020) | FI: Finland | FR: France | HR: Croatia | HU: Hungary | IE: Ireland | IS: Iceland | IT: Italy | LT: Lithuania | LU: Luxembourg | LV: Latvia | ME: Montenegro | MK: North Macedonia | MT: Malta | NL: Netherlands | NO: Norway | PL: Poland | PT: Portugal | RO: Romania | RS: Serbia | SE: Sweden | SI: Slovenia | SK: Slovakia | TR: Türkiye | UK: United Kingdom | US: United States | XK: Kosovo*
- time (341): mensilmente, dal  1997-01 al 2025-05



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

![Pasted image 20250613122728](media/Pasted%20image%2020250613122728.png)


## Riferimenti

- [Prezzi al consumo armonizzati per i paesi dell'Unione europea](Github/IPCA/README.md)
- [IPCA](Github/IPCA/README.md)
- [Eurostat - IPCA - tutti gli articoli](https://ec.europa.eu/eurostat/databrowser/product/page/teicp000)

[^1]: https://it.wikipedia.org/wiki/Indice_dei_prezzi_al_consumo
