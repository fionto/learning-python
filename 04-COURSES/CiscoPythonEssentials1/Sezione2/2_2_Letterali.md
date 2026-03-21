# Capitolo 2: Sezione 2.2 - Letterali Python: I Dati Nel Loro Stato Puro

## Introduzione: Cosa Sono i Letterali

Abbiamo imparato a usare `print()` per visualizzare le informazioni. Ma dove vengono queste informazioni? Come le comunichiamo al nostro programma? La risposta risiede in un concetto fondamentale chiamato **letterale**.

Un **letterale** è un valore di dati rappresentato direttamente nel codice. È il dato stesso, nella sua forma più pura e immediata. Quando scrivete semplicemente il numero `42` nel vostro codice, state creando un letterale numerico. Quando scrivete la stringa `"Ciao"`, state creando un letterale di stringa.

### Letterali vs. Variabili: Una Distinzione Critica

Per comprendere meglio cosa sia un letterale, è utile distinguerlo da una variabile. Considerate questi due esempi:

```python
print(123)        # Questo è un letterale - il valore 123 direttamente nel codice
print(numero)     # Questo NON è un letterale - è una variabile
```

Nel primo caso, `123` è un letterale: il valore è scritto esattamente così nel codice. Nel secondo caso, `numero` è una variabile: è un nome che punta a un valore memorizzato da qualche parte in memoria.

### L'Importanza dei Letterali

I letterali sono il modo in cui comunicate valori concreti al vostro programma. Sono i "dati grezzi" che fornite. Senza letterali, avreste bisogno di scrivere lunghe procedure complicate per creare anche i dati più semplici. I letterali ci permettono di dire direttamente: "voglio questo numero, questa stringa, questo valore".

## 2.2.1 Il Concetto di Letterale: Dati Che Si Identificano Da Soli

Immaginiamo una conversazione tra voi e qualcuno. Dite: "Pensa al numero uno, due, tre". Immediatamente, la persona sa di quale numero state parlando: 123.

Ora, dite: "Pensa alla lettera c". Di quale "c" state parlando? Potrebbe essere:
- La velocità della luce in fisica
- Una costante di integrazione in matematica
- La lunghezza di un cateto nel teorema di Pitagora
- Semplicemente la lettera c in un alfabeto
- Una variabile in un programma

Senza contesto aggiuntivo, "c" è ambigua. Ma "123" non è ambigua—è il numero 123, punto.

Questo è il cuore della definizione: un **letterale è una rappresentazione di dati il cui valore è univoco e autodeterminato dal modo in cui è scritto**.

### Un Esperimento Pratico

Considerate questo codice:

```python
print("2")
print(2)
```

Eseguitelo. Vedrete:

```
2
2
```

Le due righe stampano lo stesso output visivo, ma il loro significato interno è completamente diverso. Nel primo caso, `"2"` è un letterale di stringa—è il carattere "2" trattato come testo. Nel secondo caso, `2` è un letterale numerico—è il numero due come valore aritmetico.

Python sa distinguere questi due casi dal **contesto e dalla forma**. La presenza di virgolette rende il primo una stringa. L'assenza di virgolette rende il secondo un numero. Questo è un aspetto fondamentale di come Python riconosce i tipi di dati: il **formato del letterale determina il suo tipo**.

## 2.2.2 I Numeri Interi: Gli Integer

### Cosa Sono gli Interi?

Un **numero intero** (integer, abbreviato `int` in Python) è un numero senza una parte frazionaria. È come contare con le dita: 1, 2, 3, 10, 1000. Non ci sono decimali.

Nel mondo reale, i computer elaborano due tipi fondamentali di numeri:

**Interi** – Numeri senza parte decimale (10, -5, 0, 999)

**Numeri in virgola mobile (float)** – Numeri con parte decimale (3.14, -0.5, 0.001)

Questa distinzione è cruciale. Internamente, il computer li immagazzina in modi completamente diversi. Gli interi occupano meno memoria e le operazioni su di essi sono più veloci. Ma gli interi non possono rappresentare valori frazionari.

### Scrivere Letterali Interi

Quando scrivete un numero intero nel vostro codice, Python riconosce automaticamente che è un intero dal formato:

```python
print(42)              # Il numero quarantadue
print(-15)             # Il numero meno quindici
print(0)               # Zero
print(1000000)         # Un milione
print(+100)            # Cento (il + è opzionale)
```

Python è flessibile: non richiede segni per i numeri positivi, anche se potete includerli se volete.

### Leggibilità: Gli Underscore nei Numeri

Quando scrivete numeri molto grandi, il codice diventa difficile da leggere. Qual è la differenza tra questi due?

```python
print(11111111)      # Difficile da contare
print(11_111_111)    # Chiaro: è una cifra con separatori
```

Sono esattamente lo stesso numero! Python consente di aggiungere **underscore** (`_`) tra le cifre per migliorare la leggibilità. Non influisce sul valore:

```python
# Tutti questi rappresentano il numero duecentoquarantacinque milioni trecentoventi mila uno
print(245320001)
print(245_320_001)
print(245_320_001)   # Stesso numero, più leggibile
```

Questa caratteristica è stata introdotta in Python 3.6 ed è utilissima quando si lavora con numeri grandi come:

```python
distanza_terra_sole = 149_600_000  # 149,6 milioni di km
popolazione_mondiale = 8_000_000_000  # 8 miliardi
codice_fiscale = 12_345_678
```

### Numeri Negativi e Positivi

Un numero negativo è semplicemente preceduto dal segno meno:

```python
print(-42)
print(-1_000_000)
```

I numeri positivi non necessitano del segno più, ma potete includerlo se lo desiderate:

```python
print(+42)    # Stesso di print(42)
print(42)     # Perfettamente equivalente
```

### Numeri in Notazione Ottale e Esadecimale

Python consente di scrivere numeri in basi diverse da quella decimale (base 10) che usiamo normalmente.

#### Notazione Ottale (Base 8)

Se precedete un numero con `0o` (zero seguita dalla lettera "o" minuscola), Python lo interpreta come un numero **ottale**:

```python
print(0o10)      # Output: 8 (uno-zero in ottale = otto in decimale)
print(0o123)     # Output: 83
print(0o777)     # Output: 511
```

I numeri ottali usano solo le cifre da 0 a 7. Se digitate `0o8`, Python darà un errore perché 8 non è una cifra valida in base 8.

Quando usate la notazione ottale, Python converte automaticamente il valore e lo visualizza in decimale. Questa notazione è poco comune nel lavoro quotidiano, ma rimane disponibile per compiti specifici (spesso legati a permessi di file in sistemi Unix/Linux).

#### Notazione Esadecimale (Base 16)

Se precedete un numero con `0x` (zero seguita dalla lettera "x" minuscola), Python lo interpreta come **esadecimale**:

```python
print(0x10)      # Output: 16 (uno-zero in hex = sedici in decimale)
print(0xFF)      # Output: 255 (massimo valore a due cifre hex)
print(0x1A)      # Output: 26
```

I numeri esadecimali usano le cifre 0-9 e le lettere A-F (dove A=10, B=11, ..., F=15). Python accetta sia lettere maiuscole che minuscole:

```python
print(0xFF)      # Output: 255
print(0xff)      # Output: 255 (stesso valore)
print(0xAbCd)    # Output: 43981 (maiuscole e minuscole mischiate vanno bene)
```

I numeri esadecimali sono molto comuni nella programmazione quando si lavora con colori, indirizzi di memoria, o dati binari.

**Esempio pratico – Colore esadecimale:**

```python
colore_rosso = 0xFF0000      # Rosso puro in formato RGB
colore_blu = 0x0000FF        # Blu puro in formato RGB
colore_verde = 0x00FF00      # Verde puro in formato RGB
```

## 2.2.3 I Numeri in Virgola Mobile: I Float

### Cosa Sono i Float?

Un **numero in virgola mobile** (floating-point number, abbreviato `float`) è un numero che ha (o può avere) una parte frazionaria. È qualsiasi numero che richiede un punto decimale.

Quando dite "due e mezzo" o "meno zero virgola quattro", state parlando di numeri che Python classifica come float:

```python
print(2.5)       # Due e mezzo
print(-0.4)      # Meno zero virgola quattro
print(3.14159)   # Pi greco
print(0.0)       # Zero virgola zero
```

### Il Punto Decimale è Essenziale

Il punto decimale è critico. Distingue gli interi dai float:

```python
print(4)         # Intero (quattro)
print(4.0)       # Float (quattro virgola zero)
print(4.)        # Float (equivalente a 4.0)
print(.4)        # Float (equivalente a 0.4)
```

Anche se `4` e `4.0` hanno lo stesso valore numerico, Python li tratta internamente in modo completamente diverso. Uno è un intero, l'altro è un float. Questa distinzione è importante perché influisce su come Python esegue certe operazioni.

### Regola di Omissione degli Zeri

Se uno zero è l'unica cifra davanti o dopo il punto decimale, potete ometterlo:

```python
print(0.5)       # Tradizionale
print(.5)        # Senza lo zero iniziale - equivalente

print(5.0)       # Tradizionale
print(5.)        # Senza lo zero finale - equivalente
```

Sebbene queste forme abbreviate siano permesse, molti sviluppatori preferiscono la forma completa per chiarezza. La scelta è vostra.

### Notazione Scientifica

Per numeri molto grandi o molto piccoli, Python supporta la **notazione scientifica** usando la lettera `E` (o `e`):

```python
print(3E8)       # Output: 300000000.0 (3 × 10⁸)
print(1.5E-3)    # Output: 0.0015 (1.5 × 10⁻³)
```

La lettera E significa "per dieci alla potenza di". La notazione scientifica è estremamente utile in fisica e astronomia.

#### Esempi Pratici di Notazione Scientifica

**Velocità della luce** – 300.000.000 m/s:

```python
velocita_luce = 3E8  # m/s
print(velocita_luce)  # Output: 300000000.0
```

**Costante di Planck** – 0,0000000000000000000000000000000662607 J·s:

```python
costante_planck = 6.62607E-34  # J·s
print(costante_planck)  # Output: 6.62607e-34
```

**Distanza Terra-Sole** – 149.600.000 km:

```python
distanza_terra_sole = 1.496E8  # km
print(distanza_terra_sole)  # Output: 149600000.0
```

### Notate: Python Sceglie la Rappresentazione Più Economica

Un aspetto importante: il modo in cui **voi** scrivete un float non determina come Python lo **visualizza**:

```python
numero_molto_piccolo = 0.0000000000000000000001
print(numero_molto_piccolo)  # Output: 1e-22
```

Python ha scelto di usare la notazione scientifica perché è più breve e leggibile. Questo è saggio dal punto di vista della leggibilità, ma significa che non potete controllare completamente come appare l'output di un float.

## 2.2.4 Le Stringhe: Testo nel Vostro Codice

### Cosa Sono le Stringhe?

Una **stringa** è una sequenza di caratteri. È il modo di Python di rappresentare il **testo**. Se avete bisogno di elaborare nomi, indirizzi, messaggi, poesia—qualsiasi cosa che sia testo—userete stringhe.

Le stringhe sono circondate da **virgolette** (quote):

```python
print("Ciao, mondo!")
print("La programmazione è fantastica")
print("123 Main Street")
```

Le virgolette segnalano a Python che il contenuto deve essere trattato come testo, non come codice. Se scrivete `Hello` senza virgolette, Python lo cercherebbe come variabile. Se scrivete `"Hello"`, Python sa che è una stringa di testo.

### Singole vs. Doppie Virgolette

Python accetta indifferentemente **virgolette singole** (`'`) o **doppie** (`"`):

```python
print("Ciao")      # Doppia virgoletta
print('Ciao')      # Singola virgoletta
```

Entrambe producono lo stesso output. La scelta è vostra, ma dovete essere **coerenti**: se aprite con una virgoletta doppia, dovete chiudere con una virgoletta doppia. Non potete mischiarle:

```python
print("Ciao')  # ERRORE - aperto con doppia, chiuso con singola
```

### Il Problema delle Virgolette Dentro le Stringhe

Supponiamo che vogliate stampare il testo:

```
I like "Monty Python"
```

Come lo fate in Python? Se scrivete semplicemente:

```python
print("I like "Monty Python"")  # ERRORE!
```

Python penserà che la stringa termina alla prima virgoletta dentro il testo, producendo un errore.

#### Soluzione 1: L'Escape Character (Barra Rovesciata)

Usate il **carattere di escape** `\` per "scappare" la virgoletta interna:

```python
print("I like \"Monty Python\"")  # Corretto
```

La barra rovesciata dice a Python: "Il prossimo carattere non è speciale, è solo una virgoletta letterale".

#### Soluzione 2: Mischiate i Tipi di Virgolette

Se la stringa contiene virgolette doppie, circondatela con singole, e viceversa:

```python
print('I like "Monty Python"')   # Corretto - niente escape necessario
print("It's a beautiful day")    # Corretto - apostrofo dentro doppie virgolette
```

Questa è spesso la soluzione più pulita e leggibile.

### Apostrofi Dentro le Stringhe

Lo stesso principio vale per gli apostrofi. Se volete stampare:

```
I'm a programmer
```

Potete scrivere:

```python
print("I'm a programmer")        # Corretto - apostrofo dentro doppie virgolette
print('I\'m a programmer')       # Corretto - apostrofo scappato dentro singole
```

La prima opzione è più leggibile.

### Stringhe Vuote

Una stringa non deve contenere necessariamente caratteri. Una stringa vuota è ancora una stringa:

```python
stringa_vuota = ""
stringa_vuota_singola = ''

print(stringa_vuota)      # Output: (riga vuota)
print(len(stringa_vuota)) # Output: 0
```

Le stringhe vuote sono più utili di quanto possa sembrare. Sono usate per inizializzare variabili, come placeholder, o per verificare se un testo è stato inserito.

### Concatenazione Semplice (Anteprima)

Potete combinare stringhe con il segno `+`:

```python
nome = "Alice"
print("Ciao, " + nome)  # Output: Ciao, Alice
```

Lo vedremo più approfonditamente nel prossimo capitolo.

## 2.2.5 I Valori Booleani: Vero e Falso

### Introduzione ai Booleani

Finora abbiamo incontrato tre tipi di letterali: interi, float, e stringhe. Esiste un quarto tipo che rappresenta qualcosa di molto astratto: la **verità**.

Un **valore booleano** rappresenta uno di due stati: vero oppure falso. Non c'è mezzo. Non c'è "forse". È l'uno o l'altro.

Il nome viene da **George Boole** (1815-1864), un matematico che ha sviluppato l'algebra booleana—un sistema di logica basato su due stati: vero (1) e falso (0).

### Vero e Falso in Python

In Python, i due valori booleani sono rappresentati come:

```python
print(True)
print(False)
```

Notate le **maiuscole**. In Python, `True` e `False` sono **parole riservate** e devono essere scritte esattamente così. `true`, `false`, `TRUE`, `FALSE` sono tutte errate.

### I Booleani Nelle Domande

I valori booleani emergono naturalmente quando fate domande ai dati:

```python
print(5 > 3)        # Output: True (cinque è maggiore di tre)
print(5 < 3)        # Output: False (cinque non è minore di tre)
print(5 == 5)       # Output: True (cinque è uguale a cinque)
print(5 != 3)       # Output: True (cinque non è uguale a tre)
```

Quando confrontate due valori, Python risponde con un booleano: `True` o `False`. Questa risposta è deterministica—non dipende dall'opinione, è una fact logico.

### Un Esperimento Interessante

Considerata questa domanda: "Vero è maggiore di Falso?"

```python
print(True > False)
```

Output:
```
True
```

Internamente, Python tratta `True` come il numero 1 e `False` come il numero 0. Quindi la domanda diventa "1 > 0?", la cui risposta è `True`.

Allo stesso modo:

```python
print(True == 1)         # Output: True
print(False == 0)        # Output: True
print(True + True)       # Output: 2 (1 + 1)
print(True + False)      # Output: 1 (1 + 0)
```

Anche se i booleani e i numeri sono diversi concettualmente, Python ha costruito un ponte tra loro per comodità.

### Perché I Booleani Sono Importanti

I booleani sono il fondamento della programmazione. Ogni volta che un programma prende una decisione ("Se questo è vero, fai quello"), usa un booleano. Sono il linguaggio della logica computazionale.

Nel prossimo capitolo, vedrete come usare i booleani con le istruzioni `if` per controllare il flusso di esecuzione del vostro programma. Per ora, ricordate semplicemente che i booleani sono il modo di Python di rappresentare sì/no, vero/falso, acceso/spento.

## Conclusione: Tipi di Dati e Forme di Letterali

In questa sezione, abbiamo visto che ogni dato ha una **forma** e un **tipo**. La forma è come lo scrivete (con virgolette, con un punto decimale, ecc.). Il tipo è come Python lo interpreta internamente (stringa, intero, float, booleano).

Questa distinzione è fondamentale perché il tipo di un dato determina:
- Come viene immagazzinato in memoria
- Quali operazioni potete effettuare su di esso
- Come Python lo visualizza

Abbiamo anche visto che Python è intelligente nel riconoscere i tipi: se scrivete `123`, sa che è un intero. Se scrivete `"123"`, sa che è una stringa. Se scrivete `123.0`, sa che è un float. Se scrivete `True`, sa che è un booleano.

Questa capacità di Python di capire automaticamente il tipo di un letterale è una delle sue caratteristiche più eleganti. Linguaggi meno potenti richiedono di dire esplicitamente "questo è un intero" o "questo è una stringa". Python lo capisce dal contesto.

Nei capitoli successivi, impareremo a combinare questi letterali in espressioni complesse, a memorizzarli in variabili, e a farli interagire attraverso operatori. Ma il fondamento rimane sempre lo stesso: i letterali sono i dati grezzi che comunicate direttamente nel vostro codice.

Capire i letterali è capire il linguaggio stesso. Sono il vostro modo di dire a Python: "Eccomi qui un numero, una stringa, una verità". E Python risponde appropriatamente.