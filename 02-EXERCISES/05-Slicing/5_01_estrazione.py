# ESERCIZIO 1: Estrazione tramite indici positivi e negativi
# Obiettivo: Estrarre sottostringhe specifiche dalla variabile 'testo'.
# 1. Estrarre i primi 5 caratteri.
# 2. Estrarre gli ultimi 4 caratteri usando indici negativi.
# 3. Estrarre la parola "corso".

testo = "Benvenuti al corso di Python"

# Risultati attesi:
# 1. "Benve"
# 2. "thon"
# 3. "corso"

risultato_uno = testo[:5]
print(risultato_uno)

risultato_due = testo[-4:]
print(risultato_due)

risultato_tre = testo[13:18]
print(risultato_tre)