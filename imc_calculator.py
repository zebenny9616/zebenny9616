def grandeur_en_metre (): 
    def poids_en_kg (): 

        def IMC (): poids_en_kg / (grandeur_en_metre)**2

        if IMC <18.5:
            print("Poids insuffisant")
        elif 18.5 <= IMC < 25 :
            print("Poids santé")
        elif 25 <=  IMC < 30 :
            print("Excès de poids")
        elif IMC <= 30 :
            print("Obèse")

    print(f"Vous êtes dans la catégorie d'IMC suivante : {IMC}. ")


int(input("Entrez votre grandeur en metre : "))
int(input("Entrez votre poids en kilogramme : "))

