def validate_data(df):
    """
    Very basic validation example. Expand as needed.
    """
    issues = []

    if df.empty:
        issues.append("Dataset is empty.")

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            issues.append(f"Column '{col}' has missing values.")

    return {"validation_issues": issues}
