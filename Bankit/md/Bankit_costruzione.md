```python
import requests, pandas as pd, os, sqlalchemy, sqlite3, sys, duckdb
from io import BytesIO
from sqlalchemy import create_engine
ddb     = duckdb.connect('D:/Bankit.duckdb')
```


```python
tabella = 'TDB10224'
TDB10224 = ddb.execute(f"SELECT 'TDB10224' tabella,* FROM {tabella} WHERE LOC_CTP = 'ITF11' ORDER BY DATA_OSS").fetchdf()
TDB10224

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tabella</th>
      <th>ATECO_CTP</th>
      <th>DATA_OSS</th>
      <th>ENTE_SEGN</th>
      <th>FENEC</th>
      <th>LOC_CTP</th>
      <th>SET_CTP</th>
      <th>VALORE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TDB10224</td>
      <td>1005001</td>
      <td>2010-06-30</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>482106.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TDB10224</td>
      <td>F</td>
      <td>2010-06-30</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>488508.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TDB10224</td>
      <td>1005009</td>
      <td>2010-06-30</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI42</td>
      <td>3770130.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TDB10224</td>
      <td>1004999</td>
      <td>2010-06-30</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>2016072.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TDB10224</td>
      <td>1005003</td>
      <td>2010-06-30</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>935735.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>870</th>
      <td>TDB10224</td>
      <td>1005009</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI42</td>
      <td>3481387.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>871</th>
      <td>TDB10224</td>
      <td>F</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>276823.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>872</th>
      <td>TDB10224</td>
      <td>1005003</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>665319.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>873</th>
      <td>TDB10224</td>
      <td>1005001</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>279161.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>874</th>
      <td>TDB10224</td>
      <td>1004999</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>1350775.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>875 rows × 9 columns</p>
</div>




```python
tabella = 'TDB10226'
TDB10226 = ddb.execute(f"SELECT 'TDB10226' tabella,* FROM {tabella} WHERE LOC_CTP = 'ITF11' ORDER BY DATA_OSS").fetchdf()
TDB10226
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tabella</th>
      <th>DATA_OSS</th>
      <th>ENTE_SEGN</th>
      <th>FENEC</th>
      <th>LOC_CTP</th>
      <th>SET_CTP</th>
      <th>VALORE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TDB10226</td>
      <td>2007-12-31</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI42</td>
      <td>3162661.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TDB10226</td>
      <td>2007-12-31</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>1772792.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TDB10226</td>
      <td>2007-12-31</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI33</td>
      <td>627272.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TDB10226</td>
      <td>2007-12-31</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>S11BI13</td>
      <td>1145519.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TDB10226</td>
      <td>2007-12-31</td>
      <td>1100010</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI28</td>
      <td>1326350.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1020</th>
      <td>TDB10226</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI28</td>
      <td>1915254.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1021</th>
      <td>TDB10226</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI33</td>
      <td>406643.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1022</th>
      <td>TDB10226</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI42</td>
      <td>3481387.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1023</th>
      <td>TDB10226</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>SBI25</td>
      <td>1350775.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1024</th>
      <td>TDB10226</td>
      <td>2024-12-31</td>
      <td>1070001</td>
      <td>52000139</td>
      <td>ITF11</td>
      <td>S11BI13</td>
      <td>944132.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1025 rows × 8 columns</p>
</div>




```python
tabella = 'TFR10281'
TFR10281 = ddb.execute(f"SELECT 'TFR10281' tabella,* FROM {tabella} ORDER BY DATA_OSS").fetchdf()
TFR10281
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tabella</th>
      <th>DATA_OSS</th>
      <th>DESINV</th>
      <th>ENTE_SEGN</th>
      <th>FENEC</th>
      <th>LOC_CTP</th>
      <th>SET_CTP</th>
      <th>VALORE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TFR10281</td>
      <td>2008-12-31</td>
      <td>997</td>
      <td>1100010</td>
      <td>5800524</td>
      <td>ITG</td>
      <td>SBI119</td>
      <td>10624561.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TFR10281</td>
      <td>2008-12-31</td>
      <td>997</td>
      <td>1100010</td>
      <td>5800526</td>
      <td>ITF</td>
      <td>SBI28</td>
      <td>37210352.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TFR10281</td>
      <td>2008-12-31</td>
      <td>997</td>
      <td>1100010</td>
      <td>5800536</td>
      <td>ITI</td>
      <td>SBI28</td>
      <td>63230.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TFR10281</td>
      <td>2008-12-31</td>
      <td>997</td>
      <td>1100010</td>
      <td>5800526</td>
      <td>ITF</td>
      <td>S14BI2</td>
      <td>7987818.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TFR10281</td>
      <td>2008-12-31</td>
      <td>997</td>
      <td>1100010</td>
      <td>5800538</td>
      <td>ITC</td>
      <td>S12BI39</td>
      <td>34135.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>13517</th>
      <td>TFR10281</td>
      <td>2024-09-30</td>
      <td>997</td>
      <td>1070001</td>
      <td>5800538</td>
      <td>ITH</td>
      <td>S12BI7</td>
      <td>72820.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13518</th>
      <td>TFR10281</td>
      <td>2024-09-30</td>
      <td>997</td>
      <td>1070001</td>
      <td>5800534</td>
      <td>ITF</td>
      <td>SBI28</td>
      <td>14405478.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13519</th>
      <td>TFR10281</td>
      <td>2024-09-30</td>
      <td>997</td>
      <td>1070001</td>
      <td>5800536</td>
      <td>ITF</td>
      <td>S14BI2</td>
      <td>56447.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13520</th>
      <td>TFR10281</td>
      <td>2024-09-30</td>
      <td>997</td>
      <td>1070001</td>
      <td>5800536</td>
      <td>ITG</td>
      <td>SBI28</td>
      <td>79331.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13521</th>
      <td>TFR10281</td>
      <td>2024-09-30</td>
      <td>997</td>
      <td>1070001</td>
      <td>5800536</td>
      <td>ITH</td>
      <td>S11</td>
      <td>3666253.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>13522 rows × 9 columns</p>
</div>




```python
tabella = 'TFR10420'
TFR10420 = ddb.execute(f"SELECT 'TDB10420' tabella,* FROM {tabella} ORDER BY DATA_OSS").fetchdf()
TFR10420
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tabella</th>
      <th>DATA_OSS</th>
      <th>DESINV</th>
      <th>DURORI</th>
      <th>ENTE_SEGN</th>
      <th>FENEC</th>
      <th>LOC_CTP</th>
      <th>RESIDENZA1</th>
      <th>TIPTASSO</th>
      <th>VALORE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TDB10420</td>
      <td>2008-12-31</td>
      <td>902</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITC41</td>
      <td>IT</td>
      <td>800</td>
      <td>599481.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TDB10420</td>
      <td>2008-12-31</td>
      <td>80</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITC48</td>
      <td>IT</td>
      <td>80</td>
      <td>594.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TDB10420</td>
      <td>2008-12-31</td>
      <td>120</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITH59</td>
      <td>IT</td>
      <td>800</td>
      <td>301115.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TDB10420</td>
      <td>2008-12-31</td>
      <td>80</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITG27</td>
      <td>IT</td>
      <td>10000</td>
      <td>70421.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TDB10420</td>
      <td>2008-12-31</td>
      <td>40</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITH51</td>
      <td>IT</td>
      <td>10000</td>
      <td>14318.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>344816</th>
      <td>TDB10420</td>
      <td>2024-09-30</td>
      <td>912</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITH51</td>
      <td>IT</td>
      <td>80</td>
      <td>4771.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>344817</th>
      <td>TDB10420</td>
      <td>2024-09-30</td>
      <td>905</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITF65</td>
      <td>IT</td>
      <td>80</td>
      <td>6224.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>344818</th>
      <td>TDB10420</td>
      <td>2024-09-30</td>
      <td>905</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITG11</td>
      <td>IT</td>
      <td>80</td>
      <td>5129.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>344819</th>
      <td>TDB10420</td>
      <td>2024-09-30</td>
      <td>916</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITF46</td>
      <td>IT</td>
      <td>10000</td>
      <td>2726188.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>344820</th>
      <td>TDB10420</td>
      <td>2024-09-30</td>
      <td>998</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITG15</td>
      <td>IT</td>
      <td>10000</td>
      <td>713717.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>344821 rows × 11 columns</p>
</div>




```python
tabella = 'TFR10430'
TFR10430 = ddb.execute(f"SELECT 'TDB10430' tabella,* FROM {tabella} ORDER BY DATA_OSS").fetchdf()
TFR10430
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tabella</th>
      <th>DATA_OSS</th>
      <th>DESINV</th>
      <th>DURORI</th>
      <th>ENTE_SEGN</th>
      <th>FENEC</th>
      <th>LOC_CTP</th>
      <th>RESIDENZA1</th>
      <th>TIPTASSO</th>
      <th>VALORE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TDB10430</td>
      <td>2008-12-31</td>
      <td>914</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001531</td>
      <td>ITH42</td>
      <td>IT</td>
      <td>80</td>
      <td>1387.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TDB10430</td>
      <td>2008-12-31</td>
      <td>914</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001531</td>
      <td>ITH44</td>
      <td>IT</td>
      <td>10000</td>
      <td>7368.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TDB10430</td>
      <td>2008-12-31</td>
      <td>914</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001531</td>
      <td>ITI1</td>
      <td>IT</td>
      <td>800</td>
      <td>217524.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TDB10430</td>
      <td>2008-12-31</td>
      <td>914</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001531</td>
      <td>ITI4</td>
      <td>IT</td>
      <td>80</td>
      <td>1953.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TDB10430</td>
      <td>2008-12-31</td>
      <td>902</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001531</td>
      <td>ITH44</td>
      <td>IT</td>
      <td>10000</td>
      <td>13272.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>295967</th>
      <td>TDB10430</td>
      <td>2024-09-30</td>
      <td>998</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001531</td>
      <td>ITF46</td>
      <td>IT</td>
      <td>10000</td>
      <td>179855.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>295968</th>
      <td>TDB10430</td>
      <td>2024-09-30</td>
      <td>998</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001531</td>
      <td>ITF61</td>
      <td>IT</td>
      <td>80</td>
      <td>637.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>295969</th>
      <td>TDB10430</td>
      <td>2024-09-30</td>
      <td>997</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001531</td>
      <td>ITH32</td>
      <td>IT</td>
      <td>80</td>
      <td>20339.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>295970</th>
      <td>TDB10430</td>
      <td>2024-09-30</td>
      <td>110</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001531</td>
      <td>ITH3</td>
      <td>IT</td>
      <td>800</td>
      <td>315815.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>295971</th>
      <td>TDB10430</td>
      <td>2024-09-30</td>
      <td>998</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001531</td>
      <td>ITH55</td>
      <td>IT</td>
      <td>80</td>
      <td>2207.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>295972 rows × 11 columns</p>
</div>




```python
tabella = 'TFR10460'
TFR10460 = ddb.execute(f"SELECT 'TFR10460' tabella,* FROM {tabella} ORDER BY DATA_OSS").fetchdf()
TFR10460
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tabella</th>
      <th>DATA_OSS</th>
      <th>DESINV</th>
      <th>DURORI</th>
      <th>ENTE_SEGN</th>
      <th>FENEC</th>
      <th>LOC_CTP</th>
      <th>RESIDENZA1</th>
      <th>TIPTASSO</th>
      <th>VALORE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TFR10460</td>
      <td>2008-12-31</td>
      <td>20</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITG13</td>
      <td>IT</td>
      <td>800</td>
      <td>12682.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TFR10460</td>
      <td>2008-12-31</td>
      <td>996</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITC4C</td>
      <td>IT</td>
      <td>800</td>
      <td>971990.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TFR10460</td>
      <td>2008-12-31</td>
      <td>996</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITF63</td>
      <td>IT</td>
      <td>10000</td>
      <td>58482.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TFR10460</td>
      <td>2008-12-31</td>
      <td>996</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITH43</td>
      <td>IT</td>
      <td>800</td>
      <td>41929.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TFR10460</td>
      <td>2008-12-31</td>
      <td>996</td>
      <td>18</td>
      <td>1100010</td>
      <td>1001530</td>
      <td>ITH58</td>
      <td>IT</td>
      <td>800</td>
      <td>140676.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>96611</th>
      <td>TFR10460</td>
      <td>2024-09-30</td>
      <td>50</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITC1</td>
      <td>IT</td>
      <td>10000</td>
      <td>329844.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96612</th>
      <td>TFR10460</td>
      <td>2024-09-30</td>
      <td>50</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITH3</td>
      <td>IT</td>
      <td>10000</td>
      <td>412329.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96613</th>
      <td>TFR10460</td>
      <td>2024-09-30</td>
      <td>90</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITI14</td>
      <td>IT</td>
      <td>10000</td>
      <td>16444.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96614</th>
      <td>TFR10460</td>
      <td>2024-09-30</td>
      <td>20</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITI16</td>
      <td>IT</td>
      <td>800</td>
      <td>14732.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96615</th>
      <td>TFR10460</td>
      <td>2024-09-30</td>
      <td>20</td>
      <td>18</td>
      <td>1070001</td>
      <td>1001530</td>
      <td>ITI22</td>
      <td>IT</td>
      <td>800</td>
      <td>7782.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>96616 rows × 11 columns</p>
</div>




```python

```
