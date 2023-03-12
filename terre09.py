
#créez un programme qui affiche la racine carée d'un entier positif 

"""a=int(input("calculer la racine carré de : "))
b=0.5
print(pow(a,b))"""

import math

a = int(input("calculer la racine caré de : "))
try:
    a=print(math.sqrt(a))
    if a <=1:
        print("erreur: entrez un entier positif")
except:
    print("ValueError: entré un entier positif")
    