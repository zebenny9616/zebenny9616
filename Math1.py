import math

def carre_racine(base):
    if base > 0 :
        return base * base , math.sqrt(base)
    else:
        return base*base, 0

n = int(input("Rentrer un numéro: "))

carre, racine = carre_racine(n)

if racine == 0 :
    print(f"Le carré de {n} est {carre}")
else:
    print(f"Le carré de {n} est {carre} et sa racine carré est {racine}")