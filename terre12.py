#Créez un programme qui transforme une heure affichée en format 12h en une heure affichée en format 24h.


def convert(s):
    
      if s[-2:] == "AM" and s[:2] == "12":
         return "00" + s[2:-2]

      elif s[-2:] == "AM":
         return s[:-2]

      elif s[-2:] == "PM" and s[:2] == "12":
         return s[:-2]
        
      else:
          return str(int(s[:2]) + 12) + s[2:8]

s=input("entre l'heure ")
print(convert(s))




