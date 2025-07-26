---
title: "How to use the ECB API with Python"
source: "https://ramin.org/posts/ecb-api-python"
author:
  - "[[ramin azhdari]]"
published:
created: 2025-07-12
description:
tags:
  - "clippings"
---
If you – like me – had a hard time understanding the ECB API from its [official documentation](https://data.ecb.europa.eu/help/api/data) this guide is for you. We will walk through an example in which we query 10 year and 1 year maturity government bond yield curves. I will show you how to smoothly extract and plot whatever ECB dataset you need with the help of a few simple functions.

The ECB API is based on the Statistical Data and Metadata Exchange ([SDMX](https://en.wikipedia.org/wiki/SDMX)) standard. The standard is quite painful to work with directly, which is why we will be using the `sdmx1` Python library to interact with the API, as well as `pandas` itself. You can find the official `sdmx1` documentation [here](https://sdmx1.readthedocs.io/en/latest/index.html).

## Setup

To get started we need to install the libraries, if you haven’t done so already.

```bash
pip install sdmx1
pip install pandas
```

For the rest of the examples you will need to have the following setup in your file/notebook.

```python
import sdmx
import pandas as pd

ecb = sdmx.Client("ECB")
```

## List available dataflows

To start exploring the available data we will need a list of the available *dataflows* (in the SDMX standard a *dataflow* is called a collection of datasets that have the same form). You can do this manually by visiting their [Datasets](https://data.ecb.europa.eu/data/datasets) page or programmatically like this:

```python
def get_available_dataflows(client):
    dataflow_message = client.dataflow()
    dataflows_df = sdmx.to_pandas(dataflow_message.dataflow)
    dataflows_df.name = f"{client.source.id} Dataflows"
    return dataflows_df

dataflows = get_available_dataflows(ecb)
dataflows

"""
Outputs a Series with the dataflow's id as the index
and its name as the value:

AME                                                AMECO
BKN                                 Banknotes statistics
BLS                       Bank Lending Survey Statistics
BNT        Shipments of Euro Banknotes Statistics (ESCB)
BOP    Euro Area Balance of Payments and Internationa...
                             ...
SUR                                      Opinion Surveys
TGB                                      Target Balances
TRD                                       External Trade
WTS                                        Trade weights
YC                   Financial market data - yield curve
Name: ECB Available Dataflows, Length: 80, dtype: object
"""
```

## Understanding a dataflow

In this example we will use the ECB’s "Financial market data - yield curve" (`'YC'`) *dataflow*. Now we need to gather the information needed to specify which of the dataflow’s datasets we want to use. These *dataflows* are usually very big and the API will refuse to respond if our query is too broad. In SDMX terms this is called *slicing the dataflow*.

First we need to find out how to use our dataflow. We can query the API to receive some metadata about the dataflow. This metadata includes the *data structure definition* and the *constraints*.

The *data structure definition* includes the *dimensions* of the *dataflow*. *Dimensions* specify concepts of the recorded values, like which currency was used or what is the frequency of the data points.

But everything in the *data structure definition* doesn’t define **which** currency was actually used and with **which** frequency the data points have. For this we need the *constraints* which define that.

```python
def get_dataflow_metadata(client, dataflow_id):
    dataflow_message = ecb.dataflow(dataflow_id)
    return (
        dataflow_message.dataflow[dataflow_id].structure,
        dataflow_message.constraint[f"{dataflow_id}_CONSTRAINTS"].data_content_region[0],
        dataflow_message.dataflow[dataflow_id].name
    )

yc_data_structure_definition, yc_constraints, yc_name = get_dataflow_metadata(ecb, 'YC')
yc_data_structure_definition

"""
Output:

<DataStructureDefinition ECB:ECB_FMD2(1.0): Financial market data (not related to foreign exchange)>
"""
```

The first thing we can take a look at is which *dimensions* our *dataflow* uses. Here is how we query the full list of *dimensions* and store them in a pandas Series:

```python
def get_dataflow_dimensions(data_structure_definition, dataflow_name):
    dimensions = data_structure_definition.dimensions
    return pd.Series({
        dimension.id: dimension.concept_identity.name
        for dimension in dimensions
    }, name=f"'{dataflow_name}' Dimensions")

yc_dimensions = get_dataflow_dimensions(yc_data_structure_definition, yc_name)
yc_dimensions

"""
Outputs a Series with the dimension's id as the index
and its name as the value:

FREQ                                         Frequency
REF_AREA                                Reference area
CURRENCY                                      Currency
PROVIDER_FM                  Financial market provider
INSTRUMENT_FM              Financial market instrument
PROVIDER_FM_ID    Financial market provider identifier
DATA_TYPE_FM                Financial market data type
TIME_PERIOD                       Time period or range
Name: 'Financial market data - yield curve' Dimensions,
dtype: object
"""
```

Now that we know which dimensions exist we will need to figure out which values have been used in our *dataflow*. These values are called *codes* and they come in standardized *codelists*.

There are a lot more concepts in the standard that further define a dataflow and its properties, but we will keep it pragmatic and only look at what we need. To find out which *codes* are implemented for our dataflow we need to look at the *constraints*.

The raw constraint data returned by the API is a bit difficult to work with, which is why we use a few helper functions to collect each *dimension* with the *codes* we can use as a list of pandas Series.

```python
def get_code_description(code, dimension):
    codelist = dimension.local_representation.enumerated
    return codelist[code].name

def get_constraint_codes(constraints, dimension):
    try:
        codes = constraints.member[dimension.id].values
    except:
        return pd.Series(name=f"'{dimension.id}' Codes", dtype='object')

    codes_with_description = {
        code.value: get_code_description(code.value, dimension)
        for code in codes
    }
    return pd.Series(codes_with_description, name=f"'{dimension.id}' Codes")

def get_constraints_with_codes(data_structure_definition, constraints):
    dimensions = data_structure_definition.dimensions
    return [
        get_constraint_codes(constraints, dimension)
        for dimension in dimensions
    ]

yc_constraints_with_codes = get_constraints_with_codes(yc_data_structure_definition, yc_constraints)
yc_constraints_with_codes

"""
Outputs a list of Series.
The Series' index is set to the code's id and
its value to the code's name.
The Series' name itself is set to the dimension's id:

[
 B    Daily - businessweek
 Name: 'FREQ' Codes, dtype: object,

 U2    Euro area (changing composition)
 Name: 'REF_AREA' Codes, dtype: object,

 EUR    Euro
 Name: 'CURRENCY' Codes, dtype: object,

 4F    ECB
 Name: 'PROVIDER_FM' Codes, dtype: object,

 G_N_W    Government bond, nominal, all issuers whose ra...
 G_N_A    Government bond, nominal, all issuers whose ra...
 G_N_C    Government bond, nominal, all issuers all rati...
 Name: 'INSTRUMENT_FM' Codes, dtype: object,
 ...
]
"""
```

As you can see the dataflow only uses the *code* "B" which stands for "Daily - businessweek" for the *dimension* "Frequency" (`'FREQ'`).

### Shortcut: Series Keys

If you are in a hurry and you just want to see a list of all the available datasets, you can query the *series keys* of a dataflow. This shows you a list of which datasets are available inside the dataflow.

*Series Keys* are the arrangement of the different dimension codes that define a given dataset.

Here is how we query the list

```python
def parse_series_key(series_key):
    result = {value.id: value.value for value in series_key.values.values()}
    return result

def get_dataflow_series_keys(client, dataflow_id, dataflow_name):
    data_message = client.series_keys('YC')
    series_keys = [parse_series_key(series_key) for series_key in list(data_message)]
    df = pd.DataFrame.from_records(series_keys)
    df.name = f"'{dataflow_name}' Series Keys"
    return df

series_keys = get_dataflow_series_keys(ecb, 'YC', yc_name)
series_keys

"""
Output:

FREQ REF_AREA CURRENCY PROVIDER_FM INSTRUMENT_FM PROVIDER_FM_ID DATA_TYPE_FM
0 B U2 EUR 4F G_N_C SV_C_YM SR_25Y5M
1 B U2 EUR 4F G_N_C SV_C_YM SR_25Y6M
2 B U2 EUR 4F G_N_C SV_C_YM SR_25Y7M
3 B U2 EUR 4F G_N_C SV_C_YM SR_25Y8M
4 B U2 EUR 4F G_N_C SV_C_YM SR_25Y9M
... ... ... ... ... ... ... ...
2160 B U2 EUR 4F G_N_A SV_C_YM IF_5Y6M
2161 B U2 EUR 4F G_N_A SV_C_YM IF_5Y7M
2162 B U2 EUR 4F G_N_A SV_C_YM IF_5Y8M
2163 B U2 EUR 4F G_N_A SV_C_YM IF_5Y9M
2164 B U2 EUR 4F G_N_A SV_C_YM IF_6M
2165 rows × 7 columns
"""
```

This way we can directly see which datasets are available for the code we are looking for.

```python
series_keys[series_keys.DATA_TYPE_FM == 'SR_10Y']

"""
Output:

FREQ REF_AREA CURRENCY PROVIDER_FM INSTRUMENT_FM PROVIDER_FM_ID DATA_TYPE_FM
579 B U2 EUR 4F G_N_C SV_C_YM SR_10Y
1655 B U2 EUR 4F G_N_A SV_C_YM SR_10Y
"""
```

Afterwards we could just copy those values and use them for the next step where we define the keys that we use to *slice the dataflow*.

## Querying datasets

Now that we have all the information in hand we can query the datasets we want to download. For our example we’re interested in the *codes* "Yield curve spot rate, 10-year maturity" (`'SR_10Y'`) and "Yield curve spot rate, 1-year maturity" (`'SR_1Y'`) from the "Financial market data type" (`'DATA_TYPE_FM'`) *dimension*, as well as the *code* "Government bond, nominal, all issuers whose rating is triple A" (`'G_N_A'`) from the "Financial market instrument" (`'INSTRUMENT_FM'`) *dimension*.

The standard also allows to optionally add a `startPeriod` and/or `endPeriod` parameter. We will limit the data to everything from 2012 onwards.

The following function will return the data as a pandas DataFrame with the time period set as the index and the columns set to the different dimension arrangements.

**Important:** When you query the dataflow for datasets make sure that they are all in the same frequency (`'FREQ'`) otherwise pandas will not be able to align the index based on the time period.

```python
def get_column(series_key):
    column = series_key.attrib.TITLE.value
    return column if len(column) <= 90 else column[:90] + '...'

def get_unit(data_message):
    unit_codelist = data_message.structure.attributes.get('UNIT').local_representation.enumerated
    series_key = next(iter(data_message.data[0].series))
    return unit_codelist[series_key.attrib.UNIT.value].name.localized_default()

def get_datasets(client, dataflow_id, keys=None, startPeriod=None, endPeriod=None, data_structure_definition=None):
    data_message = client.data(dataflow_id, key=keys, params={'startPeriod': startPeriod, 'endPeriod': endPeriod})

    df = sdmx.to_pandas(data_message, datetime={'dim': 'TIME_PERIOD'})
    columns = [get_column(series_key) for series_key in data_message.data[0].series]

    return df, columns, unit

yc_df, yc_columns, yc_unit = get_datasets(
    ecb,
    'YC',
    keys={'DATA_TYPE_FM': ['SR_10Y', 'SR_1Y'], 'INSTRUMENT_FM': ['G_N_A'], 'FREQ': 'B'},
    startPeriod='2012',
)
yc_df

"""
Output:

FREQ                         B
REF_AREA                    U2
CURRENCY                   EUR
PROVIDER_FM                 4F
INSTRUMENT_FM            G_N_A
PROVIDER_FM_ID         SV_C_YM
DATA_TYPE_FM  SR_10Y     SR_1Y
TIME_PERIOD
2012-01-02  2.717862  0.135763
2012-01-03  2.744522  0.117707
2012-01-04  2.776691  0.103733
2012-01-05  2.784807  0.161397
2012-01-06  2.788371  0.187312
... ... ...
2023-08-08  2.523608  3.285734
2023-08-09  2.567893  3.325601
2023-08-10  2.578223  3.325811
2023-08-11  2.688460  3.349347
2023-08-14  2.692476  3.366395
2966 rows × 2 columns
"""
```

If you receive an error fetching the data your request might be either too big or there is no available data for your key. In both cases the API responds with a **404 error**.

## Plotting the data

We can plot the data thanks to pandas with a simple lines of code.

```python
import matplotlib.pyplot as plt

yc_data.plot(title=yc_name)
plt.legend(yc_columns, loc='upper left', title=None)
plt.xlabel(None)
plt.ylabel(yc_unit)
```

[![YC datasets plotted](https://ramin.org/images/ecb-api-python-0.jpeg "YC Datasets Plotted")](https://ramin.org/images/ecb-api-python-0.jpeg)

Now you should know everything needed to query the ECB’s API with ease! If you want to dig deeper, `sdmx1` 's [docs](https://sdmx1.readthedocs.io/) are a great place to start otherwise if you have any questions feel free to reach out to me.