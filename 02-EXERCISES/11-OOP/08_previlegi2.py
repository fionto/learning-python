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
        print(f"Età: {self.età}")

    def saluta_utente(self):
        print(f"Ciao, {self.username.title()}! Benvenuto nel sistema.")

    def incrementa_login(self):
        self.tentativi_login += 1
    
    def resetta_login(self):
        self.tentativi_login = 0


class GestorePrivilegi:
    """
    Classe separata per gestire i privilegi (Composizione).
    PROMEMORIA: Ho cambiato nome da 'Privilegi' a 'GestorePrivilegi'.
    Questo aiuta a capire che questo oggetto 'gestisce' la lista, non è la lista stessa.
    """

    # IMPORTANTE: Mai usare una lista vuota [] come default!
    # Se scrivo (privilegi=[]), tutte le istanze condividono la stessa lista in memoria.
    # Se un admin aggiunge un privilegio, potrebbe apparire magicamente anche su un altro admin.
    # Usiamo None e creiamo la lista dentro.
    def __init__(self, privilegi_iniziali=None):
        if privilegi_iniziali is None:
            self.lista_privilegi = []
        else:
            self.lista_privilegi = privilegi_iniziali
    
    def mostra_privilegi(self):
        print("\n--- Privilegi Speciali ---")
        if self.lista_privilegi:
            for privilegio in self.lista_privilegi:
                print(f" - {privilegio}")
        else:
            print(" Nessun privilegio assegnato.")

    def assegna_privilegi(self, nuovi_privilegi):
        """
        Metodo per assegnare la lista dall'esterno.
        PROMEMORIA: Meglio usare un metodo invece di accedere direttamente alla variabile.
        In futuro potrei voler controllare se i privilegi sono validi prima di salvarli.
        """
        self.lista_privilegi = nuovi_privilegi


class Admin(Utente):
    """
    Modella un profilo utente da amministratore.
    PROMEMORIA: Eredita da Utente (è un utente speciale).
    """

    def __init__(self, username, nome, cognome, età):
        # super() chiama il costruttore della classe padre (Utente).
        # Così non devo riscrivere nome, cognome, età, ecc.
        super().__init__(username, nome, cognome, età)
        
        # Nel libro era: self.privileges = Privileges()
        # Questo creava confusione: obj.privileges.privileges
        # Ora scrivo: self.gestione_privilegi = GestorePrivilegi()
        # Così la catena di accesso sarà: admin.gestione_privilegi.lista_privilegi
        # È molto più leggibile: "Prendi l'admin, vai nella sua gestione privilegi, prendi la lista".
        self.gestione_privilegi = GestorePrivilegi()


def main():
    # Creo un amministratore
    fabbrozzio = Admin("theking", "Fabbrozzio", "Timoni", 85)
    
    fabbrozzio.saluta_utente()
    fabbrozzio.descrivi_utente()

    # All'inizio non ha privilegi speciali
    fabbrozzio.gestione_privilegi.mostra_privilegi()

    lista_previlegi = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
    ]

    # Come assegno i privilegi?
    # Vecchio modo (confuso e rischioso): fabbrozzio.privilegi.privilegi = lista
    # Nuovo modo (pulito): uso il metodo della classe composta
    fabbrozzio.gestione_privilegi.assegna_privilegi(lista_previlegi)

    # Verifico che abbiano been assegnati
    fabbrozzio.gestione_privilegi.mostra_privilegi()
    
    # Posso ancora usare i metodi di Utente perché Admin ereda da Utente
    fabbrozzio.incrementa_login()
    print(f"Tentativi di login attuali: {fabbrozzio.tentativi_login}")

if __name__ == "__main__":
    main()