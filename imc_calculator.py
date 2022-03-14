import_math

def grandeur_en_metre (): 
    int(input("Entrez votre grandeur en metre : "))
def poids_en_kg (): 
    int(input("Entrez votre poids en kilogramme : "))

def IMC (poids_en_kg / (grandeur_en_metre)**2)) 

if IMC < 18.5 :
    IMC = str("Poids insuffisant")
elif IMC <= 18.5 or > 25 :
    IMC = str("Poids santé")
elif IMC <= 25 or > 30 :
    IMC = str("Léger excès de poids")
elif IMC <= 30 :
    IMC = str("Obèse")
return None

print(f"Vous êtes dans la catégorie d'IMC suivante : {IMC}. ")