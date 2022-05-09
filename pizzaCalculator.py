#Lukas van Hulst 
#opdracht: Pizza calculator
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|Voer in hoeveel je van elke soort wilt")

#input voor hoeveelheid pizza's
def vraag(groote):
    while True:
        try:
            pizza = input(f"|{groote} Pizza's :")
            pizza = int(pizza)
            return pizza

        except ValueError as error:
            print("Gebruik hele getallen")

Spizza = vraag("Small")            
Mpizza = vraag("Medium")
Lpizza = vraag("Large")

#prijzen van pizza's
Psmall   = 5.99
Pmedium  = 7.99
Plarge   = 11.99

#prijs bereken
totaal = Spizza * Psmall + Mpizza * Pmedium + Lpizza * Plarge 

#overzicht van bestelling
print("U heeft een bestelling gemaakt van " + str(totaal) + " voor " + str(Spizza) + " small pizza's, " + str(Mpizza) + " medium pizza's en " + str(Lpizza) + " large pizza's")