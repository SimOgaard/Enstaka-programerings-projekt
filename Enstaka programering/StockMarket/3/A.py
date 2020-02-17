import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
style.use("ggplot")

df = web.DataReader("TSLA", "yahoo", dt.datetime(2019,4,1), dt.datetime(2019, 4, 10))
print(df)

invest = str(input("invest?"))

if invest == "ja":
    print(df.tail(1))
    df = web.DataReader("TSLA", "yahoo", dt.datetime(2019,4,10), dt.datetime.now())
    print(df)
    print(df.tail(1))