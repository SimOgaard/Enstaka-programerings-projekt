import MySQLdb
import pygal

from pygal.style import Style
custom_style = Style(
    colors=('#999999','#ff0000'))

db = MySQLdb.connect(host="localhost",
                    user="root",
                    password="",
                    db="termometer")

cur = db.cursor()

cur.execute("SELECT * FROM tempratur1")

Tid=[]
Tempratur=[]

for row in cur.fetchall():
    print(row[0])
    Tempratur.append(row[1])
    print(row[1])
    Tid.append(row[0])

bar_chart = pygal.Bar(style=custom_style)
bar_chart.title="Klimat"

counter= len(Tid)
counter= len(Tempratur)

while counter>0:
    #bar_chart.add('Tid',Tid[counter],"Tempratur", Tempratur[counter])                                  y u no work?
    bar_chart.add("Tid",Tid[counter])
    bar_chart.add("Tempratur", Tempratur[counter])
    counter-=1

bar_chart.add("Tid",Tid[0])
bar_chart.add("Tempratur",Tempratur[1])

bar_chart.render_to_file('bar_chart.svg')
bar_chart.render_in_browser()