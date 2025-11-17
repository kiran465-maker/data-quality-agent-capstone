import pandas as pd
import os

class AutoFixAgent:

    def __init__(self, output_path="data/output/cleaned.csv"):
        self.output_path = output_path

    def run(self, df):
        # Example fix
        df = df.fillna("UNKNOWN")

        # SAVE CLEANED FILE
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        df.to_csv(self.output_path, index=False)

        print(f"[AutoFixAgent] Cleaned file saved to: {self.output_path}")
        return df
