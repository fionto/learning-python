# Capitolo 3: Sezione 3.4 - Liste: Container Intelligenti per Dati Multipli

## Introduzione: Il Problema del Programmatore Pigro

Immaginate di dover leggere 1000 numeri dall'utente. Cosa fate? Create una variabile per ognuno?

```python
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
# ... 997 volte in più!
```

È insano. È impraticabile. Peggio ancora: dopo aver letto 1000 numeri, volete ordinarli dal più piccolo al più grande. Senza liste, avreste bisogno di... non sapete nemmeno da dove cominciare. **Ecco perché le liste sono fondamentali in programmazione.** Una lista è un contenitore singolo che può contenere **centinaia, migliaia, o milioni di elementi**. Tutto gestito con una sola variabile.

### L'Analogia della Scatola Numerata

Immaginate una scatola con scomparti numerati:

```
┌─────────────────────────────┐
│ Scatola "numeri"            │
├─────────────────────────────┤
│ [0] │ 10 │                  │
│ [1] │ 5  │                  │
│ [2] │ 7  │                  │
│ [3] │ 2  │                  │
│ [4] │ 1  │                  │
└─────────────────────────────┘
```

Ogni scomparto ha un numero (indice), partendo da 0. Potete accedere a qualsiasi scomparto per leggere, modificare, o aggiungere un valore. Questa è una lista.

## 3.4.1 Che Cosa È Una Lista: La Definizione

Una **lista** è una collezione ordinata di elementi racchiusi tra **parentesi quadre** `[` e `]`, separati da **virgole**.

```python
numeri = [10, 5, 7, 2, 1]
nomi = ["Alice", "Bob", "Charlie"]
misti = [1, "due", 3.0, True]
```

### Caratteristiche Fondamentali

**Ordinata:** Gli elementi hanno un ordine. Il primo elemento è sempre il primo, il secondo è sempre il secondo.

**Indicizzata da zero:** Il primo elemento ha indice 0, il secondo ha indice 1, ecc. Questo all'inizio confonde, ma diventerà naturale.

**Mutabile:** Potete **modificare** gli elementi. Potete aggiungere, rimuovere, sostituire.

**Eterogenea:** Una lista può contenere elementi di **tipi diversi**:
```python
lista_mista = [42, "ciao", 3.14, True, [1, 2, 3]]
#             intero, stringa, float, booleano, lista!
```

### Creazione di Liste

**Esplicitamente con valori:**
```python
colori = ["rosso", "verde", "blu"]
temperature = [20.5, 22.0, 18.5, 25.0]
```

**Vuota, da riempire dopo:**
```python
lista_vuota = []
# Più tardi, potete aggiungere elementi
```

**Con la funzione list():**
```python
lista_da_stringa = list("abc")  # ['a', 'b', 'c']
```

## 3.4.2 Indicizzazione: Accedere agli Elementi

### La Sintassi Fondamentale

Per accedere a un elemento, usate il nome della lista seguito da **parentesi quadre** con **l'indice**:

```python
numeri = [10, 5, 7, 2, 1]

print(numeri[0])  # Output: 10 (primo elemento)
print(numeri[1])  # Output: 5 (secondo elemento)
print(numeri[4])  # Output: 1 (quinto elemento)
```

### Modificare Elementi

Potete **assegnare un nuovo valore** a un elemento:

```python
numeri = [10, 5, 7, 2, 1]
numeri[0] = 111  # Cambia il primo elemento

print(numeri)    # Output: [111, 5, 7, 2, 1]
```

### Copiare Elementi da una Posizione all'Altra

Potete usare il valore di un elemento per assegnarlo altrove:

```python
numeri = [10, 5, 7, 2, 1]
numeri[1] = numeri[4]  # Copia il quinto elemento al secondo

print(numeri)  # Output: [10, 1, 7, 2, 1]
```

### Indici come Espressioni

L'indice non deve essere un numero fisso. Può essere **un'espressione**:

```python
numeri = [10, 20, 30, 40, 50]

i = 2
print(numeri[i])        # Output: 30

print(numeri[i + 1])    # Output: 40
print(numeri[len(numeri) - 1])  # Output: 50 (ultimo elemento)
```

Questo vi permette di **iterare** attraverso liste con i loop.

## 3.4.3 Accedere e Stampare: Visualizzare le Liste

### Stampare Un Singolo Elemento

```python
colori = ["rosso", "verde", "blu"]
print(colori[0])  # Output: rosso
print(colori[2])  # Output: blu
```

### Stampare Tutta la Lista

```python
colori = ["rosso", "verde", "blu"]
print(colori)  # Output: ['rosso', 'verde', 'blu']
```

Python visualizza la lista con le parentesi quadre e le virgole: è la rappresentazione interna.

### Ottenere la Lunghezza: len()

La funzione `len()` ritorna il **numero di elementi** in una lista:

```python
numeri = [10, 5, 7, 2, 1]
print(len(numeri))  # Output: 5

nomi = ["Alice"]
print(len(nomi))    # Output: 1

vuota = []
print(len(vuota))   # Output: 0
```

Questo è cruciale per **loop che processano liste di lunghezza sconosciuta**.

## 3.4.4 Eliminare Elementi: L'Istruzione del

Per **rimuovere** un elemento da una lista, usate l'istruzione `del`:

```python
numeri = [10, 5, 7, 2, 1]
del numeri[1]  # Rimuove il secondo elemento (5)

print(numeri)      # Output: [10, 7, 2, 1]
print(len(numeri)) # Output: 4
```

### Importante: Errore di IndexError

Dopo aver eliminato un elemento, **non potete accedere a un indice che non esiste**:

```python
numeri = [10, 5, 7, 2, 1]
del numeri[1]       # Lunghezza ora è 4

print(numeri[4])    # ERRORE: IndexError - indice fuori intervallo
numeri[4] = 100     # ERRORE: stessa cosa
```

Con 4 elementi, gli indici validi sono **0, 1, 2, 3**. L'indice 4 non esiste.

Questo è un errore comune: i principianti eliminano un elemento e poi cercano di accedere a indici vecchi.

## 3.4.5 Indici Negativi: Accesso Inverso

Python permette **indici negativi**, che contano dal **fondo della lista**:

```python
numeri = [111, 7, 2, 1]

print(numeri[-1])   # Output: 1 (ultimo elemento)
print(numeri[-2])   # Output: 2 (penultimo)
print(numeri[-3])   # Output: 7 (terz'ultimo)
print(numeri[-4])   # Output: 111 (primo elemento, da dietro)
```

### Come Funzionano gli Indici Negativi

Per una lista di 4 elementi:

```
Indici positivi:  [0]  [1]  [2]  [3]
Valori:           111   7    2    1
Indici negativi: [-4] [-3] [-2] [-1]
```

**Caso d'uso pratico:** Accedere agli ultimi elementi senza sapere la lunghezza:

```python
lista_con_lunghezza_sconosciuta = get_lista_da_database()

ultimo = lista_con_lunghezza_sconosciuta[-1]
penultimo = lista_con_lunghezza_sconosciuta[-2]
```

Non dovete fare `len(lista) - 1`. Usate `-1`.

## 3.4.6 Metodi di Lista: Manipolare Dinamicamente

Le liste hanno **metodi**—funzioni speciali che operano sulla lista stessa.

### append(): Aggiungere alla Fine

```python
colori = ["rosso", "verde"]
colori.append("blu")
colori.append("giallo")

print(colori)  # Output: ['rosso', 'verde', 'blu', 'giallo']
```

### insert(): Inserire in una Posizione Specifica

```python
colori = ["rosso", "verde", "blu"]
colori.insert(1, "arancione")  # Inserisce a indice 1

print(colori)  # Output: ['rosso', 'arancione', 'verde', 'blu']
```

`insert(indice, valore)` sposta tutti gli elementi successivi a destra.

### remove(): Rimuovere per Valore

```python
colori = ["rosso", "verde", "blu", "rosso"]
colori.remove("rosso")  # Rimuove la PRIMA occorrenza

print(colori)  # Output: ['verde', 'blu', 'rosso']
```

**Nota:** Rimuove solo la **prima occorrenza**. Se "rosso" appare due volte, rimuove solo il primo.

### pop(): Rimuovere per Indice e Ottenere il Valore

```python
numeri = [10, 20, 30, 40]
ultimo = numeri.pop()  # Rimuove e ritorna l'ultimo elemento

print(ultimo)    # Output: 40
print(numeri)    # Output: [10, 20, 30]

secondo = numeri.pop(1)  # Rimuove e ritorna l'elemento a indice 1

print(secondo)   # Output: 20
print(numeri)    # Output: [10, 30]
```

### clear(): Svuotare la Lista

```python
numeri = [1, 2, 3, 4, 5]
numeri.clear()

print(numeri)  # Output: []
```

### sort(): Ordinare la Lista

```python
numeri = [3, 1, 4, 1, 5, 9, 2, 6]
numeri.sort()

print(numeri)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
```

**Nota:** `sort()` ordina la lista **in place**—modifica la lista originale.

Per una **copia ordinata**, usate `sorted()`:

```python
numeri = [3, 1, 4, 1, 5]
ordinati = sorted(numeri)  # Ritorna nuova lista ordinata

print(numeri)     # Output: [3, 1, 4, 1, 5] (inalterata)
print(ordinati)   # Output: [1, 1, 3, 4, 5]
```

### reverse(): Invertire l'Ordine

```python
numeri = [1, 2, 3, 4, 5]
numeri.reverse()

print(numeri)  # Output: [5, 4, 3, 2, 1]
```

### count() e index(): Ricerca

```python
numeri = [1, 2, 3, 2, 4, 2, 5]

print(numeri.count(2))    # Output: 3 (quante volte appare 2)
print(numeri.index(2))    # Output: 1 (primo indice dove appare 2)
print(numeri.index(4))    # Output: 4
```

## 3.4.7 Inizializzare Liste: Dalla Pratica

### Creare Liste Vuote e Riempirle

Un pattern comune è creare una lista vuota e riempirla man mano:

```python
numeri = []

for i in range(5):
    numeri.append(i + 1)

print(numeri)  # Output: [1, 2, 3, 4, 5]
```

### Creare Liste con Motivi Specifici

**Usando insert(0, ...)** per inserire all'inizio (ordine inverso):

```python
numeri = []

for i in range(5):
    numeri.insert(0, i + 1)  # Inserisce sempre all'inizio

print(numeri)  # Output: [5, 4, 3, 2, 1]
```

Ogni volta che inserite all'inizio, gli elementi precedenti sono spinti a destra.

## 3.4.8 Iterare su Liste: I Loop for

### Pattern 1: Iterare per Indice

```python
numeri = [10, 20, 30, 40, 50]
somma = 0

for i in range(len(numeri)):
    somma += numeri[i]

print(somma)  # Output: 150
```

Utile quando **avete bisogno dell'indice** per calcoli complessi.

### Pattern 2: Iterare Direttamente sui Valori (Preferito)

```python
numeri = [10, 20, 30, 40, 50]
somma = 0

for numero in numeri:
    somma += numero

print(somma)  # Output: 150
```

Questo è **più leggibile e Pythonic**. Usate questo quando non vi serve l'indice.

### Caso Pratico: Calcolare la Media

```python
voti = [18, 24, 20, 19, 22]

somma = 0
for voto in voti:
    somma += voto

media = somma / len(voti)
print(f"Media: {media}")  # Output: Media: 20.6
```

## 3.4.9 Algoritmi su Liste: Scambio e Inversione

### Il Problema dello Scambio

Per invertire l'ordine manualmente, dovete scambiare elementi. Ma c'è un'insidia:

```python
# Sbagliato
a = 1
b = 2
a = b  # Ora a = 2
b = a  # Ora b = 2 (perdete il valore di a!)
```

### La Soluzione: Variabile Ausiliaria

```python
# Corretto (vecchio metodo)
a = 1
b = 2
temp = a
a = b
b = temp
```

### La Soluzione Pythonica: Assegnamento Parallelo

```python
# Elegante
a = 1
b = 2
a, b = b, a  # Scambio in una riga!

print(a, b)  # Output: 2 1
```

### Invertire una Lista Manualmente

```python
numeri = [1, 2, 3, 4, 5]

# Versione semplice
numeri[0], numeri[4] = numeri[4], numeri[0]
numeri[1], numeri[3] = numeri[3], numeri[1]

print(numeri)  # Output: [5, 4, 3, 2, 1]
```

### Versione Automatica: Loop che Scala

```python
numeri = [10, 1, 8, 3, 5]
lunghezza = len(numeri)

for i in range(lunghezza // 2):
    numeri[i], numeri[lunghezza - i - 1] = numeri[lunghezza - i - 1], numeri[i]

print(numeri)  # Output: [5, 3, 8, 1, 10]
```

Come funziona:
- `lunghezza // 2` itera solo metà della lista (l'altra metà si scambia naturalmente)
- `lunghezza - i - 1` dà l'indice "specchio" (per i=0, dà 4; per i=1, dà 3)

### Nota sulla Lunghezza Dispari

```python
numeri = [1, 2, 3, 4, 5]
lunghezza = 5

# range(lunghezza // 2) produce range(2) = [0, 1]
# Quindi scambia elementi 0-4 e 1-3
# L'elemento al centro (indice 2) rimane invariato
```

Geniale!

## Laboratorio 1: The Beatles

### Scenario

Create un programma che simula i cambiamenti nella lineup dei Beatles:

1. Crea una lista vuota
2. Aggiungi i tre membri originali (append)
3. Leggi da input due nuovi membri
4. Rimuovi due membri
5. Inserisci Ringo Starr all'inizio

### Soluzione Completa

```python
# Step 1: Lista vuota
beatles = []
print("Step 1:", beatles)  # Output: []

# Step 2: Aggiungi i tre originali
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)
# Output: ['John Lennon', 'Paul McCartney', 'George Harrison']

# Step 3: Loop per aggiungere da input
nomi_da_aggiungere = ["Stu Sutcliffe", "Pete Best"]
for nome in nomi_da_aggiungere:
    beatles.append(nome)
print("Step 3:", beatles)
# Output: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe', 'Pete Best']

# Step 4: Rimuovi i due ultimi
beatles.pop()  # Rimuove Pete Best
beatles.pop()  # Rimuove Stu Sutcliffe
print("Step 4:", beatles)
# Output: ['John Lennon', 'Paul McCartney', 'George Harrison']

# Step 5: Inserisci Ringo all'inizio
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)
# Output: ['Ringo Starr', 'John Lennon', 'Paul McCartney', 'George Harrison']

# Finale
print("The Fab", len(beatles))
# Output: The Fab 4
```

## Laboratorio 2: Ordinamento Semplice

### Scenario

Leggete 5 numeri e ordinate dal più piccolo al più grande.

### Soluzione

```python
numeri = []

print("Inserisci 5 numeri:")
for i in range(5):
    numero = int(input(f"Numero {i+1}: "))
    numeri.append(numero)

print("\nListaOriginale:", numeri)

# Metodo 1: Usare sort()
numeri.sort()
print("Lista Ordinata:", numeri)

# Metodo 2: Usare sorted() (per ottenere copia)
numeri_originali = [3, 1, 4, 1, 5]
ordinati = sorted(numeri_originali)
print("Ordinati:", ordinati)
print("Originali (inalterati):", numeri_originali)
```

## Laboratorio 3: Trovare il Massimo e il Minimo

### Scenario

Create un programma che trovate il numero più grande e più piccolo in una lista.

### Soluzione Manuale

```python
numeri = [3, 7, 2, 9, 1, 5]

massimo = numeri[0]
minimo = numeri[0]

for numero in numeri:
    if numero > massimo:
        massimo = numero
    if numero < minimo:
        minimo = numero

print(f"Massimo: {massimo}")  # Output: 9
print(f"Minimo: {minimo}")    # Output: 1
```

### Soluzione Built-in

```python
numeri = [3, 7, 2, 9, 1, 5]

print(f"Massimo: {max(numeri)}")  # Output: 9
print(f"Minimo: {min(numeri)}")   # Output: 1
print(f"Somma: {sum(numeri)}")    # Output: 27
```

Python ha funzioni built-in per questi compiti comuni.

## Conclusione: Le Liste Come Fondamento

Le liste sono il **fondamento** della programmazione Python. Praticamente ogni programma utile usa liste.

✅ **Memorizzare dati multipli** – Una variabile, molti valori
✅ **Accedere dinamicamente** – Per indice, con loop, negativamente
✅ **Modificare dinamicamente** – append, insert, remove, pop
✅ **Ordinare e manipolare** – sort, reverse, count, index
✅ **Iterare efficientemente** – for loops che scalano a liste di qualsiasi lunghezza

Avete imparato il concetto più importante della programmazione oltre alla sintassi: **come gestire collezioni di dati**.

Nei capitoli successivi, vedrete che liste possono contenere altre liste (nested lists), possono essere elaborate con list comprehensions, e sono la base per database e strutture dati più complesse.

Per ora, praticate con i laboratori. Scrivete programmi che creano liste, le modificano, le ordinano, le processano. Sperimentate con diversi metodi. Capite l'indice da zero—è la fondazione di tutto il resto della programmazione.