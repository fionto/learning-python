# Iterazione Avanzata in Python: Strumenti per Cicli Espressivi

## Il Problema dei Cicli Verbosi

Chi comincia a scrivere codice Python porta spesso con sé il modo di pensare all'iterazione ereditato da altri linguaggi: un indice numerico che parte da zero, cresce a ogni passo, e serve da maniglia per accedere agli elementi di una sequenza. Il risultato è un ciclo come questo:

```python
misure = [23.4, 19.8, 31.2, 27.6]

for i in range(len(misure)):
    print(f"Campione {i}: {misure[i]} µm")

# Stampa:
# Campione 0: 23.4 µm
# Campione 1: 19.8 µm
# Campione 2: 31.2 µm
# Campione 3: 27.6 µm
```

Il codice funziona, ma porta con sé del rumore: `range(len(...))` è un costrutto che richiede di leggere dall'interno verso l'esterno, e l'accesso tramite indice `misure[i]` introduce un livello di indiretto che non aggiunge informazione. Il problema reale (stampare ogni elemento con la sua posizione) è sepolto sotto la meccanica del conteggio.

Python offre una collezione di strumenti della libreria standard, molti concentrati nel modulo `itertools`, che risolvono questi problemi in modo diretto ed espressivo. Non si tratta di scorciatoie superficiali: ciascuno di questi strumenti incarna una precisa astrazione sul concetto di iterazione, e riconoscerli nel codice altrui (e saperli usare nel proprio) è un tratto distintivo del codice Python maturo.

---

## `enumerate`: Iterare con Indice

La funzione `enumerate` risponde esattamente al problema dell'esempio iniziale. Prende un iterabile qualsiasi e restituisce coppie (indice, valore) per ogni elemento, senza richiedere all'utente di gestire il conteggio manualmente.

```python
misure = [23.4, 19.8, 31.2, 27.6]

for i, valore in enumerate(misure):
    print(f"Campione {i}: {valore} µm")

# Stampa:
# Campione 0: 23.4 µm
# Campione 1: 19.8 µm
# Campione 2: 31.2 µm
# Campione 3: 27.6 µm
```

Il ciclo diventa una dichiarazione: "per ogni indice e valore in questa sequenza, fai qualcosa". L'intenzione emerge direttamente dalla struttura del codice.

`enumerate` accetta un secondo argomento opzionale, `start`, che permette di far partire il conteggio da un valore diverso da zero. Questo è utile ogni volta che l'indice ha un significato per l'utente finale (il primo campione è il numero 1, non lo zero):

```python
etichette = ["alfa", "beta", "gamma"]

for n, etichetta in enumerate(etichette, start=1):
    print(f"Serie {n}: {etichetta}")

# Stampa:
# Serie 1: alfa
# Serie 2: beta
# Serie 3: gamma
```

---

## `zip`: Iterare su Più Sequenze in Parallelo

Se `enumerate` risolve il problema dell'indice, `zip` risolve quello dell'iterazione parallela: scorrere due o più sequenze contemporaneamente, associando gli elementi in corrispondenza di posizione.

Un caso tipico è la correlazione tra due liste di dati acquisiti in modo separato:

```python
temperature = [300, 350, 400, 450]
correnti = [0.12, 0.31, 0.58, 0.94]

for T, I in zip(temperature, correnti):
    print(f"T = {T} K → I = {I} A")

# Stampa:
# T = 300 K → I = 0.12 A
# T = 350 K → I = 0.31 A
# T = 400 K → I = 0.58 A
# T = 450 K → I = 0.94 A
```

Senza `zip`, si sarebbe ricorsi all'indice numerico; con `zip`, la struttura del ciclo comunica direttamente la relazione tra i due insiemi di dati.

`zip` può combinare più di due sequenze contemporaneamente:

```python
campioni = ["A1", "A2", "A3"]
rugosita = [0.34, 0.41, 0.29]
spessori = [120, 115, 130]

for nome, Ra, d in zip(campioni, rugosita, spessori):
    print(f"{nome}: Ra = {Ra} nm, spessore = {d} nm")

# Stampa:
# A1: Ra = 0.34 nm, spessore = 120 nm
# A2: Ra = 0.41 nm, spessore = 115 nm
# A3: Ra = 0.29 nm, spessore = 130 nm
```

`zip` e `enumerate` si combinano naturalmente quando serve sia l'indice che la correlazione parallela:

```python
etichette = ["bassa", "media", "alta"]
potenze = [0.5, 1.0, 1.5]

for i, (label, P) in enumerate(zip(etichette, potenze), start=1):
    print(f"Misura {i} ({label} potenza): {P} W")

# Stampa:
# Misura 1 (bassa potenza): 0.5 W
# Misura 2 (media potenza): 1.0 W
# Misura 3 (alta potenza): 1.5 W
```

---

## `zip` con Sequenze di Lunghezza Diversa: `zip_longest`

Il comportamento predefinito di `zip` è conservativo: si ferma quando la sequenza più corta è esaurita. Se le due sequenze hanno lunghezze diverse, gli elementi in eccesso vengono silenziosamente ignorati.

```python
nomi = ["alfa", "beta", "gamma", "delta"]
valori = [10, 20]

for n, v in zip(nomi, valori):
    print(n, v)

# Stampa solo:
# alfa 10
# beta 20
# ("gamma" e "delta" vengono ignorati)
```

Quando invece si vuole preservare tutti gli elementi, riempiendo con un valore sentinella le posizioni mancanti, si usa `itertools.zip_longest`:

```python
from itertools import zip_longest

nomi = ["alfa", "beta", "gamma", "delta"]
valori = [10, 20]

for n, v in zip_longest(nomi, valori, fillvalue=None):
    print(n, v)

# Stampa:
# alfa 10
# beta 20
# gamma None
# delta None
```

Il parametro `fillvalue` accetta qualsiasi oggetto Python: `0`, `"N/A"`, `float("nan")`. La scelta dipende dal contesto e da come i dati mancanti devono essere trattati a valle.

---

## `reversed`: Invertire l'Ordine di Iterazione

`reversed` restituisce un iteratore che percorre una sequenza dall'ultimo elemento al primo. A differenza di `list[::-1]`, che crea una nuova lista in memoria, `reversed` è pigro: genera i valori uno alla volta senza copiare nulla.

```python
fasi = ["deposizione", "ricottura", "ossidazione", "misura"]

for fase in reversed(fasi):
    print(fase)

# Stampa:
# misura
# ossidazione
# ricottura
# deposizione
```

`reversed` funziona con qualsiasi sequenza che supporta l'accesso per indice e la funzione `len` (liste, tuple, stringhe, oggetti personalizzati con `__reversed__` o `__len__` e `__getitem__`). Non funziona su iteratori generici o su dizionari nelle versioni di Python precedenti alla 3.8.

Per i dizionari, a partire da Python 3.8, `reversed` è applicabile alle viste `.keys()`, `.values()` e `.items()`:

```python
parametri = {"fluenza": 2.5, "ripetizione": 100, "lunghezza_d_onda": 1030}

for chiave in reversed(parametri):
    print(chiave)

# Stampa:
# lunghezza_d_onda
# ripetizione
# fluenza
```

---

## `sorted` e `sort`: Ordinare Durante l'Iterazione

Spesso si vuole iterare su una sequenza non nell'ordine in cui è memorizzata, ma in un ordine significativo. `sorted` restituisce una nuova lista ordinata, lasciando intatta la sequenza originale. Il metodo `.sort()`, invece, ordina la lista sul posto.

```python
misure_disordinate = [31.2, 19.8, 27.6, 23.4]

# sorted produce una nuova lista; la originale non cambia
for v in sorted(misure_disordinate):
    print(v)

# Stampa: 19.8, 23.4, 27.6, 31.2
```

Entrambi accettano due argomenti opzionali fondamentali. Il primo è `reverse=True`, che inverte l'ordine dell'ordinamento. Il secondo è `key`, una funzione applicata a ogni elemento prima del confronto: l'ordinamento avviene sul risultato di quella funzione, non sull'elemento diretto.

```python
campioni = [("A3", 0.29), ("A1", 0.34), ("A2", 0.41)]

# Ordina per rugosità (secondo elemento della tupla)
for nome, Ra in sorted(campioni, key=lambda x: x[1]):
    print(f"{nome}: {Ra} nm")

# Stampa:
# A3: 0.29 nm
# A1: 0.34 nm
# A2: 0.41 nm
```

L'argomento `key` è uno dei meccanismi più versatili di Python per personalizzare l'ordinamento senza modificare i dati. Qualsiasi funzione con un parametro e un valore di ritorno può fungere da chiave: una funzione lambda, una funzione definita con `def`, o persino un metodo come `str.lower` per ordinare stringhe in modo case-insensitive.

---

## `itertools.chain`: Concatenare Sequenze

`itertools.chain` permette di iterare su più sequenze come se fossero una sola, senza crearle fisicamente in memoria. È utile ogni volta che si hanno dati distribuiti su più collezioni e si vuole processarli con un unico ciclo.

```python
from itertools import chain

serie_1 = [10, 20, 30]
serie_2 = [40, 50]
serie_3 = [60, 70, 80, 90]

for valore in chain(serie_1, serie_2, serie_3):
    print(valore, end=" ")

# Stampa: 10 20 30 40 50 60 70 80 90
```

La variante `chain.from_iterable` accetta un singolo iterabile di iterabili, utile quando il numero di sequenze da concatenare non è noto a priori:

```python
from itertools import chain

gruppi = [[1, 2], [3, 4], [5, 6]]

for valore in chain.from_iterable(gruppi):
    print(valore, end=" ")

# Stampa: 1 2 3 4 5 6
```

---

## `itertools.islice`: Tagliare un Iteratore

`itertools.islice` è l'equivalente dello slicing (`[start:stop:step]`) per gli iteratori generici. Gli iteratori non supportano lo slicing diretto, perché non conoscono la propria lunghezza; `islice` aggira questo limite consumando l'iteratore fino alla posizione desiderata.

```python
from itertools import islice

def genera_misure():
    """Generatore che produce misure simulate all'infinito."""
    import random
    while True:
        yield round(random.uniform(20.0, 35.0), 2)

# Prende solo le prime 5 misure dal generatore infinito
for misura in islice(genera_misure(), 5):
    print(misura)

# Stampa (valori casuali, es.):
# 27.34
# 22.11
# 33.90
# 24.56
# 29.03
```

`islice` accetta fino a tre argomenti: `islice(iterabile, stop)` oppure `islice(iterabile, start, stop)` oppure `islice(iterabile, start, stop, step)`. La semantica è identica a quella dello slicing sulle liste.

---

## `itertools.groupby`: Raggruppare Elementi Contigui

`groupby` raggruppa elementi consecutivi di un iterabile che condividono lo stesso valore di una chiave. È l'analogo dell'operazione `GROUP BY` del linguaggio SQL, con una differenza cruciale: lavora solo su elementi contigui, non sull'intera sequenza. Perché il raggruppamento sia completo, la sequenza deve essere ordinata per la stessa chiave prima di passarla a `groupby`.

```python
from itertools import groupby

risultati = [
    {"campione": "A", "esito": "ok"},
    {"campione": "B", "esito": "ok"},
    {"campione": "C", "esito": "errore"},
    {"campione": "D", "esito": "errore"},
    {"campione": "E", "esito": "ok"},
]

# Ordiniamo prima per esito, poi raggruppiamo
dati_ordinati = sorted(risultati, key=lambda r: r["esito"])

for esito, gruppo in groupby(dati_ordinati, key=lambda r: r["esito"]):
    campioni = [r["campione"] for r in gruppo]
    print(f"{esito}: {campioni}")

# Stampa:
# errore: ['C', 'D']
# ok: ['A', 'B', 'E']
```

`groupby` restituisce coppie (chiave, iteratore_del_gruppo). L'iteratore del gruppo è pigro: si esaurisce non appena si passa alla coppia successiva nel ciclo esterno. Per questo motivo, se si vuole conservare i dati di un gruppo per uso successivo, bisogna convertirlo esplicitamente in lista (come nella riga `[r["campione"] for r in gruppo]` nell'esempio sopra).

---

## Un Trabocchetto: gli Iteratori si Esauriscono

La maggior parte degli strumenti visti in questa dispensa restituiscono iteratori, non liste. Questa distinzione è importante: un iteratore può essere percorso una sola volta. Una volta esaurito, non produce più valori e non segnala errori: restituisce semplicemente vuoto.

```python
numeri = [1, 2, 3, 4, 5]
it = reversed(numeri)

# Prima iterazione: funziona
print(list(it))  # [5, 4, 3, 2, 1]

# Seconda iterazione: l'iteratore è esausto
print(list(it))  # []
```

Lo stesso vale per `zip`, `enumerate`, `chain`, `islice` e gli iteratori prodotti da `groupby`. Se si ha bisogno di iterare più volte sullo stesso risultato, bisogna convertirlo in lista con `list(...)` prima di usarlo la seconda volta, oppure ricostruire l'iteratore da capo.

```python
from itertools import chain

serie_a = [1, 2, 3]
serie_b = [4, 5, 6]

# Salviamo come lista per poter iterare due volte
tutti = list(chain(serie_a, serie_b))

print(tutti)  # [1, 2, 3, 4, 5, 6]
print(tutti)  # [1, 2, 3, 4, 5, 6] — funziona ancora
```

---

## Dove Questi Strumenti Compaiono nel Codice Reale

Gli strumenti di questa dispensa non sono funzionalità di nicchia: compaiono in quasi tutto il codice Python scritto con attenzione alla chiarezza. `enumerate` sostituisce `range(len(...))` in una quota enorme del codice scientifico e di analisi dati. `zip` è indispensabile ogni volta che si lavora con dati tabulari distribuiti su più liste parallele. `sorted` con `key` è il fondamento dell'ordinamento flessibile in Python e si incontra in ogni sistema che gestisce collezioni di oggetti.

`itertools` è una libreria piccola ma densa: i costrutti che offre (tra cui `chain`, `islice`, `groupby`, ma anche `product`, `combinations`, `permutations` e altri) permettono di esprimere algoritmi complessi su sequenze in modo dichiarativo, spostando l'attenzione dal "come si itera" al "cosa si vuole ottenere".

Chi approfondisce questi strumenti trova anche una naturale connessione con i generatori, cioè funzioni che producono valori uno alla volta tramite `yield`. I generatori e `itertools` condividono la stessa filosofia: elaborare i dati in modo pigro, senza costruire strutture intermedie in memoria. Quella è la prossima frontiera naturale dopo aver assimilato i contenuti di questa dispensa.
