# ESERCIZIO: Tentativi di accesso
# 
# Aggiungi un attributo chiamato login_attempts alla tua classe User 
# (dell'esercizio precedente).
# 
# 1. Scrivi un metodo chiamato increment_login_attempts() che incrementi 
#    il valore di login_attempts di 1.
# 
# 2. Scrivi un altro metodo chiamato reset_login_attempts() che reimposti 
#    il valore di login_attempts a 0.
# 
# 3. Crea un'istanza della classe User e chiama increment_login_attempts() 
#    diverse volte.
# 
# 4. Stampa il valore di login_attempts per verificare che sia stato 
#    incrementato correttamente.
# 
# 5. Poi chiama reset_login_attempts() e stampa di nuovo login_attempts 
#    per verificare che sia stato reimpostato a 0.
# 
# Esempio di output desiderato:
#   Tentativi di accesso: 3
#   Tentativi di accesso dopo il reset: 0
# 
# (Nota: mantieni la classe User che hai creato nell'esercizio precedente 
# e aggiungi il nuovo attributo e i nuovi metodi)

# Scrivi il tuo codice qui sotto:

class Utente:
    """Classe che modella un semplice profilo utente"""

    def __init__(self, username, nome, cognome, età):
        self.username = username
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.tentativi_login = 0
    
    def descrivi_utente(self):
        print(f"Username: {self.username}")
        print(f"Utente: {self.nome.title()} {self.cognome.title()}")
        print(f"Age: {self.età}")

    def saluta_utente(self):
        print(f"Ciao, {self.username.title()}! Benvenuto nel sistema.")

    def increment_login_attempts(self):
        self.tentativi_login += 1
    
    def reset_login_attempts(self):
        self.tentativi_login = 0
    
def main():
    primo = Utente("theking", "Fabbrozzio", "Timoni", 85)

    primo.increment_login_attempts()
    primo.increment_login_attempts()
    primo.increment_login_attempts()

    print(f"Il numero di tentativi di login è: {primo.tentativi_login}")

    primo.reset_login_attempts()

    print(f"Il numero di tentativi di login è: {primo.tentativi_login}")

main()