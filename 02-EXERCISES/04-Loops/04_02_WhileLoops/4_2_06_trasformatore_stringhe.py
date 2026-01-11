# ESERCIZIO 6
# 
# OBIETTIVO: Data una stringa di input contenente coppie "chiave:valore" separate
# da virgole (es: "nome:Mario,cognome:Rossi"), usa un ciclo while e i metodi 
# .find() e .partition() per estrarre i dati e inserirli in un dizionario.
# Non è consentito l'uso del metodo .split().
# REQUISITO EXTRA: Studia attentamente come .partition() restituisce una tupla
# di tre elementi e usa questa caratteristica per avanzare nel ciclo sulla stringa.

dati_grezzi = "id:001,stato:attivo,livello:esperto,punteggio:85"

dati_singoli = []
dati_puliti = {}

while True:
    i = dati_grezzi.find(',')

    if i != -1:
        grezzo = dati_grezzi[:i]
        dati_singoli.append(grezzo)
        dati_grezzi = dati_grezzi[i + 1:]
        i = dati_grezzi.find(',')
    else:
        dati_singoli.append(dati_grezzi)
        break

while dati_singoli:
    chiave, delim, valore = dati_singoli.pop(0).partition(':')
    dati_puliti[chiave] = valore

print(dati_puliti)