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

# Inizializzo le variabili su false per entrare la prima volta nel while
is_long = False
has_upper = False
has_digit = False
has_special = False
valid_password = is_long and has_upper and has_digit and has_special

# Nel primo ciclo sarà sicuramente False
while not valid_password:
    password = input("Inserisci una password valida: ")

    # Controllo dei criteri di validità
    is_long = len(password) >= 8
    # Uso funzione any() che restituisce True se almeno un suo elemento è truthy
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)
    valid_password = is_long and has_upper and has_digit and has_special
    
    # Guard Clause
    if valid_password:
        print("La password è valida.")
        continue
    
    if not is_long:
        print("La password deve contenere almeno 8 caratteri")
    if not has_upper:
        print("La password deve contenere almeno una maiuscola")
    if not has_digit:
        print("La password deve contenere almeno un numero")
    if not has_special:
        print("La password deve contenere almeno un carattere speciale (!@#$%)")