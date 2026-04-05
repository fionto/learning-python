# Capitolo 1: Sezione 1.4 – Operatori e Tipi di Dati: Il Calcolatore Universale

## Introduzione: Più di una Semplice Calcolatrice

Immaginate di essere al banco di un mercato ortofrutticolo. Avete tre chili di mele a 1,50 € al chilo, e volete sapere quanto spenderete. Fate il conto mentalmente: 3 volte 1,50 fa 4,50. Poi ricordate che avete un buono sconto del 10%, quindi calcolate il 10% di 4,50 (0,45) e lo sottraete. Il totale finale è 4,05 €. In pochi secondi avete eseguito una moltiplicazione, una divisione, una sottrazione, e avete anche confrontato due quantità (il prezzo prima e dopo lo sconto).

Python fa esattamente questo: prende dei valori, li combina attraverso operatori, e produce risultati. Ma a differenza di una semplice calcolatrice tascabile, Python dispone di una famiglia molto più ricca di operatori: non solo quelli aritmetici che conoscete dalla scuola, ma anche operatori per confrontare valori, per costruire ragionamenti logici, e persino per manipolare i bit interni dei numeri. Questa dispensa vi porta in giro per tutta questa famiglia, mostrandovi come i diversi operatori si combinano e quale precedenza ha ciascuno rispetto agli altri.

Un prerequisito fondamentale: la dispensa assume che abbiate già familiarità con i letterali numerici (interi, float, booleani), le variabili, e il concetto di tipo di dato, trattati nella sezione 1.3. Gli operatori sono, in fondo, i verbi della lingua Python: hanno bisogno dei sostantivi (i valori e le variabili) per dire qualcosa di sensato.

## Gli Operatori Aritmetici: La Matematica di Tutti i Giorni

Python riconosce i classici operatori aritmetici, più qualche aggiunta utile. Partiamo dall'insieme di base:

```python
# Addizione e sottrazione
a = 10 + 3    # a vale 13
b = 10 - 3    # b vale 7

# Moltiplicazione
c = 10 * 3    # c vale 30

# Esponenziazione: ** eleva a potenza
d = 2 ** 10   # d vale 1024 (2 alla decima)
```

Fin qui niente di sorprendente. Le novità arrivano con la divisione, che in Python esiste in due varianti:

```python
# Divisione vera: restituisce sempre un float
e = 10 / 3    # e vale 3.3333... (tipo float)
f = 9 / 3     # f vale 3.0, NON 3 (ancora float!)

# Divisione intera (floor division): restituisce la parte intera
g = 10 // 3   # g vale 3 (tipo int)
h = 10 // -3  # h vale -4 (arrotonda verso meno infinito, non verso zero)
```

La distinzione tra `/` e `//` sorprende spesso i principianti. In Python 3, la barra singola produce sempre un numero decimale, anche se la divisione è esatta. La doppia barra tronca verso il basso: con numeri positivi si comporta come un "taglia la virgola", ma con numeri negativi il risultato è leggermente diverso da quanto ci si potrebbe aspettare (−10 // 3 fa −4, non −3).

Il terzo operatore della divisione è il modulo, rappresentato da `%`:

```python
# Modulo: restituisce il resto della divisione intera
i = 10 % 3    # i vale 1 (10 = 3*3 + 1, il resto è 1)
j = 9 % 3     # j vale 0 (9 è divisibile per 3 senza resto)

# Applicazione pratica: capire se un numero è pari o dispari
numero = 17
if numero % 2 == 0:
    print("pari")
else:
    print("dispari")   # Stampa: dispari
```

Il modulo è più utile di quanto sembri: consente di verificare la divisibilità, di lavorare con angoli circolari, o di ciclare attraverso una sequenza di valori senza andare fuori dai limiti.

### Operatori su Stringhe

Due degli operatori aritmetici hanno un significato speciale anche quando applicati alle stringhe:

```python
# Concatenazione con +
saluto = "Ciao" + " " + "mondo"
print(saluto)   # Stampa: Ciao mondo

# Ripetizione con *
riga = "-" * 20
print(riga)     # Stampa: --------------------

# Attenzione: non si possono sommare stringa e numero direttamente
# "Ciao" + 3   # Questo produce un errore TypeError
```

L'operatore `+` tra stringhe le incolla in sequenza; l'operatore `*` tra una stringa e un intero la ripete quel numero di volte. Mescolate i due senza conversione esplicita e Python protesterà con un errore di tipo.

## Operatori Unari e Binari: Quanti Operandi?

Prima di affrontare la priorità, è utile distinguere tra operatori **binari** (che agiscono su due valori) e operatori **unari** (che agiscono su uno solo). La maggior parte di quelli visti finora sono binari: `3 + 5` richiede due operandi, `10 // 3` anche.

Gli operatori unari in aritmetica sono il più (`+`) e il meno (`-`) usati come segno:

```python
x = 5
print(-x)   # Stampa: -5 (negazione unaria)
print(+x)   # Stampa:  5 (positivo unario, quasi sempre inutile ma lecito)

y = -x      # y vale -5
z = -(-x)   # z vale 5 (doppia negazione)
```

In Python, il segno meno unario ha una precedenza molto elevata: viene applicato prima delle operazioni aritmetiche binarie. Vale la pena tenere presente questo quando si costruiscono espressioni con potenze: `−2 ** 2` in Python restituisce `−4`, non `4`, perché `**` viene valutato prima dell'unario meno.

## Priorità e Binding: Chi Va Prima?

Torniamo all'analogia del mercato: se dite "tre chili di mele più due chili di pere per 1,20 €", la frase è ambigua. Si intende `(3 + 2) * 1.20` oppure `3 + (2 * 1.20)`? In matematica, per convenzione si moltiplica prima di sommare. Python segue regole simili, chiamate **regole di priorità** (o precedenza).

La tabella seguente riassume i principali operatori in ordine dalla priorità più alta alla più bassa:

| Priorità | Operatore(i) | Descrizione |
|----------|-------------|-------------|
| 1 (alta) | `**` | Esponenziazione |
| 2 | `+x`, `-x`, `~x` | Unari: positivo, negativo, NOT bitwise |
| 3 | `*`, `/`, `//`, `%` | Moltiplicazione, divisioni, modulo |
| 4 | `+`, `-` | Addizione, sottrazione |
| 5 | `<<`, `>>` | Shift bitwise |
| 6 | `&` | AND bitwise |
| 7 | `^` | XOR bitwise |
| 8 | `\|` | OR bitwise |
| 9 | `==`, `!=`, `<`, `<=`, `>`, `>=` | Confronto relazionale |
| 10 | `not` | NOT logico (unario) |
| 11 | `and` | AND logico |
| 12 (bassa) | `or` | OR logico |

Quando due operatori hanno la stessa priorità, entra in gioco il **binding**: quasi tutti gli operatori sono **left-binding**, cioè vengono valutati da sinistra a destra. L'eccezione notevole è `**`, che è **right-binding**: `2 ** 3 ** 2` si valuta come `2 ** (3 ** 2)` = `2 ** 9` = 512, non come `(2 ** 3) ** 2` = 64.

```python
# Esempi di precedenza
risultato = 2 + 3 * 4      # 2 + 12 = 14, NON 5 * 4 = 20
print(risultato)            # Stampa: 14

risultato2 = (2 + 3) * 4   # Le parentesi forzano l'addizione prima
print(risultato2)           # Stampa: 20

# Right-binding dell'esponenziazione
print(2 ** 3 ** 2)          # Stampa: 512 (2 ** 9)
print((2 ** 3) ** 2)        # Stampa: 64  (8 ** 2)
```

Quando avete dubbi sulla precedenza, usate le parentesi: rendono il codice più chiaro e non hanno alcun costo.

## Operatori di Assegnazione e le Forme Abbreviate

L'operatore di assegnazione `=` non va confuso con il confronto di uguaglianza `==`. L'assegnazione collega un nome a un valore; il confronto restituisce True o False.

Spesso si incontrano costrutti del tipo "aggiungi 5 alla variabile x". Python offre una forma abbreviata per tutte le operazioni aritmetiche (e bitwise):

```python
x = 10

x += 5     # equivale a x = x + 5 → x vale 15
x -= 3     # equivale a x = x - 3 → x vale 12
x *= 2     # equivale a x = x * 2 → x vale 24
x //= 5    # equivale a x = x // 5 → x vale 4
x **= 3    # equivale a x = x ** 3 → x vale 64
x %= 10    # equivale a x = x % 10 → x vale 4

print(x)   # Stampa: 4
```

Questi operatori abbreviati non sono semplicemente zucchero sintattico per risparmiare battute: indicano chiaramente l'intenzione di aggiornare una variabile esistente, rendendo il codice più espressivo.

## Operatori Relazionali: Confrontare Valori

Gli operatori relazionali confrontano due valori e restituiscono un booleano: `True` se la relazione è soddisfatta, `False` altrimenti.

```python
a = 10
b = 3

print(a == b)   # False: a non è uguale a b
print(a != b)   # True:  a è diverso da b
print(a > b)    # True:  a è maggiore di b
print(a >= b)   # True:  a è maggiore o uguale a b
print(a < b)    # False: a non è minore di b
print(a <= b)   # False: a non è minore o uguale a b
```

Python permette di concatenare i confronti in modo elegante, seguendo la notazione matematica:

```python
numero = 7
print(0 < numero < 10)   # True: numero è nell'intervallo aperto (0, 10)
print(1 <= numero <= 5)  # False: numero non è nell'intervallo [1, 5]
```

Questa forma è molto più leggibile dell'equivalente `numero > 0 and numero < 10`, ed è idiomatica in Python.

## Operatori Booleani: Ragionamento Logico

Gli operatori booleani (`and`, `or`, `not`) combinano valori o espressioni booleane per costruire condizioni composite. Se vi siete già imbattuti nella sezione 1.4 dell'esempio sulla logica booleana e sui bitwise, troverete qui una sintesi che li inserisce nel quadro complessivo della precedenza.

```python
# and: vero solo se entrambi sono True
print(True and True)    # True
print(True and False)   # False

# or: vero se almeno uno è True
print(False or True)    # True
print(False or False)   # False

# not: inverte il valore
print(not True)         # False
print(not False)        # True
```

Un comportamento interessante degli operatori `and` e `or` in Python è la **valutazione cortocircuitata** (short-circuit evaluation): se il risultato può essere determinato dal primo operando, il secondo non viene nemmeno valutato.

```python
# and: se il primo è False, il secondo non viene valutato
x = 0
if x != 0 and 10 / x > 1:   # Sicuro: la divisione avviene solo se x != 0
    print("condizione vera")

# or: se il primo è True, il secondo non viene valutato
y = 5
if y > 0 or y / 0 > 1:      # Il secondo ramo non viene mai eseguito
    print("condizione vera")  # Stampa: condizione vera
```

Questa proprietà è molto utile per scrivere condizioni sicure che evitino divisioni per zero o accessi a oggetti nulli.

## Quando il Vero vale Uno

Immaginate un interruttore della luce. Può essere acceso oppure spento: due soli stati possibili, nessuna via di mezzo. Ora immaginate che qualcuno vi chieda: "Quanti interruttori sono accesi in questa stanza?" Per rispondere, dovete *contare* qualcosa che prima era solo una condizione logica. Questo passaggio, dal concetto di "acceso/spento" alla quantità numerica, rispecchia esattamente ciò che Python fa internamente con il tipo `bool`.

Sappiamo già che Python possiede il tipo `bool` con i due soli valori `True` e `False`. Li abbiamo usati nelle condizioni degli `if`, nelle espressioni logiche con `and`, `or` e `not`, nei confronti con `==` e `!=`. Sembravano entità a sé stanti, distaccate dal mondo dei numeri. Eppure, non è esattamente così.

In Python, `bool` è una **sottoclasse** di `int`. Questa non è solo una curiosità: è una scelta di progettazione deliberata che ha conseguenze concrete sul comportamento del linguaggio. `True` si comporta come il numero intero `1` ogni volta che viene usato in un contesto aritmetico, e `False` si comporta come il numero intero `0`. Questa regola è semplice, ma è uno dei tranelli più frequenti nell'esame PCEP, perché è controintuitiva: ci aspettiamo che `True + True` sollevi un errore, invece Python la esegue serenamente.

## `bool` è una sottoclasse di `int`

Per capire davvero cosa significa, partiamo dalla conferma diretta che Python stesso ci fornisce.

```python
# Verificare la gerarchia di tipo
print(isinstance(True, int))   # Stampa: True
print(isinstance(False, int))  # Stampa: True
print(type(True))              # Stampa: <class 'bool'>
```

`isinstance(True, int)` restituisce `True` perché `bool` eredita da `int`. Non si tratta di una conversione implicita che avviene al volo: `True` *è già* un intero, di valore `1`, avvolto in un tipo più specializzato. Allo stesso modo, `False` *è già* un intero di valore `0`.

Questo significa che tutte le operazioni aritmetiche che funzionano sugli interi funzionano anche sui booleani, senza bisogno di alcuna conversione esplicita.

## Aritmetica con `True` e `False`

Osservate questi esempi con attenzione, perché ciascuno illustra un aspetto diverso del comportamento.

```python
# Addizione di booleani
print(True + True)         # Stampa: 2
print(True + False)        # Stampa: 1
print(False + False)       # Stampa: 0
print(True + True + False) # Stampa: 2
```

Il risultato di `True + True` è l'intero `2`, non il booleano `True`. Questo è il punto critico: quando i booleani partecipano a un'operazione aritmetica, il risultato è un `int`, non un `bool`. Python "promuove" il risultato al tipo più generale della gerarchia.

```python
# Moltiplicazione
print(True * 5)    # Stampa: 5
print(False * 5)   # Stampa: 0
print(True * True) # Stampa: 1
```

`True * 5` produce `5` perché `1 * 5 = 5`. `False * 5` produce `0` perché `0 * 5 = 0`. Questo ha un utilizzo pratico: si può usare un booleano come "interruttore" per includere o escludere un valore da una somma, senza ricorrere a un `if`.

```python
# Un esempio pratico: sommare un valore solo se una condizione è vera
prezzo_base = 100
sconto_attivo = True
sconto = 20

totale = prezzo_base - sconto * sconto_attivo
print(totale)  # Stampa: 80
```

Se `sconto_attivo` fosse `False`, `sconto * False` darebbe `0` e `totale` rimarrebbe `100`. Questo schema è lecito in Python, anche se nella maggior parte dei casi è preferibile usare un `if` esplicito per leggibilità.

Infine, vale la pena verificare il comportamento con la divisione e il modulo.

```python
print(True / True)   # Stampa: 1.0  (divisione reale, risultato float)
print(True // False) # ZeroDivisionError: integer division or modulo by zero
```

`True // False` è identico a `1 // 0` e solleva lo stesso errore. I booleani non sono esenti dalle regole matematiche fondamentali.

## Confronti tra booleani e interi

Poiché `True == 1` e `False == 0`, i confronti tra booleani e interi danno risultati che possono sorprendere chi non conosce questa regola.

```python
print(True == 1)    # Stampa: True
print(False == 0)   # Stampa: True
print(True == 2)    # Stampa: False
print(False == 0.0) # Stampa: True  (0.0 è uguale a 0)
```

Un caso particolarmente insidioso nell'esame è il confronto con stringhe.

```python
print(True == "True")  # Stampa: False
print(False == "")     # Stampa: False
```

La stringa `"True"` non è un intero, quindi il confronto con `True` (che vale `1`) restituisce `False`. Non c'è alcuna conversione automatica tra stringhe e booleani nella comparazione con `==`.

## Valori Truthy e Falsy: la logica del "come se"

Fino ad ora abbiamo parlato di `True` e `False` come valori espliciti. Ma Python ha un meccanismo più ampio: ogni valore di ogni tipo può essere usato in un contesto booleano, come la condizione di un `if`. In quel contesto, Python valuta implicitamente il valore e decide se considerarlo "vero" o "falso".

Torniamo all'analogia degli interruttori, ampliandola. Immaginate che un sistema automatico debba decidere se accendere una pompa basandosi su diversi tipi di sensori: uno restituisce il numero di litri in un serbatoio, uno restituisce il testo di un messaggio di allerta, uno restituisce una lista di anomalie rilevate. In tutti i casi, la domanda sottostante è la stessa: "c'è qualcosa di significativo qui?". Un serbatoio con zero litri dice "no", uno con cento litri dice "sì". Un messaggio vuoto dice "no", un messaggio con testo dice "sì". Python formalizza esattamente questa intuizione.

I valori che Python considera **falsy** (equivalenti a `False` in contesto booleano) sono i seguenti.

| Valore | Tipo | Perché è falsy |
|--------|------|----------------|
| `False` | `bool` | È il falso per definizione |
| `0` | `int` | Lo zero intero |
| `0.0` | `float` | Lo zero in virgola mobile |
| `""` | `str` | La stringa vuota |
| `[]` | `list` | La lista vuota |
| `()` | `tuple` | La tupla vuota |
| `{}` | `dict` | Il dizionario vuoto |
| `None` | `NoneType` | L'assenza di valore |

Tutto il resto è **truthy**: qualsiasi intero diverso da zero, qualsiasi float diverso da zero, qualsiasi stringa non vuota, qualsiasi lista con almeno un elemento, e così via.

```python
# Esempi di valori falsy in un contesto if
if 0:
    print("non verrà mai stampato")

if "":
    print("neanche questo")

if []:
    print("nemmeno questo")

# Esempi di valori truthy
if 42:
    print("42 è truthy")          # Stampa: 42 è truthy

if "ciao":
    print("una stringa è truthy") # Stampa: una stringa è truthy

if [0]:
    print("lista con un elemento è truthy")  # Stampa: lista con un elemento è truthy
```

Notate l'ultimo caso con attenzione: `[0]` è una lista che contiene l'elemento `0`. La lista stessa non è vuota, quindi è truthy, anche se il suo unico contenuto è un valore falsy. Il contesto booleano valuta il *contenitore*, non il suo contenuto.

## La funzione `bool()`: rendere esplicito l'implicito

Qualsiasi valore può essere convertito esplicitamente in `bool` tramite la funzione `bool()`. Questo è utile sia per chiarire l'intenzione nel codice, sia per capire esattamente cosa valuta Python quando incontra un valore in un contesto booleano.

```python
print(bool(0))      # Stampa: False
print(bool(1))      # Stampa: True
print(bool(-5))     # Stampa: True   (qualsiasi intero diverso da zero)
print(bool(0.0))    # Stampa: False
print(bool(0.001))  # Stampa: True
print(bool(""))     # Stampa: False
print(bool("0"))    # Stampa: True   (la stringa "0" non è vuota)
print(bool([]))     # Stampa: False
print(bool([0]))    # Stampa: True
print(bool(None))   # Stampa: False
```

Un caso che sorprende molti è `bool("0")`: la stringa che contiene il carattere zero. Essa è truthy perché è una stringa *non vuota*. Falsy non significa "contiene uno zero" ma "non contiene nulla" oppure "vale numericamente zero" (per i tipi numerici) oppure "è il valore speciale `None`".

## Il tipo del risultato: `bool` o `int`?

Questa distinzione è importante per l'esame. Quando si usa `bool()` esplicitamente, il risultato è di tipo `bool`. Quando si eseguono operazioni aritmetiche su booleani, il risultato è di tipo `int`.

```python
# Risultato di tipo bool
x = bool(1)
print(type(x))        # Stampa: <class 'bool'>
print(x)              # Stampa: True

# Risultato di tipo int (operazione aritmetica)
y = True + True
print(type(y))        # Stampa: <class 'int'>
print(y)              # Stampa: 2

# Confronto: anche il confronto restituisce bool
z = (1 == 1)
print(type(z))        # Stampa: <class 'bool'>
print(z)              # Stampa: True
```

## I tranelli più comuni nell'esame PCEP

Raccolgo qui i pattern che appaiono più frequentemente nelle domande di sezione 1, proprio per consolidare i punti critici.

Il primo riguarda l'addizione di booleani: `True + True` è `2`, non `True`. Il tipo del risultato è `int`, non `bool`.

Il secondo riguarda il confronto con stringhe: `True == "True"` è `False`, e `False == ""` è `False`. I tipi non vengono coercizzati automaticamente nella comparazione.

Il terzo riguarda il valore falsy dei contenitori: `[0]`, `[False]`, `[""]` sono tutti truthy perché le liste non sono vuote, indipendentemente da cosa contengono.

Il quarto riguarda `None`: è sempre falsy, e non è equivalente a `0` né a `False`. `None == False` restituisce `False`.

```python
# Verifica rapida dei quattro tranelli
print(True + True)       # 2, non True
print(True == "True")    # False
print(bool([False]))     # True
print(None == False)     # False
```

Il tipo `bool` in Python non è un'isola isolata nella gerarchia dei tipi: è figlio di `int`, e questa eredità è visibile ogni volta che un booleano partecipa a un calcolo numerico. `True` porta con sé il valore `1`, `False` porta il valore `0`, e quando vengono coinvolti in aritmetica restituiscono interi ordinari.

Al tempo stesso, il meccanismo truthy/falsy estende la logica booleana in direzione opposta: non solo i booleani si comportano come numeri, ma i numeri (e le stringhe, e le liste, e molto altro) si comportano come booleani ogni volta che Python ne ha bisogno. Il confine tra i tipi è permeabile, e capirne le regole permette di leggere codice altrui senza sorprese e di rispondere con sicurezza alle domande dell'esame che sfruttano queste sfumature.

Questi concetti si collegano direttamente alla Sezione 2 del syllabus: nel momento in cui si usano variabili di tipo non booleano come condizioni di `if` o `while`, il meccanismo truthy/falsy entra in gioco automaticamente. Avere già chiaro il quadro completo renderà quella sezione molto più immediata.

## Accuratezza dei Float: Il Problema della Virgola Mobile

Un tema che sorprende quasi tutti i nuovi programmatori è l'imprecisione dei numeri in virgola mobile. I computer rappresentano i float in binario, e alcune frazioni decimali (come 0.1 o 0.3) non possono essere rappresentate esattamente in binario, proprio come 1/3 non può essere scritto esattamente in decimale.

```python
# Il risultato atteso sarebbe 0.3, ma...
print(0.1 + 0.2)          # Stampa: 0.30000000000000004

# Confronto diretto: trappola comune!
print(0.1 + 0.2 == 0.3)   # Stampa: False (!)

# Come confrontare float in modo sicuro
differenza = abs((0.1 + 0.2) - 0.3)
print(differenza < 1e-9)  # Stampa: True (usa una tolleranza)
```

La lezione pratica è semplice: non confrontate mai due float con `==`. Usate sempre un confronto con una soglia di tolleranza (epsilon). Questa non è una stranezza di Python: è una caratteristica di tutti i linguaggi che usano la rappresentazione IEEE 754, ossia praticamente tutti i linguaggi di programmazione moderni.

## Operatori Bitwise: Sotto il Cofano del Calcolatore

Gli operatori bitwise agiscono direttamente sui bit che compongono un numero intero. Sono operatori di basso livello, vicini all'hardware, e trovano applicazione nella programmazione di sistemi, nella gestione di flag hardware, e nell'ottimizzazione di alcune operazioni.

Python offre sei operatori bitwise:

```python
a = 0b1100   # 12 in binario: bit 3 e bit 2 attivi
b = 0b1010   # 10 in binario: bit 3 e bit 1 attivi

# AND bitwise (&): 1 solo dove entrambi hanno 1
print(a & b)    # 0b1000 = 8

# OR bitwise (|): 1 dove almeno uno ha 1
print(a | b)    # 0b1110 = 14

# XOR bitwise (^): 1 dove i bit sono diversi
print(a ^ b)    # 0b0110 = 6

# NOT bitwise (~): inverte tutti i bit (complemento a due)
print(~a)       # -13 (vedi spiegazione sotto)

# Shift a sinistra (<<): sposta i bit verso sinistra, equivale a * 2^n
print(a << 1)   # 0b11000 = 24 (12 * 2)

# Shift a destra (>>): sposta i bit verso destra, equivale a // 2^n
print(a >> 1)   # 0b0110 = 6 (12 // 2)
```

Il NOT bitwise merita una nota: `~a` produce `-(a + 1)`. Questo perché Python usa il complemento a due per i numeri negativi: invertire tutti i bit di 12 produce un numero che nel sistema complemento a due vale −13. È un risultato corretto, anche se all'inizio sembra sorprendente.

Esistono anche le forme abbreviate per i bitwise: `&=`, `|=`, `^=`, `<<=`, `>>=`, che funzionano esattamente come quelle aritmetiche.

## Type Casting: Trasformare un Tipo in un Altro

Spesso si lavora con un valore di un tipo e si ha bisogno di convertirlo in un altro. Questa operazione si chiama **type casting** (o conversione di tipo). Python mette a disposizione alcune funzioni built-in per le conversioni più comuni:

```python
# Da stringa a intero
testo = "42"
numero_intero = int(testo)
print(numero_intero + 1)   # Stampa: 43

# Da stringa a float
testo_decimale = "3.14"
numero_float = float(testo_decimale)
print(numero_float * 2)    # Stampa: 6.28

# Da float a intero: tronca la parte decimale (non arrotonda)
pi_greco = 3.99
intero = int(pi_greco)
print(intero)              # Stampa: 3, non 4!

# Da intero a float
n = 5
come_float = float(n)
print(come_float)          # Stampa: 5.0

# Da intero a stringa
numero = 100
come_stringa = str(numero)
print("Il risultato è: " + come_stringa)   # Stampa: Il risultato è: 100

# Da stringa a booleano: quasi tutto è True
print(bool(""))      # False: stringa vuota
print(bool("ciao"))  # True:  stringa non vuota
print(bool(0))       # False: zero
print(bool(42))      # True:  qualsiasi numero non-zero
```

È importante capire che `int()` **tronca** il float verso lo zero, non lo arrotonda: `int(3.99)` fa 3, `int(-3.99)` fa -3. Se volete l'arrotondamento vero, usate la funzione `round()`.

Il casting fallisce con un'eccezione se la conversione non è possibile:

```python
# Questo produce un errore ValueError
try:
    int("ciao")   # "ciao" non può diventare un numero
except ValueError as e:
    print(f"Errore: {e}")
    # Stampa: Errore: invalid literal for int() with base 10: 'ciao'
```

Gestire questi errori gracefully (con blocchi `try/except`) è buona pratica, ma il suo approfondimento è rimandato alla sezione 4.4 sulle eccezioni.

## Mettere Tutto Insieme: Un Calcolo Reale

A titolo di sintesi, consideriamo un piccolo esempio che combina diversi degli operatori visti:

```python
# Calcolo del prezzo finale con sconto e IVA
prezzo_netto = float(input("Inserisci il prezzo netto: "))  # es. 100.0
sconto_percentuale = 10   # 10% di sconto

# Calcolo del prezzo scontato
prezzo_scontato = prezzo_netto * (1 - sconto_percentuale / 100)

# Aggiunta IVA al 22%
prezzo_finale = prezzo_scontato * 1.22

# Arrotondamento a 2 decimali
prezzo_finale = round(prezzo_finale, 2)

print(f"Prezzo finale (IVA inclusa, sconto {sconto_percentuale}%): {prezzo_finale} €")
# Con input 100.0 → Stampa: Prezzo finale (IVA inclusa, sconto 10%): 109.8 €
```

Leggendo questo frammento, si riconoscono: casting con `float()`, operatori aritmetici `*` e `-`, priorità implicita (la divisione e la sottrazione avvengono nell'ordine corretto grazie alle parentesi), e l'operatore di assegnazione semplice.

## Conclusione: Tutti gli Strumenti sul Banco

Abbiamo fatto un percorso completo attraverso la toolbox degli operatori Python. Partendo dagli aritmetici che già conoscevate dalla scuola, abbiamo visto come la divisione si sdoppi in due varianti (`/` e `//`), come il modulo `%` riveli la divisibilità di un numero, come le stringhe si comportino con `+` e `*`, e come la priorità stabilisca chi va prima quando gli operatori si accumulano in un'espressione.

Abbiamo poi incontrato i comparatori relazionali (che producono booleani), gli operatori logici `and`, `or`, `not` (che ragionano su condizioni composite), e i bitwise (che lavorano sui singoli bit dei numeri interi). Infine, il type casting ci ha mostrato come trasformare un tipo in un altro in modo controllato.

Tutti questi operatori torneranno protagonisti nella sezione successiva, dedicata al flusso di controllo: le istruzioni `if`, `elif`, `else` (sezione 2.1) e i cicli `while` e `for` (sezione 2.2) si appoggiano quasi interamente sugli operatori relazionali e logici per decidere quale ramo di codice eseguire o quando fermarsi. Con la padronanza di questa sezione, siete pronti a costruire i vostri primi programmi realmente interattivi e decisionali.
