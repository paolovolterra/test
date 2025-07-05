# DBNomics


![](https://db.nomics.world/_app/immutable/assets/dbnomics@2x.DkOK0P40.png)


DBnomics è una piattaforma open source e gratuita per l’accesso unificato ai dati economici e statistici pubblici provenienti da numerose fonti ufficiali.

> DBnomics = _Database for Economic Data from Official Sources_

È un data hub globale che raccoglie, standardizza e rende interrogabili via web API e Python/R i dati economici e statistici di enti come:

- OCSE (OECD)
    
- FMI (IMF)
    
- Eurostat
    
- Banca Mondiale
    
- ISTAT
    
- Banca d’Italia
    
- INSEE (Francia)
    
- e molti altri (oltre 80 provider).
    

### Cosa lo rende utile

- ✅ Interfaccia comune: unifica codifiche, metadati, strutture e formato dei dataset.
    
- ✅ API RESTful: permette interrogazioni automatiche da script Python/R.
    
- ✅ Esplorabile via web: [https://db.nomics.world](https://db.nomics.world/) con ricerca full-text, filtri, grafici.
    
- ✅ Accesso a serie storiche e time-series: spesso più comodo rispetto ai singoli portali dei provider.
    
- ✅ Formato JSON standardizzato: facile integrazione con librerie come `pandas` o `statsmodels`.
    


### Come usarlo in Python

Installazione:

```bash
pip install dbnomics
```

Esempio:

```python
from dbnomics import fetch_series

# PIL Italia, fonte Eurostat
df = fetch_series(provider_code='EUROSTAT', dataset_code='nama_10_gdp', series_code='B1GQ.IT.CP_MEUR.N')
print(df[['period', 'value']].tail())
```

Puoi anche scaricare tutti i dataset disponibili per un provider.


### Architettura tecnica

DBnomics raccoglie i dati direttamente via API o download dai provider, li _standardizza_ in un formato omogeneo (`JSON-stat-like`) e li _espone_ via:

- REST API: `https://api.db.nomics.world/v22`
    
- Web interface: `https://db.nomics.world`
    
- Python client (`dbnomics`)
    
- R package
    

### Risorse utili

- 📘 Docs ufficiali: [https://docs.db.nomics.world](https://docs.db.nomics.world/)
    
- 🔍 Web portal: [https://db.nomics.world](https://db.nomics.world/)
    
- 🧑‍💻 Codice su GitHub: [https://github.com/dbnomics](https://github.com/dbnomics)
    

###  Esempi di utilizzo

- Analisi macroeconomica comparata (PIL, disoccupazione, inflazione)
    
- Automazione dashboard (Power BI, Jupyter, Streamlit)
    
- Ricerca economica e visualizzazioni interattive
    
- Integrazione in modelli econometrici
    


## [Istat](Istat)


![Data providers](Data%20providers.md)