#Einfache Berechnung ohne Eingabe des Users
from datetime import date
d0 = date(2025, 4, 11)
d1 = date(2026, 4, 16)
delta = d1 - d0
print(delta.days)

#Da müssen Eingabemöglichkeiten her, sonst machts kein Spass
#So ist es ja nur statisch
