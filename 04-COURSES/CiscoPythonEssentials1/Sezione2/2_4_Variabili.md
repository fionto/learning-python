# Capitolo 2: Sezione 2.4 - Variabili: I Contenitori del Vostro Programma

## Introduzione: Dal Letterale alla Variabile

Finora, abbiamo lavorato con **letterali**: dati scritti direttamente nel codice. Abbiamo imparato che `print(2 + 3)` produce `5`. Ma cosa succede quando volete usare quel risultato più tardi? Cosa se volete fare operazioni con il risultato di altre operazioni?

Qui entra in gioco la domanda fondamentale: **come immagazzino i dati nel mio programma in modo da poterli riutilizzare?**

La risposta è: **variabili**.

### Cosa Sono le Variabili: Un'Analogia

Immaginate una biblioteca. I **letterali** sono come libri che portate direttamente dalla libreria—hanno il loro contenuto scritto su di loro. Ma cosa se volete **tornare a casa** con un libro? Non potete tenere il libro in mano per sempre.

Quindi, create uno **scafale** nella vostra casa. Date allo scafale un nome: "Il mio primo scafale". Mettete il libro nello scafale. Ora, ogni volta che volete il libro, non dovete ricordare il suo contenuto—ricordate semplicemente: "Mio primo scafale".

Più tardi, togliete il libro e ne mettete un altro nello stesso scafale. Il nome dello scafale rimane lo stesso, ma il contenuto è cambiato.

Le **variabili** sono esattamente questi scafali. Hanno:
- Un **nome** (come "Il mio primo scafale")
- Un **contenuto** (il libro, che può cambiare)

In Python, potete avere quante variabili volete, con qualsiasi nome (entro i limiti delle regole che impareremo), e potete mettere qualsiasi dato dentro di esse.

### Perché le Variabili Sono Cruciali

Senza variabili, la programmazione sarebbe quasi inutile. Considera questo scenario:

```python
# Senza variabili (praticamente impossibile per problemi reali)
print(3 + 5)                    # Output: 8
print(3 + 5 + 10)               # Devi ricordare il risultato precedente e scriverlo di nuovo
print(3 + 5 + 10 + 20)          # Sempre peggio
```

Con variabili:

```python
# Con variabili (elegante e pratico)
risultato = 3 + 5
print(risultato)                # Output: 8
risultato = risultato + 10
print(risultato)                # Output: 18
risultato = risultato + 20
print(risultato)                # Output: 38
```

Le variabili vi permettono di **pensare logicamente** al vostro programma, invece di dovervi ricordare manualmente ogni risultato intermedio.

## 2.4.1 Creazione di Variabili: Il Momento Magico

### Come Nasce una Variabile

In molti linguaggi di programmazione, dovete dire esplicitamente al computer: "Voglio creare una variabile di tipo intero". È come compilare un modulo burocratico.

Python è diverso. **Una variabile nasce semplicemente quando le assegnate un valore**. Non c'è ceremonia, non c'è dichiarazione. Semplicemente la create:

```python
numero = 42
```

Questa singola riga:
1. **Crea** una variabile di nome `numero`
2. **Assegna** il valore `42` a quella variabile

Se la variabile `numero` non esisteva prima, ora esiste. Se esisteva, il suo valore è stato sostituito.

### La Sintassi di Base

La sintassi è semplicissima:

```python
nome_variabile = valore
```

Il segno `=` è l'**operatore di assegnazione**. Non significa "è uguale a" (come in matematica). Significa "assegna il valore sulla destra alla variabile sulla sinistra".

Alcuni esempi:

```python
eta = 25                        # Una variabile con un intero
nome = "Alice"                  # Una variabile con una stringa
altezza = 1.75                  # Una variabile con un float
è_maggiorenne = True            # Una variabile con un booleano
```

Potete assegnare qualsiasi tipo di dato a una variabile. E potete cambiarla:

```python
x = 10
print(x)                        # Output: 10

x = "Ciao"
print(x)                        # Output: Ciao

x = 3.14
print(x)                        # Output: 3.14
```

La stessa variabile `x` contiene prima un intero, poi una stringa, poi un float. Python **non si lamenta** perché è un linguaggio **dinamicamente tipizzato**.

## 2.4.2 Le Regole dei Nomi di Variabili

Sebbene Python vi dia grande libertà, ci sono **regole rigide** per i nomi delle variabili.

### Quello Che Potete Fare

Un nome di variabile può contenere:
- **Lettere** maiuscole e minuscole: `A-Z`, `a-z`
- **Cifre**: `0-9`
- **Underscore**: `_`

### Quello Che Non Potete Fare

Un nome di variabile:
- **Non può iniziare con una cifra**: `3numero` è **vietato**, ma `numero3` è **permesso**
- **Non può contenere spazi**: `mio numero` è **vietato**, ma `mio_numero` è **permesso**
- **Non può contenere caratteri speciali**: `mio-numero` è **vietato**
- **Non può essere una parola riservata di Python**: `if`, `for`, `while`, ecc. sono **vietati**

### Esempi di Nomi Validi

```python
x = 5                           # Minimalista ma valido
counter = 0                     # Descrittivo
_private = 100                  # Inizia con underscore (spesso per "privato")
my_variable = "test"            # Snake case (consigliato)
MyVariable = "test"             # Camel case (meno comune in Python)
CONSTANT = 3.14                 # Maiuscole per costanti
numero_di_giorni = 365          # Lungo ma chiaro
```

### Esempi di Nomi Invalidi

```python
3numero = 5                     # ERRORE: inizia con una cifra
mio numero = 5                  # ERRORE: contiene uno spazio
mio-numero = 5                  # ERRORE: il trattino non è permesso
if = 5                          # ERRORE: "if" è una parola riservata
!importante = 5                 # ERRORE: ! non è permesso
```

### Case-Sensitive: Attenzione!

Python **distingue** tra maiuscole e minuscole:

```python
numero = 5
Numero = 10
NUMERO = 15

print(numero)                   # Output: 5
print(Numero)                   # Output: 10
print(NUMERO)                   # Output: 15
```

Sono **tre variabili diverse**. Un errore comune dei principianti è confondere `numero` con `Numero`.

### La Convenzione PEP 8: Come Dovrebbero Essere Nominati

La comunità Python ha stabilito delle linee guida sulla nomenclatura nel documento **PEP 8** (Python Enhancement Proposal 8). Anche se non è obbligatorio, è **vivamente consigliato**:

**Per variabili e funzioni:**
- Usate **lettere minuscole**
- Separate le parole con **underscore** (snake_case)
- **Esempi corretti**: `mio_numero`, `conteggio_mele`, `velocita_auto`

**Per costanti (valori che non cambiano):**
- Usate **MAIUSCOLE**
- Separate con **underscore**
- **Esempi**: `PI = 3.14159`, `VELOCITA_LUCE = 3e8`

**Evitate:**
- Nomi troppo lunghi: `questo_e_un_nome_troppo_lungo_e_difficile_da_leggere`
- Nomi troppo brevi (tranne `i`, `j` per contatori): `x`, `a`, `b`
- Nomi poco descrittivi: `var1`, `var2`, `dato`

Applicare PEP 8 rende il vostro codice più leggibile e professionale. Quando altri (o voi stessi tra sei mesi) leggeranno il vostro codice, lo apprezzeranno.

### Parole Riservate di Python

Python ha **35 parole riservate** che non potete usare come nomi di variabili. Ecco le principali (imparerete cosa significano man mano):

```
False, True, None, and, or, not, if, elif, else, for, while, 
break, continue, def, class, return, import, from, try, except, 
finally, raise, with, as, lambda, pass, yield, del, global, 
nonlocal, assert, is, in
```

Se tentate di usarle:

```python
import = 5                      # ERRORE: "import" è riservato
```

**Trucco:** Se per qualche motivo volete un nome simile a una parola riservata, potete cambiarne la capitalizzazione:

```python
Import = 5                      # Valido! (anche se confuso)
```

Ma questo non è consigliato perché crea confusione.

## 2.4.3 Assegnare e Riassegnare Valori

### L'Operatore di Assegnazione: `=`

Il simbolo `=` **non significa "è uguale a"**. Significa **"assegna il valore sulla destra alla variabile sulla sinistra"**.

Questo è fondamentale per non confondere la programmazione con la matematica:

```python
# In matematica: "x non può essere uguale a x + 1" (contraddizione)
# In programmazione: "Prendi il valore di x, aggiungi 1, e salva il risultato in x"
x = 5
x = x + 1
print(x)                        # Output: 6
```

### Assegnazione Multipla Simultanea

Python consente di assegnare più variabili nella stessa riga:

```python
a = b = c = 0
print(a, b, c)                  # Output: 0 0 0
```

Oppure assegnazioni diverse in parallelo:

```python
x, y, z = 1, 2, 3
print(x, y, z)                  # Output: 1 2 3
```

Questo secondo modo è particolarmente utile e Pythonic.

### Scambiare i Valori di Due Variabili

Un caso d'uso interessante:

```python
a = 5
b = 10

# Metodo tradizionale (altri linguaggi richiedono una variabile temporanea)
a, b = b, a
print(a, b)                     # Output: 10 5
```

Python permette di scambiare simultaneamente senza variabili temporanee!

## 2.4.4 Usare Variabili: Le Variabili Devono Esistere

Un punto cruciale: **potete usare solo variabili che esistono**.

```python
x = 10
print(x)                        # OK: x esiste

print(y)                        # ERRORE: y non esiste (NameError)
```

Questo errore è molto comune quando:
1. Vi dimenticate di assegnare un valore prima di usare la variabile
2. Scrivete il nome in modo sbagliato (case-sensitive!)

```python
numero = 5
print(Numero)                   # ERRORE: Numero non esiste (è numero, minuscolo)
```

### Combinare Stringhe e Variabili con `print()`

Un uso pratico è combinare testo e variabili:

```python
nome = "Alice"
eta = 25

# Metodo 1: Virgola (più leggibile)
print("Nome:", nome, "Età:", eta)
# Output: Nome: Alice Età: 25

# Metodo 2: Concatenazione con + (richiede conversione esplicita per numeri)
print("Nome: " + nome + " Età: " + str(eta))
# Output: Nome: Alice Età: 25
```

Il primo metodo è preferibile perché è più chiaro e non richiede conversioni di tipo.

## 2.4.5 Riassegnazione: Cambiare il Valore di una Variabile

Una variabile può cambiare valore tutte le volte che volete:

```python
x = 5
print(x)                        # Output: 5

x = 10
print(x)                        # Output: 10

x = x + 5
print(x)                        # Output: 15
```

### Comprendere l'Assegnazione: Un Processo a Tre Passi

La riga `x = x + 5` potrebbe confondere. Ecco cosa accade:

1. **Valuta il lato destro**: Prendi il valore attuale di `x` (15), aggiungi 5, ottieni 20
2. **Assegna il risultato**: Metti il valore 20 nella variabile `x`
3. **Completa l'operazione**: Ora `x` contiene 20

Non è matematica. È un'istruzione che dice al computer cosa fare.

### Un Caso Pratico: Calcolare il Risultato di Un'Operazione

```python
prezzo = 100.0
sconto = 0.2                    # 20% di sconto

prezzo_scontato = prezzo * (1 - sconto)
print(f"Prezzo originale: {prezzo}")
print(f"Prezzo scontato: {prezzo_scontato}")
# Output:
# Prezzo originale: 100.0
# Prezzo scontato: 80.0
```

Qui le variabili vi permettono di:
1. Immagazzinare dati
2. Eseguire calcoli
3. Usare i risultati in altre operazioni

## 2.4.6 Gli Operatori di Abbreviazione: Fare Meno Digitazione

Spesso fate operazioni come `x = x + 1` o `y = y * 2`. Python offre una forma abbreviata:

### La Tavola degli Operatori di Abbreviazione

| Operazione | Forma Lunga | Forma Abbreviata |
|------------|-----------|------------------|
| Addizione | `x = x + 1` | `x += 1` |
| Sottrazione | `x = x - 1` | `x -= 1` |
| Moltiplicazione | `x = x * 2` | `x *= 2` |
| Divisione | `x = x / 2` | `x /= 2` |
| Floor Division | `x = x // 2` | `x //= 2` |
| Modulo | `x = x % 2` | `x %= 2` |
| Esponenziazione | `x = x ** 2` | `x **= 2` |

### Esempi Pratici

```python
conteggio = 0
conteggio += 1                  # Equivalente a: conteggio = conteggio + 1
print(conteggio)                # Output: 1

conteggio += 5
print(conteggio)                # Output: 6

saldo = 1000
saldo -= 250
print(saldo)                     # Output: 750

velocita = 10
velocita *= 2
print(velocita)                  # Output: 20
```

Questi operatori abbreviati non sono solo "trucchi"—sono leggibili e comuni nel codice professionale.

## 2.4.7 Applicazione Pratica: Risolvere Problemi Matematici

### Esempio 1: Il Teorema di Pitagora

Ricordate? Per un triangolo rettangolo: c² = a² + b²

```python
a = 3.0
b = 4.0

# Calcolate la lunghezza dell'ipotenusa
c_squared = a ** 2 + b ** 2
c = c_squared ** 0.5           # La radice quadrata è l'esponenziazione a 0.5

print(f"Lati: {a} e {b}")
print(f"Ipotenusa: {c}")
# Output:
# Lati: 3.0 e 4.0
# Ipotenusa: 5.0
```

### Esempio 2: Conversione di Valute

```python
euro = 100
tasso_cambio = 1.10            # 1 euro = 1.10 dollari

dollari = euro * tasso_cambio
print(f"€{euro} = ${dollari}")  # Output: €100 = $110.0
```

### Esempio 3: Calcolo dello Sconto Finale

```python
prezzo_originale = 150.0
sconto_percentuale = 10        # 10% di sconto

importo_sconto = prezzo_originale * (sconto_percentuale / 100)
prezzo_finale = prezzo_originale - importo_sconto

print(f"Prezzo originale: €{prezzo_originale}")
print(f"Sconto ({sconto_percentuale}%): €{importo_sconto}")
print(f"Prezzo finale: €{prezzo_finale}")
# Output:
# Prezzo originale: €150.0
# Sconto (10%): €15.0
# Prezzo finale: €135.0
```

## Laboratorio 1: Le Mele di Appleland

### Scenario

Nel mitico regno di Appleland:
- John ha 3 mele
- Mary ha 5 mele
- Adam ha 6 mele

Volete sapere quante mele hanno in totale.

### Soluzione Passo-Passo

```python
# Passo 1: Create le variabili per ogni persona
john = 3
mary = 5
adam = 6

# Passo 2: Stampate i valori individuali
print("John:", john, "mele")
print("Mary:", mary, "mele")
print("Adam:", adam, "mele")

# Passo 3: Create una variabile per il totale
total_apples = john + mary + adam

# Passo 4: Stampate il totale
print("Totale mele:", total_apples)
# Output:
# John: 3 mele
# Mary: 5 mele
# Adam: 6 mele
# Totale mele: 14
```

### Espansione: Aggiungere Più Persone

```python
john = 3
mary = 5
adam = 6
peter = 2                       # Una nuova persona!

total_apples = john + mary + adam + peter
print(f"Totale mele: {total_apples}")  # Output: Totale mele: 16
```

## Laboratorio 2: Convertitore di Misure

### Scenario

Volete creare un programma che converte:
- Miglia in chilometri (1 miglio ≈ 1.609 km)
- Chilometri in miglia

### Soluzione

```python
# Costanti di conversione
miglia_a_km = 1.609
km_a_miglia = 1 / miglia_a_km

# Valori da convertire
miles = 10
kilometers = 25

# Conversioni
miles_in_km = miles * miglia_a_km
km_in_miles = kilometers * km_a_miglia

# Stampa con arrotondamento
print(f"{miles} miglia = {round(miles_in_km, 2)} km")
print(f"{kilometers} km = {round(km_in_miles, 2)} miglia")
# Output:
# 10 miglia = 16.09 km
# 25 km = 15.54 miglia
```

**Nota sulla funzione `round()`:** Arrotonda il numero al numero specificato di decimali. `round(3.14159, 2)` produce `3.14`.

### Espansione: Più Conversioni

```python
# Convertitore universale
meters = 1000
feet = meters * 3.28084         # 1 metro ≈ 3.28084 piedi
print(f"{meters}m = {feet:.2f} feet")  # Output: 1000m = 3280.40 feet
```

## Laboratorio 3: Valutare Espressioni Polinomiali

### Scenario

Volete valutare il polinomio: **3x³ - 2x² + 3x - 1**

Per diversi valori di x.

### Soluzione

```python
# Funzione polinomiale: 3x³ - 2x² + 3x - 1

# Test con x = 0
x = 0.0
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print(f"x = {x}: y = {y}")      # Output: x = 0.0: y = -1.0

# Test con x = 1
x = 1.0
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print(f"x = {x}: y = {y}")      # Output: x = 1.0: y = 3.0

# Test con x = -1
x = -1.0
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print(f"x = {x}: y = {y}")      # Output: x = -1.0: y = -9.0

# Test con x = 2
x = 2.0
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print(f"x = {x}: y = {y}")      # Output: x = 2.0: y = 21.0
```

### Versione Più Elegante

```python
def valuta_polinomio(x):
    return 3 * x**3 - 2 * x**2 + 3 * x - 1

valori_test = [0, 1, -1, 2, 0.5]
for x in valori_test:
    y = valuta_polinomio(float(x))
    print(f"x = {x}: y = {y}")
```

(Non preoccupatevi se non comprendete il concetto di funzione—lo imparerete presto!)

## Conclusione: Le Variabili Come Fondamento della Programmazione

Le variabili trasformano Python da una semplice calcolatrice a uno strumento di programmazione vero e proprio. Vi permettono di:

✅ **Immagazzinare** dati per uso futuro  
✅ **Riutilizzare** i risultati di calcoli  
✅ **Costruire** programmi logicamente ordinati  
✅ **Rendere il codice leggibile** dando nomi significativi ai dati  

Una buona pratica nel naming—seguendo PEP 8—rende il vostro codice professionale e facilmente mantenibile.

Ricordate:
- Una variabile ha un **nome** e un **valore**
- Il valore può **cambiare**
- Il nome deve **seguire le regole**
- Usate nomi **descrittivi**
- L'operatore `=` **assegna**, non confronta

Nei prossimi capitoli, combinerete variabili con strutture di controllo (if, loop) per creare programmi che prendono decisioni e risolvono problemi reali. Le variabili sono il vostro fondamento.

Praticate creando le vostre variabili, assegnate loro valori, e fate calcoli. Sperimentate con nomi diversi. Verificate quali nomi sono validi e quali no. La programmazione si impara facendo.