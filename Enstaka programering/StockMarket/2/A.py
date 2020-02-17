import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
style.use("ggplot")

fond = str(input("Jag vill se information på: "))

print(web.DataReader(fond, "yahoo", dt.datetime(2019,4,1), dt.datetime.now()))