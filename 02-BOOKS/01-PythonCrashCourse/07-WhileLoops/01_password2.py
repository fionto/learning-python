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

# NOTA: In Python, per i cicli di validazione, 
# si preferisce l'uso di un ciclo infinito + break.

while True:

    password = input("Inserisci una password valida: ")

    # Eseguo i controlli direttamente dentro il ciclo.
    # Non ho bisogno di dichiarare queste variabili fuori dal while.
    is_long = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)

    # Verifico se TUTTE le condizioni sono True.
    # Se lo sono, stampo il successo ed esco immediatamente dal ciclo con break.
    if is_long and has_upper and has_digit and has_special:
        print("Password accettata")
        break

    # Se il codice arriva qui, significa che almeno una condizione è False.
    # Mostro solo gli errori specifici.
    if not is_long:
        print("La password deve contenere almeno 8 caratteri")
    if not has_upper:
        print("La password deve contenere almeno una maiuscola")
    if not has_digit:
        print("La password deve contenere almeno un numero")
    if not has_special:
        print("La password deve contenere almeno un carattere speciale (!@#$%)")
    
    # Il ciclo ricomincerà automaticamente da "password = input(...)"