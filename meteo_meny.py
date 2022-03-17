#Créer un programme prenant en paramètre les conditions météorologiques suivantes:
# L'état du ciel(Ensoleillé, nuageux ou éclaircies), 
# Les précipitations (aucune, pluie, neige ou verglas), 
# La vitesse des vents en km/h 
# La température en C.
# Ensuite : Alerte si :
# Il y a des précipitations et les vents sont supérieurs à 30 km/h
# Il y a du verglas
# Il fait soleil, mais les vents sont supérieurs à 70km/h ou les températures sont supérieures à 30C ou inférieures à -25C.
# Il fait nuageux et les vents sont supérieurs à 50km/h.
# Il fait nuageux et les vents sont supérieurs à 30km/h, mais la température est supérieure à 25C ou inférieure à -20C
# Il neige et la température est inférieure à -25C.
# Il fait ensoleillé, il n'y a pas de vent et la température est supérieure à 25C.

# État du Ciel
def menu():
    print("Voici vos choix dans le menu État du ciel : ")
    print("#1. Ensoleillé")
    print("#2. Nuageux")
    print("#3. Éclaircies")
    choix_État_Du_Ciel = int(input("Veuillez entrer votre choix: "))
    if choix_État_Du_Ciel == 1:
        print("Ensoleillé")
    elif choix_État_Du_Ciel == 2:
        print("Nuageux")
    elif choix_État_Du_Ciel == 3:
        print("Éclaircies")
    else:
        print("Choix invalide")
    return None
menu()

# Précipitations
def menu():
    print("Voici vos choix dans le menu précipitations : ")
    print("#1. Aucune")
    print("#2. Pluie")
    print("#3. Neige")
    print("#4. Verglas")
    choix_precipitation = int(input("Veuillez entrer votre choix: "))
    if choix_precipitation == 1:
        print("Aucune précipitation")
    elif choix_precipitation == 2:
        print("Pluie")
    elif choix_precipitation == 3:
        print("Neige")
    elif choix_precipitation == 4:
        print("Verglas")
    else:
        print("Choix invalide")
    return None
menu()