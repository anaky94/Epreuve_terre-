# Créez un programe qui transforme une heure affiché en format 24h en une heure affichée en format 12h
"""d=int(input("indiquez le format d'heure en 24h:"))
c=d(-12)
if d >= 12:
    print(c,":pm")
elif d <=12:
    print(c,"0 :am")"""

def convert(s):
    
      if s[-2:] == "AM" and s[:2] == "-12":
         return "00" + s[2:-2]

      elif s[-2:] == "AM":
         return s[:-2]

      elif s[-2:] == "PM" and s[:2] == "-12":
         return s[:-2]
        
      else:
          return str(int(s[:2]) - 12) + s[2:8]

s=input("entre l'heure ")
print(convert(s))
