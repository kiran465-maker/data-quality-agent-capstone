def autofix(df):
    """
    Example auto-fix: fill missing values + fix string formatting.
    """
    df = df.copy()

    # Fill missing text with "MISSING"
    df = df.fillna("MISSING")

    # Trim extra spaces
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    return df
