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

spesa = {}

# Tuple unpacking: direttamente nella riga del for
for frutto, quantità in acquisti:
    
    # metodo .get(key, value) per accedere al valore conoscendo la chiave
    # key è un valore richiesto
    # value è opzionale, in questo caso restituisce 0 se la chiave non esiste.
    spesa[frutto] = spesa.get(frutto, 0) + quantità

print (spesa)