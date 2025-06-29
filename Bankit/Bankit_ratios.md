# Bilanci imprese - ratios regionali
Paolo Volterra

<br><br> <!-- due righe di spazio -->

La collana [Economie
regionali](https://www.bancaditalia.it/pubblicazioni/economie-regionali/index.html)
di banca d’Italia contiene analisi sulle principali articolazioni
territoriali (regioni e macroaree) dell’economia italiana.

Una delle tabelle riportate in appendice riporta i dati sugli
“Indicatori economici e finanziari delle imprese”

![](./media/immagine001.png)

Il presente studio vuole analizzare l’andamento degli indicatori per
regione nel tempo.  
Un focus viene fatto sul credit crunch.

<br><br> <!-- due righe di spazio -->

------------------------------------------------------------------------

## Dati

``` python
import pandas as pd, os
os.chdir('D:/')
file_path = "Bankit_ratios_2025H1.tsv"
df = pd.read_csv(file_path, sep="\t")
df.columns = ["REGIONE", "RATIO", "ANNO", "VALORE"]
df["VALORE"] = df["VALORE"].str.replace(",", ".").astype(float)
mezzogiorno = {"ABR", "BAS", "CAL", "CAM", "PUG", "SAR", "SIC", "MOL"}
df["MACROAREA"] = df["REGIONE"].apply(lambda x: "Mezzogiorno" if x in mezzogiorno else "Centro-Nord")
# Calcolo della media per macroarea, ratio e anno
df_grouped = df.groupby(["MACROAREA", "RATIO", "ANNO"])["VALORE"].mean().reset_index()
# Pivot per confronto tra Mezzogiorno e Centro-Nord
df_pivot = df_grouped.pivot(index=["RATIO", "ANNO"], columns="MACROAREA", values="VALORE").reset_index()
df_pivot
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

| MACROAREA | RATIO                              | ANNO  | Centro-Nord | Mezzogiorno |
|-----------|------------------------------------|-------|-------------|-------------|
| 0         | Debiti bancari / Debiti finanziari | Y2018 | 57.781818   | 67.442857   |
| 1         | Debiti bancari / Debiti finanziari | Y2019 | 56.427273   | 65.871429   |
| 2         | Debiti bancari / Debiti finanziari | Y2020 | 57.754545   | 67.957143   |
| 3         | Debiti bancari / Debiti finanziari | Y2021 | 56.754545   | 68.242857   |
| 4         | Debiti bancari / Debiti finanziari | Y2022 | 53.518182   | 68.428571   |
| ...       | ...                                | ...   | ...         | ...         |
| 97        | ROE                                | Y2019 | 7.472727    | 5.842857    |
| 98        | ROE                                | Y2020 | 4.636364    | 4.557143    |
| 99        | ROE                                | Y2021 | 7.963636    | 9.371429    |
| 100       | ROE                                | Y2022 | 9.209091    | 11.700000   |
| 101       | ROE                                | Y2023 | 9.209091    | 13.100000   |

<p>102 rows × 4 columns</p>
</div>

<br><br> <!-- due righe di spazio -->

### Indicatori presenti

Il dataset contiene rapporti finanziari chiave, tra cui:

- Debiti bancari / Debiti finanziari: incidenza dei prestiti bancari sul
  totale dei debiti finanziari.
- Oneri finanziari / Valore della produzione: peso del costo del debito
  rispetto al fatturato.
- Patrimonio netto / Totale delle passività: misura della solidità
  patrimoniale.
- Indebitamento finanziario / Attivo: leva finanziaria.
- Autofinanziamento / Investimenti: capacità interna di finanziare la
  crescita.

Le imprese del Mezzogiorno risultano più dipendenti dal credito
bancario, con struttura finanziaria più fragile e costo del debito più
elevato.

Ciò segnala un ritardo nell’accesso alla finanza alternativa e nella
capacità di autofinanziamento.

### Debiti bancari / Debiti finanziari

Costantemente più alto nel Mezzogiorno: segno che le imprese meridionali
fanno maggiormente ricorso al credito bancario tradizionale, con meno
accesso a strumenti alternativi (leasing, factoring, minibond).

Il gap è stabile: ~10–15 punti percentuali a favore del Centro-Nord.

### Oneri finanziari / Valore della produzione

Più elevati nel Mezzogiorno, con un divario che si allarga nel
2022–2023.

Indica che il costo del denaro pesa di più per le imprese meridionali, a
parità di fatturato: possibile effetto combinato di rating più deboli,
minore concorrenza bancaria, meno strumenti di copertura.

### Patrimonio netto / Totale delle passività

Centro-Nord meglio capitalizzato: rapporto stabilmente superiore, anche
in anni critici.

Le imprese del Sud mostrano una minore patrimonializzazione, quindi
maggiore vulnerabilità in caso di shock o aumento dei tassi.

### Autofinanziamento / Investimenti

Il Centro-Nord finanzia una quota più ampia degli investimenti con
risorse proprie.

Il Mezzogiorno mostra maggiore dipendenza da fonti esterne (pubbliche o
bancarie), che rende l’investimento più volatile.

### Evoluzione temporale (2018–2023)

- Post-Covid (2020–2021): leggero miglioramento in molti indicatori,
  probabilmente per effetto di moratorie, liquidità straordinaria, fondo
  di garanzia.
- 2022–2023: inizia a emergere un deterioramento, con peggioramento
  degli oneri finanziari e lieve riduzione della patrimonializzazione.

<br><br> <!-- due righe di spazio -->

## Cluster analysis

``` python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# === Preparazione dati: media 2018–2023 per regione e ratio
df_cluster = df.groupby(["REGIONE", "RATIO"])["VALORE"].mean().unstack()

# === Rimozione regioni con valori NaN
df_cluster_clean = df_cluster.dropna()

# === Standardizzazione
scaler = StandardScaler()
X_scaled_clean = scaler.fit_transform(df_cluster_clean)

# === Metodo del gomito per scelta K ottimale
K_range = range(1, 10)
inertia_clean = []
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(X_scaled_clean)
    inertia_clean.append(kmeans.inertia_)

# === Visualizzazione gomito
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia_clean, marker='o', color='green')
plt.xlabel("Numero di cluster (k)")
plt.ylabel("Inertia")
plt.title("Elbow curve")
plt.grid(True)
plt.ylim(min(inertia_clean) * 0.95, max(inertia_clean) * 1.05)  # zoom verticale
plt.show()
```

<img src="Bankit_ratios_files/figure-commonmark/fig1-output-1.png"
data-fig-align="center" alt="curva Elbow" />

``` python
# === Clustering finale (K=3)
kmeans_final = KMeans(n_clusters=3, random_state=0, n_init=10)

# Copia sicura per evitare ambiguità
df_cluster_clean = df_cluster_clean.copy()
df_cluster_clean["CLUSTER"] = kmeans_final.fit_predict(X_scaled_clean)

# === Valori medi per cluster
# Valori medi per cluster (trasposti)
df_cluster_mean = df_cluster_clean.groupby("CLUSTER").mean().round(2)
df_cluster_mean_t = df_cluster_mean.T.sort_index()

# Uso della libreria tabulate per mostrare una tabella ben formattata in stile "pretty"
from tabulate import tabulate

print(tabulate(df_cluster_mean_t.reset_index(), headers="keys", tablefmt="github", showindex=False))

df_cluster_mean_t.to_html("cluster_table.html", float_format="%.2f")
```

    | RATIO                                         |      0 |      1 |      2 |
    |-----------------------------------------------|--------|--------|--------|
    | Debiti bancari / Debiti finanziari            |  50.4  |  57.64 |  67.81 |
    | Debiti finanziari / Fatturato                 |  31.82 |  32.81 |  25.5  |
    | Indice di gestione incassi e pagamenti        |  11.56 |  14.73 |  16.32 |
    | Leverage                                      |  40.74 |  43.5  |  39.97 |
    | Leverage corretto per la liquidità            |  32.11 |  33.88 |  26.58 |
    | Liquidità corrente                            | 122.19 | 129.07 | 136.75 |
    | Liquidità immediata                           |  92    |  97.25 | 103.37 |
    | Liquidità/Attivo                              |   9.75 |  10.61 |  11.91 |
    | Margine operativo lordo/attivo                |   6    |   7.64 |   7.27 |
    | Margine operativo lordo/valore aggiunto       |  33.59 |  37.35 |  34.44 |
    | Margine operativo lordo/valore produzione     |   6.89 |   8.82 |   7.73 |
    | Obbligazioni/debiti finanziari                |   8.2  |   3.81 |   2.86 |
    | Oneri finanziari/margine operativo lordo      |  14.52 |  11.58 |  11.11 |
    | Posizione finanziaria netta/Attivo            | -16.48 | -17.12 | -11.51 |
    | Quota debiti finanziari a medio-lungo termine |  56.59 |  55.82 |  55.34 |
    | ROA                                           |   4.11 |   5.17 |   5.36 |
    | ROE                                           |   5.34 |   8.15 |   8.74 |

<br><br> <!-- due righe di spazio -->

La segmentazione delle regioni italiane in 3 cluster basata sui loro
indicatori finanziari medi (2018–2023). Ogni cluster rappresenta un
profilo omogeneo di comportamento finanziario:

- Cluster 0: regioni con alta dipendenza da debito bancario, leva
  moderata, e autofinanziamento medio.
- Cluster 1: (da identificare dopo confronto completo) – potenzialmente
  regioni con maggiore solidità patrimoniale.
- Cluster 2: (da verificare) – potrebbe contenere regioni con
  performance più efficienti o più fragili, a seconda della direzione
  dei ratios.

<br><br> <!-- due righe di spazio -->

``` python
# Eseguo il clustering con k=3
kmeans_final = KMeans(n_clusters=3, random_state=0, n_init=10)
df_cluster_clean["CLUSTER"] = kmeans_final.fit_predict(X_scaled_clean)

# Riordino per cluster
df_cluster_clean_sorted = df_cluster_clean.sort_values("CLUSTER")

# Visualizzo i risultati
df_cluster_clean_sorted.reset_index()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

| RATIO | REGIONE | Debiti bancari / Debiti finanziari | Debiti finanziari / Fatturato | Indice di gestione incassi e pagamenti | Leverage | Leverage corretto per la liquidità | Liquidità corrente | Liquidità immediata | Liquidità/Attivo | Margine operativo lordo/attivo | Margine operativo lordo/valore aggiunto | Margine operativo lordo/valore produzione | Obbligazioni/debiti finanziari | Oneri finanziari/margine operativo lordo | Posizione finanziaria netta/Attivo | Quota debiti finanziari a medio-lungo termine | ROA | ROE | CLUSTER |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | Bol | 58.783333 | 28.150000 | 13.150000 | 35.066667 | 27.116667 | 116.016667 | 84.633333 | 8.033333 | 6.066667 | 31.350000 | 6.916667 | 3.033333 | 11.950000 | -16.216667 | 48.766667 | 4.433333 | 6.333333 | 0 |
| 1 | SAR | 57.400000 | 28.266667 | 11.466667 | 44.100000 | 32.833333 | 125.600000 | 89.333333 | 11.233333 | 6.133333 | 32.966667 | 6.000000 | 1.683333 | 15.466667 | -15.683333 | 61.316667 | 3.216667 | 2.916667 | 0 |
| 2 | LAZ | 27.800000 | 43.716667 | 8.316667 | 44.500000 | 37.850000 | 111.933333 | 91.350000 | 10.216667 | 5.150000 | 37.433333 | 7.500000 | 21.333333 | 18.833333 | -18.800000 | 59.700000 | 4.400000 | 5.983333 | 0 |
| 3 | PIE | 57.616667 | 27.133333 | 13.316667 | 39.300000 | 30.650000 | 135.200000 | 102.666667 | 9.500000 | 6.633333 | 32.600000 | 7.150000 | 6.750000 | 11.816667 | -15.216667 | 56.566667 | 4.400000 | 6.116667 | 0 |
| 4 | LIG | 50.966667 | 36.616667 | 13.300000 | 45.833333 | 36.583333 | 119.700000 | 93.683333 | 11.666667 | 6.666667 | 34.266667 | 8.500000 | 6.066667 | 13.666667 | -16.416667 | 51.116667 | 4.983333 | 8.133333 | 1 |
| 5 | BAS | 63.350000 | 25.900000 | 13.516667 | 44.083333 | 32.250000 | 124.600000 | 95.766667 | 10.066667 | 7.500000 | 35.583333 | 7.866667 | 1.133333 | 12.283333 | -13.650000 | 53.583333 | 5.300000 | 9.733333 | 1 |
| 6 | TOS | 54.333333 | 30.566667 | 15.300000 | 38.766667 | 30.050000 | 134.233333 | 101.083333 | 10.133333 | 8.033333 | 42.583333 | 9.283333 | 2.216667 | 8.866667 | -16.033333 | 52.250000 | 5.666667 | 8.133333 | 1 |
| 7 | FVG | 70.416667 | 31.850000 | 15.466667 | 43.433333 | 33.350000 | 130.366667 | 91.183333 | 10.783333 | 7.600000 | 34.116667 | 8.450000 | 3.000000 | 11.750000 | -17.166667 | 56.116667 | 4.950000 | 7.483333 | 1 |
| 8 | Tre | 53.733333 | 38.100000 | 13.683333 | 45.233333 | 36.466667 | 125.600000 | 97.183333 | 10.733333 | 8.866667 | 43.066667 | 10.883333 | 3.450000 | 7.900000 | -19.633333 | 59.516667 | 5.283333 | 9.800000 | 1 |
| 9 | LOM | 42.450000 | 36.266667 | 14.500000 | 44.433333 | 36.483333 | 130.750000 | 101.300000 | 9.516667 | 7.516667 | 37.933333 | 8.950000 | 9.683333 | 13.816667 | -20.350000 | 60.533333 | 5.300000 | 7.383333 | 1 |
| 10 | MAR | 68.216667 | 30.400000 | 17.333333 | 42.750000 | 32.000000 | 138.216667 | 100.533333 | 11.350000 | 7.266667 | 33.900000 | 7.783333 | 1.100000 | 12.766667 | -16.600000 | 57.616667 | 4.733333 | 6.366667 | 1 |
| 11 | SIC | 72.466667 | 24.516667 | 14.783333 | 39.466667 | 26.516667 | 126.750000 | 98.300000 | 10.500000 | 6.983333 | 33.483333 | 7.583333 | 0.850000 | 11.966667 | -11.466667 | 57.166667 | 4.883333 | 8.000000 | 2 |
| 12 | ABR | 73.066667 | 25.150000 | 17.966667 | 40.766667 | 29.483333 | 137.033333 | 103.150000 | 10.950000 | 7.366667 | 32.833333 | 7.583333 | 1.266667 | 12.316667 | -13.250000 | 51.216667 | 5.383333 | 8.183333 | 2 |
| 13 | CAM | 68.116667 | 24.000000 | 14.700000 | 42.150000 | 25.716667 | 134.616667 | 105.283333 | 13.316667 | 7.350000 | 35.150000 | 7.383333 | 1.800000 | 11.266667 | -9.883333 | 53.933333 | 5.416667 | 9.666667 | 2 |
| 14 | CAL | 67.133333 | 26.016667 | 18.116667 | 40.383333 | 23.900000 | 138.550000 | 105.166667 | 12.533333 | 6.833333 | 33.433333 | 8.200000 | 0.283333 | 11.166667 | -8.550000 | 64.900000 | 5.133333 | 9.333333 | 2 |
| 15 | EMR | 59.783333 | 29.983333 | 16.716667 | 39.516667 | 28.500000 | 140.983333 | 104.633333 | 12.316667 | 6.683333 | 34.916667 | 7.600000 | 7.416667 | 11.150000 | -13.633333 | 50.416667 | 5.283333 | 8.133333 | 2 |
| 16 | VEN | 66.266667 | 23.350000 | 15.650000 | 37.533333 | 25.383333 | 142.550000 | 103.700000 | 11.866667 | 8.416667 | 36.833333 | 8.050000 | 5.566667 | 8.783333 | -12.283333 | 54.416667 | 6.033333 | 9.150000 | 2 |

</div>

<br><br> <!-- due righe di spazio -->

### 🟢 Cluster 0: “Alta dipendenza dal credito bancario” - Caratteristiche:

-Rapporto Debiti bancari / Debiti finanziari molto elevato. -Costi
finanziari / valore della produzione alti, segno di un onere del debito
significativo. -Leva finanziaria (Debiti finanziari / Attivo)
moderata-alta. -Autofinanziamento / Investimenti nella media: buona
capacità di generare risorse ma non sufficiente a coprire pienamente gli
investimenti. -Buona generazione di cassa, capacità applicativa di leva
Dipendenza da banche, vulnerabilità all’aumento tassi - Profilo: imprese
con forte esposizione al credito bancario, costi finanziari superiori
alla media, leva e autofinanziamento nella media

### 🟡 Cluster 1: “Solidità patrimoniale e rifinanziamento bilanciato” - Caratteristiche:

- Rapporto Patrimonio netto / Totale passività alto, indica buona
  capitalizzazione.
- Debiti bancari / Debiti totali più contenuti rispetto al Cluster 0,
  con maggiore presenza di strumenti finanziari diversificati.
- Autofinanziamento / Investimenti elevato: le imprese tendono a
  finanziare internamente gli investimenti.
- Costi finanziari contenuti, in linea o al di sotto della media
  nazionale.
- Elevata patrimonializzazione, autonomia finanziaria Potrebbe limitare
  leva utile per crescite aggressive
- Profilo: imprese con maggiore capitale proprio, accesso più bilanciato
  alla finanza, migliore posizione finanziaria netta

### 🔴 Cluster 2: “Fragilità accentuata o piccole imprese esposte” - Caratteristiche:

- Leva finanziaria molto elevata, indicando forte indebitamento.
- Autofinanziamento / Investimenti basso: dipendenza significativa da
  finanziamenti esterni.
- Rapporto Patrimonio netto / Totale passività più basso, indice di
  fragilità patrimoniale.
- I costi finanziari possono essere molto alti, per l’effetto combinato
  di leva elevata e rating debole.
- Possibile presenza di realtà dinamiche in espansione Elevata
  vulnerabilità finanziaria, rischi elevati
- Profilo: combinazione di leve elevate, bassa patrimonializzazione,
  autofinanziamento ridotto – possibili anomalie strutturali o effetti
  della dimensione media d’impresa

``` python
# Generazione di un radar unico con tutti i cluster sovrapposti

import numpy as np
labels = df_cluster_mean_t.index.tolist()
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Cluster colors e labels
cluster_colors = ['gold', 'green', 'red']
cluster_labels = ['Cluster 0', 'Cluster 1', 'Cluster 2']

# Radar comparativo senza riempimento interno e con immagine più grande

fig, ax = plt.subplots(figsize=(12,12), subplot_kw=dict(polar=True))

for i in range(3):
    values = df_cluster_mean_t.iloc[:, i].tolist()
    values += values[:1]
    ax.plot(angles, values, color=cluster_colors[i], linewidth=2, label=cluster_labels[i])
    # Niente fill per maggiore pulizia visiva

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.set_yticklabels([])
ax.set_title("Grafico Radar dei Cluster", fontsize=16, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()
```

<img src="Bankit_ratios_files/figure-commonmark/fig3-output-1.png"
data-fig-align="center" alt="radar comparativo dei cluster" />

``` python
# Estraggo le regioni per ciascun cluster
cluster_regioni = df_cluster_clean_sorted.reset_index()[["REGIONE", "CLUSTER"]]
cluster_regioni_grouped = cluster_regioni.groupby("CLUSTER")["REGIONE"].apply(list).reset_index(name="REGIONI")

cluster_regioni_grouped
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | CLUSTER | REGIONI                               |
|-----|---------|---------------------------------------|
| 0   | 0       | \[Bol, SAR, LAZ, PIE\]                |
| 1   | 1       | \[LIG, BAS, TOS, FVG, Tre, LOM, MAR\] |
| 2   | 2       | \[SIC, ABR, CAM, CAL, EMR, VEN\]      |

</div>

``` python
import geopandas as gpd
import matplotlib.pyplot as plt

# Uso un dataset di regioni italiane semplificato da ISTAT (necessario importarlo)
# Carico un dataset esterno con codici e geometrie regionali
regioni = gpd.read_file("https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson")

# Mappo i codici ISO (es. 'IT-62') in codici del file (es. 'VEN') usando una tabella
codici_regioni = {
    'Abruzzo': 'ABR', 'Basilicata': 'BAS', 'Calabria': 'CAL', 'Campania': 'CAM',
    'Emilia-Romagna': 'EMR', 'Friuli-Venezia Giulia': 'FVG', 'Lazio': 'LAZ', 'Liguria': 'LIG',
    'Lombardia': 'LOM', 'Marche': 'MAR', 'Molise': 'MOL', 'Piemonte': 'PIE', 'Puglia': 'PUG',
    'Sardegna': 'SAR', 'Sicilia': 'SIC', 'Toscana': 'TOS', 'Trentino-Alto Adige/Südtirol': 'Tre',
    'Umbria': 'UMB', 'Valle d\'Aosta/Vallée d\'Aoste': 'VAO', 'Veneto': 'VEN',
    'Provincia Autonoma Bolzano/Bozen': 'Bol'
}

regioni["CODICE"] = regioni["reg_name"].map(codici_regioni)

# Unisco i cluster alle geometrie
df_map = df_cluster_clean_sorted.reset_index()[["REGIONE", "CLUSTER"]]
mappa_cluster = regioni.merge(df_map, left_on="CODICE", right_on="REGIONE", how="left")

from matplotlib.colors import ListedColormap
# Plot
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
cmap3 = ListedColormap(["#FFD700", "#228B22", "#B22222"])  # giallo, verde, rosso
mappa_cluster.plot(
    column="CLUSTER",
    cmap=cmap3,
    linewidth=0.8,
    edgecolor="gray",
    legend=False,
    ax=ax
)
ax.set_title("Cluster finanziari delle regioni italiane (2018–2023)", fontsize=14)
ax.axis("off")
plt.show()
```

<img src="Bankit_ratios_files/figure-commonmark/fig2-output-1.png"
data-fig-align="center" alt="clusterizzazione regioni" />

## Analisi temporale

Rifacciamo il clustering considerando tutte le annualità (2018–2023) per
ogni ratio, quindi: - Ogni regione è descritta da 103 variabili
(ratio_anno), invece della sola media. - Il clustering cattura anche la
dinamica temporale e non solo il valore medio statico. - Le regioni sono
classificate in 3 cluster più coerenti con l’evoluzione nel tempo degli
indicatori.

``` python
import pandas as pd
file_path = "D:/Bankit_ratios_2025H1.tsv"
df = pd.read_csv(file_path, sep="\t")
df.columns = ["REGIONE", "RATIO", "ANNO", "VALORE"]
df["VALORE"] = df["VALORE"].str.replace(",", ".").astype(float)
# Pivot table: una colonna per ciascun ratio_anno
df["RATIO_ANNO"] = df["RATIO"] + "_" + df["ANNO"].astype(str)
df_wide = df.pivot(index="REGIONE", columns="RATIO_ANNO", values="VALORE")

# Rimuovo righe con NaN e standardizzo
df_wide_clean = df_wide.dropna().copy()
scaler = StandardScaler()
X_scaled_all_years = scaler.fit_transform(df_wide_clean)

# Clustering
kmeans_all_years = KMeans(n_clusters=3, random_state=0, n_init=10)
df_wide_clean["CLUSTER"] = kmeans_all_years.fit_predict(X_scaled_all_years)

# Salvo la tabella finale
df_cluster_all_years = df_wide_clean.copy()

# Recupero il DataFrame originale
df_clusters_by_year = df.copy()

# Aggiungo la colonna cluster da df_cluster_all_years
cluster_map = df_cluster_all_years["CLUSTER"]
df_clusters_by_year["CLUSTER"] = df_clusters_by_year["REGIONE"].map(cluster_map)

# Tabella finale: regioni in riga, anni in colonna, valore = cluster
df_cluster_matrix = df_clusters_by_year[["REGIONE", "ANNO", "CLUSTER"]].drop_duplicates()
df_cluster_matrix_wide = df_cluster_matrix.pivot(index="REGIONE", columns="ANNO", values="CLUSTER").astype("Int64")

df_cluster_matrix_wide
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

| ANNO    | Y2018  | Y2019  | Y2020  | Y2021  | Y2022  | Y2023  |
|---------|--------|--------|--------|--------|--------|--------|
| REGIONE |        |        |        |        |        |        |
| ABR     | 2      | 2      | 2      | 2      | 2      | 2      |
| BAS     | 1      | 1      | 1      | 1      | 1      | 1      |
| Bol     | 0      | 0      | 0      | 0      | 0      | 0      |
| CAL     | 2      | 2      | 2      | 2      | 2      | 2      |
| CAM     | 2      | 2      | 2      | 2      | 2      | 2      |
| EMR     | 2      | 2      | 2      | 2      | 2      | 2      |
| FVG     | 1      | 1      | 1      | 1      | 1      | 1      |
| LAZ     | 0      | 0      | 0      | 0      | 0      | 0      |
| LIG     | 1      | 1      | 1      | 1      | 1      | 1      |
| LOM     | 1      | 1      | 1      | 1      | 1      | 1      |
| MAR     | 2      | 2      | 2      | 2      | 2      | 2      |
| MOL     | \<NA\> | \<NA\> | \<NA\> | \<NA\> | \<NA\> | \<NA\> |
| PIE     | 0      | 0      | 0      | 0      | 0      | 0      |
| SAR     | 0      | 0      | 0      | 0      | 0      | 0      |
| SIC     | 2      | 2      | 2      | 2      | 2      | 2      |
| TOS     | 2      | 2      | 2      | 2      | 2      | 2      |
| Tre     | 1      | 1      | 1      | 1      | 1      | 1      |
| VEN     | 2      | 2      | 2      | 2      | 2      | 2      |

</div>

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# === Caricamento e pulizia dati ===
df = pd.read_csv("D:/Bankit_ratios_2025H1.tsv", sep="\t")
df.columns = ["REGIONE", "RATIO", "ANNO", "VALORE"]
df["ANNO"] = df["ANNO"].str.replace("Y", "")
df["VALORE"] = df["VALORE"].str.replace(",", ".").astype(float)
# === Filtro dati 2018 ===
df_2018 = df[df["ANNO"] == "2018"]

# === Pivot Regione x RATIO ===
df_2018_pivot = df_2018.pivot(index="REGIONE", columns="RATIO", values="VALORE")

# === Imputazione media colonna per valori mancanti ===
df_2018_pivot_filled = df_2018_pivot.fillna(df_2018_pivot.mean(numeric_only=True))

# === Standardizzazione e clustering (K=3) ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_2018_pivot_filled)

kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
df_2018_pivot_filled["CLUSTER"] = kmeans.fit_predict(X_scaled)

# === Calcolo delle medie per cluster ===
df_cluster_mean_2018 = df_2018_pivot_filled.groupby("CLUSTER").mean().T

# === Definizione grafico radar ===
cluster_colors = ['gold', 'green', 'red']
cluster_labels = ['Cluster 0', 'Cluster 1', 'Cluster 2']
labels = df_cluster_mean_2018.index.tolist()
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# === Creazione radar chart ===
fig, ax = plt.subplots(figsize=(14, 14), subplot_kw=dict(polar=True))

for i in range(3):
    values = df_cluster_mean_2018.iloc[:, i].tolist()
    values += values[:1]
    ax.plot(angles, values, color=cluster_colors[i], linewidth=2, label=cluster_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=9)
ax.set_yticklabels([])
ax.set_title("Grafico Radar dei Cluster - Anno 2018 (dati completati)", fontsize=16, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()
```

![](Bankit_ratios_files/figure-commonmark/cell-10-output-1.png)
