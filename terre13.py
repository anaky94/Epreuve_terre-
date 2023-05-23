#Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.

#exemple 11 40 34 => 34

# etape 1: inscrit un parametre qui prend 3 entier => fonction input

# etape 2: les triés si il se suivent du genre 1,2,3 alors il sont trié si non 1,3,5 alors il ne sont pas trié
# calculer la moyen des 3 trois element afficher 
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

result = petit, moyen, grand


if petit < grand and petit < moyen:
    print(moyen) 
else:
    print(grand)
    
if petit == grand and petit == moyen and grand ==moyen:
    print("erreur")
