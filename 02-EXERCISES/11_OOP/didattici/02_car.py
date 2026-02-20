class Car:
    """Modello digitale di una macchina per gestirne i dati."""

    def __init__(self, marca, modello, anno):
        """Inizializza gli attributi necessari per descrivere il veicolo."""
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
        # VALORE PREDEFINITO (Stato Iniziale):
        # Non tutti i dati devono essere forniti dall'utente al momento della creazione.
        # Qui definiamo lo 'stato iniziale' dell'oggetto: ogni auto nasce con 0 km.
        self.contachilometri = 0 
    
    def get_nome_descrittivo(self):
        """Restituisce una stringa di presentazione formattata."""
        nome_completo = f"{self.anno} {self.marca} {self.modello}"
        return nome_completo.title()
    
    def leggi_contachilometri(self):
        """Mostra il chilometraggio attuale dell'istanza."""
        print(f"Questa macchina ha percorso {self.contachilometri} km.")

    # INCAPSULAMENTO: Protezione del dato tramite Metodi
    def aggiorna_contachilometri(self, chilometraggio):
        """
        Modifica il valore del contachilometri.
        Include una logica di controllo (Validazione) per impedire dati errati.
        """
        if chilometraggio >= self.contachilometri:
            self.contachilometri = chilometraggio
        else:
            # Questo impedisce modifiche esterne che violano le regole della classe
            print("Errore: Non puoi scalare il contachilometri!")

    # ESTENSIONE DELLE FUNZIONALITÀ
    def incrementa_contachilometri(self, km_percorsi):
        """
        Aggiunge chilometri al valore esistente.
        Permette all'oggetto di evolvere nel tempo in base agli eventi (viaggi).
        """
        if km_percorsi >= 0:
            self.contachilometri += km_percorsi
        else:
            print("Errore: Non puoi incrementare con valori negativi!")

# --- TEST DELLE FUNZIONALITÀ ---

# 1. Creazione dell'oggetto (Istanza)
mia_auto = Car('audi', 'a4', '2024')
print(f"Auto creata: {mia_auto.get_nome_descrittivo()}")

# 2. Modifica DIRETTA dell'attributo (Sconsigliato per dati sensibili)
# Questo metodo è veloce ma non offre controlli di sicurezza.
mia_auto.contachilometri = 23
print("--- Aggiornamento diretto ---")
mia_auto.leggi_contachilometri()

# 3. Modifica tramite METODO (Best Practice)
# Il metodo agisce da 'filtro' e valida il dato prima di salvarlo.
# Usiamo un'interfaccia sicura per cambiare lo stato interno
mia_auto.aggiorna_contachilometri(100)
mia_auto.leggi_contachilometri()

# 4. Test della logica di controllo
# Proviamo a inserire un valore inferiore a quello attuale.
print("--- Test tentativo di frode ---")
mia_auto.aggiorna_contachilometri(10) 
mia_auto.leggi_contachilometri()

# 5. Incremento (Evoluzione dell'oggetto)
# L'oggetto 'ricorda' il suo stato precedente e lo aggiorna
mia_auto.incrementa_contachilometri(50)
mia_auto.leggi_contachilometri()