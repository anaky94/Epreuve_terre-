#Créez un programme qui détermine si une liste d’entiers est triée ou pas
"""
$> ruby exo.rb 9 8 3
Pas triée !

$> ruby exo.rb 3 8 9 12
Triée !

$> ruby exo.rb “Salut”
erreur.
"""
while tri==0:
    tri=int(input("taper un chifre"))
    tri2=int(input("taper un chifre"))
    tri3=int(input("taper un chifre"))

if tri <= tri2 and tri:
    print("triée")
elif tri2 <=tri3:
    print("triée")
else:
    print("pas trié")
    
try:
    valeur_int=int(tri)
    valeur_int=int(tri2)
    valeur_int=int(tri3)

except ValueError:
    print("Erreur taper un enteir")
