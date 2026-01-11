# ESERCIZIO 2: Analizzatore di Sequenze Numeriche
#
# Scrivi un programma che:
# 1. Chieda ripetutamente all'utente di inserire numeri interi
# 2. Memorizzi i numeri in una lista
# 3. Quando l'utente inserisce 'stop', il programma termina l'input
# 4. Calcola e stampa:
#    - La mediana della sequenza
#    - Il numero che appare più frequentemente (moda)
#    - Tutti i numeri che appaiono più di una volta
#
# Se l'utente inserisce valori non validi, ignora l'input e continua.
#
# Nota: dovrai implementare la logica per trovare mediana e moda
# senza usare librerie esterne (solo metodi built-in di liste/dizionari).

def main():
    numeri = []

    print("Crea una sequenza di numeri, premendo Invio \n"
    "termina la sequenza scrivendo stop")

    while True:
        dato_ingresso = input("Nuovo numero:").strip()
        is_float = check_float(dato_ingresso)
    
        if dato_ingresso == 'stop':
            break
        elif not dato_ingresso or not is_float:
            continue
        else:
            numeri.append(float(dato_ingresso))  

    print(f"La mediana della sequenza è pari a: {mediana(numeri)}")
    print(f"La moda della sequenza è pari a: {moda(numeri)}")
    print(f"I numeri che appaiono più di una volta sono: {ripetuti(numeri)}")

def check_float(stringa):    
    stringa = stringa.strip()

    # Gestisce il segno opzionale all'inizio
    if stringa.startswith(("+", "-")):
        stringa = stringa[1:]

    # Gestisce se è vuota
    if not stringa or stringa == ".":
        return False
    
    dot_count = 0
    for char in stringa:
        if char == ".":
            dot_count += 1
            if dot_count > 1: return False # Massimo un punto permesso
        elif not ('0' <= char <= '9'): # Confronto tabella
            return False    
    return True

def mediana(numeri):
    
    if not numeri:
        return None
    
    numeri_ordinati = sorted(numeri)
    elementi = len(numeri_ordinati)

    if elementi % 2 != 0:
        mediana = numeri_ordinati[((elementi + 1) // 2) - 1]
    else:
        mediana = (numeri_ordinati[(elementi//2) - 1] + numeri_ordinati[(elementi//2)])/2

    return mediana

def moda(numeri):
    
    if not numeri:
        return None
    
    moda = numeri[0]
    contatore_massimo = 0
        
    for numero in numeri:
        contatore_corrente = numeri.count(numero)
        if(contatore_corrente > contatore_massimo):
            contatore_massimo = contatore_corrente
            moda = numero

    return moda

def ripetuti(numeri):
    if not numeri:
        return None

    conteggi = {}
    for n in numeri:
        conteggi[n] = conteggi.get(n, 0) + 1

    return [n for n, c in conteggi.items() if c > 1]

main()