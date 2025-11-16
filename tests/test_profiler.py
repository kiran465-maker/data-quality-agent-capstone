from tools.data_profiler import profile_data
import pandas as pd

def test_profile():
    df = pd.DataFrame({'a':[1,None,3]})
    res = profile_data(df)
    assert 'missing' in res
