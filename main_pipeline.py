from agents.ingestion_agent import ingest_data
from agents.quality_check_agent import detect_quality_issues
from agents.autofix_agent import autofix
from agents.validation_agent import validate_data
from agents.reporting_agent import generate_reports

def run_pipeline(input_json):
    """
    Complete end-to-end pipeline called by app.py
    """

    # 1. Ingest
    df = ingest_data(json_data=input_json["data"])

    # 2. Quality check (Gemini included)
    quality_report = detect_quality_issues(df)

    # 3. Auto-fix
    fixed_df = autofix(df)

    # 4. Validate
    validation_report = validate_data(fixed_df)

    # 5. Export reports
    generate_reports(fixed_df, quality_report, validation_report)

    return {
        "quality_report": quality_report,
        "validation_report": validation_report,
        "message": "Processing complete. Check data/output/"
    }
