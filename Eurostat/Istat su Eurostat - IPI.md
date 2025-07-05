I dati dell'immagine provengono da **ISTAT** e riguardano **l’indice della produzione industriale** #IPI, corretto per gli effetti di calendario, con base 2021=100, aggiornato ad **aprile 2025**.  
I valori sono espressi per ramo di attività economica secondo la classificazione ATECO.


![|500](media/Pasted%20image%2020250705075131.png)

immagine estratta da _Luigi dell’Olio. 2025. «Innovazione e distretti Le eccellenze nascoste del made in Italy». la Repubblica Affari & Finanza, 7 luglio 2025_


**Eurostat** pubblica un indicatore del tutto analogo, chiamato:

> **Production in industry - monthly data (sts_inpr_m)**  
> [https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en](https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en)

Questo dataset contiene:

- Indici mensili della produzione industriale per settore (NACE Rev.2),
    
- Correzione per effetti di calendario e destagionalizzazione,
    
- Possibilità di filtrare per **Stato membro (es. Italia)**,
    
- Serie storiche con diverse basi (l’ultima disponibile è spesso base 2021=100).
    

### 🔍 Come trovare l’equivalente delle voci italiane?

Ecco alcuni esempi di corrispondenze tra i codici ATECO italiani (NACE Rev.2) e le voci nel dataset Eurostat:

|Descrizione (ISTAT)|NACE Rev.2|Eurostat voce|
|---|---|---|
|Industria legno, carta e stampa|C16, C17, C18|`Industry, excl. construction → Manufacture of wood and of products of wood and cork, paper, printing`|
|Fornitura di energia elettrica, gas, vapore e aria|D|`Electricity, gas, steam and air conditioning supply`|
|Computer, elettronica|C26|`Manufacture of computer, electronic and optical products`|
|Alimentari, bevande, tabacco|C10-C12|`Manufacture of food products, beverages and tobacco`|
|Attività estrattiva|B|`Mining and quarrying`|
|Prodotti chimici|C20|`Manufacture of chemicals and chemical products`|
|Prodotti farmaceutici di base e preparati|C21|`Manufacture of basic pharmaceutical products`|
|Mezzi di trasporto|C29, C30|`Manufacture of motor vehicles, trailers and other transport equipment`|
|Apparecchiature elettriche e non|C27, C28|`Manufacture of electrical equipment / machinery`|

### 📦 Dataset Eurostat specifico consigliato

- Codice: **STS_INPR_M**
    
- Link diretto: [https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en](https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en)
    
- Filtri consigliati:
    
    - **GEO = Italy**
        
    - **S_ADJ = Calendar adjusted data (CA)**
        
    - **UNIT = I15 (Index, 2021=100)**
        
    - **NACE_R2 = Seleziona i codici rilevanti (es. C20, C21, C26, ecc.)**
        
    - **FREQ = M (Monthly)**
        

Se vuoi, posso prepararti direttamente la query SDMX o lo script Python per scaricare i dati da Eurostat filtrati sulle stesse categorie. Vuoi procedere in questo modo?