# ESERCIZIO 5: Slicing combinato su liste e stringhe
# Obiettivo: Estrarre dati complessi combinando start, stop e step negativi.
# 1. Data la stringa 'alfabeto', estrarre la sequenza "zyx" usando solo indici negativi e step.
# 2. Dalla lista 'misto', estrarre gli elementi dall'indice 1 all'indice 5, ma restituiti al contrario.

alfabeto = "abcdefghijklmnopqrstuvwxyz"
misto = [10, "A", 20, "B", 30, "C", 40, "D"]

# Risultati attesi:
# 1. "zyx"
# 2. ["C", 30, "B", 20, "A"]

risultato_uno = alfabeto[-1:-4:-1]
print(risultato_uno)

risultato_due = misto[5:0:-1]
print(risultato_due)