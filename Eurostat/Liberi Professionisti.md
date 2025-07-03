---
created: 2025-07-03
---
# principali dataset Eurostat dedicati ai “liberi professionisti” 

(intesi come adult self-employment, professionisti e lavoratori autonomi) disponibili nel database europeo:

## Riepilogo dei dataset principali

| Codice        | Tematica                                        |
| ------------- | ----------------------------------------------- |
| lfsa_esgan    | Autonomi per sesso, età e cittadinanza          |
| lfsa_esgais   | Autonomi per sesso, età e professione           |
| lfsa_esgaed   | Autonomi per sesso, età e livello di istruzione |
|               |                                                 |
| lfso_17seclnt | Numero di clienti (LFS 2017)                    |
| lfso_17seworg | Controllo dell’orario (LFS 2017) & sesso        |
| lfso_17sediff | Principali difficoltà percepite (LFS 2017)      |


##  1. Self‑employment by sex, age and citizenship

- **Codice dataset**: `lfsa_esgan`
- https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_esgan?geo=IT
- Variabili annuali su persone autonome suddivise per sesso, fasce d’età e cittadinanza (1 000 individui). Puoi filtrare per paese, periodo e gruppo demografico ([ec.europa.eu](https://ec.europa.eu/eurostat/databrowser/view/lfsa_esgan/default/table?lang=en"[lfsa_esgan] Self-employment by sex, age and citizenship (1 000)"))
-   "id": "freq", "unit", "wstatus", "citizen", "sex", "age", "geo","time"

### freq

          "A": "Annual"
		  
### "unit", 

          "THS_PER": "Thousand persons",
          "PC_EMP": "Percentage of total employment"
		  
### "wstatus"

          "SELF": "Self-employed persons",
          "SELF_S": "Self-employed persons with employees (employers)",
          "SELF_NS": "Self-employed persons without employees (own-account workers)"
		  
### "citizen"

          "EU27_2020_FOR": "EU27 countries (from 2020) except reporting country",
          "NEU27_2020_FOR": "Non-EU27 countries (from 2020) nor reporting country",
          "FOR": "Foreign country",
          "NAT": "Reporting country",
          "STLS": "Stateless",
          "TOTAL": "Total",
          "NRP": "No response"

### "sex"

          "T": "Total",
          "M": "Males",
          "F": "Females"
		  
### "age"
          "Y15-19": "From 15 to 19 years",
          "Y15-24": "From 15 to 24 years",
          "Y15-29": "From 15 to 29 years",
          "Y15-39": "From 15 to 39 years",
          "Y15-59": "From 15 to 59 years",
          "Y15-64": "From 15 to 64 years",
          "Y15-74": "From 15 to 74 years",
          "Y_GE15": "15 years or over",
          "Y20-24": "From 20 to 24 years",
          "Y20-64": "From 20 to 64 years",
          "Y25-29": "From 25 to 29 years",
          "Y25-49": "From 25 to 49 years",
          "Y25-54": "From 25 to 54 years",
          "Y25-59": "From 25 to 59 years",
          "Y25-64": "From 25 to 64 years",
          "Y25-74": "From 25 to 74 years",
          "Y_GE25": "25 years or over",
          "Y30-34": "From 30 to 34 years",
          "Y35-39": "From 35 to 39 years",
          "Y40-44": "From 40 to 44 years",
          "Y40-59": "From 40 to 59 years",
          "Y40-64": "From 40 to 64 years",
          "Y45-49": "From 45 to 49 years",
          "Y50-54": "From 50 to 54 years",
          "Y50-59": "From 50 to 59 years",
          "Y50-64": "From 50 to 64 years",
          "Y50-74": "From 50 to 74 years",
          "Y_GE50": "50 years or over",
          "Y55-59": "From 55 to 59 years",
          "Y55-64": "From 55 to 64 years",
          "Y60-64": "From 60 to 64 years",
          "Y65-69": "From 65 to 69 years",
          "Y65-74": "From 65 to 74 years",
          "Y_GE65": "65 years or over",
          "Y70-74": "From 70 to 74 years",
          "Y_GE75": "75 years or over"
 

## 2. Self‑employment by sex, age and occupation

- **Codice dataset**: `lfsa_esgais` / `lfsq_esgais`
- https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsq_esgais?geo=IT
- Simile al precedente, ma con dettaglio per occupazione professionale ([ec.europa.eu](https://ec.europa.eu/eurostat/databrowser/product/view/lfsa_esgais?category=labour.employ.lfsa.lfsa_empsel"Self-employment by sex, age and occupation (1 000)")).
- id":"freq","unit","sex","age","wstatus","isco08","geo","time"
	

### "freq"

          "Q": "Quarterly"

### "unit"

          "THS_PER": "Thousand persons"

### "sex"

          "T": "Total",
          "M": "Males",
          "F": "Females"

### "age"

          "Y15-19": "From 15 to 19 years",
          "Y15-24": "From 15 to 24 years",
          "Y15-29": "From 15 to 29 years",
          "Y15-39": "From 15 to 39 years",
          "Y15-59": "From 15 to 59 years",
          "Y15-64": "From 15 to 64 years",
          "Y15-74": "From 15 to 74 years",
          "Y_GE15": "15 years or over",
          "Y20-64": "From 20 to 64 years",
          "Y25-49": "From 25 to 49 years",
          "Y25-59": "From 25 to 59 years",
          "Y25-64": "From 25 to 64 years",
          "Y25-74": "From 25 to 74 years",
          "Y_GE25": "25 years or over",
          "Y40-59": "From 40 to 59 years",
          "Y40-64": "From 40 to 64 years",
          "Y50-59": "From 50 to 59 years",
          "Y50-64": "From 50 to 64 years",
          "Y50-74": "From 50 to 74 years",
          "Y_GE50": "50 years or over",
          "Y55-64": "From 55 to 64 years",
          "Y55-74": "From 55 to 74 years",
          "Y_GE65": "65 years or over",
          "Y_GE75": "75 years or over"

### "wstatus"

          "SELF": "Self-employed persons",
          "SELF_S": "Self-employed persons with employees (employers)",
          "SELF_NS": "Self-employed persons without employees (own-account workers)"

### "isco08"

          "TOTAL": "Total",
          "OC1": "Managers",
          "OC2": "Professionals",
          "OC3": "Technicians and associate professionals",
          "OC4": "Clerical support workers",
          "OC5": "Service and sales workers",
          "OC6": "Skilled agricultural, forestry and fishery workers",
          "OC7": "Craft and related trades workers",
          "OC8": "Plant and machine operators and assemblers",
          "OC9": "Elementary occupations",
          "OC0": "Armed forces occupations",
          "NRP": "No response"

### "geo"


### "time"

...
          "2024-Q3": "2024-Q3",
          "2024-Q4": "2024-Q4",
          "2025-Q1": "2025-Q1"

## 3. Self‑employment by sex, age and educational attainment

- **Codice dataset**: `lfsa_esgaed`
- https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_esgaed?geo=IT
- Analisi annuale dell’occupazione autonoma in base al livello di istruzione ([ec.europa.eu](https://ec.europa.eu/eurostat/databrowser/product/view/lfsa_esgaed "Self-employment by sex, age and educational attainment level (1 000)")).
- "id":"freq","unit","sex","age","isced11","wstatus","geo","time"


### "freq"

          "A": "Annual"

### "unit"

          "THS_PER": "Thousand persons"

### "sex"

          "T": "Total",
          "M": "Males",
          "F": "Females"

### "age"

          "Y15-19": "From 15 to 19 years",
          "Y15-24": "From 15 to 24 years",
          "Y15-39": "From 15 to 39 years",
          "Y15-59": "From 15 to 59 years",
          "Y15-64": "From 15 to 64 years",
          "Y15-74": "From 15 to 74 years",
          "Y20-64": "From 20 to 64 years",
          "Y25-49": "From 25 to 49 years",
          "Y25-54": "From 25 to 54 years",
          "Y25-59": "From 25 to 59 years",
          "Y25-64": "From 25 to 64 years",
          "Y25-74": "From 25 to 74 years",
          "Y40-59": "From 40 to 59 years",
          "Y40-64": "From 40 to 64 years",
          "Y50-59": "From 50 to 59 years",
          "Y50-64": "From 50 to 64 years",
          "Y50-74": "From 50 to 74 years",
          "Y55-64": "From 55 to 64 years",
          "Y55-74": "From 55 to 74 years"

### "isced11"

          "TOTAL": "All ISCED 2011 levels",
          "ED0-2": "Less than primary, primary and lower secondary education (levels 0-2)",
          "ED3_4": "Upper secondary and post-secondary non-tertiary education (levels 3 and 4)",
          "ED3_4GEN": "Upper secondary and post-secondary non-tertiary education (levels 3 and 4) - general",
          "ED3_4VOC": "Upper secondary and post-secondary non-tertiary education (levels 3 and 4) - vocational",
          "ED5-8": "Tertiary education (levels 5-8)",
          "NRP": "No response"

### "wstatus"

          "SELF": "Self-employed persons",
          "SELF_S": "Self-employed persons with employees (employers)",
          "SELF_NS": "Self-employed persons without employees (own-account workers)"

### "geo"



### "time"

...
          "2021": "2021",
          "2022": "2022",
          "2023": "2023",
          "2024": "2024"
