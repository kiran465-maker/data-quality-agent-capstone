import pandas as pd

def ingest_data(source_path=None, json_data=None):
    """
    Ingests data either from CSV file or directly from JSON input.
    """
    if json_data:
        return pd.DataFrame(json_data)
    
    if source_path:
        return pd.read_csv(source_path)
    
    raise ValueError("Provide either JSON data or a CSV path.")
