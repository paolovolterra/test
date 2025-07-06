# mia funzione per estrarre il json Eurostat utile, passando i parametri necessari

from itertools import product
import requests
import pandas as pd

def fetch_eurostat_data(dataset, filters):
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
    query_parts = []
    for key, value in filters.items():
        if isinstance(value, list):
            query_parts.extend([f"{key}={v}" for v in value])
        else:
            query_parts.append(f"{key}={value}")
    query_str = "&".join(query_parts)
    url = f"{base_url}/{dataset}?{query_str}&format=JSON"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Errore {response.status_code}: {response.text}")
    data = response.json()
    dims = data["dimension"]
    dim_order = data["id"]
    dim_labels = {dim: dims[dim]["category"]["label"] for dim in dim_order}
    dim_keys = {dim: list(dim_labels[dim].keys()) for dim in dim_order}
    combinations = list(product(*[dim_keys[dim] for dim in dim_order]))
    records = []
    for i, combo in enumerate(combinations):
        if str(i) in data["value"]:
            record = {}
            for dim, key in zip(dim_order, combo):
                record[f"{dim}_code"] = key
                record[f"{dim}_label"] = dim_labels[dim][key]
            record["value"] = data["value"][str(i)]
            records.append(record)
    df = pd.DataFrame(records)
    if 'time_label' in df.columns:
        df['time'] = pd.to_datetime(df['time_label'], errors='coerce')
        mask_quarter = df['time'].isna() & df['time_label'].str.contains('Q')
        df.loc[mask_quarter, 'time'] = pd.PeriodIndex(df.loc[mask_quarter, 'time_label'], freq='Q').to_timestamp()
    return df
