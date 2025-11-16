from tools.data_profiler import profile_data
class QualityCheckAgent:
    def run(self, df):
        return profile_data(df)
