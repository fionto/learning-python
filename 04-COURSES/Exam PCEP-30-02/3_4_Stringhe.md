# Capitolo 3: Sezione 3.4 — Stringhe: Slicing, Immutabilità, Caratteri Escape e Metodi di Base

## Introduzione: Lettere in Fila, con Regole Precise

Immaginate un binario ferroviario. Ogni vagone è numerato a partire da zero, e i vagoni sono agganciati uno all'altro in un ordine preciso. Potete salire sul terzo vagone, oppure prendere un intero tratto del treno dal quinto all'ottavo. Ma non potete spostare un vagone nel mezzo del convoglio senza ristrutturare tutto il treno: l'ordine è fisso, fa parte della natura di quella struttura.

Le stringhe in Python funzionano esattamente così. Una stringa è una sequenza ordinata di caratteri, dove ogni carattere occupa una posizione ben precisa, numerata a partire da zero. Avete già incontrato le stringhe fin dai primissimi capitoli: ogni volta che avete scritto `"ciao"` o usato `input()` per leggere qualcosa dall'utente, stavate lavorando con stringhe. In questa sezione le esaminiamo in profondità, scoprendo come accedere ai loro elementi, come estrarne porzioni, quali regole impongono la loro natura immutabile, e quale ricco repertorio di metodi Python mette a disposizione per trasformarle e interrogarle.

Le stringhe appartengono alla stessa famiglia concettuale delle liste e delle tuple che abbiamo incontrato nelle sezioni precedenti: sono sequenze. Molte delle operazioni che avete imparato sulle liste si applicano anche alle stringhe, con una differenza fondamentale che capiremo presto. Questo rende la sezione 3.4 un momento di consolidamento e di scoperta insieme.

## Costruire una Stringa

Una stringa si crea racchiudendo del testo tra apici singoli, apici doppi, o apici tripli. Python non distingue tra apici singoli e doppi dal punto di vista del contenuto: `'ciao'` e `"ciao"` sono identici. La scelta tra i due serve spesso a comodità di lettura, per esempio quando il testo stesso contiene un apostrofo.

```python
# Tre modi equivalenti di creare la stessa stringa
saluto1 = 'buongiorno'
saluto2 = "buongiorno"
print(saluto1 == saluto2)  # Stampa: True

# Stringa con apostrofo: si usa il delimitatore doppio
frase = "l'aquila vola alta"
print(frase)  # Stampa: l'aquila vola alta

# Stringa con virgolette interne: si usa il delimitatore singolo
titolo = 'Il romanzo si chiama "Promessi Sposi"'
print(titolo)  # Stampa: Il romanzo si chiama "Promessi Sposi"
```

Quando il testo deve occupare più righe, Python offre i delimitatori tripli, sia con apici singoli che doppi. Tutto ciò che si trova tra `"""` e `"""` (o tra `'''` e `'''`) fa parte della stringa, inclusi i caratteri di a-capo.

```python
# Stringa multi-linea con apici tripli doppi
poesia = """La luna è una lampadina
che non si può spegnere
ma si oscura da sola."""

print(poesia)
# Stampa:
# La luna è una lampadina
# che non si può spegnere
# ma si oscura da sola.
```

Infine, è possibile costruire una stringa per concatenazione usando l'operatore `+`, o per ripetizione usando l'operatore `*`, esattamente come avete visto per le liste.

```python
parte1 = "euro"
parte2 = "pa"
continente = parte1 + parte2
print(continente)   # Stampa: europa

linea = "-" * 20
print(linea)        # Stampa: --------------------
```

## Indicizzazione: Accedere ai Singoli Caratteri

Ogni carattere di una stringa ha un indice, a partire da zero per il primo carattere. Questo vale anche per gli indici negativi: `-1` indica l'ultimo carattere, `-2` il penultimo, e così via. È lo stesso sistema che avete usato con le liste.

```python
parola = "Python"
#          P  y  t  h  o  n
# indici:  0  1  2  3  4  5
# neg:    -6 -5 -4 -3 -2 -1

print(parola[0])    # Stampa: P
print(parola[3])    # Stampa: h
print(parola[-1])   # Stampa: n
print(parola[-2])   # Stampa: o
```

Se si tenta di accedere a un indice che non esiste, Python solleva un `IndexError`: è lo stesso errore che avete già visto con le liste. La funzione `len()` restituisce la lunghezza della stringa, utile per calcolare gli indici in modo dinamico.

```python
testo = "Bologna"
lunghezza = len(testo)
print(lunghezza)              # Stampa: 7
print(testo[lunghezza - 1])   # Stampa: a (ultimo carattere)
```

## Slicing: Ritagliare Porzioni di Stringa

Lo slicing permette di estrarre una sottostringa specificando un intervallo di indici. La sintassi è la stessa delle liste: `stringa[inizio:fine]`, dove `inizio` è incluso e `fine` è escluso. Si può anche specificare un passo: `stringa[inizio:fine:passo]`.

```python
frase = "informatica"
#          i  n  f  o  r  m  a  t  i  c  a
# indici:  0  1  2  3  4  5  6  7  8  9 10

print(frase[0:5])    # Stampa: infor
print(frase[5:])     # Stampa: matica  (fino alla fine)
print(frase[:4])     # Stampa: info    (dall'inizio)
print(frase[-5:])    # Stampa: atica   (ultimi 5 caratteri)
print(frase[::2])    # Stampa: ifrai   (ogni due caratteri)
print(frase[::-1])   # Stampa: acitamrofni  (stringa rovesciata)
```

Il trucco `[::-1]` per rovesciare una stringa è particolarmente elegante e vale la pena di memorizzarlo: è idiomatico in Python e funziona su qualsiasi sequenza.

Quando gli indici di slicing escono dal range della stringa, Python non solleva alcun errore: semplicemente restituisce quello che c'è disponibile. Questo comportamento è diverso dall'indicizzazione singola, che invece produce `IndexError`.

```python
parola = "mare"
print(parola[0:100])   # Stampa: mare  (nessun errore, anche se 100 > len)
print(parola[10:20])   # Stampa:       (stringa vuota, senza errori)
```

## Immutabilità: Cosa Non Si Può Fare con una Stringa

Torniamo all'analogia del treno. Potete fotografare il terzo vagone, potete descrivere il tratto dal quinto all'ottavo, ma non potete aprire un vagone e cambiarne il contenuto senza costruire un treno nuovo. Le stringhe in Python sono **immutabili**: una volta create, i loro caratteri non possono essere modificati.

Questo è il contrasto fondamentale con le liste. Se avete una lista, potete scrivere `lista[2] = "x"` e la lista cambia. Con una stringa, lo stesso tentativo provoca un `TypeError`.

```python
parola = "gatto"

# Tentativo di modifica: ERRORE
# parola[0] = "G"
# TypeError: 'str' object does not support item assignment

# Il modo corretto: creare una stringa nuova
parola_modificata = "G" + parola[1:]
print(parola_modificata)   # Stampa: Gatto
```

L'immutabilità non significa che non possiate "cambiare" il valore di una variabile stringa: potete sempre riassegnare la variabile a una stringa nuova. Quello che non potete fare è modificare i caratteri della stringa esistente dall'interno. Dal punto di vista pratico, questo significa che tutte le operazioni sulle stringhe (concatenazione, sostituzione, conversione maiuscolo/minuscolo) producono **nuove stringhe**, e non modificano quella originale.

```python
testo = "hello"
testo_maiuscolo = testo.upper()   # Crea una nuova stringa

print(testo)             # Stampa: hello  (invariata)
print(testo_maiuscolo)   # Stampa: HELLO  (nuova stringa)
```

## Caratteri Escape: Inserire Simboli Speciali

A volte il testo che volete rappresentare contiene caratteri che Python interpreterebbe in modo speciale: le virgolette di delimitazione, il carattere di a-capo, la tabulazione, la barra rovesciata stessa. Per inserire questi caratteri in una stringa si usa la **barra rovesciata** (`\`) come carattere di escape: essa segnala a Python che il carattere seguente va trattato in modo speciale, non letteralmente.

I caratteri escape più comuni sono i seguenti:

| Sequenza | Significato               |
|----------|---------------------------|
| `\n`     | A-capo (newline)          |
| `\t`     | Tabulazione orizzontale   |
| `\\`     | Barra rovesciata letterale |
| `\'`     | Apice singolo letterale   |
| `\"`     | Apice doppio letterale    |
| `\r`     | Ritorno a inizio riga     |

```python
# \n: a-capo all'interno di una stringa su una sola riga di codice
indirizzo = "Via Roma 12\nFirenze\nItalia"
print(indirizzo)
# Stampa:
# Via Roma 12
# Firenze
# Italia

# \t: tabulazione per allineare colonne
intestazione = "Nome\tCognome\tEtà"
print(intestazione)
# Stampa: Nome    Cognome    Età

# \': apostrofo in una stringa delimitata da apici singoli
messaggio = 'L\'aquila è alta'
print(messaggio)   # Stampa: L'aquila è alta

# \\: barra rovesciata letterale (necessaria per percorsi Windows)
percorso = "C:\\Users\\matteo\\Documenti"
print(percorso)   # Stampa: C:\Users\matteo\Documenti
```

Un'alternativa comoda alla doppia barra rovesciata per i percorsi di file è la **raw string**, preceduta dal prefisso `r`. In una raw string, la barra rovesciata viene trattata come carattere letterale e non come escape.

```python
# Raw string: nessun carattere escape interpretato
percorso_raw = r"C:\Users\matteo\Documenti"
print(percorso_raw)   # Stampa: C:\Users\matteo\Documenti
```

Vale la pena notare che anche all'interno delle stringhe triple è possibile usare `\n` e `\t`, ma spesso non è necessario perché le stringhe triple preservano gli a-capo già presenti nel codice sorgente.

## L'Operatore `in` e la Funzione `len()`

Prima di passare ai metodi, due strumenti generali si applicano alle stringhe tanto quanto alle liste. L'operatore `in` verifica se una sottostringa è contenuta nella stringa principale: restituisce `True` o `False`.

```python
frase = "la programmazione è creativa"

print("program" in frase)     # Stampa: True
print("musica" in frase)      # Stampa: False
print("not" in frase)         # Stampa: False
print("è" in frase)           # Stampa: True

# Utile nei cicli: iterare carattere per carattere
for carattere in "abc":
    print(carattere)
# Stampa:
# a
# b
# c
```

La funzione `len()`, già usata sopra, restituisce il numero di caratteri della stringa, spazi e punteggiatura inclusi.

```python
print(len("ciao"))       # Stampa: 4
print(len("ciao mondo")) # Stampa: 10 (spazio incluso)
print(len(""))           # Stampa: 0 (stringa vuota)
```

## Metodi di Base delle Stringhe

Le stringhe in Python sono oggetti, e come tali dispongono di un ricco set di **metodi** richiamabili tramite la notazione a punto: `stringa.metodo()`. Tutti i metodi restituiscono nuove stringhe (o altri valori), lasciando l'originale invariata, in accordo con l'immutabilità che abbiamo discusso.

### Conversione di Caso

I metodi `upper()` e `lower()` convertono rispettivamente l'intera stringa in maiuscolo o in minuscolo. Il metodo `capitalize()` porta in maiuscolo solo il primo carattere, lasciando il resto in minuscolo. Il metodo `title()` porta in maiuscolo la prima lettera di ciascuna parola.

```python
testo = "la SCIENZA è meravigliosa"

print(testo.upper())       # Stampa: LA SCIENZA È MERAVIGLIOSA
print(testo.lower())       # Stampa: la scienza è meravigliosa
print(testo.capitalize())  # Stampa: La scienza è meravigliosa
print(testo.title())       # Stampa: La Scienza È Meravigliosa
```

### Ricerca all'Interno di una Stringa

Il metodo `find()` cerca una sottostringa e restituisce l'indice della prima occorrenza; se non la trova, restituisce `-1`. Il metodo `index()` si comporta in modo simile, ma solleva un `ValueError` se la sottostringa non è presente: utile quando siete certi che l'elemento ci sia e volete un errore esplicito in caso contrario.

```python
frase = "il gatto e il cane"

print(frase.find("gatto"))    # Stampa: 3
print(frase.find("pesce"))    # Stampa: -1 (non trovato)
print(frase.index("cane"))    # Stampa: 14

# find() con posizione di inizio
print(frase.find("il", 5))    # Stampa: 11 (cerca da posizione 5 in poi)
```

Il metodo `count()` conta quante volte una sottostringa appare nella stringa principale.

```python
testo = "banana"
print(testo.count("a"))    # Stampa: 3
print(testo.count("an"))   # Stampa: 2
```

### Verifica delle Estremità

I metodi `startswith()` e `endswith()` verificano se una stringa inizia o termina con una certa sottostringa, restituendo un booleano. Sono particolarmente utili per filtrare nomi di file, URL, o prefissi di testo.

```python
nome_file = "relazione_finale.pdf"

print(nome_file.startswith("relazione"))   # Stampa: True
print(nome_file.endswith(".pdf"))          # Stampa: True
print(nome_file.endswith(".docx"))         # Stampa: False
```

### Rimozione degli Spazi

Il metodo `strip()` rimuove gli spazi bianchi (e i caratteri di a-capo) all'inizio e alla fine della stringa. `lstrip()` agisce solo sul lato sinistro, `rstrip()` solo sul lato destro. Sono indispensabili quando si legge input dall'utente o da un file, dove spazi indesiderati si insinuano facilmente.

```python
voce = "   Milano   "

print(repr(voce.strip()))    # Stampa: 'Milano'
print(repr(voce.lstrip()))   # Stampa: 'Milano   '
print(repr(voce.rstrip()))   # Stampa: '   Milano'
```

Nell'esempio sopra è stato usato `repr()` per rendere visibili gli spazi nella stampa: non è necessario nel codice normale, ma aiuta a capire cosa sta succedendo durante il debug.

### Sostituzione

Il metodo `replace()` crea una nuova stringa in cui tutte le occorrenze di una sottostringa vengono sostituite da un'altra. Si può passare un terzo argomento per limitare il numero di sostituzioni.

```python
testo = "il sole sorge e il sole tramonta"

print(testo.replace("sole", "vento"))        # Stampa: il vento sorge e il vento tramonta
print(testo.replace("sole", "luna", 1))      # Stampa: il luna sorge e il sole tramonta
```

### Divisione e Unione

Il metodo `split()` divide la stringa in una lista di sottostringhe, usando come separatore un carattere o una sequenza di caratteri (per default, lo spazio bianco). Il metodo `join()` fa l'operazione inversa: prende una lista di stringhe e le unisce in un'unica stringa usando il testo su cui è chiamato come separatore.

```python
# split: da stringa a lista
frase = "Firenze Roma Napoli Milano"
citta = frase.split()          # Separatore default: spazio
print(citta)                   # Stampa: ['Firenze', 'Roma', 'Napoli', 'Milano']

dati = "10;25;37;42"
numeri = dati.split(";")       # Separatore esplicito
print(numeri)                  # Stampa: ['10', '25', '37', '42']

# join: da lista a stringa
parole = ["la", "vita", "è", "breve"]
frase_unita = " ".join(parole)
print(frase_unita)             # Stampa: la vita è breve

codice = "-".join(["IT", "001", "2024"])
print(codice)                  # Stampa: IT-001-2024
```

La coppia `split()`/`join()` è uno dei pattern più frequenti nella manipolazione di testi in Python: merita di essere padroneggiata fin da subito.

### Verifica del Contenuto

Esistono metodi che testano la composizione di una stringa, tutti restituendo `True` o `False`. I più utili sono `isdigit()`, che restituisce `True` se tutti i caratteri sono cifre decimali; `isalpha()`, vero se tutti sono lettere alfabetiche; `isalnum()`, vero se sono lettere o cifre; e `isspace()`, vero se la stringa è composta solo da spazi bianchi.

```python
print("12345".isdigit())     # Stampa: True
print("12.3".isdigit())      # Stampa: False (il punto non è una cifra)
print("Python".isalpha())    # Stampa: True
print("Py3".isalpha())       # Stampa: False
print("Py3".isalnum())       # Stampa: True
print("   ".isspace())       # Stampa: True
```

Questi metodi sono molto utili per validare l'input dell'utente prima di convertirlo in numero o di usarlo in un calcolo.

## Mettere Tutto Insieme: Un Esempio Integrato

L'esempio seguente combina diversi dei concetti introdotti in questa sezione: lettura di un testo, pulizia degli spazi, analisi del contenuto e trasformazione.

```python
# Simulazione di un dato letto da file (con spazi extra e maiuscole miste)
voce_grezza = "   Matteo Rossi   "

# Pulizia e normalizzazione
nome_pulito = voce_grezza.strip()
nome_formattato = nome_pulito.title()

# Estrazione di nome e cognome
parti = nome_formattato.split()
nome = parti[0]
cognome = parti[1]

# Verifica
print(f"Nome: {nome}")          # Stampa: Nome: Matteo
print(f"Cognome: {cognome}")    # Stampa: Cognome: Rossi

# Creazione di un identificatore
id_utente = (nome[0] + cognome).lower()
print(f"ID: {id_utente}")       # Stampa: ID: mrossi

# Slicing: iniziali
iniziali = nome[0] + "." + cognome[0] + "."
print(f"Iniziali: {iniziali}")  # Stampa: Iniziali: M.R.
```

Si noti come ogni passo produca una stringa nuova, lasciando la precedente invariata: questo è l'immutabilità in azione nel codice reale.

## Conclusione: Una Struttura Dati Versatile e Precisa

Le stringhe occupano un posto centrale in qualsiasi programma che interagisca con il mondo esterno: file di testo, input dell'utente, messaggi di log, nomi di variabili in protocolli di comunicazione. Avere una padronanza solida del loro funzionamento significa poter trattare informazione testuale con la stessa sicurezza con cui si maneggiamo i numeri.

In questa sezione avete visto che le stringhe si costruiscono in modi diversi, con delimitatori singoli, doppi o tripli, e che i caratteri escape permettono di rappresentare simboli che altrimenti sarebbero ambigui o impossibili da inserire. Avete scoperto che l'indicizzazione e lo slicing funzionano esattamente come sulle liste, ma con il vincolo dell'immutabilità: nessuna modifica in-place è possibile, solo la creazione di nuove stringhe. Infine, avete esplorato un arsenale di metodi che coprono le operazioni più frequenti: ricerca, sostituzione, divisione, unione, pulizia e verifica del contenuto.

Con le stringhe, le liste, le tuple e i dizionari visti nelle sezioni 3.1 — 3.4, disponete ora di tutta la cassetta degli attrezzi per rappresentare e manipolare dati strutturati. Il passo successivo, nella Sezione 4, sarà organizzare il codice che lavora su questi dati in funzioni riutilizzabili: un salto di astrazione che renderà i vostri programmi più leggibili, testabili e mantenibili.
