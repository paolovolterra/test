---
abstract: |
  Questo report analizza l'evoluzione del PIL pro capite a prezzi
  correnti nelle regioni italiane NUTS2, utilizzando i dati del dataset
  Eurostat `nama_10r_2gdp`.
affiliation: UO Studi e Governo Iniziative
author:
- Paolo Volterra
authors:
- Paolo Volterra
created: 2025-06-25
jupyter: python3
keywords:
- economia
- PIL
- Italia
- NUTS2
- Eurostat
- nama_10r_2gdp
subtitle: Analisi per area geografica basata su dati Eurostat
title: Prodotto Interno Lordo (PIL) a prezzi correnti, analizzato per
  regioni NUTS2
toc-title: Table of contents
---

-   [Executive Summary](#executive-summary){#toc-executive-summary}

::: callout-summary
### Executive Summary

Questo report analizza il **Prodotto Interno Lordo (PIL) pro capite** a
prezzi correnti nelle regioni italiane NUTS2, con dati Eurostat
aggiornati.

-   Ampie differenze territoriali: persistente divario Nord-Sud
-   Dinamiche post-COVID: resilienza variabile tra macroaree
-   Periodo osservato: **2000--2024**

I dati provengono dal dataset `nama_10r_2gdp` e sono visualizzati con
serie storiche comparate.
:::

:::: {.cell fig-width="100%" execution_count="3"}
::: {.cell-output .cell-output-display}
![Prodotto Interno Lordo (PIL) a prezzi correnti, analizzato per regioni
NUTS2](nama_10r_2gdp_files/figure-markdown/fig1-output-1.png){#fig1
fig-align="center"}
:::
::::

:::: {.cell execution_count="4"}
``` {.python .cell-code}
from IPython.display import display, HTML
display(HTML(df_pivot.to_html(classes='dataframe styled-table')))
```

::: {.cell-output .cell-output-display}
  geo_label   Centro (IT)   Isole     Nord-Est   Nord-Ovest   Sud
  ----------- ------------- --------- ---------- ------------ ---------
  time_code                                                   
  2000        24500.0       14200.0   25900.0    26800.0      14800.0
  2001        25900.0       15100.0   26900.0    28100.0      15600.0
  2002        27000.0       15500.0   27400.0    29100.0      16100.0
  2003        27600.0       16100.0   28100.0    30000.0      16400.0
  2004        28800.0       16600.0   29100.0    30700.0      16900.0
  2005        29300.0       17300.0   29700.0    31400.0      17300.0
  2006        30300.0       17900.0   30800.0    32200.0      18000.0
  2007        31300.0       18300.0   32000.0    33300.0      18600.0
  2008        31100.0       18600.0   31900.0    34000.0      18600.0
  2009        30200.0       18000.0   30300.0    32000.0      18000.0
  2010        30300.0       18000.0   30900.0    33200.0      18100.0
  2011        30800.0       18100.0   31900.0    33800.0      18300.0
  2012        30000.0       18100.0   31300.0    32900.0      18300.0
  2013        29500.0       17800.0   31400.0    32600.0      18000.0
  2014        29700.0       17500.0   31900.0    33100.0      18000.0
  2015        30000.0       18000.0   32500.0    33700.0      18500.0
  2016        30900.0       18100.0   33500.0    34700.0      18800.0
  2017        31500.0       18600.0   34400.0    35700.0      19200.0
  2018        32100.0       18800.0   35200.0    36500.0      19600.0
  2019        32900.0       19200.0   35700.0    36900.0      20000.0
  2020        30000.0       18100.0   33200.0    34500.0      18700.0
  2021        33200.0       19900.0   37000.0    38800.0      20700.0
  2022        36600.0       22100.0   39900.0    41800.0      22400.0
  2023        38500.0       23800.0   42500.0    44700.0      24000.0
:::
::::
