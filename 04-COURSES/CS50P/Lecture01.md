# 📓 Riassunto Lezione 1: Condizionali (Conditionals)
**Video:** [Conditionals - CS50P](https://www.youtube.com/watch?v=_b6NgY_pMdw)

## 1. Introduzione alla Logica [00:00:00]
I condizionali permettono al computer di eseguire istruzioni diverse in base a determinate condizioni (True/False). Questo rende il codice dinamico e capace di rispondere agli input.

## 2. Operatori di Comparazione [00:04:30]
Simboli fondamentali per testare le relazioni tra i dati:
- `> ` : Maggiore
- `>=` : Maggiore o uguale
- `< ` : Minore
- `<=` : Minore o uguale
- `==` : Uguale a (confronto di uguaglianza)
- `!=` : Diverso da

## 3. Strutture Decisionali: If, Elif, Else [00:05:30]
La gerarchia delle condizioni è fondamentale per l'efficienza del codice:

### 3.1 If e l'efficienza degli Elif [00:15:20]
Usare una serie di `if` indipendenti costringe Python a controllarli tutti. Usando `elif` (else if), Python interrompe i controlli non appena trova la prima condizione vera, risparmiando cicli di calcolo.

```python
if x < y:
    print("x è minore di y")
elif x > y:
    print("x è maggiore di y")
else:
    print("x è uguale a y")
```

### 3.2 Il ruolo di Else [00:20:00]
`else` agisce come un caso di default. Non richiede una condizione esplicita perché cattura tutto ciò che non è stato gestito dai blocchi precedenti.

## 4. Operatori Logici e Semplificazioni [00:26:40]
### 4.1 OR e AND
- `or`: Vero se almeno una condizione è soddisfatta.
- `and`: Vero solo se tutte le condizioni sono soddisfatte. [00:46:15]

### 4.2 Concatenazione delle Comparazioni [00:48:30]
In Python è possibile concatenare gli operatori come in matematica, rendendo il codice estremamente leggibile:
```python
# Invece di: if score >= 90 and score <= 100:
if 90 <= score <= 100:
    print("Voto: A")
```

## 5. Modulo (%) e Parità [01:00:00]
L'operatore modulo `%` restituisce il resto di una divisione. È lo strumento standard per determinare se un numero è pari o dispari:
- `n % 2 == 0` -> Il numero è Pari.
- `n % 2 != 0` -> Il numero è Dispari.

## 6. L'Eleganza del "Boolean Return" [01:14:10]
Malan mostra come scrivere funzioni "Pythonic". Poiché un'espressione di confronto è già di per sé un valore booleano, non serve racchiuderla in un `if/else` per restituire `True` o `False`.

**Approccio Principiante:**
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

**Approccio Professionale (Senior):** [01:18:20]
```python
def is_even(n):
    return n % 2 == 0
```
*Teoria:* La funzione valuta `n % 2 == 0` e restituisce immediatamente il risultato della valutazione (True o False).

## 7. Il Costrutto Match (Python 3.10+) [01:21:50]
Alternativa moderna e pulita alle catene di `elif` quando si confronta una singola variabile con valori multipli.

```python
name = input("Qual è il tuo nome? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Sconosciuto")
```

### Concetti Chiave del Match:
- **Il simbolo `|` (Pipe)**: Funziona come un `OR` logico tra i casi. [01:28:00]
- **Il Wildcard `_`**: Rappresenta il caso di default (simile all' `else`). Gestisce qualsiasi input che non ha trovato corrispondenza nei `case` precedenti. [01:29:40]

## 8. Sintesi Teorica
1. **Less is More**: Se un'espressione restituisce già un booleano, usala direttamente invece di creare rami logici extra.
2. **Short-circuiting**: Python smette di valutare una condizione `OR` se la prima parte è già vera, e una `AND` se la prima parte è già falsa.
3. **Leggibilità**: Scegli `match` per confronti diretti su valori fissi e `if/elif` per logiche basate su range o condizioni complesse.