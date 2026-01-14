# ESERCIZIO 3
# Data una lista di stringhe, crea una nuova lista che contenga
# solo le stringhe con lunghezza maggiore di 5 caratteri.
#
# Esempio:
# input  -> ["python", "c", "java", "matlab", "go"]
# output -> ["python", "matlab"]
#
# Obiettivo: allenarsi all'uso delle list comprehension con stringhe.

linguaggi = ["python", "c", "java", "matlab", "go"]

linguaggi_lunghi = [linguaggio for linguaggio in linguaggi if len(linguaggio) > 5]

print(linguaggi_lunghi)