#Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair.. 
#Exemples d’utilisation :

#1 : determiner un bout de code qui donne les entiers au hasard
#2 : determiner que pair et impair apparaisse 
#3 : faire en sorte qu'il donne un entier (paire ou impair)

a=2
i = int(input("Entrez un chiffre "))
try:
    if i%a == 0: 
        print("pair")
    else:
        print("impair")
except:
    print("Erreur entre un nombre")
