# Capitolo 3: Sezione 3.6 - Operazioni su Liste: Slicing, Ricerca, e Applicazioni

## Introduzione: Le Liste Non Sono Variabili Semplici

Abbiamo imparato a manipolare liste. Ma c'è un concetto **cruciale** che distingue le liste dalle variabili ordinarie.

Vedrete presto che questa distinzione può causare **bug difficili da trovare** se non la capite bene.

Iniziamo con un esperimento che vi sorprenderà.

## 3.6.1 Il Problema della Copia: Aliasing vs Copia Profonda

### L'Esperimento Sorprendente

Eseguire questo codice:

```python
lista_1 = [1]
lista_2 = lista_1
lista_1[0] = 2

print(lista_2)  # Output: [2] (non [1]!)
```

**Aspettate [1], ma ottenete [2]. Perché?**

### La Spiegazione: Nomi vs Contenuti

Questa è la distinzione cruciale:

**Variabili scalari** (numeri, stringhe):
```python
x = 5
y = x
x = 10

print(y)  # Output: 5 (inalterato)
```

Il nome `y` è il nome del **contenuto**. Quando assegnate `y = x`, copiate il valore.

**Liste**:
```python
lista_1 = [1]
lista_2 = lista_1  # Copiate il NOME, non il contenuto!
lista_1[0] = 2

print(lista_2)  # Output: [2] (modificato!)
```

Il nome `lista_1` non è il nome della lista stessa. È il nome **dell'indirizzo di memoria dove la lista è immagazzinata**.

Quando fate `lista_2 = lista_1`, state copiando l'**indirizzo**, non il contenuto. Entrambi i nomi puntano alla stessa lista in memoria.

### Visualizzazione

```
Quello che vi aspettate:
lista_1 = [1]  →  Indirizzo A
lista_2 = [1]  →  Indirizzo B
(due liste separate)

Quello che realmente succede:
lista_1 = [1]  ↘
lista_2 = ????  ↗  Indirizzo A (stesso indirizzo!)
(un'unica lista, due nomi)
```

Modificare attraverso `lista_1` modifica anche `lista_2` perché sono lo stesso oggetto.

### Il Termine: Aliasing

Quando due variabili puntano allo stesso oggetto, si chiama **aliasing**. È una feature potente, ma può essere insidiosa.

```python
# Aliasing intenzionale
utente_principale = ["Alice", 25, "Milano"]
utente_alias = utente_principale  # Stesso oggetto

# Questo affetta entrambi
utente_principale[0] = "Alicia"
print(utente_alias)  # ["Alicia", 25, "Milano"]
```

## 3.6.2 La Soluzione: Slicing per Copiare

### Che Cos'è uno Slice?

Uno **slice** è una porzione di una lista. Ma quando usate slice per la copia, **crea una nuova lista** con i contenuti copiati.

```python
lista_1 = [1]
lista_2 = lista_1[:]  # [:] copia tutta la lista
lista_1[0] = 2

print(lista_2)  # Output: [1] (inalterato!)
```

La sintassi `[:]` significa **"dal primo elemento all'ultimo"**—cioè, tutta la lista. Ma crea una **nuova copia** piuttosto che un alias.

### Slice Syntax: `[start:end]`

La forma generale di uno slice è:

```python
new_list = my_list[start:end]
```

Dove:
- **start**: indice del **primo elemento incluso**
- **end**: indice del **primo elemento NON incluso** (importante!)

```python
numeri = [10, 8, 6, 4, 2]

slice_1 = numeri[1:3]  # Elementi agli indici 1 e 2
print(slice_1)         # Output: [8, 6]

slice_2 = numeri[0:2]  # Elementi agli indici 0 e 1
print(slice_2)         # Output: [10, 8]
```

### Visualizzazione della Regola end-1

```
Lista:      [10,  8,  6,  4,  2]
Indici:      0   1   2   3   4

numeri[1:3] prende indici 1 e 2 (non 3!)
            ↓      ↓
            [8,    6]
```

**Ricordate**: end è **esclusivo**—non viene incluso.

### Slicing con Indici Negativi

```python
numeri = [10, 8, 6, 4, 2]

slice_1 = numeri[1:-1]  # Da indice 1 all'indice -1 (esclusivo)
print(slice_1)          # Output: [8, 6, 4]

# Visualizzazione:
# numeri[1:-1] = numeri[1:4]
# Prende indici 1, 2, 3 (l'ultimo 2 è all'indice 4, che è escluso)
```

### Slice con Omissioni

**Omettere start** (inizia da 0):
```python
numeri = [10, 8, 6, 4, 2]
slice_1 = numeri[:3]  # Equivalente a numeri[0:3]
print(slice_1)        # Output: [10, 8, 6]
```

**Omettere end** (va fino alla fine):
```python
numeri = [10, 8, 6, 4, 2]
slice_1 = numeri[2:]  # Equivalente a numeri[2:5]
print(slice_1)        # Output: [6, 4, 2]
```

**Omettere entrambi** (copia intera lista):
```python
numeri = [10, 8, 6, 4, 2]
copia = numeri[:]  # Equivalente a numeri[0:5]
print(copia)       # Output: [10, 8, 6, 4, 2]
```

### Slice che Vanno "Al Contrario"

Se start è **dopo** end (verso la fine della lista), il slice è vuoto:

```python
numeri = [10, 8, 6, 4, 2]
slice_1 = numeri[-1:1]  # Indice -1 è dopo indice 1
print(slice_1)          # Output: [] (vuoto)
```

## 3.6.3 Cancellazione con Slicing: del

L'istruzione `del` può cancellare non solo singoli elementi, ma anche **slice interi**:

```python
numeri = [10, 8, 6, 4, 2]
del numeri[1:3]  # Cancella elementi agli indici 1 e 2

print(numeri)    # Output: [10, 4, 2]
```

**Nota importante**: `del numeri[1:3]` **cancella gli elementi**, non crea un nuovo slice. Modifica la lista originale.

### Cancellare Tutta la Lista (Contenuti)

```python
numeri = [10, 8, 6, 4, 2]
del numeri[:]  # Cancella TUTTI gli elementi

print(numeri)  # Output: []
```

### Cancellare la Variabile Stessa

```python
numeri = [10, 8, 6, 4, 2]
del numeri     # Cancella la VARIABILE stessa (non il contenuto)

print(numeri)  # ERRORE: NameError - numeri non esiste più
```

Questa è una distinzione importante: `del numeri[:]` svuota la lista, `del numeri` elimina la variabile.

## 3.6.4 Operatori di Membership: in e not in

### Che Cosa Sono?

L'operatore `in` verifica se un valore esiste in una lista:

```python
numeri = [0, 3, 12, 8, 2]

print(5 in numeri)      # Output: False
print(12 in numeri)     # Output: True
print(5 not in numeri)  # Output: True
```

### Sintassi

```python
elemento in lista      # Ritorna True se elemento è in lista
elemento not in lista  # Ritorna True se elemento NON è in lista
```

### Caso d'Uso Pratico: Controllo di Appartenenza

```python
colori_disponibili = ["rosso", "verde", "blu"]
colore_scelto = "giallo"

if colore_scelto in colori_disponibili:
    print("Colore disponibile")
else:
    print("Colore non disponibile")
# Output: Colore non disponibile
```

### Combinazione con Logica

```python
numeri = [1, 2, 3, 4, 5]

if 3 in numeri and 6 not in numeri:
    print("3 è presente, ma 6 no")
# Output: 3 è presente, ma 6 no
```

## 3.6.5 Applicazioni Pratiche: Programmi Semplici su Liste

### Programma 1: Trovare il Massimo

**Versione 1: Con indice**
```python
numeri = [17, 3, 11, 5, 1, 9, 7, 15, 13]
massimo = numeri[0]

for i in range(1, len(numeri)):
    if numeri[i] > massimo:
        massimo = numeri[i]

print(massimo)  # Output: 17
```

**Versione 2: Direttamente sui valori**
```python
numeri = [17, 3, 11, 5, 1, 9, 7, 15, 13]
massimo = numeri[0]

for numero in numeri:
    if numero > massimo:
        massimo = numero

print(massimo)  # Output: 17
```

**Versione 3: Con slice (evita il primo elemento)**
```python
numeri = [17, 3, 11, 5, 1, 9, 7, 15, 13]
massimo = numeri[0]

for numero in numeri[1:]:
    if numero > massimo:
        massimo = numero

print(massimo)  # Output: 17
```

**Nota**: La versione 1 fa una comparazione inutile (17 con se stesso). La versione 2 fa la stessa cosa ma è più leggibile. La versione 3 la evita, ma crea un slice (che costa risorse). Quale scegliere? **Dipende dal contesto**.

### Programma 2: Trovare la Posizione di un Elemento

```python
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
da_trovare = 5
trovato = False

for i in range(len(numeri)):
    if numeri[i] == da_trovare:
        trovato = True
        break

if trovato:
    print(f"Elemento trovato all'indice {i}")
else:
    print("Elemento assente")
# Output: Elemento trovato all'indice 4
```

**Nota**: Usiamo `break` per uscire dal loop non appena lo troviamo. Non c'è bisogno di continuare.

### Programma 3: Controllare Appartenenza (Semplificato)

Usando l'operatore `in`:

```python
numeri = [1, 2, 3, 4, 5]

if 3 in numeri:
    print("Elemento trovato")
else:
    print("Elemento assente")
# Output: Elemento trovato
```

Molto più semplice! Usate `in` quando volete solo verificare l'appartenenza, non la posizione.

### Programma 4: Loteria - Quanti Numeri Avete Indovinato?

```python
estratti = [5, 11, 9, 42, 3, 49]
scommesse = [3, 7, 11, 42, 34, 49]
vincite = 0

for numero in scommesse:
    if numero in estratti:
        vincite += 1

print(f"Numeri indovinati: {vincite}")
# Output: Numeri indovinati: 4
```

Questo mostra la **potenza dell'operatore `in`**: potete facilmente contare quanti elementi di una lista sono presenti in un'altra.

## Laboratorio 1: Rimuovere Duplicati

### Scenario

Date una lista con numeri ripetuti, create una nuova lista senza duplicati:

```
Input:  [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
Output: [1, 2, 4, 6, 9]
```

### Soluzione 1: Usando una Nuova Lista

```python
lista_originale = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_unica = []

for numero in lista_originale:
    if numero not in lista_unica:
        lista_unica.append(numero)

print("Lista originale:", lista_originale)
print("Lista senza duplicati:", lista_unica)
```

**Output:**
```
Lista originale: [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
Lista senza duplicati: [1, 2, 4, 6, 9]
```

### Soluzione 2: Più Elegante con Set (Preview)

```python
lista_originale = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_unica = list(set(lista_originale))

print("Lista senza duplicati:", lista_unica)
```

(Vedrai i set presto—sono collezioni senza duplicati per default.)

## Laboratorio 2: Confrontare Due Liste

### Scenario

Verificate quanti elementi di `lista_1` sono presenti in `lista_2`:

```python
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 4, 5, 6, 7]

# Quanti elementi di lista_1 sono in lista_2?
# Risposta: 3 (i numeri 3, 4, 5)
```

### Soluzione

```python
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 4, 5, 6, 7]
comuni = 0

for elemento in lista_1:
    if elemento in lista_2:
        comuni += 1

print(f"Elementi comuni: {comuni}")
# Output: Elementi comuni: 3
```

## Laboratorio 3: Reverse Senza Usare reverse()

### Scenario

Invertite una lista senza usare `.reverse()`:

### Soluzione

```python
numeri = [1, 2, 3, 4, 5]
invertiti = numeri[::-1]  # Slice con step -1

print(invertiti)
# Output: [5, 4, 3, 2, 1]
```

**Nota**: Lo slice `[::-1]` è una scorciatoia Pythonica per invertire. Significa "tutti gli elementi, ma in ordine inverso".

Versione manuale:
```python
numeri = [1, 2, 3, 4, 5]
invertiti = []

for i in range(len(numeri) - 1, -1, -1):
    invertiti.append(numeri[i])

print(invertiti)
# Output: [5, 4, 3, 2, 1]
```

## Laboratorio 4: Filtrare una Lista

### Scenario

Create una nuova lista contenente solo gli elementi che soddisfano una condizione:

```python
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Vogliamo solo i pari
```

### Soluzione

```python
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = []

for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)

print(pari)
# Output: [2, 4, 6, 8, 10]
```

**Alternativa con List Comprehension** (vedrai presto):
```python
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = [n for n in numeri if n % 2 == 0]

print(pari)
# Output: [2, 4, 6, 8, 10]
```

## Conclusione: Liste Come Strutture Dati Potenti

Avete imparato:

✅ **Aliasing**: Come le liste puntano a indirizzi di memoria, non a valori
✅ **Slicing**: Come copiare liste e selezionare porzioni
✅ **Operatori di membership**: `in` e `not in` per verificare l'appartenenza
✅ **Applicazioni pratiche**: Trovare massimi, filtrare, confrontare liste

Le liste sono una **struttura dati fondamentale**. Capire come copiarle, sliciarle, e cercarle è cruciale.

Nel prossimo capitolo, vedrete techniche ancora più avanzate (list comprehensions, funzioni su liste, ecc.). Ma il fondamento che avete imparato qui è sufficiente per risolvere molti problemi reali.

Praticate con i laboratori. Sperimentate con slice diversi. Usate `in` e `not in` frequentemente. Diventate fluenti nella manipolazione di liste—è una competenza che userete **ogni giorno** come programmatore.