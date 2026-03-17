# ESERCIZIO: Classe User
# 
# Crea una classe chiamata User. 
# 
# 1. Crea due attributi chiamati first_name e last_name, e poi crea diversi altri 
#    attributi che sono tipicamente memorizzati in un profilo utente (es. età, 
#    città, email, hobby, professione, ecc.).
# 
# 2. Crea un metodo chiamato describe_user() che stampi un riepilogo delle 
#    informazioni dell'utente.
# 
# 3. Crea un altro metodo chiamato greet_user() che stampi un saluto 
#    personalizzato per l'utente.
# 
# 4. Crea diverse istanze che rappresentano utenti diversi e chiama entrambi 
#    i metodi per ciascun utente.
# 
# (Nota: sentiti libero di personalizzare gli attributi aggiuntivi 
# e il formato dell'output come preferisci)

class Utente:
    """Classe che modella un semplice profilo utente"""

    def __init__(self, username, nome, cognome, età):
        self.username = username
        self.nome = nome
        self.cognome = cognome
        self.età = età
    
    def descrivi_utente(self):
        print(f"Username: {self.username}")
        print(f"Utente: {self.nome.title()} {self.cognome.title()}")
        print(f"Age: {self.età}")

    def saluta_utente(self):
        print(f"Ciao, {self.username.title()}! Benvenuto nel sistema.")
    
def main():
    primo = Utente("drunk1", "Mario", "Rossi", 25)
    secondo = Utente("theking", "Fabbrozzio", "Timoni", 85)

    primo.descrivi_utente()
    secondo.saluta_utente()

main()