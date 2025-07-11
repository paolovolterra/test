# Gli indicatori macroeconomici e congiunturali 


dataset `EI_`, `AEI_`, `TPS` in base all’uso per analisi macroeconomica e congiunturale:

---

## 🧭 EI_ – Economic Indicators (congiunturali)

Indicatori di fiducia e clima economico, mensili o trimestrali, da indagini Eurostat/AdF:

- EI_ISEN_M – _Economic Sentiment Indicator_ (composito: industria, servizi, consumatori…)
    
- EI_ISBU_M, EI_ISIR_M, EI_ISSP_Q, EI_ISSET_Q, ecc.: fedeltà su specifici settori (imprese, industria, servizi, occupazione)
    

📌 Frequenza: principalmente mensili  
✅ Uso: perfetti per [[../../../MD/nowcasting]] e anticipate svolte economiche.



## ⚙️ AEI_ – Advance Economic Indicators (nowcasting)

Noti meno ma molto utili per stimare la situazione corrente:

- AEI_PR_GNB, AEI_PR_SER: produzione manifatturiera e servizi  
    (i treni delle previsioni su output reale—PIL, produzione industriale)
    

📌 Frequenza: mensile  
✅ Uso: stime dinamiche del PIL prima dei dati ufficiali.

---

## 🧩 TPS – Thematic Pre-aggregated Sets

Raccolte tematiche di indicatori sintetici; utile per presentazioni e dashboard:

- ⚠️ TPS00001: Popolazione al 1° gennaio (solo demografia, non congiuntura) ([ec.europa.eu](https://ec.europa.eu/dgs/eurostat/contingency/table_of_contents_en.pdf?utm_source=chatgpt.com "[PDF] Eurostat Data Navigation Tree - European Commission"))
    
- ✅ TPS00029: indicatori anticipatori del ciclo (leading indicators)
    
- ✅ TPS00204: indicatori di breve periodo per analisi ciclica
    
- Altri TPS come TPS00005 → fiducia, ma controlla tema e frequenza.
    

---

## ✅ Filtrati per il forecasting 2025 H2

|Dataset|Contenuto|Frequenza|Uso per 2025 H2|
|---|---|---|---|
|EI_ISEN_M|Clima economico composito|Mensile|Svolte macro, trend consumi|
|EI_ISBU_M, EI_ISIR_M, EI_ISSP_Q|Fiducia per imprese, industria, occupazione|Mensile/Trimestrale|Indicatori settoriali specifici|
|AEI_PR_GNB, AEI_PR_SER|Produzione anticipata manuf./servizi|Mensile|Proxy PIL, produzione aggregata|
|TPS00029|Indicatori ciclici anticipatori|Variabile|Dashboard congiunturale generale|
|TPS00204|Previsioni a breve, indicatori flash|Variabile|Nowcasting breve periodo|

---

## 🔄 Scarti: cosa non usare per previsioni congiunturali

- TPS00001 → demografia (popolazione) – inutilizzabile per forecast economico ([ec.europa.eu](https://ec.europa.eu/dgs/eurostat/contingency/table_of_contents_en.pdf?utm_source=chatgpt.com "[PDF] Eurostat Data Navigation Tree - European Commission"))
    
- Altri TPS demografici/statistici – es. struttura per età, salubrità, ambientali
    

---

## 📌 Cosa posso fare ora:

- Prepararti un foglio Excel/CSV con questi indicatori (ID, titolo, frequenza, tema, motivazione uso).
    
- Generare uno script Python/Pandas/Jupyter che scarichi mensilmente questi dataset (via SDMX o API) e aggiorni un grafico o modello di previsione.
    
- Creare una mini-dashboard (Plotly Dash o PowerBI) con i principali indicatori per tracciare il secondo semestre 2025.
    

Dimmi cosa preferisci: ti preparo il file, lo script o l’ambiente visuale?