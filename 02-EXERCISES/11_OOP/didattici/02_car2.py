# ============================================================================
# PARTE 2: NUOVO CONCETTO - LA CLASSE CAR (Evoluzione)
# ============================================================================

print("\n" + "=" * 80)
print("PARTE 2: NUOVO LIVELLO - LA CLASSE CAR (Stato e Validazione)")
print("=" * 80)

class Car:
    """
    Modello digitale di un'automobile.
    
    NOVITÀ rispetto a Dog:
    1. ATTRIBUTI CON VALORE PREDEFINITO: contachilometri inizia a 0
    2. METODI GETTER: leggono attributi (leggi_contachilometri)
    3. METODI SETTER: modificano attributi con CONTROLLI
    4. VALIDAZIONE: proteggono i dati da stati inconsistenti
    5. INCAPSULAMENTO: interfaccia sicura tra esterno e dati interni
    """

    def __init__(self, marca, modello, anno):
        """
        Inizializza gli attributi essenziali della macchina.
        
        Parametri:
            marca: Casa produttrice (es. "Audi")
            modello: Modello auto (es. "A4")
            anno: Anno di fabbricazione (es. 2024)
        
        ATTRIBUTO CON VALORE PREDEFINITO:
        contachilometri non viene passato come parametro, ma inizializzato
        a 0 automaticamente. Rappresenta lo "stato iniziale" della macchina:
        quando l'auto esce dalla fabbrica, ha 0 km percorsi.
        
        Questo è un pattern importante: non tutti i dati vengono ricevuti
        dall'esterno al momento della creazione.
        """
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
        # STATO INIZIALE: ogni auto nasce con contachilometri a zero
        self.contachilometri = 0

    # ========================================================================
    # METODO GETTER: LEGGERE GLI ATTRIBUTI
    # ========================================================================

    def get_nome_descrittivo(self):
        """
        Restituisce una descrizione formattata dell'auto.
        
        PATTERN GETTER:
        Un getter è un metodo che LEGGE e FORMATTA i dati, senza modificarli.
        Non è strettamente necessario (potremmo leggere direttamente gli
        attributi), ma rende il codice più mantenibile e coerente.
        
        Vantaggio: se domani vogliamo cambiare il formato della descrizione,
        modifichiamo solo questo metodo, non tutto il codice che la usa.
        """
        nome_completo = f"{self.anno} {self.marca} {self.modello}"
        return nome_completo.title()

    def leggi_contachilometri(self):
        """
        Mostra il chilometraggio attuale dell'auto.
        
        Altro getter: stampa informazioni sull'istanza in modo leggibile.
        """
        print(f"Questa macchina ha percorso {self.contachilometri} km.")

    # ========================================================================
    # METODO SETTER CON VALIDAZIONE: MODIFICARE ATTRIBUTI IN SICUREZZA
    # ========================================================================

    def aggiorna_contachilometri(self, chilometraggio):
        """
        Modifica il valore del contachilometri con CONTROLLO.
        
        PATTERN SETTER ROBUSTO:
        Un setter non modifica semplicemente l'attributo, ma lo fa in sicurezza:
        - Valida il nuovo valore PRIMA di assegnarlo
        - Rifiuta valori che violerebbero lo stato coerente della classe
        
        PROBLEMA REALE:
        Un contachilometri non dovrebbe mai DIMINUIRE (sarebbe frode!).
        Se permettessimo assegnazioni dirette tipo:
            mia_auto.contachilometri = 10  # dopo che era 100!
        L'oggetto entrerebbe in uno stato incoerente.
        
        SOLUZIONE:
        Usare questo metodo come FILTRO che rifiuta modifiche illegittime.
        
        Parametri:
            chilometraggio: Il nuovo valore da impostare
        """
        # Controllo: il nuovo valore deve essere >= valore attuale
        if chilometraggio >= self.contachilometri:
            # Assegnazione sicura dopo validazione
            self.contachilometri = chilometraggio
            print(f"Contachilometri aggiornato a {self.contachilometri} km.")
        else:
            # Se il controllo fallisce, rifiutiamo e avvisiamo
            print(
                f"Errore: Non puoi scalare il contachilometri! "
                f"(tentativo di andare da {self.contachilometri} a {chilometraggio})"
            )

    # ========================================================================
    # METODO SETTER PER OPERAZIONI INCREMENTALI
    # ========================================================================

    def incrementa_contachilometri(self, km_percorsi):
        """
        Aumenta il contachilometri di una data quantità.
        
        PATTERN INCREMENTALE:
        Anziché impostare un valore assoluto, aggiungiamo un delta.
        Questo modella meglio il mondo reale: un'auto percorre X km in un viaggio,
        quindi accumula quei km al totale precedente.
        
        Vantaggi:
        - Semanticamente più chiaro (rappresenta un evento: "ho guidato 50 km")
        - Meno propenso a errori (non rischio di sovrascrivere il valore)
        - Coerente con il concetto di "evoluzione" dell'oggetto nel tempo
        
        Validazione:
        km_percorsi deve essere >= 0 (non puoi percorrere km negativi!)
        
        Parametri:
            km_percorsi: Quantità di km da aggiungere (deve essere positiva)
        """
        if km_percorsi >= 0:
            # Accumula il valore al totale precedente
            self.contachilometri += km_percorsi
            print(
                f"Aggiunti {km_percorsi} km. "
                f"Totale: {self.contachilometri} km."
            )
        else:
            # Rifiuta quantità negative
            print(
                f"Errore: Non puoi aggiungere km negativi! "
                f"(ricevuto: {km_percorsi})"
            )


# ============================================================================
# PARTE 3: DEMO - INCAPSULAMENTO E PROTEZIONE DATI
# ============================================================================

print("\n1. Creazione dell'istanza (stato iniziale):")
mia_auto = Car("audi", "a4", 2024)
print(f"   Auto creata: {mia_auto.get_nome_descrittivo()}")
mia_auto.leggi_contachilometri()
# Output: Questa macchina ha percorso 0 km.

# ========================================================================
# PROBLEMA: Accesso diretto agli attributi (NO - Sconsigliato!)
# ========================================================================

print("\n2. ANTIPATTERN - Modifica diretta dell'attributo (SCONSIGLIATO):")
print("   Codice: mia_auto.contachilometri = 23")
mia_auto.contachilometri = 23
print("   Risultato:")
mia_auto.leggi_contachilometri()

print("\n   ⚠️  PROBLEMA: Abbiamo aggirato i controlli di sicurezza!")
print("   Se domani aggiungiamo logica più complessa (es. controlli assicurativi),")
print("   il codice che modifica direttamente sarà INCONSISTENTE con quel controllo.")

# ========================================================================
# SOLUZIONE: Usare metodi setter (BEST PRACTICE!)
# ========================================================================

print("\n3. BEST PRACTICE - Modifica tramite METODO con validazione:")
print("   Codice: mia_auto.aggiorna_contachilometri(100)")
mia_auto.aggiorna_contachilometri(100)
print("   (Il metodo ha validato e approvato il cambio)")

print("\n4. Test della validazione - Tentativo di FRODE:")
print("   Codice: mia_auto.aggiorna_contachilometri(10)")
print("   (tentare di far regredire il contachilometri)")
mia_auto.aggiorna_contachilometri(10)
print("   ✓ Il metodo ha RIFIUTATO il cambio illegittimo!")

# ========================================================================
# EVOLUZIONE DELL'OGGETTO: L'auto "vive" e accumula km
# ========================================================================

print("\n5. Evoluzione dell'oggetto nel tempo (Viaggio 1):")
print("   L'auto percorre 50 km da Milano a Como")
mia_auto.incrementa_contachilometri(50)

print("\n6. Evoluzione dell'oggetto nel tempo (Viaggio 2):")
print("   L'auto percorre 100 km da Como a Bergamo")
mia_auto.incrementa_contachilometri(100)

print("\n7. Stato attuale dopo i viaggi:")
mia_auto.leggi_contachilometri()

print("\n8. Test della validazione su incremento - Valore negativo:")
print("   Codice: mia_auto.incrementa_contachilometri(-10)")
mia_auto.incrementa_contachilometri(-10)
print("   ✓ Il metodo ha RIFIUTATO (non puoi 'tornare indietro')")


# ============================================================================
# PARTE 4: ISTANZE MULTIPLE E INDIPENDENZA
# ============================================================================

print("\n" + "=" * 80)
print("PARTE 4: ISTANZE MULTIPLE - OGNI AUTO HA LA SUA VITA")
print("=" * 80)

# Creiamo una seconda auto con storia diversa
tua_auto = Car("fiat", "500", 2020)
print(f"\n1. Auto creata: {tua_auto.get_nome_descrittivo()}")
tua_auto.leggi_contachilometri()

print("\n2. Questa auto ha più km (è più vecchia):")
tua_auto.aggiorna_contachilometri(45000)

print("\n3. Confronto tra le due auto:")
print(f"   {mia_auto.get_nome_descrittivo()}:")
mia_auto.leggi_contachilometri()
print(f"   {tua_auto.get_nome_descrittivo()}:")
tua_auto.leggi_contachilometri()

print("\n   ✓ Due istanze completamente indipendenti:")
print(f"   - mia_auto.contachilometri = {mia_auto.contachilometri}")
print(f"   - tua_auto.contachilometri = {tua_auto.contachilometri}")
print(f"   - sono la stessa classe (Car), ma dati diversi!")


# ============================================================================
# PARTE 5: SINTESI E CONCETTI CHIAVE
# ============================================================================

print("\n" + "=" * 80)
print("PARTE 5: SINTESI - CONCETTI IMPARATI")
print("=" * 80)

sintesi = """
EVOLUZIONE DA DOG A CAR:

1. ATTRIBUTI CON VALORE PREDEFINITO:
   - Dog: tutti gli attributi ricevuti da parametri
   - Car: contachilometri inizializzato a 0 (stato iniziale)
   ➜ Non tutti i dati devono arrivare da fuori!

2. METODI GETTER (Lettura):
   - get_nome_descrittivo(): formatta i dati per presentazione
   - leggi_contachilometri(): stampa lo stato attuale
   ➜ Separare "come mostro i dati" dalla "lettura grezza"

3. METODI SETTER CON VALIDAZIONE (Modifica sicura):
   - aggiorna_contachilometri(x): imposta valore assoluto con controllo
   - incrementa_contachilometri(x): aggiunge delta con controllo
   ➜ Non permettere modifiche che violerebbero l'invariante di classe

4. INCAPSULAMENTO:
   - I dati interni (contachilometri) sono "privati" concettualmente
   - L'accesso avviene solo tramite interfacce (metodi) che hanno controlli
   - Il codice esterno non deve "toccare direttamente" gli attributi sensibili
   ➜ Proteggere l'integrità logica dell'oggetto

5. EVOLUZIONE NEL TEMPO:
   - Un oggetto non è statico: cambia stato nel tempo
   - incrementa_contachilometri() modella gli eventi che cambiano l'oggetto
   - La classe "ricorda" lo stato precedente
   ➜ Gli oggetti hanno una "storia"

6. ISTANZE INDIPENDENTI:
   - mia_auto e tua_auto condividono lo stesso codice (classe Car)
   - Ma hanno dati completamente separati
   - Modificare uno non influenza l'altro
   ➜ Tante vite parallele, stesso modello

PROSSIMO PASSO (Capitoli 9.3+):
- Valori predefiniti per gli attributi (default values in __init__)
- Ereditarietà (una classe che estende un'altra)
- Metodi speciali (__str__, __repr__)
"""

print(sintesi)

# ============================================================================
# PARTE 6: APPROFONDIMENTO - DIFFERENZA ACCESSO DIRETTO VS METODI
# ============================================================================

print("\n" + "=" * 80)
print("BONUS: PERCHÉ USARE METODI INVECE DI ACCESSO DIRETTO?")
print("=" * 80)

bonus = """
SCENARIO REALISTICO:

Immagina che domani la legislazione cambi e le auto immatricolate prima del 2020
non possono superare 100.000 km.

CODICE CON ACCESSO DIRETTO (PROBLEMA):
    if tua_auto.contachilometri < 100000:
        tua_auto.contachilometri += 500  # Diretto!
    else:
        print("Bloccato da normativa!")

PROBLEMA: Abbiamo scritto questo controllo ovunque nel nostro codice!
Se poi troviamo un altro posto dove modifichiamo direttamente l'attributo,
potremmo violare la normativa senza accorgercene.

CODICE CON METODO (SOLUZIONE):
    def incrementa_contachilometri(self, km_percorsi):
        # NUOVO: controlliamo la normativa qui!
        if self.anno < 2020 and self.contachilometri + km_percorsi > 100000:
            print("Errore: Auto pre-2020 non può superare 100k km!")
            return
        
        if km_percorsi >= 0:
            self.contachilometri += km_percorsi
        else:
            print("Errore: km non può essere negativo!")

VANTAGGIO: Modifichiamo il controllo in UN SOLO POSTO (il metodo).
Tutti i punti del codice che usano incrementa_contachilometri() automaticamente
rispetteranno la nuova normativa!

LEZIONE:
Non è pigrizia usare metodi setter. È **defensive programming**:
proteggere la classe dalle modifiche esterne che potrebbero danneggiare
la coerenza logica dell'oggetto.
"""

print(bonus)