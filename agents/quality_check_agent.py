class QualityCheckAgent:
    def __init__(self):
        pass

    def run(self, df):
        if df is None:
            raise ValueError("[QualityCheckAgent] ERROR — No DataFrame received. Pipeline stopped.")

        print("[QualityCheckAgent] Running basic checks...")
        print(df.info())
        print(df.describe())

        # MUST RETURN df
        return df
