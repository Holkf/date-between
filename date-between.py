#Einfache Berechnung ohne Eingabe des Users
from datetime import date
d0 = date(2017, 8, 18)
d1 = date(2017, 10, 26)
delta = d1 - d0
print(delta.days)

#Da müssen Eingabemöglichkeiten her, sonst machts kein Spass
