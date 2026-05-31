try:
    file = open("dati_inesistenti.txt", "r")
except FileNotFoundError as errore:
    print(f"Non riesco a trovare il file: {errore.filename}")
    print(f"Messaggio: {errore.strerror}")