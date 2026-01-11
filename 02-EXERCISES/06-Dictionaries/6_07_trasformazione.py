# ESERCIZIO 7
# Dato un dizionario che associa parole a numeri interi,
# scrivi un codice che restituisca una nuova versione del dizionario
# in cui:
# - le chiavi con valore negativo vengono rimosse
# - i valori pari vengono raddoppiati
# - i valori dispari rimangono invariati
#
# INPUT:

dati = {
    "a": 4,
    "b": -3,
    "c": 7,
    "d": 10,
    "e": -1
}

dati_elaborati = {}

for nome, dato in dati.items():
    valore = int(dato)
    if valore < 0:
       continue 
    if valore % 2 == 0:
        dati_elaborati[nome] = valore * 2
    else:
        dati_elaborati[nome] = valore

print(dati_elaborati)