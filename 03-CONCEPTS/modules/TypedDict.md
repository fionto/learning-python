# TypedDict: Strutturare i Dati con Sicurezza di Tipo

## Introduzione: Dal Caos al Controllo

Finora avete lavorato con i dizionari come contenitori flessibili: potete aggiungere qualunque chiave, con qualunque valore, senza vincoli. Questo vi offre libertà, ma comporta un prezzo. Immaginate di gestire i dati dei sensori della vostra base spaziale. Scrivete funzioni che si aspettano un dizionario con le chiavi `"modulo"`, `"stato"`, `"timestamp"`, ma quando lo ricevete da un collega, scoprite che contiene `"modulo_name"` al posto di `"modulo"`, oppure che `"stato"` è una stringa quando dovrebbe essere un numero. Non ottenete un errore durante l'esecuzione: il codice semplicemente non funziona.

Oppure, ancora peggio, scrivete una funzione che accetta un dizionario arbitrario come parametro. Tra sei mesi, quando tornate a leggerla, dovete ricostruire mentalmente quali chiavi sono obbligatorie, quali opzionali, e di quale tipo sono i valori. Il codice diventa una scatola nera.

Python offre uno strumento per trasformare questa flessibilità incontrollata in struttura rigorosa: **`TypedDict`**. Non è uno strumento magico che crea dizionari "speciali": è un meccanismo di **annotazione di tipo** che vi consente di documentare—e farvi controllare automaticamente—la forma esatta di un dizionario. Quando usate `TypedDict`, state dicendo al vostro ambiente di sviluppo: "Questo dizionario ha esattamente queste chiavi, con esattamente questi tipi di valori". Gli strumenti come **mypy** possono poi verificare che il vostro codice rispetti questa promessa.

## Che Cosa È TypedDict?

`TypedDict` è una classe speciale, importata dal modulo `typing`, che vi permette di definire uno "schema" per un dizionario. È simile a una ricetta: non è il piatto vero e proprio, ma vi dice esattamente quali ingredienti ci vanno, e il tipo (peso, volume) di ciascuno.

Considerate questo esempio senza `TypedDict`:

```python
# Senza TypedDict: ambiguità pura
sensore = {"id": 42, "lettura": 23.5, "timestamp": "2025-04-26T10:30:00"}

def processa_sensore(dati):
    # Quali chiavi mi aspetto?
    # Sono obbligatorie tutte?
    # "id" è davvero un intero?
    print(dati["id"])
```

Con `TypedDict`, potete scrivere:

```python
from typing import TypedDict

class Sensore(TypedDict):
    id: int
    lettura: float
    timestamp: str

def processa_sensore(dati: Sensore) -> None:
    # Ora è chiaro: id è int, lettura è float, timestamp è str
    # mypy vi avvertirà se passate un dizionario "sbagliato"
    print(dati["id"])
```

## Sintassi Base: Definire un TypedDict

Esistono due modi equivalenti di definire un `TypedDict`. Il primo è quello più familiare, se siete abituati alle classi:

```python
from typing import TypedDict

class Persona(TypedDict):
    nome: str
    eta: int
    email: str

# Ora potete crearne istanze (in realtà, dizionari):
persona1 = {"nome": "Alice", "eta": 30, "email": "alice@example.com"}
```

Notate che `Persona` non è una classe vera e propria nel senso tradizionale (non ha `__init__`, non cresce le istanze con `Persona(...)`). È una **classe di annotazione**, una descrizione del tipo. Il dizionario `persona1` rimane un dizionario ordinario, ma voi—e soprattutto i vostri strumenti di analisi—sapete quale forma deve avere.

Il secondo modo, meno elegante ma a volte utile, è la sintassi funzionale:

```python
Persona = TypedDict('Persona', {'nome': str, 'eta': int, 'email': str})
```

Preferiamo la prima sintassi perché è più leggibile e coerente con il resto di Python.

## Chiavi Opzionali: Quando non Tutto è Obbligatorio

Non tutti i campi di un dizionario sono sempre presenti. Immaginate il modello di un utente: ha sempre un nome e una email, ma il numero di telefono è opzionale. `TypedDict` offre il modo di esprimere questa distinzione tramite la parola chiave `Required` e `NotRequired` (Python 3.11+), oppure tramite parametri speciali nella definizione.

Se usate Python 3.10 o precedente, la soluzione è utilizzare il parametro `total`:

```python
from typing import TypedDict

class Utente(TypedDict, total=False):
    # total=False significa che TUTTE le chiavi sono opzionali
    nome: str
    email: str
    telefono: str

# Questi sono tutti validi:
u1 = {"nome": "Bob"}
u2 = {"nome": "Bob", "email": "bob@test.com"}
u3 = {"nome": "Bob", "email": "bob@test.com", "telefono": "555-1234"}
u4 = {}  # anche un dizionario vuoto è valido
```

Se volete un mix—alcune chiavi obbligatorie, altre no—la soluzione in Python 3.11+ è usare gli annotatori `Required` e `NotRequired`:

```python
from typing import TypedDict, NotRequired

class Prodotto(TypedDict):
    id: int           # obbligatorio
    nome: str         # obbligatorio
    descrizione: NotRequired[str]  # opzionale
    prezzo: float     # obbligatorio

# Validi:
p1 = {"id": 1, "nome": "Mela", "prezzo": 0.50}
p2 = {"id": 2, "nome": "Pera", "descrizione": "Dolcissima", "prezzo": 0.75}

# Invalido (se usate mypy):
p3 = {"id": 3, "nome": "Banana"}  # Manca prezzo
```

Se usate Python 3.10 o precedente, non avete `NotRequired`. Una soluzione è ereditare da una classe base con `total=True` e una derivata con `total=False`, ma è più verbose. Per semplicità, vi consiglio di usare la strategia del `total=False` per interi dizionari opzionali, oppure di aggiornare a Python 3.11+.

## Ereditarietà e Composizione: Costruire Dizionari Complessi

Così come le classi ordinarie possono ereditare da altre classi, i `TypedDict` possono estendere altri `TypedDict`. Questo vi permette di riutilizzare strutture e di costruire gerarchie logiche.

Immaginate di modellare l'entità "Evento" di un sistema di monitoraggio. Tutti gli eventi hanno un ID, un timestamp e una severità. Ma alcuni eventi (errori) hanno anche un messaggio di errore e uno stack trace, mentre altri (avvertimenti) hanno solo un messaggio. Potete dire:

```python
from typing import TypedDict

class EventoBase(TypedDict):
    id: int
    timestamp: str
    severita: str  # "LOW", "MEDIUM", "HIGH", "CRITICAL"

class Errore(EventoBase):
    messaggio: str
    stack_trace: str

class Avvertimento(EventoBase):
    messaggio: str

# Uso:
errore: Errore = {
    "id": 1,
    "timestamp": "2025-04-26T10:30:00",
    "severita": "HIGH",
    "messaggio": "Divisione per zero",
    "stack_trace": "File 'script.py', line 42, in <module> ..."
}

avvertimento: Avvertimento = {
    "id": 2,
    "timestamp": "2025-04-26T10:31:00",
    "severita": "MEDIUM",
    "messaggio": "Memoria in esaurimento"
}
```

Con l'ereditarietà, evitate di riscrivere `id`, `timestamp`, `severita` ogni volta. Inoltre, chiunque legga il codice capisce immediatamente che `Errore` e `Avvertimento` condividono una struttura comune.

## Combinare TypedDict e Funzioni: Type Hints Completi

Il valore vero di `TypedDict` emerge quando lo usate in annotazioni di funzioni. Vedete subito quali dati la funzione si aspetta e quali produce.

```python
from typing import TypedDict

class Misurazione(TypedDict):
    sensore_id: int
    valore: float
    unita: str

class Elaborazione(TypedDict):
    media: float
    minimo: float
    massimo: float
    campioni: int

def elabora_misurazioni(dati: list[Misurazione]) -> Elaborazione:
    """
    Calcola statistiche da una lista di misurazioni.
    
    Args:
        dati: Lista di dizionari con 'sensore_id', 'valore', 'unita'
    
    Returns:
        Dizionario con 'media', 'minimo', 'massimo', 'campioni'
    """
    valori = [m["valore"] for m in dati]
    
    return {
        "media": sum(valori) / len(valori),
        "minimo": min(valori),
        "massimo": max(valori),
        "campioni": len(valori)
    }

# Uso:
dati = [
    {"sensore_id": 1, "valore": 23.5, "unita": "°C"},
    {"sensore_id": 1, "valore": 24.0, "unita": "°C"},
    {"sensore_id": 1, "valore": 23.8, "unita": "°C"}
]

risultato = elabora_misurazioni(dati)
print(f"Media: {risultato['media']}")  # mypy sa che 'media' esiste
```

Ora, se qualcuno tenta di passare una lista con dizionari malformati—per esempio, senza `"valore"`—mypy vi avvertirà **durante lo sviluppo**, non durante l'esecuzione. Se tentate di accedere a una chiave che non esiste in `risultato`, mypy vi fermerà.

## Nested TypedDict: Dizionari Dentro Dizionari

È comune avere strutture dati nidificate. Un record di un modulo della Stazione Spaziale potrebbe contenere informazioni annidate: dati generali del modulo, e un sotto-oggetto per lo stato dei sistemi.

```python
from typing import TypedDict

class StatoSistema(TypedDict):
    potenza: str  # "ON" o "OFF"
    temperatura: float
    pressione: float

class Modulo(TypedDict):
    nome: str
    funzione: str  # "Life Support", "Power", etc.
    stato_sistema: StatoSistema

# Creazione di un dizionario annidato:
modulo = {
    "nome": "COLUMBUS",
    "funzione": "European Lab Module",
    "stato_sistema": {
        "potenza": "ON",
        "temperatura": 22.5,
        "pressione": 101.3
    }
}

# Le annotazioni funzionano anche per dati annidati:
def accedi_temperatura(m: Modulo) -> float:
    return m["stato_sistema"]["temperatura"]
```

mypy ora capisce la forma completa della struttura dati e vi avvertirà se tentate di accedere a `m["stato_sistema"]["velocita"]`, che non esiste.

## Limitazioni: Cosa TypedDict NON FA

È importante sottolineare che `TypedDict` è un **strumento di annotazione statica**. Non impone alcun controllo a runtime. Se scrivete:

```python
class Persona(TypedDict):
    nome: str
    eta: int

p = {"nome": "Charlie", "eta": "ventuno"}  # eta è una stringa, non un intero
```

Python eseguirà il codice senza protestare. Il dizionario contiene una stringa dove ci si aspetta un intero. **mypy** vi avvertirà se fate un controllo statico del tipo, ma Python stesso—durante l'esecuzione—non fa nulla. È vostra responsabilità usare uno strumento come **mypy** per verificare la correttezza dei tipi.

```bash
# Per controllare il codice con mypy:
mypy script.py
```

Se avete bisogno di validazione a runtime (cioè, assicurarvi che un dizionario ricevuto da fuori abbia veramente la forma giusta), dovete scrivere manualmente i controlli, oppure usare librerie come **pydantic** che offrono validazione stricta. Ma per la maggior parte dei casi dove controllate il vostro proprio codice, mypy è sufficiente.

## Pattern Pratico: Dati Scientifici Strutturati

Ipotizzate di sviluppare un sistema che raccoglie dati spettroscopici. Ogni spettro ha un ID, parametri di acquisizione, e i dati grezzi. Potete organizzare questo con `TypedDict`:

```python
from typing import TypedDict, NotRequired

class ParametriAcquisizione(TypedDict):
    tempo_integrazione: float  # secondi
    lunghezza_onda_inizio: float  # nanometri
    lunghezza_onda_fine: float
    numero_pixel: int

class Spettro(TypedDict):
    id: str
    campione: str
    data_acquisizione: str
    parametri: ParametriAcquisizione
    intensita: list[float]
    note: NotRequired[str]

# Utilizzo in una funzione di elaborazione:
def estrai_picchi(spettro: Spettro) -> dict:
    """Trova i picchi nello spettro acquisito."""
    intensita = spettro["intensita"]
    parametri = spettro["parametri"]
    
    # elaborazione...
    return {
        "picchi": [...],
        "energia_totale": sum(intensita)
    }

# Creazione di un dato spettroscópico:
spec = {
    "id": "RAMAN_2025_001",
    "campione": "Mars_Soil_Sample",
    "data_acquisizione": "2025-04-26",
    "parametri": {
        "tempo_integrazione": 1.5,
        "lunghezza_onda_inizio": 400.0,
        "lunghezza_onda_fine": 2000.0,
        "numero_pixel": 1024
    },
    "intensita": [12.3, 14.5, 16.1, ...]
}
```

Con questo approccio, il vostro codice è auto-documentante. Chiunque legga `estrai_picchi` sa subito quale forma devono avere i dati in entrata.

## Conclusione: Dall'Ambiguità alla Struttura

`TypedDict` non vi rende improvvisamente infallibili, ma trasforma il vostro codice da un territorio selvaggio—dove i dizionari possono contenere qualunque cosa—a una regione mappata, dove ogni strada ha un nome e un'altitudine nota. Quando combinate `TypedDict` con mypy, guadagnate la capacità di **rilevare errori prima che il codice venga eseguito**, durante una fase di "revisione statica" che può essere integrata nel vostro workflow di sviluppo.

Nel prossimo capitolo, approfondiremo come integrare `TypedDict` con **pydantic**, una libreria che aggiunge validazione a runtime e serializzazione automatica. Ma per ora, considerate `TypedDict` come il primo passo verso una pratica di programmazione Python più rigorosa: scrivere meno sorprese, produrre codice più manutenibile, e soprattutto, documentare le intenzioni dei vostri dati.

Quando ritornerete al vostro codice tra tre mesi, non dovrete ricostruire mentalmente quale chiave dovrebbe avere quale tipo: lo vedrete scritto in forma dichiarativa. E quando collaborerete con altri, non dovrete spendere tempo a spiegare quale sia la forma di un dizionario: ve lo dirà il codice stesso.
