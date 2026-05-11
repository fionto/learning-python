# Generatori: Sequenze che Non Esistono Tutte in una Volta

## Il Problema della Lista che Pesa Troppo

Considerate questa situazione: dovete elaborare i numeri da uno a un milione, applicare
un'operazione a ciascuno, e raccogliere i risultati. L'approccio immediato è costruire
una lista:

```python
# Approccio diretto: tutti i numeri in memoria contemporaneamente
numeri = [i * 2 for i in range(1_000_000)]
primo = numeri[0]
```

Il codice funziona, ma crea in memoria un milione di interi prima ancora di iniziare
l'elaborazione. Se il dato è grande — file di log, sequenze genomiche, stream di
transazioni — questa strategia diventa rapidamente impraticabile.

Il problema non è l'elaborazione in sé, ma il fatto di materializzare l'intera sequenza
prima di utilizzarla. In molti casi reali, ci serve un elemento per volta: lo elaboriamo,
lo scartiamo, e passiamo al successivo. Non abbiamo bisogno di tutti i valori simultaneamente.

I **generatori** nascono esattamente per questa situazione: sono oggetti che producono
valori uno alla volta, su richiesta, senza mai costruire la sequenza completa in memoria.

---

## La Parola Chiave `yield`

La differenza tra una funzione normale e una funzione generatrice è una sola parola:
`yield` al posto di `return`.

```python
# Funzione normale: calcola tutto e restituisce
def quadrati_lista(n: int) -> list[int]:
    risultati = []
    for i in range(n):
        risultati.append(i ** 2)
    return risultati  # restituisce l'intera lista

# Funzione generatrice: produce un valore per volta
def quadrati_gen(n: int):
    for i in range(n):
        yield i ** 2  # "emette" un valore e si sospende
```

Chiamare `quadrati_gen(5)` non esegue nulla del corpo della funzione. Restituisce un
**oggetto generatore**, una specie di macchina in attesa. La macchina si mette in moto
solo quando qualcuno richiede il prossimo valore, tipicamente con un ciclo `for` o con
la funzione built-in `next()`.

```python
gen = quadrati_gen(5)

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4
# ... e così via fino all'esaurimento
```

Ogni chiamata a `next()` riprende l'esecuzione dal punto in cui si era fermata (subito
dopo l'ultimo `yield`), produce il valore successivo, e si sospende di nuovo. Quando
la funzione termina senza più `yield` da eseguire, il generatore solleva
`StopIteration`, che un ciclo `for` cattura silenziosamente come segnale di fine.

```python
# Il ciclo for gestisce StopIteration in automatico
for valore in quadrati_gen(5):
    print(valore)

# Output:
# 0
# 1
# 4
# 9
# 16
```

---

## Come lo Stato Viene Preservato

Il comportamento di sospensione e ripresa è il cuore concettuale dei generatori. Quando
una funzione normale termina, il suo stato locale scompare. Quando un generatore esegue
`yield`, il suo stato locale viene **congelato**: le variabili locali, il punto di
esecuzione, persino i valori nei cicli interni rimangono intatti fino alla prossima
richiesta.

```python
def contatore_con_log(limite: int):
    """Generatore che mostra esplicitamente i momenti di sospensione."""
    i = 0
    while i < limite:
        print(f"  [generatore] sto per emettere {i}")
        yield i
        print(f"  [generatore] sono tornato, incremento da {i}")
        i += 1
    print("  [generatore] terminato")

print("Inizio iterazione")
for valore in contatore_con_log(3):
    print(f"Ho ricevuto: {valore}")

# Output:
# Inizio iterazione
#   [generatore] sto per emettere 0
# Ho ricevuto: 0
#   [generatore] sono tornato, incremento da 0
#   [generatore] sto per emettere 1
# Ho ricevuto: 1
#   [generatore] sono tornato, incremento da 1
#   [generatore] sto per emettere 2
# Ho ricevuto: 2
#   [generatore] sono tornato, incremento da 2
#   [generatore] terminato
```

Il dialogo tra generatore e ciclo `for` è un'alternanza precisa: il generatore emette,
il ciclo consuma, il generatore riprende. Non c'è sovrapposizione, non c'è accumulo.

---

## Il Vantaggio sulla Memoria

Per quantificare la differenza, Python offre il modulo `sys` con la funzione `getsizeof()`,
che restituisce la dimensione in byte di un oggetto in memoria.

```python
import sys

# Lista: contiene tutti gli elementi
lista = [i * 2 for i in range(100_000)]
print(f"Lista: {sys.getsizeof(lista):,} byte")  # Output: Lista: 800,056 byte

# Generatore: contiene solo lo stato della funzione
gen = (i * 2 for i in range(100_000))  # notare le parentesi tonde
print(f"Generatore: {sys.getsizeof(gen):,} byte")  # Output: Generatore: 208 byte
```

La lista occupa circa 800 KB; il generatore equivalente occupa 208 byte indipendentemente
da quanti elementi produrrà. Questo non è un trucco: il generatore non ha ancora prodotto
nulla. Produrrà ogni elemento solo quando richiesto, e lo scarta subito dopo.

La seconda riga introduce la **generator expression**: la sintassi con le parentesi tonde
è l'equivalente in linea di una funzione generatrice, esattamente come la list
comprehension è l'equivalente in linea di un ciclo che costruisce una lista.

```python
# List comprehension: costruisce la lista intera
quadrati_lista = [x**2 for x in range(10)]

# Generator expression: produce un valore per volta
quadrati_gen = (x**2 for x in range(10))

# Entrambi si iterano allo stesso modo
for q in quadrati_gen:
    print(q)
```

Le generator expression sono particolarmente comode quando il generatore è un argomento
di una funzione che già accetta un iterabile:

```python
# sum() accetta qualsiasi iterabile: non serve costruire la lista
totale = sum(x**2 for x in range(1_000_000))
```

---

## Sequenze Potenzialmente Infinite

Un caso d'uso che le liste non possono nemmeno approcciare è la generazione di sequenze
senza fine definita. Un generatore può produrre valori indefinitamente, e sarà il
codice chiamante a decidere quando fermarsi.

```python
def numeri_pari():
    """Genera tutti i numeri pari, senza limite."""
    n = 0
    while True:  # ciclo infinito: intenzionale
        yield n
        n += 2

# Prendere solo i primi 5
gen = numeri_pari()
primi_cinque = [next(gen) for _ in range(5)]
print(primi_cinque)  # Output: [0, 2, 4, 6, 8]
```

Oppure, usando `itertools.islice` dalla libreria standard per estrarre una fetta da un
generatore infinito senza dover gestire manualmente `next()`:

```python
import itertools

gen = numeri_pari()
print(list(itertools.islice(gen, 5)))  # Output: [0, 2, 4, 6, 8]
```

Questa capacità è utile non solo per sequenze matematiche, ma per qualsiasi sorgente
dati che produce elementi in modo continuo: lettura riga per riga di un file molto
grande, polling di un'API, ascolto di eventi in una coda.

---

## Una Nota Critica: il Generatore è Usa e Getta

Il comportamento più sorprendente per chi usa i generatori per la prima volta è questo:
**un generatore può essere iterato una volta sola**. Dopo che ha emesso l'ultimo valore,
è esaurito, e qualsiasi tentativo di iterarlo di nuovo produce semplicemente niente.

```python
gen = quadrati_gen(5)

# Prima iterazione: funziona
print(list(gen))  # Output: [0, 1, 4, 9, 16]

# Seconda iterazione: il generatore è esaurito
print(list(gen))  # Output: []
```

Questo non è un bug né un difetto: è una conseguenza diretta del fatto che il generatore
non ricorda i valori già emessi. Una volta che lo stato interno ha raggiunto la fine,
non c'è modo di tornare indietro senza creare un nuovo oggetto generatore.

La trappola più comune è passare un generatore a più funzioni aspettandosi che ognuna
lo veda dall'inizio:

```python
gen = (x**2 for x in range(5))

prima_meta = list(itertools.islice(gen, 3))  # consuma i primi 3: [0, 1, 4]
tutto = list(gen)  # il generatore riprende da dove si era fermato: [9, 16]

# Non si ottiene [0, 1, 4, 9, 16] la seconda volta,
# perché gen è lo stesso oggetto, non una copia.
```

Se serve iterare la sequenza più volte, la soluzione è creare una funzione generatrice
e chiamarla ogni volta che serve un iteratore fresco, oppure convertire i risultati in
una lista quando le dimensioni lo permettono.

---

## Dove i Generatori Appaiono nel Codice Reale

I generatori non sono uno strumento di nicchia: Python stesso li usa pervasivamente.
La funzione built-in `range()` è tecnicamente un iterabile pigro (non un generatore
nel senso stretto, ma produce valori su richiesta). Le funzioni `map()`, `filter()`, e
`zip()` restituiscono oggetti iteratori. Aprire un file con `open()` e iterare sulle
righe funziona riga per riga senza caricare il file in memoria.

Imparare a riconoscere questo pattern — "produco un valore per volta invece di costruire
tutto in anticipo" — cambia il modo in cui si affronta qualsiasi problema che coinvolge
sequenze di dati. Non sempre un generatore è la scelta migliore: se la sequenza è
piccola e serve accedervi più volte, una lista è più semplice e diretta. Ma quando
i dati sono grandi, potenzialmente infiniti, o provengono da una sorgente esterna, il
generatore è spesso lo strumento naturale.

Un passo successivo naturale è esplorare il modulo `itertools` della libreria standard,
che offre una collezione di generatori e strumenti per combinarli: `chain()` per
concatenare iterabili, `takewhile()` per fermarsi a una condizione, `groupby()` per
raggruppare elementi consecutivi. Sono tutti costruiti sullo stesso principio pigro che
rende i generatori potenti.
