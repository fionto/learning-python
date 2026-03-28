# Capitolo 3: Sezione 3.1 — Le Liste: Raccogliere, Organizzare, Trasformare

## Introduzione: Quando una Variabile Non Basta

Fino ad ora, ogni variabile che avete incontrato conteneva un solo valore: un numero, una stringa, un booleano. Ma pensate a un caso concreto: volete scrivere un programma che calcoli la media dei voti di uno studente in dieci materie. Con quello che sapete oggi, dovreste dichiarare dieci variabili separate — `voto1`, `voto2`, `voto3`... — e gestirle tutte individualmente. Se i voti diventano venti, il programma diventa venti volte più lungo. Se diventano cento, è praticamente ingestibile.

La lista è la soluzione Python a questo problema. Immaginate una lista come una fila di cassetti in un mobile: ogni cassetto ha un numero d'ordine, si apre nello stesso modo degli altri, e potete aggiungerne di nuovi o svuotarne uno senza buttare via il mobile. In un'unica variabile, una lista può contenere zero, dieci, o un milione di valori. Il programma che calcola la media di cento voti con le liste è lungo quasi quanto quello che la calcola per dieci.

La lista è il primo di quattro tipi di strutture dati che esploreremo nella Sezione 3. Dopo averne capito il meccanismo, vi accorgerete che le tuple, i dizionari e le stringhe condividono molti dei suoi comportamenti: l'investimento fatto qui si ripaga subito.

## Costruire una Lista

In Python, una lista si crea racchiudendo una sequenza di valori tra parentesi quadre, separati da virgole. Il tipo di dati degli elementi può essere misto: interi, float, stringhe, booleani — o addirittura altre liste — possono coesistere nello stesso contenitore.

```python
# Una lista di numeri interi
voti = [8, 6, 9, 7, 10]

# Una lista con tipi misti
scheda = ["Mario Rossi", 1998, 8.4, True]

# Una lista vuota (utile come punto di partenza)
vuota = []

# Verifica del tipo
print(type(voti))   # Output: <class 'list'>
print(len(voti))    # Output: 5
```

La funzione `len()` restituisce il numero di elementi presenti nella lista. È uno strumento che userete in continuazione, sia per sapere quanti elementi ci sono, sia nei cicli per non sforare i limiti.

## Indicizzazione: Accedere a un Singolo Elemento

Ogni elemento di una lista ha una posizione, chiamata **indice**. Python conta a partire da zero: il primo elemento si trova all'indice 0, il secondo all'indice 1, e così via. Questo è uno dei punti dove i principianti fanno più errori, quindi vale la pena interiorizzarlo subito con un esempio concreto.

```python
capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Lisbona"]

# Accesso tramite indice positivo
print(capitali[0])   # Output: Roma
print(capitali[2])   # Output: Berlino

# Python supporta anche indici negativi: -1 è l'ultimo elemento
print(capitali[-1])  # Output: Lisbona
print(capitali[-2])  # Output: Madrid
```

Gli indici negativi sono un'eleganza di Python: evitano di dover scrivere `capitali[len(capitali) - 1]` ogni volta che volete l'ultimo elemento. L'indice `-1` equivale esattamente a quell'espressione.

Le liste sono **mutabili**: potete modificare un elemento senza ricreare tutta la lista, semplicemente assegnando un nuovo valore alla sua posizione.

```python
capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Lisbona"]
capitali[1] = "Lyon"   # Sostituzione di "Parigi"
print(capitali)
# Output: ['Roma', 'Lyon', 'Berlino', 'Madrid', 'Lisbona']
```

L'operatore `del` permette invece di eliminare un elemento dalla lista; gli elementi successivi si spostano automaticamente per riempire il buco.

```python
capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Lisbona"]
del capitali[2]       # Rimuove "Berlino"
print(capitali)
# Output: ['Roma', 'Parigi', 'Madrid', 'Lisbona']
print(len(capitali))  # Output: 4
```

## Slicing: Ritagliare una Porzione di Lista

L'indicizzazione vi dà un singolo elemento. Lo **slicing** (affettatura) vi dà una porzione: una sotto-lista estratta indicando un intervallo di indici. La sintassi è `lista[inizio:fine]`, dove `inizio` è incluso e `fine` è escluso.

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Elementi dall'indice 2 (incluso) all'indice 5 (escluso)
print(numeri[2:5])    # Output: [2, 3, 4]

# Dall'inizio fino all'indice 4 (escluso)
print(numeri[:4])     # Output: [0, 1, 2, 3]

# Dall'indice 6 fino alla fine
print(numeri[6:])     # Output: [6, 7, 8, 9]

# Tutta la lista (copia)
print(numeri[:])      # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

È possibile aggiungere un terzo parametro, detto **passo** (`step`), che specifica quanti elementi saltare ad ogni passo. La sintassi diventa `lista[inizio:fine:passo]`.

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ogni secondo elemento
print(numeri[::2])     # Output: [0, 2, 4, 6, 8]

# Ogni terzo elemento tra indice 1 e 8
print(numeri[1:8:3])   # Output: [1, 4, 7]

# Lista rovesciata con passo -1
print(numeri[::-1])    # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

Il passo negativo è un idioma molto usato per invertire una lista in modo conciso. Tenete presente che lo slicing produce sempre una **nuova lista**: la lista originale rimane intatta.

## Iterare su una Lista

Avere una lista è inutile se non sapete come scorrerla. Il ciclo `for` con l'operatore `in` è il modo naturale per visitare tutti gli elementi, uno alla volta.

```python
temperature = [22.3, 19.8, 25.1, 17.6, 23.0]

# Iterazione diretta sugli elementi
for temp in temperature:
    print(f"Temperatura rilevata: {temp} °C")

# Output:
# Temperatura rilevata: 22.3 °C
# Temperatura rilevata: 19.8 °C
# ... e così via
```

Se avete bisogno anche dell'indice durante l'iterazione, il modo più idiomatico è usare `range()` insieme a `len()`:

```python
temperature = [22.3, 19.8, 25.1, 17.6, 23.0]

for i in range(len(temperature)):
    print(f"Giorno {i+1}: {temperature[i]} °C")

# Output:
# Giorno 1: 22.3 °C
# Giorno 2: 19.8 °C
# ...
```

L'operatore `in` funziona anche come test di appartenenza, restituendo un booleano:

```python
frutta = ["mela", "pera", "banana", "kiwi"]

print("banana" in frutta)       # Output: True
print("ananas" in frutta)       # Output: False
print("ananas" not in frutta)   # Output: True
```

Questi test sono particolarmente utili nelle condizioni `if`, per verificare la presenza di un elemento prima di elaborarlo.

## Metodi delle Liste

Python mette a disposizione una serie di metodi integrati per manipolare le liste. Ogni metodo si chiama con la notazione a punto: `lista.metodo(argomenti)`. Alcuni metodi modificano la lista sul posto (in-place), altri restituiscono un nuovo valore senza alterare l'originale.

**`append(elemento)`** aggiunge un elemento in coda alla lista. È il modo più comune per costruire una lista dinamicamente.

```python
spesa = ["pane", "latte"]
spesa.append("uova")
spesa.append("burro")
print(spesa)
# Output: ['pane', 'latte', 'uova', 'burro']
```

**`pop([indice])`** rimuove l'elemento alla posizione specificata e, a differenza di `del` o `remove()`, **restituisce** il valore rimosso. Questo lo rende utilissimo quando non vuoi solo eliminare un dato, ma anche "estrarlo" per lavorarci subito dopo. Se non passi alcun indice tra le parentesi, Python rimuove automaticamente l'ultimo elemento. È importante ricordare che, come per l'indicizzazione standard, se provate a usare `pop()` su una lista vuota o con un indice inesistente, Python solleverà un `IndexError`.

```python
computer_stoccaggio = ["RAM", "CPU", "SSD", "GPU"]

# Rimuove l'elemento in posizione 1 (CPU) e lo salva in una variabile
componente = computer_stoccaggio.pop(1)

print(f"Abbiamo rimosso: {componente}") 
# Output: Abbiamo rimosso: CPU

print(computer_stoccaggio)              
# Output: ['RAM', 'SSD', 'GPU']

# Senza argomenti, rimuove l'ultimo (GPU)
ultimo = computer_stoccaggio.pop()
print(f"Ultimo rimosso: {ultimo}")      
# Output: Ultimo rimosso: GPU
```

**`insert(indice, elemento)`** inserisce un elemento in una posizione specifica, spostando in avanti tutti gli elementi successivi.

```python
spesa = ["pane", "latte", "uova"]
spesa.insert(1, "formaggio")   # Inserisce alla posizione 1
print(spesa)
# Output: ['pane', 'formaggio', 'latte', 'uova']
```

**`remove(elemento)`** elimina la prima occorrenza dell'elemento specificato. Se l'elemento non esiste, viene sollevata un'eccezione; conviene quindi verificare con `in` prima di chiamarlo.

```python
colori = ["rosso", "verde", "blu", "verde"]
colori.remove("verde")   # Rimuove solo il primo "verde"
print(colori)
# Output: ['rosso', 'blu', 'verde']
```

**`index(elemento)`** restituisce l'indice della prima occorrenza dell'elemento. Anche qui, se l'elemento non è presente, viene sollevata un'eccezione.

```python
pianeti = ["Mercurio", "Venere", "Terra", "Marte"]
pos = pianeti.index("Terra")
print(pos)   # Output: 2
```

**`sort()`** ordina la lista in-place (modifica direttamente la lista, senza crearne una nuova). La funzione **`sorted()`**, invece, restituisce una nuova lista ordinata senza alterare l'originale.

```python
punteggi = [45, 12, 78, 33, 90, 5]

# sorted() non modifica l'originale
ordinati = sorted(punteggi)
print(punteggi)    # Output: [45, 12, 78, 33, 90, 5]  (invariato)
print(ordinati)    # Output: [5, 12, 33, 45, 78, 90]

# sort() modifica in-place
punteggi.sort()
print(punteggi)    # Output: [5, 12, 33, 45, 78, 90]

# Ordine decrescente
punteggi.sort(reverse=True)
print(punteggi)    # Output: [90, 78, 45, 33, 12, 5]
```

**`reverse()`** inverte l'ordine degli elementi in-place.

**`count(elemento)`** conta quante volte un elemento appare nella lista.

**`clear()`** svuota la lista, lasciandola vuota ma ancora esistente.

```python
dati = [3, 1, 4, 1, 5, 9, 2, 6, 1]
print(dati.count(1))   # Output: 3

dati.reverse()
print(dati)            # Output: [1, 6, 2, 9, 5, 1, 4, 1, 3]

dati.clear()
print(dati)            # Output: []
```

## Copia e Clonazione

Un errore molto comune per i principianti è pensare che assegnando una lista a una nuova variabile si crei una copia indipendente. In realtà, si crea un secondo nome che punta allo stesso oggetto in memoria: modificare uno modifica anche l'altro.

```python
originale = [1, 2, 3, 4, 5]
alias = originale         # Alias, NON una copia

alias[0] = 99
print(originale)   # Output: [99, 2, 3, 4, 5]  (modificato!)
```

Per creare una vera copia indipendente, si usa lo slicing completo `[:]` oppure il metodo `copy()`:

```python
originale = [1, 2, 3, 4, 5]

# Metodo 1: slicing completo
copia1 = originale[:]

# Metodo 2: metodo copy()
copia2 = originale.copy()

copia1[0] = 99
print(originale)   # Output: [1, 2, 3, 4, 5]  (invariato)
print(copia1)      # Output: [99, 2, 3, 4, 5]
```

Questo comportamento vale per tutti gli oggetti mutabili in Python ed è importante capirlo prima di scrivere programmi più complessi.

## List Comprehension

La **list comprehension** è una sintassi concisa per costruire una lista applicando un'espressione a ogni elemento di un iterabile, con la possibilità di filtrare gli elementi tramite una condizione. È una delle caratteristiche più eleganti di Python.

La forma base è:

```
[espressione for variabile in iterabile]
```

con un filtro opzionale:

```
[espressione for variabile in iterabile if condizione]
```

Vediamo prima il modo "lungo" e poi la versione compressa, per capire il parallelismo:

```python
# Modo tradizionale: costruire la lista dei quadrati con un ciclo for
quadrati = []
for n in range(1, 6):
    quadrati.append(n ** 2)
print(quadrati)   # Output: [1, 4, 9, 16, 25]

# Modo compresso: list comprehension equivalente
quadrati = [n ** 2 for n in range(1, 6)]
print(quadrati)   # Output: [1, 4, 9, 16, 25]
```

Il vantaggio diventa ancora più evidente quando si aggiunge un filtro. Supponiamo di voler costruire la lista dei quadrati solo per i numeri pari:

```python
# Solo i quadrati dei numeri pari tra 1 e 10
quadrati_pari = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(quadrati_pari)   # Output: [4, 16, 36, 64, 100]
```

La list comprehension può anche lavorare su liste già esistenti:

```python
parole = ["mela", "Banana", "KIWI", "pera", "Arancia"]

# Converti tutte le parole in minuscolo
minuscole = [p.lower() for p in parole]
print(minuscole)
# Output: ['mela', 'banana', 'kiwi', 'pera', 'arancia']

# Tieni solo le parole con più di 4 caratteri
lunghe = [p for p in parole if len(p) > 4]
print(lunghe)
# Output: ['Banana', 'pera', 'Arancia']
```

La list comprehension è potente, ma usatela con giudizio: se l'espressione diventa troppo lunga o annida più livelli di logica, spesso un ciclo `for` esplicito è più leggibile. La chiarezza del codice viene prima della compattezza.

## Matrici: Liste di Liste

Finora ogni lista conteneva valori semplici. Ma gli elementi di una lista possono essere a loro volta delle liste: si ottiene così una struttura bidimensionale, comunemente chiamata **matrice**. Questa è la struttura naturale per rappresentare tabelle, griglie, immagini pixel per pixel, o scacchiere.

Una matrice 3×4 (tre righe, quattro colonne) si costruisce come una lista di tre liste, ciascuna con quattro elementi:

```python
# Matrice 3x4
matrice = [
    [1,  2,  3,  4],   # Riga 0
    [5,  6,  7,  8],   # Riga 1
    [9, 10, 11, 12]    # Riga 2
]

# Accedere all'elemento in riga 1, colonna 2
print(matrice[1][2])   # Output: 7

# Accedere a tutta la riga 0
print(matrice[0])      # Output: [1, 2, 3, 4]
```

Il doppio indice `matrice[riga][colonna]` è il modo standard di accedere agli elementi. Per scorrere tutti gli elementi di una matrice, si usano due cicli `for` annidati:

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Stampa ogni elemento con la sua posizione
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(f"matrice[{i}][{j}] = {matrice[i][j]}")

# Output:
# matrice[0][0] = 1
# matrice[0][1] = 2
# ...
# matrice[2][2] = 9
```

Le matrici possono avere righe di lunghezza diversa (strutture "a dente di sega"), ma le griglie regolari come quella sopra sono le più comuni. Per strutture tridimensionali (cubi), il principio si estende: si aggiunge un terzo livello di annidamento e un terzo indice.

```python
# Un "cubo" 2x2x2
cubo = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Elemento in posizione [strato][riga][colonna]
print(cubo[0][1][0])   # Output: 3
print(cubo[1][0][1])   # Output: 6
```

Con strutture di questa complessità, la leggibilità del codice dipende molto dalla cura con cui si nominano le variabili di indice: preferite `strato`, `riga`, `colonna` a `i`, `j`, `k` non appena la struttura diventa più profonda di due dimensioni.

## Conclusione: Una Cassetta degli Attrezzi Flessibile

Avete ora una cassetta degli attrezzi completa per lavorare con le liste. Sapete costruirle, accedere a singoli elementi tramite indice, ritagliarne porzioni con lo slicing, aggiungere e rimuovere elementi con i metodi, ordinarle, copiarle in sicurezza, costruirne di nuove in modo compatto con la list comprehension, e organizzarle in strutture bidimensionali e tridimensionali.

La lista è la struttura dati più versatile che incontrerete in Python, e le tecniche che avete imparato qui si ripresentano quasi identiche nelle sezioni successive: le tuple condividono indicizzazione e slicing, le stringhe si comportano come sequenze immutabili di caratteri, e i dizionari estendono il concetto di contenitore associando chiavi arbitrarie ai valori invece di usare indici numerici.

Nel prossimo capitolo esploreremo le **tuple** (Sezione 3.2): strutture molto simili alle liste, ma immutabili. Scoprirete perché questa limitazione apparente è in realtà una garanzia di affidabilità, e in quali situazioni preferire una tupla a una lista.
