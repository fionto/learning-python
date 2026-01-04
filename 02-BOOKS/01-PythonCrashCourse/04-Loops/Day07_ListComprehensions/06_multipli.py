# ESERCIZIO 6
# Data una lista di numeri interi, costruisci una nuova lista contenente
# solo i numeri che sono multipli sia di 3 che di 5.
#
# L'obiettivo è ottenere la lista finale usando una singola list comprehension.

multipli = [n for n in range(1, 100) if n % 15 == 0]

print(multipli)