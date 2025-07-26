---
title: "Accessing ECB Exchange Rate Data in Python"
source: "https://www.datacareer.de/blog/accessing-ecb-exchange-rate-data-in-python/"
author:
  - "[[datacareer.de]]"
published:
created: 2025-07-12
description: "In this Jupyter Notebook we will retrieve data from the European Central Bank (ECB). The ECB publishes through the European Open Data Portal, which we discussed in the previous post."
tags:
  - "clippings"
---
16/10/2018

![Accessing ECB Exchange Rate Data in Python](https://www.datacareer.de/files/pictures/image_exchangrates2.png)

In this Jupyter Notebook we will retrieve data from the European Central Bank (ECB). The ECB publishes through the European Open Data Portal, which we discussed in the [previous tutorial](https://www.datacareer.de/blog/eu-open-data-portal-api/).

Before diving into the code, please take a quick look at the following websites, to get a feel for what we will be dealing with.

---

EU portal: [https://data.europa.eu/euodp/en/data/publisher/ecb](https://data.europa.eu/euodp/en/data/publisher/ecb)

ECB SDMX 2.1 RESTful web service: [https://sdw-wsrest.ecb.europa.eu/help/](https://sdw-wsrest.ecb.europa.eu/help/)

SDMX documentation: [https://sdmx.org](https://sdmx.org/)

ECB statistics: [https://www.ecb.europa.eu/stats/ecb\_statistics/html/index.en.html](https://www.ecb.europa.eu/stats/ecb_statistics/html/index.en.html)

Statistical Data Warehouse: [https://sdw.ecb.europa.eu](https://sdw.ecb.europa.eu/)

[![](https://datacareergermany.mysmartjobboard.com/files/userfiles/Banner%20DC%20DE.JPG)](https://www.datacareer.de/)

In this tutorial we will specifically take a look at foreign exchange (FX) rates, using **Python 3**. As always, let's start with importing some packages we will use for this exercise.

In \[1\]:

```
import requests     # 2.18.4
import pandas as pd # 0.23.0
import io
```

In this notebook, we will retrieve the Euro / Swiss Francs (EURCHF) exchange rate time series from the year 2000 until today. To retrieve the data, we need to construct an URL which we can use in a HTTP request. Fortunately, this is pretty simple.

The query string is basically:  
**protocol://wsEntryPoint/resource/flowRef/key?parameters**  
And the parameters are defined as follows: **startPeriod=value&endPeriod=value&updatedAfter=value&firstNObservations=value&lastNObservations=value&detail=value&includeHistory=value**

Let's break this down:

In \[2\]:

```
# Building blocks for the URL
entrypoint = 'https://sdw-wsrest.ecb.europa.eu/service/' # Using protocol 'https'
resource = 'data'           # The resource for data queries is always'data'
flowRef ='EXR'              # Dataflow describing the data that needs to be returned, exchange rates in this case
key = 'D.CHF.EUR.SP00.A'    # Defining the dimension values, explained below

# Define the parameters
parameters = {
    'startPeriod': '2000-01-01',  # Start date of the time series
    'endPeriod': '2018-10-01'     # End of the time series
}
```

Key (dimensions) explained:

- the frequency of the measurement: **D** for daily
- the currency being measured: **CHF** for Swiss Francs
- the currency against which a currency is being measured: **EUR** for Euros
- the type of exchange rates: foreign exchange reference rates have code **SP00**
- the series variation (such as average or standardised measure for given frequency): code **A**

For this example we only use two parameters, `startPerdiod` and `endPeriod`, but you can add more if you like.

Now we have to put all this together to construct the URL:

In \[3\]:

```
# Construct the URL: https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.CHF.EUR.SP00.A
request_url = entrypoint + resource + '/'+ flowRef + '/' + key

# Make the HTTP request
response = requests.get(request_url, params=parameters)

# Check if the response returns succesfully with response code 200
print(response)

# Print the full URL
print(response.url)
```

```
<Response [200]>
https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.CHF.EUR.SP00.A?startPeriod=2000-01-01&endPeriod=2018-10-01
```

The request/response has been successful. If you click on this link, it will download the data as a file. It doesn't have a useful extension, but you can open it as a text file if you would like to inspect its contents. But of course, we can do this in Python too without leaving this notebook. Let's take a sneak peek at the data we received.

Hmmm, the response is in XML. Not impossible, but also not the easiest format to work within Pandas. Fortunately, the ECB's API lets us get the data in CSV format by specifying it in the header of the request.

In \[6\]:

```
# Print the first 1000 characters to inspect the response
response.text[0:1000]
```

Out\[6\]:

```
'KEY,FREQ,CURRENCY,CURRENCY_DENOM,EXR_TYPE,EXR_SUFFIX,TIME_PERIOD,OBS_VALUE,OBS_STATUS,OBS_CONF,OBS_PRE_BREAK,OBS_COM,TIME_FORMAT,BREAKS,COLLECTION,COMPILING_ORG,DISS_ORG,DOM_SER_IDS,PUBL_ECB,PUBL_MU,PUBL_PUBLIC,UNIT_INDEX_BASE,COMPILATION,COVERAGE,DECIMALS,NAT_TITLE,SOURCE_AGENCY,SOURCE_PUB,TITLE,TITLE_COMPL,UNIT,UNIT_MULT\r\nEXR.D.CHF.EUR.SP00.A,D,CHF,EUR,SP00,A,2000-01-03,1.6043,A,,,,P1D,,A,,,,,,,,,,4,,4F0,,Swiss franc/Euro,"ECB reference exchange rate, Swiss franc/Euro, 2:15 pm (C.E.T.)",CHF,0\r\nEXR.D.CHF.EUR.SP00.A,D,CHF,EUR,SP00,A,2000-01-04,1.6053,A,,,,P1D,,A,,,,,,,,,,4,,4F0,,Swiss franc/Euro,"ECB reference exchange rate, Swiss franc/Euro, 2:15 pm (C.E.T.)",CHF,0\r\nEXR.D.CHF.EUR.SP00.A,D,CHF,EUR,SP00,A,2000-01-05,1.606,A,,,,P1D,,A,,,,,,,,,,4,,4F0,,Swiss franc/Euro,"ECB reference exchange rate, Swiss franc/Euro, 2:15 pm (C.E.T.)",CHF,0\r\nEXR.D.CHF.EUR.SP00.A,D,CHF,EUR,SP00,A,2000-01-06,1.6068,A,,,,P1D,,A,,,,,,,,,,4,,4F0,,Swiss franc/Euro,"ECB reference exchange rate, Swiss franc/Euro, '
```

Excellent! Now we only need to load this response in a Pandas DataFrame. We can use 'StringIO' to read the strings as a file. This way we don't need to save it first and we can use it directly.

In \[7\]:

```
# Read the response as a file into a Pandas DataFrame
df = pd.read_csv(io.StringIO(response.text))
```

In \[8\]:

```
# Check the DataFrame's information
df.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4859 entries, 0 to 4858
Data columns (total 32 columns):
KEY                4859 non-null object
FREQ               4859 non-null object
CURRENCY           4859 non-null object
CURRENCY_DENOM     4859 non-null object
EXR_TYPE           4859 non-null object
EXR_SUFFIX         4859 non-null object
TIME_PERIOD        4859 non-null object
OBS_VALUE          4798 non-null float64
OBS_STATUS         4859 non-null object
OBS_CONF           238 non-null object
OBS_PRE_BREAK      0 non-null float64
OBS_COM            0 non-null float64
TIME_FORMAT        4859 non-null object
BREAKS             0 non-null float64
COLLECTION         4859 non-null object
COMPILING_ORG      0 non-null float64
DISS_ORG           0 non-null float64
DOM_SER_IDS        0 non-null float64
PUBL_ECB           0 non-null float64
PUBL_MU            0 non-null float64
PUBL_PUBLIC        0 non-null float64
UNIT_INDEX_BASE    0 non-null float64
COMPILATION        0 non-null float64
COVERAGE           0 non-null float64
DECIMALS           4859 non-null int64
NAT_TITLE          0 non-null float64
SOURCE_AGENCY      4859 non-null object
SOURCE_PUB         0 non-null float64
TITLE              4859 non-null object
TITLE_COMPL        4859 non-null object
UNIT               4859 non-null object
UNIT_MULT          4859 non-null int64
dtypes: float64(15), int64(2), object(15)
memory usage: 1.2+ MB
```

You can see there are 4858 rows, which makes sense for almost 19 years of daily prices. There are 32 columns, which is probably more than we need. We can inspect the DataFrame to see which columns we need.

In \[9\]:

```
# Show the last 5 entries of the DataFrame
df.tail()
```

Out\[9\]:

|  | KEY | FREQ | CURRENCY | CURRENCY\_DENOM | EXR\_TYPE | EXR\_SUFFIX | TIME\_PERIOD | OBS\_VALUE | OBS\_STATUS | OBS\_CONF | ... | COMPILATION | COVERAGE | DECIMALS | NAT\_TITLE | SOURCE\_AGENCY | SOURCE\_PUB | TITLE | TITLE\_COMPL | UNIT | UNIT\_MULT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4854 | EXR.D.CHF.EUR.SP00.A | D | CHF | EUR | SP00 | A | 2018-09-25 | 1.1376 | A | F | ... | NaN | NaN | 4 | NaN | 4F0 | NaN | Swiss franc/Euro | ECB reference exchange rate, Swiss franc/Euro,... | CHF | 0 |
| 4855 | EXR.D.CHF.EUR.SP00.A | D | CHF | EUR | SP00 | A | 2018-09-26 | 1.1369 | A | F | ... | NaN | NaN | 4 | NaN | 4F0 | NaN | Swiss franc/Euro | ECB reference exchange rate, Swiss franc/Euro,... | CHF | 0 |
| 4856 | EXR.D.CHF.EUR.SP00.A | D | CHF | EUR | SP00 | A | 2018-09-27 | 1.1371 | A | F | ... | NaN | NaN | 4 | NaN | 4F0 | NaN | Swiss franc/Euro | ECB reference exchange rate, Swiss franc/Euro,... | CHF | 0 |
| 4857 | EXR.D.CHF.EUR.SP00.A | D | CHF | EUR | SP00 | A | 2018-09-28 | 1.1316 | A | F | ... | NaN | NaN | 4 | NaN | 4F0 | NaN | Swiss franc/Euro | ECB reference exchange rate, Swiss franc/Euro,... | CHF | 0 |
| 4858 | EXR.D.CHF.EUR.SP00.A | D | CHF | EUR | SP00 | A | 2018-10-01 | 1.1414 | A | F | ... | NaN | NaN | 4 | NaN | 4F0 | NaN | Swiss franc/Euro | ECB reference exchange rate, Swiss franc/Euro,... | CHF | 0 |

5 rows × 32 columns

The columns we need are **'TIME\_PERIOD'** for the dates and **'OBS\_VALUE'** for the prices. Let's also do a sanity check on the prices in 'OBS\_VALUE'.

In \[10\]:

```
# Inspect the prices. Do the mean, minimum and maximum make sense?
df['OBS_VALUE'].describe()
```

Out\[10\]:

```
count    4798.000000
mean        1.379459
std         0.193938
min         0.981600
25%         1.205500
50%         1.467300
75%         1.547200
max         1.680300
Name: OBS_VALUE, dtype: float64
```

Now we will make a new DataFrame called 'ts' (for time series) with just the dates and EURCHF prices.

In \[11\]:

```
# Create a new DataFrame called 'ts'
ts = df.filter(['TIME_PERIOD', 'OBS_VALUE'], axis=1)
# 'TIME_PERIOD' was of type 'object' (as seen in df.info). Convert it to datetime first
ts['TIME_PERIOD'] = pd.to_datetime(ts['TIME_PERIOD'])
# Set 'TIME_PERIOD' to be the index
ts = ts.set_index('TIME_PERIOD')
# Print the last 5 rows to screen
ts.tail()
```

Out\[11\]:

|  | OBS\_VALUE |
| --- | --- |
| TIME\_PERIOD |  |
| 2018-09-25 | 1.1376 |
| 2018-09-26 | 1.1369 |
| 2018-09-27 | 1.1371 |
| 2018-09-28 | 1.1316 |
| 2018-10-01 | 1.1414 |

To conclude, we make a chart of the time series:

In \[12\]:

```
%matplotlib inline
ts.plot()
```

Out\[12\]:

```
<matplotlib.axes._subplots.AxesSubplot at 0x11d9beba8>
```

 ![](https://datacareergermany.mysmartjobboard.com/files/userfiles/image_exchangrates1.png)

## BONUS: pandaSDMX

Very often, there are already convenient Python packages available on the internet you can use. For instance, if you search the internet for "Python ECB SDMX" you will undoubtly find the 'pandaSDMX' package. It is, as they call it, a "Python client to retrieve and acquire statistical data and metadata disseminated in SDMX 2.1, an ISO-standard widely used by institutions such as statistics offices, central banks, and international organisations."

Interestingly, pandaSDMX ships with built-in support for the following agencies:

- Australian Bureau of Statistics (ABS)
- European Central Bank (ECB)
- Eurostat
- French National Institute for Statistics (INSEE)
- Instituto Nacional de la Estadìstica y Geografìa - INEGI (Mexico)
- International Monetary Fund (IMF) - SDMX Central only
- International Labour Organization (ILO)
- Italian statistics Office (ISTAT)
- Norges Bank (Norway)
- Organisation for Economic Cooperation and Development (OECD)
- United Nations Statistics Division (UNSD)
- UNESCO (free registration required)
- World Bank - World Integrated Trade Solution (WITS)

More information can be found at:[https://pandasdmx.readthedocs.io/en/latest/index.html](https://pandasdmx.readthedocs.io/en/latest/index.html)

In this last section, we are going to retrieve the same data (EURCHF daily exchange rates) with this package. First though, you need to install the package via 'pip' (via the command line):

**pip install pandasdmx**

Now let's get the data!

In \[13\]:

```
from pandasdmx import Request

# Define the source
ecb = Request('ECB')
```

In \[14\]:

```
# Retrieve the data (we start at 2016, because are requesting a larger dataset (including other frequencies))
data_response = ecb.data(resource_id = 'EXR', key={'CURRENCY': ['CHF', 'EUR']}, params = {'startPeriod': '2016'})
data = data_response.data
```

In \[15\]:

```
# The data will be a pandaSDMC 'DataSet'
type(data)
```

Out\[15\]:

```
pandasdmx.model.DataSet
```

In \[16\]:

```
# Show which frequencies are available ('D' is 'daily', you can probably guess the other ones)
set(s.key.FREQ for s in data.series)
```

Out\[16\]:

```
{'A', 'D', 'H', 'M', 'Q'}
```

In \[17\]:

```
# Filter the the daily data and 'write' it to a DataFrame
daily = (s for s in data.series if s.key.FREQ == 'D')
ts2 = data_response.write(daily)
ts2.tail()
```

Out\[17\]:

| FREQ | D |
| --- | --- |
| CURRENCY | CHF |
| CURRENCY\_DENOM | EUR |
| EXR\_TYPE | SP00 |
| EXR\_SUFFIX | A |
| TIME\_PERIOD |  |
| 2018-10-09 | 1.1381 |
| 2018-10-10 | 1.1412 |
| 2018-10-11 | 1.1430 |
| 2018-10-12 | 1.1470 |
| 2018-10-15 | 1.1428 |

In \[18\]:

```
%matplotlib inline
ts2.plot()
```

Out\[18\]:

```
<matplotlib.axes._subplots.AxesSubplot at 0x12235c080>
```

 ![](https://datacareergermany.mysmartjobboard.com/files/userfiles/image_exchangrates2.png)

As you can see, the pandaSDMX pacakage is another easy way to retrieve the same data. Hopefully these examples will help you get started. Thanks for reading!

About the author:  
Joris H., Python & open source enthusiast. Entrepreneur @ PythonSherpa - [https://www.pythonsherpa.com](https://www.pythonsherpa.com/)

Our website uses cookies so that we can provide you with the best user experience. By using our website, you agree to using cookies. [Read more](https://www.datacareer.de/terms-and-conditions-privacy-policy/)