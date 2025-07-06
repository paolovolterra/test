I dati dell'immagine provengono da **ISTAT** e riguardano **l’indice della produzione industriale** #IPI, corretto per gli effetti di calendario, con base 2021=100, aggiornato ad **aprile 2025**.  
I valori sono espressi per ramo di attività economica secondo la classificazione ATECO.


![|500](media/Pasted%20image%2020250705075131.png)

immagine estratta da _Luigi dell’Olio. 2025. «Innovazione e distretti Le eccellenze nascoste del made in Italy». la Repubblica Affari & Finanza, 7 luglio 2025_


La selezione dei settori **non si basa sui codici ATECO/NACE "più rilevanti" in termini strutturali**, ma su quelli che hanno mostrato i maggiori scostamenti (variazioni) ad aprile 2025, sia in positivo che in negativo

## come è stata costruita la selezione

- Mostrare **i settori con variazioni estreme**, positive o negative, **rispetto alla media (indice generale = +0,3%)**
    
- Evidenziare in rosso i settori in calo
    
- Dare visibilità a quelli in crescita (grigi), ma meno accentuata
    

|Settore visualizzato|Probabile codice NACE (ATECO)|Note|
|---|---|---|
|Industria legno, carta e stampa|`C16-C18`|+4,7%|
|Fornitura energia, gas, vapore, aria|`D35`|+4,3%|
|Computer, elettronica|`C26`|+3,3%|
|Alimentari, bevande, tabacco|`C10-C12`|+3,2%|
|**Prodotti farmaceutici di base e preparati**|`C21`|**−11,0%**|
|**Fabbricazione di mezzi di trasporto**|`C29-C30`|−9,5%|
|**Coke e raffinati**|`C19`|−5,0%|

### Strategia di comunicazione

- Visualizza **alcuni macrosettori in positivo** (alimentari, energia, elettronica, estrattivo) per mostrare la tenuta dell’industria
    
- Evidenzia **settori con crisi marcata** (farmaceutico, auto, coke, apparecchiature) come warning economico
    
- Mostra anche settori in flessione leggera per dare **profondità** (es. tessile, -0,5%)
    

### Confronto con i codici "più rilevanti" (strutturalmente)

Se l’obiettivo fosse stato selezionare i settori:

- più **pesanti in valore aggiunto**
    
- o più **strategici per policy industriale (es. high-tech)**
    

allora avrebbero incluso:

- `C20_C21` → Chimica + farmaceutica
    
- `C26_C27` → Elettronica + apparecchi elettrici
    
- `C28` → Macchinari
    
- `C29_C30` → Auto, aerospazio
    
- `C10-C12` → Alimentari
    
- `C24_C25` → Metalli
    
###  In sintesi:

- La grafica non mostra "i più rilevanti in assoluto"  
- Ma "quelli che **hanno avuto scostamenti maggiori** a livello congiunturale"  
- Ottima per l’analisi **a breve termine** (es. shock settoriali, segnali d’allarme)  
- Per l’analisi **strutturale**, serve partire dai codici aggregati `C_HTC`, `C_LTC`, `MIG_*`, ecc.

---
# [[md/sts_inpr]]

**Eurostat** pubblica un indicatore del tutto analogo, chiamato: **Production in industry - monthly data 

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
        


