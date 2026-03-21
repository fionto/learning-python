# Capitolo 1: Introduzione alla Programmazione e a Python

## Parte 1: Fondamenti della Programmazione

### 1.0.1 Imparare Python: Il Linguaggio di Oggi e di Domani

Questo corso rappresenta il primo capitolo di una serie didattica su Python Essentials. È stato progettato per fornire tutto ciò che occorre sapere per iniziare a progettare, scrivere, eseguire, sottoporre a debug e migliorare programmi Python a livello fondamentale. Il corso prepara completamente gli studenti all'esame di certificazione PCEP (Certified Entry-Level Python Programmer) dell'Istituto Python.

### 1.0.2 Informazioni sul Corso

Python Essentials 1 è stato progettato e sviluppato dall'OpenEDG Python Institute. Il corso è stato creato per chiunque desideri imparare Python e le moderne tecniche di programmazione.

Rivolto particolarmente a:

- Programmatori aspiranti e studenti interessati ad apprendere la programmazione per hobby o per compiti legati al lavoro
- Chi cerca di acquisire competenze fondamentali e conoscenze per ruoli entry-level come sviluppatore di software, analista di dati o tester
- Professionisti del settore che desiderano esplorare tecnologie connesse con Python o che lo utilizzano come fondamento
- Leader di team, product manager e project manager che vogliono comprendere la terminologia e i processi nel ciclo di sviluppo del software

### 1.0.3 Programma del Corso

In questo corso imparerete:

- I concetti universali della programmazione informatica
- La sintassi e la semantica del linguaggio Python
- Competenze pratiche nella risoluzione di sfide di implementazione tipiche
- Come utilizzare gli elementi più importanti della Libreria Standard di Python
- Come installare il vostro ambiente di runtime
- Come progettare, sviluppare, testare e sottoporre a debug programmi Python semplici

Il corso è diviso in quattro moduli:

**Modulo 1:** Introduzione a Python e alla programmazione informatica

**Modulo 2:** Tipi di dati, variabili, operazioni di input-output di base e operatori di base

**Modulo 3:** Valori booleani, esecuzione condizionale, cicli, elaborazione di liste, operazioni logiche e bitwise

**Modulo 4:** Funzioni, tuple, dizionari, eccezioni ed elaborazione dati

## Parte 2: Come Funziona un Programma per Computer

### 1.1.1 La Natura del Computer: Semplicità e Velocità

Un programma rende un computer utilizzabile. Senza un programma, anche il computer più potente è poco più che un oggetto inerte. Analogamente, senza un musicista, un pianoforte è solo una scatola di legno. La bellezza del piano risiede nella sua capacità di diventare vivo attraverso chi sa come suonarlo. Lo stesso vale per i computer e i programmi.

I computer possono eseguire compiti estremamente complessi, ma questa capacità non è innata. La natura reale del computer è molto più semplice e, paradossalmente, è questa semplicità che genera la sua potenza.

Un computer moderno può eseguire solo operazioni estremamente semplici. Ad esempio, un computer non può comprendere il valore di una complicata funzione matematica per conto proprio. Tuttavia, può eseguire operazioni molto elementari (come l'addizione o la divisione) con straordinaria velocità, e può ripetere queste azioni praticamente un numero illimitato di volte.

Qui risiede il segreto: la complessità non viene da operazioni singole complicate, ma dall'accumulo di miliardi di operazioni semplici, eseguite in sequenza ben orchestrata. È come costruire una cattedrale con singoli mattoni: nessun mattone è straordinario, ma l'architettura complessiva crea qualcosa di magnifico.

Considerate questo esempio: volete calcolare la velocità media che avete raggiunto durante un lungo viaggio. Conoscete la distanza percorsa, conoscete il tempo impiegato, e volete la velocità media.

Intuitivamente, il computer dovrebbe essere in grado di calcolarla. Ma il computer non è consapevole di concetti come "distanza", "velocità" o "tempo". Non ha intuizione del mondo fisico. Pertanto, è necessario istruire il computer a:

1. Accettare un numero che rappresenta la distanza (in chilometri, per esempio)
2. Accettare un numero che rappresenta il tempo di viaggio (in ore)
3. Dividere il primo numero per il secondo e immagazzinare il risultato in memoria
4. Visualizzare il risultato (che rappresenta la velocità media) in un formato leggibile

Queste quattro azioni semplici formano un programma. Naturalmente, queste istruzioni non sono ancora formalizzate nel linguaggio che il computer può capire, ma sono sufficientemente vicine. Il compito del programmatore è di tradurre queste istruzioni naturali in un linguaggio che il computer capisce.

**Language is the keyword** — il linguaggio è la chiave di tutto. È il ponte tra il nostro modo di pensare e il modo in cui il computer opera.

### 1.1.2 Linguaggi Naturali vs. Linguaggi di Programmazione

Un linguaggio è un mezzo e uno strumento per esprimere e registrare il pensiero. Intorno a noi ci sono molti linguaggi. Alcuni non richiedono né parole né scrittura, come il linguaggio del corpo; è possibile esprimere i propri sentimenti più profondi con estrema precisione senza pronunciare una sola parola.

Un altro linguaggio che usate ogni giorno è la vostra lingua madre, che usate per manifestare la vostra volontà e per riflettere sulla realtà. I computer hanno il loro linguaggio, chiamato linguaggio macchina, che è molto rudimentale.

Un computer, anche il più tecnicamente sofisticato, è privo di qualsiasi traccia di intelligenza vera. Potremmo dire che è come un cane ben addestrato: risponde solo a un insieme predeterminato di comandi noti. I comandi che riconosce sono molto semplici. Possiamo immaginare che il computer risponda a ordini come "prendi questo numero, dividilo per un altro e salva il risultato".

Un insieme completo di comandi noti è chiamato **lista di istruzioni** (Instruction List, abbreviato IL). Computer diversi possono variare in base alla dimensione della loro IL, e le istruzioni potrebbero essere completamente diverse in modelli diversi.

**Nota:** I linguaggi macchina sono sviluppati dagli umani, non dai computer. Nessun computer attualmente è in grado di creare un nuovo linguaggio. Tuttavia, questo potrebbe cambiare presto.

Proprio come le persone usano molti linguaggi diversi, anche le macchine hanno molti linguaggi diversi. La differenza, però, è che i linguaggi naturali si sono sviluppati naturalmente. Inoltre, continuano a evolversi, e ogni giorno vengono create nuove parole mentre le vecchie scompaiono. Questi linguaggi sono chiamati **linguaggi naturali**.

I linguaggi di programmazione, al contrario, sono artificiali. Sono stati creati intenzionalmente da umani per comunicare con le macchine. Hanno una struttura rigorosa e regole ben definite che non variano o cambiano in modo casuale.

### 1.1.3 Cosa Costituisce un Linguaggio: Gli Elementi Fondamentali

Possiamo dire che ogni linguaggio—che sia naturale o artificiale—consiste di quattro elementi fondamentali:

#### 1. **Alfabeto**

L'alfabeto è l'insieme di simboli di base utilizzati per costruire il linguaggio. Nel linguaggio naturale italiano, l'alfabeto comprende lettere come A, B, C... Z, nonché numeri, punteggiatura e altri simboli. Nel linguaggio di programmazione Python, l'alfabeto comprende i caratteri ASCII standard: lettere (maiuscole e minuscole), cifre (0-9), e vari simboli come `+`, `-`, `*`, `/`, `=`, `(`, `)`, ecc.

```python
# L'alfabeto di Python comprende questi simboli
# che utilizziamo per costruire il codice
variabile = 42
risultato = variabile + 8
```

Nel frammento di codice sopra possiamo riconoscere chiaramente l’alfabeto del linguaggio Python all’opera. Le lettere dell’alfabeto vengono combinate per formare identificatori come `variabile` e `risultato`, che sono nomi scelti dal programmatore. Le cifre (`42`, `8`) fanno parte anch’esse dell’alfabeto e permettono di rappresentare valori numerici. I simboli speciali, come `=` e `+`, sono elementi fondamentali dell’alfabeto di Python: il primo serve per assegnare un valore a una variabile, il secondo per eseguire un’operazione aritmetica. Anche spazi, a capo e parentesi (quando presenti) contribuiscono a rendere il codice interpretabile. Proprio come in una lingua naturale, l’alfabeto da solo non dice ancora *cosa* stiamo comunicando, ma fornisce i mattoni elementari con cui il linguaggio può essere costruito.

#### 2. **Lessico (Vocabolario)**

Il lessico è l'insieme di parole e simboli combinati che hanno un significato riconosciuto nel linguaggio. Nel linguaggio naturale, il lessico include tutte le parole che troviamo in un dizionario. Nel linguaggio di programmazione Python, il lessico include:

- **Parole chiave** (keywords): parole riservate che hanno un significato speciale, come `if`, `while`, `for`, `def`, `class`, `import`, ecc.
- **Identificatori**: nomi che voi create per variabili, funzioni e classi
- **Letterali**: valori espliciti come `42`, `"ciao"`, `3.14`
- **Operatori**: simboli come `+`, `-`, `*`, `/`, `==`, `!=`, ecc.

```python
# Parole chiave di Python
if temperatura > 30:
    print("Fa caldo!")  # print è una funzione built-in

# Identificatori creati da voi
mio_nome = "Alice"
velocita_auto = 120
```

Alcune parole fanno parte del vocabolario ufficiale del linguaggio, come `if`, che introduce una scelta logica, o `print`, che è una funzione già pronta per visualizzare informazioni. Queste parole non possono essere usate liberamente come nomi, perché hanno un ruolo preciso e condiviso. Accanto a esse compaiono parole create dal programmatore, come `temperatura`, `mio_nome` e `velocita_auto`: sono identificatori costruiti usando l’alfabeto del linguaggio, ma il loro significato nasce dal contesto in cui vengono usati. Proprio come in una lingua naturale, il vocabolario mescola termini “ufficiali” e parole inventate sul momento, purché rispettino le regole di formazione. È a questo livello che il codice inizia davvero a dire qualcosa, andando oltre i semplici simboli.

#### 3. **Sintassi**

La sintassi è l'insieme di regole che determinano come gli elementi del linguaggio (alfabeto e lessico) possono essere combinati per formare costrutti validi. È il "grammatica" del linguaggio di programmazione. La sintassi specifica, ad esempio, che una istruzione `if` deve essere seguita da una condizione e poi da un colon, e che il blocco di codice deve essere indentato.

Nel linguaggio naturale italiano, la sintassi specifica che un'affermazione semplice dovrebbe avere un soggetto, un verbo e un oggetto, in un ordine particolare: "Il gatto mangia il pesce" è sintatticamente corretto, mentre "Mangia il gatto pesce il" non lo è.

```python
# Sintassi corretta di Python
if numero > 10:
    print("Il numero è grande")

# Sintassi errata (mancherebbe il colon)
if numero > 10
    print("Errore!")
```

Nel primo esempio, la riga `if numero > 10:` rispetta perfettamente la sintassi di Python: la parola chiave `if` introduce la condizione, la variabile `numero` fa parte del vocabolario, il simbolo `>` indica un confronto, e i due punti `:` segnalano l’inizio del blocco di istruzioni. Tutto è al posto giusto, quindi il codice viene eseguito senza problemi. Nel secondo esempio, invece, manca il `:`: la sintassi è violata e Python non capisce cosa deve fare, generando un errore. Proprio come in una lingua naturale, anche in Python non basta avere le parole giuste: devono essere messe nell’ordine corretto e con i segni di punteggiatura appropriati, altrimenti la comunicazione si interrompe.

#### 4. **Semantica**

La semantica è il significato. È il concetto che sta dietro i simboli e alle strutture syntattiche. Un'affermazione può essere sintatticamente corretta ma semanticamente priva di senso.

Nel linguaggio naturale: "Il cemento dorme profondamente" è sintatticamente corretto in italiano, ma è semanticamente privo di senso (il cemento non può dormire).

In programmazione:

```python
# Sintatticamente corretto, ma semanticamente problematico
risultato = "ciao" + 5
# Python non sa come aggiungere una stringa a un numero
# Questo produrrà un errore di tipo
```

Oppure, più sottilmente:

```python
# Sintatticamente e formalmente corretto,
# ma semanticamente illogico per il vostro scopo
eta_persona = -25  # Quanti anni vuol dire un'età negativa?
```

Un’istruzione può essere formalmente giusta e rispettare tutte le regole del linguaggio, ma avere comunque un senso logico sbagliato. Ad esempio, `risultato = "ciao" + 5` è sintatticamente corretto perché Python sa riconoscere le parole e i simboli, ma semanticamente è problematico: non ha senso aggiungere una stringa a un numero, quindi il programma genera un errore di tipo. Allo stesso modo, assegnare un valore negativo a una variabile chiamata `eta_persona` è sintatticamente corretto, ma semanticamente illogico: cosa significa avere un’età di -25 anni? La semantica, insomma, è ciò che trasforma il codice da una sequenza di simboli e parole in un messaggio coerente e interpretabile, proprio come nella lingua naturale.

### 1.1.4 Linguaggio Macchina vs. Linguaggi di Alto Livello

Se volessimo comunicare direttamente con il computer utilizzando il suo linguaggio nativo—il linguaggio macchina—dovremmo imparare la lista di istruzioni della macchina e scrivere ogni comando come una sequenza di numeri binari o esadecimali. Questo era esattamente come funzionava la programmazione nei primi giorni dell'informatica:

```
10110000 01100001  (un'istruzione semplice in linguaggio macchina)
```

Non è neanche necessario sottolineare che questo approccio è estremamente difficile e soggetto a errori. È come se doveste comunicare ogni vostro pensiero utilizzando solamente i codici morse. È tecnicamente possibile, ma è straordinariamente impraticabile.

Per risolvere questo problema, gli scienziati informatici hanno creato **linguaggi di programmazione di alto livello**. Questi linguaggi sono molto più vicini al linguaggio naturale umano rispetto al linguaggio macchina, anche se comunque molto più rigorosi e precisi del linguaggio naturale.

Il compito di tradurre codice scritto in un linguaggio di alto livello in linguaggio macchina spetta a un programma speciale chiamato **compilatore** o **interprete**. Un compilatore traduce l'intero programma in una volta prima dell'esecuzione. Un interprete, invece, traduce il programma riga per riga durante l'esecuzione.

Python è un linguaggio interpretato, il che significa che il codice Python viene tradotto e eseguito riga per riga dall'interprete Python mentre il programma è in esecuzione.

## Parte 3: Python — Il Linguaggio del Presente

### 1.2.1 Come è Nato Python

Python fu creato da Guido van Rossum, uno scienziato informatico olandese, alla fine del 1989. Van Rossum iniziò il lavoro su Python come progetto hobby durante le vacanze di Natale, ispirato da un linguaggio precedente di nome ABC. L'intenzione era di creare un linguaggio che fosse:

- Facile da imparare e da insegnare
- Potente quanto i linguaggi concorrenti
- Open source, così che chiunque potesse contribuire al suo sviluppo
- Codice leggibile come l'inglese semplice
- Adatto a compiti quotidiani, permettendo tempi di sviluppo brevi

Circa 35 anni dopo la sua creazione, è chiaro che tutte queste intenzioni sono state pienamente realizzate. Secondo molte fonti, Python è il linguaggio di programmazione più popolare al mondo, sebbene altre fonti lo collochino al secondo o terzo posto.

In ogni caso, occupa ancora un posto di rilievo nei primi dieci del PYPL (PopularitY of Programming Language) e dell'indice TIOBE della Comunità di Programmazione.

Python non è più un linguaggio giovane. È maturo e affidabile. Non è una meraviglia effimera. È una stella brillante nel firmamento della programmazione, e il tempo dedicato all'apprendimento di Python è un investimento molto valido.

### 1.2.4 Cosa Rende Python Così Speciale?

Come accade che programmatori, giovani e anziani, esperti e principianti, vogliano usarlo? Come è successo che grandi aziende abbiano adottato Python e implementato i loro prodotti di punta utilizzandolo?

Ci sono molte ragioni. Alcune che abbiamo già menzionato, ma enuchiamole di nuovo in modo più pratico:

**È facile da imparare.** Il tempo necessario per imparare Python è più breve rispetto a molti altri linguaggi. Questo significa che è possibile iniziare la programmazione vera e propria più velocemente. Un nuovo programmatore può afferrare i concetti fondamentali di Python in poche settimane, mentre linguaggi come C++ potrebbero richiedere mesi.

**È facile da insegnare.** Il carico di lavoro didattico è minore rispetto a quello necessario per altri linguaggi. Questo significa che gli insegnanti possono concentrare più attenzione sulle tecniche di programmazione generali, indipendenti dal linguaggio, piuttosto che sprecare energie su trucchi esotici, eccezioni strane e regole incomprensibili.

**È facile da usare per scrivere nuovo software.** È spesso possibile scrivere il codice più velocemente con Python. Quello che richiederebbe cinquanta righe di C potrebbe richiederne solo dieci di Python.

**È facile da capire.** È spesso più facile comprendere rapidamente il codice di qualcun altro se è scritto in Python. La sintassi è pulita e intuitiva, e la leggibilità è una priorità del linguaggio.

**È facile da ottenere, installare e distribuire.** Python è gratuito, open source e multipiattaforma. Non tutti i linguaggi possono vantare queste caratteristiche. Potete scaricare Python, installarlo su praticamente qualsiasi computer moderno (Windows, macOS, Linux, Raspberry Pi, ecc.) e iniziare a programmare immediatamente, senza costi aggiuntivi.

### 1.2.5 I Rivali di Python

Python ha due concorrenti diretti con proprietà e predisposizioni comparabili:

**Perl** – Un linguaggio di scripting originariamente creato da Larry Wall nel 1987. Perl è un linguaggio estremamente potente e flessibile, ma è conosciuto per la sua sintassi complessa. Il motto non ufficiale di Perl è "C'è più di una via per fare qualcosa" (There's More Than One Way To Do It, TMTOWTDI), il che riflette la sua filosofia di massima flessibilità. Perl è tradizionale e conservatore, assomigliando a linguaggi più vecchi derivati da C.

**Ruby** – Un linguaggio di scripting creato da Yukihiro Matsumoto in Giappone negli anni '90. Ruby è progettato per massimizzare la felicità del programmatore. È più innovativo e pieno di idee fresche rispetto a Python, ma talvolta questa innovazione lo rende meno stabile e prevedibile.

Python si trova da qualche parte tra questi due. È meno conservatore di Perl ma meno radicale di Ruby. È un equilibrio intelligente tra potenza e semplicità, tra flessibilità e chiarezza.

Internet è piena di forum con discussioni infinite sulla superiorità di uno di questi tre rispetto agli altri. Se volete approfondire ulteriormente le differenze, quei forum sono il posto giusto.

### 1.2.6 Python in Azione: Dove lo Vediamo Oggi

Vediamo Python ogni giorno, quasi ovunque. È utilizzato estesamente per implementare servizi Internet complessi come motori di ricerca, strumenti di archiviazione nel cloud, social media e così via. Ogni volta che usate uno di questi servizi, siete effettivamente molto vicini a Python, sebbene non lo saprete.

Molti strumenti di sviluppo sono implementati in Python. Sempre più applicazioni di uso quotidiano vengono scritte in Python. Molti scienziati hanno abbandonato costosi strumenti proprietari e sono passati a Python. Molti tester di progetti IT hanno iniziato a usare Python per eseguire procedure di test ripetibili. L'elenco è lungo.

Tra le applicazioni specifiche:

- **Data Science e Machine Learning:** Python è il linguaggio dominante nella ricerca in intelligenza artificiale e apprendimento automatico. Librerie come NumPy, Pandas e TensorFlow sono scritte in Python.
- **Sviluppo Web:** Framework web come Django e Flask sono costruiti su Python.
- **Automazione e Scripting:** I sistema administrators usano Python per automatizzare compiti ripetitivi.
- **Analisi Scientifica:** Ricercatori in biologia, fisica, chimica e altre discipline usano Python per analizzare dati.
- **Game Development:** Anche l'industria dei videogiochi usa Python per scripting e development.

### 1.2.7 Perché Non Python?

Nonostante la crescente popolarità di Python, ci sono ancora alcune nicchie dove Python è assente o raramente visto:

**Programmazione a basso livello.** Se volete implementare un driver estremamente efficiente o un motore grafico, non usereste Python. I compiti critici per le prestazioni a livello hardware richiedono linguaggi compilati come C o C++ che generano codice machine estremamente ottimizzato.

**Applicazioni per dispositivi mobili.** Sebbene questo territorio stia ancora aspettando di essere conquistato da Python, è molto probabile che accadrà un giorno. Attualmente, gli standard di facto per lo sviluppo mobile sono Java/Kotlin (Android) e Swift/Objective-C (iOS), ma Python sta guadagnando terreno anche in questo spazio.

**Embedded Systems con risorse molto limitate.** Su microcontroller con memoria estremamente limitata, Python potrebbe non essere pratico. In questi casi, si preferiscono linguaggi più leggeri come C.

### 1.2.8 Esiste Più di Un Python: Python 2 vs. Python 3

Ci sono due versioni principali di Python, chiamate **Python 2** e **Python 3**.

**Python 2** è la versione più vecchia del Python originale. Il suo sviluppo è stato intenzionalmente fermato, anche se questo non significa che non riceva aggiornamenti. Al contrario, gli aggiornamenti vengono rilasciati regolarmente, ma non sono intesi a modificare il linguaggio in modo significativo. Piuttosto, risolvono bug e vulnerabilità di sicurezza appena scoperti.

Il percorso di sviluppo di Python 2 ha raggiunto un punto morto, ma Python 2 stesso è ancora molto vivo. Milioni di linee di codice Python 2 sono ancora in produzione in aziende di tutto il mondo.

**Python 3** è la versione più recente (o più precisamente, quella attuale) del linguaggio. Sta percorrendo il suo proprio percorso evolutivo, creando i suoi standard e le sue abitudini.

Queste due versioni di Python **non sono compatibili tra loro**. Gli script Python 2 non funzioneranno in un ambiente Python 3 e viceversa. Se volete che il vecchio codice Python 2 funzioni con un interprete Python 3, l'unica soluzione possibile è riscriverlo.

Non serve riscrivere da zero, naturalmente, poiché gran parte del codice può rimanere inalterata, ma dovete comunque revisionare tutto il codice per trovare tutte le possibili incompatibilità.

Purtroppo, questo processo non può essere completamente automatizzato. È troppo difficile, troppo dispendioso in termini di tempo, troppo costoso e troppo rischioso migrare un'antica applicazione Python 2 a una nuova piattaforma. È persino possibile che riscrivere il codice introduca nuovi bug. È più facile e più sensato lasciare questi sistemi in pace e migliorare l'interprete esistente, piuttosto che cercare di lavorare all'interno del codice sorgente già funzionante.

**Python 3 non è solo una versione migliore di Python 2.** È un linguaggio completamente diverso, sebbene molto simile al suo predecessore. Quando li guardate da lontano, sembrano uguali. Ma quando guardate da vicino, notate molte differenze. Queste differenze non sono banali.

Se state modificando una soluzione Python esistente e già affermata, è altamente probabile che sia stata codificata in Python 2. Questa è la ragione per cui Python 2 è ancora in uso. Ci sono troppi programmi Python 2 già esistenti per scartarli completamente.

**Nota importante:** Se state per avviare un nuovo progetto Python, dovete usare Python 3. Questa è la versione di Python che sarà utilizzata durante questo corso, e l'unica versione con un futuro di lungo termine.

È importante ricordare che potrebbe esserci variabilità tra le versioni successive di Python 3 (ad esempio, Python 3.6 ha introdotto la garanzia che le chiavi del dizionario fossero ordinate per impostazione predefinita, ossia ora i dizionari ricordano sempre l'ordine con cui hai inserito le informazioni). La buona notizia, tuttavia, è che tutte le versioni più recenti di Python 3 sono retrocompatibili con le versioni precedenti di Python 3.

### 1.2.9 Implementazioni di Python: Cosa Significa?

Abbiamo detto che esistono "Python 2" e "Python 3". Ma c'è ancora un altro livello di complessità: esiste più di un modo di far funzionare Python.

Che cosa intendiamo per "implementazione"? Pensiamo a un'analogia. Supponiamo che le regole del calcio siano come il "linguaggio Python": sono le regole ufficiali su come si gioca. Ma il calcio viene giocato ovunque nel mondo: negli stadi professionisti italiani, negli stadi americani, in piccoli campi amatoriali del Brasile. Tutti seguono le stesse regole (più o meno), ma il modo di giocare (lo stadio, l'attrezzatura, le persone che lo organizzano) è diverso.

Allo stesso modo, Python è il "linguaggio ufficiale": le regole di come scrivere codice Python. Ma questo codice può essere eseguito in modi diversi. Ogni modo diverso di far eseguire il vostro codice Python si chiama **implementazione**.

Una **implementazione di Python** è essenzialmente un **programma che legge il vostro codice Python e lo fa funzionare**. È come un traduttore: voi scrivete in Python, il programma dell'implementazione lo traduce e lo esegue sul vostro computer.

### L'Implementazione Tradizionale: CPython

La più comune (e quella che userete) si chiama **CPython**. Il nome è strano, ma è semplice da capire.

**C** = il linguaggio C (un linguaggio di programmazione molto antico e veloce)  
**Python** = il nostro linguaggio

**CPython** significa: "Un interprete Python scritto nel linguaggio C".

Guido van Rossum, il creatore di Python, ha scritto il primo interprete Python usando il linguaggio C. Non lo ha scritto in Python (sarebbe un'auto-referenza!), ma in C. Quando digitate `python` nel terminale e il vostro codice viene eseguito, state usando CPython. Questo è il Python "ufficiale" mantenuto dalla PSF (Python Software Foundation), l'organizzazione che controlla Python.

Perché scriverlo in C? Semplice: C è un linguaggio vecchio e molto compreso. Viene eseguito su praticamente ogni computer moderno—Windows, macOS, Linux, Raspberry Pi, persino telefoni. Scrivere CPython in C ha significato che Python poteva funzionare ovunque. È stato una scelta astuta.

**In pratica:** Quando scaricate Python da python.org e lo installate, state installando CPython. È il Python "di default". Per il vostro corso, CPython è quello che userete.

### Altre Implementazioni Notevoli di Python: Quando Servono Cose Diverse

Oltre a CPython, ci sono altre implementazioni di Python che sono state create per scopi specifici. Non le userete nel vostro corso, ma è utile sapere che esistono.

**PyPy** – Immaginate di voler eseguire un programma Python, ma **molto più velocemente**. PyPy è un'implementazione di Python che è stata progettata per essere più veloce di CPython. Come fa? Usa una tecnica chiamata "compilazione JIT" (Just-In-Time): analizza il vostro codice mentre viene eseguito e lo ottimizza al volo. Per programmi che ripetono lo stesso codice molte volte (loop intensivi), PyPy può essere **10-100 volte più veloce** di CPython. Ma per programmi semplici, non fa molta differenza. Usate PyPy quando la velocità è davvero critica.

**Jython** – A volte le aziende usano il linguaggio Java (completamente diverso da Python). Jython è Python che funziona dentro l'ecosistema Java. Cosa significa? Significa che potete scrivere codice Python e usare le librerie Java direttamente. È utile se lavorate in un'azienda dove Java è già ovunque e volete i vantaggi di Python senza abbandonare Java.

**IronPython** – Simile a Jython, ma per la piattaforma Microsoft .NET. Se lavorate in un'azienda che usa solamente strumenti Microsoft, IronPython vi permette di scrivere Python che funziona con C# e altri linguaggi .NET.

**MicroPython** – Supponiamo che vogliate programmmare un microcontroller (un piccolissimo computer che controlla un robot, una lampadina intelligente, ecc.). I microcontroller hanno pochissima memoria, quindi non potete installarvi CPython intero. MicroPython è una versione **molto più piccola** di Python, disegnata appositamente per questi dispositivi minuscoli. È quello che usate se programmate una BBC Micro:bit o un piccolo sensore IoT.

**La cosa importante da sapere:** Per il vostro corso e per la stragrande maggioranza dei vostri programmi futuri, userete **CPython**. Quando scaricate Python da python.org, state scaricando CPython. È il "Python standard". Le altre implementazioni esistono per casi speciali—quando avete bisogno di velocità estrema, quando volete usare librerie Java, quando programmate microcontroller, ecc.

**Non vi preoccupate di queste altre implementazioni per ora.** Imparate Python usando CPython, e quando (se) vi troverete in una situazione dove un'altra implementazione serve, saprete che esiste.

### 1.2.10 Strumenti Essenziali: Editor, Console e Debugger

Per scrivere ed eseguire programmi Python, avete bisogno di alcuni strumenti essenziali:

#### L'Editor di Testo

Un **editor di testo** è il software che usate per scrivere il codice Python. Non è un word processor come Microsoft Word (che aggiunge formattazione e molto altro). È un semplice editor che permette di digitare il testo puro.

Esempi di editor di testo includono:

- **VS Code (Visual Studio Code)** – L'editor di testo moderno più popolare. È gratuito, leggero, estensibile con plugin, e ha ottimo supporto per Python. È la scelta consigliata per questo corso.
- **PyCharm** – Un IDE (Integrated Development Environment) professionale per Python. Ha più funzionalità di un semplice editor, inclusi debugger avanzati e strumenti di refactoring. Disponibile in una versione community gratuita.
- **Sublime Text** – Un editor leggerissimo e veloce, molto amato dai programmatori.
- **Vim/Neovim** – Editor potentissimo ma con una curva di apprendimento ripida.
- **IDLE** – L'editor semplice che viene fornito con Python. È minimalista ma sufficiente per iniziare.

#### La Console (Il Terminale/Interprete Interattivo)

La **console** è un'interfaccia testuale in cui potete digitare comandi e ricevere output immediato. In Python, il termine "console" può riferirsi a:

- **Il Prompt dei Comandi (Command Prompt) su Windows** o il **Terminale su macOS/Linux** – La console del sistema operativo
- **L'Interprete Interattivo di Python** – Un programma speciale che esegue immediatamente il codice Python riga per riga

Quando avviate l'interprete interattivo di Python (generalmente digitando `python` o `python3` nel terminale), vedete il prompt `>>>`:

```
Python 3.10.2 (main, Feb  4 2022, 17:14:38) [GCC 10.2.1]
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

A questo punto, potete digitare codice Python, e viene eseguito immediatamente:

```python
>>> print("Ciao, mondo!")
Ciao, mondo!
>>> numero = 42
>>> numero * 2
84
>>>
```

L'interprete interattivo è fantastico per sperimentare e imparare Python, perché ricevete feedback immediato. È come avere una calcolatrice intelligente che comprende Python.

#### Il Debugger

Un **debugger** è uno strumento che vi aiuta a trovare e correggere gli errori ("bug") nei vostri programmi. Quando eseguite un programma in modalità debug, potete:

- Eseguire il programma riga per riga
- Ispezionare i valori delle variabili in qualsiasi punto
- Impostare punti di interruzione (breakpoint) per pausare l'esecuzione in punti specifici
- Continuare l'esecuzione fino al prossimo breakpoint
- Valutare espressioni per vedere come si comporterebbero

VS Code ha un debugger integrato per Python. PyCharm ha un debugger ancora più avanzato. Imparare a usare un debugger è una competenza cruciale per un programmatore perché vi farà risparmiare ore di lavoro quando cercate di capire perché il vostro programma non funziona come previsto.

Ecco un esempio di sessione di debug:

```python
# Nel vostro programma
numero = 10
risultato = numero * 2

# Impostate un breakpoint all'ultima riga
# Quando il debugger raggiunge quel punto, si ferma e potete ispezionare:
# numero = 10
# risultato = 20
```

## Conclusione: Fondamenti e Prospettive

Abbiamo iniziato questo capitolo con una domanda fondamentale: come funziona un programma per computer? E abbiamo scoperto che la risposta è affascinantemente semplice. Un computer non è intelligente. Non è un pensatore. È uno strumento meravigliosamente efficiente che può eseguire operazioni banali con velocità inimmaginabile.

È questa semplicità, tuttavia, che genera la possibilità. Perché, come abbiamo visto, dalla combinazione intelligente di miliardi di operazioni semplici emerge la complessità.

Abbiamo poi esaminato il ruolo cruciale del linguaggio. Un linguaggio di programmazione è il ponte tra il nostro modo di pensare (logico, concettuale, talvolta vago) e il modo in cui il computer opera (binario, preciso, letterale). Senza il linguaggio, saremmo costretti a comunicare con il computer a livello di singoli bit e istruzioni di macchina. Con il linguaggio, possiamo esprimere idee complesse in modo relativamente leggibile e mantenibile.

Python emerge come una scelta eccezionale in questo panorama. Non è il linguaggio più veloce, non è il più vicino al hardware, non è il più potente in senso assoluto. Quello che Python offre è un equilibrio raro: è facile da imparare, leggibile, potente per una straordinaria varietà di compiti, e circondata da una comunità vivace e accogliente.

Quando iniziate a imparare la programmazione, state intraprendendo un percorso che vi insegnerà a pensare in modo diverso. Vi insegnerà a scomporre problemi complessi in sotto-problemi più semplici. Vi insegnerà a essere precisi e a prestare attenzione ai dettagli. Vi insegnerà che spesso la soluzione più elegante non è sempre la più ovvia.

Negli ultimi decenni, la programmazione è passata da un'attività di nicchia per esperti a una competenza fondamentale. Nel 21° secolo, comprendere come funziona il codice (come pensano i computer) è diventato una forma di alfabetismo. Non è necessario diventare un professionista della programmazione. Ma capire i principi di base farà una differenza reale nel vostro modo di pensare e di affrontare i problemi.

Python sarà il vostro compagno in questo viaggio. Nei capitoli che seguono, costruiremo su questi fondamenti. Impareremo come dare istruzioni specifiche al computer, come memorizzare e manipolare i dati, come prendere decisioni sulla base delle condizioni, come ripetere azioni, e come organizzare il codice in strutture significative.

Ma tutto comincia qui, con la comprensione di questo fatto semplice ma profondo: che un computer è uno strumento, e come qualsiasi strumento, la sua utilità dipende completamente da chi lo sa usare. Voi state per imparare a usarlo.

Il vostro viaggio nella programmazione è appena iniziato.