# Confindustria e il PIL Eurostat

_impariamo da chi ci sa fare_

I grafici di Confindustria. 2025. «Congiuntura Flash». [https://www.confindustria.it/centro-studi/congiuntura-flash/](https://www.confindustria.it/centro-studi/congiuntura-flash/) mi piacciono molto.  
Eurostat è facile da interrogare visto che ha una API dedicata, ma ognuno degli oltre 9.300 dataset contengono una miriade di informazioni nelle quali ci si perde.  
OVVIAMENTE, si tratta di uno studio per imparare Pytrhon su opendata Eurostat, seguendo chi ci sa fare, come Confidustria in questo caso.  

## Libreria `eurostat`

La  libreria Python [eurostat](https://pypi.org/project/eurostat/). facilita l’accesso ai dati ufficiali dell’Unione Europea:

- Permette di scaricare dataset (es. `namq_10_gdp`) in formato `pandas.DataFrame`;
    
- Supporta query tramite `filter_pars`, con parametri come `geo`, `unit`, `na_item`, `s_adj`, etc;
    
- Produce output pulito, compatibile con `pandas`, rendendo semplice la manipolazione dei dati per analisi e visualizzazioni.  



## Industria europea

Il grafico mostra l’**andamento dell’indice della produzione industriale destagionalizzata**. 

- **Produzione industriale (in volume, destagionalizzata, medie trimestrali) 
- Paesi: **Italia, Germania, Francia, Spagna, Eurozona**  
- Periodo: **2022-Q1 → 2025-Q1**
- - base 100 nel 2022-Q1**  

![./media/Pasted image 20250621195903.png|300](./media/Pasted%20image%2020250621195903.png)
_Industria europea: segnali di ripartenza, soprattutto in Germania (Produzione, in volume, destag., medie trim., indici: 2022-Q1=100) Fonte: elaborazioni Centro Studi Confindustria su dati Eurostat_

Usiamo **Eurostat → `sts_inpr_q`**, che fornisce **dati trimestrali sulla produzione industriale** per settore C (industria), unità `I15` (indice, base 2015=100), **destagionalizzati** (`SA`).

Eurostat → dataset [`sts_inpr_m`](https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table)  
(ma disponibile anche trimestrale: `sts_inpr_q`)

- `unit`: I15 → Indice (2015 = 100)
    
- `s_adj`: SA → destagionalizzato
    
- `nace_r2`: C → industria (sezione C)
    
- `geo`: IT, DE, FR, ES, EA
    
- `freq`: M (mensile) oppure Q (trimestrale)


teiis080


## PIL Italia vs Spagna

Il grafico prodotto dal Centro Studi Confindustria (CSC) mostra l’**andamento comparato del PIL reale** di Italia e Spagna, su base trimestrale, negli ultimi dieci anni.  
L’obiettivo è evidenziare in modo immediato il diverso ritmo di crescita tra le due economie, soprattutto nel periodo post-COVID.

### Dati utilizzati

Il grafico si basa su dati ufficiali **Eurostat**, in particolare dal dataset:

- **Codice**: `namq_10_gdp`
    
- **Indicatore**: `B1GQ` → PIL lordo ai prezzi di mercato
    
- **Unità**: `CLV10_MEUR` → volume a prezzi concatenati 2010 (milioni di euro)
    
- **Aggiustamento**: `SCA` → destagionalizzato e corretto per effetti di calendario
    

Si tratta dunque del **PIL reale**, corretto per stagionalità e confrontabile tra trimestri.

![Github/Eurostat/media/Pasted image 20250621195258.png|400](./media/Pasted%20image%2020250621195258.png)
_l PIL spagnolo cresce di più almeno da un decennio (Dati trimestrali, in volume, destag, indici: 2014-Q1=100). Fonte: elaborazioni CSC su dati Eurostat._

### Cosa mostra il grafico

- **Asse X**: i trimestri dal 2014 al 2025, con etichette annuali (solo Q1).
- 
- **Asse Y**: un indice che misura il PIL reale (volume) e ne mostra la variazione nel tempo.
    
- **Indice base**: entrambi i paesi partono da **100 nel primo trimestre del 2014 (2014-Q1)**.
    
- **Colori**:
    
    - 🔴 Spagna → linea rossa
        
    - 🔵 Italia → linea blu

```Python
import re
import eurostat
import pandas as pd
import matplotlib.pyplot as plt

# 1. Scarica dati da Eurostat
df_raw = eurostat.get_data_df(
    code='namq_10_gdp',
    flags=False,
    filter_pars={
        'geo': ['IT', 'ES'],
        'unit': 'CLV10_MEUR',
        'na_item': 'B1GQ',
        's_adj': 'SCA',
        'startPeriod': '2014-Q1',
        'endPeriod': '2025-Q1'
    }
)
# 2. Rinomina colonne
df_raw = df_raw.rename(columns={'geo\\TIME_PERIOD': 'geo'})
period_cols = [c for c in df_raw.columns if re.match(r'^\d{4}-Q[1-4]$', c)]
df_tmp = df_raw[['geo'] + period_cols]

# 3. Long → Wide
df_long = df_tmp.melt(id_vars='geo', var_name='time', value_name='value')
df_long['value'] = pd.to_numeric(df_long['value'], errors='coerce')
df_pivot = df_long.pivot(index='time', columns='geo', values='value').sort_index()
df_pivot = df_pivot.dropna(how='all')

# 4. Rebase su 2014-Q1 = 100
base = df_pivot.loc['2014-Q1']
df_index = df_pivot.div(base) * 100

# 5. Plot con asse X trimestrale, ma etichette ogni anno
x_labels = df_index.index
x_ticks = [i for i, t in enumerate(x_labels) if t.endswith('Q1')]
x_ticklabels = [t[:4] for t in x_labels if t.endswith('Q1')]
plt.figure(figsize=(8, 6))  # quadrato
plt.plot(df_index.index, df_index['ES'], color='red', linewidth=2, label='Spagna')
plt.plot(df_index.index, df_index['IT'], color='blue', linewidth=2, label='Italia')

# plt.axhline(100, color='black', linestyle='--', linewidth=0.8)
plt.ylim(85, 130)
plt.xticks(ticks=x_ticks, labels=x_ticklabels)
plt.title('PIL in volume – Indice (2014-Q1 = 100)')
plt.ylabel('Indice (2014-Q1 = 100)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
```

### Logica dello script

Lo script Python utilizza questi passaggi:

1. **Scarica i dati Eurostat** tramite la libreria `eurostat`.
    
2. **Filtra solo Italia e Spagna**, il periodo 2014–2025 e la metrica corretta (CLV10, SCA).
    
3. **Pulisce e riorganizza i dati** in una tabella con un valore per ogni trimestre.
    
4. **Ricalcola gli indici** ponendo il valore del PIL del 2014-Q1 pari a 100.
    
5. **Traccia due linee** che rappresentano l’evoluzione dell’indice per i due paesi.
    

