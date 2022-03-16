#Écrire un programme offrant un menu à un utilisateur avec 3 choix et lui affichant la phrase suivante une fois sélectionné:
#1. Bonjour
#2. Au revoir
#3. À plus tard

def menu():
    print("Bonjour utilisateur voici vos choix aujourd'hui: ")
    print("#1. Bonjour")
    print("#2. Au revoir")
    print("#3. À plus tard")
    choix = int(input("Veuillez entrer votre choix: "))
    if choix == 1:
        print("Bonjour")
    elif choix == 2:
        print("Au revoir")
    elif choix == 3:
        print("À plus tard")
    else:
        print("Choix invalide")
    return None
menu()

