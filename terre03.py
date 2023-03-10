#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne



alphabet = []
lettre=input("entrez une lettre ")
start = ord(lettre)
for i in range (26):
    alphabet.append(chr(start+i))
print(alphabet)
input()