# ESERCIZIO: Amministratore
# 
# Un amministratore è un tipo speciale di utente.
# 
# 1. Scrivi una classe chiamata Admin che erediti dalla classe User che hai 
#    creato negli esercizi precedenti.
# 
# 2. Aggiungi un attributo chiamato privileges che memorizzi una lista di 
#    stringhe come:
#    - "può aggiungere post"
#    - "può eliminare post" 
#    - "può bannare utenti"
#    - e così via (sentiti libero di aggiungere altri privilegi)
# 
# 3. Scrivi un metodo chiamato show_privileges() che elenchi i privilegi 
#    dell'amministratore.
# 
# 4. Crea un'istanza di Admin e chiama il metodo show_privileges().
# 
# Esempio di output desiderato:
#   Privilegi dell'amministratore:
#   - può aggiungere post
#   - può eliminare post
#   - può bannare utenti
#   - può modificare impostazioni
# 
# (Nota: eredita dalla classe User esistente e mantieni tutti i suoi attributi 
# e metodi, aggiungendo solo le funzionalità specifiche per Admin)

class Utente:
    """Modella un semplice profilo utente"""

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


class Admin(Utente):
    """
    Modella un profilo utente da amministratore 
    con previlegi speciali
    """

    def __init__(self, username, nome, cognome, età):
        super().__init__(username, nome, cognome, età)
        self.previlegi = []

    def mostra_previlegi(self):
        if self.previlegi:
            for previlegio in self.previlegi:
                print(f" -{previlegio}")
        else:
            print("Nessun previlegio")

def main():
    fabbrozzio = Admin("theking", "Fabbrozzio", "Timoni", 85)

    fabbrozzio.mostra_previlegi()

    fabbrozzio.previlegi = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
    ]

    fabbrozzio.mostra_previlegi()

main()