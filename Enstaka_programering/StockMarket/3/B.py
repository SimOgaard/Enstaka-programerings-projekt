import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
style.use("ggplot")

import os
clear = lambda: os.system('cls')

fond=""
idk=0

while fond != "esc":
    if idk != 1:
        villgöra = str(input("Jag vill "))
        idk = 1
        if villgöra == "se information":
            continue
        elif villgöra == "esc":
            break
        elif villgöra == "se tillgänglig information":
            continue
        elif villgöra == "investera":
            continue
        else:
            idk = 0
            print(villgöra, "är inget alternativ")
            continue
    idk = 0

    if villgöra == "se information" or villgöra == "investera":
        fond = str(input("Jag vill se information på: "))

        tidstart = str(input("Från "))
        tidslut = str(input("till "))
        if villgöra == "investera":
            invest = str(input("och investera tills "))
            investto = list(map(int, invest.split()))

        start = list(map(int, tidstart.split()))
        end = list(map(int, tidslut.split()))

        df = web.DataReader(fond, "yahoo", dt.datetime(start[0],start[1],start[2]), dt.datetime(end[0],end[1],end[2]))

        valinfo = str(input("Jag vill se "))
        valinfoslice = valinfo.split()
        df = df[valinfoslice]
    else:
        csv = str(input("Jag vill se filen "))
        valinfo = str(input("Jag vill se "))
        df = pd.read_csv(csv, parse_dates=True, index_col=0)
        valinfoslice = valinfo.split()    
        df = df[valinfoslice]

    valvisa = ""
    while valvisa != "terminalen" or valvisa != "en graf":
        valvisa = str(input("Jag vill se informationen genom "))
        if valvisa == "terminalen":
            clear()
            print(df)
            break
        elif valvisa == "en graf":
            clear()
            df.plot()
            plt.show()
            break
        else:
            print(valvisa, "är inte ett alternativ")
    
    valspara = ""
    while valspara != "ja" and villgöra != "se tillgänglig information" or valspara != "nej" and villgöra != "se tillgänglig information":
        valspara = str(input("Jag vill spara informationen "))
        if valspara == "ja":
            df.to_csv(fond+".csv")
            break
        elif valspara == "nej":
            break
        else:
            print(valspara, "är inte ett alternativ")

    dff = web.DataReader(fond, "yahoo", dt.datetime(end[0],end[1],end[2]), dt.datetime(investto[0],investto[1],investto[2]))

    valinvesta = "kolla på information"
    valinvest = valinvesta.split()
    dag = 0
    dff["            du valde att"] = valinvesta
    dff["            antal aktsier"] = valinvest[1]

    if villgöra == "investera":
        for index, row in dff.iterrows():
            clear()
            df = dff.head(dag)
            if valvisa == "en graf" and dag != 0:
                df.plot()
                plt.show()
            else:
                print(df)
            valinvesta = str(input("Jag tänker "))
            valinvest = valinvesta.split()
            valinvest.append("")
            if valinvest[0] == "hålla" or valinvest[0] == "sälja" or valinvest[0] == "köpa":
                dff.at[index, "            du valde att"] = valinvest[0]
                dff.at[index, "            antal aktsier"] = valinvest[1]
                dag+=1
            else:
                print(valinvest, "är inte ett alternativ")
                continue