try: #door try te gebruiken hier hoef ik niet te checken of de input een getal is en probeer ik gewoon de code uit te voeren
    #in plaats hiervan kun je ook eerst checken of dat input een int kan worden en daarna de rest van de code uitvoeren
    getal = int(input("geef een nummer onder de tien\n"))
    if getal < 10:
        print("goed gedaan")
    else:
        print("dit is niet onder de tien")
except ValueError as error:
    raise NameError("je moet in hele getallen antwoord geven")
finally:
    print("de code is uit gevoerd")