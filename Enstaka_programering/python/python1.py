text="simon"
nr=24
hår=False
Hockeylag=["Djurgården","Aki","MODO"]
text="simme"
print(text)

if hår==True:
    print("Du har hår")
else:
    print("Du har inte hår")

while nr>4:
    print(nr)
    nr-=5

for tecken in text:
    print(tecken)

for lag in Hockeylag:
    print(lag)

def MestMål(Lag1,Lag2,Mål1,Mål2):
    if Mål1>Mål2:
        print(Lag1+ " gjorde fler mål än "+ Lag2)
    else:
        print(Lag2+ " gjorde fler mål än "+ Lag1)

MestMål(Hockeylag[0],Hockeylag[1],14,15)

from info import Statestik
Statestik()

