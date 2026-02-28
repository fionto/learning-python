# File I/O e la Funzione open() in Python

## Introduzione: Il Dialogo tra Programma e Filesystem

Fino ad ora abbiamo lavorato principalmente con dati che risiedono nella memoria del nostro computer. Quando scriviamo una lista, un dizionario, o leggiamo l'input dell'utente, stiamo operando su informazioni transitorie: non appena il programma termina, tutto scompare. Ma cosa succede quando dobbiamo salvare informazioni che devono persistere oltre l'esecuzione del nostro codice? Cosa fare quando abbiamo migliaia di record da elaborare e non possiamo caricarli tutti in memoria contemporaneamente?

La risposta a queste domande risiede nel concetto di **File I/O** (Input/Output su file), che rappresenta il ponte tra il nostro programma Python e il sistema di storage permanente del computer. Un file, nel suo senso più astratto, è una sequenza di dati memorizzata sul disco rigido, su una memoria SSD, o su qualsiasi altro supporto di archiviazione. Imparare a leggere e scrivere file è la porta d'accesso verso applicazioni vere, capaci di mantenere stato tra le esecuzioni e di comunicare con il mondo esterno.

In questo capitolo esamineremo come Python ci consente di interagire con il filesystem attraverso la funzione `open()`, affrontando non solo la sintassi, ma soprattutto la logica concettuale che la sottende. Comprenderete come Python astrae i dettagli tecnici del sistema operativo per offrirci un'interfaccia elegante e coerente con il resto del linguaggio.

---

## Cosa Succede Quando Apriamo un File

Prima di scrivere una singola riga di codice, è importante capire cosa significa veramente "aprire un file" dal punto di vista del sistema operativo e di Python. Quando il vostro programma decide di accedere a un file sul disco, non può semplicemente dire "leggi questo file" senza ulteriori dettagli. Il sistema operativo ha bisogno di sapere diverse cose: dove si trova il file nel filesystem? Voglio leggerlo, scriverci sopra, o entrambi? Come devo gestire i caratteri speciali se il file contiene testo? Quanto di una volta devo caricare in memoria prima di processare i dati?

Python risolve questa complessità attraverso un oggetto speciale: il **file object**. Quando aprite un file con `open()`, non state semplicemente accedendo a dati grezzi sul disco. State creando un oggetto intermedio che rappresenta la connessione tra il vostro programma e il file stesso. Questo oggetto mantiene traccia di dove siete nel file (quale riga state leggendo?), quale modalità di accesso state usando (lettura, scrittura, aggiunta?), come interpretare i byte sul disco (quale encoding usare?). È come avere un intermediario che conosce i dettagli tecnici e ve li nasconde dietro un'interfaccia semplice.

Questa è una decisione di design cruciale in Python: l'astrazione attraverso oggetti. Non lavorate mai direttamente con i byte grezzi del disco. Lavorate sempre con un oggetto file che incapsula quel comportamento.

---

## La Firma della Funzione open()

La funzione `open()` è fornita come built-in di Python, il che significa che non dovete importare nulla per usarla. La sua firma completa è:

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, 
     newline=None, closefd=True, opener=None)
```

Sebbene questa firma sembri intimidatoria, il 95% del vostro lavoro quotidiano userà solo i primi due o tre parametri. Conviene però capire tutti questi parametri per apprezzare la profondità del design di Python.

### Il Parametro `file`

Il primo parametro, `file`, specifica quale file desiderate aprire. Accetta due tipi di input: un percorso (path) come stringa oppure un file descriptor (numero intero che rappresenta il file a livello di sistema operativo). Nel 99% dei casi, userete un percorso come stringa.

```python
# Esempio semplice: aprire un file per lettura
with open('dati.txt') as f:
    contenuto = f.read()
```

In questo esempio, `'dati.txt'` è il percorso relativo del file. "Relativo" significa relativo alla directory di lavoro corrente del vostro script. Se il vostro script si trova in `/home/utente/progetti/` e il file `dati.txt` è nella stessa directory, Python lo troverà. Se invece fosse in una sottocartella, scrivereste `'subfolder/dati.txt'`.

Naturalmente potete anche usare percorsi assoluti, che descrivono la posizione completa del file a partire dalla radice del sistema:

```python
# Su Unix/Linux/macOS
with open('/home/utente/documents/dati.txt') as f:
    contenuto = f.read()

# Su Windows
with open('C:\\Users\\utente\\Documents\\dati.txt') as f:
    contenuto = f.read()
```

Notate come su Windows usate backslash (`\`) mentre su Unix usate forward slash (`/`). Python è intelligente: potete usare forward slash anche su Windows, e Python li convertirà automaticamente. Anzi, è consigliato per portabilità.

### Il Parametro `mode`

Il secondo parametro, `mode`, specifica cosa intendete fare con il file. Non è opzionale dal punto di vista logico: dovete sempre avere in mente se state leggendo, scrivendo, o aggiungendo dati. Il valore predefinito è `'r'` (lettura), ma è buona pratica specificarlo sempre per chiarezza.

Le modalità principali sono:

**`'r'` - Lettura (Read)**. Apre il file in modalità di sola lettura. Potete leggere il contenuto ma non modificarlo. Se il file non esiste, riceverete un'eccezione `FileNotFoundError`. Questa è la modalità predefinita.

**`'w'` - Scrittura (Write)**. Apre il file in modalità di scrittura. Se il file esiste già, viene completamente sovrascritto (troncato): il contenuto precedente è perso. Se il file non esiste, viene creato. È come prendere un foglio di carta vuoto: potete scrivere su di esso, ma non potete aggiungere testo dopo quello che c'era prima (perché non c'era niente).

**`'a'` - Aggiunta (Append)**. Apre il file in modalità di aggiunta. Se il file esiste, i nuovi dati vengono aggiunti alla fine. Se non esiste, viene creato. È la modalità opposta a `'w'`: invece di sovrascrivere, estendete.

**`'x'` - Creazione esclusiva (Exclusive creation)**. Crea un nuovo file. Se il file esiste già, riceverete un'eccezione `FileExistsError`. È utile quando siete certi che il file non dovrebbe esistere e volete un errore esplicito se qualcosa è andato storto.

Questi caratteri di base possono essere combinati con altri per specificare ulteriormente il comportamento:

**`'b'` - Modalità binaria (Binary)**. Usate questo quando lavorate con file non testuali: immagini, audio, file compressi. I dati vengono letti come `bytes` senza alcuna interpretazione di encoding.

**`'t'` - Modalità testuale (Text)**. Questa è la modalità predefinita e non occorre specificarla. I dati vengono letti come stringhe, con il sistema che automaticamente gestisce le conversioni di encoding.

**`'+'` - Lettura e scrittura (Update)**. Combine lettura e scrittura nello stesso file. Modalità avanzata, usate con cautela.

Quindi, ad esempio, `'rb'` significa "leggi il file in modalità binaria", mentre `'w+'` significa "apri per leggere e scrivere, sovrascrivendo se esiste".

```python
# Lettura di un file di testo
with open('documento.txt', 'r') as f:
    testo = f.read()

# Scrittura su un nuovo file (sovrascrive se esiste)
with open('output.txt', 'w') as f:
    f.write('Ciao, file system!')

# Aggiunta a un file esistente
with open('log.txt', 'a') as f:
    f.write('Una nuova riga di log\n')

# Lettura di un file binario (ad esempio un'immagine)
with open('foto.jpg', 'rb') as f:
    dati_immagine = f.read()

# Scrittura di dati binari
with open('output.bin', 'wb') as f:
    f.write(bytes([65, 66, 67]))  # Scrive i byte ABC
```

---

## Il Parametro `encoding`

Quando lavorate con file di testo (non binari), Python deve sapere come interpretare i byte sul disco come caratteri. Questo processo si chiama **encoding** (decodifica). Diversi encoding rappresentano i caratteri in modo diverso. Il più comune e consigliato è UTF-8, che supporta praticamente tutti i caratteri del mondo (lettere accentate, emoji, caratteri cinesi, arabi, etc.).

```python
# Se non specificate encoding, Python usa il default del vostro sistema
# Su Windows potrebbe essere 'cp1252' (codifica Windows)
# Su macOS e Linux è generalmente 'utf-8'

# È meglio essere espliciti
with open('testo_italiano.txt', 'r', encoding='utf-8') as f:
    contenuto = f.read()
```

Se il vostro file contiene caratteri speciali e non specificate l'encoding corretto, potreste ottenere errori confusi:

```python
# Esempio di errore di encoding (male)
with open('testo_con_accenti.txt', 'r') as f:
    # Se il file contiene "è" (e accentata) e il sistema
    # non aspettava UTF-8, potreste ottenere:
    # UnicodeDecodeError: 'cp1252' codec can't decode byte 0xc3...
    contenuto = f.read()

# Soluzione corretta
with open('testo_con_accenti.txt', 'r', encoding='utf-8') as f:
    contenuto = f.read()  # Funziona perfettamente
```

Python 3, la versione che state usando, ha UTF-8 come encoding di default su la maggior parte dei sistemi moderni, ma è comunque buona pratica specificarlo esplicitamente. Rende il vostro codice portabile e comprensibile.

### Il Parametro `errors`

Strettamente legato a `encoding`, il parametro `errors` specifica cosa fare quando Python incontra un byte che non può decodificare. Le opzioni principali sono:

**`'strict'` (predefinito)**: Lancia un'eccezione. Il programma si ferma. È la scelta più rigorosa e solitamente la desiderate per evitare di elaborare silenziosamente dati corrotti.

**`'ignore'`**: Ignora i caratteri problematici. Se incontra un byte illegittimo, lo salta. Potrebbe portare a perdita di dati, ma a volte è accettabile se state solo cercando informazioni sparse in un file sporco.

**`'replace'`**: Sostituisce i caratteri illegittimi con un marcatore sostitutivo (di solito `?`). Mantiene il file leggibile e vi avverte che c'è stato un problema.

**`'surrogateescape'`**: Opzione avanzata che rappresenta i byte problematici come "caratteri surrogati". Permette di ri-salvare il file in seguito e recuperare esattamente gli stessi byte originali, anche se non potete leggerli come testo.

```python
# Lettura di un file "sporco" con encoding incerto
with open('file_sporco.txt', 'r', encoding='utf-8', errors='replace') as f:
    # Se ci sono byte non-UTF-8, vengono sostituiti con '?'
    contenuto = f.read()
```

---

## Il Parametro `newline`

Un aspetto spesso trascurato ma importante è come Python gestisce i caratteri di "andare a capo" (newline). Diversi sistemi operativi usano convenzioni diverse:

- **Unix/Linux/macOS** usa `\n` (line feed)
- **Windows** usa `\r\n` (carriage return + line feed)
- **Vecchi Mac** usavano `\r` (solo carriage return)

Quando leggete un file in modalità testuale, Python normalizza automaticamente tutti questi al semplice `\n`. Quando scrivete, converte `\n` nel formato nativo del vostro sistema operativo. Di norma non dovete pensarci.

Tuttavia, il parametro `newline` vi permette di controllare questo comportamento se necessite di gestire file con convenzioni specifiche:

```python
# Lettura con normalizzazione automatica dei newline (predefinito)
with open('file.txt', 'r', newline=None) as f:
    righe = f.readlines()  # Tutte le righe finiscono con \n

# Lettura senza normalizzazione (newline restituiti come sono)
with open('file.txt', 'r', newline='') as f:
    righe = f.readlines()  # Newline rimangono come nel file originale

# Scrittura con un newline specifico
with open('file_unix.txt', 'w', newline='\n') as f:
    f.write('Riga 1\nRiga 2\n')  # Usa sempre \n anche su Windows
```

---

## Il Parametro `buffering`

Quando scrivete su un file, Python non scrive necessariamente ogni singolo carattere immediatamente sul disco. Questo sarebbe estremamente inefficiente. Invece, usa un **buffer**: accumula i dati in memoria e, ogni tanto, li scrive tutti insieme sul disco. Questo è una delle ottimizzazioni comuni in I/O che rende i programmi veloci. Il parametro `buffering` vi permette di controllare questa strategia:

**`buffering=-1` (predefinito)**: Python sceglie la strategia migliore in base al contesto. Per file binari, usa un buffer fisso (di solito 8 KB). Per file testuali, usa il buffering a livello di riga.

**`buffering=0`**: Nessun buffering. Ogni scrittura va direttamente al disco. Utile solo per file binari se dovete essere certi che i dati siano subito persistiti.

**`buffering=1`**: Buffering a livello di riga. La riga intera viene accumulata e poi scritta insieme quando incontra un `\n`. Utile per log file.

**`buffering > 1`**: Buffer di dimensione fissa. Ad esempio, `buffering=4096` accumula fino a 4KB di dati prima di scrivere.

```python
# Per scrivere un log in tempo reale senza ritardi
with open('log.txt', 'w', buffering=1) as f:
    f.write('Log start\n')  # Scritto subito
    f.write('Dati\n')       # Scritto subito
    # Ogni \n forza lo scaricamento del buffer

# Per migliore performance con molti dati
with open('output.dat', 'w', buffering=65536) as f:  # Buffer da 64KB
    for i in range(1000000):
        f.write(f'Riga {i}\n')  # Scritto ogni 64KB, molto veloce
```

Nella pratica, il buffering predefinito funziona bene per il 99% dei casi. Ne parlerò più solo quando optimize performance è critico.

---

## Leggere File: I Metodi Fondamentali

Aperto un file in modalità lettura, Python vi offre diversi metodi per accedere ai dati. Ogni metodo rappresenta una strategia diversa, utile in contesti diversi.

### `.read()` - Leggere l'Intero File

Il metodo più semplice è `.read()`, che carica l'intero contenuto del file in memoria e lo restituisce come una singola stringa (o bytes se il file è binario).

```python
with open('articolo.txt', 'r', encoding='utf-8') as f:
    testo_completo = f.read()
    print(f"Ho letto {len(testo_completo)} caratteri")
```

Questo è elegante e semplice, ma ha un'importante limitazione: se il file è molto grande (gigabyte), caricarlo interamente in memoria potrebbe essere impossibile. Immaginate di dover processare un file di log da 50 GB: il vostro computer non ha 50 GB di RAM libera.

### `.read(size)` - Leggere una Porzione

Se passate un argomento a `.read()`, legge solo quel numero di caratteri (o byte, se binario):

```python
with open('file_grande.dat', 'rb') as f:
    # Leggi i primi 1024 byte
    intestazione = f.read(1024)
    # Leggi altri 1024 byte
    dati_parte_1 = f.read(1024)
    # Leggi altri 1024 byte
    dati_parte_2 = f.read(1024)
    # Ogni read() continua da dove si è fermato l'ultimo
```

Questo permette di processare file grandi un pezzo alla volta, mantenendo costante l'uso di memoria. Il file object tiene traccia della vostra posizione nel file, come un segnalibro che si muove mentre leggete.

### `.readline()` - Leggere una Riga alla Volta

Particolarmente utile per file testuali, `.readline()` legge una singola riga (incluso il carattere di newline alla fine):

```python
with open('dati.txt', 'r') as f:
    riga_1 = f.readline()  # "Nome,Età,Città\n"
    riga_2 = f.readline()  # "Alice,30,Roma\n"
    riga_3 = f.readline()  # "Bob,25,Milano\n"
```

Il vantaggio è che potete processare il file riga per riga senza caricarlo tutto in memoria. Se il file ha milioni di righe, elaborate una riga, estraete l'informazione che vi serve, e poi passate alla prossima.

### `.readlines()` - Leggere Tutte le Righe in una Lista

Un compromesso tra `.read()` e `.readline()` è `.readlines()`, che restituisce una lista con tutte le righe:

```python
with open('lista_persone.txt', 'r') as f:
    righe = f.readlines()
    # righe = ["Nome,Età,Città\n", "Alice,30,Roma\n", "Bob,25,Milano\n"]
    
    for riga in righe:
        dati = riga.strip().split(',')
        print(f"Persona: {dati[0]}, {dati[1]} anni")
```

Notate il `.strip()`: `.readlines()` mantiene il `\n` alla fine di ogni riga, che solitamente volete rimuovere prima di processare.

### Iterazione Diretta sul File Object

In realtà, il metodo più "pythonic" è iterare direttamente sul file object, che restituisce le righe una alla volta in modo efficiente:

```python
with open('log.txt', 'r') as f:
    for riga in f:
        # Ogni iterazione legge una riga dal file
        # Il file object è un iteratore intelligente
        print(riga.strip())
```

Questo ha il vantaggio di essere sia conciso che efficiente: non caricate tutte le righe in memoria, le processate una per una man mano.

---

## Scrivere su File

Analogamente alla lettura, ci sono diversi metodi per scrivere su file. La dinamica è simile: scrivete dati che vengono accumulati in un buffer e poi persistiti sul disco.

### `.write()` - Scrivere una Stringa

Il metodo fondamentale è `.write()`, che prende una stringa (o bytes se binario) e la scrive sul file:

```python
with open('output.txt', 'w') as f:
    f.write('Prima riga\n')
    f.write('Seconda riga\n')
    f.write('Terza riga\n')
```

Importante: `.write()` NON aggiunge automaticamente newline. Se volete una nuova riga, dovete aggiungere `\n` esplicitamente. Questo è intenzionale: vi dà il massimo controllo.

Un aspetto cruciale: quando aprite un file con modalità `'w'`, il contenuto precedente viene cancellato. Se volete aggiungere dati senza perdere ciò che c'è già, usate `'a'`:

```python
# Sovrascrive completamente
with open('dati.txt', 'w') as f:
    f.write('Nuovi dati')  # Contenuto precedente è perso

# Aggiunge alla fine
with open('dati.txt', 'a') as f:
    f.write('Altri dati\n')  # Contenuto precedente è preservato
```

### `.writelines()` - Scrivere Più Righe

Se avete una lista di stringhe, potete scriverle tutte con `.writelines()`:

```python
righe = ['Riga 1\n', 'Riga 2\n', 'Riga 3\n']

with open('output.txt', 'w') as f:
    f.writelines(righe)
```

Notate che `.writelines()` scrive le righe esattamente come sono nella lista. Se le righe non hanno `\n`, non verranno aggiunti automaticamente. È un nome leggermente ingannevole: non aggiunge "line", scrive semplicemente tutte le stringhe in sequenza.

---

## Il Context Manager: `with`

Abbiamo usato il costrutto `with` in ogni esempio, ma conviene dedicarvi un'attenzione particolare perché rappresenta un pattern cruciale in Python.

Quando lavorate con file, è essenziale che il file venga chiuso quando avete finito di usarlo, anche se accade un errore durante la lettura o la scrittura. Chiudere un file significa dire al sistema operativo: "Non ho più bisogno di questo file, puoi liberare le risorse associate".

Senza `with`, dovreste scrivere così:

```python
# Modo vecchio e prono a errori
f = open('dati.txt', 'r')
try:
    contenuto = f.read()
    # Se accade un errore qui, il file non viene chiuso!
except Exception as e:
    print(f"Errore: {e}")
finally:
    f.close()  # Closure garantito anche in caso di errore
```

È verboso e prono a errori: è facile dimenticare il `.close()` e lasciare file aperti. Python offre il **context manager**, introdotto con l'istruzione `with`, che automatizza tutto questo:

```python
# Modo moderno e elegante
with open('dati.txt', 'r') as f:
    contenuto = f.read()
# Il file è automaticamente chiuso qui, anche se accade un errore

# Anche questo funziona:
try:
    with open('dati.txt', 'r') as f:
        contenuto = f.read()
        # Se accade un errore durante la lettura
        x = 1 / 0
except ZeroDivisionError:
    print("Errore matematico!")
# Il file è comunque chiuso, nonostante l'eccezione
```

Il contesto manager è un oggetto che sa come "entrare" (quando cominciate il blocco `with`) e "uscire" (quando lo terminate, per qualsiasi ragione). Quando esce, garantisce di eseguire la pulizia necessaria. Non dovete pensarci: è tutto automatico.

---

## Percorsi Relativi vs Assoluti

Quando specificate il percorso di un file, dovete decidere se usare un percorso relativo o assoluto. Comprendere la differenza è cruciale per evitare l'errore `FileNotFoundError`.

Un **percorso relativo** è relativo alla directory di lavoro corrente del vostro script:

```python
# Se il vostro script è in /home/utente/progetti/
# e dati.txt è nella stessa directory
with open('dati.txt') as f:
    pass

# Se dati.txt è in una subdirectory
with open('subfolder/dati.txt') as f:
    pass

# Se dati.txt è nella directory padre
with open('../dati.txt') as f:
    pass
```

Un **percorso assoluto** specifica la posizione completa a partire dalla radice del filesystem:

```python
# Su Unix/Linux/macOS
with open('/home/utente/progetti/dati.txt') as f:
    pass

# Su Windows
with open('C:\\Users\\utente\\Projects\\dati.txt') as f:
    pass
```

Quando lavorate in un team o pubblicate codice, i percorsi assoluti sono problematici: non funzioneranno su computer altrui. I percorsi relativi sono preferibili. Se la struttura è complessa, esiste il modulo `pathlib` che rende tutto più robusto e portabile:

```python
from pathlib import Path

# Crea un percorso relativo in modo robusta
data_dir = Path(__file__).parent / 'data'
file_path = data_dir / 'dati.txt'

with open(file_path) as f:
    contenuto = f.read()
```

`Path(__file__)` è la directory dello script corrente, e l'operatore `/` concatena i componenti del percorso in modo indipendente dal sistema operativo. Su Windows diventa automaticamente una stringa con backslash; su Unix, forward slash.

---

## Gestione degli Errori

Diverse cose possono andare storte quando lavorate con file. Comprendere gli errori comuni e come gestirli è parte della programmazione professionale.

### FileNotFoundError

L'errore più comune: il file non esiste dove lo state cercando.

```python
# Errore: il file non esiste
with open('file_inesistente.txt') as f:
    contenuto = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'file_inesistente.txt'

# Gestione dell'errore
try:
    with open('file.txt') as f:
        contenuto = f.read()
except FileNotFoundError:
    print("Il file non esiste. Sto creando uno nuovo...")
    with open('file.txt', 'w') as f:
        f.write('Contenuto predefinito')
```

### PermissionError

Il file esiste ma non avete permessi di accesso:

```python
try:
    with open('/etc/passwd', 'w') as f:  # File di sistema, non modificabile
        f.write('test')
except PermissionError:
    print("Non hai permessi per modificare questo file")
```

### IsADirectoryError

Avete specificato una directory invece di un file:

```python
try:
    with open('/home/utente/', 'r') as f:
        contenuto = f.read()
except IsADirectoryError:
    print("Questo è un percorso di directory, non di file")
```

### UnicodeDecodeError

Avete specificato un encoding sbagliato:

```python
# Il file contiene UTF-8 ma specificate un encoding diverso
try:
    with open('testo.txt', 'r', encoding='ascii') as f:
        contenuto = f.read()  # Errore se il file ha caratteri non-ASCII
except UnicodeDecodeError as e:
    print(f"Errore di encoding: {e}")
    # Retry con encoding corretto
    with open('testo.txt', 'r', encoding='utf-8') as f:
        contenuto = f.read()
```

Una buona pratica è sempre avvolgere operazioni file in try-except quando sono critiche:

```python
def leggi_configurazione(percorso):
    try:
        with open(percorso, 'r', encoding='utf-8') as f:
            config = f.read()
        return config
    except FileNotFoundError:
        print(f"Configurazione non trovata: {percorso}")
        return None
    except UnicodeDecodeError:
        print(f"Encoding non supportato in {percorso}")
        return None
    except Exception as e:
        print(f"Errore non previsto: {e}")
        return None
```

---

## Caso di Studio: Processare un File CSV

Uniamo quanto imparato con un esempio pratico. Supponete di avere un file CSV (comma-separated values) con dati di vendite e volete processarlo:

```python
# dati_vendite.csv
# prodotto,quantità,prezzo
# Mela,100,0.50
# Banana,150,0.30
# Arancia,80,0.60
```

Ecco un programma che lo legge, lo elabora e scrive un report:

```python
# Lettura e elaborazione
totale_vendite = 0
report_lines = []

try:
    with open('dati_vendite.csv', 'r', encoding='utf-8') as f:
        # Salta l'intestazione
        intestazione = f.readline()
        
        # Processa ogni riga
        for riga in f:
            # Rimuove newline e spazia
            riga = riga.strip()
            
            # Salta righe vuote
            if not riga:
                continue
            
            # Estrae i dati
            prodotto, quantita, prezzo = riga.split(',')
            quantita = int(quantita)
            prezzo = float(prezzo)
            
            # Calcola il totale per questo prodotto
            totale_prodotto = quantita * prezzo
            totale_vendite += totale_prodotto
            
            # Accumula il report
            report_lines.append(
                f"{prodotto}: {quantita} unità a €{prezzo:.2f} = €{totale_prodotto:.2f}"
            )

except FileNotFoundError:
    print("File dati_vendite.csv non trovato")
    exit(1)

# Scrive il report su file
try:
    with open('report_vendite.txt', 'w', encoding='utf-8') as f:
        f.write("=== REPORT VENDITE ===\n\n")
        
        for riga in report_lines:
            f.write(riga + '\n')
        
        f.write(f"\nTOTALE VENDITE: €{totale_vendite:.2f}\n")

    print("Report scritto su report_vendite.txt")

except PermissionError:
    print("Non hai permessi per scrivere il report")
except Exception as e:
    print(f"Errore durante la scrittura del report: {e}")
```

Questo esempio illustra concetti chiave: gestione degli errori, iterazione su righe, parsing di dati, accumulo di risultati, e scrittura strutturata del output. È una applicazione piccolina ma realistica di File I/O.

---

## Considerazioni di Performance e Best Practice

Quando lavorate con file grandi, la performance diventa importante. Ecco alcune linee guida:

**Leggete grandi file a pezzi, non tutto insieme**. Se dovete processare un file da 1 GB, non caricatelo tutto in memoria:

```python
# Male: carica tutto in memoria
with open('file_grande.txt') as f:
    contenuto = f.read()  # 1 GB di RAM usati!
    for riga in contenuto.split('\n'):
        print(riga)

# Bene: legge riga per riga
with open('file_grande.txt') as f:
    for riga in f:  # Legge una riga alla volta
        print(riga.strip())
```

**Usate buffering appropriato** quando scrivete molti dati:

```python
# Se dovete scrivere milioni di linee
with open('output.txt', 'w', buffering=65536) as f:
    for i in range(1000000):
        f.write(f'Riga {i}\n')
# Il buffering accumula i dati e riduce le operazioni disco
```

**Specificate sempre l'encoding**. È una riga in più che vi salva da ore di debug:

```python
# Sempre
with open('file.txt', 'r', encoding='utf-8') as f:
    pass

# Non
with open('file.txt', 'r') as f:
    pass
```

**Usate `with` senza eccezioni**. Non abbandonate mai file aperti:

```python
# Male
f = open('file.txt')
contenuto = f.read()
# Se accade un errore, f.close() non viene mai chiamato

# Bene
with open('file.txt') as f:
    contenuto = f.read()
# f è sempre chiuso, indipendentemente da cosa accade
```

---

## Conclusione

La funzione `open()` e il concetto di File I/O sono il fondamento di ogni applicazione che deve persistere dati, comunicare con il filesystem, o processare informazioni da sources esterni. Sebbene la funzione stessa offra una superficie semplice, la profondità del design di Python emerge una volta che comprendete i dettagli: come i context managers garantiscono pulizia, come il buffering ottimizza la performance, come gli encoding risolvono il problema della rappresentazione universale di caratteri.

Ricordate che File I/O non è solo sintassi: è il dialogo tra il vostro programma e il sistema di storage. Comprendere questa dinamica vi permette di scrivere codice robusto, efficiente, e privo di errori. E una volta che padroneggiate `open()`, scoprirete che la maggior parte dei vostri problemi reali (che siano log, CSV, JSON, o qualsiasi altro formato) diventeranno affrontabili.

Nel prossimo capitolo, esamineremo come gestire i formati strutturati come JSON e CSV usando librerie Python specializzate, costruendo su queste fondamenta di File I/O.