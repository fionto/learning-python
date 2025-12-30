# ESERCIZIO 2: Stampa invertita di una stringa
# Data una stringa (ad esempio: "python"), usa un for loop per stampare ogni 
# carattere in ordine inverso. 

stringa = "python"
for lettera in stringa[::-1]:
    print(lettera)
# Lo slicing [::-1] inverte la sequenza direttamente
# Questo crea una nuova stringa invertita e itera su quella