# Shadowing delle funzioni *built‑in* in Python

## 1. Introduzione

In Python, il termine **shadowing** indica una situazione in cui un nome definito dall’utente (variabile, funzione, parametro, modulo) **nasconde** un nome già esistente e predefinito dal linguaggio. Quando questo accade con le **funzioni o tipi built‑in**, si parla di *shadowing dei built‑ins*. Questo fenomeno non genera necessariamente un errore di sintassi, ma può introdurre **bug sottili**, perdita di funzionalità del linguaggio e codice difficile da comprendere o manutenere.

---

## 2. Cosa sono i built‑ins in Python

Python mette a disposizione un insieme di **funzioni, tipi e oggetti predefiniti**, accessibili senza alcuna importazione. Essi risiedono nel namespace speciale `builtins`.

Esempi comuni:

* Funzioni: `print`, `len`, `sum`, `max`, `min`
* Tipi: `int`, `float`, `list`, `dict`, `str`
* Costrutti utili: `range`, `enumerate`, `zip`

Questi nomi sono pensati per essere **sempre disponibili** e rappresentano un contratto implicito tra il linguaggio e il programmatore.

---

## 3. Cos’è lo shadowing

Si parla di shadowing quando un nome definito in un certo scope **sovrascrive l’accesso** a un nome con lo stesso identificatore presente in uno scope più esterno. Esempio semplice:

```python
list = [1, 2, 3]
```

Dopo questa istruzione, `list` **non è più il tipo built‑in**, ma una variabile che fa riferimento a una lista.

```python
list("abc")  # TypeError
```

Il built‑in `list()` non è più accessibile tramite il nome `list`.

---

## 4. Shadowing e modello dei namespace (LEGB)

Per comprendere davvero il fenomeno dello *shadowing* è necessario introdurre il **modello di risoluzione dei nomi** adottato da Python. Quando l’interprete incontra un identificatore (ad esempio una variabile o una funzione), deve stabilire *a quale oggetto* quel nome faccia riferimento. Questo processo segue una regola ben definita, nota come **LEGB rule**.

L’acronimo **LEGB** indica l’ordine con cui Python cerca un nome:

1. **Local (L)** – lo scope locale della funzione corrente
2. **Enclosing (E)** – gli scope delle eventuali funzioni esterne (nel caso di funzioni annidate)
3. **Global (G)** – il namespace del modulo corrente
4. **Built-in (B)** – il namespace globale `builtins`, che contiene funzioni e tipi predefiniti

La ricerca avviene **in modo sequenziale e si arresta al primo match**. Questo significa che, se un nome viene trovato in uno scope più interno, Python **non prosegue la ricerca** negli scope successivi.

### 4.1 Un esempio concettuale

Consideriamo il seguente codice:

```python
x = 10

def f():
    x = 5
    print(x)

f()
```

Quando `print(x)` viene eseguito:

* Python cerca `x` nello scope **local** della funzione `f`
* lo trova (`x = 5`)
* si ferma, ignorando `x = 10` nello scope globale

Questo è un comportamento normale e desiderato. Lo *shadowing* nasce quando lo stesso meccanismo coinvolge i **built-ins**.

### 4.2 Shadowing dei built-ins tramite LEGB

Supponiamo di scrivere:

```python
len = 42
```

Ora il nome `len` esiste nello scope globale del modulo. Quando Python incontra:

```python
len([1, 2, 3])
```

il processo è il seguente:

1. Local: nessun `len`
2. Enclosing: nessun `len`
3. Global: `len = 42` → *match trovato*
4. Built-in: **non raggiunto**

Il risultato è un errore a runtime, perché `42` non è chiamabile. Il built-in `len()` esiste ancora, ma è **irraggiungibile tramite il suo nome usuale**.

### 4.3 Shadowing locale vs globale

Lo shadowing può avvenire a diversi livelli:

```python
sum = 0  # shadowing globale del built-in sum

def f():
    sum = 10  # shadowing locale
    return sum
```

In questo esempio:

* all’interno di `f`, `sum` è una variabile locale
* all’esterno, `sum` è una variabile globale
* in nessuno dei due casi il built-in `sum()` è accessibile tramite il nome `sum`

Questo mostra come lo shadowing possa essere **limitato a uno scope** o propagarsi a tutto il modulo.

### 4.4 Perché il built-in è l’ultimo anello

Il namespace `builtins` è deliberatamente posto **alla fine della catena di ricerca**. Questo consente:

* flessibilità del linguaggio
* possibilità di overriding controllato (ad esempio nei test)

Ma comporta anche una responsabilità per il programmatore: evitare collisioni involontarie con i nomi fondamentali del linguaggio. In altre parole, i built-ins non sono protetti da errori logici: Python **si fida** delle scelte di naming dello sviluppatore.

---

## 5. Esempi tipici di shadowing dei built‑ins

### 5.1 Variabili

```python
sum = 0
for x in data:
    sum += x
```

In questo punto del codice, la funzione `sum()` non è più utilizzabile.

---

### 5.2 Parametri di funzione

```python
def media(list):
    return sum(list) / len(list)
```

Il parametro `list` oscura il tipo built‑in `list` **solo all’interno della funzione**, ma ciò può comunque generare confusione concettuale.

---

### 5.3 Import impropri

```python
from math import *
```

Questo tipo di import può introdurre nomi che sovrascrivono funzioni esistenti, rendendo il namespace ambiguo.

---

## 6. Perché lo shadowing è pericoloso

* **Riduce la leggibilità** del codice
* **Rompe aspettative implicite** del lettore
* Introduce **bug difficili da diagnosticare**
* Complica il debugging e il refactoring
* Rende il codice meno portabile e meno robusto

In contesti collaborativi o scientifici, questi effetti sono particolarmente critici.

---

## 7. Best practices per evitare lo shadowing

### 7.1 Evitare nomi di built‑ins

Preferire nomi descrittivi:

* `total` invece di `sum`
* `items` invece di `list`
* `mapping` invece di `dict`

---

### 7.2 Usare convenzioni di naming chiare

* Nomi di variabili: sostantivi descrittivi
* Funzioni: verbi o azioni
* Evitare nomi troppo generici

---

### 7.3 Controllare il namespace `builtins`

È possibile ispezionare esplicitamente i built‑ins:

```python
import builtins
dir(builtins)
```

Questo aiuta a evitare collisioni involontarie.

---

### 7.4 Affidarsi ai linter

Strumenti come **pylint**, **flake8** o **ruff** segnalano automaticamente lo shadowing dei built‑ins come *code smell*.

---

### 7.5 Ripristinare un built‑in (caso limite)

Se necessario, è possibile recuperare un built‑in esplicitamente:

```python
import builtins
builtins.list("abc")
```

Questa soluzione è didattica o di emergenza, **non una buona pratica ordinaria**.

---

## 8. Shadowing intenzionale e casi avanzati

In rari casi, lo shadowing può essere usato consapevolmente (ad esempio in test o mocking). Tuttavia, deve essere:

* Esplicito
* Localizzato
* Ben documentato

Nel codice di produzione, è generalmente sconsigliato.