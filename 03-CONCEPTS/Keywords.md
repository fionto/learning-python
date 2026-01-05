# Le Parole Chiave di Python: I Mattoni Fondamentali del Linguaggio

## Cosa Rende Speciali le Keywords

Quando iniziamo a programmare in Python, ci troviamo rapidamente di fronte a un insieme di parole che sembrano avere un potere particolare. Non possiamo usarle liberamente come nomi di variabili, non possiamo riassegnarle a nostro piacimento, e se proviamo a farlo, l'interprete ci ferma immediatamente con un messaggio di errore. Queste parole sono le **keywords** di Python, letteralmente le "parole chiave" del linguaggio.

Le keywords sono parole riservate che hanno significati e scopi specifici all'interno della sintassi di Python. Rappresentano i concetti fondamentali del linguaggio: decisioni, cicli, definizioni di funzioni, gestione delle eccezioni e molto altro. A differenza delle funzioni built-in come `print()` o `len()`, che sono sempre disponibili ma tecnicamente riassegnabili (anche se è una pessima idea), le keywords sono assolutamente intoccabili.

Proviamo a comprendere questa distinzione con un esempio concreto. Se tentassimo di usare `if` come nome di variabile, Python rifiuterebbe immediatamente il nostro codice:

```python
# Questo codice genera un SyntaxError
if = 10  # ERRORE! 'if' è una keyword riservata
```

L'interprete non ci permette nemmeno di completare questa operazione perché `if` è una parola con un significato grammaticale specifico nel linguaggio. È come tentare di usare la parola "se" come nome proprio in italiano: grammaticalmente impossibile.

Al contrario, tecnicamente potremmo sovrascrivere una funzione built-in, anche se questo creerebbe problemi enormi:

```python
# Tecnicamente possibile, ma assolutamente sconsigliato
print = "Questa è una stringa"  # Sovrascrive la funzione print()
# Ora print("Hello") non funzionerebbe più!
```

Questo codice viene accettato dall'interprete, ma rappresenta una pratica terribile che renderebbe il nostro programma inservibile. Le keywords, invece, ci proteggono da noi stessi rendendo impossibili questi errori a livello sintattico.

Python conta attualmente trentacinque keywords "vere e proprie", più quattro soft keywords introdotte nelle versioni più recenti. Questo numero è cambiato nel tempo: alcune parole sono state aggiunte con l'evoluzione del linguaggio, mentre altre sono state trasformate da keywords a funzioni built-in. È interessante notare che `print` e `exec`, che erano keywords in Python 2.7, sono diventate funzioni normali in Python 3.

## Il Concetto di Soft Keywords

Una delle innovazioni più interessanti introdotte recentemente in Python è il concetto di "soft keyword". Queste sono parole che si comportano come keywords solo in contesti specifici, permettendo così al linguaggio di evolversi senza rompere codice esistente.

L'introduzione delle soft keywords è stata resa possibile dall'adozione del parser PEG (Parsing Expression Grammar) in Python 3.9, che ha cambiato il modo in cui l'interprete analizza il codice sorgente. Questo nuovo parser è più flessibile e può distinguere quando una parola sta agendo come keyword e quando invece è semplicemente un nome di variabile o funzione.

Il motivo principale per cui sono state create le soft keywords riguarda la compatibilità con codice esistente. Quando gli sviluppatori di Python hanno introdotto il pattern matching strutturale, avevano bisogno di parole intuitive per questa funzionalità. Le scelte naturali erano `match` e `case`, usate per questo scopo in molti altri linguaggi. Tuttavia, queste parole erano già ampiamente utilizzate nel codice Python esistente come nomi di variabili o funzioni.

Trasformare `match` e `case` in keywords tradizionali avrebbe rotto milioni di righe di codice già scritto. Le soft keywords risolvono elegantemente questo problema: quando Python incontra queste parole in un contesto di pattern matching, le tratta come keywords; in tutti gli altri contesti, possono essere usate normalmente:

```python
# In questo contesto, 'match' è una soft keyword
match stato_ordine:
    case "pendente":
        print("Ordine in attesa di conferma")
    case "spedito":
        print("Ordine in transito")
    case _:
        print("Stato sconosciuto")

# In questo contesto, 'match' può essere una normale variabile
match = "La stringa corrisponde al pattern"
risultato_match = cerca_pattern(testo, pattern)
```

Attualmente, Python ha quattro soft keywords: `match`, `case`, `_` (underscore) e `type`. Quest'ultima è stata aggiunta in Python 3.12 per supportare la definizione di type alias in modo più elegante.

## Le Keywords di Valore: True, False e None

Esistono tre keywords in Python che rappresentano valori specifici e fondamentali. Questi sono valori singleton, il che significa che esiste una sola istanza di ciascuno di essi in memoria, e ogni riferimento a questi valori punta sempre esattamente allo stesso oggetto.

### True e False: I Valori Booleani

Le keywords `True` e `False` rappresentano i due stati logici fondamentali della logica booleana. A differenza di molti altri linguaggi di programmazione dove questi valori sono scritti in minuscolo (`true` e `false`), Python li richiede sempre con la prima lettera maiuscola.

Questi valori possono essere assegnati a variabili e confrontati direttamente:

```python
# Assegnazione diretta dei valori booleani
sistema_attivo = True
manutenzione_richiesta = False

# Confronto diretto con is
if sistema_attivo is True:
    print("Il sistema è operativo")
    
if manutenzione_richiesta is False:
    print("Nessuna manutenzione programmata")
```

Un concetto fondamentale in Python è quello di "truthiness" (veracità). La maggior parte dei valori in Python ha un equivalente booleano quando viene valutata in un contesto che richiede un valore vero o falso. Quasi tutti i valori sono considerati "truthy" (veritieri), mentre solo alcuni specifici sono "falsy" (falsi).

I valori falsy in Python includono: il numero zero in tutte le sue forme (`0`, `0.0`), stringhe vuote (`""`), liste vuote (`[]`), dizionari vuoti (`{}`), set vuoti (`set()`), e naturalmente `None` e `False` stesso. Tutti gli altri valori sono truthy.

Questa distinzione è importante perché ci permette di scrivere condizioni più concise:

```python
messaggio_utente = input("Inserisci un messaggio: ")

# Approccio verboso e non idiomatico
if messaggio_utente != "":
    print(f"Hai scritto: {messaggio_utente}")

# Approccio pythonic: sfrutta la truthiness
if messaggio_utente:
    print(f"Hai scritto: {messaggio_utente}")
```

È cruciale comprendere la differenza tra confrontare un valore direttamente con `True` o `False` e sfruttare la sua truthiness. Quando passiamo un valore alla funzione `bool()`, otteniamo il suo equivalente booleano:

```python
testo = "Questo è un valore truthy"

# Confronto diretto di identità (verifica se è ESATTAMENTE l'oggetto True)
print(testo is True)  # False - la stringa non è l'oggetto True

# Valutazione della truthiness
print(bool(testo) is True)  # True - la stringa è truthy

# Modo idiomatico: lascia che Python valuti la truthiness
if testo:
    print("Il testo è truthy")  # Questo viene eseguito
```

In Python idiomatico, raramente dovremmo confrontare esplicitamente con `True` o `False`. L'interprete farà automaticamente la valutazione di truthiness per noi nelle istruzioni condizionali, nei cicli, e in tutti gli altri contesti booleani.

### None: L'Assenza di Valore

La keyword `None` rappresenta l'assenza di un valore. In altri linguaggi di programmazione, questo concetto è chiamato `null`, `nil`, `undef`, o `undefined`, ma in Python abbiamo una parola specifica e inequivocabile: `None`.

`None` è particolarmente importante perché è il valore di ritorno predefinito di qualsiasi funzione che non specifica esplicitamente cosa restituire:

```python
def saluta_utente(nome):
    """Funzione che stampa un saluto ma non restituisce nulla esplicitamente"""
    print(f"Ciao, {nome}!")
    # Non c'è un'istruzione return

# Chiamiamo la funzione e catturiamo il risultato
risultato = saluta_utente("Marco")
# La funzione stampa: "Ciao, Marco!"

print(f"La funzione ha restituito: {risultato}")
# Output: "La funzione ha restituito: None"
```

Questo comportamento è perfettamente logico: se una funzione esiste principalmente per i suoi effetti collaterali (come stampare qualcosa o modificare uno stato) piuttosto che per calcolare e restituire un valore, Python restituisce automaticamente `None` per indicare "questa funzione non produce un valore significativo".

`None` è spesso usato per inizializzare variabili che verranno assegnate successivamente, o per rappresentare l'assenza opzionale di un dato:

```python
# Rappresentare un valore opzionale
configurazione_personalizzata = None  # Nessuna configurazione per ora

if utente_ha_preferenze():
    configurazione_personalizzata = carica_configurazione()

# Usare None come valore predefinito
def cerca_utente(id_utente):
    """Cerca un utente, restituisce l'utente o None se non trovato"""
    utente = database.trova(id_utente)
    return utente if utente else None
```

## Le Keywords Operatore: Logica e Confronto

Python ha scelto un approccio distintivo nel design dei suoi operatori logici e di confronto. Mentre molti linguaggi usano simboli come `&&`, `||`, e `!`, Python preferisce parole chiave in inglese: `and`, `or`, `not`. Questa scelta riflette la filosofia di Python di privilegiare la leggibilità del codice.

### L'Operatore and: La Congiunzione Logica

La keyword `and` è usata per determinare se entrambi gli operandi hanno un valore truthy. La sintassi base è semplice:

```python
espressione_sinistra and espressione_destra
```

Tuttavia, il comportamento di `and` è più sofisticato di quanto potrebbe sembrare a prima vista. Invece di valutare sempre gli operandi ai loro valori booleani e restituire `True` o `False`, `and` usa una strategia chiamata "short-circuit evaluation" (valutazione a corto circuito) e restituisce uno dei valori originali.

Ecco come funziona: se l'espressione di sinistra è falsy, `and` la restituisce immediatamente senza nemmeno valutare l'espressione di destra. Questo perché se il primo operando è falso, l'intera espressione `and` sarà comunque falsa, indipendentemente dal secondo operando. Se invece l'espressione di sinistra è truthy, `and` restituisce l'espressione di destra:

```python
# Esempio di short-circuit con and
def funzione_costosa():
    print("Questa funzione viene eseguita")
    return 42

abilitato = False

# La funzione_costosa() non viene mai chiamata perché 'abilitato' è False
risultato = abilitato and funzione_costosa()
print(f"Risultato: {risultato}")  # Output: False (la funzione non stampa nulla)

# Se abilitato fosse True, la funzione verrebbe chiamata
abilitato = True
risultato = abilitato and funzione_costosa()
# Output: "Questa funzione viene eseguita"
# Risultato: 42
```

Questo comportamento può essere sfruttato per assegnazioni condizionali concise, anche se bisogna fare attenzione a non sacrificare la leggibilità:

```python
# Assegnazione che sfrutta il comportamento di and
limiti_attivi = True
limite_massimo = 100

valore_finale = limiti_attivi and limite_massimo
# Se limiti_attivi è True, valore_finale sarà 100
# Se limiti_attivi è False, valore_finale sarà False

# Versione più esplicita e leggibile
valore_finale = limite_massimo if limiti_attivi else False
```

La versione più esplicita è generalmente preferibile perché rende immediatamente chiara l'intenzione del codice.

### L'Operatore or: La Disgiunzione Logica

La keyword `or` determina se almeno uno dei due operandi è truthy. Come `and`, anche `or` usa la valutazione a corto circuito, ma con logica inversa: se il primo operando è truthy, `or` lo restituisce immediatamente senza valutare il secondo. Altrimenti, restituisce il secondo operando:

```python
# Valutazione a corto circuito con or
configurazione_utente = None
configurazione_predefinita = {"tema": "chiaro", "lingua": "it"}

# Se configurazione_utente esiste, usala; altrimenti usa quella predefinita
configurazione_attiva = configurazione_utente or configurazione_predefinita
print(configurazione_attiva)  # Output: {"tema": "chiaro", "lingua": "it"}

# Immaginiamo che l'utente abbia configurazioni personalizzate
configurazione_utente = {"tema": "scuro", "lingua": "en"}
configurazione_attiva = configurazione_utente or configurazione_predefinita
print(configurazione_attiva)  # Output: {"tema": "scuro", "lingua": "en"}
```

Questo pattern è estremamente comune in Python per fornire valori predefiniti quando un valore potrebbe essere `None` o un'altra cosa falsy.

Un caso d'uso classico di `or` è nella validazione dell'input con condizioni multiple:

```python
def valida_credenziali(username, password):
    """Valida le credenziali, restituisce True se valide"""
    # Verifica varie condizioni di invalidità
    if not username or not password:
        print("Username e password sono obbligatori")
        return False
    
    if len(username) < 3 or len(password) < 8:
        print("Username o password troppo corti")
        return False
    
    # Se arriviamo qui, le credenziali sono valide
    return True
```

### L'Operatore not: La Negazione Logica

La keyword `not` inverte il valore di verità di un'espressione. Se l'espressione è truthy, `not` restituisce `False`; se è falsy, restituisce `True`:

```python
sistema_online = True
in_manutenzione = not sistema_online  # False

lista_risultati = []
nessun_risultato = not lista_risultati  # True (lista vuota è falsy)

# Uso comune in condizioni
if not utente_autenticato:
    print("Accesso negato: autenticazione richiesta")
    reindirizza_a_login()
```

Un idioma Python molto comune è l'uso di `not` con operatori di appartenenza per verificare l'assenza di qualcosa:

```python
utenti_bannati = ["utente123", "spammer99", "troll42"]
utente_corrente = "utente456"

# Verifica che l'utente NON sia nella lista dei bannati
if utente_corrente not in utenti_bannati:
    print("Accesso consentito")
else:
    print("Questo account è stato sospeso")
```

### L'Operatore in: Verifica di Appartenenza

La keyword `in` è un operatore di appartenenza che verifica se un elemento è contenuto in una sequenza (lista, tupla, stringa, set, dizionario):

```python
# Verifica in liste
lingue_supportate = ["italiano", "inglese", "spagnolo", "francese"]
lingua_utente = "tedesco"

if lingua_utente in lingue_supportate:
    carica_traduzione(lingua_utente)
else:
    print(f"Lingua {lingua_utente} non supportata")

# Verifica in stringhe
testo_commento = "Questo prodotto è fantastico!"
if "fantastico" in testo_commento:
    print("Commento positivo rilevato")

# Verifica in dizionari (controlla le chiavi)
configurazione = {"debug": True, "porta": 8080}
if "timeout" in configurazione:
    timeout = configurazione["timeout"]
else:
    timeout = 30  # Valore predefinito
```

L'operatore `in` è estremamente efficiente, specialmente con i set, dove la verifica di appartenenza ha complessità O(1). Con le liste, la complessità è O(n), quindi per controlli frequenti su grandi collezioni è preferibile usare set o dizionari.

### L'Operatore is: Identità degli Oggetti

La keyword `is` verifica se due riferimenti puntano esattamente allo stesso oggetto in memoria, non se i loro valori sono uguali. Questa è una distinzione sottile ma fondamentale:

```python
# Confronto di identità vs uguaglianza
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a

print(lista_a == lista_b)  # True - i valori sono uguali
print(lista_a is lista_b)  # False - sono oggetti diversi in memoria

print(lista_a is lista_c)  # True - sono lo stesso oggetto
print(lista_a == lista_c)  # True - ovviamente anche i valori sono uguali

# Visualizzare gli ID degli oggetti
print(f"ID lista_a: {id(lista_a)}")
print(f"ID lista_b: {id(lista_b)}")
print(f"ID lista_c: {id(lista_c)}")
```

L'uso più comune e appropriato di `is` è il confronto con `None`:

```python
risultato_ricerca = cerca_nel_database(query)

# Modo corretto per verificare None
if risultato_ricerca is None:
    print("Nessun risultato trovato")
else:
    elabora_risultato(risultato_ricerca)

# ERRATO: non usare == con None
if risultato_ricerca == None:  # Funziona, ma non è idiomatico
    print("Nessun risultato trovato")
```

Usare `is None` invece di `== None` è la convenzione standard in Python perché è più efficiente (confronta solo gli indirizzi di memoria) e più chiaro nell'intento.

## Keywords di Controllo del Flusso: Prendere Decisioni e Iterare

Le keywords di controllo del flusso sono quelle che permettono al nostro programma di prendere decisioni e di ripetere operazioni. Abbiamo già incontrato alcune di queste (`if`, `elif`, `else`) nella dispensa precedente, ma esistono molte altre keywords che controllano come il codice viene eseguito.

### Le Keywords dei Cicli: for, while, break, continue

Python offre due tipi principali di cicli: `for` per iterare su sequenze conosciute, e `while` per continuare finché una condizione rimane vera.

Il ciclo `for` in Python è particolarmente elegante perché itera direttamente sugli elementi di una sequenza:

```python
# Iterazione su una lista di sensori
sensori_temperatura = [22.5, 23.1, 21.8, 24.3, 22.9]

for temperatura in sensori_temperatura:
    if temperatura > 23.0:
        print(f"Temperatura elevata rilevata: {temperatura}°C")
        attiva_ventilazione()
```

Il ciclo `while` continua finché una condizione rimane vera, ed è particolarmente utile quando non sappiamo in anticipo quante iterazioni saranno necessarie:

```python
# Simulazione di un sistema di retry
tentativi_massimi = 3
tentativi_effettuati = 0
connessione_stabilita = False

while not connessione_stabilita and tentativi_effettuati < tentativi_massimi:
    print(f"Tentativo di connessione {tentativi_effettuati + 1}...")
    connessione_stabilita = prova_connessione()
    tentativi_effettuati += 1
    
    if not connessione_stabilita:
        print("Connessione fallita, riprovo tra 5 secondi...")
        time.sleep(5)

if connessione_stabilita:
    print("Connesso con successo!")
else:
    print("Impossibile stabilire la connessione dopo tutti i tentativi")
```

All'interno dei cicli, possiamo usare due keywords per controllare il flusso: `break` e `continue`.

La keyword `break` interrompe immediatamente il ciclo, uscendone completamente:

```python
# Cerca il primo elemento che soddisfa una condizione complessa
log_entries = ["INFO: Avvio sistema", "WARNING: Memoria alta", "ERROR: Crash", "INFO: Riavvio"]

for entry in log_entries:
    if "ERROR" in entry:
        print(f"Errore critico trovato: {entry}")
        break  # Interrompe la ricerca al primo errore
        # Nulla dopo break in questo blocco verrà eseguito
    print(f"Processata entry: {entry}")
```

La keyword `continue` salta il resto dell'iterazione corrente e passa immediatamente alla successiva:

```python
# Elabora solo i file validi, salta gli altri
files = ["report.pdf", "temp.tmp", "data.csv", "backup.bak", "analysis.xlsx"]

for filename in files:
    # Salta i file temporanei o di backup
    if filename.endswith((".tmp", ".bak")):
        print(f"Saltato file: {filename}")
        continue  # Passa al prossimo file
    
    # Questo codice viene eseguito solo per file validi
    print(f"Elaborazione di {filename}...")
    processa_file(filename)
```

### Le Keywords per Funzioni: def, return, yield, lambda

La keyword `def` è usata per definire funzioni in Python. Una funzione è un blocco di codice riutilizzabile che esegue un compito specifico:

```python
def calcola_sconto(prezzo_originale, percentuale_sconto):
    """
    Calcola il prezzo finale dopo l'applicazione dello sconto.
    
    Parametri:
        prezzo_originale: prezzo base del prodotto
        percentuale_sconto: sconto da applicare (0-100)
    
    Restituisce:
        Il prezzo finale scontato
    """
    if percentuale_sconto < 0 or percentuale_sconto > 100:
        raise ValueError("La percentuale deve essere tra 0 e 100")
    
    sconto = prezzo_originale * (percentuale_sconto / 100)
    prezzo_finale = prezzo_originale - sconto
    
    return prezzo_finale

# Uso della funzione
prezzo = 100.00
sconto = 20
risultato = calcola_sconto(prezzo, sconto)
print(f"Prezzo scontato: €{risultato:.2f}")
```

La keyword `return` specifica quale valore la funzione restituisce al chiamante. Una funzione può avere più istruzioni `return`, e l'esecuzione della funzione termina non appena ne viene incontrata una:

```python
def classifica_studente(voto):
    """Classifica uno studente in base al voto ottenuto"""
    if voto >= 90:
        return "Eccellente", "A"
    elif voto >= 80:
        return "Ottimo", "B"
    elif voto >= 70:
        return "Buono", "C"
    elif voto >= 60:
        return "Sufficiente", "D"
    else:
        return "Insufficiente", "F"
    
    # Questa riga non verrà mai eseguita
    print("Questo codice è irraggiungibile")

giudizio, lettera = classifica_studente(85)
print(f"Giudizio: {giudizio}, Voto: {lettera}")
```

La keyword `yield` è usata per creare generatori, funzioni speciali che producono una sequenza di valori uno alla volta invece di calcolarli tutti in una volta. Questo è estremamente utile per sequenze grandi o infinite:

```python
def genera_fibonacci(limite):
    """
    Genera i numeri di Fibonacci fino a un limite specificato.
    Usa yield per produrre un numero alla volta senza memorizzare l'intera sequenza.
    """
    a, b = 0, 1
    while a < limite:
        yield a  # Produce questo valore e sospende la funzione
        a, b = b, a + b

# I numeri vengono generati solo quando richiesti
for numero in genera_fibonacci(100):
    print(numero, end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34 55 89
```

La keyword `lambda` permette di creare piccole funzioni anonime in una singola espressione. Sono utili quando serve una funzione semplice che verrà usata una sola volta:

```python
# Lista di prodotti con prezzi
prodotti = [
    {"nome": "Laptop", "prezzo": 1200},
    {"nome": "Mouse", "prezzo": 25},
    {"nome": "Tastiera", "prezzo": 80},
    {"nome": "Monitor", "prezzo": 300}
]

# Ordina i prodotti per prezzo usando una lambda
prodotti_ordinati = sorted(prodotti, key=lambda p: p["prezzo"])

for prodotto in prodotti_ordinati:
    print(f"{prodotto['nome']}: €{prodotto['prezzo']}")

# Equivalente con una funzione normale
def estrai_prezzo(prodotto):
    return prodotto["prezzo"]

prodotti_ordinati = sorted(prodotti, key=estrai_prezzo)
```

Le lambda sono particolarmente utili con funzioni come `map()`, `filter()`, e `sorted()`, ma dovrebbero essere limitate a espressioni semplici. Per logica complessa, è sempre meglio definire una funzione normale con `def`.

## Keywords per la Gestione delle Eccezioni: try, except, finally, raise

La gestione degli errori è una parte cruciale della programmazione robusta. Python usa un sistema basato su eccezioni per gestire situazioni anomale, e le keywords `try`, `except`, `finally`, e `raise` sono gli strumenti fondamentali per questo scopo.

Il blocco `try` racchiude codice che potrebbe generare un'eccezione:

```python
def leggi_configurazione(percorso_file):
    """Legge un file di configurazione gestendo vari possibili errori"""
    try:
        # Tento di aprire e leggere il file
        with open(percorso_file, 'r') as file:
            configurazione = file.read()
            dati = json.loads(configurazione)
            return dati
            
    except FileNotFoundError:
        # Il file non esiste
        print(f"Errore: il file {percorso_file} non esiste")
        print("Utilizzo configurazione predefinita")
        return get_configurazione_predefinita()
        
    except json.JSONDecodeError as errore:
        # Il file esiste ma non è un JSON valido
        print(f"Errore nel parsing del JSON: {errore}")
        print("Il file è corrotto o malformato")
        return None
        
    except PermissionError:
        # Non abbiamo i permessi per leggere il file
        print(f"Errore: permessi insufficienti per leggere {percorso_file}")
        return None
        
    finally:
        # Questo blocco viene SEMPRE eseguito, ci sia stata o no un'eccezione
        print("Tentativo di lettura configurazione completato")
```

La keyword `except` cattura specifici tipi di eccezioni. Possiamo avere multipli blocchi `except` per gestire diversi errori in modi diversi. Il blocco `finally` è opzionale e viene eseguito sempre, sia che ci sia stata un'eccezione sia che non ce ne siano state. È tipicamente usato per operazioni di pulizia come chiudere file o connessioni.

La keyword `raise` viene usata per generare deliberatamente un'eccezione:

```python
def registra_utente(username, email, eta):
    """Registra un nuovo utente con validazione dei dati"""
    
    # Validazione username
    if not username or len(username) < 3:
        raise ValueError("L'username deve contenere almeno 3 caratteri")
    
    # Validazione email
    if "@" not in email or "." not in email:
        raise ValueError("L'email fornita non è valida")
    
    # Validazione età
    if eta < 18:
        raise ValueError("Devi avere almeno 18 anni per registrarti")
    
    if eta > 150:
        raise ValueError("Età non plausibile")
    
    # Se arriviamo qui, tutti i dati sono validi
    print(f"Utente {username} registrato con successo")
    salva_nel_database(username, email, eta)

# Uso con gestione errori
try:
    registra_utente("ab", "email@test.com", 25)
except ValueError as errore:
    print(f"Registrazione fallita: {errore}")
```

## Keywords per Classi e Programmazione Orientata agli Oggetti

Python supporta la programmazione orientata agli oggetti attraverso le keywords `class`, `self` (tecnicamente non è una keyword ma una convenzione), e varie altre che esploreremo.

La keyword `class` definisce una nuova classe, cioè un modello per creare oggetti:

```python
class ContoBancario:
    """Rappresenta un conto bancario con operazioni base"""
    
    def __init__(self, titolare, saldo_iniziale=0):
        """
        Costruttore della classe.
        __init__ non è una keyword, ma un metodo speciale.
        """
        self.titolare = titolare
        self.saldo = saldo_iniziale
        self.transazioni = []
    
    def deposita(self, importo):
        """Deposita denaro nel conto"""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        
        self.saldo += importo
        self.transazioni.append(f"Deposito: +€{importo:.2f}")
        print(f"Depositati €{importo:.2f}. Nuovo saldo: €{self.saldo:.2f}")
    
    def preleva(self, importo):
        """Preleva denaro dal conto"""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        
        if importo > self.saldo:
            raise ValueError("Saldo insufficiente")
        
        self.saldo -= importo
        self.transazioni.append(f"Prelievo: -€{importo:.2f}")
        print(f"Prelevati €{importo:.2f}. Nuovo saldo: €{self.saldo:.2f}")
    
    def mostra_saldo(self):
        """Mostra il saldo attuale"""
        return f"Saldo di {self.titolare}: €{self.saldo:.2f}"

# Creazione e uso di oggetti della classe
conto_mario = ContoBancario("Mario Rossi", 1000)
conto_mario.deposita(500)
conto_mario.preleva(200)
print(conto_mario.mostra_saldo())
```

## Keywords per Import e Modularizzazione

Python usa le keywords `import`, `from`, e `as` per gestire i moduli, permettendoci di organizzare il codice in file separati e riutilizzabili.

```python
# Import completo di un modulo
import math
risultato = math.sqrt(16)  # Usiamo math.funzione()

# Import di elementi specifici
from datetime import datetime, timedelta
adesso = datetime.now()  # Usiamo direttamente datetime()

# Import con alias
import pandas as pd  # pd è più corto di pandas
import numpy as np

# Import di tutto (sconsigliato nella maggior parte dei casi)
from math import *  # Ora tutte le funzioni di math sono disponibili direttamente
```

## Come Identificare e Lavorare con le Keywords

Python fornisce strumenti per esplorare programmaticamente le keywords disponibili. Il modulo `keyword` offre funzioni utili:

```python
import keyword

# Lista di tutte le keywords
print(f"Ci sono {len(keyword.kwlist)} keywords in Python:")
print(keyword.kwlist)

# Verifica se una stringa è una keyword
print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("print"))   # False (è una funzione built-in)

# Soft keywords
print(f"Soft keywords: {keyword.softkwlist}")
print(keyword.issoftkeyword("match"))  # True
print(keyword.issoftkeyword("type"))   # True
```

La funzione `help()` nel REPL di Python può fornire informazioni dettagliate su qualsiasi keyword:

```python
>>> help("keywords")  # Mostra tutte le keywords
>>> help("while")     # Mostra documentazione specifica su 'while'
```

## L'Evoluzione delle Keywords: Un Linguaggio che Cambia

È interessante notare come Python sia un linguaggio vivo che evolve nel tempo. Alcune parole che erano keywords in passato sono diventate funzioni, mentre nuove keywords sono state aggiunte per supportare nuove funzionalità.

Ad esempio, in Python 2.7, `print` era una keyword e si usava così:

```python
# Python 2.7 (sintassi obsoleta)
print "Hello, World"  # Nota: senza parentesi
```

In Python 3, `print` è diventata una funzione normale:

```python
# Python 3+ (sintassi attuale)
print("Hello, World")  # Con parentesi come una normale funzione
```

Questo cambiamento ha reso `print` più flessibile, permettendo ad esempio di reindirizzare l'output o specificare separatori personalizzati, operazioni impossibili quando era una keyword.

## Conclusione: I Mattoni del Linguaggio

Le keywords di Python sono i mattoni fondamentali con cui costruiamo i nostri programmi. Comprendere il loro significato, il loro uso appropriato, e le loro limitazioni è essenziale per scrivere codice Python efficace e idiomatico.

Abbiamo visto come alcune keywords (`True`, `False`, `None`) rappresentino valori fondamentali, altre (`and`, `or`, `not`, `in`, `is`) forniscano operatori logici e di confronto, altre ancora (`if`, `for`, `while`, `break`, `continue`) controllino il flusso di esecuzione, e infine come alcune (`def`, `class`, `import`) permettano di strutturare e organizzare il codice in modi sempre più sofisticati.

La distinzione tra keywords vere e proprie, che sono assolutamente riservate e immutabili, e soft keywords, che agiscono come keywords solo in contesti specifici, rappresenta un'evoluzione intelligente del linguaggio che permette di aggiungere nuove funzionalità mantenendo la compatibilità con codice esistente.

Man mano che progredirete nell'apprendimento di Python, scoprirete che padroneggiare queste keywords non significa solo memorizzare la loro sintassi, ma comprendere profondamente quando e perché usarle, sviluppando quel senso del "codice pythonic" che distingue i programmatori esperti dai principianti.