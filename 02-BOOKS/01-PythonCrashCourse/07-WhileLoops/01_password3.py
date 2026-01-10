# ESERCIZIO 1: Validatore di Password Progressivo
#
# Crea un programma che chieda all'utente di inserire una password.
# Il programma continua a chiedere finché la password non soddisfa
# TUTTI i seguenti criteri:
# - Lunghezza minima 8 caratteri
# - Contiene almeno una lettera maiuscola
# - Contiene almeno una cifra
# - Contiene almeno uno tra questi caratteri speciali: !@#$%
#
# Dopo ogni tentativo fallito, mostra SOLO i criteri non soddisfatti.
# Quando la password è valida, mostra "Password accettata" e termina.
#
# Suggerimento tecnico: dovrai cercare metodi delle stringhe che
# verifichino presenza di lettere maiuscole e cifre.

# Creo set di confronto per velocizzare operatore in
special_characters = {'!', '@', '#', '$', '%'}

# NOTA: Il codice precedente aveva una lista di if in cascata.
# Ciò crea ridondanza. Bisogna invece seguire il principio
# DRY (Don't Repeat Yourself).

while True:
    password = input("Inserisci una password valida: ")

    # Definisco i risultati dei controlli come booleani
    is_long = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)

    # Creo una lista che "accoppia" il risultato al suo messaggio di errore.
    # Ogni elemento della lista è una 'tupla' (risultato, messaggio).
    requirements = [
        (is_long, "almeno 8 caratteri"),
        (has_upper, "almeno una maiuscola"),
        (has_digit, "almeno un numero"),
        (has_special, "almeno un carattere speciale (!@#$%)")
    ]

    # Controllo se sono tutti validi. 
    # Uso una variabile di supporto (flag) per decidere se uscire.
    all_valid = True

    # Ciclo attraverso la lista dei requisiti e uso un singolo if annidato
    for satisfied, message in requirements:
        if not satisfied:
            print(f"ERRORE: {message}")
            all_valid = False # Se anche solo uno fallisce, non posso accettare la password

    # Se dopo il ciclo all_valid è ancora True, significa che nessun 'if not satisfied' è scattato
    if all_valid:
        print("Password accettata")
        break

    # NOTA: in questo modo se aggiungo un nuovo controllo devo modificare solo tupla       