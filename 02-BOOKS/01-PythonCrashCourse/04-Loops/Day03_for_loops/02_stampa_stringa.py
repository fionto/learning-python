# ESERCIZIO 2: Stampa invertita di una stringa
# Data una stringa (ad esempio: "python"), usa un for loop per stampare ogni 
# carattere in ordine inverso. Ricorda che le stringhe sono sequenze 
# indicizzabili, quindi puoi usare range() con indici negativi oppure iterare 
# normalmente e stampare al contrario.

# creo stringa
stringa = "python"

# calcolo lunghezza per creazione indici
num_lettere = len(stringa)

# metodo per scorrere for loop al contrario
# genero range con indici al contrario
indici = reversed(range(num_lettere))

# faccio scorrere il ciclo
for i in indici:
    lettera = stringa[i]
    print(lettera)