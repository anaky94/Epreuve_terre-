#Créez un programme qui détermine si une liste d’entiers est triée ou pas
"""
$> ruby exo.rb 9 8 3
Pas triée !

$> ruby exo.rb 3 8 9 12
Triée !

$> ruby exo.rb “Salut”
erreur.
"""

tri=input("taper un chifre ")
tri2=input("taper un chifre ")
tri3=input("taper un chifre ")

try:
    valeur_int=int(tri)
    valeur_int=int(tri2)
    valeur_int=int(tri3)
except ValueError:
    print("Erreur taper un entier")

print(tri, tri2, tri3,'\n') 

if tri <= tri2 and tri3:
    print("triée")
elif  tri2 <=tri3:
    print("triée")
elif tri3 >tri and tri2:
    print("pas trié")
else:
    print("pas trié")
    

