import pandas as pd
import numpy as np
"""
This file is learn basics of Pandas
"""

#Series:

series = pd.Series([1,2,3,4,5])
print(series)

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
print(df)