# Capitolo 4: Sezione 4.1 - Funzioni: Definire, Invocare e Comporre Comportamenti Riutilizzabili

## Introduzione: Il Ricettario del Programmatore

Immaginate di avere un ricettario. Ogni ricetta ha un nome, richiede certi ingredienti e descrive una serie di passi da seguire. Quando volete preparare la pasta al pomodoro, non riscrivete la ricetta ogni volta: andate alla pagina giusta, leggete, eseguite. Il risultato è lo stesso ogni volta che la seguite fedelmente.

In programmazione, le **funzioni** sono esattamente questo: ricette con un nome. Raccolgono una serie di istruzioni sotto un'unica etichetta, e quella etichetta può essere "invocata" (cioè eseguita) ogni volta che ne avete bisogno, senza dover riscrivere le stesse istruzioni da capo. Questa capacità di nominare e riutilizzare il codice è una delle idee più potenti dell'informatica moderna.

Fino a questo momento, i vostri programmi hanno avuto una struttura lineare: una lunga sequenza di istruzioni, dall'inizio alla fine. Con le funzioni, potete cominciare a organizzare il codice in blocchi logici separati, ognuno con uno scopo preciso. Un blocco calcola il totale di un acquisto, un altro verifica la password dell'utente, un terzo formatta un indirizzo. Questa separazione rende i programmi più leggibili, più facili da correggere e più semplici da estendere nel tempo.

In questa dispensa costruiremo la comprensione delle funzioni partendo da zero: come si dichiarano, come si invocano, come comunicano il loro risultato al resto del programma attraverso `return`, cosa significa il valore speciale `None`, e infine come una funzione può persino chiamare sé stessa, aprendo la porta a un paradigma elegante e potente chiamato ricorsione.

---

## Definire una Funzione: La Parola Chiave `def`

In Python, per creare una funzione si usa la parola chiave `def`, seguita dal nome che vogliamo assegnare alla funzione, una coppia di parentesi tonde e i due punti. Il corpo della funzione, cioè le istruzioni che la compongono, va scritto nel blocco indentato che segue.

```python
# Definizione di una funzione semplice
def saluta():
    print("Ciao, benvenuto nel programma!")
```

Fin qui, non è successo nulla di visibile: abbiamo solo descritto la ricetta, non l'abbiamo ancora eseguita. Python legge la definizione, la memorizza con il nome `saluta`, e aspetta. Questo è un punto fondamentale che confonde molti studenti all'inizio: **definire una funzione non la esegue**.

Per eseguirla, dobbiamo invocarla, cioè scrivere il suo nome seguito dalle parentesi tonde:

```python
# Definizione
def saluta():
    print("Ciao, benvenuto nel programma!")

# Invocazione: qui la funzione viene eseguita
saluta()
# Output: Ciao, benvenuto nel programma!
```

Le parentesi sono obbligatorie anche quando la funzione non riceve nessun dato in ingresso. Scrivere solo `saluta` senza parentesi non esegue nulla: in Python, quel nome senza parentesi si riferisce all'oggetto-funzione stesso, non alla sua esecuzione.

Una funzione può essere invocata quante volte si vuole, e ogni volta esegue le stesse istruzioni dall'inizio:

```python
def saluta():
    print("Ciao, benvenuto nel programma!")

saluta()
saluta()
saluta()
# Output:
# Ciao, benvenuto nel programma!
# Ciao, benvenuto nel programma!
# Ciao, benvenuto nel programma!
```

Tre invocazioni, tre esecuzioni. La funzione è come quel bottone nella lavastoviglie: ogni volta che lo premete, parte lo stesso ciclo.

---

## Comunicare con la Funzione: Parametri e Argomenti

Una funzione senza input è utile, ma una funzione che lavora su dati passati dall'esterno è molto più versatile. I **parametri** sono i nomi che usiamo nella definizione della funzione per indicare che questa si aspetta dei dati; gli **argomenti** sono i valori concreti che passiamo quando la invochiamo.

```python
# "nome" è un parametro
def saluta_persona(nome):
    print("Ciao,", nome)

# "Matteo" è l'argomento
saluta_persona("Matteo")
# Output: Ciao, Matteo

saluta_persona("Laura")
# Output: Ciao, Laura
```

La funzione è la stessa, ma il comportamento cambia in base ai dati ricevuti. Questo è il cuore dell'astrazione: una ricetta che funziona con qualsiasi ingrediente del tipo giusto.

I parametri e gli argomenti saranno approfonditi nella sezione 4.2. Per ora, è sufficiente sapere che esistono e che la loro presenza trasforma una funzione da uno script fisso a uno strumento flessibile.

---

## Restituire un Risultato: L'Istruzione `return`

Fin qui, le funzioni hanno prodotto output stampando qualcosa a schermo. Ma molto spesso le funzioni non devono mostrare nulla: devono **calcolare** qualcosa e consegnare il risultato al codice che le ha chiamate, in modo che quel risultato possa essere usato ulteriormente.

Pensiamo a una calcolatrice. Quando premete il tasto `=`, la calcolatrice non si limita a scrivere il risultato su un foglio di carta e buttarlo via: ve lo mostra affinché possiate usarlo nel calcolo successivo. La parola chiave `return` fa esattamente questo: consegna un valore dalla funzione al chiamante.

```python
# Funzione che somma due numeri e restituisce il risultato
def somma(a, b):
    risultato = a + b
    return risultato

# Il valore restituito viene assegnato a una variabile
totale = somma(3, 5)
print(totale)
# Output: 8
```

Il valore che segue `return` viene "consegnato" al punto del programma dove la funzione è stata invocata. In questo caso, `somma(3, 5)` vale `8`, e quel valore viene assegnato alla variabile `totale`.

Questo significa che possiamo usare la chiamata a una funzione ovunque potremmo usare un valore letterale:

```python
def quadrato(n):
    return n * n

# Usare il risultato direttamente in un'espressione
print(quadrato(4) + quadrato(3))
# Output: 25

# Oppure come condizione
if quadrato(5) > 20:
    print("Il quadrato è maggiore di 20")
# Output: Il quadrato è maggiore di 20
```

È importante capire che `return` interrompe immediatamente l'esecuzione della funzione. Qualsiasi istruzione scritta dopo un `return` non verrà mai eseguita:

```python
def esempio():
    print("Prima istruzione")
    return 42
    print("Questa riga non verrà mai eseguita")

valore = esempio()
print(valore)
# Output:
# Prima istruzione
# 42
```

Una funzione può avere più istruzioni `return` in percorsi diversi, ad esempio all'interno di blocchi `if-else`. L'esecuzione si ferma al primo `return` incontrato:

```python
def valore_assoluto(n):
    if n >= 0:
        return n
    else:
        return -n

print(valore_assoluto(7))    # Output: 7
print(valore_assoluto(-3))   # Output: 3
```

---

## Il Valore Speciale `None`

Cosa succede quando una funzione non ha un'istruzione `return`, oppure ha un `return` senza nessun valore dopo? In Python, la funzione restituisce automaticamente un valore speciale chiamato `None`.

`None` è un tipo di dato a sé stante in Python (di tipo `NoneType`). Rappresenta l'assenza di valore, un po' come lo zero di un conto bancario vuoto, ma per i dati: non è né zero, né stringa vuota, né `False`. È proprio "niente".

```python
def funzione_senza_return():
    x = 10 + 5  # Fa un calcolo, ma non restituisce nulla

risultato = funzione_senza_return()
print(risultato)
# Output: None

print(type(risultato))
# Output: <class 'NoneType'>
```

Questo vale anche per un `return` esplicito senza valore:

```python
def funzione_con_return_vuoto():
    print("Eseguo qualcosa")
    return

risultato = funzione_con_return_vuoto()
# Output: Eseguo qualcosa

print(risultato)
# Output: None
```

Il `return` senza valore viene usato quando vogliamo uscire anticipatamente dalla funzione senza restituire dati. È un modo per interrompere l'esecuzione in un certo punto, come un'uscita d'emergenza.

Occorre fare attenzione quando si cerca di usare il valore di ritorno di una funzione che non restituisce nulla. Un errore comune è questo:

```python
def stampa_doppio(n):
    print(n * 2)  # Stampa, ma non restituisce

valore = stampa_doppio(5)
# Output: 10

# Attenzione: valore è None, non 10!
print(valore + 1)
# Errore: TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

La funzione ha stampato `10`, ma non ha consegnato `10` al chiamante. Il valore effettivo di `stampa_doppio(5)` è `None`. Se volete usare il risultato nel programma, usate `return`, non `print`.

---

## Ricorsione: Quando una Funzione Chiama Sé Stessa

Arriviamo a uno dei concetti più eleganti e affascinanti della programmazione: la **ricorsione**. Una funzione ricorsiva è una funzione che, nel proprio corpo, invoca sé stessa.

Può sembrare strano all'inizio. Come può una funzione chiamare sé stessa? Non si creerebbe un loop infinito? La risposta sta nel **caso base**: ogni funzione ricorsiva ben scritta ha una condizione che ferma la ricorsione, restituendo un valore direttamente senza fare un'altra chiamata ricorsiva.

Il modo migliore per capire la ricorsione è con un esempio classico: il **fattoriale**. Il fattoriale di un numero intero positivo `n`, scritto `n!`, è definito come il prodotto di tutti i numeri interi da 1 fino a `n`:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Ma c'è un'altra definizione, matematicamente equivalente e più adatta alla ricorsione:

```
n! = n × (n-1)!
1! = 1             ← caso base
```

In altre parole: il fattoriale di `n` è `n` moltiplicato per il fattoriale di `n-1`. Il fattoriale di `1` è semplicemente `1` (e questo interrompe la catena).

Tradotto in Python:

```python
def fattoriale(n):
    # Caso base: il fattoriale di 1 è 1
    if n == 1:
        return 1
    # Caso ricorsivo: n! = n × (n-1)!
    else:
        return n * fattoriale(n - 1)

print(fattoriale(5))
# Output: 120

print(fattoriale(3))
# Output: 6
```

Per capire cosa succede davvero quando chiamiamo `fattoriale(5)`, è utile tracciare l'esecuzione passo dopo passo. Python inizia a "scendere" verso il caso base:

```
fattoriale(5) → 5 × fattoriale(4)
fattoriale(4) → 4 × fattoriale(3)
fattoriale(3) → 3 × fattoriale(2)
fattoriale(2) → 2 × fattoriale(1)
fattoriale(1) → 1   ← caso base raggiunto, nessuna altra chiamata
```

Poi i risultati "risalgono" la catena, uno dopo l'altro:

```
fattoriale(1) = 1
fattoriale(2) = 2 × 1 = 2
fattoriale(3) = 3 × 2 = 6
fattoriale(4) = 4 × 6 = 24
fattoriale(5) = 5 × 24 = 120
```

Questo meccanismo di "discesa" verso il caso base e successiva "risalita" con i risultati è il cuore di ogni funzione ricorsiva.

### Il Caso Base: la Condizione Indispensabile

Cosa accade se dimenticate il caso base? Python continua a chiamare la funzione all'infinito, fino a esaurire la memoria riservata alle chiamate di funzione. A quel punto, Python si ferma con un errore chiamato `RecursionError`:

```python
# ATTENZIONE: questa funzione non ha caso base e causa un errore
def fattoriale_errato(n):
    return n * fattoriale_errato(n - 1)

# fattoriale_errato(5)
# RecursionError: maximum recursion depth exceeded
```

Python impone un limite al numero di chiamate ricorsive annidate (per default 1000) proprio per evitare che un programma mal scritto consumi tutta la memoria disponibile. Quando vedete un `RecursionError`, il primo controllo da fare è: "ho scritto un caso base corretto?"

### Un Secondo Esempio: Contare alla Rovescia

La ricorsione non si applica solo ai calcoli matematici. Ecco un esempio che mostra come si può pensare a un problema sequenziale in modo ricorsivo:

```python
def conto_alla_rovescia(n):
    # Caso base: quando arriviamo a 0, stampiamo "Via!" e ci fermiamo
    if n == 0:
        print("Via!")
        return
    # Caso ricorsivo: stampa il numero e poi conta dall'alto verso il basso
    print(n)
    conto_alla_rovescia(n - 1)

conto_alla_rovescia(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Via!
```

Notate come questa funzione non restituisce nulla di significativo (il `return` è vuoto, quindi vale `None`): il suo scopo è produrre un effetto collaterale (stampare a schermo), non calcolare un valore.

### Ricorsione vs. Iterazione

Qualsiasi problema risolvibile con la ricorsione può essere risolto anche con un ciclo (`for` o `while`), e viceversa. Per esempio, il fattoriale iterativo si scrive così:

```python
def fattoriale_iterativo(n):
    risultato = 1
    for i in range(1, n + 1):
        risultato *= i
    return risultato

print(fattoriale_iterativo(5))
# Output: 120
```

Le due versioni producono lo stesso risultato. La scelta tra ricorsione e iterazione dipende dalla natura del problema e dalla leggibilità del codice. Alcuni problemi (come la navigazione di strutture ad albero, i fractal, o certi algoritmi su grafi) si esprimono in modo naturale e conciso con la ricorsione. Per l'esame PCEP, è sufficiente saper riconoscere una funzione ricorsiva, identificarne il caso base, e prevedere cosa stampa o restituisce.

---

## Mettere Insieme i Pezzi: un Esempio Completo

Per consolidare tutti i concetti di questa sezione, vediamo un piccolo programma che usa definizione, invocazione, `return` e ricorsione in un contesto unitario:

```python
# Funzione che calcola la somma di tutti i numeri da 1 a n (ricorsiva)
def somma_fino_a(n):
    if n == 1:
        return 1                         # caso base
    return n + somma_fino_a(n - 1)       # caso ricorsivo

# Funzione che stampa un messaggio descrittivo
def descrivi_somma(n):
    totale = somma_fino_a(n)
    print("La somma da 1 a", n, "è:", totale)

# Programma principale
descrivi_somma(5)
# Output: La somma da 1 a 5 è: 15

descrivi_somma(10)
# Output: La somma da 1 a 10 è: 55
```

In questo esempio, `somma_fino_a` calcola e restituisce un valore numerico usando la ricorsione. `descrivi_somma` la invoca, cattura il risultato in `totale` e lo usa per costruire un messaggio da stampare. Le due funzioni collaborano, ognuna con il proprio ruolo preciso.

---

## Conclusione: Organizzare il Pensiero in Blocchi Riutilizzabili

In questa dispensa abbiamo costruito la comprensione delle funzioni partendo dalla loro definizione con `def` e dalla distinzione cruciale tra definire una funzione e invocarla. Abbiamo visto come `return` consenta a una funzione di comunicare un risultato al codice chiamante, e come `None` sia il valore implicito quando una funzione non restituisce nulla di esplicito.

Infine, abbiamo incontrato la ricorsione: un modo di risolvere problemi in cui una funzione delega una versione più piccola di sé stessa a sé stessa, affidandosi a un caso base per fermare la catena di chiamate.

Le funzioni sono il mattone fondamentale con cui si costruiscono i programmi reali. Tutto il codice che avete scritto finora, da `print()` a `range()`, da `len()` a `sorted()`, è implementato come funzione (o come qualcosa di molto simile). Ora sapete come creare i vostri strumenti personali, con il nome e il comportamento che volete.

Nella sezione 4.2 approfondiremo il rapporto tra funzioni e ambiente: come i dati fluiscono dentro e fuori attraverso parametri e argomenti, cosa significa che una variabile esiste "dentro" o "fuori" da una funzione, e come gestire i valori di default. È il passo che trasforma le funzioni da semplici ricette in veri moduli di codice riutilizzabile.
