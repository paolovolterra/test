# IPCA - Indice dei Prezzi al Consumo Armonizzato

L'[[Github/Eurostat/IPCA/IPCA sts_inpp_m]] (Indice dei Prezzi al Consumo Armonizzato) è pensato per misurare l'inflazione percepita dalle famiglie consumatrici, ed è utilizzato principalmente per confronti internazionali tra paesi dell’UE.
Per monitorare i prezzi rilevanti per le imprese, esistono altri indici di prezzo specifici

### Prezzi alla produzione industriale

- Nome ISTAT/Eurostat: **PPI** – [[MD/Producer Price Index]]
- Codici Eurostat: `ppi` (es. **`sts_inpp_m`**)
- Descrizione: misura la variazione dei prezzi dei beni venduti dalle imprese manifatturiere, sia sul mercato interno che estero, al netto dell’IVA.
- Uso: **utile per monitorare la pressione sui margini, l’inflazione importata, l’evoluzione dei prezzi di cessione di beni industriali**.

### Indici dei prezzi all'importazione

- Nome ISTAT: Indice dei prezzi all'importazione dei prodotti industriali
- Codici Eurostat: **`ei_pric_im_m`** 
- Uso: rilevante per imprese che acquistano input produttivi dall’estero.

#### Indici dei prezzi dei beni intermedi (semilavorati)

- Rientrano nel PPI, ma in dettaglio si possono estrarre i sottogruppi relativi a:
    - CPA C.24 - C.25 - C.20 → metalli, chimica, materiali intermedi
        
- Oppure tramite:
    - COICOP/CPA per estrarre solo categorie di prodotti semilavorati
    - NACE Rev.2 per il dettaglio per settore produttivo
        
### Indice dei prezzi alla produzione nelle costruzioni

- Nome: Construction Cost Index (**CCI**)
- Codice: **`sts_copi_q`**
- Misura la variazione del costo per unità di output nel settore costruzioni (manodopera, materiali, ecc.)
    
### Indice dei prezzi al consumo per usi intermedi

- Eurostat/HICP a uso analitico, ma non ufficiale.
- Non esiste un indice IPCA "aziendale", ma si può creare un indice composito con pesi ad hoc per le spese aziendali.
    
### Sintesi

|Destinatario|Indicatore principale|Fonte|
|---|---|---|
|Famiglie|IPCA, NIC, FOI|ISTAT/Eurostat|
|Imprese|PPI (Prezzi alla produzione)|ISTAT/Eurostat|
|Importatori|Prezzi all’importazione|ISTAT/Eurostat|
|Settori edilizia|Prezzi costruzioni, manodopera, materiali|ISTAT|
|Filiera produttiva|Prezzi per CPA/NACE|ISTAT/Eurostat|
