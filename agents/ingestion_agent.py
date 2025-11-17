import pandas as pd
import os

class IngestionAgent:

    def __init__(self, input_path="data/input/raw.csv"):
        self.input_path = input_path

    def run(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(
                f"[ERROR] Input file not found: {self.input_path}\n"
                "Place a CSV file inside data/input/raw.csv"
            )

        df = pd.read_csv(self.input_path)
        print(f"[IngestionAgent] Loaded file from: {self.input_path}")
        return df
