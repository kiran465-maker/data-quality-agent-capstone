from tools.gemini_helper import ask_gemini

def detect_quality_issues(df):
    """
    Runs quality checks and asks Gemini to analyze issues.
    """
    summary = {
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "duplicates": int(df.duplicated().sum())
    }

    prompt = f"""
    You are a data quality expert.
    Analyze the following dataset summary:
    {summary}
    
    Identify all issues and explain solutions in simple language.
    """

    gemini_insights = ask_gemini(prompt)

    return {
        "summary": summary,
        "gemini_feedback": gemini_insights
    }
