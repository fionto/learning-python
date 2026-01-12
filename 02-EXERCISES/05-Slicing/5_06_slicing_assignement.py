# ESERCIZIO 6: Modifica di una sequenza tramite slicing assignment
# Obiettivo: Sostituire una porzione di una lista con una nuova sequenza.
# Nota bene: La lunghezza della nuova sequenza non deve necessariamente 
# coincidere con quella della fetta sostituita.
# 1. Nella lista 'dati', sostituire gli elementi dall'indice 1 all'indice 3 (escluso)
#    con la lista [99, 88, 77].
# 2. Rimuovere gli ultimi due elementi della lista risultante usando lo slicing e l'operatore 'del' 
#    oppure assegnando una lista vuota [].

dati = [10, 20, 30, 40, 50]

# Risultati attesi:
# 1. Dopo la sostituzione: [10, 99, 88, 77, 40, 50]
# 2. Dopo la rimozione finale: [10, 99, 88, 77]

sequenza_nuova = [99, 88, 77]

dati = dati[0:1] + sequenza_nuova + dati[3:]
print(dati)

del dati[-2:]
print(dati)