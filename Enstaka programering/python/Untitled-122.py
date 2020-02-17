import MySQLdb
import pygal

db = MySQLdb.connect(host="localhost",
                    user="bankkvinna",
                    password="bank",
                    db="verksamhet")

cur = db.cursor()

cur.execute("SELECT * FROM bank")

bankkunder= []
pengar =[]

for row in cur.fetchall():
    print(row[1])
    bankkunder.append(row[1])
    pengar.append(row(2))
    rows= len(row)
    for r in row:
        print(r)

cur.close()
db.close()

bankchart= pygal.Pie()
bankchart.title= "bankens resurser"
bankchart.add("vladmir", 10405)

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