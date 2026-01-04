# ESERCIZIO 4
# Data una lista di numeri (positivi e negativi), crea una nuova lista
# in cui ogni numero viene trasformato secondo la seguente regola:
# - se il numero è positivo, mantienilo
# - se il numero è negativo, sostituiscilo con 0
#
# Esempio:
# input  -> [3, -1, 0, -7, 5]
# output -> [3, 0, 0, 0, 5]
#

numeri = [3, -1, 0, -7, 5]

numeri_trasformati = [n if n > 0 else 0 for n in numeri]

print(numeri_trasformati)