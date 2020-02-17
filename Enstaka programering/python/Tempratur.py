import MySQLdb
import pygal

db = MySQLdb.connect(host="localhost",
                    user="simon",
                    password="tempratur",
                    db="temp")

cur = db.cursor()

cur.execute("SELECT * FROM temp")

Tempratur= []
Fuktighet= []
Vindhastighet= []

for row in cur.fetchall():
    print(row[1])
    Tempratur.append(row[1])
    Fuktighet.append(row(2))
    Vindhastighet.append(row[3])
    rows= len(row)
    for r in row:
        print(r)

cur.close()
db.close()

bankchart= pygal.Pie()
bankchart.title= "Väder"
bankchart.add("Tempratur i Celcius", 20)

antalkunder= len(bankkunder)-1
print(antalkunder)
while antalkunder >=0:
    bankchart.add(bankkunder[antalkunder],pengar[antalkunder])
    antalkunder-=1

temp =45
temp2=34
horizontalbar_chart = pygal.HorizontalBar()
horizontalbar_chart.title = 'tempature in celius(in %)'
horizontalbar_chart.add('temp today:', temp)
horizontalbar_chart.add('temp yesterday:', temp2)
horizontalbar_chart.add('temp 7/8', 39.4)
horizontalbar_chart.add('temp 6/8', 42.1)
horizontalbar_chart.add('temp 5/8', 32.2)
horizontalbar_chart.render()
horizontalbar_chart.render_to_file('bar_chart.svg')