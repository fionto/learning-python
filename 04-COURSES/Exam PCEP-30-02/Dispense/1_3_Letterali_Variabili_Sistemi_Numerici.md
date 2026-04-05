# Capitolo 1: Sezione 1.3 - Letterali, Variabili e Sistemi Numerici: Dare un Nome al Mondo

## Introduzione: Il Linguaggio dei Dati

Pensate alla scheda anagrafica che compilate dal medico. Ci sono campi dove scrivete valori precisi e immutabili in quel momento: 'Età: 24 anni', 'Altezza: 1.75 metri', 'Fumatore: No'. Quei valori scritti nero su bianco (24, 1.75, No) sono i **letterali**: rappresentano la realtà concreta in quell'istante. Tuttavia, il medico non ragiona dicendo 'Se 24 è maggiore di 18...'. Il medico guarda l'etichetta del campo, che si chiama 'Età'. Quella etichetta è la **variabile**. È un contenitore con un nome (`età`, `altezza`, `è_fumatore`) che può ospitare valori diversi per pazienti diversi. Oggi per voi la variabile `età` contiene il letterale `24`, domani per un altro paziente conterrà `50`. Programmare significa creare queste schede vuote (variabili) e decidere quali valori concreti (letterali) inserirci dentro per far prendere decisioni al computer.

Questa sezione vi accompagna attraverso i mattoni fondamentali di ogni programma Python: i tipi di dati elementari, il modo in cui Python comprende i numeri scritti in diverse basi, e le convenzioni con cui si dà un nome alle cose nel codice. Se la sezione 1.2 vi ha insegnato la grammatica del linguaggio (keyword, indentazione, commenti), questa sezione vi insegna il vocabolario di base, ossia le parole con cui si descrive la realtà all'interprete.

---

## I Tipi di Dati Elementari: Interi, Float, Booleani e Stringhe

Python è un linguaggio **tipizzato dinamicamente**: non siete voi a dichiarare esplicitamente il tipo di una variabile, come si fa in altri linguaggi come Java o C. È l'interprete che, nel momento in cui esegue l'istruzione, riconosce da solo di che tipo di valore si tratta. Questo rende il codice più rapido da scrivere, ma rende anche più importante capire quali tipi esistono e come si comportano.

### Gli interi (int)

Un intero è un numero senza parte decimale: può essere positivo, negativo, o zero. In Python, gli interi non hanno un limite superiore pratico di grandezza (a differenza di molti altri linguaggi), quindi potete scrivere numeri enormi senza preoccuparvi di trabocchi di memoria.

```python
# Letterali interi: numeri scritti direttamente nel codice
anno = 2025
temperatura_in_gradi = -8
zero = 0
numero_molto_grande = 1000000000000

# Python stampa il tipo di una variabile con la funzione type()
print(type(anno))   # Stampa: <class 'int'>
```

Una convenzione visiva molto utile, introdotta in Python 3.6, è l'uso del carattere underscore `_` come separatore delle migliaia. È puramente decorativo per il lettore umano: l'interprete lo ignora completamente.

```python
# Senza underscore: difficile da leggere
stipendio_annuo = 35000000

# Con underscore: molto più leggibile
stipendio_annuo = 35_000_000

print(stipendio_annuo)  # Stampa: 35000000
```

### I numeri in virgola mobile (float)

Un float è un numero che può avere una parte decimale. Il nome deriva dall'inglese *floating point*, ovvero "virgola mobile", che descrive il modo in cui questi numeri sono rappresentati internamente dal processore.

```python
# Letterali float: presenza del punto decimale li distingue dagli interi
pi_greco = 3.14159
altezza = 1.78
temperatura = -3.5
intero_scritto_come_float = 2.0  # Anche questo è un float, non un int

print(type(pi_greco))  # Stampa: <class 'float'>
print(type(2.0))       # Stampa: <class 'float'>
print(type(2))         # Stampa: <class 'int'>
```

Python conosce anche la **notazione scientifica** per i float, utile quando i valori sono molto grandi o molto piccoli. Si usa la lettera `e` (o `E`) seguita dall'esponente in base 10.

```python
# Notazione scientifica: e significa "per 10 elevato a"
velocita_luce = 3e8        # Equivale a 3 × 10^8 = 300000000.0
massa_elettrone = 9.11e-31  # Equivale a 9.11 × 10^-31

print(velocita_luce)     # Stampa: 300000000.0
print(massa_elettrone)   # Stampa: 9.11e-31

# Python usa la notazione scientifica per stampare numeri molto piccoli o grandi
print(0.000000001)       # Stampa: 1e-09
```

Come vedete nell'ultimo esempio, quando un numero è talmente piccolo (o grande) che la notazione decimale risulterebbe scomoda, Python la converte automaticamente in notazione scientifica per la stampa.

### I booleani (bool)

Il tipo booleano è il più semplice di tutti: può avere solo due valori, `True` o `False`. Questi non sono stringhe di testo, sono valori speciali del linguaggio scritti esattamente con la lettera maiuscola iniziale.

```python
# Letterali booleani
piove = True
sole = False

print(type(piove))   # Stampa: <class 'bool'>
print(piove)         # Stampa: True
```

C'è qualcosa di interessante nel rapporto tra booleani e interi in Python: `True` vale numericamente 1, e `False` vale 0. Questo non è un caso, i booleani sono in realtà una sottoclasse degli interi in Python.

```python
# I booleani sono numericamente 1 e 0
print(True + True)    # Stampa: 2
print(True + False)   # Stampa: 1
print(False + False)  # Stampa: 0
print(int(True))      # Stampa: 1
print(int(False))     # Stampa: 0
```

Questa caratteristica raramente si usa direttamente, ma è utile saperla perché spiega alcuni comportamenti apparentemente misteriosi che potreste incontrare.

### Le stringhe (str)

Una stringa è una sequenza di caratteri racchiusa tra virgolette. Può contenere lettere, numeri, spazi, simboli, praticamente qualsiasi cosa si possa digitare. In Python si possono usare virgolette singole o doppie in modo intercambiabile, a patto di usare lo stesso tipo sia all'apertura che alla chiusura.

```python
# Letterali stringa con virgolette singole o doppie: equivalenti
nome = "Alice"
cognome = 'Rossi'
frase = "Buongiorno, come stai?"

# Utile quando la stringa contiene già uno dei due tipi di virgolette
citazione = "L'interprete Python è scritto in C."
dialogo = 'Disse: "Benvenuto!"'

print(type(nome))    # Stampa: <class 'str'>
```

Per stringhe che si estendono su più righe, Python offre le **triple virgolette** (sia singole `'''` che doppie `"""`). Tutto ciò che si trova all'interno, inclusi i ritorni a capo, fa parte della stringa.

```python
# Stringa su più righe con triple virgolette
paragrafo = """Questo è il primo capoverso.
Questo è il secondo capoverso.
E questo è il terzo."""

print(paragrafo)
# Stampa:
# Questo è il primo capoverso.
# Questo è il secondo capoverso.
# E questo è il terzo.
```

Le stringhe in Python sono **immutabili**: una volta create, non possono essere modificate. Questo concetto tornerà più volte quando studierete i metodi delle stringhe e le confronterete con le liste.

### Le Sequenze di Escape: Messaggi Segreti nell'Alfabeto

Immaginate di dover scrivere un biglietto a un amico che reciti: *Lui disse: "Ciao"*. Se usate le virgolette doppie per racchiudere la stringa in Python, l'interprete si confonderà: vedrà le virgolette prima di *Ciao* e penserà che la frase sia finita lì, lasciando il resto del testo "appeso" nel vuoto, causando un errore.

Come facciamo a dire a Python: "Guarda, queste virgolette non servono a chiudere la stringa, sono solo un pezzo di testo"? Usiamo un segnale speciale: il **backslash** (`\`), chiamato anche **carattere di escape**.

Il backslash agisce come una sorta di "bacchetta magica" che cambia il significato del carattere che lo segue. Insieme, formano una **sequenza di escape**.

Ecco le più importanti per l'esame PCEP:

| Sequenza | Significato | Effetto Pratico |
| :--- | :--- | :--- |
| `\n` | **Newline** | Sposta il testo su una nuova riga (come premere Invio). |
| `\t` | **Tab** | Inserisce uno spazio di tabulazione (un salto orizzontale). |
| `\'` | **Single Quote** | Inserisce un apostrofo in una stringa delimitata da `'`. |
| `\"` | **Double Quote** | Inserisce virgolette in una stringa delimitata da `"`. |
| `\\` | **Backslash** | Inserisce un carattere backslash letterale. |



Vediamole in azione:

```python
# Usare le virgolette dentro le virgolette
citazione = "Lui disse: \"Python è fantastico\""
print(citazione) 
# Output: Lui disse: "Python è fantastico"

# Creare una lista su più righe con un solo print
lista_spesa = "Pane\nLatte\nUova"
print(lista_spesa)
# Output:
# Pane
# Latte
# Uova

# Formattare il testo a colonne con il Tab
print("Nome:\tMario")
print("Età:\t25")
# Output:
# Nome:   Mario
# Età:    25

# Scrivere un percorso di file (attenzione al doppio backslash!)
percorso = "C:\\utenti\\documenti"
print(percorso)
# Output: C:\utenti\documenti
```

Senza il carattere di escape, l'ultimo esempio sarebbe un disastro: Python leggerebbe `\u` e `\d` cercando di interpretarli come comandi speciali, fallendo miseramente. Usando `\\`, diciamo invece: "Voglio proprio un backslash normale".

---

## I Sistemi Numerici: Binario, Ottale, Esadecimale

Finora abbiamo usato i numeri nel modo in cui li usiamo nella vita di tutti i giorni: in base 10, cioè con le cifre da 0 a 9. Ma i computer, internamente, usano la base 2 (il sistema binario), e i programmatori spesso usano anche la base 8 (ottale) e la base 16 (esadecimale) per rappresentare dati in modo più compatto e leggibile.

Python permette di scrivere letterali interi in tutte e quattro queste basi direttamente nel codice, usando dei prefissi specifici.

### Il sistema binario (base 2)

Nel sistema binario si usano solo due cifre: 0 e 1. Ogni posizione ha valore doppio rispetto a quella alla sua destra (1, 2, 4, 8, 16...). Il numero binario `1011` vale quindi `1×8 + 0×4 + 1×2 + 1×1 = 11` in decimale.

Per scrivere un letterale binario in Python si usa il prefisso `0b` (zero seguito dalla lettera b, da *binary*).

```python
# Letterali binari: prefisso 0b
valore_binario = 0b1011   # Equivale a 11 in decimale
altro_binario = 0b11111111  # Equivale a 255 in decimale

print(valore_binario)    # Stampa: 11
print(altro_binario)     # Stampa: 255

# Python stampa sempre il valore in decimale, salvo richiesta esplicita
print(type(valore_binario))  # Stampa: <class 'int'> (è sempre un intero!)
```

Notate che Python memorizza sempre il valore come intero decimale, indipendentemente dalla base con cui lo avete scritto nel codice. Il prefisso è solo una convenienza per voi.

### Il sistema ottale (base 8)

Nel sistema ottale si usano le cifre da 0 a 7. Ogni posizione vale otto volte quella alla sua destra (1, 8, 64, 512...). Il numero ottale `17` vale quindi `1×8 + 7×1 = 15` in decimale.

Il prefisso Python per i letterali ottali è `0o` (zero seguito dalla lettera o, da *octal*).

```python
# Letterali ottali: prefisso 0o
valore_ottale = 0o17   # Equivale a 15 in decimale
altro_ottale = 0o777   # Equivale a 511 in decimale

print(valore_ottale)   # Stampa: 15
print(altro_ottale)    # Stampa: 511
```

Il sistema ottale era molto usato nei vecchi sistemi Unix per rappresentare i permessi dei file (dove ogni cifra ottale rappresenta tre bit di permesso), e potreste incontrarlo in contesti di programmazione di sistema.

### Il sistema esadecimale (base 16)

Il sistema esadecimale usa sedici simboli: le cifre da 0 a 9 più le lettere da A a F (o a-f, Python le accetta entrambe). Ogni posizione vale sedici volte quella alla sua destra. La lettera A vale 10, B vale 11, C vale 12, D vale 13, E vale 14, F vale 15.

Il prefisso Python per i letterali esadecimali è `0x` (zero seguito dalla lettera x, da *hexadecimal*).

```python
# Letterali esadecimali: prefisso 0x
valore_esadecimale = 0xFF    # Equivale a 255 in decimale (15×16 + 15)
colore_rosso = 0xFF0000      # Colore rosso in formato RGB esadecimale
codice = 0x1A2B              # Equivale a 6699 in decimale

print(valore_esadecimale)    # Stampa: 255
print(colore_rosso)          # Stampa: 16711680
print(codice)                # Stampa: 6699

# Le lettere possono essere maiuscole o minuscole: equivalenti
print(0xFF == 0xff)          # Stampa: True
```

L'esadecimale è il sistema più usato dai programmatori dopo il decimale, perché ogni cifra esadecimale corrisponde esattamente a quattro bit, rendendo la conversione da e verso il binario immediata. I codici colore del web (come `#FF5733`), gli indirizzi di memoria, i valori hash crittografici: tutto questo è tipicamente scritto in esadecimale.

### Convertire tra basi con le funzioni built-in

Python offre funzioni per convertire un intero nella sua rappresentazione stringa in una base diversa, e per fare il percorso inverso.

```python
# Da intero a stringa in una certa base
print(bin(255))   # Stampa: 0b11111111
print(oct(255))   # Stampa: 0o377
print(hex(255))   # Stampa: 0xff

# Da stringa in una certa base a intero
print(int("1011", 2))   # Stampa: 11  (interpreta "1011" come binario)
print(int("17", 8))     # Stampa: 15  (interpreta "17" come ottale)
print(int("FF", 16))    # Stampa: 255 (interpreta "FF" come esadecimale)
```

La funzione `int()` con due argomenti è particolarmente utile quando leggete dati da file o dall'input utente e volete convertirli in interi.

---

## Variabili: Dare un Nome ai Valori

Tornate per un momento all'analogia del cartella medica. Sulla vostra cartella non scrivete soltanto "24", ma "Età: 24". Il nome "età" identifica il contenitore; il valore "24" è ciò che ci mettete dentro. In Python, una variabile funziona esattamente così: è un nome che fate puntare a un valore nella memoria del computer.

L'operazione con cui create questo collegamento si chiama **assegnamento** e si usa il simbolo `=`.

```python
# Assegnamento: il nome a sinistra, il valore a destra
eta = 24
nome = "Marco"
temperatura = 18.5
cielo_sereno = True

# Ora potete usare i nomi al posto dei valori
print(nome)           # Stampa: Marco
print(eta + 5)        # Stampa: 30
```

Una proprietà fondamentale di Python è che le variabili non hanno un tipo fisso: potete riassegnare una variabile con un valore di tipo completamente diverso senza errori. La variabile punta semplicemente al nuovo oggetto.

```python
# Una variabile può cambiare tipo durante l'esecuzione
x = 10
print(x, type(x))    # Stampa: 10 <class 'int'>

x = "adesso sono una stringa"
print(x, type(x))    # Stampa: adesso sono una stringa <class 'str'>

x = 3.14
print(x, type(x))    # Stampa: 3.14 <class 'float'>
```

Python permette anche l'**assegnamento multiplo**, cioè assegnare lo stesso valore a più variabili in una sola riga, oppure assegnare valori diversi a variabili diverse simultaneamente.

```python
# Assegnamento multiplo allo stesso valore
a = b = c = 0
print(a, b, c)   # Stampa: 0 0 0

# Assegnamento parallelo (unpacking)
x, y, z = 1, 2, 3
print(x, y, z)   # Stampa: 1 2 3

# Trucco classico per scambiare due variabili senza una terza temporanea
primo = "rosso"
secondo = "blu"
primo, secondo = secondo, primo
print(primo, secondo)  # Stampa: blu rosso
```

---

## Convenzioni di Naming e PEP 8

Python impone alcune **regole** sui nomi delle variabili e raccomanda alcune **convenzioni**. La differenza è importante: le regole sono obbligatorie (violarle causa un errore), le convenzioni sono facoltative ma seguite quasi universalmente dalla comunità Python.

### Le regole obbligatorie

Un nome di variabile in Python deve rispettare tre vincoli: può contenere solo lettere (minuscole e maiuscole), cifre e il carattere underscore `_`; non può iniziare con una cifra; non può coincidere con una parola chiave riservata del linguaggio (come `if`, `for`, `while`, `class` e così via).

```python
# Nomi validi
eta = 25
nome_utente = "Alice"
_valore_interno = 42
misura2 = 100.0
CodicePostale = "00100"  # Valido, ma non convenzionale

# Nomi non validi (causano SyntaxError o altri errori)
# 2variabile = 10       # Errore: inizia con una cifra
# nome-utente = "Alice" # Errore: il trattino non è ammesso
# for = 5               # Errore: "for" è una keyword
```

Python distingue le maiuscole dalle minuscole: `eta`, `Eta`, `ETA` e `ETA_` sono quattro variabili completamente diverse.

### PEP 8: la guida di stile della comunità Python

PEP sta per *Python Enhancement Proposal*, cioè proposta di miglioramento per Python. Il documento PEP 8 è la guida di stile ufficiale per il codice Python, e definisce le convenzioni che praticamente tutti i programmatori Python seguono per scrivere codice leggibile e coerente.

Riguardo ai nomi, PEP 8 stabilisce le seguenti convenzioni principali.

Per le **variabili ordinarie e i parametri delle funzioni**, si usa lo `snake_case`: tutte le lettere minuscole, con le parole separate da underscore.

```python
# Stile PEP 8 per variabili: snake_case
codice_postale = "00100"
numero_studenti = 30
indirizzo_email = "mario@esempio.it"
velocita_media_kmh = 90.5
```

Per le **costanti** (valori che per convenzione non devono cambiare durante l'esecuzione), si usa l'`UPPER_CASE`: tutte le lettere maiuscole, con le parole separate da underscore. Python non ha un tipo "costante" reale come altri linguaggi, ma questa convenzione visiva comunica chiaramente l'intenzione al lettore.

```python
# Stile PEP 8 per costanti: UPPER_CASE
PI_GRECO = 3.14159265358979
VELOCITA_LUCE_MS = 299_792_458
NUMERO_MASSIMO_TENTATIVI = 3
```

Per i **nomi delle classi** (che incontrerete nelle sezioni avanzate), si usa il `PascalCase` o `CamelCase`: ogni parola inizia con la maiuscola, senza separatori.

```python
# Stile PEP 8 per classi: PascalCase
# (anticipazione: le classi si studieranno in seguito)
class ContoCorrente:
    pass

class AnalizzatoreDatiSpettrali:
    pass
```

PEP 8 raccomanda anche nomi **descrittivi e significativi**: meglio `numero_studenti_iscritti` di `n`, meglio `temperatura_celsius` di `tc`. Un nome che spiega cosa contiene la variabile rende il codice molto più facile da leggere e da mantenere, sia per altri che per voi stessi a distanza di qualche settimana.

```python
# Nomi poco descrittivi: scomodi da capire
x = 15
y = x * 60

# Nomi descrittivi: immediatamente comprensibili
ore_lavorate = 15
minuti_totali = ore_lavorate * 60
```

Una nota sull'underscore iniziale: per convenzione, un nome che inizia con `_` (come `_valore_interno`) segnala che quella variabile è destinata a uso interno, non pensata per essere usata direttamente da chi usa il vostro codice. Non è una regola tecnica, ma è un segnale che i programmatori esperti rispettano.

---

## Conclusione: I Mattoni Sono Pronti

Avete ora familiarità con i tipi di dati fondamentali di Python (interi, float, booleani e stringhe), con i modi in cui si possono scrivere letterali numerici in diverse basi, e con le regole e convenzioni che governano il naming delle variabili.

Questi elementi sono i mattoni con cui si costruisce qualsiasi programma. Ogni volta che scriverete un'istruzione complessa, uno script lungo, un modulo riutilizzabile, sarà sempre composto in fondo da questi stessi tipi base, organizzati in variabili con nomi scelti bene.

Il passo successivo logico, che affronterete nella sezione 1.4, è capire come operare su questi valori: sommarli, confrontarli, combinarli logicamente. Gli operatori di Python sono il modo in cui si dà "movimento" ai dati, e per comprenderli a fondo era essenziale avere prima chiari i tipi su cui operano. Vedremo anche come il type casting permette di convertire esplicitamente un tipo in un altro, cosa fondamentale quando ad esempio si riceve input dall'utente (sempre una stringa) e si ha bisogno di un numero.

Prima di arrivare agli operatori, la sezione 1.5 vi mostrerà come leggere dati dall'utente e stampare risultati sullo schermo: le funzioni `input()` e `print()`. Con quelle, i vostri programmi diventeranno finalmente interattivi.
