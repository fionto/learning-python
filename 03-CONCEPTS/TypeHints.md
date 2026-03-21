# Type Hints in Python: Scrivere Codice che Parla

## Perché il Codice Dovrebbe Spiegare Se Stesso

Immaginate di riaprire un progetto dopo sei mesi di inattività. Tra le prime cose che incontrerete ci sarà probabilmente una funzione simile a questa:

```python
def process_data(items, factor, output_mode):
    # ... codice ...
    return result
```

La funzione esiste, il nome suggerisce qualcosa, ma le domande si moltiplicano immediatamente: `items` è una lista? Un dizionario? Un oggetto personalizzato? E `factor` è un intero o un numero decimale? La funzione cosa restituisce esattamente?

Per rispondere, bisogna aprire il corpo della funzione, leggerne la logica, risalire ai contesti in cui viene chiamata. È tempo speso, e spesso tempo speso male, soprattutto quando il codice cresce fino a decine di funzioni interconnesse.

I **type hints** nascono per risolvere questo problema alla radice. Sono annotazioni che accompagnano i parametri e il valore di ritorno di una funzione, dichiarando esplicitamente quale tipo di dato ciascuna parte si aspetta di ricevere e di produrre. Non cambiano il comportamento del programma, ma trasformano radicalmente la sua leggibilità.

---

## La Sintassi di Base

L'idea centrale è semplice: dopo il nome di ogni parametro si aggiunge una notazione che ne specifica il tipo, e dopo la firma della funzione si indica il tipo del valore restituito. La notazione usa il carattere `:` per i parametri e la freccia `->` per il tipo di ritorno.

```python
def greet(name: str) -> str:
    """
    Saluta una persona per nome.

    Args:
        name: Il nome della persona da salutare.

    Returns:
        Un messaggio di saluto personalizzato.
    """
    return f"Ciao, {name}!"
```

Rileggendo questa firma, qualsiasi programmatore capisce immediatamente: la funzione accetta una stringa e restituisce una stringa. Nessuna ambiguità, nessuna necessità di esplorare il corpo della funzione per scoprire qualcosa che la firma stessa può comunicare.

Quando una funzione non restituisce alcun valore significativo, ma agisce sugli effetti collaterali (come scrivere su un file o stampare a schermo), il tipo di ritorno si annota con `None`:

```python
def save_file(content: str, filename: str) -> None:
    """Salva il contenuto su file. Non restituisce nulla."""
    with open(filename, "w") as f:
        f.write(content)
```

Specificare `-> None` non è ridondante: è un'affermazione esplicita che chi legge non deve aspettarsi nulla in cambio dalla chiamata a questa funzione.

---

## I Tipi Fondamentali

Per i tipi primitivi di Python, la notazione è diretta e intuitiva. Si usano direttamente i tipi built-in come `int`, `float`, `str` e `bool`:

```python
def add(a: int, b: int) -> int:
    # Due interi in ingresso, un intero in uscita.
    return a + b

def calculate_percentage(score: float, total: float) -> float:
    # Lavora con numeri decimali e ne restituisce uno.
    return (score / total) * 100

def format_name(first: str, last: str) -> str:
    # Prende due stringhe e ne produce una terza.
    return f"{first.title()} {last.title()}"
```

Leggere queste firme è come leggere un contratto: la funzione si impegna a ricevere determinati tipi e a restituirne un altro specifico. La firma diventa parte della documentazione stessa del codice.

---

## Collezioni Tipizzate: Specificare il Contenuto

Uno dei punti di forza dei type hints è la possibilità di andare oltre il semplice "questa è una lista" per arrivare a dire "questa è una lista di interi". A partire da Python 3.9, questa notazione è disponibile direttamente usando le parentesi quadre:

```python
def sum_numbers(numbers: list[int]) -> int:
    """
    Calcola la somma di una lista di numeri interi.

    Args:
        numbers: Una lista di interi da sommare.

    Returns:
        Il totale come intero.
    """
    total = 0
    for num in numbers:
        total += num
    return total
```

`list[int]` non significa semplicemente "una lista": significa "una lista i cui elementi sono tutti interi". Questa precisione aggiuntiva è preziosa perché esclude ambiguità che una semplice annotazione `list` lascerebbe aperte.

Lo stesso ragionamento si applica ai dizionari. La notazione `dict[tipo_chiave, tipo_valore]` permette di specificare entrambe le dimensioni della struttura:

```python
def get_word_counts(text: str) -> dict[str, int]:
    """
    Conta le occorrenze di ciascuna parola nel testo.

    Args:
        text: Il testo da analizzare.

    Returns:
        Un dizionario con parole come chiavi e conteggi come valori.
    """
    counts: dict[str, int] = {}
    for word in text.split():
        word = word.lower().strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    return counts
```

La firma `-> dict[str, int]` comunica con precisione: le chiavi sono stringhe (le parole), i valori sono interi (i conteggi). Chi chiama questa funzione sa esattamente con quale struttura lavorerà.

---

## Le Tuple: Strutture a Lunghezza Nota

Le tuple meritano un trattamento leggermente diverso, perché possono rappresentare sia sequenze di lunghezza fissa con tipi eterogenei, sia sequenze di lunghezza variabile con un tipo omogeneo.

Quando la tupla ha una struttura fissa e ben definita, si elencano i tipi di ciascuna posizione:

```python
def get_coordinates() -> tuple[float, float]:
    """
    Restituisce le coordinate geografiche (latitudine, longitudine).

    Returns:
        Una coppia di float che rappresentano latitudine e longitudine.
    """
    return (45.4654, 9.1859)  # Milano
```

`tuple[float, float]` specifica che la tupla contiene esattamente due float. Se invece la tupla può contenere un numero variabile di elementi dello stesso tipo, si usa la notazione con i tre puntini:

```python
def get_measurements() -> tuple[float, ...]:
    """
    Restituisce una serie di misurazioni di lunghezza arbitraria.

    Returns:
        Una tupla di float con un numero variabile di elementi.
    """
    return (10.5, 20.3, 15.8, 22.1)
```

I tre puntini `...` si leggono come "e così via, dello stesso tipo": la tupla può contenere uno, dieci o cento float, e il tipo hint lo comunica chiaramente.

---

## Optional: Quando un Valore Può Non Esistere

Uno dei pattern più comuni nella programmazione è la situazione in cui una funzione potrebbe non trovare ciò che cerca e deve quindi comunicare l'assenza di un risultato. In Python, questa situazione si gestisce tradizionalmente restituendo `None`.

Il problema sorge nell'annotare correttamente questo comportamento: se la funzione può restituire sia una stringa sia `None`, annotarla come `-> str` sarebbe scorretto. È qui che entra in gioco la notazione con l'operatore `|` (disponibile a partire da Python 3.10):

```python
def find_user(user_id: int) -> str | None:
    """
    Cerca un utente nel sistema per identificativo numerico.

    Args:
        user_id: L'identificativo univoco dell'utente.

    Returns:
        Il nome dell'utente se trovato, None se l'ID non esiste.
    """
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)  # .get() restituisce None se la chiave non esiste
```

La firma `-> str | None` è precisa e informativa: dice a chi legge che deve aspettarsi la possibilità di ricevere `None` e gestirla di conseguenza. Questo tipo di trasparenza previene un'intera classe di errori, quelli che si verificano quando si tenta di chiamare un metodo su un valore che si pensava fosse una stringa ma che in realtà è `None`.

Per chi lavora con versioni precedenti di Python (3.8 o 3.9), la stessa semantica si esprimeva importando `Optional` dal modulo `typing`:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)
```

`Optional[str]` è esattamente equivalente a `str | None`. La sintassi moderna con `|` è però più leggibile e diretta, e su Python 3.10 o successivo è quella consigliata.

---

## Union: Accettare Più Tipi

A volte una funzione è sufficientemente generica da poter accettare più di un tipo di dato. Una funzione che calcola la somma di una lista, ad esempio, potrebbe lavorare indifferentemente con interi o numeri in virgola mobile:

```python
def calculate_total(values: list[int | float]) -> float:
    """
    Calcola il totale di una lista di numeri, interi o decimali.

    Args:
        values: Una lista contenente interi, float, o un misto dei due.

    Returns:
        La somma totale come numero in virgola mobile.
    """
    return float(sum(values))
```

`list[int | float]` comunica che la lista può contenere sia `int` sia `float`, in qualsiasi combinazione. Il tipo di ritorno è sempre `float`, perché la somma di un misto di interi e decimali è concettualmente sempre un numero decimale.

---

## Type Hints e Valori di Default

Un caso molto comune nella pratica è la combinazione tra type hints e valori di default per i parametri. La regola è semplice: il type hint viene scritto **prima** del segno `=` che introduce il valore di default.

```python
def connect_to_database(
    host: str,
    port: int = 5432,
    timeout: float = 30.0,
    use_ssl: bool = True
) -> bool:
    """
    Tenta una connessione al database con i parametri specificati.

    Args:
        host: L'indirizzo del server database.
        port: La porta di connessione (default: 5432, standard PostgreSQL).
        timeout: Secondi prima di abbandonare il tentativo (default: 30.0).
        use_ssl: Se usare una connessione cifrata (default: True).

    Returns:
        True se la connessione ha avuto successo, False altrimenti.
    """
    # ... logica di connessione ...
    return True
```

La struttura è sempre `parametro: tipo = valore_default`. Quando il valore di default è `None`, però, bisogna prestare attenzione: se il parametro può essere `None`, il type hint deve rifletterlo esplicitamente con la notazione `| None`:

```python
def process_items(
    items: list[str],
    filter_by: str | None = None,
    max_count: int = 100
) -> list[str]:
    """
    Elabora una lista di elementi con filtraggio opzionale.

    Args:
        items: La lista di elementi da processare.
        filter_by: Se specificato, mantiene solo gli elementi che contengono
                   questa sottostringa. Se None, non filtra nulla (default: None).
        max_count: Numero massimo di elementi da restituire (default: 100).

    Returns:
        La lista filtrata e limitata.
    """
    result = items if filter_by is None else [i for i in items if filter_by in i]
    return result[:max_count]
```

Scrivere `filter_by: str = None` sarebbe logicamente inconsistente: si dichiara il tipo come `str` ma si assegna `None` come valore di default, e `None` non è una stringa. Un corretto type checker segnalerebbe immediatamente questa contraddizione.

---

## Un Esempio Integrato: Il Validatore di Password

Per vedere come i type hints si inseriscano in un contesto reale, consideriamo una coppia di funzioni che collaborano nella validazione di una password. Il contratto tra le due funzioni diventa esplicito grazie alle annotazioni:

```python
def validate_password(password: str) -> bool:
    """
    Verifica che una password soddisfi i criteri di sicurezza.

    Criteri: almeno 8 caratteri, una lettera maiuscola,
    una cifra numerica, un carattere speciale tra !@#$%^&*.

    Args:
        password: La stringa da validare.

    Returns:
        True se la password è valida, False altrimenti.
    """
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*" for c in password):
        return False
    return True


def get_validated_password(prompt: str) -> str:
    """
    Richiede ripetutamente una password all'utente finché non è valida.

    Args:
        prompt: Il messaggio da mostrare all'utente.

    Returns:
        Una password valida inserita dall'utente.
    """
    while True:
        pwd = input(prompt)
        if validate_password(pwd):
            return pwd
        print("Password non valida. Deve contenere almeno 8 caratteri, "
              "una maiuscola, un numero e un carattere speciale.")
```

Leggendo le firme delle due funzioni si capisce immediatamente la catena logica: `validate_password` prende una stringa e restituisce un booleano, mentre `get_validated_password` prende una stringa (il prompt) e restituisce sempre una stringa (la password valida). La seconda funzione non può restituire `None` perché il ciclo `while True` garantisce che il controllo ritorni solo quando il valore è valido.

---

## Una Nota Cruciale: i Type Hints Non Impongono Nulla

C'è un aspetto fondamentale dei type hints che potrebbe sorprendere chi viene da linguaggi come Java o C++: **Python non verifica i type hints durante l'esecuzione**. Sono annotazioni informative, non guardrail tecnici.

```python
def add(a: int, b: int) -> int:
    return a + b

# Python eseguirà questo senza sollevare alcun errore:
result = add("5", "3")
print(result)  # Stampa "53" (concatenazione di stringhe, non addizione!)
```

L'interprete Python accetta questo codice senza protestare, perché le annotazioni non alterano il comportamento a runtime. Se si vuole una validazione esplicita dei tipi, bisogna aggiungerla manualmente:

```python
def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"Attesi due interi, ricevuti: {type(a).__name__}, {type(b).__name__}")
    return a + b
```

I type hints diventano però preziosi in due contesti distinti. Il primo è la leggibilità umana: uno sviluppatore che legge una firma annotata comprende immediatamente il contratto della funzione. Il secondo è l'analisi statica del codice: strumenti come `mypy` possono leggere le annotazioni e segnalare incompatibilità di tipo prima ancora che il programma venga eseguito.

```bash
# mypy analizza il codice e segnala eventuali violazioni di tipo
mypy script.py
```

Anche gli ambienti di sviluppo moderni come VS Code sfruttano le annotazioni per offrire autocompletamento più preciso e avvisi in linea quando si usa una variabile con un tipo diverso da quello atteso.

---

## TypedDict: Strutture Dati con Forma Definita

Per situazioni avanzate, in particolare quando si lavora con dizionari che hanno una struttura fissa e ben definita, il modulo `typing` offre `TypedDict`. Questo strumento permette di dichiarare esplicitamente quali chiavi un dizionario deve avere e di quale tipo devono essere i relativi valori:

```python
from typing import TypedDict

class ModuleStatus(TypedDict):
    """Struttura che descrive lo stato di un modulo della stazione spaziale."""
    state: float       # Efficienza percentuale (0-100)
    priority: str      # Livello di allerta: LOW, MEDIUM, HIGH, CRITICAL

def analyze_module(module_data: ModuleStatus) -> str:
    """
    Analizza i dati di un modulo e produce un rapporto testuale.

    Args:
        module_data: Un dizionario con le chiavi 'state' e 'priority'.

    Returns:
        Una stringa descrittiva dello stato del modulo.
    """
    if module_data["state"] < 50:
        return f"ALLERTA: efficienza critica al {module_data['state']}%"
    return f"Modulo operativo al {module_data['state']}%, priorità {module_data['priority']}"
```

`TypedDict` è concettualmente simile a definire una "forma" attesa per un dizionario. Non crea una nuova classe nel senso tradizionale, ma fornisce al type checker (e ai lettori umani) informazioni precise su quale struttura aspettarsi. È uno strumento che diventa particolarmente utile quando si lavora con strutture dati complesse che transitano tra molte funzioni.

---

## L'Abitudine che Vale la Pena Costruire

I type hints non sono un requisito di Python: il codice funziona benissimo anche senza di essi. Sono però uno di quegli strumenti il cui valore cresce in modo non lineare con la complessità del codice. In un programma di venti righe, le annotazioni sembrano ridondanti. In un progetto di duemila righe con decine di funzioni, diventano indispensabili.

L'approccio più produttivo è iniziare ad usarli sistematicamente sulle funzioni pubbliche, quelle cioè che costituiscono l'interfaccia di un modulo o di un componente. Non è necessario annotare ogni singola variabile locale, ma ogni funzione che viene definita e potenzialmente richiamata da altro codice beneficia enormemente di una firma chiara.

Pensate ai type hints come a una forma di rispetto verso chi leggerà il codice in futuro: spesso, quel lettore siete voi stessi, a distanza di tempo. Una firma ben annotata è il modo più efficace per lasciare un messaggio chiaro a quella versione futura di voi, senza richiedere di rileggere ogni singola riga per capire cosa una funzione si aspetta e cosa produce.

In questo senso, i type hints non riguardano solo la sintassi di Python. Riguardano la qualità della comunicazione che il codice stabilisce con chi lo legge, e quella è una competenza che vale la pena coltivare fin dai primi passi.