# citat="datatyper har inga inbyggda metoder"
# Citat=citat.title()
# print(Citat)

# print("mata in ett flyttal")
# heltal=int(input("> "))
# print("närmaste heltal är "+str(heltal))

# print("Hej")
# print("vad är ditt förnamn?")
# fnamn=(input("> "))
# print("vad är ditt efternamn?")
# enamn=(input("> "))
# print("trevligt att träffas "+str(fnamn), str(enamn))

# print("hur gammal är du?")
# alder=int(input("> "))
# if alder >= 18:
#     print("du är redan myndig")
# else:
#     mynd=18-alder
#     print("du är myndig om "+str(mynd),"år")

# print("hur många vill äta 2 korvar")
# tvåkorv=int(input("> "))
# print("hur många vill äta 3 korvar")
# trekorv=int(input("> "))
# print("hur många vill äta 2 veganska korvar")
# tvåvkorv=int(input("> "))
# print("hur många vill äta 3 veganska korvar")
# trevkorv=int(input("> "))
# antalpackkorv=tvåkorv*2+trekorv*3
# apk=int(antalpackkorv/8)
# # print("du behöver köpa", str(apk), "förpackningar korvar")
# antalpackVkorv=tvåvkorv*2+trevkorv*3
# apVk=int(antalpackVkorv/4)
# # print("du behöver köpa", str(apVk), "förpackningar vego korvar")
# dryck=tvåkorv+trekorv+tvåvkorv+trevkorv
# # print("du behöver köpa in", str(dryck), ("drickor"))
# betala=int(apk*20.95+apVk*34.95+dryck*13.95)
# # print("kostnaden blir", str(betala), "kr")
# print(".:KORVKOLLEN:.")
# print("----------------------------")
# print("Hur många elever vill ha...")
# print("2 vanliga korvar -",str(tvåkorv))
# print("3 vanliga korvar -",str(trekorv))
# print("2 veganska korvar -",str(tvåvkorv))
# print("4 veganska korvar -",str(trevkorv))
# print("----------------------------")
# print("-INKÖPSLISTA-")
# print("----------------------------")
# print("Vanlig korv:",str(apk),"förpackningar")
# print("Vegansk korv:",str(apVk),"förpackningar")
# print("Dryck:",str(dryck),"drickor")
# print("----------------------------")
# print(str(betala), "SEK")
# print("----------------------------")

# male=["11","12","13","14","15"]
# female=["21","22","23","24","25"]

# print (male[0])
# print (female[2])
# print (female[4])
# print (male[1])

# del male[2]
# del female[0]

# male.append("simon")

# male.sort()
# female.sort()

# print("män:", male)
# print("kvinnor:", female)
# print("vem vill du ta bort?")
# simsalabim = str(input("> "))
# people=male+female
# people.remove(simsalabim)
# print(people)

# nummer=range(100)
# summan=0
# for mängd in nummer:
#     summan += mängd
# print(summan)

# mängd = range(500)
# summan=0
# for nummer in mängd:
#     if(nummer%2 = 1)
#         summan += nummer
# print (summan)

# registrerade = [" Anna ", " Eva ", " Erik ", " Lars ", " Karl "]
# avanmälningar = [" Anna ", " Erik ", " Karl "]

# for person in avanmälningar:
#     registrerade.remove(person)

# print ( registrerade )

# 123123123123
# förnamn =[" Maria ", " Erik ", " Karl "]
# efternamn =[" Svensson ", " Karlsson ", " Andersson "]

# for person in förnamn:
#     for persons in efternamn:
#         förnamn.append(efternamn)
# print(förnamn)

# DanielRadcliffe = ["man", "brun", "brun"]

# print("Är du man eller kvinna?")
# Kön=str(input("> "))
# print("Vad är din hårfärg?")
# Hårfärg=str(input("> "))
# print("Vad är din ögonfärg?")
# Ögonfärg=str(input("> "))

# if Kön in DanielRadcliffe:
#     if Hårfärg in DanielRadcliffe:
#         if Ögonfärg in DanielRadcliffe:
#             print("du är danielradcliffie")
#         else:
#             print("du är inte danielradcliffie")

# Åldrar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Sömnbehov = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5]

# print("skriv in din ålder")
# Ålder = int(input("> "))

# if Ålder in Åldrar:
#     timmar = Sömnbehov[Ålder-1]
# else:
#     timmar = 8
# print("du bör såva", timmar, "timmar")

# print("skriv in ett land tack!")
# Land = str(input("> "))

# Norden = ["danmark", "finnland"]
# Storbritanien = ["england", "skottland"]

# if Land.lower() in Norden:
#     print(Land, "beffiner sig i Norden")
# elif Land.lower() in Storbritanien:
#     print(Land, "befinner sig i Storbrittanien")
# else:
#     print("ditt land ligger inte på kartan")

# print("Ange ett positivt heltal")
# Heltal = int(input("> "))
# print(Heltal, "Är ett ")

# import requests
# url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm/"
# r = requests.get(url)
# response_dictionary = r.json()
# # Nu inneh ˚a ller response_dictionary objektet vi
# # h¨a mtade fr˚an API:et.
# print(response_dictionary)

# person = {
#     "first_name" : "Johan",
#     "last_name" : "Svensson",
#     "age" : 25 ,
#     "pets" : [
#         {
#             "name" : "Morris",
#             "age": 3,
#             "type" : "dog"
#         },
#         {
#             "name" : "Lisa",
#             "age" : 2,
#             "type" : "cat"
#         },
#     ]   
# }

# full_name = person["first_name"] + " " + person["last_name"]
# total_pets = str(len(person["pets"]))
# age = str (person["age"])
# print(full_name, "is", age, "years old and has", total_pets , "pets.")

# # pet_name = person["pets"][0]["name"]
# # pet_age = person["pets"][0]["age"]
# # pet_type = person["pets"][0]["type"]
# # print ("* A", pet_age , "year old", pet_type , "named", pet_name)
# # pet_name = person["pets"][1]["name"]
# # pet_age = person["pets"][1]["age"]
# # pet_type = person ["pets"][1]["type"]
# # print ("* A", pet_age , "year old", pet_type , "named", pet_name )

# for pet in person ["pets"]:
#     print("* A", pet ["age"] , "year old", pet ["type"], "named", pet ["name"])

# import requests

# print("Ange ett positivt heltal")
# tal = int(input("> "))

# url = "http://77.238.56.27/examples/numinfo/?integer="+str(tal)
# r = requests.get(url)
# response_dictionary = r.json()

# print(tal, "is even =", response_dictionary["even"], "is a prime number =", response_dictionary["prime"])
# print("talets faktorer är", response_dictionary["factors"])

# import requests

# print("skriv namnet på staden som du vill ha en prognos på")
# stad = str(input("> "))

# url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+str(stad)
# r = requests.get(url)
# response_dictionary = r.json()

# for forecast in response_dictionary["forecasts"]:
#     print(forecast["date"], forecast["forecast"])

# 123123123123
# import requests
# url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
# r = requests.get(url)
# response_dictionary = r.json()



# for artist in response_dictionary["artists"]:
#     print(artist["name"])

# response_dictionary=response_dictionary["artists"]

# print("jag vill ha artisten")
# artistt = str(input("> "))

# for artister in response_dictionary:
#     print(artister)
#     if artister.name == artistt:
#         artistid = artister.id

# url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+str(artistid)
# r = requests.get(url)
# response_dictionary = r.json()
# print(response_dictionary["artist"])

# 123123123
# print("Ange multiplikationstabell")
# tabell = int(input("> "))
# ggr = 1
# startggr = 3
# yn = "ja"
# while ggr <= startggr:
#     print(ggr*tabell)
#     ggr+=1
#     if ggr == (startggr+1):
#         print("Fortsätt?")
#         yn = str(input("> "))
#         startggr+3
#     if yn == "ja":
#         print("hej")
#         continue
#     else:
#         break


# thenumber = 10
# antalgissningar = 1
# yournumber = thenumber+1
# while yournumber != thenumber:
#     yournumber = int(input("> "))
#     if(yournumber > thenumber):
#         print("Lower")
#         antalgissningar += 1
#         continue
#     elif(yournumber < thenumber):
#         print("Higher")
#         antalgissningar += 1
#         continue
#     print(thenumber)
#     print("is correct")
#     print("it took you " + str(antalgissningar) + " guesses")
#     break

# print("Ange distans")
# yourdistance = int(input("> "))
# print("Ange metric")
# metric = str(input("> "))

# def km_to_miles(dist):
#     miles = yourdistance * 0.621371192
#     print(miles)

# def miles_to_km(dist):
#     km = yourdistance * 1.609344
#     print(km)

# if metric == "km":
#     km_to_miles(yourdistance)
# else:
#     miles_to_km(yourdistance)¨

# # import requests
# url = str(input("> "))

# # def lamao(url):
# #     r = requests.lamao(url)
# #     response_dictionary = r.json()
# #     print(response_dictionary)

# from lol import lamao
# lamao(url)



# def ui():
    

# ui.line ()
# ui.header ("EXEMPEL")
# ui.line (True)
# ui.echo ("Detta är ett exempel på hur")
# ui.echo ("ett grännsnitt kan se ut.")
# ui.line ()
# ui.header (".. vad vill du göra?")
# ui.line ()
# ui.echo ("A | Visa inköpslista")
# ui.echo ("B | Lägg till vara")
# ui.echo ("C | Ta bort vara")
# ui.echo ("X | Stäng programmet")
# ui.line ()
# ui.prompt ("Val")

# def line(bol=False):
#     amount = 30
#     rad=""
#     if(bol==False):
#         while amount >= 0:
#             rad+="-"
#             amount-=1
#         print(rad)
#     else:
#         while amount >= 0:
#             rad+="*"
#             amount-=1
#         print(rad)

# def header(medelande):
#     mellanrumm=""
#     leangthstring=((30-len(medelande))/2)-1
#     while leangthstring >= 0:
#         mellanrumm+=" "
#         leangthstring-=1
#     header="|"+mellanrumm+medelande+mellanrumm+"|"
#     print(header)

# def echo(medelande):
#     echo="| "+medelande
#     print(echo)

# def promt(medelande):
#     val = (input("| "+medelande))

#     if val == "a":
#         print("visar lista")
#     elif val == "b":
#         print("vilken vara vill du lägga in")
#     elif val == "c":
#         print("vilken vara vill du ta bort")
#     elif val == "x":
#         print("stänger programmet")
#     else:
#         print("wtf is wrong with u ill ocme over there and bash ur head in u fuikng")

# line()
# header("EXEMPEL")
# line(True)
# echo("Detta är ett exempel på hur")
# echo("ett grännsnitt kan se ut.")
# line()
# header("vad vill du göra?")
# line()
# echo("A | Visa inköpslista")
# echo("B | Lägg till vara")
# echo("C | Ta bort vara")
# echo("X | Stäng programmet")
# line()
# promt("Val ")




import requests
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)
response_dictionary = r.json()

for artist in response_dictionary["artists"]:
    print(artist["name"])

response_dictionary=response_dictionary["artists"]

print("jag vill ha artisten")
artistt = str(input("> "))

for artister in response_dictionary:
    if artister["name"] == artistt:
        url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"]
        r = requests.get(url)
        response_dictionary = r.json()
        print(response_dictionary)

def line(bol=False):
    amount = 30
    rad=""
    if(bol==False):
        while amount >= 0:
            rad+="-"
            amount-=1
        print(rad)
    else:
        while amount >= 0:
            rad+="*"
            amount-=1
        print(rad)

def header(medelande):
    mellanrumm=""
    leangthstring=((30-len(medelande))/2)-1
    while leangthstring >= 0:
        mellanrumm+=" "
        leangthstring-=1
    header="|"+mellanrumm+medelande+mellanrumm+"|"
    print(header)

def echo(medelande):
    echo="| "+medelande
    print(echo)

def promt(medelande):
    val = (input("| "+medelande))

    if val == "a":
        print("visar lista")
    elif val == "b":
        print("vilken vara vill du lägga in")
    elif val == "c":
        print("vilken vara vill du ta bort")
    elif val == "x":
        print("stänger programmet")
    else:
        print("wtf is wrong with u ill ocme over there and bash ur head in u fuikng, detta är ett skämt från en meme ok dont freak out its not an treath aight im just bored rn")

line()
header("EXEMPEL")
line(True)
echo("Detta är ett exempel på hur")
echo("ett grännsnitt kan se ut.")
line()
header("vad vill du göra?")
line()
echo("A | Visa inköpslista")
echo("B | Lägg till vara")
echo("C | Ta bort vara")
echo("X | Stäng programmet")
line()
promt("Val ")