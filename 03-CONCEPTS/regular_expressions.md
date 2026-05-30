# Espressioni Regolari in Python

## Il problema del testo non strutturato

Chi lavora con dati provenienti dal mondo reale si trova spesso a dover estrarre
informazioni da stringhe che seguono una struttura implicita ma non rigida: nomi di file
generati automaticamente da strumenti di misura, log di sistema, output di sensori,
indirizzi e-mail in un file di testo, date in formati diversi a seconda della locale di
chi ha compilato il modulo. In tutti questi casi, il confronto esatto tra stringhe non
basta: non si cerca una stringa specifica, si cerca qualcosa che *assomiglia* a un certo
schema.

Le espressioni regolari (in inglese *regular expressions*, abbreviate *regex* o *regexp*)
sono un linguaggio formale per descrivere pattern di testo. Python le espone attraverso
il modulo `re` della libreria standard. L'idea di fondo è separare la *descrizione dello
schema* (scritta nel linguaggio delle regex) dall'*applicazione* di quello schema (delegata
alle funzioni del modulo): si definisce una volta il pattern, poi lo si usa per cercare,
estrarre, validare o sostituire.

Per capire perché è utile, considerate questo compito: dato un nome di file come
`20240315_093000_GaSb_P1.2E-3_T450.txt`, estrarre data, ora, nome del campione, pressione
e temperatura. Con le operazioni su stringhe standard si potrebbe fare, ma il codice
diventa una sequenza fragile di `split`, `find` e slice che si rompe non appena il formato
varia di un millimetro. Con le regex, si descrive il pattern una volta e l'interprete si
occupa di tutto il resto.

---

## Il modulo `re` e le sue funzioni principali

Il modulo si importa con `import re`. Le funzioni più usate accettano tutte almeno due
argomenti: il pattern (la descrizione dello schema) e la stringa su cui cercarlo.

`re.search(pattern, string)` cerca il pattern *ovunque* nella stringa e restituisce un
oggetto *match* al primo incontro, oppure `None` se non trova nulla. È la funzione da
usare quando ci si chiede "questo schema è presente da qualche parte nel testo?".

`re.match(pattern, string)` è simile, ma vincola la ricerca all'inizio della stringa:
corrisponde solo se il pattern si trova a partire dal primo carattere. È utile per
validare stringhe che devono iniziare in un certo modo.

`re.fullmatch(pattern, string)` è ancora più restrittivo: la stringa intera deve
corrispondere al pattern, senza residui prima o dopo. Ideale per validare un input
che deve avere esattamente una certa struttura.

`re.findall(pattern, string)` restituisce una lista con tutte le corrispondenze trovate.
Se il pattern contiene gruppi di cattura, ogni elemento della lista è una tupla con i
valori catturati.

`re.sub(pattern, repl, string)` sostituisce ogni corrispondenza con la stringa `repl` e
restituisce la stringa modificata.

```python
import re

testo = "Temperatura: 450 K, pressione: 1.2e-3 mbar"

# Cerca il pattern ovunque nel testo
risultato = re.search(r'\d+', testo)
print(risultato.group())  # Stampa: 450

# Trova tutti i numeri (interi)
tutti = re.findall(r'\d+', testo)
print(tutti)  # Stampa: ['450', '3']
```

Notate che `re.findall` ha trovato `'3'` (parte di `1.2e-3`) ma non il numero float
completo: il pattern `\d+` descrive solo sequenze di cifre intere. Torneremo su come
descrivere numeri in virgola mobile.

---

## Costruire i pattern: metacaratteri e classi

Un pattern regex è una stringa in cui certi caratteri hanno significato speciale. I
caratteri letterali (lettere, cifre, segni di punteggiatura normali) corrispondono a se
stessi. I **metacaratteri** invece rappresentano concetti astratti.

Il punto `.` corrisponde a qualsiasi carattere eccetto il newline. L'asterisco `*` significa
"zero o più ripetizioni dell'elemento precedente". Il più `+` significa "una o più
ripetizioni". Il punto interrogativo `?` significa "zero o una ripetizione" (rende
l'elemento opzionale).

Le **classi di caratteri**, delimitate da parentesi quadre `[]`, permettono di elencare un
insieme di caratteri alternativi. `[aeiou]` corrisponde a qualsiasi vocale minuscola.
`[a-z]` corrisponde a qualsiasi lettera minuscola (per inclusione di un intervallo).
`[^abc]` corrisponde a qualsiasi carattere che *non* sia `a`, `b` o `c` (il `^` dentro
una classe nega l'insieme).

Esistono anche classi predefinite, chiamate **shorthand**:

| Shorthand | Equivalente | Significato |
|-----------|-------------|-------------|
| `\d`      | `[0-9]`     | Cifra decimale |
| `\D`      | `[^0-9]`    | Non cifra |
| `\w`      | `[a-zA-Z0-9_]` | Carattere "di parola" |
| `\W`      | `[^a-zA-Z0-9_]` | Non carattere di parola |
| `\s`      | spazio, tab, newline | Spazio bianco |
| `\S`      | opposto di `\s` | Non spazio bianco |

I **quantificatori** generalizzano `*`, `+` e `?`:

- `{n}` corrisponde esattamente *n* ripetizioni
- `{n,}` corrisponde ad *almeno* n ripetizioni
- `{n,m}` corrisponde a *tra* n e m ripetizioni (estremi inclusi)

```python
import re

data = "20240315"

# \d{4} = esattamente 4 cifre, \d{2} = esattamente 2 cifre
match = re.match(r'\d{4}\d{2}\d{2}', data)
print(match.group())  # Stampa: 20240315

# Lo stesso in modo più leggibile con un pattern separato
pattern_data = r'\d{4}\d{2}\d{2}'  # YYYYMMDD
match2 = re.match(pattern_data, '20240315_altra_roba')
print(match2.group())  # Stampa: 20240315 (match al solo prefisso)
```

---

## Gruppi di cattura

I **gruppi** sono la funzionalità che rende le regex utili non solo per cercare ma per
*estrarre*. Racchiudendo una parte del pattern tra parentesi tonde `()` si crea un gruppo
di cattura: quando il pattern trova una corrispondenza, il motore ricorda cosa ha
abbinato a quella parte del pattern, e si può recuperarlo separatamente.

L'oggetto restituito da `re.search`, `re.match` e `re.fullmatch` è un **match object**.
I metodi principali sono:

- `.group()` o `.group(0)`: l'intera stringa corrispondente al pattern
- `.group(n)`: il contenuto del gruppo numero *n* (contati da sinistra, partendo da 1)
- `.groups()`: tutti i gruppi come tupla

```python
import re

stringa = "20240315_093000"

# Due gruppi: data e ora
match = re.match(r'(\d{8})_(\d{6})', stringa)

if match:
    print(match.group(0))   # Stampa: 20240315_093000
    print(match.group(1))   # Stampa: 20240315
    print(match.group(2))   # Stampa: 093000
    print(match.groups())   # Stampa: ('20240315', '093000')
```

I gruppi possono essere **nominati** con la sintassi `(?P<nome>pattern)`. Questo rende il
codice molto più leggibile, perché si accede ai valori catturati per nome invece che per
posizione numerica, e il pattern diventa quasi auto-documentante.

```python
import re

stringa = "20240315_093000"

# Gruppi nominati
pattern = r'(?P<data>\d{8})_(?P<ora>\d{6})'
match = re.match(pattern, stringa)

if match:
    print(match.group('data'))   # Stampa: 20240315
    print(match.group('ora'))    # Stampa: 093000
    # Oppure come dizionario:
    print(match.groupdict())     # Stampa: {'data': '20240315', 'ora': '093000'}
```

Esiste anche il **gruppo non catturante** `(?:pattern)`: raggruppa una parte del pattern
(per applicarvi un quantificatore, ad esempio) senza salvarne il contenuto. È utile per
tenere il numero dei gruppi catturati basso e preciso.

---

## Ancore e delimitatori

Le **ancore** non corrispondono a caratteri ma a *posizioni* nella stringa.

`^` corrisponde all'inizio della stringa. `$` corrisponde alla fine. Usati insieme,
`^pattern$` impone che l'intera stringa corrisponda al pattern, e non solo una sua
sottostringa (questo è equivalente a `re.fullmatch`).

`\b` corrisponde a un confine di parola: la posizione tra un carattere `\w` e un
carattere `\W` (o il bordo della stringa). `\btest\b` trova "test" come parola isolata
ma non come parte di "testing" o "protest".

```python
import re

# Senza ancoraggio, trova anche sottostringhe
print(re.search(r'\d{4}', 'anno 2024 circa'))   # trova '2024'
print(re.search(r'\d{4}', 'codice AB2024X'))    # trova '2024'

# Con ancoraggio, verifica che la stringa intera sia un anno
print(re.fullmatch(r'\d{4}', '2024'))           # match
print(re.fullmatch(r'\d{4}', 'anno 2024'))      # None
```

---

## L'operatore di alternativa e i gruppi opzionali

Il metacarattere `|` funziona come OR: `A|B` corrisponde ad `A` oppure a `B`. All'interno
di un gruppo, `(A|B)` limita l'alternativa alla sola parte raggruppata, senza influenzare
il resto del pattern.

Combinando `|` con i quantificatori si possono descrivere parti opzionali complesse.
Il `?` dopo un gruppo, ad esempio `(qualcosa)?`, rende opzionale l'intera occorrenza del
gruppo.

```python
import re

# Il suffisso "_AB" o "_BA" è opzionale
pattern = r'campione_(AB|BA)?\.txt'

print(re.search(pattern, 'campione_AB.txt').group())    # campione_AB.txt
print(re.search(pattern, 'campione_BA.txt').group())    # campione_BA.txt
print(re.search(pattern, 'campione_.txt'))              # None (il gruppo vuoto non basta)
print(re.search(pattern, 'campione.txt').group())       # campione.txt
```

Notate nell'esempio precedente il punto `\.`: il punto ha bisogno del backslash per
essere trattato come carattere letterale, non come metacarattere "qualsiasi carattere".
In generale, per includere un metacarattere come carattere letterale nel pattern, lo si
precede con `\`.

---

## Raw strings: perché si scrive `r'...'`

In Python, i letterali stringa interpretano le sequenze di escape: `'\n'` è un newline,
`'\t'` è un tab, `'\d'` è un'd' con backslash (perché `\d` non è una sequenza speciale
Python, ma lo diventa se la stringa la passate al motore regex).

Il problema sorge quando le regex usano `\` per le proprie sequenze: per scrivere `\d`
in una stringa normale si dovrebbe scrivere `'\\d'` (doppio backslash, di cui uno viene
"consumato" dall'interprete Python lasciando `\d` al motore regex). Con pattern complessi
la situazione degenera: `\\b\\w+\\b` invece di `\b\w+\b`.

La soluzione standard è usare le **raw string literals** con il prefisso `r`: in una
raw string i backslash non vengono interpretati da Python e arrivano intatti al motore
regex. `r'\d+'` è equivalente a `'\\d+'` ma molto più leggibile. Per convenzione, i
pattern regex si scrivono sempre come raw string.

```python
import re

# Senza raw string: il doppio backslash è necessario
pattern_brutto = '\\d{4}-\\d{2}-\\d{2}'

# Con raw string: un solo backslash, come ci si aspetta
pattern_bello = r'\d{4}-\d{2}-\d{2}'

data = "Data: 2024-03-15"
print(re.search(pattern_bello, data).group())  # Stampa: 2024-03-15
```

---

## Compilare i pattern con `re.compile`

Se lo stesso pattern viene utilizzato molte volte (ad esempio in un ciclo su migliaia di
stringhe), conviene **compilarlo** in anticipo con `re.compile`. La funzione restituisce
un oggetto `Pattern` che espone gli stessi metodi di `re` (`search`, `match`, `findall`,
ecc.) ma senza dover rianalizzare il pattern a ogni chiamata.

```python
import re

# Compilare una volta
pattern_compilato = re.compile(r'\d{8}_\d{6}')

# Usare molte volte
nomi_file = [
    '20240315_093000_campione.txt',
    '20240316_100000_altro.txt',
    'file_senza_data.txt',
]

for nome in nomi_file:
    m = pattern_compilato.search(nome)
    if m:
        print(f"Trovato timestamp: {m.group()}")
    else:
        print(f"Nessun timestamp in: {nome}")

# Output:
# Trovato timestamp: 20240315_093000
# Trovato timestamp: 20240316_100000
# Nessun timestamp in: file_senza_data.txt
```

---

## Una nota sui quantificatori greedy e lazy

I quantificatori `*`, `+` e `{n,m}` sono per default **greedy** (avidi): cercano di
abbinare il maggior numero possibile di caratteri. Questo può sorprendere quando il
pattern contiene classi generiche.

Considerate `r'_(.+)_'` applicato a `'_alfa_beta_gamma_'`: il gruppo cattura
`'alfa_beta_gamma'` (dalla prima all'ultima sottolineatura), non `'alfa'` come ci si
potrebbe aspettare. Per ottenere il comportamento *lazy* (abbina il meno possibile)
si aggiunge `?` dopo il quantificatore: `r'_(.+?)_'` cattura solo `'alfa'`.

Nella pratica, quando la struttura del formato è nota e precisa (come in un nome di file
con separatori fissi), è meglio descrivere esplicitamente i caratteri ammessi con classi
`[^_]+` (qualsiasi cosa che non sia il separatore) invece di affidarsi ai quantificatori
lazy.

```python
import re

s = '_alfa_beta_gamma_'

# Greedy: cattura tutto tra la prima e l'ultima _
print(re.search(r'_(.+)_', s).group(1))    # Stampa: alfa_beta_gamma

# Lazy: cattura il minimo possibile
print(re.search(r'_(.+?)_', s).group(1))   # Stampa: alfa

# Esplicito: cattura solo caratteri non-underscore
print(re.search(r'_([^_]+)_', s).group(1)) # Stampa: alfa
```

---

## Verso un pattern reale: nomi di file di misura

Mettendo insieme quanto visto, si è ora in grado di costruire un pattern per un caso
concreto: i file generati da una sessione di misura elettrica sotto vuoto seguono questa
convenzione:

```
YYYYMMDD_HHMMSS_SAMPLE_PPRESSURE_TTEMPERATURE[_(AB|BA)].txt
```

Per esempio: `20240315_093000_GaSb_P1.2E-3_T450.txt`
oppure: `20240315_093000_GaSb_P1.2E-3_T450_AB.txt`

I campi da estrarre sono:

- **timestamp**: data e ora, da convertire in un oggetto `datetime`
- **sample**: nome del campione (caratteri alfanumerici e trattini)
- **pressure_torr**: valore numerico dopo la lettera `P` (può essere in notazione
  scientifica: `1.2E-3`)
- **temperature_k**: valore intero dopo la lettera `T`
- **alignment**: suffisso opzionale `AB` o `BA` (allineamento Van der Pauw)

Si procede per costruzione progressiva, un campo alla volta.

**Timestamp.** La data è `\d{8}`, l'ora è `\d{6}`, separati da `_`:

```python
r'(?P<ts>\d{8}_\d{6})'
```

**Nome campione.** Segue un separatore `_`, poi una sequenza di caratteri alfanumerici
(nessuno spazio, nessun separatore):

```python
r'_(?P<sample>[A-Za-z0-9]+)'
```

**Pressione.** La lettera `P` seguita da un numero che può contenere cifre, punto
decimale, e notazione scientifica (`E` o `e` con segno opzionale):

```python
r'_P(?P<pressure>[0-9]*\.?[0-9]+(?:[Ee][+-]?\d+)?)'
```

Il sottogruppo `(?:[Ee][+-]?\d+)?` gestisce l'esponente opzionale. Il `(?:...)` è non
catturante: non vogliamo che l'esponente diventi un gruppo separato.

**Temperatura.** La lettera `T` seguita da un intero:

```python
r'_T(?P<temperature>\d+)'
```

**Allineamento.** Opzionale, separatore `_` seguito da `AB` o `BA`:

```python
r'(?:_(?P<alignment>AB|BA))?'
```

**Estensione e ancoraggio.** Il file deve terminare con `.txt`. Si ancora la fine con `$`:

```python
r'\.txt$'
```

**Pattern completo:**

```python
import re
from datetime import datetime

FILENAME_PATTERN = re.compile(
    r'^'
    r'(?P<ts>\d{8}_\d{6})'       # timestamp YYYYMMDD_HHMMSS
    r'_(?P<sample>[A-Za-z0-9]+)'  # nome campione
    r'_P(?P<pressure>[0-9]*\.?[0-9]+(?:[Ee][+-]?\d+)?)'  # pressione
    r'_T(?P<temperature>\d+)'     # temperatura
    r'(?:_(?P<alignment>AB|BA))?' # allineamento opzionale
    r'\.txt$',                    # estensione
    re.IGNORECASE
)

def parse_filename(filename: str) -> dict | None:
    """Estrae i metadati da un nome file di misura.

    Args:
        filename: Nome del file da analizzare.

    Returns:
        Dizionario con i campi estratti, oppure None se il formato
        non corrisponde.
    """
    m = FILENAME_PATTERN.match(filename)
    if not m:
        return None

    return {
        'sample':       m.group('sample'),
        'timestamp':    datetime.strptime(m.group('ts'), '%Y%m%d_%H%M%S'),
        'pressure_torr': float(m.group('pressure')),
        'temperature_k': int(m.group('temperature')),
        'alignment':    m.group('alignment'),  # None se assente
    }


# --- Test ---
casi = [
    '20240315_093000_GaSb_P1.2E-3_T450.txt',
    '20240315_093000_GaSb_P1.2E-3_T450_AB.txt',
    '20240316_120000_InAs_P5e-4_T300_BA.txt',
    'file_senza_formato.txt',
    '20240315_093000_GaSb_P1.2E-3_T450_CD.txt',  # allineamento non valido
]

for nome in casi:
    risultato = parse_filename(nome)
    if risultato:
        print(f"OK  {nome}")
        print(f"    campione:     {risultato['sample']}")
        print(f"    timestamp:    {risultato['timestamp']}")
        print(f"    pressione:    {risultato['pressure_torr']} Torr")
        print(f"    temperatura:  {risultato['temperature_k']} K")
        print(f"    allineamento: {risultato['alignment']}")
    else:
        print(f"NO  {nome}")
    print()
```

L'output produce:

```
OK  20240315_093000_GaSb_P1.2E-3_T450.txt
    campione:     GaSb
    timestamp:    2024-03-15 09:30:00
    pressione:    0.0012 Torr
    temperatura:  450 K
    allineamento: None

OK  20240315_093000_GaSb_P1.2E-3_T450_AB.txt
    campione:     GaSb
    timestamp:    2024-03-15 09:30:00
    pressione:    0.0012 Torr
    temperatura:  450 K
    allineamento: AB

OK  20240316_120000_InAs_P5e-4_T300_BA.txt
    campione:     InAs
    timestamp:    2024-03-16 12:00:00
    pressione:    0.0005 Torr
    temperatura:  300 K
    allineamento: BA

NO  file_senza_formato.txt

NO  20240315_093000_GaSb_P1.2E-3_T450_CD.txt
```

Il flag `re.IGNORECASE` è stato aggiunto per accettare sia `P1.2E-3` che `P1.2e-3` senza
dover duplicare la logica nel pattern. Il nome del campione è limitato a `[A-Za-z0-9]+`:
se i nomi possono contenere trattini o altri caratteri, basterà estendere la classe a
`[A-Za-z0-9\-]+`.

---

## Conclusioni

Le espressioni regolari occupano una posizione precisa nell'arsenale di chi elabora testi:
non sostituiscono il parsing strutturato (un parser JSON, un lettore CSV, una libreria
dedicata ai formati scientifici) ma sono insostituibili quando si ha a che fare con
stringhe semi-strutturate il cui formato è noto ma non è codificato in uno schema formale.
È il caso tipico dei nomi di file generati da strumenti di misura, dei log, delle
configurazioni testuali.

La capacità di usarle bene si costruisce per livelli: prima si impara a riconoscere i
caratteri letterali e i metacaratteri, poi si aggiungono i quantificatori, poi i gruppi
di cattura nominati. Il salto qualitativo arriva quando si passa da "scrivere un pattern
che funzioni" a "scrivere un pattern che comunichi la struttura": il pattern completo
nell'esempio finale, pur nella sua lunghezza, è leggibile perché ogni gruppo ha un nome
che rivela il suo significato.

Chi vuole approfondire può esplorare i **lookahead e lookbehind** (`(?=...)`, `(?!...)`,
`(?<=...)`, `(?<!...)`), che permettono di imporre condizioni sul contesto senza includerlo
nella corrispondenza. Un'altra direzione utile è la modalità `re.VERBOSE`, che permette
di spezzare un pattern su più righe e aggiungere commenti in linea: ideale per pattern
lunghi come quello sviluppato in questa dispensa.
