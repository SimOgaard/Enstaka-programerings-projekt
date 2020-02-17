import bs4 as bs # importerar bibloteket beautiful soup 4 som bs som kan hämta data ut ur html och xml filer 
import requests # importerar request som tillåter oss att skicka http requests
import datetime as dt # importerar datetime som dt som levererar klasser för att manipiluera datum och tider
from datetime import timedelta # tar timedelta av bibloteket datetime för att ändra på datum och tider
from matplotlib import style # vem orkar göra fina grafer när bibloteket matplotlib har din rygg
style.use("ggplot") # detta är stilen som vi använder, det finns fler
import matplotlib.pyplot as plt # låter oss ändra graferna, tänk som scss
import pandas as pd # huvud bibloteken pandas som tillhandshåller datastrukturer och dataanalysverktyg
import pandas_datareader.data as web # pandas tillåter oss även att hämta och läsa data från webben pandas är ta mig tusan fantastiskt
import re # tillåter dig att matcha eller hitta andra str
import os # "operating system" helt enkelt låter oss ändra i ui (terminalen)
clear = lambda: os.system("cls") # här sätter vi upp en funktion kallad clear, den raderar allt som visas i terminalen
from random import randint # randit(a,b) ger oss "random" värden mellan a-b
import pickle # ett sätt att konvertera ett pythonobject (list etc) till ett teckenflöde

allfiles = 0 # definerar en int med värde 0 som kallas allfiles
print("Detta krävs ej men om du funderar på att köra 'ai' flertals gånger eller under långa tidsintervall rekomenderas detta, Under extrema tidsintervall kör quick.py istället där det krävs att du har laddat ner:") # skriver ut str i terminalen
download = str(input("Jag 'vill' / 'vill inte' ladda ner informationen ")) # input funktion, skriver ut str och tillåtes inmatning av str, int, float
if not os.path.exists("csv"): os.makedirs("csv") # om csv mapp ej finns skapas csv mappen
if os.path.exists("sp500tickers.pickle"):
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
else:
    table = bs.BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies").text, "lxml").find("table", {"class":"wikitable sortable"}) # skapar en request till wiki, får tillgång till text som vi gör om till "soup" genom (bs) de kan användas mer som ett python object
    tickers = [] # skapar en lista kallad tickers
    for row in table.findAll("tr")[1:]: # för varje rad efter huvudet [1:]
        ticker = row.find_all('td')[0].text # tar vi .text från table data och kallar ticker
        tickers.append(ticker[:-1]) # och lägger till till våran lista
    with open("sp500tickers.pickle","wb") as f: # sparar våran fil för att användas i quick.py
        pickle.dump(tickers,f)
for ticker in tickers[:25]: # för varje ticker i de första 25 tickers
    if not os.path.exists("csv/{}.csv".format(ticker)): # kollar om filen i csv mappen kallad ticker.csv inte finns
        if download == "vill": # kollar om download är vill
            df = web.DataReader(ticker, "yahoo", dt.datetime(2016, 1, 1), dt.datetime.now()) # hämtar en data ram på aktsien ticker från 2010 1 1 tills idag
            df.to_csv("csv/{}.csv".format(ticker)) # tar den hämtade data ramen och skapar en csv fil till csv mapen kallad ticker
    else: allfiles += 1
    if allfiles >= 25: download = "vill" # om alla filer är nerladdade ändra download så vi vet i framtiden
def tex(medelande): # funktioner vid anrop tar inmatningen och lägger på en angiven str och skriver ut den i terminalen
    tex="| tex: "+medelande 
    print(tex)
def kap(medelande):
    kap="| "+medelande+"; alla kapitalicerade ord får du välja"
    print(kap)
def line():
    line="-------------------------------------------------------------------------------------------------------------------------------------"
    print(line)
def WARNING(medelande):
    WARNING = "*** "+medelande+" ***"
    print(WARNING)

WARNING("OM PROGRAMMET F**K AR UPP SÄNK INT I 'timedelta(days=5)' TILLS DET FUNKAR DÅ MARKNADEN KANSKE INTE ÄR ÖPPEN DET KAN ÄVEN VARA NÄR AI KÖRS DÅ ETT ERROR LIKT KeyError: 1494892800000000000 UPPSTÅR, DÄR NÅGON AKTSIE I sp500 INTE HAR VÄRDET FÖR DATUMET DÅ KAN DU VARA TVUNGEN ATT RADERA CSV MAPPEN")
howtoval = str(input("Jag 'vill' / 'vill inte' se en how to "))
if howtoval == "vill":
    line()
    kap("Du kommer få välja vilket datum du vill börja din buisniss 'ÅR MÅN DAG' och startkapital '$' samt om 'JAG'/'AI' ska köra") # anropar funktionen kap medelande blir stringen
    tex("2019 4 20")
    tex("4206942")
    tex("jag")
    tex("ai")
    line()
    print("| Och du kommer få investera tills datumet är dagens datum eller du går bankrupt. Sedan kommer du få valet att skriva:")
    line()
    kap("'sova i ANTAL dagar'; där du går förbi ANTAL dagar")
    tex("sova i 1 dag")
    line()
    kap("'se info om AKTSIE från ÅR MÅN DAG genom EN GRAF / TERMINALEN'")
    tex("se info om tsla från 2019 3 12 genom en graf")
    tex("se info om googl från 2019 2 19 genom terminalen")
    line()
    kap("'investera i AKTSIE och KÖPA/SÄLJA ANTAL aktsier'")
    tex("investera i roku och köpa 11 aktsier")
    tex("investera i intc och sälja 1000 aktsier")
Aktsier = pd.DataFrame(columns=["Stock","Antal","Position","Live","täljare","nämnare"]) # skapar en data ram kallad aktsier som har 6 colummer
summary = pd.DataFrame(columns=["Datum", "Pengar", "Aktsier", "AktsierVärde", "PengarTot"])
AktsierSummary = pd.DataFrame(columns=["Datum"])
noneedbutineedcuzimbadandcantthinkstraight = -1 # självförklarande
zzz = 1
dag = str(input("Datum: "))
pengar = int(input("Pengar: "))
startpengar = pengar
spelare = str(input("Spelare: "))
if spelare == "jag": person = "du"
else: person = "ai"
start = list(map(int, dag.split())) # splittar str dag till en list och definerar sedan de som ints
df = web.DataReader("TSLA", "yahoo", dt.datetime(start[0],start[1],start[2]), dt.datetime(2020,1,1)) # dt.datetime.today() - timedelta(days=10)) # hemtar en data ram kallad df, med info tagen från yahoo, om aktsiebolaget tsla från angiven tid tills idag, tar bort x antal dagar för att hindra flervärden i framtida hämtad data. Detta är för att få fram dagarna du investerar i, ger oss öppen/stängd marknad.

for index, row in df.iterrows(): # för varje index (Date) i hela data ramen df
    indexx = index # datumet blir indexx då index kommer i andra ställen användas
    if spelare == "jag": clear()
    idag = list(map(int, re.split("-| |:",str(indexx)))) # Date visar - : så funktionen .split() funkar ej, re.split kan ha flera parameters (kan inte ordet på svenska)
    for index, row in Aktsier.iterrows(): Aktsier.loc[index, "Live"] = (pd.read_csv(("csv/"+str(Aktsier.at[index, "Stock"])+".csv"), parse_dates=True, index_col=0).at[indexx, "Open"].astype(int) * int(Aktsier.at[index, "Antal"])) # för varje index i aktsie (de aktiser vi äger) ändrar vi live värdet som är antalet aktsier * nupriset
    while pengar > 0 or Aktsier["Antal"].astype(int).sum() > 0: # så länge pengar och aktsier är naturliga körs allt innom, break används för att skippa dagar
        if zzz <= 1: # är falsk då antalet dagar du vill sova är mindre än eller lika med 1
            print("Det är den", str(idag[0])+"-"+str(idag[1])+"-"+str(idag[2]), "och", person, "erhåller", pengar, "$. Här är aktsierna:")
            print(Aktsier[["Stock","Antal","Position","Live"]]) # skriver ut stock antal... från data ramen aktsier
            if spelare == "jag": villgöra = str(input("Jag vill ")).split()
            else:
                x = randint(0,2)
                villgöra = ["0","0","0","0","0","0"]
                if x == 0:
                    villgöra[0] = "sova"
                    villgöra[2] = randint(1,10)
                else:
                    villgöra[0] = "investera"
                    if x == 1 and Aktsier["Antal"].astype(int).sum() > 0 and len(Aktsier.index) > 1: # kollar så att ai äger aktsier
                        villgöra[4] = "sälja"
                        villgöra[2] = Aktsier.at[randint(0,(len(Aktsier.index))-1), "Stock"] # random nummer från 0 till antalet ägda aktsier som sedan hänger ihop med aktsien som ai väljer
                    else:
                        villgöra[4] = "köpa"
                        villgöra[2] = tickers[randint(0,24)] # random aktsie från de 25 i tickers
            if spelare == "jag": clear()
            if villgöra[0] == "sova":
                zzz = int(villgöra[2])
                break # hoppar ut ur loopen den är i
            if villgöra[1] == "info":
                dfinfo = web.DataReader(villgöra[3], "yahoo", dt.datetime(int(villgöra[5]),int(villgöra[6]),int(villgöra[7])), dt.datetime(idag[0],idag[1],idag[2]))
                if villgöra[9] == "en":
                    dfinfo[["High", "Low", "Open", "Close", "Adj Close"]].plot() # sätter in high, low... i en graf
                    plt.show() # visar grafen
                else: print(dfinfo)
            if villgöra[0] == "investera":
                for index, row in Aktsier.iterrows(): 
                    if villgöra[2] == (Aktsier.at[index, "Stock"]): # om aktsien vald finns i dataramen aktsier
                        dfinvest = pd.read_csv("csv/"+(str(villgöra[2])+".csv"), parse_dates=True, index_col=0) # vet vi att den är nerladdad och kan läsa från csvfilen
                        if villgöra[4] == "köpa" and pengar >= (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])): # om valet är att köpa och du har råd
                            if spelare != "jag": villgöra[5] = randint(0,(int(pengar/dfinvest.at[indexx, "Open"].astype(int))))-1 # antalet som ska köpas anges i random nummer mellan 0 och antalet möjliga
                            Aktsier.loc[index, "Antal"] = (int(villgöra[5])+int(Aktsier.at[index, "Antal"])) # ändrar värdet på antalet aktsier till de förra + de inköpta i dataramen aktsier
                            pengar -= (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])) # subtraherar kostnaden 
                            Aktsier.loc[index, "täljare"] += (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])) # ändrar värdet på täljare,nämnare för att få fram din possition, aktsier saker svårt att förklara, du får fråga
                            Aktsier.loc[index, "nämnare"] += int(villgöra[5]) 
                            Aktsier.loc[index, "Position"] = ((int(Aktsier.at[index, "täljare"]) / int(Aktsier.at[index, "nämnare"])) * int(Aktsier.at[index, "Antal"]))
                            Aktsier.loc[index, "Live"] = (pd.read_csv(("csv/"+str(Aktsier.at[index, "Stock"])+".csv"), parse_dates=True, index_col=0).at[indexx, "Open"].astype(int) * int(Aktsier.at[index, "Antal"]))
                            break
                        elif int(villgöra[5]) <= int(Aktsier.at[index, "Antal"]) and villgöra[4] == "sälja": # lik ovan
                            if spelare != "jag" and int(Aktsier.at[index, "Antal"]) > 1: villgöra[5] = randint(1,int(Aktsier.at[index, "Antal"]))
                            elif spelare != "jag": break
                            Aktsier.loc[index, "Antal"] = (int(Aktsier.at[index, "Antal"]))-(int(villgöra[5]))
                            pengar += (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5]))
                            Aktsier.loc[index, "Position"] = ((int(Aktsier.at[index, "täljare"]) / int(Aktsier.at[index, "nämnare"])) * int(Aktsier.at[index, "Antal"]))
                            Aktsier.loc[index, "Live"] = (pd.read_csv(("csv/"+str(Aktsier.at[index, "Stock"])+".csv"), parse_dates=True, index_col=0).at[indexx, "Open"].astype(int) * int(Aktsier.at[index, "Antal"]))
                            if Aktsier.at[index, "Antal"] == 0 and person == "jag": Aktsier = Aktsier.drop([Aktsier.index[index]])
                            break
                        elif villgöra[4] == "sälja":
                            WARNING("tsktsktsk, för lite aktsier")
                            break
                else:
                    if download == "vill" and spelare != "jag": dfinvest = pd.read_csv(("csv/"+str(villgöra[2])+".csv"), parse_dates=True, index_col=0) # ai kan bara använda sig av de 25 aktsierna från p500, är de nerladdade läs från fil
                    else:
                        dfinvest = web.DataReader(villgöra[2], "yahoo", dt.datetime(idag[0],idag[1],idag[2]), dt.datetime.today()) # annars måste vi ta från webben
                        dfinvest.to_csv(("csv/"+str(villgöra[2])+".csv").format(ticker)) # sparar lokalt så nästa gång vi slipper köra från webben
                    if spelare != "jag":
                        if (int((pengar)/(dfinvest.at[indexx, "Open"].astype(int)))) <= 1: break
                        villgöra[5] = randint(1,(int((pengar)/(dfinvest.at[indexx, "Open"].astype(int)))))
                    if (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])) > pengar and villgöra[4] == "köpa": WARNING("nonono, för lite pengar")
                    if villgöra[4] == "köpa" and (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])) <= pengar:
                        if spelare == "jag": dfinvest.to_csv(("csv/"+str(villgöra[2])+".csv").format(ticker))
                        Aktsier = Aktsier.append({"Stock": villgöra[2], "Antal": villgöra[5], "täljare": (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])), "nämnare": int(villgöra[5]), "Position": (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])), "Live": (dfinvest.at[indexx, "Open"].astype(int)) * int(villgöra[5])}, ignore_index=True)
                        pengar -= (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5]))
                    elif (dfinvest.at[indexx, "Open"].astype(int) * int(villgöra[5])) < pengar: WARNING("oof, inga aktsier, ajda")
        else:
            zzz-=1
            break
    summary = summary.append({"Datum": indexx.strftime("%Y-%m-%d"), "Pengar": pengar, "Aktsier": Aktsier["Antal"].astype(int).sum(), "AktsierVärde": Aktsier["Live"].astype(int).sum(), "PengarTot": (pengar + Aktsier["Live"].astype(int).sum())}, ignore_index=True) # ändrar båda dataramarna med info om hur det gick för varje dag
    AktsierSummary = AktsierSummary.append({"Datum": indexx.strftime("%Y-%m-%d")}, ignore_index=True)
    noneedbutineedcuzimbadandcantthinkstraight += 1
    for index, row in Aktsier.iterrows():
        if not Aktsier.at[index, "Stock"] in AktsierSummary: AktsierSummary[Aktsier.at[index, "Stock"]] = 0
        AktsierSummary.loc[noneedbutineedcuzimbadandcantthinkstraight, Aktsier.at[index, "Stock"]] = Aktsier.at[index, "Live"]
lastly = "då" # massa saker för att få sista meningen korrekt, det är allt självförklarande
if startpengar >= pengar+Aktsier["Live"].astype(int).sum():
    conclution = "Aktsier är inte så lätt va?"
    laaaastly = "back"
else:
    conclution = "Ez game, ez life"
    laaaastly = "plus"
if startpengar >= pengar+Aktsier["Live"].astype(int).sum() and spelare == "ai":
    conclution = "datorer är fortfarande bra ok..."
    lastly = "fastän"
elif spelare == "ai": conclution = "datorer är helt enkelt bättre"

print(person.title(), "började med", startpengar, "$ och efter", len(summary.index), "dagar slutade", person, "med", pengar, "$ och", Aktsier["Antal"].astype(int).sum(), "aktsier med totalt värde på", Aktsier["Live"].astype(int).sum(), "$ sammanlagt slutade", person, "med", (pengar + Aktsier["Live"].astype(int).sum()), "$.", conclution, lastly, person, "gick", laaaastly, "med", abs(startpengar-(pengar + Aktsier["Live"].astype(int).sum())), "$")
summary[["Pengar", "AktsierVärde", "PengarTot"]].plot()
plt.xticks(summary.index,summary["Datum"].values) # sätter x axelns värden till datum
plt.tick_params(axis="x", rotation=90) # ändrar x axelns rotation på datum
plt.show()

AktsierSummary.plot()
plt.xticks(AktsierSummary.index,AktsierSummary["Datum"].values)
plt.tick_params(axis="x", rotation=90)
plt.show()