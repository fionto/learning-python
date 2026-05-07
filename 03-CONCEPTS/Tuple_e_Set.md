# Capitolo 7: Tuple e Set in Python

## Introduzione: Contenitori con caratteri diversi

Quando andate al supermercato, avete due tipi di borse. La prima è una cassetta rigida da frutta: ci mettete dentro le arance in un certo ordine, ma una volta sigillata non potete aggiungere né togliere niente. La seconda è un sacchetto a rete dove buttate dentro i prodotti alla rinfusa: non importa l'ordine, e se ci mettete due confezioni identiche una è superflua. Python ha due strutture dati che ricordano esattamente queste due borse: le tuple e i set.

Finora avete incontrato le liste, che sono sequenze ordinate e modificabili. Capire quando usare una lista, una tupla o un set è una delle prime vere scelte da programmatore che vi troverete a fare. Non è una questione di gusti: ognuna di queste strutture ha proprietà precise che la rendono la scelta giusta in certi contesti e sbagliata in altri.

In questa dispensa esploriamo prima le tuple in profondità, poi i set, e infine il frozenset. Alla fine avrete gli strumenti per scegliere la struttura giusta al momento giusto.

---

## Le tuple: ordine immutabile

Una tupla è una sequenza ordinata di elementi che, una volta creata, non può essere modificata. La sintassi di base è una lista di valori separati da virgole, racchiusi tra parentesi tonde:

```python
# Creazione di una tupla con tre elementi
coordinate = (10, 20, 30)
print(coordinate)  # Output: (10, 20, 30)
print(type(coordinate))  # Output: <class 'tuple'>
```

Le parentesi, però, non sono obbligatorie. Python riconosce una tupla anche solo dalla presenza delle virgole: questo meccanismo si chiama *packing*:

```python
# Packing: le virgole fanno la tupla, non le parentesi
colori = "rosso", "verde", "blu"
print(colori)  # Output: ('rosso', 'verde', 'blu')
print(type(colori))  # Output: <class 'tuple'>
```

Questa caratteristica vi sembrerà curiosa adesso, ma tornerà utile tra poco quando parleremo di funzioni che restituiscono più valori.

Ci sono due casi speciali da tenere a mente. La tupla vuota si crea con `()` oppure con `tuple()`:

```python
vuota = ()
anche_vuota = tuple()
print(len(vuota), len(anche_vuota))  # Output: 0 0
```

La tupla con un solo elemento è la trappola classica per i principianti. `(42)` non è una tupla: è semplicemente il numero 42 racchiuso tra parentesi, come in matematica. Per creare una tupla da un singolo elemento, la virgola finale è obbligatoria:

```python
non_e_una_tupla = (42)
e_una_tupla = (42,)
anche_tupla = 42,  # forma compatta

print(type(non_e_una_tupla))  # Output: <class 'int'>
print(type(e_una_tupla))      # Output: <class 'tuple'>
print(e_una_tupla)            # Output: (42,)
```

---

## Indicizzazione, slicing e metodi

Poiché le tuple sono sequenze ordinate, potete accedere ai loro elementi esattamente come fareste con una lista: con l'indice positivo che parte da zero, con l'indice negativo che parte da -1 dalla fine, e con lo slicing per estrarre sottosequenze.

```python
dati = (10, 20, 30, 40, 50)

print(dati[0])     # Output: 10
print(dati[-1])    # Output: 50
print(dati[1:4])   # Output: (20, 30, 40)
print(dati[::-1])  # Output: (50, 40, 30, 20, 10)
```

Le tuple offrono solo due metodi nativi, perché tutto il resto richiederebbe modifiche che l'immutabilità non consente:

```python
numeri = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

# .count(valore): conta quante volte appare un elemento
print(numeri.count(1))  # Output: 2
print(numeri.count(5))  # Output: 2
print(numeri.count(7))  # Output: 0

# .index(valore): restituisce l'indice della prima occorrenza
print(numeri.index(4))  # Output: 2
print(numeri.index(5))  # Output: 4  (la prima, non la seconda)
```

Se cercate con `.index()` un valore che non esiste nella tupla, Python solleva un `ValueError`. Tenete questo in mente quando lavorate con dati che potrebbero non contenere il valore che cercate.

---

## L'immutabilità: cosa significa davvero

L'immutabilità di una tupla significa che non potete aggiungere, togliere né sostituire i suoi elementi dopo la creazione. Qualsiasi tentativo genera un `TypeError`:

```python
punto = (3, 7)

# Questo produce un errore:
# punto[0] = 10  # TypeError: 'tuple' object does not support item assignment
# punto.append(5)  # AttributeError: 'tuple' object has no attribute 'append'
```

Tuttavia, c'è una sottigliezza importante: se una tupla contiene al suo interno una lista, quella lista rimane modificabile. La tupla garantisce che il *riferimento* agli oggetti al suo interno non cambi, non che gli oggetti stessi siano congelati:

```python
# Una tupla può contenere una lista mutabile
record = ("Mario", [85, 90, 78])

# record[0] = "Luigi"  # Errore: non posso cambiare l'elemento della tupla
record[1].append(95)    # Questo invece funziona: modifico la lista interna

print(record)  # Output: ('Mario', [85, 90, 78, 95])
```

---

## Unpacking: distribuire i valori

Una delle operazioni più eleganti sulle tuple è l'*unpacking*: assegnare in una sola istruzione gli elementi di una tupla a più variabili. Python controlla che il numero di variabili a sinistra corrisponda esattamente al numero di elementi della tupla:

```python
coordinata = (4, 7)
x, y = coordinata
print(x)  # Output: 4
print(y)  # Output: 7

# Con tre elementi
rosso, verde, blu = (255, 128, 0)
print(rosso)  # Output: 255
```

L'*extended unpacking* permette di catturare un numero variabile di elementi con l'operatore `*`. La variabile preceduta da asterisco raccoglie tutto ciò che rimane in una lista:

```python
numeri = (1, 2, 3, 4, 5)

primo, *centro, ultimo = numeri
print(primo)   # Output: 1
print(centro)  # Output: [2, 3, 4]
print(ultimo)  # Output: 5

# La variabile stella può essere ovunque
testa, *coda = (10, 20, 30, 40)
print(testa)  # Output: 10
print(coda)   # Output: [20, 30, 40]
```

Un uso classico e pratico dell'unpacking è lo scambio di valori tra due variabili. In molti linguaggi serviva una variabile temporanea; in Python basta una riga:

```python
a = 5
b = 10

# Scambio senza variabile temporanea
a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5
```

Quello che succede internamente è che `b, a` costruisce una tupla `(10, 5)` e poi l'unpacking la distribuisce.

---

## Tuple come valori di ritorno e come chiavi

Una funzione in Python può restituire più valori separati da virgola. Tecnicamente sta restituendo una tupla, che poi potete unpackare immediatamente:

```python
def dividi(dividendo, divisore):
    quoziente = dividendo // divisore
    resto = dividendo % divisore
    return quoziente, resto  # restituisce una tupla

q, r = dividi(17, 5)
print(f"17 diviso 5: quoziente {q}, resto {r}")  # Output: 17 diviso 5: quoziente 3, resto 2
```

Un'altra proprietà importante dell'immutabilità è l'*hashability*: gli oggetti immutabili possono essere usati come chiavi nei dizionari o come elementi di un set (lo vedremo tra poco). Le liste, essendo mutabili, non possono. Le tuple sì, purché non contengano al loro interno oggetti mutabili come liste:

```python
# Tupla come chiave di dizionario: utile per coordinate o griglia
griglia = {}
griglia[(0, 0)] = "origine"
griglia[(1, 2)] = "punto A"
griglia[(3, 4)] = "punto B"

print(griglia[(1, 2)])  # Output: punto A

# Una lista non può essere chiave:
# griglia[[0, 0]] = "errore"  # TypeError: unhashable type: 'list'
```

---

## Named tuple: tuple con nomi

La libreria standard offre uno strumento molto comodo per creare tuple i cui campi hanno un nome, rendendo il codice più leggibile. Si importa `namedtuple` dal modulo `collections`:

```python
from collections import namedtuple

# Definisco un tipo "Punto" con due campi
Punto = namedtuple('Punto', ['x', 'y'])

p = Punto(3, 7)
print(p)         # Output: Punto(x=3, y=7)
print(p.x)       # Output: 3
print(p.y)       # Output: 7
print(p[0])      # Output: 3  (funziona anche l'indicizzazione classica)
```

Una named tuple si comporta in tutto e per tutto come una tupla normale (è immutabile, hashable, unpackable), ma aggiunge la leggibilità dei nomi. È molto usata per rappresentare record strutturati come punti geometrici, colori RGB, coordinate geografiche.

```python
from collections import namedtuple

Colore = namedtuple('Colore', ['r', 'g', 'b'])
rosso = Colore(255, 0, 0)
verde = Colore(0, 255, 0)

r, g, b = rosso  # unpacking classico funziona ancora
print(f"Rosso: r={rosso.r}, g={rosso.g}, b={rosso.b}")
# Output: Rosso: r=255, g=0, b=0
```

---

## I set: insiemi matematici in Python

Pensate a un set come a un insieme nel senso matematico del termine: una collezione non ordinata di elementi tutti distinti. Non importa in quale ordine li inserite, e ogni elemento può comparire al massimo una volta.

La sintassi di creazione usa le parentesi graffe con elementi separati da virgole:

```python
frutti = {"mela", "pera", "banana", "mela"}  # "mela" appare due volte
print(frutti)  # Output: {'pera', 'banana', 'mela'}  (un solo "mela")
```

L'ordine di stampa potrebbe variare: i set non garantiscono alcun ordine particolare.

Attenzione alla trappola delle parentesi vuote: `{}` crea un dizionario vuoto, non un set vuoto. Per creare un set vuoto dovete usare obbligatoriamente `set()`:

```python
dizionario_vuoto = {}
print(type(dizionario_vuoto))  # Output: <class 'dict'>

set_vuoto = set()
print(type(set_vuoto))  # Output: <class 'set'>
```

Potete anche creare un set a partire da una lista o da qualsiasi sequenza iterabile. Questo è un modo pratico per eliminare i duplicati:

```python
voti = [8, 7, 9, 7, 8, 10, 9, 7]
voti_unici = set(voti)
print(voti_unici)  # Output: {8, 9, 10, 7}  (ordine variabile)
print(len(voti_unici))  # Output: 4
```

---

## Aggiungere, rimuovere e svuotare elementi

I set sono mutabili: potete aggiungere e rimuovere elementi dopo la creazione.

Per aggiungere un elemento si usa `.add()`. Se l'elemento è già presente, l'operazione non fa nulla:

```python
colori = {"rosso", "verde"}
colori.add("blu")
colori.add("rosso")  # già presente: nessun effetto

print(colori)  # Output: {'rosso', 'verde', 'blu'}
```

Per rimuovere, avete due opzioni con comportamenti diversi. `.remove(elemento)` rimuove l'elemento, ma se non esiste solleva un `KeyError`. `.discard(elemento)` fa la stessa cosa ma non genera alcun errore se l'elemento non c'è:

```python
animali = {"gatto", "cane", "pesce"}

animali.remove("cane")
print(animali)  # Output: {'gatto', 'pesce'}

animali.discard("pesce")
print(animali)  # Output: {'gatto'}

animali.discard("aquila")  # nessun errore, elemento non presente
print(animali)  # Output: {'gatto'}

# animali.remove("aquila")  # Questo causerebbe: KeyError: 'aquila'
```

`.pop()` rimuove e restituisce un elemento arbitrario dal set. Poiché i set non hanno un ordine definito, non potete prevedere quale elemento verrà estratto. È utile quando volete "consumare" un set elemento per elemento senza importarvi dell'ordine:

```python
numeri = {10, 20, 30}
estratto = numeri.pop()
print(f"Estratto: {estratto}")  # un numero qualsiasi dei tre
print(f"Rimasti: {numeri}")     # i restanti due
```

`.clear()` svuota completamente il set:

```python
s = {1, 2, 3, 4}
s.clear()
print(s)  # Output: set()
```

---

## Operazioni insiemistiche

La vera potenza dei set emerge con le operazioni matematiche di teoria degli insiemi. Python le supporta sia tramite operatori simbolici che tramite metodi espliciti.

L'*unione* di due set produce un nuovo set con tutti gli elementi di entrambi, senza duplicati:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

unione = a | b
print(unione)  # Output: {1, 2, 3, 4, 5, 6}

# Equivalente con metodo:
print(a.union(b))  # Output: {1, 2, 3, 4, 5, 6}
```

L'*intersezione* produce solo gli elementi presenti in entrambi i set:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

intersezione = a & b
print(intersezione)  # Output: {3, 4}

print(a.intersection(b))  # Output: {3, 4}
```

La *differenza* `a - b` produce gli elementi di `a` che non sono in `b`:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

differenza = a - b
print(differenza)  # Output: {1, 2}

# Nota: non è commutativa
print(b - a)  # Output: {5, 6}

print(a.difference(b))  # Output: {1, 2}
```

La *differenza simmetrica* produce gli elementi presenti in uno dei due set ma non in entrambi (è l'opposto dell'intersezione):

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

sim_diff = a ^ b
print(sim_diff)  # Output: {1, 2, 5, 6}

print(a.symmetric_difference(b))  # Output: {1, 2, 5, 6}
```

Infine, potete verificare relazioni di sottoinsieme e soprainsieme:

```python
piccolo = {1, 2}
grande = {1, 2, 3, 4, 5}

print(piccolo <= grande)          # Output: True  (piccolo è sottoinsieme di grande)
print(piccolo.issubset(grande))   # Output: True

print(grande >= piccolo)          # Output: True  (grande è soprainsieme di piccolo)
print(grande.issuperset(piccolo)) # Output: True

print(piccolo <= piccolo)  # Output: True  (un set è sottoinsieme di se stesso)
```

---

## Membership testing: il vantaggio O(1)

Una delle ragioni pratiche per preferire un set a una lista è la velocità nella verifica di appartenenza. Con una lista, l'operatore `in` deve scorrere gli elementi uno per uno finché non trova quello cercato (nel caso peggiore, fino alla fine). Con un set, l'operazione è costante indipendentemente da quanti elementi contiene: si dice che ha complessità O(1).

```python
# Con una lista
nomi_lista = ["Alice", "Bruno", "Carlo", "Diana", "Elena"]
print("Carlo" in nomi_lista)  # True, ma scorre la lista

# Con un set
nomi_set = {"Alice", "Bruno", "Carlo", "Diana", "Elena"}
print("Carlo" in nomi_set)  # True, accesso immediato
```

Per piccole collezioni la differenza è impercettibile. Ma se avete migliaia o milioni di elementi e fate molte verifiche di appartenenza, la differenza diventa enorme.

---

## Il frozenset: set immutabile

Così come le tuple sono la versione immutabile delle liste, il `frozenset` è la versione immutabile del `set`. Si crea con la funzione `frozenset()`:

```python
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})
print(type(fs))  # Output: <class 'frozenset'>
```

Essendo immutabile, un frozenset è hashable: può essere usato come chiave di un dizionario o inserito in un altro set, cosa che un set normale non può fare:

```python
# Un frozenset può essere elemento di un altro set
insieme_di_insiemi = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})}
print(insieme_di_insiemi)  # Output: {frozenset({1, 2}), frozenset({3, 4})}  (un solo {1,2})

# Un frozenset può essere chiave di un dizionario
cache = {}
chiave = frozenset({"python", "programmazione"})
cache[chiave] = "risultato cached"
print(cache[chiave])  # Output: risultato cached
```

Il frozenset supporta tutte le operazioni di consultazione e le operazioni insiemistiche dei set normali, ma non i metodi di modifica come `.add()`, `.remove()` o `.clear()`.

---

## Quando usare cosa: la bussola

Arrivati a questo punto, conviene riassumere in modo discorsivo quando preferire ciascuna struttura.

Usate una **lista** quando avete una sequenza di elementi che potrebbe cambiare nel tempo, quando l'ordine conta, e quando i duplicati sono ammessi e significativi (per esempio, la lista delle temperature orarie di una giornata).

Usate una **tupla** quando avete una collezione di valori che concettualmente non dovrebbe cambiare: le coordinate di un punto, i parametri di configurazione, i valori di ritorno multipli di una funzione. L'immutabilità serve da documentazione implicita: chi legge il codice capisce che quei dati sono stabili. Usatele anche come chiavi di dizionari o dove serve hashability.

Usate un **set** quando la caratteristica che vi interessa è l'unicità degli elementi e quando avete bisogno di fare operazioni insiemistiche o verifiche di appartenenza rapide. Un set è la scelta naturale per rappresentare una collezione di elementi univoci come i tag di un articolo, le parole distinte in un testo, o gli ID univoci di utenti visitatori.

Usate un **frozenset** nelle stesse situazioni in cui usereste un set, ma quando avete bisogno che quella collezione sia hashable e quindi usabile come chiave o come elemento di un altro set.

---

## Conclusione: strutture per ogni occasione

Le tuple e i set completano il quadro delle strutture dati fondamentali di Python. Con liste, tuple, dizionari e set avete a disposizione quattro contenitori con caratteristiche diverse e complementari. La scelta giusta non dipende da quale vi è più familiare, ma da quale rispecchia la natura dei dati con cui state lavorando: se i dati sono ordinati o no, se cambieranno o no, se i duplicati hanno senso o no.

La prossima dispensa si occuperà delle stringhe in modo più approfondito: le stringhe in Python si comportano in molti modi come tuple (sono sequenze immutabili indicizzabili), ma offrono un ricco ecosistema di metodi dedicati alla manipolazione del testo.
