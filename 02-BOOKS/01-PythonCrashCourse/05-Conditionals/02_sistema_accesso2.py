# Scrivi un programma che:
# saluti ogni utente
# se l’utente non è attivo, mostri un messaggio di account sospeso
# se è attivo:
# se è admin, mostri un messaggio speciale
# se è guest, limiti l’accesso
# altrimenti, accesso standard

users = [
    {"username": "admin", "role": "admin", "active": True},
    {"username": "mario", "role": "user", "active": True},
    {"username": "lucia", "role": "user", "active": False},
    {"username": "guest", "role": "guest", "active": True},
]

for user in users:
    username = user["username"]
    role = user["role"]
    active = user["active"]

    print(f"Ciao, {username.title()}. Benvenuto!")

    if not active:
        print("Questo account è sospeso.")
    elif role == "admin":
        print("Il sistema è in modalità amministratore")
    elif role == "guest":
        print("Il sistema è in modalità accesso limitato")
    else:
        print("Il sistema è in modalità accesso standard")
