# Capitolo 2: Sezione 2.3 - Operatori: Gli Strumenti di Manipolazione dei Dati

## Introduzione: Python Come Calcolatore e Oltre

Quando siamo bambini, apprendiamo l'aritmetica come il primo livello di manipolazione dei numeri: addizione, sottrazione, moltiplicazione, divisione. Python possiede tutti questi strumenti e molti altri. Ma più importante ancora, Python ci insegna che il calcolo non è il fine, ma il mezzo.

Un **operatore** è un simbolo che istruisce il programma a eseguire un'azione su uno o più valori. Quando vedete `2 + 2`, il `+` è un operatore. Quando vedete `5 * 3`, il `*` è un operatore. Ma gli operatori in Python vanno ben oltre l'aritmetica di base.

### Il Primo Esperimento: Python Come Calcolatrice

Iniziamo con qualcosa di semplice:

```python
print(2 + 2)
```

Output:
```
4
```

È banale, ma importante: avete appena visto che Python non solo **immagazzina** i dati, ma li **elabora**. La funzione `print()` non stampa solo letterali—stampa anche i **risultati** delle operazioni.

Questo è il nostro primo assaggio di ciò che gli operatori possono fare. Insieme ai letterali, gli operatori formano le **espressioni**: i blocchi di costruzione della logica computazionale.

## 2.3.1 Gli Operatori Aritmetici Fondamentali

Python supporta sette operatori aritmetici principali. Andiamoli ad esaminare uno per uno, non in ordine di importanza, ma in ordine di priorità (vi spiegherò perché tra poco).

### L'Esponente: `**` (Doppio Asterisco)

L'operatore `**` esegue l'**elevamento a potenza**. È come scrivere 2³ in matematica:

```python
print(2 ** 3)        # 2 alla potenza di 3 = 8
print(5 ** 2)        # 5 al quadrato = 25
print(10 ** 6)       # 10 alla potenza di 6 = 1.000.000
```

Output:
```
8
25
1000000
```

Un aspetto cruciale: quando si usa `**` con interi, il risultato è un intero. Quando almeno uno degli operandi è un float, il risultato è un float:

```python
print(2 ** 3)        # Entrambi interi → Output: 8 (intero)
print(2 ** 3.0)      # Uno è float → Output: 8.0 (float)
print(2.0 ** 3)      # Uno è float → Output: 8.0 (float)
print(2.0 ** 3.0)    # Entrambi float → Output: 8.0 (float)
```

Questa regola vale per quasi tutti gli operatori aritmetici: **il tipo del risultato dipende dai tipi degli operandi**.

### La Moltiplicazione: `*` (Asterisco)

L'operatore `*` moltiplica due numeri:

```python
print(3 * 4)         # Output: 12
print(2.5 * 4)       # Output: 10.0
print(0 * 1000)      # Output: 0
```

Come l'esponente, la moltiplicazione segue la regola int/float: se entrambi gli operandi sono interi, il risultato è intero. Se almeno uno è float, il risultato è float.

**Un uso inaspettato della moltiplicazione:**

```python
print("*" * 10)      # Output: **********
print("ciao" * 3)    # Output: ciaoaiaociao
```

Sì, potete moltiplicare anche stringhe! Quando moltiplicate una stringa per un numero, la ripetete quel numero di volte. Questo è utile per creare barre, separatori, o pattern.

### La Divisione: `/` (Slash)

L'operatore `/` esegue la divisione. Ma attenzione: **la divisione in Python produce sempre un float, indipendentemente dagli operandi**:

```python
print(6 / 2)         # Output: 3.0 (NON 3!)
print(7 / 2)         # Output: 3.5
print(10 / 4)        # Output: 2.5
```

Questo è diverso da molti altri linguaggi, dove `6 / 2` darebbe `3` (intero). Python ha scelto di essere sempre "esatto" nella divisione, anche se il risultato è un numero intero espresso come float.

### La Divisione Intera: `//` (Doppio Slash)

Spesso, volete il risultato della divisione **senza la parte decimale**. Per questo, Python offre l'operatore `//`, chiamato **floor division** (divisione per difetto):

```python
print(6 // 2)        # Output: 3 (intero)
print(7 // 2)        # Output: 3 (arrotonda verso il basso)
print(10 // 3)       # Output: 3 (non 3.33...)
print(10 // 4)       # Output: 2 (non 2.5)
```

L'aspetto cruciale di `//` è che **arrotonda sempre verso il basso**, verso l'intero minore. Non è arrotondamento "normale" (dove 2.5 diventerebbe 3). È arrotondamento verso il basso, sempre:

```python
print(6 // 4)        # Output: 1 (6/4 = 1.5, arrotonda a 1)
print(-6 // 4)       # Output: -2 (!!!) 
```

Quel -2 sorprende molti principianti. Spieghiamo: -6/4 = -1.5. Se arrotonda verso il basso, il basso di -1.5 è -2, non -1. Questo è cruciale per capire `//`:

**Regola d'oro di floor division:** Il risultato è sempre l'intero più grande che è minore o uguale al risultato reale.

### Il Resto (Modulo): `%` (Percentuale)

L'operatore `%` è uno dei meno intuitivi, ma anche uno dei più utili. Non calcola una percentuale—calcola il **resto** dopo una divisione intera.

Pensate a come si divide manualmente: se dividete 14 per 4, ottenete 3 con un resto di 2. L'operatore `%` vi dà proprio quel resto:

```python
print(14 % 4)        # Output: 2
# Perché? 14 // 4 = 3, quindi 14 - (3 * 4) = 14 - 12 = 2

print(17 % 5)        # Output: 2 (17 = 3 × 5 + 2)
print(20 % 3)        # Output: 2 (20 = 6 × 3 + 2)
print(10 % 2)        # Output: 0 (10 è perfettamente divisibile)
```

**Casi d'uso pratici del modulo:**

Determinare se un numero è pari o dispari:
```python
numero = 7
if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")  # Output: Dispari
```

Ottenere le ultime cifre di un numero:
```python
numero = 123456
ultime_due_cifre = numero % 100  # Output: 56
ultima_cifra = numero % 10        # Output: 6
```

Creare cicli che si ripetono ogni N elementi:
```python
for i in range(10):
    if i % 3 == 0:
        print(f"{i} è divisibile per 3")
# Output: 0, 3, 6, 9 sono divisibili per 3
```

### L'Addizione: `+`

L'addizione è quello che vi aspettate:

```python
print(2 + 3)         # Output: 5
print(-4 + 8)        # Output: 4
print(3.5 + 2.5)     # Output: 6.0
```

Segue la regola int/float: int + int = int, ma se uno è float, il risultato è float.

### La Sottrazione: `-`

La sottrazione funziona come l'addizione, ma con una complicazione: il `–` ha due significati.

```python
print(10 - 3)        # Sottrazione binaria: 10 meno 3 = 7
print(-5)            # Negazione unaria: il negativo di 5
```

Nel primo caso, `–` è un **operatore binario** (richiede due operandi, uno a sinistra e uno a destra). Nel secondo caso, `–` è un **operatore unario** (richiede un solo operando, quello a destra).

Python è intelligente abbastanza da capire dalla contesto quale intendete. Se c'è un valore prima del `–`, è una sottrazione. Se c'è solo un valore dopo, è una negazione.

```python
x = 5
print(-x)            # Output: -5 (negazione unaria)
print(10 - x)        # Output: 5 (sottrazione binaria)
print(10 - -x)       # Output: 15 (sottrazione seguita da negazione)
```

Quel `10 - -x` è confuso? È per questo che gli spazi aiutano! Leggete come "10 meno il negativo di x".

### L'Operatore Unario Positivo: `+`

Esiste anche un operatore unario positivo `+`, anche se è raramente usato:

```python
print(+5)            # Output: 5 (non cambia nulla)
```

Esiste per simmetria con `–`, ma non ha quasi mai un motivo di esistere nel codice reale.

### Prevenire la Divisione per Zero

Prima di andare avanti, un avvertimento: **non dividete mai per zero**:

```python
print(10 / 0)        # ERRORE: ZeroDivisionError
print(10 // 0)       # ERRORE: ZeroDivisionError
print(10 % 0)        # ERRORE: ZeroDivisionError
```

Python si rifiuterà di eseguire qualsiasi divisione dove il divisore è zero. Non è una "limitazione"—è una protezione contro un'operazione matematicamente indefinita.

## 2.3.2 Il Concetto di Priorità: Perché 2 + 3 * 5 Non è 25

Ricordate la scuola? Quando insegnanti vi hanno insegnato l'ordine delle operazioni? Avete imparato che moltiplicazione e divisione vengono prima di addizione e sottrazione. Questo si chiama la **gerarchia di priorità** (order of operations).

In Python funziona esattamente allo stesso modo, ma è ancora più rigoroso e formale.

### Il Problema Fondamentale

Considerate questa espressione:

```python
print(2 + 3 * 5)
```

Quant'è il risultato? Dipende da **quale operazione fai per prima**:

- Se fai prima l'addizione: (2 + 3) * 5 = 5 * 5 = 25
- Se fai prima la moltiplicazione: 2 + (3 * 5) = 2 + 15 = 17

Python sceglierà sempre la moltiplicazione per prima, dando 17. Perché? Perché la moltiplicazione ha una **priorità più alta** dell'addizione.

### La Gerarchia di Priorità Completa

Python definisce una gerarchia precisa. Ecco gli operatori che abbiamo visto, ordinati da priorità più alta a più bassa:

| Priorità | Operatori | Descrizione | Associatività |
|----------|-----------|-------------|---------------|
| 1 (Massima) | `**` | Esponenziazione | Destra a sinistra |
| 2 | `+x`, `-x`, `+` unario | Negazione/Positività | Destra a sinistra |
| 3 | `*`, `/`, `//`, `%` | Moltiplicazione, Divisione, Floor Division, Modulo | Sinistra a destra |
| 4 (Minima) | `+`, `-` (binari) | Addizione, Sottrazione | Sinistra a destra |

### Esempi di Priorità in Azione

Proviamo alcuni esempi:

**Esempio 1: Moltiplicazione prima dell'addizione**
```python
print(2 + 3 * 4)     # Output: 14
# Perché: 3 * 4 = 12, poi 2 + 12 = 14
```

**Esempio 2: Esponenziazione prima di moltiplicazione**
```python
print(2 * 3 ** 2)    # Output: 18
# Perché: 3 ** 2 = 9, poi 2 * 9 = 18
```

**Esempio 3: Negazione unaria ha priorità alta**
```python
print(-2 ** 2)       # Output: -4 (NON 4!)
# Perché: 2 ** 2 = 4, poi negazione: -4
# Se voleste 4 positivo, scrivereste (-2) ** 2 = 4
```

**Esempio 4: Espressione complessa**
```python
print(2 + 3 * 4 - 5 // 2)
# Passo 1: 3 * 4 = 12 (moltiplicazione ha priorità)
# Passo 2: 5 // 2 = 2 (floor division ha priorità)
# Passo 3: 2 + 12 - 2 = 14 - 2 = 12 (addizione/sottrazione da sinistra a destra)
# Output: 12
```

## 2.3.3 L'Associatività: Quando gli Operatori Hanno la Stessa Priorità

Cosa succede quando avete due operatori con la stessa priorità nella stessa espressione? Ad esempio:

```python
print(10 - 3 - 2)
```

Potete calcolare questo in due modi:
- Da sinistra a destra: (10 - 3) - 2 = 7 - 2 = 5
- Da destra a sinistra: 10 - (3 - 2) = 10 - 1 = 9

Quale vi dà Python? La risposta è nell'**associatività**.

### Associatività Sinistra (Left-to-Right)

La maggior parte degli operatori ha **associatività sinistra**, il che significa che vengono valutati da sinistra verso destra:

```python
print(10 - 3 - 2)    # Output: 5 (valuta (10-3)-2)
print(20 / 4 / 2)    # Output: 2.5 (valuta (20/4)/2 = 5/2)
print(14 % 6 % 2)    # Output: 1 (valuta (14%6)%2 = 2%2)
```

### Associatività Destra (Right-to-Left): L'Eccezione

C'è un'eccezione importante: l'**esponenziazione** ha associatività **destra**:

```python
print(2 ** 2 ** 3)   # Output: 256
# Valuta da destra a sinistra: 2 ** (2 ** 3) = 2 ** 8 = 256
# NON (2 ** 2) ** 3 = 4 ** 3 = 64
```

Questo è controintuitivo! Quando vedete `2 ** 2 ** 3`, il cervello potrebbe pensare di fare prima il `2 ** 2`, ma Python fa il `2 ** 3` per primo.

Perché? Storicamente, in matematica, l'esponenziazione è stata tradizionalmente considerata un'operazione "destra-associativa". Python ha seguito questa convenzione.

### Conseguenze Pratiche

Capire l'associatività vi salva da errori sottili:

```python
# Esempio 1: Sottrazione
print(10 - 5 - 2)    # Output: 3 (=(10-5)-2=5-2)

# Esempio 2: Divisione
print(100 / 10 / 2)  # Output: 5.0 (=(100/10)/2=10/2)

# Esempio 3: Esponenziazione (attenzione!)
print(2 ** 3 ** 2)   # Output: 512 (=2**(3**2)=2**9)
```

## 2.3.4 Usare le Parentesi per Controllare l'Ordine

La bellezza della programmazione è che **non dovete fidarvi della memoria sulla priorità**. Potete usare le **parentesi** per esplicitare esattamente quale ordine volete:

```python
print(2 + 3 * 5)           # Output: 17 (priorità naturale)
print((2 + 3) * 5)         # Output: 25 (addizione prima)
```

Le parentesi hanno la priorità massima assoluta. Tutto dentro le parentesi viene valutato prima di tutto il resto.

### Parentesi Annidate

Potete annidare le parentesi tanto quanto volete:

```python
print(((2 + 3) * (5 - 1)) // (3 + 1))
# Passo 1: (2+3) = 5
# Passo 2: (5-1) = 4
# Passo 3: 5 * 4 = 20
# Passo 4: (3+1) = 4
# Passo 5: 20 // 4 = 5
# Output: 5
```

### Buone Pratiche: Priorità e Leggibilità

Anche se Python vi permette di scrivere espressioni complicate senza parentesi, **usate le parentesi quando aiutano la leggibilità**:

```python
# Difficile da leggere (e sbagliato se non ricordate le priorità)
print(a + b * c - d / e ** 2)

# Molto più leggibile
print(a + (b * c) - (d / (e ** 2)))
```

Non è una debolezza usare parentesi "inutili"—è una forza. Il codice leggibile è migliore del codice conciso.

## 2.3.5 Esempi Pratici Complessi

Vediamo alcuni esempi più realistici che combinano priorità e associatività:

### Esempio 1: Calcolo di Area e Perimetro

```python
raggio = 5
pi = 3.14159

area_cerchio = pi * raggio ** 2
print(f"Area del cerchio: {area_cerchio}")  
# Output: Area del cerchio: 78.54...
# Perché: raggio**2 prima (priorità), poi moltiplicazione

circonferenza = 2 * pi * raggio
print(f"Circonferenza: {circonferenza}")
# Output: Circonferenza: 31.415...
# Moltiplicazioni valutate da sinistra a destra
```

### Esempio 2: Conversione di Valute

```python
euro = 100
tasso_cambio = 1.10  # 1 euro = 1.10 dollari
commissione_percentuale = 2  # 2% di commissione

dollari_grezzi = euro * tasso_cambio
commissione = dollari_grezzi * commissione_percentuale / 100
dollari_finali = dollari_grezzi - commissione

print(f"€{euro} = ${dollari_finali:.2f}")
# Output: €100 = $107.58
```

### Esempio 3: Scorporo di Cifre da un Numero

```python
numero = 123456

cifra_unitaria = numero % 10                    # 6
cifra_decine = (numero % 100) // 10             # 5
cifra_centinaia = (numero % 1000) // 100        # 4

print(f"Unità: {cifra_unitaria}, Decine: {cifra_decine}, Centinaia: {cifra_centinaia}")
# Output: Unità: 6, Decine: 5, Centinaia: 4
```

## Laboratorio: Esercizi Progressivi

### Esercizio 1: Predire il Risultato

Senza eseguire il codice, prevedete l'output:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 - 2 - 3)
print(10 // 3 // 2)
print(2 ** 3 ** 2)
```

Poi eseguete e controllate!

### Esercizio 2: Aggiungere Parentesi per Ottenere un Risultato Specifico

Date l'espressione `2 + 3 * 4`, aggiungete parentesi per ottenere:
- 14 (risultato naturale)
- 20 (aggiungete parentesi)

### Esercizio 3: Calcoli Realistici

Scrivete espressioni Python per:

1. Calcolare il valore finale di un investimento di €1000 con interesse annuale del 5% per 3 anni
   ```python
   # Suggerimento: 1000 * (1.05 ** 3)
   ```

2. Calcolare il numero di ore, minuti e secondi da un numero totale di secondi (es. 3661)
   ```python
   # Suggerimento: usate // per ore, % per i secondi rimanenti
   ```

3. Determinare se un numero di 4 cifre è palindromo
   ```python
   # Suggerimento: usate % per estrarre le cifre
   ```

## Conclusione: Gli Operatori Come Linguaggio del Calcolo

Gli operatori sono il vostro modo di istruire il computer a manipolare i dati. Non sono solo simboli matematici—sono comandi precisi che dicono al computer esattamente cosa fare, in quale ordine, e come interpretare il risultato.

Capire la priorità e l'associatività non è un'esercizio di noia. È capire il **linguaggio** che il computer parla. Quando leggete un'espressione complessa e capite esattamente cosa farà Python, state padroneggiando un livello profondo della programmazione.

Nei prossimi capitoli, vedrete come gli operatori si combinano con variabili, funzioni, e strutture di controllo per creare programmi reali. Ma il fondamento rimane sempre lo stesso: gli operatori che abbiamo imparato qui.

Non memorizzate la tabella di priorità. Usate le parentesi quando avete dubbi. Scrivete codice leggibile. E quando vedete un'espressione complessa, prendetevi un momento per analizzarla passo dopo passo. È così che i programmatori esperti leggono il codice.