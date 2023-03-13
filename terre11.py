# Créez un programe qui transforme une heure affiché en format 24h en une heure affichée en format 12h
d=str(input("indiquez le format d'heure en 24h:"))
c=d(-12)
if d >= 12:
    print(c,":pm")
elif d <=12:
    print(c,"0 :am")