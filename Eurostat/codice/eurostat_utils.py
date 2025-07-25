from itertools import product
import requests
import pandas as pd
from dateutil import parser


def parse_time_label(t):
    """Converte una stringa tempo (anno, trimestre o mese) in datetime."""
    t = str(t)
    try:
        if "-Q" in t:
            return pd.Period(t, freq='Q').to_timestamp()
        elif len(t) == 6 and t.isdigit():
            return pd.to_datetime(t, format="%Y%m")
        elif len(t) == 4 and t.isdigit():
            return pd.to_datetime(t + "-01-01")
        else:
            return parser.parse(t)
    except Exception:
        return pd.NaT


def fetch_eurostat_data(dataset, filters):
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"

    # Costruzione URL
    query_parts = []
    for key, value in filters.items():
        if isinstance(value, list):
            query_parts.extend([f"{key}={v}" for v in value])
        else:
            query_parts.append(f"{key}={value}")
    query_str = "&".join(query_parts)
    url = f"{base_url}/{dataset}?{query_str}&format=JSON"

    # Richiesta dati
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Errore {response.status_code}: {response.text}")
    data = response.json()

    # Parsing dimensioni
    dims = data["dimension"]
    dim_order = data["id"]
    dim_labels = {dim: dims[dim]["category"]["label"] for dim in dim_order}
    dim_keys = {dim: list(dim_labels[dim].keys()) for dim in dim_order}

    # Combinazioni
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

    # Costruzione DataFrame
    df = pd.DataFrame(records)

    # Parsing data intelligente
    if 'time_label' in df.columns:
        df['time'] = df['time_label'].apply(parse_time_label)
        df = df[df['time'].notna()]  # opzionale: rimuove righe malformate

    return df
