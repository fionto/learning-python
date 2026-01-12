# ESERCIZIO 2: Lavorare con le omissioni e l'inversione
# Obiettivo: Utilizzare la sintassi abbreviata per gestire una lista di numeri.
# 1. Creare una sottolista che contenga i primi 4 elementi.
# 2. Creare una sottolista che contenga tutti gli elementi dal quinto in poi.
# 3. Creare una versione invertita della lista originale.

numeri = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Risultati attesi:
# 1. [0, 10, 20, 30]
# 2. [40, 50, 60, 70, 80, 90]
# 3. [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

risultato_uno = numeri[:4]
risultato_due = numeri[4:]
risultato_tre = numeri[::-1] # start, stop, step = -1

print(risultato_uno)
print(risultato_due)
print(risultato_tre)