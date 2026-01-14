# ESERCIZIO 2
# Data una lista di numeri interi, costruisci una nuova lista contenente
# solo i numeri dispari.
#
# Esempio:
# input  -> [10, 15, 22, 33, 40]
# output -> [15, 33]
#

numeri = [10, 15, 22, 33, 40]

dispari = [n for n in numeri if n % 2 != 0]

print(dispari)