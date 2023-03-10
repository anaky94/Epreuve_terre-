#créer un programe qui affiche le nombre de caractère d'une chaîne de caractères passée en argument.

#fonction intégral lens()

a =input("entez un mot ")
try:
    a=str
    print(len(a))
except:
    print("erreur")
    