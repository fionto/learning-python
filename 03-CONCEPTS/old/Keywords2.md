# Le **Keywords** in Python

## 1. Introduzione

In Python, le **keywords** (parole chiave) sono parole **riservate dal linguaggio** che hanno un significato sintattico preciso e non possono essere utilizzate come identificatori (nomi di variabili, funzioni, classi, moduli). Esse costituiscono la base grammaticale del linguaggio Python: senza le keywords, Python non sarebbe in grado di interpretare la struttura del codice.

---

## 2. Keywords e grammatica del linguaggio

Python è un linguaggio **interpretato**: il codice sorgente viene analizzato da un *parser* che segue una grammatica formale. Le keywords sono token speciali riconosciuti direttamente da questa grammatica. Quando il parser incontra una keyword, non la interpreta come un nome arbitrario, ma come un comando strutturale.

Esempio:

```python
for i in range(10):
    print(i)
```

Qui:

* `for` indica l’inizio di un ciclo
* `in` specifica l’iterazione su un oggetto iterabile

Tentare di usare una keyword come identificatore produce un errore sintattico:

```python
for = 5  # SyntaxError
```

---

## 3. Elenco delle Keywords in Python

Python definisce **35 keywords standard** (il numero può variare leggermente tra versioni). È possibile ottenere la lista aggiornata direttamente dall’interprete:

```python
import keyword
keyword.kwlist
```

Questo approccio è preferibile rispetto alla memorizzazione manuale, perché garantisce coerenza con la versione di Python in uso.

---

## 4. Categorie concettuali delle Keywords

### 4.1 Valori speciali

* `True`, `False`
* `None`

Queste parole rappresentano **singleton**: esiste una sola istanza di ciascun valore in tutto il programma.

---

### 4.2 Operatori logici e di appartenenza

* `and`, `or`, `not`
* `in`, `is`

Queste keywords operano su espressioni booleane o relazioni tra oggetti. Esempio:

```python
x is None
x in lista
```

---

### 4.3 Controllo di flusso

* `if`, `elif`, `else`
* `for`, `while`
* `break`, `continue`, `return`, `yield`

Queste keywords determinano **l’ordine di esecuzione** del codice.

`yield`, in particolare, introduce il concetto di *generator*, fondamentale per la programmazione lazy.

---

### 4.4 Definizione di strutture

* `def`, `class`
* `lambda`
* `with`, `as`, `pass`

Consentono di definire nuove entità astratte e strutturare il codice in modo modulare.

---

### 4.5 Namespace e importazione

* `import`, `from`
* `global`, `nonlocal`

Queste keywords regolano la **visibilità delle variabili** e l’accesso ai moduli.

---

### 4.6 Gestione delle eccezioni

* `try`, `except`, `finally`
* `raise`, `assert`

Consentono di gestire errori in modo controllato, separando la logica principale dalla gestione delle anomalie.

---

### 4.7 Programmazione asincrona

* `async`, `await`

Introducono il modello asincrono basato su coroutine, fondamentale per applicazioni I/O‑bound moderne.

---

## 5. Soft Keywords

Alcune parole, come `match`, `case`, `_` e `type`, sono **soft keywords**: sono riservate solo in contesti sintattici specifici.

Esempio:

```python
match x:
    case 1:
        print("uno")
```

Fuori da questo contesto, possono essere usate come normali identificatori.

---

## 6. Keywords vs Built‑ins

È importante distinguere tra:

* **Keywords**: parte della grammatica (non ridefinibili)
* **Built‑ins**: funzioni e tipi predefiniti (`print`, `len`, `list`), che tecnicamente possono essere sovrascritti

Questa distinzione è cruciale per comprendere la struttura del linguaggio.

---

## 7. Riconoscere una Keyword

* Gli editor evidenziano le keywords con colori dedicati
* L’uso improprio genera `SyntaxError`
* Il modulo `keyword` fornisce strumenti di verifica

```python
import keyword
keyword.iskeyword("for")   # True
keyword.iskeyword("print") # False
```