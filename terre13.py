#Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.

#exemple 11 40 34 => 34

# etape 1: inscrit un parametre qui prend 3 entier => fonction input

# etape 2: les triés si il se suivent du genre 1,2,3 alors il sont trié si non 1,3,5 alors il ne sont pas trié
# calculer la moyen des 3 trois element afficher 
# 
#etape 3:

""" 
==      égal à 
!=      différent de (fonctionne aussi avec )
>       strictement supérieur à 
>=      supérieur ou égal à
<       strictement inférieur à 
<=      inférieur ou égal à

"""


petit=int(input("taper un  entier"))
moyen=int(input("taper un  entier"))
grand=int(input("taper un entier"))

result=petit, moyen, grand
"""
if no1 <= no2:
    print(no1)
else:
    print(no2) 
if result == no1:
    if no2 <= no3:
        print(no2)
    else:
        print(no3)
else:
    if no1 <= no3:
        print(no1)
    else:
        print(no3)
"""

if petit < grand and petit < moyen:
    print(moyen) 
    if petit <moyen:
        print(moyen)
    elif moyen<grand:
        print (moyen)
  

