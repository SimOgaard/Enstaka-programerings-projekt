import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
style.use("ggplot")

df = web.DataReader("TSLA", "yahoo", dt.datetime(2019,4,1), dt.datetime.now())
df.to_csv("tsla.csv")