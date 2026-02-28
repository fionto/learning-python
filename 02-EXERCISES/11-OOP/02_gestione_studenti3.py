class Studente:
    
    def __init__(self, nome):
        self.nome = nome

        # Creo una lista interna per i voti.
        # Il trattino basso indica che è un attributo "interno"
        # e non dovrebbe essere modificato direttamente dall'esterno.
        self._voti = []

    def aggiungi_voto(self, voto):
        # Questo è il metodo ufficiale per modificare i voti.
        # Qui posso applicare controlli e regole.
        if 0 <= voto <= 30:
            self._voti.append(voto)

    @property
    def voti(self):
        # Questa è una property: permette di leggere i voti
        # come se fossero un attributo pubblico (nomeoggetto.voti),
        # ma in realtà sto eseguendo questo metodo.
        
        # Non restituisco la lista originale _voti.
        # Restituisco una COPIA della lista.
        # Questo è fondamentale per l'incapsulamento:
        # chi riceve questa lista non può modificare quella interna.
        return self._voti.copy()


# Creo un nuovo oggetto Studente.
s = Studente('Jimmy')

# Qui sembra che io stia modificando i voti dello studente.
s.voti.append(30) # Ma in realtà cosa succede?

# 1) Python esegue la property "voti"
# 2) La property restituisce una COPIA della lista _voti (che è vuota)
# 3) append(30) viene eseguito su quella copia
# 4) La copia modificata NON viene salvata da nessuna parte
#
# Quindi la lista interna _voti rimane invariata.

# Qui di nuovo viene chiamata la property.
# Viene restituita una nuova copia di _voti.
# Siccome _voti è ancora vuota, verrà stampata una lista vuota.
print(s.voti)
