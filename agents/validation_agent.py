import json
import os

class ValidationAgent:

    def __init__(self, output_path="data/output/validation_report.json"):
        self.output_path = output_path

    def run(self, df):
        report = {
            "rows": len(df),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict()
        }

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        with open(self.output_path, "w") as f:
            json.dump(report, f, indent=4)

        print(f"[ValidationAgent] Report saved to: {self.output_path}")
        return report
