#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne

"""
alphabet=input("entre une letre :")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for lettre in range(26):
    
    print (alphabet=alphabet+str(1)) 
    input()"""

alphabet = []
lettre=input("entter yu letter ")
start = ord(lettre)
for i in range (26):
    alphabet.append(chr(start+i))

print(alphabet)