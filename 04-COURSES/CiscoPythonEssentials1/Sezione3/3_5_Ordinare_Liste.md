# Capitolo 3: Sezione 3.5 - Bubble Sort: Imparare a Ordinare

## Introduzione: Ordinare è Difficile?

Abbiamo imparato a manipolare liste. Abbiamo imparato a scambiare elementi. Ma come ordinamo veramente una lista?

Python ha `sort()`, è vero. Potete usarlo così:

```python
numeri = [8, 10, 6, 2, 4]
numeri.sort()
print(numeri)  # Output: [2, 4, 6, 8, 10]
```

Fine della storia.

Ma questo è **barare**. Non imparerete **come** funziona l'ordinamento. Non capirete i principi dietro questa magia.

In questa sezione, imparerete a **scrivere il vostro ordinamento da zero**. Non sarà il più veloce—è lento, in realtà. Ma è facile da capire e mostra i **principi fondamentali** di come gli algoritmi processano i dati.

Questo vi preparerà per algoritmi più avanzati e vi insegnerà a **pensare algoritmicamente**.

### L'Analogia: Ordinare le Persone in una Fila

Immaginate che volete ordinare un gruppo di persone per altezza, da più bassa a più alta. Come lo fate?

Un approccio semplice: guardate le prime due persone. Se sono nel ordine sbagliato (la prima è più alta della seconda), le scambiate. Poi guardare le second e terza, le scambiate se necessario. Continuate finché non raggiungete la fine.

Quando raggiungete la fine, una cosa curiosa è accaduta: la **persona più alta è finita alla fine della fila**—il posto dove dovrebbe essere.

Ripetete il processo. La prossima volta, la persona più alta avrà già raggiunto il fondo, quindi dovete solo ordinare il resto. Continuate finché non è tutto ordinato.

Questo, in essenza, è il Bubble Sort.

## 3.5.1 L'Algoritmo Bubble Sort: La Metafora della Bolla

### Il Concetto: Bubbles che Salgono

Il nome "Bubble Sort" viene da un'analogia visiva. Immaginate il vostro array scritto **verticalmente**:

```
Prima del Bubble Sort:
8
10
6
2
4

Dopo il primo "pass":
8
6
2
4
10  ← Il 10 è "galleggiato" al top!
```

Il numero più grande galleggia verso l'alto come una bolla in un bicchiere di champagne. Da qui il nome.

### Il Processo Dettagliato: Un Primo Esempio

Partiamo con questa lista:

```
[8, 10, 6, 2, 4]
```

**Pass 1 (primo passaggio):**

Confrontiamo coppie adiacenti da sinistra a destra:

1. **8 e 10**: 8 < 10? Sì. Nessuno scambio. `[8, 10, 6, 2, 4]`
2. **10 e 6**: 10 > 6? Sì. Scambiamo. `[8, 6, 10, 2, 4]`
3. **10 e 2**: 10 > 2? Sì. Scambiamo. `[8, 6, 2, 10, 4]`
4. **10 e 4**: 10 > 4? Sì. Scambiamo. `[8, 6, 2, 4, 10]`

**Osservazione cruciale**: Il 10 (il più grande) è finito al fondo. È **al suo posto finale**.

**Pass 2:**

Ricominciano dalle coppie:

1. **8 e 6**: 8 > 6? Sì. Scambiamo. `[6, 8, 2, 4, 10]`
2. **8 e 2**: 8 > 2? Sì. Scambiamo. `[6, 2, 8, 4, 10]`
3. **8 e 4**: 8 > 4? Sì. Scambiamo. `[6, 2, 4, 8, 10]`

Il 10 rimane dov'è (già al suo posto). Il 8 è ora al suo posto finale.

**Pass 3:**

1. **6 e 2**: 6 > 2? Sì. Scambiamo. `[2, 6, 4, 8, 10]`
2. **6 e 4**: 6 > 4? Sì. Scambiamo. `[2, 4, 6, 8, 10]`

Il 6 è al suo posto.

**Pass 4:**

1. **2 e 4**: 2 < 4? Sì. Nessuno scambio. `[2, 4, 6, 8, 10]`

Nessun scambio è accaduto! La lista è ordinata.

### Principio Fondamentale

L'idea è semplice: **Confrontate elementi adiacenti e scambiateli se sono nel ordine sbagliato. Ripetete finché non ci sono più scambi.**

## 3.5.2 Implementazione: Un Singolo Pass

Iniziamo a codificare un **singolo pass**:

```python
my_list = [8, 10, 6, 2, 4]

# Un singolo pass: confronta ogni coppia adiacente
for i in range(len(my_list) - 1):  # Iteriamo 4 volte (5-1)
    if my_list[i] > my_list[i + 1]:  # Elemento corrente > elemento successivo?
        # Scambia
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)  # Output: [8, 6, 2, 4, 10]
```

### Perché `range(len(my_list) - 1)`?

Con 5 elementi (indici 0-4), abbiamo 4 coppie da confrontare:
- (0, 1), (1, 2), (2, 3), (3, 4)

Se iterassimo fino a 5, cercheremmo di accedere a `my_list[5]`, che non esiste (IndexError).

`range(len(my_list) - 1)` produce `range(4)`, che è esatto.

### Un Singolo Pass Non Basta

Un pass ordina solo **parzialmente**. Nel nostro esempio, dopo un pass abbiamo `[8, 6, 2, 4, 10]`—ancora non è ordinato.

Dobbiamo ripetere i pass.

## 3.5.3 L'Algoritmo Completo: Ripetere Finché Ordinato

Come sappiamo quando smettere? **Quando un pass completo non fa scambi**.

Se in un intero pass non scambiate nulla, significa che la lista è già ordinata. Non dovete fare altro.

Codifichiamo questa logica:

```python
my_list = [8, 10, 6, 2, 4]
swapped = True  # Flag per tracciare se c'è stato uno scambio

while swapped:
    swapped = False  # Assumiamo che non ci siano scambi
    
    # Un pass completo
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # Un scambio è accaduto!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)  # Output: [2, 4, 6, 8, 10]
```

### Come Funziona

1. **Inizializzate `swapped = True`** per entrare nel loop (senza di ciò, non entrereste mai)
2. **Ogni iterazione del `while`**: settate `swapped = False`
3. **Nel `for` loop**: se fate uno scambio, settate `swapped = True`
4. **Dopo il `for` loop**: se `swapped` è ancora `False`, nessuno scambio è accaduto—la lista è ordinata. Uscite dal `while`

### Tracciamento dell'Esecuzione

Proviamo il codice sopra:

```
Stato iniziale: [8, 10, 6, 2, 4]

While Iteration 1:
  swapped = False
  Pass 1: [8, 6, 2, 4, 10]  (swapped = True)
  Continua il while

While Iteration 2:
  swapped = False
  Pass 2: [6, 2, 4, 8, 10]  (swapped = True)
  Continua il while

While Iteration 3:
  swapped = False
  Pass 3: [2, 4, 6, 8, 10]  (swapped = True)
  Continua il while

While Iteration 4:
  swapped = False
  Pass 4: [2, 4, 6, 8, 10]  (swapped = False, nessuno scambio)
  Esci dal while

Risultato finale: [2, 4, 6, 8, 10]
```

## 3.5.4 Ottimizzazione: Una Versione Più Intelligente

C'è un'ottimizzazione: **dopo ogni pass, un elemento in più è già al suo posto**. Non dovete controllarlo di nuovo.

```python
my_list = [8, 10, 6, 2, 4]

for passnum in range(len(my_list) - 1):
    for i in range(len(my_list) - 1 - passnum):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
```

L'idea: nel primo pass, controllate tutte le 4 coppie. Nel secondo pass, controllate solo le prime 3 (il 10 è già al posto). Nel terzo, le prime 2, ecc.

Questo è **leggermente più veloce**, ma la logica del `while swapped` è più elegante e intuitiva.

## 3.5.5 Versione Interattiva: Bubble Sort Pratico

Combiniamo il bubble sort con input utente:

```python
my_list = []
num = int(input("Quanti elementi vuoi ordinare? "))

# Leggi gli elementi
for i in range(num):
    val = float(input(f"Elemento {i + 1}: "))
    my_list.append(val)

print(f"\nLista originale: {my_list}")

# Bubble sort
swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f"Lista ordinata: {my_list}")
```

### Test

```
Quanti elementi vuoi ordinare? 5
Elemento 1: 8
Elemento 2: 10
Elemento 3: 6
Elemento 4: 2
Elemento 5: 4

Lista originale: [8.0, 10.0, 6.0, 2.0, 4.0]
Lista ordinata: [2.0, 4.0, 6.0, 8.0, 10.0]
```

## 3.5.6 Limitazioni del Bubble Sort

### È Lento

Bubble Sort ha una complessità di **O(n²)**. Per 1000 elementi, farà circa 1.000.000 di confronti.

Per 100.000 elementi, farà 10 miliardi di confronti. Inaccettabile.

### Quando è Utile

1. **Educativo**: Imparare come funzionano gli algoritmi
2. **Piccole liste**: Se avete solo 5-10 elementi, è abbastanza veloce
3. **Liste quasi ordinate**: Se la lista è quasi ordinata, il `while swapped` lo nota e esce velocemente

### Algoritmi Migliori

Python usa **Timsort** (una combinazione di merge sort e insertion sort). È complesso, ma molto veloce.

```python
my_list = [8, 10, 6, 2, 4]
my_list.sort()  # Usa Timsort internamente
print(my_list)  # [2, 4, 6, 8, 10]
```

**Morale**: Non scrivete mai bubble sort in codice di produzione. Usate `sort()` o `sorted()`.

Ma imparare bubble sort vi insegna come gli algoritmi **pensano** ai dati.

## Laboratorio 1: Implementare Bubble Sort Puro

### Scenario

Implementate il bubble sort esattamente come descritto, senza ottimizzazioni.

### Soluzione

```python
numeri = [64, 34, 25, 12, 22, 11, 90]

print(f"Lista originale: {numeri}")

# Bubble Sort
swapped = True
while swapped:
    swapped = False
    for i in range(len(numeri) - 1):
        if numeri[i] > numeri[i + 1]:
            swapped = True
            numeri[i], numeri[i + 1] = numeri[i + 1], numeri[i]

print(f"Lista ordinata: {numeri}")
```

### Output

```
Lista originale: [64, 34, 25, 12, 22, 11, 90]
Lista ordinata: [11, 12, 22, 25, 34, 64, 90]
```

## Laboratorio 2: Bubble Sort con Conteggio dei Pass

### Scenario

Modificate il bubble sort per contare **quanti pass** sono necessari.

### Soluzione

```python
numeri = [8, 10, 6, 2, 4]

print(f"Lista originale: {numeri}")

swapped = True
pass_count = 0

while swapped:
    swapped = False
    pass_count += 1
    print(f"\nPass {pass_count}:")
    
    for i in range(len(numeri) - 1):
        if numeri[i] > numeri[i + 1]:
            swapped = True
            numeri[i], numeri[i + 1] = numeri[i + 1], numeri[i]
    
    print(f"  Dopo: {numeri}")

print(f"\nLista ordinata: {numeri}")
print(f"Necessari {pass_count} pass per ordinare")
```

### Output

```
Lista originale: [8, 10, 6, 2, 4]

Pass 1:
  Dopo: [8, 6, 2, 4, 10]

Pass 2:
  Dopo: [6, 2, 4, 8, 10]

Pass 3:
  Dopo: [2, 4, 6, 8, 10]

Pass 4:
  Dopo: [2, 4, 6, 8, 10]

Lista ordinata: [2, 4, 6, 8, 10]
Necessari 4 pass per ordinare
```

## Laboratorio 3: Bubble Sort per Stringhe

### Scenario

Usate bubble sort per ordinare stringhe alfabeticamente.

### Soluzione

```python
nomi = ["Zoe", "Alice", "Bob", "Charlie"]

print(f"Lista originale: {nomi}")

swapped = True
while swapped:
    swapped = False
    for i in range(len(nomi) - 1):
        if nomi[i] > nomi[i + 1]:  # Confronto lessicografico
            swapped = True
            nomi[i], nomi[i + 1] = nomi[i + 1], nomi[i]

print(f"Lista ordinata: {nomi}")
```

### Output

```
Lista originale: ['Zoe', 'Alice', 'Bob', 'Charlie']
Lista ordinata: ['Alice', 'Bob', 'Charlie', 'Zoe']
```

**Nota**: Python confronta stringhe **lessicograficamente** (come in un dizionario). Maiuscole vengono prima di minuscole per il default.

## Laboratorio 4: Ordinamento Decrescente

### Scenario

Modificate il bubble sort per ordinare dal più grande al più piccolo.

### Soluzione

```python
numeri = [8, 10, 6, 2, 4]

print(f"Lista originale: {numeri}")

swapped = True
while swapped:
    swapped = False
    for i in range(len(numeri) - 1):
        if numeri[i] < numeri[i + 1]:  # Invertite il confronto
            swapped = True
            numeri[i], numeri[i + 1] = numeri[i + 1], numeri[i]

print(f"Lista ordinata (decrescente): {numeri}")
```

### Output

```
Lista originale: [8, 10, 6, 2, 4]
Lista ordinata (decrescente): [10, 8, 6, 4, 2]
```

## Conclusione: Bubble Sort Come Insegnamento

Bubble Sort non è pratico per codice di produzione. Ma è **cruciale per comprensione algoritmica**.

Avete imparato:

✅ **Come funzionano gli algoritmi** – Step by step
✅ **Confronto di elementi** – Il blocco di costruzione di molti algoritmi
✅ **Flag per tracciamento di stato** – Pattern comune in programmazione
✅ **Ottimizzazione** – Quando smettere (nessuno scambio = lista ordinata)
✅ **Ordine crescente vs decrescente** – Semplice inversione della logica

Nel vostro futuro di programmatore, non scriverete bubble sort. Userete `sort()` di Python o algoritmi più sofisticati.

Ma la comprensione di come bubble sort funziona vi aiuterà a:
- Debuggare algoritmi complessi
- Capire la complessità temporale
- Pensare in termini di iterazione e confronto
- Apprezzare algoritmi più veloci

Bubble Sort è una "porta d'ingresso" al pensiero algoritmico. Non è la destinazione—è il primo passo del viaggio.

Praticate variazioni di bubble sort (ordinamento per stringhe, ordinamento decrescente, conteggio dei pass). Capite **perché** funziona. Solo allora potete progredire verso algoritmi più avanzati.