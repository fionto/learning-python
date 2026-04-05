# Capitolo 1: Sezione 1.4 — Gli Operatori Bitwise

## Introduzione: quando il computer parla in binario

Fino a questo punto del corso avete imparato a usare Python per fare calcoli, confrontare valori e comunicare con l'utente attraverso la console. Tutti questi strumenti operano a un livello che potremmo chiamare "umano": lavoriamo con numeri interi come 42, con testi come `"ciao"`, con valori veri o falsi. Eppure, sotto questa superficie familiare, il computer non vede nulla di tutto questo. Vede soltanto una lunghissima sequenza di zero e uno: i **bit**.

Pensate a una serie di interruttori della luce in un corridoio: ogni interruttore può essere acceso (1) o spento (0). Un singolo interruttore da solo può codificare pochissime informazioni. Ma se ne mettete otto in fila, avete già 256 combinazioni possibili, più che sufficienti per rappresentare tutti i caratteri dell'alfabeto latino. I computer sfruttano esattamente questa logica: raggruppano i bit in insiemi di otto (i cosiddetti **byte**) e li combinano in sequenze sempre più lunghe per rappresentare testi, immagini, suoni, qualsiasi tipo di dato.

Gli **operatori bitwise** sono gli strumenti che Python vi offre per lavorare direttamente su questi interruttori, bit per bit. A differenza degli operatori aritmetici che avete già visto (`+`, `-`, `*`, `/`), gli operatori bitwise non si preoccupano del valore complessivo di un numero: agiscono su ogni singola cifra binaria in modo indipendente. Questa dispensa è una dispensa di approfondimento: l'argomento non è al centro dell'esame PCEP-30-02, ma una comprensione solida del sistema binario e del funzionamento dei bit vi renderà programmatori molto più consapevoli e vi aprirà le porte verso aree importanti come la crittografia, i protocolli di rete, la programmazione embedded e la compressione dei dati.

**Prerequisiti:** questa dispensa assume che abbiate già familiarità con i tipi di dato interi e booleani (Sezione 1.3), con gli operatori aritmetici e le loro precedenze, e con i costrutti di input/output della Sezione 1.5.

---

## Il sistema binario in cinque minuti

Prima di incontrare i veri protagonisti di questa dispensa, vale la pena fermarsi un momento sul sistema binario, perché è il terreno su cui tutti gli operatori bitwise lavorano.

Nel sistema decimale che usate ogni giorno, ogni cifra di un numero occupa una *posizione* che vale una potenza di dieci: le unità, le decine, le centinaia, e così via. Il numero 347 si legge come tre centinaia più quattro decine più sette unità. Il sistema binario funziona esattamente allo stesso modo, ma al posto delle potenze di dieci usa le potenze di due. Ogni cifra binaria, chiamata **bit**, può valere solo 0 oppure 1.

Prendete il numero binario `1011`. Leggendolo da destra a sinistra, la prima cifra vale 1 (cioè 2⁰ = 1), la seconda vale 1 (2¹ = 2), la terza vale 0 (2² = 4, ma il bit è 0, quindi contribuisce per zero), la quarta vale 1 (2³ = 8). Il risultato è 8 + 0 + 2 + 1 = 11 in decimale. Non è difficile: è solo un modo diverso di scrivere lo stesso numero.

Python vi permette di scrivere i numeri direttamente in notazione binaria usando il prefisso `0b`. Potete anche usare la funzione built-in `bin()` per vedere la rappresentazione binaria di qualsiasi intero:

```python
# Scrittura diretta di un numero binario
numero = 0b1011
print(numero)        # Stampa: 11

# Conversione di un decimale in stringa binaria
print(bin(11))       # Stampa: 0b1011
print(bin(255))      # Stampa: 0b11111111

# Lunghezza in bit di un intero
print((42).bit_length())   # Stampa: 6  (42 in binario è 101010)
```

È utile ricordare alcune potenze di due a memoria: 2⁰ = 1, 2¹ = 2, 2² = 4, 2³ = 8, 2⁴ = 16, 2⁷ = 128, 2⁸ = 256. Questi numeri compariranno spesso ogni volta che lavorerete a basso livello.

Un'osservazione importante riguarda il modo in cui Python gestisce gli interi negativi. A differenza di molti altri linguaggi, Python non usa un numero fisso di bit per i suoi interi: può crescere quanto serve per contenere qualsiasi valore. Questo rende i calcoli bitwise su negativi leggermente diversi da quello che ci si potrebbe aspettare venendo da linguaggi come C o Java, come vedremo a breve.

---

## I sei operatori bitwise di Python

Python dispone di sei operatori bitwise, elencati qui con la loro sintassi:

| Operatore | Simbolo | Tipo      |
|-----------|---------|-----------|
| AND       | `&`     | binario   |
| OR        | `\|`    | binario   |
| XOR       | `^`     | binario   |
| NOT       | `~`     | unario    |
| Shift sinistro | `<<` | binario |
| Shift destro   | `>>` | binario |

Ognuno di questi operatori esiste anche nella forma abbreviata per l'assegnazione composta: `&=`, `|=`, `^=`, `<<=`, `>>=`. Queste forme funzionano esattamente come i loro analoghi aritmetici `+=` e `-=`: aggiornano il valore della variabile a sinistra applicando l'operazione.

---

## AND, OR e XOR: la logica booleana applicata ai bit

I primi tre operatori che esaminiamo (AND, OR, XOR) funzionano in modo identico ai loro corrispettivi logici `and`, `or` e al concetto di "o esclusivo", ma li applicano in *parallelo* a ogni coppia di bit nella stessa posizione dei due operandi. Immaginate di avere due mazzi di carte affiancati, ognuno aperto su una pagina diversa: gli operatori bitwise confrontano la prima carta del mazzo A con la prima carta del mazzo B, poi la seconda con la seconda, e così via, senza mai mescolare le posizioni.

**L'operatore AND (`&`)** produce un 1 in una posizione soltanto se *entrambi* i bit corrispondenti valgono 1. In tutti gli altri casi il risultato è 0.

```python
# 12 in binario è 00001100
# 10 in binario è 00001010
# AND            00001000  (solo le posizioni dove ENTRAMBI sono 1)

a = 12   # 0b00001100
b = 10   # 0b00001010
print(a & b)        # Stampa: 8
print(bin(a & b))   # Stampa: 0b1000
```

**L'operatore OR (`|`)** produce un 1 in una posizione se *almeno uno* dei due bit corrispondenti vale 1. Il risultato è 0 solo quando entrambi i bit sono 0.

```python
# 12 in binario è 00001100
# 10 in binario è 00001010
# OR             00001110  (1 dove ALMENO UNO è 1)

a = 12   # 0b00001100
b = 10   # 0b00001010
print(a | b)        # Stampa: 14
print(bin(a | b))   # Stampa: 0b1110
```

**L'operatore XOR (`^`)**, detto "OR esclusivo", produce un 1 in una posizione se i due bit corrispondenti sono *diversi* tra loro: uno vale 0 e l'altro vale 1. Se entrambi sono uguali (entrambi 0 oppure entrambi 1), il risultato è 0. Lo XOR è particolarmente utile in crittografia e nel rilevamento degli errori, proprio perché "accende" i bit in cui due valori differiscono.

```python
# 12 in binario è 00001100
# 10 in binario è 00001010
# XOR            00000110  (1 dove i bit sono DIVERSI)

a = 12   # 0b00001100
b = 10   # 0b00001010
print(a ^ b)        # Stampa: 6
print(bin(a ^ b))   # Stampa: 0b110
```

Una proprietà elegante dello XOR è che applicarlo due volte con lo stesso valore riporta al valore originale: `(a ^ b) ^ b == a`. Questo è il principio alla base di alcuni algoritmi di cifratura elementari.

Le tavole di verità riassumono il comportamento dei tre operatori per ogni combinazione possibile di bit:

| Bit A | Bit B | A & B | A \| B | A ^ B |
|-------|-------|-------|--------|-------|
| 0     | 0     | 0     | 0      | 0     |
| 0     | 1     | 0     | 1      | 1     |
| 1     | 0     | 0     | 1      | 1     |
| 1     | 1     | 1     | 1      | 0     |

---

## NOT: l'operatore unario che ribalta tutto

L'operatore NOT bitwise (`~`) è l'unico **unario** tra i sei: prende un solo operando e ne inverte tutti i bit, trasformando ogni 0 in 1 e ogni 1 in 0. È come girare contemporaneamente tutti gli interruttori del corridoio.

Il risultato in Python potrebbe sorprendervi la prima volta:

```python
a = 12      # 0b00001100
print(~a)   # Stampa: -13
```

Perché −13 e non 243 (come ci si potrebbe aspettare invertendo tutti gli otto bit di un byte)? La risposta sta nel modo in cui Python rappresenta i numeri negativi: usa la convenzione del **complemento a due**, secondo la quale `~n` equivale sempre a `-(n + 1)`. Questa formula è facile da ricordare: NOT di 0 è −1, NOT di 1 è −2, NOT di 12 è −13, NOT di 100 è −101.

```python
print(~0)    # Stampa: -1
print(~1)    # Stampa: -2
print(~-1)   # Stampa: 0   (simmetria: NOT di -1 ritorna 0)
print(~100)  # Stampa: -101
```

Un'avvertenza importante: in Python 3.12 è stata deprecata e nelle versioni successive sarà rimossa la possibilità di usare `~` direttamente su valori booleani (`True` e `False`). Se avete bisogno di negare logicamente un booleano, usate sempre l'operatore logico `not`.

---

## Gli operatori di shift: moltiplicare e dividere in binario

Gli ultimi due operatori bitwise spostano i bit di un numero verso sinistra o verso destra di un certo numero di posizioni. Immaginate la sequenza di bit come una fila di tessere del domino: lo shift le fa scorrere tutte insieme in una direzione, aggiungendo zeri dall'altro lato.

**Lo shift sinistro (`<<`)** sposta tutti i bit verso sinistra di *n* posizioni, riempiendo le posizioni libere a destra con zeri. Ogni spostamento di una posizione equivale a moltiplicare il numero per 2; spostarsi di *n* posizioni equivale a moltiplicare per 2ⁿ. Questo è molto più veloce di una vera moltiplicazione perché il processore non deve eseguire alcun calcolo aritmetico: sposta semplicemente i bit.

```python
valore = 3      # 0b11  (in binario: ...00000011)

# Shift di 1 posizione a sinistra: equivale a moltiplicare per 2
print(valore << 1)   # Stampa: 6   (0b110)

# Shift di 2 posizioni a sinistra: equivale a moltiplicare per 4
print(valore << 2)   # Stampa: 12  (0b1100)

# Shift di 3 posizioni a sinistra: equivale a moltiplicare per 8
print(valore << 3)   # Stampa: 24  (0b11000)
```

**Lo shift destro (`>>`)** sposta tutti i bit verso destra di *n* posizioni. I bit che "escono" a destra vengono semplicemente scartati, mentre le posizioni libere a sinistra vengono riempite con zeri (per i numeri positivi). Ogni spostamento di una posizione equivale a dividere il numero per 2 e scartare il resto (divisione intera).

```python
valore = 24     # 0b11000

# Shift di 1 posizione a destra: equivale a divisione intera per 2
print(valore >> 1)   # Stampa: 12  (0b1100)

# Shift di 2 posizioni a destra: equivale a divisione intera per 4
print(valore >> 2)   # Stampa: 6   (0b110)

# Shift di 3 posizioni a destra: equivale a divisione intera per 8
print(valore >> 3)   # Stampa: 3   (0b11)

# Se si sposta troppo, si perde tutto
print(valore >> 10)  # Stampa: 0
```

Vale la pena notare che Python non ha un operatore di shift destro *non con segno* (nei linguaggi C o Java esiste come `>>>`): in Python, lo shift a destra di un numero negativo continua a propagare il bit di segno verso sinistra, mantenendo il numero negativo.

```python
print(-8 >> 1)   # Stampa: -4   (il segno viene preservato)
```

---

## Precedenza degli operatori bitwise

Come tutti gli operatori Python, anche quelli bitwise hanno una precedenza che determina l'ordine di valutazione in un'espressione che ne contiene più di uno. La tabella seguente mostra la priorità in ordine decrescente (da più alta a più bassa) per i soli operatori bitwise nel contesto degli operatori più comuni:

| Priorità (alta → bassa) | Operatori                        |
|-------------------------|----------------------------------|
| più alta                | `~` (NOT, unario)                |
| ↓                       | `<<`, `>>` (shift)               |
| ↓                       | `&` (AND)                        |
| ↓                       | `^` (XOR)                        |
| più bassa (tra bitwise) | `\|` (OR)                        |

Questo significa che `a & b | c ^ d` viene valutato come `(a & b) | (c ^ d)`. Tuttavia, come per gli operatori aritmetici, il consiglio pratico è sempre lo stesso: se avete dubbi, usate le parentesi esplicite per rendere il codice più leggibile e inequivocabile.

Un errore molto comune tra i principianti è confondere gli operatori bitwise con quelli logici. Ricordate: `&` non è `and`, `|` non è `or`, `~` non è `not`. I primi lavorano bit per bit su interi; i secondi valutano espressioni booleane intere e possono cortocircuitare la valutazione.

```python
# Differenza fondamentale tra & e and
x = 5
y = 0

# Logico: se x è truthy e y è falsy, il risultato è y (ovvero 0)
print(x and y)   # Stampa: 0

# Bitwise: opera sui singoli bit di x e y
# 5 in binario è 101, 0 in binario è 000, AND = 000
print(x & y)     # Stampa: 0

# Ma attenzione: i risultati non sono sempre identici!
a = 6   # 0b110
b = 3   # 0b011
print(a and b)   # Stampa: 3  (b, perché a è truthy)
print(a & b)     # Stampa: 2  (0b010, AND bit per bit)
```

---

## Le bitmask: un uso pratico degli operatori bitwise

Una delle applicazioni più classiche degli operatori bitwise è la **bitmask** (maschera di bit): una tecnica che consente di leggere, impostare, azzerare o invertire uno specifico bit all'interno di un numero, senza toccare gli altri.

Immaginate di dover memorizzare in una singola variabile intera una serie di flag booleani (per esempio: "l'utente è amministratore?", "l'utente è attivo?", "l'utente ha accettato i termini?"). Invece di usare tre variabili separate, potete usare un solo intero e assegnare un bit diverso a ciascun flag.

```python
# Definiamo tre flag come potenze di 2 (ognuna occupa un solo bit)
FLAG_ADMIN   = 0b001   # bit 0: valore 1
FLAG_ATTIVO  = 0b010   # bit 1: valore 2
FLAG_TERMINI = 0b100   # bit 2: valore 4

# Partiamo da un utente senza nessun permesso
permessi = 0b000

# --- Impostare un bit (SET): usare OR con la maschera ---
permessi = permessi | FLAG_ATTIVO
print(bin(permessi))   # Stampa: 0b10  (solo FLAG_ATTIVO è attivo)

# Aggiungere anche il flag TERMINI
permessi |= FLAG_TERMINI
print(bin(permessi))   # Stampa: 0b110

# --- Leggere un bit (GET): usare AND con la maschera ---
# Se il risultato è diverso da 0, il bit è acceso
if permessi & FLAG_ADMIN:
    print("È amministratore")
else:
    print("Non è amministratore")   # Questo viene stampato

if permessi & FLAG_ATTIVO:
    print("È attivo")               # Questo viene stampato

# --- Azzerare un bit (CLEAR): usare AND con il NOT della maschera ---
# ~FLAG_ATTIVO inverte tutti i bit di FLAG_ATTIVO,
# lasciando a 1 tutte le altre posizioni
permessi = permessi & ~FLAG_ATTIVO
print(bin(permessi))   # Stampa: 0b100  (FLAG_ATTIVO è stato rimosso)

# --- Invertire un bit (TOGGLE): usare XOR con la maschera ---
# Se il bit era 1 diventa 0, se era 0 diventa 1
permessi = permessi ^ FLAG_TERMINI
print(bin(permessi))   # Stampa: 0b0   (FLAG_TERMINI è stato invertito)
permessi = permessi ^ FLAG_TERMINI
print(bin(permessi))   # Stampa: 0b100  (invertito di nuovo, ritorna)
```

Questo schema di SET, GET, CLEAR e TOGGLE è estremamente diffuso nella programmazione di sistemi embedded, nei protocolli di comunicazione seriale (come il Modbus RTU che usano i sistemi industriali), nella gestione dei permessi su file Unix, e ovunque sia necessario memorizzare molti flag booleani in modo compatto ed efficiente.

---

## Conversione tra binario e intero

Python offre due strumenti immediati per navigare tra rappresentazione binaria e intera: la funzione `bin()`, che avete già incontrato, e la funzione `int()` con l'argomento `base`.

```python
# Da intero a stringa binaria
print(bin(42))        # Stampa: '0b101010'

# Da stringa binaria a intero (specificando base 2)
print(int('101010', 2))    # Stampa: 42
print(int('0b101010', 2))  # Stampa: 42  (il prefisso 0b è accettato)

# Analoghe funzioni esistono per ottale (oct, base 8)
# ed esadecimale (hex, base 16)
print(oct(42))        # Stampa: '0o52'
print(hex(42))        # Stampa: '0x2a'
print(int('2a', 16))  # Stampa: 42
```

L'esadecimale (base 16) merita un cenno: ogni cifra esadecimale corrisponde esattamente a quattro bit, il che rende la notazione esadecimale molto più compatta della binaria pur mantenendo una corrispondenza diretta con i bit sottostanti. Per questo motivo, i valori esadecimali sono onnipresenti nella documentazione di hardware, nei dump di memoria e nei protocolli di rete.

---

## Conclusione: la macchina sotto il cappotto

Gli operatori bitwise sono come la fondamenta di un edificio: quasi sempre invisibili, ma portanti. Nella programmazione di tutti i giorni incontrerete raramente la necessità di manipolare i bit direttamente, a meno che non lavoriate con hardware, protocolli di comunicazione, crittografia o strutture dati compatte. Eppure, sapere come funzionano vi darà una comprensione molto più profonda di ciò che il vostro programma sta facendo davvero, e vi permetterà di leggere e capire codice scritto da altri in questi domini specialistici.

Vale la pena tenere a mente le quattro operazioni fondamentali sulle bitmask: impostare un bit con OR (`|`), leggere un bit con AND (`&`), azzerarlo con AND e NOT (`& ~`), invertirlo con XOR (`^`). Queste quattro ricette, insieme alla comprensione degli shift come moltiplicazioni e divisioni per potenze di due, coprono la grande maggioranza degli usi pratici.

Il passo successivo, nella progressione del corso, sarà approfondire gli operatori relazionali e booleani (anch'essi parte della voce 1.4 del syllabus), che operano a un livello più alto rispetto ai bitwise: invece di agire sui singoli bit, confrontano interi valori e producono risultati di tipo booleano che guidano il flusso di controllo dei vostri programmi. Troverete molte analogie con quanto avete visto qui, ma anche differenze importanti che vale la pena esplorare con attenzione.
