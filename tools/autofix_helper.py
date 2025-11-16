import pandas as pd
def attempt_fixes(df, issues):
    df2 = df.copy()
    if 'amount' in df2.columns:
        df2['amount'] = pd.to_numeric(df2['amount'], errors='coerce')
    if 'country' in df2.columns:
        df2['country'] = df2['country'].str.upper().str.replace('.', '', regex=False).str.strip()
    if 'email' in df2.columns:
        df2['email'] = df2['email'].where(df2['email'].str.contains('@', na=False))
    if 'date' in df2.columns:
        df2['date'] = pd.to_datetime(df2['date'], errors='coerce')
    df2 = df2.fillna(method='ffill').fillna(method='bfill')
    df2 = df2.drop_duplicates()
    return df2
