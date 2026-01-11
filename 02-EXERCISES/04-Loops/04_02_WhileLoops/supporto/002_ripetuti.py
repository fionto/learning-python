def ripetuti(numeri):
    
    if not numeri:
        return None
    
    numeri_ripetuti = []
        
    for numero in set(numeri):
        if(numeri.count(numero) > 1):
            numeri_ripetuti.append(numero)

    return numeri_ripetuti

serie_di_numeri = [7, 10, 6, 2, 1, 2, 2, 1, 3, 3, 3, 3, 4, 1, 1, 1, 4]
print(ripetuti(serie_di_numeri))