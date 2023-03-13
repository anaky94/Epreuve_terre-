
#créez un programme qui affiche la racine carée d'un entier positif 


import math

la_racine = int(input("calculer la racine caré ? : "))
if la_racine >0:
    print("la racine caré de ",la_racine," = ", math.sqrt(la_racine))
elif la_racine <= 0:
    print("erreur: choisir un entier positif")

    
    