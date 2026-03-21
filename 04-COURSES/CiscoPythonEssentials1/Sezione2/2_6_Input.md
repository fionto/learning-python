# Capitolo 2: Sezione 2.6 - Interazione con l'Utente: Input, Conversioni, Stringhe

## Introduzione: Un Programma "Sordo" Non È Utile

Finora, abbiamo insegnato ai nostri programmi a **parlare** usando `print()`. Ma i programmi che solo parlano sono come persone sorde—possono comunicare in una sola direzione.

Un programma senza input è come una radio che trasmette solo in una direzione. Vi dice cose, ma non vi ascolta. Non collabora con voi. Non reagisce a quello che volete.

**Un programma sordo non è un programma utile.**

Praticamente ogni programma che usate legge dati. Accetta input. Reagisce ad esso. In questa sezione, insegneremo ai vostri programmi come **ascoltare**.

Trasformeremo i programmi da **monologhi a dialoghi**.

## 2.6.1 La Funzione input(): L'Ascoltatore

### Il Parallelo Inverso di print()

Se `print()` **invia** dati al console, `input()` **riceve** dati dal console.

Se `print()` non ha un risultato utilizzabile, `input()` **restituisce un risultato che potete usare**.

È come uno specchio inverso della funzione che già conoscete.

### Il Primo Esempio: Una Conversazione Semplice

```python
print("Dimmi qualsiasi cosa...")
anything = input()
print("Hmm...", anything, "... Davvero?")
```

Cosa accade quando eseguite questo:

1. **print()** visualizza il messaggio "Dimmi qualsiasi cosa..."
2. **input()** viene invocato. Il programma **si ferma e aspetta**
3. Vedete un cursore lampeggiante nel console
4. Digitate qualcosa (supponiamo `"Ciao"`)
5. Premete **Enter**
6. Il testo viene **trasmesso** al programma
7. La variabile `anything` **riceve** il valore
8. Il programma **continua** con la riga successiva

Output:
```
Dimmi qualsiasi cosa...
Ciao                    ← Voi digitate questo
Hmm... Ciao ... Davvero?
```

### Il Punto Critico: Assegnate Sempre il Risultato

Questo è **fondamentale**: il risultato di `input()` deve essere assegnato a una variabile. Altrimenti, il dato **scompare**:

```python
# Sbagliato: il dato è perso
input("Il tuo nome: ")
print("Ciao!")  # Non sappiamo il nome dell'utente!

# Corretto: il dato è salvato
nome = input("Il tuo nome: ")
print("Ciao,", nome)
```

Ricordate: `input()` restituisce una stringa. Se non la assegnate a una variabile, è come scartare un regalo che vi è appena stato dato.

## 2.6.2 input() con Argomenti: Il Prompt Integrato

Scrivere `print()` prima di `input()` è **ridondante** e poco elegante:

```python
# Metodo 1: separato (vecchio)
print("Qual è il tuo nome?")
nome = input()

# Metodo 2: integrato (preferito)
nome = input("Qual è il tuo nome? ")
```

Entrambi fanno esattamente la stessa cosa. La differenza è che il secondo è **più conciso e leggibile**.

Quando passate un argomento a `input()`, esso diventa il **prompt**: il messaggio visualizzato prima del cursore.

```python
eta = input("Quanti anni hai? ")
citta = input("In quale città vivi? ")
hobby = input("Qual è il tuo hobby preferito? ")

print(f"Hai {eta} anni, vivi a {citta}, e ami {hobby}.")
```

Output:
```
Quanti anni hai? 25
In quale città vivi? Milano
Qual è il tuo hobby preferito? la programmazione
Hai 25 anni, vivi a Milano, e ami la programmazione.
```

**Notate lo spazio alla fine del prompt** (`"...? "`). Senza di esso, l'input appare incollato:
```
# Senza spazio (brutto)
Quanti anni hai?25

# Con spazio (bello)
Quanti anni hai? 25
```

Questi piccoli dettagli rendono l'interazione utente **gradevole**, non **confusa**.

## 2.6.3 Il Concetto Critico: input() Restituisce SEMPRE una Stringa

Questa è la lezione più importante di questa sezione: **input() restituisce sempre una stringa, indipendentemente da cosa digita l'utente.**

Anche se l'utente digita `42`, il risultato non è il numero 42. È la **stringa** `"42"`.

```python
numero = input("Inserisci un numero: ")
print(type(numero))  # Output: <class 'str'>
```

Questo è vero sempre. Senza eccezioni.

### Il Problema: Operazioni Aritmetiche su Stringhe

Questo crea un problema quando volete fare operazioni aritmetiche:

```python
# Sbagliato
numero = input("Inserisci un numero: ")
risultato = numero ** 2  # ERRORE!
```

Se l'utente digita `5`, Python vi dà:

```
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

**Che cosa significa?** "Non posso elevare una stringa alla potenza di un intero."

Matematicamente ha senso. Cosa significa `"ciao" ** 2`? Non ha significato. Non potete elevare il testo alla potenza.

### Capire il Tipo di Dato

L'origine del problema è la **differenza di tipo**:

```python
numero_da_input = input("Numero: ")   # Ritorna "5" (stringa)
numero_matematico = 5                  # È 5 (intero)

# Stringhe e numeri sono specie diverse
# Non potete operarci insieme in certi modi
```

Python è rigoroso su questo. Non permette di mescolare tipi casualmente. È una protezione contro errori.

## 2.6.4 Type Casting: Conversione di Stringhe in Numeri

La soluzione è **type casting**—convertire il tipo di dato.

Python offre due funzioni principali per questo:

### int(): Stringa → Intero

La funzione `int()` prende una stringa e la converte in un intero:

```python
numero_stringa = "42"
numero_intero = int(numero_stringa)

print(numero_intero)        # Output: 42
print(type(numero_intero))  # Output: <class 'int'>
```

Potete usare `int()` direttamente con `input()`:

```python
numero = int(input("Inserisci un numero: "))
# Se l'utente digita 5, numero è il numero 5 (non stringa)

risultato = numero ** 2
print(risultato)  # Output: 25 (funziona!)
```

Ecco il flusso:
1. L'utente digita `5`
2. `input()` restituisce `"5"` (stringa)
3. `int("5")` converte a `5` (intero)
4. La variabile `numero` contiene `5` (intero)
5. `5 ** 2 = 25` (operazione aritmetica funziona)

### float(): Stringa → Float

Per numeri con decimali, usate `float()`:

```python
prezzo_stringa = "19.99"
prezzo_float = float(prezzo_stringa)

print(prezzo_float)         # Output: 19.99
print(type(prezzo_float))   # Output: <class 'float'>
```

Con `input()`:

```python
altezza = float(input("Qual è la tua altezza in metri? "))
# Se l'utente digita 1.75, altezza contiene il float 1.75

area = altezza ** 2
print(area)  # Output: 3.0625
```

### Cosa Succede Se la Conversione Fallisce?

Se l'utente digita qualcosa che **non può** essere convertito:

```python
numero = int(input("Numero intero: "))
# L'utente digita: "ciao"
```

Output:
```
ValueError: invalid literal for int() with base 10: 'ciao'
```

Il programma **crasha**. Non potete trasformare `"ciao"` in un intero.

**Per ora, ignoriamo questo problema.** Assumete che l'utente digiti dati validi. Nel capitolo sulle eccezioni, imparerete come **gestire gli errori** elegantemente.

## 2.6.5 Applicazione Pratica: Il Teorema di Pitagora Interattivo

Ricordate il Teorema di Pitagora? Classicamente era così:

```python
# Versione statica
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
```

Rendete interattivo:

```python
# Versione interattiva
cateto_a = float(input("Inserisci il primo cateto: "))
cateto_b = float(input("Inserisci il secondo cateto: "))

ipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
print("Ipotenusa =", ipotenusa)
```

Ora potete testare con **qualsiasi** triangolo:

```
Inserisci il primo cateto: 3
Inserisci il secondo cateto: 4
Ipotenusa = 5.0
```

Oppure:
```
Inserisci il primo cateto: 5.5
Inserisci il secondo cateto: 7.2
Ipotenusa = 9.019376700564849
```

### Versione Senza Variabile Intermedia

Notate che `ipotenusa` è usata solo per immagazzinare il risultato brevemente. Potete eliminate:

```python
cateto_a = float(input("Primo cateto: "))
cateto_b = float(input("Secondo cateto: "))
print("Ipotenusa =", (cateto_a ** 2 + cateto_b ** 2) ** 0.5)
```

Più conciso. Comunque leggibile.

## 2.6.6 Gli Operatori Sulle Stringhe: `+` e `*`

Abbiamo visto `+` e `*` come operatori aritmetici. Ma hanno un **secondo significato** quando applicati a stringhe.

### Il `+` Operator: Concatenazione di Stringhe

Quando applicate `+` a due stringhe, le **incollate insieme**:

```python
nome = "Alice"
cognome = "Rossi"

nome_completo = nome + " " + cognome
print(nome_completo)  # Output: Alice Rossi
```

**Aspetti importanti:**

**Non è commutativo:**
```python
"ab" + "ba" = "abba"
"ba" + "ab" = "baab"
# Sono DIVERSI
```

**Entrambi gli argomenti devono essere stringhe:**
```python
"Numero: " + 42      # ERRORE: non potete concatenare stringa e numero
"Numero: " + str(42) # OK: entrambi stringhe
```

**Potete concatenare più di due stringhe:**
```python
risultato = "A" + "B" + "C" + "D"
print(risultato)  # ABCD
```

### Il `*` Operator: Replicazione di Stringhe

Quando applicate `*` a una stringa e un numero, **replicate la stringa** quel numero di volte:

```python
print("*" * 5)       # Output: *****
print("ab" * 3)      # Output: ababab
print(3 * "la")      # Output: lalala (commutativo)
print("2" * 5)       # Output: 22222 (è una stringa, non numero!)
```

**È commutativo:**
```python
"ab" * 3 = "ababab"
3 * "ab" = "ababab"
# Stesso risultato
```

**Zero o negativo produce stringa vuota:**
```python
"test" * 0    # Output: ""
"test" * -5   # Output: ""
```

### Caso Pratico: Disegnare Forme

Potete usare `+` e `*` insieme per creare forme ASCII:

```python
# Un rettangolo
print("+" + "-" * 10 + "+")
print("|" + " " * 10 + "|")
print("|" + " " * 10 + "|")
print("|" + " " * 10 + "|")
print("+" + "-" * 10 + "+")
```

Output:
```
+----------+
|          |
|          |
|          |
+----------+
```

**Versione più elegante con replicazione:**

```python
print("+" + "-" * 10 + "+")
print(("| " + " " * 9 + "|\n") * 3, end="")
print("+" + "-" * 10 + "+")
```

La riga del corpo è replicata 3 volte usando `* 3`.

## 2.6.7 str(): Convertire Numeri in Stringhe

Abbiamo convertito stringhe in numeri. Potete fare anche il **contrario**: convertire numeri in stringhe con `str()`:

```python
numero = 42
stringa = str(numero)

print(stringa)         # Output: 42
print(type(stringa))   # Output: <class 'str'>
```

### Quando Serve str()

La situazione più comune è quando volete **concatenare** numeri con stringhe:

```python
# Sbagliato
eta = 25
print("La mia età è " + eta)  # ERRORE: no stringa + numero

# Corretto
eta = 25
print("La mia età è " + str(eta))  # Output: La mia età è 25

# Ancora meglio (f-string)
print(f"La mia età è {eta}")  # Output: La mia età è 25
```

Preferite le f-string. Sono più leggibili.

### str() su Qualsiasi Cosa

`str()` converte **qualsiasi cosa** in una rappresentazione stringa:

```python
str(42)           # "42"
str(3.14)         # "3.14"
str(True)         # "True"
str([1, 2, 3])    # "[1, 2, 3]"
```

## Laboratorio 1: Calcolatore di Quattro Operazioni

### Scenario

Create un programma che:
1. Legge due numeri dall'utente
2. Calcola addizione, sottrazione, moltiplicazione, divisione
3. Stampa i risultati in modo ordinato

### Soluzione

```python
# Input
a = float(input("Primo numero: "))
b = float(input("Secondo numero: "))

# Calcoli
print(f"\nAddizione: {a} + {b} = {a + b}")
print(f"Sottrazione: {a} - {b} = {a - b}")
print(f"Moltiplicazione: {a} * {b} = {a * b}")
print(f"Divisione: {a} / {b} = {a / b}")
print("\nGrazie per aver usato la calcolatrice!")
```

### Test

```
Primo numero: 10
Secondo numero: 3

Addizione: 10.0 + 3.0 = 13.0
Sottrazione: 10.0 - 3.0 = 7.0
Moltiplicazione: 10.0 * 3.0 = 30.0
Divisione: 10.0 / 3.0 = 3.3333333333333335

Grazie per aver usato la calcolatrice!
```

## Laboratorio 2: Convertitore di Temperature

### Scenario

Create un convertitore da Celsius a Fahrenheit.

Formula: F = (C × 9/5) + 32

### Soluzione

```python
celsius = float(input("Temperatura in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Test

```
Temperatura in Celsius: 25
25.0°C = 77.0°F
```

### Espansione: Bidirezionale

```python
print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")

scelta = input("Scelta (1 o 2): ")

if scelta == "1":
    c = float(input("Celsius: "))
    f = c * 9/5 + 32
    print(f"{c}°C = {f}°F")
elif scelta == "2":
    f = float(input("Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")
```

(Non preoccupatevi dell'`if`—lo vedrete nel prossimo capitolo.)

## Laboratorio 3: Costruzione di Nomi

### Scenario

Create un programma che legge nome, cognome, e città, poi costruisce una presentazione personalizzata.

### Soluzione

```python
nome = input("Nome: ")
cognome = input("Cognome: ")
citta = input("Città: ")

print("\n" + "=" * 40)
print(f"Nome completo: {nome} {cognome}")
print(f"Città: {citta}")
print("=" * 40)
```

## Laboratorio 4: Calcolatore di BMI

### Scenario

Calcolate l'Indice di Massa Corporea: BMI = peso / (altezza²)

### Soluzione

```python
peso = float(input("Peso (kg): "))
altezza = float(input("Altezza (m): "))

bmi = peso / (altezza ** 2)
print(f"Il tuo BMI è: {bmi:.2f}")
```

## Conclusione: Dialogo vs Monologo

Con `input()`, type casting, e operatori di stringhe, avete trasformato i vostri programmi:

✅ **Da statici a dinamici** – Non più valori hardcodati
✅ **Da monologhi a dialoghi** – Il programma comunica con l'utente  
✅ **Da inutili a pratici** – Possono risolvere problemi reali

Avete le fondamenta per il **Capitolo 3**, dove imparerete a prendere **decisioni** e creare **cicli**.

Ricordate:
- `input()` restituisce **sempre** una stringa
- Convertite con `int()`, `float()`, `str()` quando necessario
- `+` concatena stringhe
- `*` replica stringhe
- F-string sono il modo moderno di formattare

Il vostro programma non è più sordo. Ascolta. Reagisce. È pronto per l'intelligenza. 🚀