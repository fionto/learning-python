# ESERCIZIO: Classe Privileges separata
# 
# Scrivi una classe separata chiamata Privileges. 
# 
# 1. La classe dovrebbe avere un attributo, privileges, che memorizza una lista 
#    di stringhe come descritto nell'Esercizio 9-7:
#    - "può aggiungere post"
#    - "può eliminare post"
#    - "può bannare utenti"
#    - ecc.
# 
# 2. Sposta il metodo show_privileges() in questa classe.
# 
# 3. Crea un'istanza di Privileges come attributo nella classe Admin.
# 
# 4. Crea una nuova istanza di Admin e usa il tuo metodo per mostrare i suoi privilegi.
# 
# (Nota: questa separazione segue il principio di composizione invece dell'ereditarietà,
# rendendo il codice più modulare e flessibile)

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

class Previlegi:

    def __init__(self, previlegi=[]):
        self.previlegi = previlegi
    
    def mostra_previlegi(self):
        if self.previlegi:
            for previlegio in self.previlegi:
                print(f" -{previlegio}")
        else:
            print("Nessun previlegio")

class Admin(Utente):
    """
    Modella un profilo utente da amministratore 
    con previlegi speciali
    """

    def __init__(self, username, nome, cognome, età):
        super().__init__(username, nome, cognome, età)
        self.previlegi = Previlegi()

def main():
    fabbrozzio = Admin("theking", "Fabbrozzio", "Timoni", 85)

    fabbrozzio.previlegi.mostra_previlegi()

    lista_previlegi = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
    ]

    fabbrozzio.previlegi.previlegi = lista_previlegi

    fabbrozzio.previlegi.mostra_previlegi()
    
main()
