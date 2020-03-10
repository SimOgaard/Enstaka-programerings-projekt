import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
style.use("ggplot")
import re

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                'B': [5, 6, 7, 8, 9],
                'C': ['a', 'b', 'c', 'd', 'e']})

print(df)

df = df.replace({'B': {5: 100, 8: 400}})

print(df)

df.loc[0, "A"] = 10000

print(df)