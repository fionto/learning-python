# Capitolo 3: Sezione 3.7 - Liste Avanzate: Comprehensions e Matrici

## Introduzione: Dalla Semplicità alla Complessità

Finora, abbiamo trattato liste di numeri semplici. Ma Python permette strutture molto più potenti: **liste di liste**, che rappresentano **matrici**, **tabelle**, e persino **spazi 3D**. In questa sezione, imparerete due abilità fondamentali:

1. **List Comprehensions**: Modo elegante e Pythonic di creare liste
2. **Liste Multidimensionali**: Come modellare dati complessi (tabelle, scacchiere, hotel)

Iniziamo con una sintassi potente che renderà il vostro codice più conciso e leggibile.

## 3.7.1 List Comprehensions: Creare Liste in Una Riga

### Il Problema: Codice Ripetitivo

Supponiamo volete creare una lista di 8 elementi, tutti uguali:

```python
# Metodo vecchio: noioso
riga = []
for i in range(8):
    riga.append(PEDONE_BIANCO)

# Risultato: [PEDONE_BIANCO, PEDONE_BIANCO, ..., PEDONE_BIANCO]
```

È efficiente, ma verboso. Python offre un modo migliore.

### La Soluzione: List Comprehension

```python
# Metodo nuovo: conciso
riga = [PEDONE_BIANCO for i in range(8)]
```

Leggete così: **"Crea una lista contenente PEDONE_BIANCO, ripetuto 8 volte"**.

### Sintassi Generale

```python
[espressione for variabile in iterabile]
```

Dove:
- **espressione**: Cosa mettere nella lista
- **variabile**: Nome della variabile di iterazione
- **iterabile**: Su cosa iterare (lista, range, ecc.)

### Esempi Progressivi

**Esempio 1: Quadrati da 0 a 9**

```python
quadrati = [x ** 2 for x in range(10)]
print(quadrati)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Esempio 2: Potenze di 2**

```python
potenze = [2 ** i for i in range(8)]
print(potenze)
# Output: [1, 2, 4, 8, 16, 32, 64, 128]
```

**Esempio 3: Stringhe Duplicate**

```python
nomi = ["Alice", "Bob", "Charlie"]
saluti = [f"Ciao, {nome}!" for nome in nomi]
print(saluti)
# Output: ['Ciao, Alice!', 'Ciao, Bob!', 'Ciao, Charlie!']
```

### List Comprehension con Condizione

Potete **filtrare** durante la creazione con una clausola `if`:

```python
[espressione for variabile in iterabile if condizione]
```

**Esempio: Solo Numeri Dispari**

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dispari = [x for x in numeri if x % 2 != 0]
print(dispari)
# Output: [1, 3, 5, 7, 9]
```

**Esempio: Quadrati degli Elementi Pari**

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrati_pari = [x ** 2 for x in numeri if x % 2 == 0]
print(quadrati_pari)
# Output: [0, 4, 16, 36, 64]
```

### List Comprehension con Ternario

Potete anche usare un'espressione condizionale **all'interno** della comprehension:

```python
[espressione_se_vero if condizione else espressione_se_falso for variabile in iterabile]
```

**Esempio: Convertire Numeri Pari a 'E', Dispari a 'D'**

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
etichette = ["E" if x % 2 == 0 else "D" for x in numeri]
print(etichette)
# Output: ['E', 'D', 'E', 'D', 'E', 'D', 'E', 'D', 'E', 'D']
```

### Perché Usare List Comprehensions?

**Vantaggi:**
1. **Concisione**: Una riga al posto di tre
2. **Leggibilità**: È chiaro cosa state facendo
3. **Performance**: Leggermente più veloce dei loop tradizionali
4. **Pythonic**: È il modo standard di fare in Python

```python
# Non-Pythonic
lista_nuova = []
for elemento in lista_vecchia:
    if elemento > 10:
        lista_nuova.append(elemento * 2)

# Pythonic
lista_nuova = [x * 2 for x in lista_vecchia if x > 10]
```

## 3.7.2 Liste Nidificate: Matrici 2D

### Il Concetto: Una Lista di Liste

Una **matrice 2D** è una lista che contiene altre liste come elementi:

```python
scacchiera = [
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 0
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 1
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 2
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 3
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 4
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 5
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 6
    [0, 0, 0, 0, 0, 0, 0, 0],  # Riga 7
]
```

### Creazione con Nested Loops

```python
VUOTO = 0

scacchiera = []

for riga in range(8):
    riga_nuova = [VUOTO for colonna in range(8)]
    scacchiera.append(riga_nuova)

print(scacchiera)
```

### Creazione con Nested List Comprehension

```python
VUOTO = 0

scacchiera = [[VUOTO for colonna in range(8)] for riga in range(8)]

print(scacchiera)
# Output: [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], ...]
```

Leggete come: **"Per ogni riga (0-7), crea una lista di 8 colonne vuote"**.

### Accesso a Elementi 2D

Per accedere a un elemento, usate **due indici**:

```python
scacchiera[riga][colonna]
```

**Esempio: Accedere alla posizione (3, 4)**

```python
valore = scacchiera[3][4]
```

**Visualizzazione:**

```
       0  1  2  3  4  5  6  7  (colonne)
    0  .  .  .  .  .  .  .  .
    1  .  .  .  .  .  .  .  .
    2  .  .  .  .  .  .  .  .
    3  .  .  .  .  X  .  .  .  ← scacchiera[3][4]
    4  .  .  .  .  .  .  .  .
    5  .  .  .  .  .  .  .  .
    6  .  .  .  .  .  .  .  .
    7  .  .  .  .  .  .  .  .
(righe)
```

### Modificare Elementi

```python
TORRE = 5
CAVALLO = 3
PEDONE = 1

# Aggiungere le torri negli angoli
scacchiera[0][0] = TORRE
scacchiera[0][7] = TORRE
scacchiera[7][0] = TORRE
scacchiera[7][7] = TORRE

# Aggiungere un cavallo in C4 (riga 4, colonna 2)
scacchiera[4][2] = CAVALLO

# Aggiungere un pedone in E5 (riga 3, colonna 4)
scacchiera[3][4] = PEDONE
```

## 3.7.3 Applicazioni Pratiche: Dati del Mondo Reale

### Applicazione 1: Temperatura Mensile

**Scenario**: Una stazione meteorologica registra la temperatura ogni ora per 31 giorni. Abbiamo 31 × 24 = 744 valori.

**Creazione della Matrice**:

```python
temperature = [[0.0 for ora in range(24)] for giorno in range(31)]
```

Struttura:
- Ogni **riga** = un giorno (0-30)
- Ogni **colonna** = un'ora (0-23)
- Ogni elemento = temperatura in °C

### Calcolare la Temperatura Media a Mezzogiorno

Mezzogiorno = ora 11 (0-indexed). Volete la media di `temperatura[0][11]` a `temperatura[30][11]`:

```python
# Ipotizziamo che la matrice sia già riempita con dati reali

totale = 0.0

for giorno in temperature:
    totale += giorno[11]  # Accedi alla temperatura a mezzogiorno di quel giorno

media = totale / 31
print(f"Temperatura media a mezzogiorno: {media}°C")
```

### Trovare la Temperatura Massima del Mese

```python
massima = -100.0  # Assumete un valore minore di qualsiasi temperatura

for giorno in temperature:
    for temp in giorno:
        if temp > massima:
            massima = temp

print(f"Temperatura massima: {massima}°C")
```

### Contare i Giorni "Caldi" (T ≥ 20°C a Mezzogiorno)

```python
giorni_caldi = 0

for giorno in temperature:
    if giorno[11] > 20.0:  # Se la temperatura a mezzogiorno > 20°C
        giorni_caldi += 1

print(f"{giorni_caldi} giorni sono stati caldi")
```

## 3.7.4 Tre Dimensioni: Array 3D

### Il Concetto: Una Lista di Liste di Liste

Python **non limita la profondità** di nidificazione. Potete avere 3D, 4D, persino più.

**Esempio: Un Hotel**

Immaginate un hotel con:
- 3 edifici
- 15 piani per edificio
- 20 stanze per piano

Creiate una **matrice 3D** per tracciare se le stanze sono occupate:

```python
stanze = [[[False for stanza in range(20)] for piano in range(15)] for edificio in range(3)]
```

### Struttura

```
stanze[edificio][piano][stanza]
```

Dove:
- **edificio**: 0-2
- **piano**: 0-14
- **stanza**: 0-19

### Accedere a Elementi 3D

**Prenotare una stanza**: Secondo edificio, decimo piano, stanza 14:

```python
stanze[1][9][13] = True  # True = occupato
```

**Liberare una stanza**: Primo edificio, quinto piano, stanza 2:

```python
stanze[0][4][1] = False  # False = libero
```

### Contare le Stanze Libere

**Quante stanze libere al 15° piano (indice 14) del terzo edificio (indice 2)?**

```python
libere = 0

for numero_stanza in range(20):
    if not stanze[2][14][numero_stanza]:  # Se NON occupato
        libere += 1

print(f"Stanze libere al 15° piano del 3° edificio: {libere}")
```

### Pattern Generale per N Dimensioni

Per una struttura **qualsiasi** di profondità N, usate **N indici**:

```python
# 1D
lista[i]

# 2D
matrice[i][j]

# 3D
cubo[i][j][k]

# ND
ipercubo[i1][i2][i3]...[in]
```

## Laboratorio 1: Crea una Scacchiera con List Comprehension

### Scenario

Crea una scacchiera 8×8 utilizzando **esclusivamente list comprehension**.

### Soluzione

```python
# Definire i pezzi
VUOTO = "."
PEDONE = "P"
TORRE = "R"
CAVALLO = "N"
ALFIERE = "B"
REGINA = "Q"
RE = "K"

# Creazione della scacchiera con list comprehension annidato
scacchiera = [[VUOTO for _ in range(8)] for _ in range(8)]

# Aggiungere i pezzi
# Torri
scacchiera[0][0] = TORRE
scacchiera[0][7] = TORRE

# Cavalli
scacchiera[0][1] = CAVALLO
scacchiera[0][6] = CAVALLO

# Alfieri
scacchiera[0][2] = ALFIERE
scacchiera[0][5] = ALFIERE

# Regina e Re
scacchiera[0][3] = REGINA
scacchiera[0][4] = RE

# Pedoni
for i in range(8):
    scacchiera[1][i] = PEDONE

# Stampa
for riga in scacchiera:
    print(" ".join(riga))
```

**Output:**
```
R N B Q K B N R
P P P P P P P P
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

## Laboratorio 2: Calcolare Statistiche su Matrice 2D

### Scenario

Date una matrice 3×3 di numeri, calcolare:
1. Somma totale
2. Media
3. Elemento massimo
4. Elemento minimo

### Soluzione

```python
dati = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Somma totale
totale = 0
for riga in dati:
    for numero in riga:
        totale += numero

# Media
media = totale / 9

# Massimo e minimo
massimo = dati[0][0]
minimo = dati[0][0]

for riga in dati:
    for numero in riga:
        if numero > massimo:
            massimo = numero
        if numero < minimo:
            minimo = numero

print(f"Somma: {totale}")
print(f"Media: {media}")
print(f"Massimo: {massimo}")
print(f"Minimo: {minimo}")
```

**Output:**
```
Somma: 450
Media: 50.0
Massimo: 90
Minimo: 10
```

## Laboratorio 3: Transpose una Matrice

### Scenario

Date una matrice 3×3, create la sua **trasposizione** (scambiare righe e colonne).

```
Originale:      Trasposizione:
1 2 3           1 4 7
4 5 6    -->    2 5 8
7 8 9           3 6 9
```

### Soluzione

```python
originale = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Metodo 1: Con loop
trasposta = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        trasposta[j][i] = originale[i][j]

# Stampa
print("Originale:")
for riga in originale:
    print(riga)

print("\nTrasposizione:")
for riga in trasposta:
    print(riga)
```

**Metodo 2: Con List Comprehension (Avanzato)**

```python
trasposta = [[originale[i][j] for i in range(3)] for j in range(3)]
```

## Laboratorio 4: Somma di Righe e Colonne

### Scenario

Date una matrice 4×4, calcolate:
1. La somma di ogni riga
2. La somma di ogni colonna

### Soluzione

```python
matrice = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Somma di ogni riga
somme_righe = []
for riga in matrice:
    somme_righe.append(sum(riga))

print("Somma righe:", somme_righe)
# Output: Somma righe: [10, 26, 42, 58]

# Somma di ogni colonna
somme_colonne = []
for j in range(4):
    somma_colonna = 0
    for i in range(4):
        somma_colonna += matrice[i][j]
    somme_colonne.append(somma_colonna)

print("Somma colonne:", somme_colonne)
# Output: Somma colonne: [28, 32, 36, 40]
```

**Versione con List Comprehension:**

```python
somme_righe = [sum(riga) for riga in matrice]

somme_colonne = [sum(matrice[i][j] for i in range(4)) for j in range(4)]

print("Somme righe:", somme_righe)
print("Somme colonne:", somme_colonne)
```

## Conclusione: Strutture Dati Complesse, Codice Elegante

Avete imparato:

✅ **List Comprehensions** – Modo conciso e Pythonic di creare liste
✅ **Matrici 2D** – Modellare tabelle, scacchiere, griglie
✅ **Matrici 3D e Oltre** – Strutture ancora più complesse
✅ **Applicazioni Pratiche** – Dati reali (temperature, hotel, scacchiere)
✅ **Nested Comprehensions** – Creare matrici in una sola riga

### Quando Usare List Comprehensions

```python
# Semplice trasformazione → List Comprehension
quadrati = [x ** 2 for x in range(10)]

# Con filtro → List Comprehension
pari = [x for x in range(10) if x % 2 == 0]

# Logica complessa → Loop tradizionale
risultati = []
for x in range(10):
    if x % 2 == 0:
        if x > 5:
            risultati.append(x ** 2)
```

### Quando Usare Matrici

```python
# Dati 2D (righe e colonne) → Matrice 2D
temperatura_mensile = [[temp for ora in range(24)] for giorno in range(31)]

# Dati 3D (x, y, z) → Matrice 3D
stanze_hotel = [[[False for stanza in range(20)] for piano in range(15)] for edificio in range(3)]
```

Avete completato il **Modulo 3**! Avete imparato a lavorare con liste in ogni forma: semplici, nidificate, con comprehensions, con algoritmi di ordinamento.

Nel prossimo modulo, imparerete come creare **funzioni riutilizzabili** e **organizzare il codice** in modo professionale.