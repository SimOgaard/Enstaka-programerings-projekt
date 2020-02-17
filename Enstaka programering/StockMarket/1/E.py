import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
style.use("ggplot")

df = pd.read_csv("tsla.csv", parse_dates=True, index_col=0)
df["Volume"].plot()
df[["High","Low","Open","Close","Adj Close"]].plot()
plt.show()