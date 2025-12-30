# ESERCIZIO 2: Stampa invertita di una stringa
# Data una stringa (ad esempio: "python"), usa un for loop per stampare ogni 
# carattere in ordine inverso. 

# METODO 2: Usare reversed() direttamente nel for (come il tuo, ma più conciso)
stringa = "python"
for lettera in reversed(stringa):
    print(lettera)
# reversed() funziona direttamente su stringhe, non servono indici
# Genera le lettere al contrario una per una