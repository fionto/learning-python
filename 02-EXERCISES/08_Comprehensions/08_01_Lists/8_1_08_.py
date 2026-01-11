# ESERCIZIO 8
# Data una lista di numeri reali, costruisci una nuova lista in cui:
# - i numeri negativi vengono scartati
# - i numeri positivi vengono trasformati
#
# L'esercizio richiede l'uso combinato di più elementi tipici
# delle list comprehension in Python.

numeri = [-3, -7, 10, 250, 0, 69, -85, 45, 12, -12]

elaborati = [n ** 2 for n in numeri if n >= 0]

print(elaborati)