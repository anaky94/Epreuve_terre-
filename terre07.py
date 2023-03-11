
#créer un programe qui affiche le nombre de caractère d'une chaîne de caractères passée en argument.

#fonction intégral lens()

affiche_mot =input("entez un mot: ")

try:
    affiche_mot=str(affiche_mot)
except:
    print("erreur")

print(len(affiche_mot))
