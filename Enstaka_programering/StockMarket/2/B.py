import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
style.use("ggplot")

fond = str(input("Jag vill se information på: "))
tidstart = str(input("Från: "))
tidslut = str(input("Till: "))

start = list(map(int, tidstart.split()))
end = list(map(int, tidslut.split()))

print(web.DataReader(fond, "yahoo", dt.datetime(start[0],start[1],start[2]), dt.datetime(end[0],end[1],end[2])))