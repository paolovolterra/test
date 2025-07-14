# Gross domestic product (GDP) and main components (output, expenditure and income)

#PIL #GDP #dataset #Eurostat 

- _Fonte: Banca Intesa. (2025). _La variante iberica: Un confronto tra la performance  economica di Italia e Spagna_. [blob:https://imi.intesasanpaolo.com/629f973f-4c7f-4c7e-aba1-45a67bbd98da](https://doi.org/blob:https://imi.intesasanpaolo.com/629f973f-4c7f-4c7e-aba1-45a67bbd98da)
- https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?geo=IT&s_adj=SCA
- "id":"freq","unit","s_adj","na_item","geo","time"


## "CLV20_MEUR": "Chain linked volumes (2020), million euro",

![](../codice/media/20250707112807.png)


## 

- Dataset Eurostat `namq_10_gdp`
- Variabili:
    - `na_item = B1GQ` (PIL reale)
    - `unit = CLV20_MEUR` (volumi concatenati, base 2020, milioni di euro)
    - `s_adj = SCA` (destagionalizzato e corretto per calendario)
    - `geo = ['IT', 'DE', 'FR', 'ES']`

![](../codice/media/Pasted%20image%2020250707122520.png)


## PIL pro-capite, 2019 4° trim. = 100. Fonte: Intesa Sanpaolo, Eurostat

![](../codice/media/Pasted%20image%2020250707125258.png)



# Dimensioni

## unit - Unit of measure

- "CLV_I20": "Chain linked volumes, index 2020=100",
- "CLV_I15": "Chain linked volumes, index 2015=100",
- "CLV_I10": "Chain linked volumes, index 2010=100",
- "CLV_I05": "Chain linked volumes, index 2005=100",
- "PC_GDP": "Percentage of gross domestic product (GDP)",
- "CP_MEUR": "Current prices, million euro",
- "CP_MNAC": "Current prices, million units of national currency",
- "CLV20_MEUR": "Chain linked volumes (2020), million euro",
- "CLV15_MEUR": "Chain linked volumes (2015), million euro",
- "CLV10_MEUR": "Chain linked volumes (2010), million euro",
- "CLV05_MEUR": "Chain linked volumes (2005), million euro",
- "CLV20_MNAC": "Chain linked volumes (2020), million units of national currency",
- "CLV15_MNAC": "Chain linked volumes (2015), million units of national currency",
- "CLV10_MNAC": "Chain linked volumes (2010), million units of national currency",
- "CLV05_MNAC": "Chain linked volumes (2005), million units of national currency",
- "CLV_PCH_PRE": "Chain linked volumes, percentage change on previous period",
- "CLV_PCH_SM": "Chain linked volumes, percentage change compared to same period in previous year",
- "CLV_PCH_ANN": "Chain linked volumes, annualized percentage change on previous period",
- "PYP_MEUR": "Previous year prices, million euro",
- "PYP_MNAC": "Previous year prices, million units of national currency",
- "CON_PPCH_PRE": "Contribution to GDP growth, percentage point change on previous period",
- "CON_PPCH_SM": "Contribution to GDP growth, percentage point change compared to same period in previous year",
- "PD20_EUR": "Price index (implicit deflator), 2020=100, euro",
- "PD15_EUR": "Price index (implicit deflator), 2015=100, euro",
- "PD10_EUR": "Price index (implicit deflator), 2010=100, euro",
- "PD05_EUR": "Price index (implicit deflator), 2005=100, euro",
- "PD20_NAC": "Price index (implicit deflator), 2020=100, national currency",
- "PD15_NAC": "Price index (implicit deflator), 2015=100, national currency",
- "PD10_NAC": "Price index (implicit deflator), 2010=100, national currency",
- "PD05_NAC": "Price index (implicit deflator), 2005=100, national currency",
- "PD_PCH_PRE_EUR": "Price index (implicit deflator), percentage change on previous period, euro",
- "PD_PCH_PRE_NAC": "Price index (implicit deflator), percentage change on previous period, national currency",
- "PD_PCH_SM_EUR": "Price index (implicit deflator), percentage change compared to same period in previous year, euro",
- "PD_PCH_SM_NAC": "Price index (implicit deflator), percentage change compared to same period in previous year, national currency"

## s_adj - Seasonal adjustment

- "SCA": "Seasonally and calendar adjusted data"


## na_item - National accounts indicator (ESA 2010)

- "B1GQ": "Gross domestic product at market prices",
- "B1G": "Value added, gross",
- "P3": "Final consumption expenditure",
- "P3_S13": "Final consumption expenditure of general government",
- "P31_S13": "Individual consumption expenditure of general government",
- "P32_S13": "Collective consumption expenditure of general government",
- "P31_S14_S15": "Household and NPISH final consumption expenditure",
- "P31_S14": "Final consumption expenditure of households",
- "P31_S15": "Final consumption expenditure of NPISH",
- "P41": "Actual individual consumption",
- "P5G": "Gross capital formation",
- "P51G": "Gross fixed capital formation",
- "P52_P53": "Changes in inventories and acquisitions less disposals of valuables",
- "P52": "Changes in inventories",
- "P53": "Acquisitions less disposals of valuables",
- "P6": "Exports of goods and services",
- "P61": "Exports of goods",
- "P62": "Exports of services",
- "P7": "Imports of goods and services",
- "P71": "Imports of goods",
- "P72": "Imports of services",
- "B11": "External balance of goods and services",
- "B111": "External balance - goods",
- "B112": "External balance - services",
- "D1": "Compensation of employees",
- "D11": "Wages and salaries",
- "D12": "Employers' social contributions",
- "B2A3G": "Operating surplus and mixed income, gross",
- "D2X3": "Taxes on production and imports less subsidies",
- "D2": "Taxes on production and imports",
- "D3": "Subsidies",
- "D21X31": "Taxes less subsidies on products",
- "D21": "Taxes on products",
- "D31": "Subsidies on products",
- "YA1": "Statistical discrepancy (production approach)",
- "YA0": "Statistical discrepancy (expenditure approach)",
- "YA2": "Statistical discrepancy (income approach)",
- "P3_P5": "Final consumption expenditure and gross capital formation",
- "P3_P6": "Final consumption expenditure, gross capital formation and exports of goods and services"

## time

- "1975-Q1": 0,
- "1975-Q2": 1,
- "1975-Q3": 2,
- "1975-Q4": 3,
- ....
- "2024-Q2": "2024-Q2",
- "2024-Q3": "2024-Q3",
- "2024-Q4": "2024-Q4",
- "2025-Q1": "2025-Q1"