# Day 03: For Loops, Slicing e Manipolazione di Liste e Stringhe

**Data**: 31/12/2025  
**Argomento**: Python Crash Course - Capitolo 4 (Working with Lists)  
**Esercizi completati**: 14

---

## Concetti Fondamentali Appresi

### 1. Il For Loop

Il `for` loop permette di iterare su sequenze (liste, stringhe, range) senza dover usare indici e condizioni di stop manualmente.

**Sintassi di base:**
```python
for elemento in sequenza:
    # codice da eseguire per ogni elemento
```

L'elemento assunto dal loop è una variabile che cambia ad ogni iterazione, prendendo il valore di ogni elemento della sequenza.

**Esempio:**
```python
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)
```

### 2. Accumulazione con For Loop

Un pattern fondamentale è l'accumulazione: creare una variabile che accumula risultati man mano che si itera.

```python
numeri = [2, 5, 8, 12, 3]
somma = 0  # Variabile accumulatore

for numero in numeri:
    somma = somma + numero  # Accumula il valore

print(somma)  # 30
```

### 3. Range Objects vs Liste

Un **range** è un oggetto iterabile che rappresenta una sequenza di numeri senza memorizzarli tutti in memoria. È una "ricetta" che genera numeri al bisogno.

Una **lista** è una sequenza concreta: tutti gli elementi sono memorizzati.

**Differenza pratica:**
```python
lista = [0, 1, 2, 3, 4, 5]  # Memorizza 6 elementi
range_obj = range(6)         # Genera al bisogno

# Entrambi possono essere usati nei for loop
for i in lista:
    print(i)

for i in range_obj:
    print(i)  # Stesso output, meno memoria
```

**Conversione:**
```python
lista = list(range(6))  # [0, 1, 2, 3, 4, 5]
```

### 4. Range con Parametri: start, stop, step

```python
range(stop)              # range(5) = 0, 1, 2, 3, 4
range(start, stop)       # range(2, 7) = 2, 3, 4, 5, 6
range(start, stop, step) # range(0, 10, 2) = 0, 2, 4, 6, 8
```

Lo **step** può essere negativo per andare all'indietro:
```python
range(5, 0, -1)  # 5, 4, 3, 2, 1
```

### 5. Range con Underscores per Leggibilità

Per numeri grandi, puoi usare underscores per separare le cifre (non influenzano il valore):
```python
numeri = range(0, 1_000_001)  # Un milione + 1
```

### 6. Iterabili e Oggetti Iterabili

Un **iterabile** è una sequenza su cui si può fare un loop. Esempi: liste, stringhe, range, reversed objects.

Un **oggetto iterabile** non materializza tutti i valori in memoria, ma li genera al bisogno. Esempi: `range()`, `reversed()`, oggetti generatori.

```python
reversed(range(5))  # È un oggetto iterabile (reversed object)
list(reversed(range(5)))  # Lo converte in lista concreta
```

### 7. Reversed Objects

`reversed()` ritorna un oggetto iterabile che genera elementi in ordine inverso. Funziona su qualsiasi sequenza.

```python
stringa = "python"
for lettera in reversed(stringa):
    print(lettera)  # Stampa: n, o, h, t, y, p
```

Per vedere gli elementi, converti a lista:
```python
reversed_list = list(reversed(range(5)))  # [4, 3, 2, 1, 0]
```

---

## Slicing: Estrarre Porzioni di Sequenze

Lo **slicing** permette di estrarre una sottosezione da una sequenza usando la notazione `[start:stop:step]`.

### Sintassi Base

```python
sequenza[start:stop:step]
```

- `start`: Indice di inizio (incluso, default 0)
- `stop`: Indice di fine (escluso, default fine sequenza)
- `step`: Incremento (default 1)

### Esempi Comuni

```python
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista[2:5]      # [2, 3, 4] - Dall'indice 2 al 4
lista[:3]       # [0, 1, 2] - Primi 3 elementi
lista[7:]       # [7, 8, 9] - Ultimi 3 elementi
lista[-3:]      # [7, 8, 9] - Ultimi 3 elementi (con indici negativi)
lista[::2]      # [0, 2, 4, 6, 8] - Ogni 2 elementi
lista[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Inverso completo
```

### Slicing con Stringhe

Le stringhe sono sequenze, quindi lo slicing funziona allo stesso modo:

```python
stringa = "python"
stringa[2:5]    # "tho"
stringa[::-1]   # "nohtyp" - Stringa invertita
```

### Copia di Liste con Slicing

Il slicing crea una **nuova lista** (copia), non un alias:

```python
originale = [1, 2, 3]
copia = originale[:]  # Copia intera lista

copia.append(4)
print(originale)  # [1, 2, 3] - Non modificata
print(copia)      # [1, 2, 3, 4] - Modificata
```

Senza slicing, assegneresti solo un alias:
```python
originale = [1, 2, 3]
alias = originale  # Punta alla stessa lista

alias.append(4)
print(originale)  # [1, 2, 3, 4] - Modificata!
```

---

## Metodi Utili per Stringhe e Liste

### Stringhe

- `stringa.capitalize()`: Prima lettera maiuscola, resto minuscolo
  ```python
  "python".capitalize()  # "Python"
  ```

- `stringa.title()`: Prima lettera di ogni parola maiuscola
  ```python
  "hello world".title()  # "Hello World"
  ```

- `len(stringa)`: Lunghezza della stringa
  ```python
  len("python")  # 6
  ```

### Liste

- `lista.append(elemento)`: Aggiunge elemento alla fine
- `len(lista)`: Numero di elementi
- `lista[:]`: Crea copia della lista

### Funzioni Built-in

- `min(sequenza)`: Valore minimo
- `max(sequenza)`: Valore massimo
- `sum(sequenza)`: Somma di tutti gli elementi

```python
numeri = range(0, 1_000_001)
print(min(numeri))  # 0
print(max(numeri))  # 1_000_000
print(sum(numeri))  # 500_000_500_000
```

---

## F-String Formatting

Le f-string permettono di inserire variabili direttamente nella stringa con la sintassi `f"{variabile}"`.

```python
nome = "python"
lunghezza = len(nome)
print(f"{nome} ha {lunghezza} lettere")  # "python ha 6 lettere"
```

Puoi anche applicare metodi direttamente:
```python
print(f"{nome.capitalize()} ha {lunghezza} lettere")  # "Python ha 6 lettere"
```

---

## Loop Nidificati

Un **loop nidificato** è un loop dentro un altro loop. Il loop interno scorre completamente per ogni iterazione del loop esterno.

```python
for moltiplicando in range(1, 6):
    for moltiplicatore in range(1, 6):
        prodotto = moltiplicando * moltiplicatore
        print(f"{moltiplicando} x {moltiplicatore} = {prodotto}")
```

Il loop interno (moltiplicatore) completa tutte le 5 iterazioni per ogni valore del loop esterno (moltiplicando). Risultato: 5 × 5 = 25 righe stampate.

---

## PEP8 e Formattazione del Codice

### Limiti di Lunghezza Linea

PEP8 consiglia di mantenere le linee sotto i 79-80 caratteri per leggibilità.

### Spezzare Liste Lunghe

Usa le parentesi per spezzare senza backslash:

```python
# ✓ Buono
playlist = [
    "Song 1",
    "Song 2",
    "Song 3",
]

# Virgola finale è best practice per Git diffs più puliti
```

### Spezzare Stringhe Lunghe

Le stringhe letterali adiacenti vengono concatenate automaticamente:

```python
messaggio = ("Questo è un messaggio molto lungo "
             "che si estende su più linee")
```

### Spezzare Print Statements

```python
print(
    "^ nome_due è rimasta invariata perché "
    "nome_uno ora punta a un nuovo oggetto"
)
```

---

## Riepilogo Esercizi Completati

| Esercizio | Concetti | Output |
|-----------|----------|--------|
| 01 | Accumulazione con loop | Somma di sequenza |
| 02-05 | Reversed, slicing, iterabili | Stringhe invertite (4 metodi) |
| 06 | Metodo `.title()`, f-string | Lunghezze stringhe formattate |
| 07 | Loop nidificati | Tabelline 5×5 |
| 08 | Slicing negativo, accumulazione | Somma ultimi 3 elementi |
| 09 | Range con step, `min()`, `max()`, `sum()` | Statistiche numeri |
| 10 | Range con step 2 | Numeri dispari |
| 11 | Range con step 3 | Multipli di 3 |
| 12 | Operatore `**` (potenza) | Cubi di numeri |
| 13 | Slicing positivo e negativo | Sezioni di lista |
| 14 | Copia con slicing vs aliasing | Dimostrazione mutabilità liste |

---

## Punti Chiave da Ricordare

1. **For loop**: Usa per iterare su sequenze, non su indici numerici
2. **Range**: Non memorizza valori, genera al bisogno
3. **Slicing**: Crea nuove sequenze, utile per copie e sottoinsiemi
4. **F-string**: Modo moderno e leggibile per formattare stringhe
5. **Reversed objects**: Generano valori inversi senza materializzare
6. **Loop nidificati**: Il loop interno completa per ogni iterazione dell'esterno
7. **PEP8**: Linee < 80 caratteri, parentesi per spezzare, virgola finale nelle liste

---

## Prossimo Passo

Capitolo 5: If Statements (Condizionali) - Permetteranno di scrivere logica decisionale nei programmi, essenziale per filtri e controlli nei loop.
