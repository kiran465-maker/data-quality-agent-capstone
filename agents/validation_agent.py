from tools.data_profiler import profile_data
def compare_profiles(before, after):
    b = profile_data(before); a = profile_data(after)
    return {'before': b, 'after': a}
class ValidationAgent:
    def validate(self, before_df, after_df):
        return compare_profiles(before_df, after_df)
