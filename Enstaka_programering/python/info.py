

Rubrik = ["Alla barn", "Ett  barn", "Tvillingar", "Trillingar"]
Allabarn= [56898,54894,56016,57414,60790]
Ettbarn= [55669,53718 ,54949, 56443,59739]
Tvillingar = [1219,1163,1058,961,1042]
Trillingar = [10,13,9,10,9]

Startår= 2012

def Statestik():
    AntalVarv= len(Allabarn)
    while AntalVarv>0:
        print("Dansk statestik år "+ str(Startår+AntalVarv))
        print(Rubrik[0]+"  "+ str(Allabarn[AntalVarv-1]))
        print(Rubrik[1]+"  "+ str(Ettbarn[AntalVarv-1]))
        print(Rubrik[2]+"  "+ str(Tvillingar[AntalVarv-1]))
        Tvillinggranskning(Tvillingar[AntalVarv-1],Startår+AntalVarv)
        print(Rubrik[3]+"  "+ str(Trillingar[AntalVarv-1]))
        AntalVarv-=1


def Tvillinggranskning(antaltvillingar,vilketar):
    if antaltvillingar>3000:
        print("Det har fötts fler tvillingar än det förväntades år" +str(vilketar))
    else:
        print("Det har fötts färre tvillingar än det förväntades år "+str(vilketar))


     