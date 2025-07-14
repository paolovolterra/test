# Turnover in industry - manufacturing

#Eurostat #dataset 

The Turnover Index is a business cycle indicator showing the monthly evolution of the market of goods and services in the industrial sector. It also records the evolution of turnover over longer periods of time. The turnover of industry index is not deflated. It is therefore the objective of this indicator to measure the market activity in the industrial sector in value. Data are compiled according to the Statistical classification of economic activities in the European Community, (NACE Rev. 2, Eurostat). Industrial turnover is compiled as a \"fixed base year Laspeyres type volume-index\". The current base year is 2021 (Index 2021 = 100). The index is presented in calendar and seasonally adjusted form. Growth rates with respect to the previous month (M/M-1) are calculated from calendar and seasonally adjusted figures while growth rates with respect to the same month of the previous year (M/M-12) are calculated from calendar adjusted figures.


- https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/TEIIS150?geo=IT

  "id": [
    "freq",
    "indic_bt",
    "nace_r2",
    "unit",
    "geo",
    "time"
  ],
  "size": [1, 1, 1, 3, 1, 12],
  "dimension": {
    "freq": {
      "label": "Time frequency",
      "category": {
        "index": {
          "M": 0
        },
        "label": {
          "M": "Monthly"
        }
      }
    },
    
    "indic_bt": {      "label": "Business trend indicator",

          "NETTUR": "Net turnover"


    "nace_r2": {
      "label": "Statistical classification of economic activities in the European Community (NACE Rev. 2)",

          "I21_SCA": "Index, 2021=100 (SCA)",
          "PCH_M1_SCA": "Percentage change m/m-1 (SCA)",
          "PCH_M12_CA": "Percentage change m/m-12 (CA)"

