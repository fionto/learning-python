# ESERCIZIO 5
# 
# OBIETTIVO: Chiedi all'utente di inserire una frase. Usa un ciclo while per 
# contare quante volte compare ogni carattere e salva i risultati in un dizionario.
# Successivamente, chiedi all'utente quale carattere vuole eliminare dal conteggio.
# Usa un ciclo while insieme al metodo .popitem() per svuotare il dizionario
# e stampare solo le coppie chiave-valore che NON corrispondono al carattere scelto.
# REQUISITO EXTRA: Studia il funzionamento di .popitem() per i dizionari.

frase = input("Inserisci una frase: ")
caratteri = list(frase)

conteggi = {}

while caratteri:
    carattere = caratteri.pop(0)
    conteggi[carattere] = conteggi.get(carattere, 0) + 1

da_eliminare = input("Inserisci un solo carattere da eliminare: ").strip()
da_eliminare = da_eliminare[0]

while conteggi:
    char, frequenza = conteggi.popitem() # NOTA: Tupla

    if char != da_eliminare:
        print(f"La lettera '{char}' appare {frequenza} volte")