# ESERCIZIO 5
#
# Data una lista di tuple (prodotto, quantità),
# scrivi un codice che costruisca un dizionario
# con il totale delle quantità per ciascun prodotto.
#

# Lista di tuples
acquisti = [
    ("mele", 3),
    ("pere", 5),
    ("mele", 2),
    ("banane", 4),
    ("pere", 1)
]

totale = {}
articoli = []

for acquisto in acquisti:
    
    if acquisto[0] not in totale.keys():
        totale[acquisto[0]] = acquisto[1]
    else:
        nuova_quantita = totale[acquisto[0]] + acquisto[1]
        totale[acquisto[0]] = nuova_quantita

print(totale)