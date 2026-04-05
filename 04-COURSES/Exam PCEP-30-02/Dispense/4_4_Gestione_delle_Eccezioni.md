# Capitolo 4: Sezione 4.4 - Gestione delle Eccezioni: Anticipare l'Imprevisto

## Introduzione: Quando i Piani Non Reggono la Realtà

Immaginate di essere un cassiere in un supermercato. Di solito il lavoro scorre liscio: il cliente porta la spesa, voi scansionate i prodotti, lui paga. Ma la realtà ha i suoi imprevisti: la carta di credito viene rifiutata, il codice a barre è illeggibile, il cliente vuole pagare con un assegno scaduto. Un cassiere esperto non va nel panico e non blocca tutta la cassa: ha una procedura per ogni anomalia. Chiede un altro metodo di pagamento, chiama un collega, trova una soluzione, e permette alla coda di avanzare.

In programmazione, le eccezioni sono quegli imprevisti. Quando un programma tenta di dividere un numero per zero, di aprire un file che non esiste, o di convertire la stringa `"ciao"` in un numero intero, Python si trova davanti a una situazione che non sa come risolvere in modo ordinario. In questi casi, Python "lancia" un'eccezione: segnala il problema interrompendo il flusso normale del codice. Se nessuno intercetta questo segnale, il programma termina con un messaggio di errore. Ma se voi, come il cassiere esperto, avete previsto l'anomalia, potete intercettarla e gestirla in modo elegante.

Nella dispensa precedente (sezione 4.3) avete incontrato la **gerarchia delle eccezioni built-in**: `BaseException`, `Exception`, `ArithmeticError`, `ValueError`, e così via. Sapete già che le eccezioni sono oggetti con un nome e una struttura. In questa dispensa imparerete a intercettarle attivamente usando il costrutto `try-except`, a scegliere con precisione quale eccezione catturare, e a capire come un'eccezione si propaga attraverso le funzioni fino a trovare chi se ne occupa.

## Il Costrutto `try-except`: La Rete di Sicurezza

La struttura di base per gestire un'eccezione è il blocco `try-except`. La logica è semplice: all'interno del blocco `try` mettete il codice che volete eseguire, quello che potrebbe causare problemi. All'interno del blocco `except` mettete il codice da eseguire se si verifica un errore.

```python
# Tentativo di conversione di un input utente in numero intero
testo = "quarantadue"

try:
    numero = int(testo)          # Questa riga solleva ValueError
    print("Numero:", numero)     # Questa riga NON viene eseguita
except ValueError:
    print("Il testo non è un numero valido.")   # Stampa: Il testo non è un numero valido.
```

Quando Python entra nel blocco `try` e incontra una riga che solleva un'eccezione, interrompe immediatamente l'esecuzione delle righe rimanenti nel `try` e salta direttamente al blocco `except` corrispondente. Se nessuna eccezione si verifica, il blocco `except` viene ignorato completamente e il programma continua normalmente.

Nell'esempio qui sopra, la riga `print("Numero:", numero)` non viene mai raggiunta, perché l'eccezione viene sollevata nella riga precedente. Questa è una caratteristica fondamentale: il `try` non è una zona sicura dove tutto viene eseguito comunque; è piuttosto un blocco sorvegliato, dove l'esecuzione si interrompe non appena emerge un problema.

Vale la pena confrontare il comportamento con e senza protezione:

```python
# Senza gestione: il programma crasha
# testo = "quarantadue"
# numero = int(testo)
# Risultato: ValueError: invalid literal for int() with base 10: 'quarantadue'
# (il programma termina qui)

# Con gestione: il programma continua
testo = "quarantadue"

try:
    numero = int(testo)
except ValueError:
    numero = 0   # Valore di default in caso di errore

print("Valore usato:", numero)   # Stampa: Valore usato: 0
```

La differenza è sostanziale: nel primo caso il programma crasha e l'utente vede un messaggio di errore tecnico incomprensibile; nel secondo caso il programma continua a funzionare, recupera con un valore di default, e l'esperienza rimane coerente.

## Catturare Eccezioni Diverse: Rami `except` Multipli

Spesso un singolo blocco `try` può sollevare eccezioni di tipo diverso, a seconda di cosa va storto. Python permette di definire più rami `except`, ognuno dedicato a un tipo specifico di eccezione.

```python
def dividi(a, b):
    try:
        risultato = a / b            # Può sollevare ZeroDivisionError
        return risultato
    except ZeroDivisionError:
        print("Errore: divisione per zero.")
        return None

# Chiamate di test
print(dividi(10, 2))    # Stampa: 5.0
print(dividi(10, 0))    # Stampa: Errore: divisione per zero. poi: None
```

Ma immaginate di voler gestire anche il caso in cui qualcuno passi una stringa invece di un numero:

```python
def dividi_robusto(a, b):
    try:
        risultato = a / b
        return risultato
    except ZeroDivisionError:
        print("Errore: il divisore non può essere zero.")
        return None
    except TypeError:
        print("Errore: i valori devono essere numeri.")
        return None

# Chiamate di test
print(dividi_robusto(10, 2))       # Stampa: 5.0
print(dividi_robusto(10, 0))       # Stampa: Errore: il divisore non può essere zero.
print(dividi_robusto(10, "due"))   # Stampa: Errore: i valori devono essere numeri.
```

Quando si verifica un'eccezione all'interno del `try`, Python esamina i rami `except` nell'ordine in cui sono scritti, dall'alto verso il basso, e salta al primo che corrisponde al tipo dell'eccezione sollevata. Gli altri rami `except` vengono ignorati, esattamente come succede con i rami `elif` in un costrutto condizionale.

## L'Ordine dei Rami `except`: Una Regola da Non Ignorare

Proprio perché Python seleziona il primo ramo `except` compatibile, l'ordine in cui li scrivete è importante: le eccezioni più specifiche devono venire prima di quelle più generiche. Se invertite quest'ordine, le eccezioni più specifiche non verranno mai raggiunte.

Ricordate dalla sezione 4.3 che `ZeroDivisionError` è una sottoclasse di `ArithmeticError`, che a sua volta è sottoclasse di `Exception`. Questo significa che un ramo `except ArithmeticError` cattura anche i `ZeroDivisionError`. Se lo mettete prima, il ramo specifico per `ZeroDivisionError` non verrà mai eseguito:

```python
# SBAGLIATO: l'ordine è invertito
try:
    x = 1 / 0
except ArithmeticError:
    print("Errore aritmetico generico.")   # Questo viene eseguito...
except ZeroDivisionError:
    print("Divisione per zero!")           # ...e questo non viene mai raggiunto!
```

```python
# CORRETTO: dal più specifico al più generico
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Divisione per zero!")           # Stampa: Divisione per zero!
except ArithmeticError:
    print("Errore aritmetico generico.")   # Non raggiunto in questo caso
```

La regola pratica è: ordinate i rami `except` dal più specifico al più generico, allo stesso modo in cui nella vita reale si gestiscono prima i casi particolari e poi quelli generali. Se avete un blocco `except Exception` alla fine, funzionerà come un "acchiappa-tutto" per qualsiasi eccezione derivata da `Exception` che non sia stata intercettata dai rami precedenti.

```python
# Schema con "acchiappa-tutto" finale
try:
    operazione_rischiosa()
except ValueError:
    print("Valore non valido.")
except TypeError:
    print("Tipo errato.")
except Exception as errore:
    # Cattura qualsiasi altra eccezione non prevista
    print(f"Errore imprevisto: {errore}")
```

La sintassi `except Exception as errore` assegna l'oggetto eccezione alla variabile `errore`, permettendovi di stampare o registrare il messaggio di errore originale. Questa tecnica è utile per il debugging e per fornire messaggi informativi all'utente.

## Catturare Più Tipi con un Solo Ramo

A volte volete eseguire la stessa azione di gestione per due o più tipi di eccezione diversi. Invece di duplicare il codice del ramo `except`, potete elencare i tipi in una tupla all'interno dello stesso ramo:

```python
testo = input("Inserisci un numero intero: ")

try:
    valore = int(testo)
    risultato = 100 / valore
    print(f"100 / {valore} = {risultato}")
except (ValueError, ZeroDivisionError):
    print("Input non valido: inserisci un intero diverso da zero.")
```

In questo modo, sia che l'utente inserisca una stringa non convertibile (che produce `ValueError`) sia che inserisca zero (che produce `ZeroDivisionError`), la risposta del programma è la stessa. La tupla tra parentesi raccoglie tutti i tipi che volete intercettare con quel ramo.

## La Propagazione delle Eccezioni: Chi Gestisce il Problema?

Finora abbiamo visto esempi in cui il `try-except` si trova nella stessa funzione dove si verifica l'errore. Ma cosa succede quando l'eccezione si solleva all'interno di una funzione chiamata, e lì non c'è nessun gestore?

In questo caso, l'eccezione non scompare: si **propaga** verso l'alto nella catena delle chiamate. Python cerca un gestore risalendo le chiamate di funzione una a una, finché non ne trova uno. Se arriva in cima alla catena (cioè nel codice principale del programma) senza trovare nessun gestore, il programma termina con un traceback.

```python
def converti(testo):
    # Nessun try-except qui: se si solleva un'eccezione, si propaga verso chi chiama
    return int(testo)

def elabora(valore):
    # Nessun try-except neanche qui
    return converti(valore) * 2

# Il gestore si trova qui, al livello più alto
try:
    risultato = elabora("ciao")
    print("Risultato:", risultato)
except ValueError:
    print("Impossibile elaborare il valore: non è un numero intero.")

# Stampa: Impossibile elaborare il valore: non è un numero intero.
```

Nell'esempio, `elabora()` chiama `converti()`, che tenta di eseguire `int("ciao")`. Questa riga solleva un `ValueError`. Dal momento che `converti()` non ha un gestore, l'eccezione risale a `elabora()`. Neanche `elabora()` ha un gestore, quindi l'eccezione continua a risalire fino al blocco `try-except` nel codice principale, che finalmente la intercetta.

Questo meccanismo è potente perché separa il codice che fa il lavoro dal codice che gestisce gli errori. Le funzioni interne possono concentrarsi sulla loro responsabilità principale, senza essere appesantite dalla logica di gestione degli errori; il livello che ha il contesto giusto per decidere cosa fare si occupa di intercettare il problema.

## Delega della Responsabilità: Progettare la Gestione degli Errori

La propagazione non è solo un meccanismo tecnico: è uno strumento di progettazione. Decidere dove mettere il `try-except` equivale a decidere chi ha la responsabilità di gestire un certo tipo di errore.

Considerate questa situazione: avete una funzione che legge un numero da un file. Se il file contiene dati corrotti, si solleva un'eccezione. Chi dovrebbe gestirla?

```python
def leggi_numero_da_file(nome_file):
    """Legge un intero da un file. Propaga FileNotFoundError e ValueError."""
    with open(nome_file, "r") as f:     # Può sollevare FileNotFoundError
        contenuto = f.read().strip()
        return int(contenuto)           # Può sollevare ValueError

def calcola_doppio(nome_file):
    """Calcola il doppio del numero nel file."""
    numero = leggi_numero_da_file(nome_file)   # Non gestisce: propaga verso l'alto
    return numero * 2

# Il livello principale gestisce entrambi i casi
try:
    risultato = calcola_doppio("dati.txt")
    print("Doppio:", risultato)
except FileNotFoundError:
    print("Errore: il file 'dati.txt' non esiste.")
except ValueError:
    print("Errore: il file non contiene un numero intero valido.")
```

La funzione `leggi_numero_da_file()` è una funzione di utilità: sa fare una cosa sola e la fa bene. Non ha il contesto per decidere cosa fare se il file manca (forse il chiamante vuole crearlo, forse vuole usare un valore di default, forse vuole chiedere all'utente un percorso alternativo). Quindi non gestisce l'eccezione: la documenta nel suo docstring e la lascia propagare. Il codice principale, che ha il contesto completo dell'applicazione, decide come comportarsi.

Questo approccio rende il codice più modulare e riutilizzabile: la stessa funzione `leggi_numero_da_file()` può essere chiamata da contesti diversi, ognuno dei quali gestirà le eccezioni in modo appropriato alla propria logica.

## Un Esempio Completo: Validazione Interattiva

Per consolidare tutti i concetti, ecco uno scenario realistico: un ciclo che continua a chiedere all'utente un numero intero finché non ne inserisce uno valido.

```python
def chiedi_intero(messaggio):
    """
    Chiede all'utente di inserire un numero intero.
    Ripete la richiesta finché l'input non è valido.
    Restituisce sempre un intero.
    """
    while True:
        testo = input(messaggio)
        try:
            valore = int(testo)
            return valore   # Esce dal ciclo solo se la conversione ha avuto successo
        except ValueError:
            print(f"'{testo}' non è un numero intero. Riprova.")

def calcola_quoziente():
    """Chiede dividendo e divisore, gestisce la divisione per zero."""
    a = chiedi_intero("Inserisci il dividendo: ")
    b = chiedi_intero("Inserisci il divisore: ")

    try:
        risultato = a / b
        print(f"{a} / {b} = {risultato}")
    except ZeroDivisionError:
        print("Impossibile dividere per zero.")

calcola_quoziente()
```

In questo programma i ruoli sono ben separati. La funzione `chiedi_intero()` si occupa esclusivamente di ottenere un intero valido dall'utente, gestendo localmente il `ValueError` perché è l'unica che sa come recuperare (chiedere di nuovo). La funzione `calcola_quoziente()` gestisce il `ZeroDivisionError` perché è lei che esegue la divisione e ha il contesto per decidere cosa stampare. La struttura è pulita, ogni livello gestisce quello che gli compete.

## L'Istruzione `raise`: Sollevare Eccezioni Intenzionalmente

Finora abbiamo parlato di eccezioni come di eventi che Python solleva automaticamente quando qualcosa va storto a livello tecnico: una divisione per zero, un tipo sbagliato, un indice fuori range. Ma esiste un altro scenario, altrettanto comune: voi, come programmatori, volete interrompere il flusso perché una condizione logica non è soddisfatta, anche se Python non si accorgerebbe di niente.

Pensate a una funzione che calcola la radice quadrata di un numero. Dal punto di vista di Python, chiamare quella funzione con un numero negativo non causa nessun errore immediato: il problema emerge solo più tardi, quando il risultato non ha senso. Voi potete intercettare il problema all'ingresso usando l'istruzione `raise`, che permette di sollevare deliberatamente un'eccezione specifica.

```python
import math

def radice_quadrata(numero):
    """Calcola la radice quadrata. Accetta solo valori non negativi."""
    if numero < 0:
        raise ValueError("Il numero deve essere non negativo.")
    return math.sqrt(numero)

# Chiamata corretta
print(radice_quadrata(9))    # Stampa: 3.0

# Chiamata scorretta: raise interrompe l'esecuzione
print(radice_quadrata(-4))   # Solleva: ValueError: Il numero deve essere non negativo.
```

La sintassi è semplice: `raise` seguito dal nome della classe di eccezione, con un messaggio descrittivo tra parentesi. Una volta eseguita, l'istruzione `raise` si comporta esattamente come se l'eccezione fosse stata sollevata da Python stesso: interrompe il flusso corrente e inizia a propagarsi verso l'alto nella catena delle chiamate, dove potrà essere intercettata da un blocco `try-except`.

Questa combinazione, funzione che solleva con `raise` e codice chiamante che cattura con `try-except`, è uno dei pattern più frequenti nella programmazione Python:

```python
def calcola_media(valori):
    """Calcola la media di una lista. Richiede una lista non vuota."""
    if len(valori) == 0:
        raise ValueError("Impossibile calcolare la media di una lista vuota.")
    return sum(valori) / len(valori)

dati = []

try:
    media = calcola_media(dati)
    print(f"Media: {media}")
except ValueError as errore:
    print(f"Errore nei dati: {errore}")

# Stampa: Errore nei dati: Impossibile calcolare la media di una lista vuota.
```

Scegliere quale eccezione sollevare non è arbitrario: conviene usare il tipo che meglio descrive la natura del problema. Se il problema riguarda il valore di un argomento (`-4` per una radice quadrata, lista vuota per una media), `ValueError` è la scelta naturale. Se il problema riguarda il tipo dell'argomento (avete ricevuto una stringa dove vi aspettavate un numero), `TypeError` è più appropriato. Usare i tipi built-in standard rende il codice leggibile e compatibile con le aspettative di chi usa le vostre funzioni.

## L'Istruzione `assert`: Verificare le Ipotesi Interne

Accanto a `raise`, Python offre un secondo strumento per segnalare situazioni anomale: l'istruzione `assert`. Il suo scopo è diverso e più specifico: non serve a gestire errori dell'utente o condizioni di runtime impreviste, ma a verificare le **ipotesi interne** che il programmatore fa sul proprio codice durante lo sviluppo.

L'analogia giusta è quella di un ingegnere che, mentre costruisce un ponte, inserisce dei sensori di controllo: non perché si aspetti che il ponte crolli, ma perché vuole essere avvertito immediatamente se qualcosa non torna, prima che il problema diventi critico.

La sintassi di `assert` è la seguente:

```python
assert condizione
assert condizione, "messaggio di errore"
```

Se la condizione è `True`, l'istruzione non fa nulla e il programma continua. Se la condizione è `False`, Python solleva automaticamente un'eccezione di tipo `AssertionError`, opzionalmente con il messaggio che avete fornito.

```python
def calcola_sconto(prezzo, percentuale):
    """Applica uno sconto a un prezzo."""
    # Ipotesi interne: i valori devono essere sensati
    assert prezzo >= 0, "Il prezzo non può essere negativo."
    assert 0 <= percentuale <= 100, "La percentuale deve essere tra 0 e 100."

    sconto = prezzo * percentuale / 100
    return prezzo - sconto

print(calcola_sconto(100, 20))    # Stampa: 80.0
print(calcola_sconto(50, 0))      # Stampa: 50.0
calcola_sconto(-10, 20)           # Solleva: AssertionError: Il prezzo non può essere negativo.
```

È importante capire la differenza tra `assert` e `raise`. L'istruzione `raise` è pensata per segnalare errori che possono verificarsi in un programma correttamente funzionante, come un input utente sbagliato o un file mancante: situazioni che il codice deve essere in grado di affrontare. L'istruzione `assert`, invece, segnala errori nella logica del programmatore stesso: situazioni che non dovrebbero mai verificarsi se il codice è corretto. Se un `assert` scatta in produzione, significa che c'è un bug nel programma, non che l'utente ha fatto qualcosa di sbagliato.

Per questa ragione, `assert` viene usata tipicamente durante lo sviluppo e il debugging, per rendere esplicite le assunzioni e scoprire velocemente dove la logica si rompe. Un uso classico è la verifica dei risultati intermedi in funzioni complesse:

```python
def inverti_lista(lst):
    """Restituisce una nuova lista con gli elementi in ordine inverso."""
    risultato = lst[::-1]
    # Verifica interna: la lista invertita deve avere la stessa lunghezza dell'originale
    assert len(risultato) == len(lst), "Errore interno: lunghezze diverse dopo l'inversione."
    return risultato

print(inverti_lista([1, 2, 3]))   # Stampa: [3, 2, 1]
```

In questo caso l'`assert` è ridondante dal punto di vista logico (è impossibile che lo slicing cambi la lunghezza), ma rende esplicita un'ipotesi e funge da documentazione eseguibile: chiunque legga il codice capisce immediatamente che il programmatore si aspetta quella proprietà.

## Conclusione: La Robustezza come Abitudine

Le eccezioni non sono incidenti da nascondere o da temere: sono eventi prevedibili che un programma ben scritto anticipa e gestisce con cura. Il costrutto `try-except` è lo strumento principale per intercettarle; i rami `except` multipli permettono risposte diverse a problemi diversi; l'ordine dal più specifico al più generico garantisce che la gestione sia precisa; la propagazione offre la libertà di centralizzare la logica di errore dove ha più senso. A questi strumenti si aggiungono `raise`, per segnalare intenzionalmente condizioni anomale e delegare la gestione al livello chiamante, e `assert`, per rendere esplicite le ipotesi interne e scoprire i bug prima che si nascondano in profondità.

L'abitudine di pensare in termini di "cosa può andare storto qui, e chi deve occuparsene?" è una delle caratteristiche che distingue il codice robusto dal codice fragile. Un programma che crasha al primo input inatteso non è finito: è semplicemente un programma che non ha ancora incontrato la realtà.

Con la sezione 4.4 si chiude il Capitolo 4 dedicato alle funzioni e alle eccezioni. Avete ora una visione completa di come definire funzioni (4.1), come gestire parametri, scope e visibilità (4.2), come leggere la gerarchia delle eccezioni built-in (4.3), e finalmente come intercettare e gestire quelle eccezioni in modo strutturato (4.4). I capitoli successivi vi porteranno verso le collezioni di dati, i moduli, e la programmazione orientata agli oggetti: un mondo più vasto, che si fonda sulle stesse fondamenta che avete costruito qui.