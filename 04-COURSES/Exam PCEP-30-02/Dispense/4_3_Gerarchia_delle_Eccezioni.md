# Capitolo 4: Sezione 4.3 - Gerarchia delle Eccezioni: Quando Python Segnala che Qualcosa è Andato Storto

## Introduzione: Le Eccezioni Come Segnali di Allarme

Immaginate di trovarvi in cucina e di chiedere a qualcuno di prendere il sale dall'armadietto. Se l'armadietto è vuoto, quella persona non può semplicemente restituirvi il nulla e andare avanti come se niente fosse: deve fermarsi, dirvi che il sale non c'è, e aspettare che voi decidiate cosa fare. Non può neanche inventarsi il sale al posto. Si ferma, segnala il problema, e la palla torna a voi.

Python funziona in modo molto simile. Quando un programma incontra una situazione che non riesce a gestire da solo, non inventa un risultato a caso né prosegue silenziosamente: si ferma e lancia un segnale di errore ben preciso. Questo segnale si chiama **eccezione**. Un'eccezione non è un bug segreto: è Python che vi dice, chiaramente e in modo strutturato, che cosa è andato storto e dove.

Fino a questo punto del corso avete probabilmente già incontrato qualche eccezione, magari per sbaglio: avete diviso un numero per zero, o avete cercato di sommare un numero a una stringa. Quello che avete visto sullo schermo non era un messaggio generico, ma un messaggio preciso con un nome specifico. In questa dispensa capiremo perché quei nomi esistono, come sono organizzati, e cosa comunicano ciascuno.

Comprendere la gerarchia delle eccezioni è fondamentale per due ragioni. La prima: quando leggete un messaggio di errore, sapete immediatamente di che natura è il problema. La seconda: quando imparerete a gestire le eccezioni (che è il tema della prossima sezione, 4.4), saprete scegliere con precisione quali errori intercettare e quali lasciare propagare. Iniziamo dall'alto della gerarchia e scendiamo verso i casi concreti.

## La Radice di Tutto: `BaseException`

Tutte le eccezioni di Python sono oggetti. E come tutti gli oggetti, appartengono a delle classi. Le classi delle eccezioni sono organizzate in un albero genealogico: ogni eccezione ha un "genitore" più generale, e può avere dei "figli" più specifici. Questa organizzazione si chiama **gerarchia delle eccezioni**.

Al vertice assoluto di questa gerarchia si trova la classe `BaseException`. È la radice dell'albero: ogni singola eccezione che Python può sollevare è, in un certo senso, una specializzazione di `BaseException`. Non la vedrete quasi mai scritta direttamente nel vostro codice, ma è importante sapere che esiste, perché tutto quello che studieremo discende da essa.

Direttamente sotto `BaseException` si trovano alcune eccezioni speciali che non riguardano gli errori del vostro codice, ma eventi particolari del ciclo di vita del programma. Le due più importanti per l'esame PCEP sono `SystemExit` e `KeyboardInterrupt`.

`SystemExit` viene sollevata quando il programma chiede esplicitamente di terminare, di solito tramite la funzione `sys.exit()`. Non è un errore nel senso tradizionale: è il programma stesso che decide di fermarsi in modo controllato.

`KeyboardInterrupt` invece viene sollevata quando l'utente preme `Ctrl+C` durante l'esecuzione di un programma. Anche in questo caso, non è un bug del codice: è un segnale esterno che interrompe il flusso. Se avete mai fermato un programma con `Ctrl+C` in un terminale e avete visto comparire il messaggio `KeyboardInterrupt`, ora sapete da dove viene.

```python
# Questo script dimostra come KeyboardInterrupt possa comparire
# (non eseguire in ambienti interattivi senza terminale)
import sys

# sys.exit() solleva SystemExit internamente
# sys.exit(0)  # 0 significa uscita normale

# KeyboardInterrupt non si genera nel codice:
# arriva dall'esterno quando l'utente preme Ctrl+C
```

## La Classe `Exception`: Il Cuore degli Errori del Programmatore

Subito sotto `BaseException`, e separata da `SystemExit` e `KeyboardInterrupt`, si trova la classe `Exception`. Questa è la classe più importante per chi scrive codice Python di tutti i giorni. Tutti gli errori che derivano da un problema nel vostro programma (un calcolo impossibile, un tipo sbagliato, un indice fuori range) discendono da `Exception`.

La distinzione non è casuale. `SystemExit` e `KeyboardInterrupt` non sono errori del programmatore: sono eventi del sistema. `Exception`, invece, raccoglie tutto ciò che è andato storto per una ragione legata alla logica del codice. Quando studierete la gestione delle eccezioni, quasi sempre lavorerete con sottoclassi di `Exception`, non con `BaseException` direttamente.

Anche `Exception` è una classe astratta nel senso pratico: non la userete quasi mai da sola. Serve come punto comune da cui discendono famiglie di eccezioni più specifiche. Due di queste famiglie sono particolarmente importanti: `ArithmeticError` e `LookupError`.

## `ArithmeticError`: Gli Errori dei Calcoli

`ArithmeticError` è la classe genitore di tutti gli errori che riguardano operazioni aritmetiche. È anch'essa una classe "intermedia", cioè esiste per raggruppare logicamente gli errori numerici, ma difficilmente la incontrerete da sola in un messaggio di errore. Quello che vedrete più spesso sono i suoi figli.

Il caso più classico è la divisione per zero. In matematica, la divisione per zero non è definita. In Python, se tentate di dividere un numero per zero, ottenete un errore. Questo errore si chiama `ZeroDivisionError` ed è una sottoclasse di `ArithmeticError`.

```python
# Divisione per zero con numeri interi
risultato = 10 / 0
# Output:
# ZeroDivisionError: division by zero
```

```python
# Anche la divisione intera e il modulo per zero producono lo stesso errore
risultato = 10 // 0
# ZeroDivisionError: integer division or modulo by zero

resto = 10 % 0
# ZeroDivisionError: integer division or modulo by zero
```

Il messaggio di errore è preciso: Python vi dice esattamente dove ha trovato il problema e perché non ha potuto continuare. Questo è il valore delle eccezioni nominate: non leggete "errore generico", leggete `ZeroDivisionError`, e capite immediatamente.

## `LookupError`: Gli Errori di Ricerca

`LookupError` raggruppa gli errori che si verificano quando cercate qualcosa in una struttura dati e non lo trovate, oppure lo cercate in una posizione che non esiste. Anche in questo caso è una classe genitore, e i suoi figli più importanti sono `IndexError` e `KeyError`.

### `IndexError`: L'Indice Fuori Range

Quando lavorate con le liste (o le tuple, o le stringhe), ogni elemento ha una posizione numerica chiamata **indice**. Se cercate di accedere a un indice che non esiste, Python solleva un `IndexError`. Pensate a una fila di sedie numerate: se la fila ha cinque posti (numerati da 0 a 4) e chiedete il posto numero 10, non esiste, e qualcuno ve lo farà notare.

```python
# Una lista con tre elementi (indici 0, 1, 2)
frutti = ["mela", "banana", "ciliegia"]

print(frutti[0])   # Stampa: mela     — corretto
print(frutti[2])   # Stampa: ciliegia — corretto

print(frutti[5])
# Output:
# IndexError: list index out of range
```

```python
# Lo stesso vale con gli indici negativi fuori range
print(frutti[-4])
# IndexError: list index out of range
# (con 3 elementi, il minimo indice negativo valido è -3)
```

`IndexError` è tra le eccezioni che incontrerete più spesso, specialmente quando lavorate con i cicli e le liste. Di solito indica che il vostro codice sta cercando di accedere a un elemento in più rispetto a quelli disponibili.

### `KeyError`: La Chiave Assente nel Dizionario

Se `IndexError` riguarda le posizioni nelle sequenze, `KeyError` riguarda le chiavi nei dizionari. Quando tentate di accedere a un valore usando una chiave che non esiste nel dizionario, Python solleva un `KeyError`. L'analogia è quella di un archivio: se cercate una cartella con un'etichetta che non esiste nell'archivio, l'archivista non può inventarla.

```python
# Un dizionario con alcune chiavi
capitali = {"Italia": "Roma", "Francia": "Parigi", "Germania": "Berlino"}

print(capitali["Italia"])    # Stampa: Roma      — chiave presente
print(capitali["Spagna"])
# Output:
# KeyError: 'Spagna'
# (la chiave "Spagna" non esiste nel dizionario)
```

La differenza tra `IndexError` e `KeyError` rispecchia la differenza tra le strutture dati sottostanti: le sequenze si accedono per posizione numerica, i dizionari si accedono per chiave arbitraria. Quando leggete l'uno o l'altro in un messaggio di errore, sapete già se il problema riguarda una lista o un dizionario.

## `TypeError`: Il Tipo Sbagliato per l'Operazione

`TypeError` è un'eccezione che discende direttamente da `Exception` (non passa per `ArithmeticError` né per `LookupError`) e segnala che un'operazione è stata applicata a un oggetto del tipo sbagliato. È come usare un cacciavite come martello: lo strumento esiste, ma non è quello giusto per il compito.

Il caso più intuitivo è tentare di sommare tipi incompatibili. In Python, potete sommare due stringhe (concatenazione) oppure due numeri, ma non un numero e una stringa.

```python
# Tentativo di sommare un intero e una stringa
numero = 42
testo = " è la risposta"

risultato = numero + testo
# Output:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Il messaggio è dettagliato: Python vi dice quali tipi erano coinvolti e per quale operazione non era supportata.

```python
# TypeError può comparire anche chiamando una funzione
# con il tipo di argomento sbagliato
import math

math.sqrt("quattro")
# Output:
# TypeError: must be real number, not str
```

```python
# O cercando di iterare su un oggetto non iterabile
for carattere in 42:
    print(carattere)
# Output:
# TypeError: 'int' object is not iterable
```

`TypeError` è spesso il segnale che c'è una conversione di tipo mancante nel vostro codice. La soluzione tipica è usare le funzioni di casting come `int()`, `str()`, `float()` che avete incontrato nella sezione 1.4.

## `ValueError`: Il Tipo Giusto, ma il Valore Sbagliato

`ValueError`, anch'essa figlia diretta di `Exception`, segnala una situazione leggermente diversa da `TypeError`. Qui il tipo dell'argomento è quello corretto, ma il **valore** specifico non è accettabile per l'operazione. Il tipo era giusto, ma il contenuto no.

L'esempio più classico: provate a convertire in intero una stringa che contiene del testo che non rappresenta un numero.

```python
# str -> int funziona solo se la stringa contiene cifre
numero = int("42")       # Funziona: "42" rappresenta il numero 42
print(numero)            # Stampa: 42

numero_sbagliato = int("quarantadue")
# Output:
# ValueError: invalid literal for int() with base 10: 'quarantadue'
```

Il tipo (`str`) era quello atteso da `int()`, ma il valore `"quarantadue"` non può essere convertito. Confrontate questo con `TypeError`: se aveste passato una lista invece di una stringa, otterreste `TypeError`; passando una stringa con contenuto non numerico, ottenete `ValueError`.

```python
# ValueError con math.sqrt per radice di numero negativo
import math

radice = math.sqrt(-1)
# Output:
# ValueError: math domain error
# (-1 non ha radice quadrata nel campo dei reali)
```

```python
# ValueError con il metodo index() delle liste
frutti = ["mela", "banana", "ciliegia"]
posizione = frutti.index("kiwi")
# Output:
# ValueError: 'kiwi' is not in list
```

La distinzione tra `TypeError` e `ValueError` è sottile ma importante. Quando costruite funzioni che accettano argomenti, capire se dovete aspettarvi l'uno o l'altro vi aiuta a interpretare i messaggi di errore e a scrivere controlli più precisi.

## La Gerarchia in Prospettiva: Perché Questo Albero Esiste

Avete ora incontrato le eccezioni più importanti per l'esame PCEP. Vale la pena fermarsi un momento per capire perché Python ha costruito questa struttura ad albero invece di avere semplicemente un elenco piatto di errori.

La ragione è che la gerarchia permette di "catturare" le eccezioni a diversi livelli di specificità. Questo diventerà chiaro nella sezione 4.4, quando studierete i blocchi `try-except`. Per ora, basti sapere che se intercettate `LookupError`, state intercettando sia `IndexError` che `KeyError` in un colpo solo. Se intercettate `Exception`, state intercettando praticamente qualsiasi errore del programma. Se intercettate `BaseException`, intercettate persino `SystemExit` e `KeyboardInterrupt`, il che è quasi sempre sbagliato fare.

La gerarchia, riassunta in modo visivo, è questa:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    └── ValueError
```

Ogni nodo dell'albero è una classe Python. Ogni eccezione "è un" caso più specifico del suo genitore: un `IndexError` è una forma di `LookupError`, che è una forma di `Exception`, che è una forma di `BaseException`. Questa relazione si chiama **ereditarietà**, e tornerà centrale quando approfondirete la programmazione orientata agli oggetti.

## Leggere i Traceback: Un'Abilità Pratica

Conoscere i nomi delle eccezioni diventa immediatamente utile quando Python vi mostra un **traceback**, cioè il messaggio di errore completo che appare quando un'eccezione non viene gestita. Un traceback contiene tre informazioni essenziali: dove è andato storto il codice (il file e la riga), qual è la sequenza di chiamate che ci ha portato lì, e il nome e la descrizione dell'eccezione.

```python
# Questo codice produce un traceback completo
def dividi(a, b):
    return a / b    # Riga 2

def calcola():
    risultato = dividi(10, 0)   # Riga 5
    print(risultato)

calcola()   # Riga 8
```

```
Traceback (most recent call last):
  File "esempio.py", line 8, in <module>
    calcola()
  File "esempio.py", line 5, in calcola
    risultato = dividi(10, 0)
  File "esempio.py", line 2, in dividi
    return a / b
ZeroDivisionError: division by zero
```

Il traceback si legge dal basso verso l'alto: l'ultima riga indica il tipo di eccezione e il motivo, le righe precedenti mostrano la catena di chiamate che ha portato all'errore. Notate come Python sia preciso: non dice "c'è un errore da qualche parte", dice "riga 2 della funzione `dividi`, chiamata dalla riga 5 di `calcola`, chiamata dalla riga 8". Con questa informazione e la conoscenza del tipo di eccezione, individuare e correggere il problema diventa molto più rapido.

## Conclusione: Una Mappa per Orientarsi negli Errori

Avete ora una mappa concettuale delle eccezioni built-in di Python. Al vertice sta `BaseException`, dalla quale discendono due rami particolari (`SystemExit` per le uscite controllate e `KeyboardInterrupt` per le interruzioni da tastiera) e la grande famiglia di `Exception`, che raccoglie tutti gli errori che riguardano il codice. Dentro `Exception` trovate `ArithmeticError` (e il suo figlio `ZeroDivisionError`), `LookupError` (con `IndexError` e `KeyError`), `TypeError` e `ValueError`.

Ogni nome non è arbitrario: è una descrizione precisa della natura dell'errore. `TypeError` significa che il tipo dell'oggetto non era adatto all'operazione. `ValueError` significa che il tipo andava bene, ma il valore no. `IndexError` e `KeyError` significano che avete cercato qualcosa che non c'era, rispettivamente in una sequenza o in un dizionario.

Nella prossima sezione (4.4) metterete questa conoscenza al lavoro. Imparerete a scrivere blocchi `try-except` che intercettano le eccezioni prima che il programma si blocchi, permettendovi di gestire i casi anomali in modo elegante e controllato. La gerarchia che avete appena imparato sarà il vostro strumento per decidere, con precisione chirurgica, quali eccezioni gestire e come.
