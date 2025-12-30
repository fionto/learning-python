# ESERCIZIO 3: Stampa invertita di una stringa

# Creo una stringa
stringa = "python"

# Calcolo la lunghezza per creare gli indici
# len() ritorna un intero
num_lettere = len(stringa)

# range(num_lettere) crea un RANGE OBJECT (oggetto iterabile, non una lista)
# Un range NON memorizza tutti i numeri in memoria, ma li genera al bisogno
# range(6) è come una "ricetta" che dice "genera numeri da 0 a 5"
indici_in_avanti = range(num_lettere)

# reversed() prende un iterabile e ritorna un REVERSED OBJECT (oggetto iterabile)
# Anche reversed() NON materializza i numeri, ma li genera al bisogno, inversi
# reversed() lavora su qualsiasi sequenza (range, liste, stringhe, ecc.)
indici = reversed(indici_in_avanti)

# Il for loop può iterare su oggetti iterabili senza convertirli a lista
# Python genera un numero alla volta dal reversed object mentre il loop scorre
for i in indici:
    lettera = stringa[i]
    print(lettera)

# Se volessi materializzare l'oggetto iterabile in una lista concreta:
# indici_lista = list(reversed(range(num_lettere)))
# Allora print(indici_lista) darebbe [5, 4, 3, 2, 1, 0]