# Förkortad verition av färdiga projectet, ganska likt, bara för att testa 'ai' så kommer ej vara kommenterad. Du måste ha laddat ner sp500 (kört project+ai)
import bs4 as bs
import requests
import datetime as dt
from datetime import timedelta
from matplotlib import style
style.use("ggplot")
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web 
import re
import os
clear = lambda: os.system("cls")
from random import randint
import pickle
with open("sp500tickers.pickle", "rb") as f:
    tickers = pickle.load(f)
Aktsier = pd.DataFrame(columns=["Stock","Antal"])
pengar = int(input("Pengar: "))
startpengar = pengar
zzz = 1
df = pd.read_csv("csv/A.csv", parse_dates=True, index_col=0)
for index, row in df.iterrows():
    indexx = index
    idag = list(map(int, re.split("-| |:",str(indexx))))
    while zzz <= 1:
        print(str(idag[0])+"-"+str(idag[1])+"-"+str(idag[2]), pengar)
        print(Aktsier[["Stock","Antal"]])
        x = randint(0,2)
        villgöra = ["0","0","0","0","0","0"]
        if x == 0:
            villgöra[0] = "sova"
            villgöra[2] = randint(1,10)
        else:
            villgöra[0] = "investera"
            if x == 1 and Aktsier["Antal"].astype(int).sum() > 0 and len(Aktsier.index) > 1:
                villgöra[4] = "sälja"
                villgöra[2] = Aktsier.at[randint(0,(len(Aktsier.index))-1), "Stock"]
            else:
                villgöra[4] = "köpa"
                villgöra[2] = tickers[randint(0,24)]
        if villgöra[0] == "sova":
            zzz = int(villgöra[2])
            break
        if villgöra[0] == "investera":
            dfinvest = pd.read_csv("csv/"+(str(villgöra[2])+".csv"), parse_dates=True, index_col=0)
            for index, row in Aktsier.iterrows():
                if villgöra[2] == (Aktsier.at[index, "Stock"]):
                    if villgöra[4] == "köpa" and pengar >= (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])):
                        villgöra[5] = randint(0,(int(pengar/dfinvest.at[indexx, "Open"].astype(int))))-1
                        Aktsier.loc[index, "Antal"] = (int(villgöra[5])+int(Aktsier.at[index, "Antal"]))
                        pengar -= (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])) 
                        break
                    elif int(villgöra[5]) <= int(Aktsier.at[index, "Antal"]) and villgöra[4] == "sälja":
                        if int(Aktsier.at[index, "Antal"]) > 1: villgöra[5] = randint(1,int(Aktsier.at[index, "Antal"]))
                        else: break
                        Aktsier.loc[index, "Antal"] = (int(Aktsier.at[index, "Antal"]))-(int(villgöra[5]))
                        pengar += (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5]))
                        break
            else:
                if (int((pengar)/(dfinvest.at[indexx, "Open"].astype(int)))) <= 1: break
                villgöra[5] = randint(1,(int((pengar)/(dfinvest.at[indexx, "Open"].astype(int)))))
                Aktsier = Aktsier.append({"Stock": villgöra[2], "Antal": villgöra[5]}, ignore_index=True)
                pengar -= (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5]))
    zzz-=1