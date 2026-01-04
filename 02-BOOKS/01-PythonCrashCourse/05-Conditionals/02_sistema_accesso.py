# ESERCIZIO 2
#
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
    print(f"Ciao, {user.get('username').title()}. Benvenuto!")

    if user.get("active"):
        
        if user.get("role") == "admin":
            print("Il sistema è in modalità amministratore")

        elif user.get("role") == "guest":
            print("Il sistema è in modalità acccesso limitato")

        else:
            print("Il sistema è in modalità acccesso standard")
    
    else:
        print("Questo account è sospeso.")

