# ============================================
# ESERCIZIO 5 – Verifica username intelligente
#
# Chiedi all’utente di inserire uno username.
#
# Lo username è valido solo se:
# - ha almeno 5 caratteri
# - non contiene spazi
# - non è già presente nella lista esistente
# - non è composto solo da numeri
#
# Stampa TUTTI i problemi trovati.
# ============================================

existing_users = ["admin", "mario", "lucia", "guest"]

new_username = input("Inserisci uno username: ")

# Flag di controllo. Per il numero ho inserito strip() in modo da segnalare errore solo numeri in caso di stringhe tipo "12 3"
has_spaces = " " in new_username
is_in_list = new_username in existing_users
is_number = new_username.strip().isdigit()
is_short = len(new_username) < 5

username_ok = not has_spaces and not is_in_list and not is_number and not is_short

if username_ok:
    print("L'username è valido e libero")
else:
    if has_spaces:
       print("L'username contiene spazi")
    if is_in_list:
       print("L'username è già in uso")
    if is_number:
       print("L'username è un numero") 
    if is_short:
       print("L'username è troppo corto") 