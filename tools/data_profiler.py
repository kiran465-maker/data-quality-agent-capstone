import numpy as np
def profile_data(df):
    missing = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())
    types = {c: str(df[c].dtype) for c in df.columns}
    stats = {}
    try:
        stats = df.describe(include=[np.number]).to_dict()
    except Exception:
        stats = {}
    return {'missing': missing, 'duplicates': duplicates, 'types': types, 'numeric_stats': stats}
