from agents.ingestion_agent import IngestionAgent
from agents.quality_check_agent import QualityCheckAgent
from agents.autofix_agent import AutoFixAgent
from agents.validation_agent import ValidationAgent
from agents.reporting_agent import ReportingAgent
from agents.memory_agent import MemoryAgent
import os

DATA_IN = os.path.join('data','input','raw.csv')
OUT_DIR = os.path.join('data','output')

def main():
    ingest = IngestionAgent()
    qc = QualityCheckAgent()
    autofix = AutoFixAgent()
    val = ValidationAgent()
    reporter = ReportingAgent()
    memory = MemoryAgent()

    res = ingest.ingest(DATA_IN)
    df = res['df']
    issues = qc.run(df)
    df_fixed, fixes = autofix.run(df, issues)
    validation = val.validate(df, df_fixed)
    reporter.generate(df, df_fixed, issues, fixes, validation, OUT_DIR)
    memory.save('last_run', {'issues': issues, 'fixes': fixes, 'validation': validation})
    print('Pipeline complete. Outputs written to', OUT_DIR)

if __name__ == '__main__':
    main()
