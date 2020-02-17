import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd
style.use("ggplot")

df = pd.read_csv("tsla.csv", parse_dates=True, index_col=0)
print(df)