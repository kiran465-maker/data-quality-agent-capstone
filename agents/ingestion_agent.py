import pandas as pd, os
class IngestionAgent:
    def ingest(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        df = pd.read_csv(path)
        return {'status':'loaded','rows':len(df),'columns':list(df.columns),'df':df}
