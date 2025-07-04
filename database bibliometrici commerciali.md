---
created: 2025-07-04
---
# Database bibliometrici commerciali


## 1.  [Scopus API (Elsevier)](https://dev.elsevier.com/)

Scopus è uno dei più grandi database bibliometrici commerciali (Elsevier), usato per tracciare pubblicazioni, autori, citazioni, riviste, affiliazioni.

### API disponibili:

- Abstract Retrieval API: recupera metadati di articoli (titolo, autori, abstract, citazioni)
- Search API: ricerca per parola chiave, autore, affiliazione, DOI, etc.
- Author/Institution API: profili pubblici e metriche
- Affiliation API: analisi per enti e università
    
### Accesso:

- Richiede API key e licenza Elsevier / Scopus tramite istituzione
- Gratuito solo per istituzioni con abbonamento
    
### A cosa serve:

Puoi cercare articoli che citano specifici dataset Eurostat (es. `nama_10_gdp`) per misurare l'impatto nella letteratura.

## 2. [Dimensions API (Digital Science)](https://www.digital-science.com/product/dimensions/)

Dimensions è una piattaforma bibliometrica più aperta e dinamica rispetto a Scopus. Contiene:
- articoli scientifici 
- grants
- policy document
- clinical trials 
- brevetti
- dataset (collegati a pubblicazioni)
### API disponibili:

- DSL API (Dimensions Search Language): query tipo SQL/GraphQL
- Puoi cercare per: dataset, autore, affiliazione, keywords, citazioni
### Accesso:

- Gratuito (con registrazione) per uso personale/accademico
- Licenze commerciali disponibili
    
### A cosa serve:

- Puoi cercare tutte le pubblicazioni che usano dataset Eurostat
- Puoi classificare i dataset per numero di citazioni
- Eseguire analisi temporali su uso dei dati
    
## 3.  [CORE API (Open Access, The Open University + Jisc)](https://core.ac.uk/)


CORE raccoglie oltre 250 milioni di articoli open access da università, repository e preprint server (es. arXiv, HAL, RePEc, SSRN).

### API disponibili:

- CORE REST API: accesso a metadati e testi
- CORE Recommender / Search: ricerca simile per documenti 
- CORE Dataset API: indicizzazione di dataset menzionati
  
### Accesso:

- Gratuito con registrazione
- Permette anche analisi di menzioni nei full-text (non solo nei metadati)
    
### A cosa serve:

- Traccia dataset citati o utilizzati nei full-text
- Buona per studiare l’uso di Eurostat nei preprint o paper open access
    
## 🧭 In sintesi

|Fonte|Accesso|Punti di forza|Limiti|
|---|---|---|---|
|Scopus|🔒 A pagamento|Alta qualità e copertura citazionale|Accesso limitato|
|Dimensions|✅ Gratuito accademico|Copre dataset + articoli + grants|DSL complesso|
|CORE|✅ Gratuito open|Copre open access + full-text search|No citazioni ufficiali|
