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

# Python "apre" la lista originale tra l'indice 1 e 3 e 
# ci inserisce dentro i nuovi elementi, 
# adattando la lunghezza della lista automaticamente
dati[1:3] = [99, 88, 77] 
print(dati)

del dati[-2:]
print(dati)