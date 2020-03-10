from tkinter import * # importerar allt från tkinter
import time # importerar tid som vi kan använda som en delay
from random import randint # importerar randint från random som ger "slumper" fastän datorer inte kan

# variabler
korttidsminne=[] # minne som vi anväder i looking short term
långtidsminne=[] # minne som vi använder i looking long term
energi=50 # en variabel som används för musens steg

mouse=[5,5] # minne för vart han är men inte vart han står det är denhär vi ändrar på när vi flyttar på musen, dock så printar vi honnom vid rad 223
cheeseeaten=0 # räknar hur många ostar musen ätit
cheeseamount=100 # hur många ostar som kan ligga på plan
currentcheeses=0 # hur många ostar det är på plan
cheeseplaces=[[3,3],[2,1],[4,5],[7,3],[2,8],[9,1],[5,7],[8,3],[4,1],[2,7],[5,4],[19,19],[19,0],[0,19],[0,0],[7,0],[12,0],[16,7],[16,5],[13,16],[9,13],[19,15],[13,13],[9,17],[14,12],[9,11],[15,12],[9,19],[12,15],[10,10],[12,18],[12,17],[16,11],[12,15],[11,16],[17,19],[18,18],[16,4],[19,5],[19,15],[16,1],[16,2],[13,3],[9,4],[19,6],[13,5],[9,7],[14,8],[9,5],[15,1],[9,5],[12,4],[10,3],[12,2],[12,1],[1,11],[2,15],[1,16],[7,19],[8,18],[1,11],[3,1],[9,15],[3,16],[2,13],[7,12],[1,11],[6,11],[6,18],[8,18]] # vart ostartna kan placeras
speed=0.5 # time som vi importar för att hålla koll på hur snabbt saker händer
ormspeed=0.5 # -II-

def Movespeed(): # egen gjord def som ändrar musens speed altså sänker "delayn" till varje steg den tar, ändras efter hur många ostar den ätit
    global speed
    print(cheeseeaten)
    if cheeseeaten > 5 and cheeseeaten < 10:
        speed=0.4
    elif cheeseeaten > 10 and cheeseeaten < 15:
        speed=0.3
    elif cheeseeaten > 15:
        speed=0.2

def Wanderrandom (steps): # metod som säger åt musen att gå
    steglista=[] # idk really
    formerstep=5 # sätter variabel till 5
    while steps>0: # medans den är större än 0
        samma=False # är detta falskt så den kommer i slutet ta och subtrahera ett till denna variabeln
        typavsteg=randint(0,3) # sätter variabeln till ett "random" nummer från 0-3
        if typavsteg==0 and formerstep!=1: # här används de nummret för vilket steg den ska ta
            steglista.append("upp")
        elif typavsteg==1 and formerstep!=0:
            steglista.append("ner")
        elif typavsteg==2 and formerstep!=3:
            steglista.append("vänster")
        elif typavsteg==3 and formerstep!=2:
            steglista.append("höger")
        else:
            samma=True # om nu nummret varken var 0-3 så kommer den att ta ett nytt nummer inte säker men tror
        if samma==False: # om samma är falskt så kommer den
            formerstep=typavsteg # overvrita former step till typavsteg
            steps-=1 # sedan subtrahera ett steg
    return steglista

def MovePlanner(steps):
    whattodo=randint(0,3) # sätter variabeln whattodo till 0-3 på "random"
    if whattodo==0: # beroende på nummret
        print("lång") # så skriver den i terminalen antingen lång/kort osv
        korttidsminne=Lookinlongterm(steps) # den kan antingen använda sig utav de tre olika metoderna looking long term
    elif whattodo==1:
        print("korttids")
        korttidsminne=Lookinshortterm(steps) # looking short term
    else:
        print("random")
        korttidsminne=Wanderrandom(steps) # eller wanderrandom det är större chans att den går random 0,1 går inte random 2,3 går random
    print(korttidsminne)
    return korttidsminne

def Lookinlongterm(steps):
    if len(långtidsminne)==0: # om det inte finns något långtidsminne
        return Wanderrandom(steps) # går den random
    else: # annars
        print(långtidsminne) #printar den ut minnet (vart den har gått)
        Memoryplace=randint(0,len(långtidsminne)-1)
        Minnet=långtidsminne[Memoryplace]
        målX=Minnet[0]-mouse[0]
        print(Minnet+mouse)
        målY=Minnet[1]-mouse[1]
        steglista=[]
        while steps>0: # och medans steggen är större än 0 så kommer den
            if målX<0: # om den har gått på under sig (x axeln)
                steglista.append("upp") # går den upp osv
                målX+=1
            elif målX>0:
                steglista.append("ner")
                målX-=1
            elif målY<0:
                steglista.append("vänster")
                målY+=1
            elif målY>0:
                steglista.append("höger")
                målY-=1
            else:
                steglista.append(Wanderrandom(1)[0])
            steps-=1
        return steglista

def Lookinshortterm(steps): # om fanskapet har gått i en rak linje så vänder han om och tänker om sinna livsval
    if len(korttidsminne)==0: # om det inte finns något minne
        return Wanderrandom(steps) # går den random
    else: # om det finns 
        meströrelse=[0,0,0,0] # variabel som håller i värdet (antalet) på 4 stegval
        for minnen in korttidsminne: 
            if minnen in korttidsminne: 
                if minnen=="upp": # om den gått upp
                    meströrelse[0]+=1 # lägg till i 1a värdet på arrayen att den gått upp
                elif minnen=="ner": # fortsätter för alla håll och kanter
                    meströrelse[1]+=1
                elif minnen=="vänster":
                    meströrelse[2]+=1
                elif minnen=="höger":
                    meströrelse[3]+=1
            Lodrätt="" # skriver in upp / ner osv när nesta if sats har gått igenom
            Vågrätt="" 
            if meströrelse[0]>meströrelse[1]: # kollar om den första värdet i arrayen är mest då kommer den här säga att upp har använt mest
                Lodrätt="upp"
            else:
                Lodrätt="ner"
            if meströrelse [2]>meströrelse[3]:
                Vågrätt="Vänster"
            else: 
                Vågrätt="höger"
        steglista=[]
        while steps>0:
            if steps%2==0: 
                steglista.append(Lodrätt)
            else: 
                steglista.append(Vågrätt)
            steps-=1
        return steglista

def FoundCheese(mousepos): # noterar och informera om musen gått på en ost
    global Map
    if Map[mousepos[0]][mousepos[1]]==1: # om den står på en ost
        outputtext="We found cheese Wallace at"+str(mouse[0])+" X " +str(mouse[1])+" Y " # skriver den ut var den står och säger att den hitade osten
        global cheeseeaten 
        cheeseeaten+=1 # lägger till att den ätit ennu en ost
        text.insert(INSERT, outputtext)
        global långtidsminne
        långtidsminne.append([mousepos[0],mousepos[1]]) # minns vart osten stod
        C.create_rectangle(getcoord(mousepos[0],mousepos[1]), fill="gold") # ändrar färgen på rutan för att visa att osten är äten
        Map[mousepos[0]][mousepos[1]]=0 # tar bort osten så den inte kan gå där igen och äta nogot som inte finns
        global energi
        energi+=10 # och ger den mer energi för att gå längre 
        global currentcheeses
        currentcheeses-=1 # minskar antalet ostar som finns på plan

def Movemouse(mouse1,Movingobject):
    # time.sleep(1)
    global mouse
    if mouse[0]<=-1:
        mouse1[0]=1
        mouse[0]= mouse[0]+2
    elif mouse[1]<=-1:
        mouse1[1]=1
        mouse[1]= mouse[1]+2
    elif mouse[0]>=w:
        mouse1[0]=-1
        mouse[0]= mouse[0]-2
    elif mouse[1]>=h:
        mouse1[1]=-1
        mouse[1]= mouse[1]-2

    dx=mouse1[0]*sizevalue # denna används hela tiden så vi väljer att säga åt den här att göra sakerna den utför om och om igen orkar äligt talat inte skriva för alla dock har jag fortsattit komenterat så sluta inte läsa
    dy=mouse1[1]*sizevalue
    C.move(Movingobject, dx, dy)
    time.sleep(speed)
    Createcheese()
    Createcheese()
    Movespeed()
    C.update()

def rs(inputval,sizevalue): # tar in två inputs inputval sizeval och räknar ut start kordinater
    return inputval*sizevalue 

def getcoord(x,y): # tar in x och y platsen i rutnätet genom att multiplicera den med sizevalue (25) och returnar den som en coord variabel
    sizevalue=25
    x=rs(x,sizevalue)
    y=rs(y,sizevalue)
    return x,y,x+sizevalue,y+sizevalue

def Createcheese(): # lägger ut ostarna
    global currentcheeses # måste sättas för att ändra på en global variabel ie de variablerna vi skrev högst upp
    if cheeseamount>currentcheeses: # om antalet ostar tillåtna är mindre än ostarna vi har på plan
        ptpc=randint(0, len(cheeseplaces)-1) # tar den och på random sätter ut en ny ost på plan
        x=cheeseplaces[ptpc][0] # vart ostarna kan sitta på x led
        y=cheeseplaces[ptpc][1] # y led
        C.create_rectangle(getcoord(x,y), fill="yellow") # och tar de placeringarna för att lägga en ost där
        currentcheeses+=1 # lägger till i variabeln att en ost har laggts till
        global Map
        Map[x][y]=1

master = Tk() # genererar våran värld

w = 20 # antalet brickor på banan x led
h = 20 # -II- y led
Map = [[0 for x in range(w)] for y in range(h)] # lägger värdet 0 på 20 platser
food=1 # sätter variabeln food till 1
wall=2 # -II- wall till 2
Map[2][2]=food 
Map[0][1]=wall 

print(Map[0][0]) #låter oss se vad som finns på en viss plats, skriver om de tidigare värdet 0

C = Canvas(master, bg="black", height=500, width=500) #"målartavla" bakgrunden 
C.pack() # krävs programet fuckar om de inte finns

distanceY=0 #längden mellan rutorna
distanceX=0 #-II-
sizevalue=25 #storlek på rutorna

for row in range(0,w): #skapar ränderna
    for col in range(0,h):
        coord = distanceX, distanceY, distanceX+sizevalue, distanceY+sizevalue
        distanceX+=sizevalue
        # if Map[col][row]==1:
        #     C.create_rectangle(coord, fill="yellow") # en ensam liten ost som var som ett test
        if col%2==0:
            C.create_rectangle(coord, fill="white")
        elif col%2==1:
            C.create_rectangle(coord, fill="gray")
    distanceY+=sizevalue
    distanceX=0

# mouse=[5,5]
x=mouse[0]*sizevalue
y=mouse[1]*sizevalue
coord=x,y,x+sizevalue,y+sizevalue
Mouse=C.create_rectangle(getcoord(5,5), fill="red") # med detta kan vi se våran mus
mousemove=MovePlanner(10)

text = Text(master, height=2, width=35) # lilla ruten längst ner på tk där vi kan skriva in saker
text.pack()
text.insert(END, "Wallace went looking for cheese") # som dethär

while energi>0: # energiförbrukningen för musen medans energin är större än 0 så kommer den orka att ta ett til steg vissa saker vet jag inte varför vi har kvar de
    energiförbrukning=randint(1,energi) 
    mousemove=MovePlanner(energiförbrukning)
    energi-=energiförbrukning
    while len(mousemove)>0: 
        # print(str(mouse[0])+"  "+str(mouse[1]))
        steg=[0,0]
        # C.create_rectangle(getcoord(mouse[0],mouse[1]), fill="blue")
        if mousemove[0]=="upp":
            mouse[1]= mouse[1]-1
            steg[1]-=1
        elif mousemove[0]=="ner":
            mouse[1]= mouse[1]+1
            steg[1]+=1
        elif mousemove[0]=="vänster":
            steg[0]-=1
            mouse[0]= mouse[0]-1
        elif mousemove[0]=="höger":
            steg[0]+=1
            mouse[0]= mouse[0]+1
        Movemouse(steg,Mouse)
        FoundCheese(mouse)
        mousemove.pop(0)
    text.delete("insert linestart", "insert lineend") # tar bort skriver osv texter där vi också använder oss utav variablerna som string format för att skriva hur mycket energi han har kvar
    text.insert(END, str(energiförbrukning)+" steps taken, "+str(energi)+" energy left")
        # C.move(Mouse,mouse[0]*sizevalue,mouse[1]*sizevalue)

text.delete("insert linestart", "insert lineend")
text.insert(END,"Out of steps Wallace eate "+str(cheeseeaten)+" cheese")

mainloop()
