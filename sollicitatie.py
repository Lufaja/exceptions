geschikt = True


#naam
naam = input("|Wat is uw naam: ")


#de leeftijd
leeftijd = int(input("|Wat is uw leeftijd?: "))
if leeftijd == 69:
    raise NameError("Nice")


#lust banaan
banaan = input("|Lust u een banaan? Y/N: ").lower()


#wat is 9 + 10
wiskunde = input("|Wat is 9 + 10?: ")
if wiskunde == "19":
    raise NameError("Hoe kom je nou weer aan 19")



#IMPOSTER?
vent = input("|Heb je gevent? Y/N: ").lower()



#Ervaringen 
ervaring = input("|Heeft u ervaring in een van de volgende dieren-dressuur/jongleren/acrobatiek?: ").lower()
jaar = int(input("|Hoeveel jaar ervering heeft u hier in?: "))


#Diploma MBO-4 Ondernemen
diploma = input("|Bent u in bezit van een diploma MBO-4 Ondernemen? Y/N: ").lower()


#Heeft persoon rijbewijs
rijbewijs = input("|Heeft u een geldig vrachtwagen rijbewijs? Y/N: ").lower()



#Hoge hoed
hoed = input("|Bent u in bezit van een hoge hoed? Y/N: ").lower()


#Man of vrouw?
gember = input("|Bent u een man of vrouw?: ").lower()
if gember == "man":
    snor = input("|Hoe breed is uw snor in cm?: ")
elif gember == "vrouw":
    haar = input("|Hoe lang is uw rood krulhaar in cm?: ")



#Lengte
lengte = int(input("|Hoe lang bent u in cm?: "))
if lengte == 200:
    raise NameError("Je mag niet liegen over je lengte")


#gewicht
gewicht = int(input("|Wat is uw gewicht?: "))



#Certificaat
papiertje = input("Heeft U het Certificaat “Overleven met gevaarlijk personeel”? Y/N: ").lower()




#resultaat
if gember == "man" and int(snor) > 10 or gember == "vrouw" and int(haar) >= 20:
    var1 = True
if ervaring == "dieren-dressuur" and jaar >= 4 or ervaring == "jongleren" and jaar >= 5 or ervaring == "acrobatiek" and jaar >= 3:
    var2 = True
if  leeftijd >= 21 and banaan == "y" and wiskunde == "21" and vent == "n" and diploma == "y" and rijbewijs == "y" and hoed == "y" and lengte >= 150 and gewicht > 90 and papiertje == "y" and var1 == True and var2 == True:
    print("|U bent geschikt om een vervolg gesprek te doen.")
else:
    print("|U bent niet geschikt voor deze baan.")