# ESERCIZIO 6: Somma degli ultimi tre numeri
# Data una lista di numeri, usa lo slicing per estrarre gli ultimi tre elementi
# e calcola la loro somma usando un for loop.

numeri = [0, 1 ,1, 2, 3, 5, 8, 13, 21]

numeri_sliced = numeri [-3:]
somma = 0

for numero in numeri_sliced:
    somma = numero + somma

print("La somma degli ultimi 3 numeri è:", somma)