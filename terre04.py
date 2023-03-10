#Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair.. 
#Exemples d’utilisation :

#1 : determiner un bout de code qui donne les entiers au hasard
#2 : determiner que pair et impair apparaisse 
#3 : faire en sorte qu'il donne un entier (paire ou impair)

a=2
argument = int(input("Entrez un chiffre "))
try:
    argument=int(argument)
    if argument%a == 0: 
        print("pair") 
    else:
        print("impair")       
except ValueError :
    print("entré un chiffre")


"""
if argument%a == 0: 
    print("pair")
else:
    print("impair")
    """