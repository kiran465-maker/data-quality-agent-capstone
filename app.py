from agents.ingestion_agent import IngestionAgent
from agents.quality_check_agent import QualityCheckAgent
from agents.autofix_agent import AutoFixAgent
from agents.validation_agent import ValidationAgent
from agents.reporting_agent import ReportingAgent

class DataQualityPipeline:

    def __init__(self):
        self.ingestor = IngestionAgent()
        self.qc = QualityCheckAgent()
        self.autofix = AutoFixAgent()
        self.validator = ValidationAgent()
        self.report = ReportingAgent()

    def run(self):
        print("\n=== DATA QUALITY AGENT PIPELINE STARTED ===\n")

        df = self.ingestor.run()
        print("\n[STEP 1] Ingestion completed.\n")

        df = self.qc.run(df)
        print("\n[STEP 2] Quality Check completed.\n")

        df = self.autofix.run(df)
        print("\n[STEP 3] Autofix completed.\n")

        self.validator.run(df)
        print("\n[STEP 4] Validation completed.\n")

        self.report.run("Pipeline completed successfully.")
        print("\n[STEP 5] Reporting completed.\n")

        print("\n=== PIPELINE FINISHED SUCCESSFULLY ===\n")


if __name__ == "__main__":
    pipeline = DataQualityPipeline()
    pipeline.run()
