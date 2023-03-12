# Créer un programme qui affiche si un nombre est premier ou pas. 
#un nombre premier est quand un entier est divisible par 2 diviseurs positif 
a = int(input("entrez un entier : "))
c=0
for i in range(1,a+1): # les diviseurs positif de a s'afficherons
    if a%i ==0:
        c=c+1
        print(i)

if c==2:
    print("oui " + str(a)+" est un nombre premier" )
elif  c==1:
    print("non " +str(a)+ " n'est pas un nombre premier.")
elif c==0:
    print("non "+str(a)+"n'est pas un nombre premier;")
else:
    print("non " +str(a)+ " n'est pas un nombre premier." )