def moda(numeri):
    
    if not numeri:
        return None
    
    # Fase 1: Creazione del dizionario delle frequenze
    conteggi = {}
    for numero in numeri:
        conteggi[numero] = conteggi.get(numero, 0) + 1

    # Fase 2: Ricerca manuale del massimo
    # Inizializziamo due variabili per "tenere traccia" del meglio che troviamo
    numero_più_frequente = None
    massima_frequenza_trovata = -1 # Partiamo da un valore bassissimo
    
    # Usiamo .items() per avere sia la 'chiave' (il numero) che il 'valore' (la frequenza)
    for numero, frequenza in conteggi.items():
        # Se la frequenza del numero che stiamo guardando ora è superiore
        # a quella massima registrata finora...
        if frequenza > massima_frequenza_trovata:
            # ...allora questo numero diventa il nostro nuovo candidato principale
            massima_frequenza_trovata = frequenza
            numero_più_frequente = numero

    return numero_più_frequente