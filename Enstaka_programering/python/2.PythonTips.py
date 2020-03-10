#Tips

#Detta är en variabel, den är numerisk
siffra= 5
#Detta är också en variabel men den är textbaserad och måste därför ha prefixet och suffixet ".
bokstäver = "Hej"
#Även detta är en variabel, den är boolsk alltså sann eller falsk
flintskallig =True

print(flintskallig)
#Variabler kan ändras, till exempel om håret växer ut.
flintskallig= False

print(flintskallig)

#I python kan man forma variablerna hur man vill, en som tidigare har använts för text kan göras om till nummer.
bokstäver=4.5

#Variabler kan skapas från andra variabler med till exempel
Storsiffra= siffra+siffra+3
Namn = "Jocke"
Efternamn= "Flink"
HelaNamn = Namn+ Efternamn

#print fungerar så att den skriver ut saker som en textsträng (string) är det boolsk eller numeriska värden så konverterar den det till string
#Om man blandar olika typer av värden som text och nummer så måste man ha str() runt numret för att förklara för programmet att den ska omvandlas.
print(HelaNamn+ str(Storsiffra))

#Förutom + fungerar såklart - * / för att skapa mindre och mer avancerade uträkningar. Det är alltid bra att kommentera (#) de avancerade uträkningarna.
Netflixkostnad = (109/5)*12 #Netflix kostnad för en familj på fem över ett år
Netflixkostnad= (109/1)*12 #Verklig netflix kostnad över ett år (Sannolikheten säger att den som äger abbonemanget betalar allt.)

print("Netflix kostnaden " + str(Netflixkostnad))
#Då uppstår den stora frågan, vem betalar för netflix? Det får man vet genom att skriva input() , inputen måste såklart sparas någonstans, i detta fall i variabeln betalarn 
betalarn = input('Vem betalar? ')
print(betalarn+ " betalar")