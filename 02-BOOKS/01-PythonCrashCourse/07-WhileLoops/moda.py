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