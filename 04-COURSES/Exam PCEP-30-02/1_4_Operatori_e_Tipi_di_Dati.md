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
