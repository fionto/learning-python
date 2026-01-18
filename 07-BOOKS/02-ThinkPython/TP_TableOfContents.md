# Parte I – Programmare come forma di pensiero

## Capitolo 1 – Programmare come modo di pensare

Questo capitolo introduce la programmazione come attività concettuale prima ancora che tecnica. Vengono presentati gli operatori aritmetici, le espressioni e le funzioni matematiche di base, insieme all’uso delle stringhe e alla distinzione tra valori e tipi. Il capitolo riflette anche sulla differenza tra linguaggi formali e linguaggi naturali, mostrando come la programmazione richieda precisione e rigore. Ampio spazio è dedicato al debugging come pratica fondamentale per comprendere il comportamento del codice e sviluppare un approccio analitico alla risoluzione dei problemi.

---

## Capitolo 2 – Variabili e istruzioni

Questo capitolo approfondisce il concetto di variabile come strumento per rappresentare lo stato di un programma. Vengono introdotti i diagrammi di stato per visualizzare l’evoluzione delle variabili nel tempo, insieme alle regole per la scelta dei nomi. Il capitolo chiarisce la differenza tra espressioni e istruzioni, presenta l’uso dell’istruzione `import`, della funzione `print` e degli argomenti, e introduce i commenti come supporto alla leggibilità del codice. Il debugging viene ripreso come strumento essenziale per interpretare il comportamento dei programmi.

---

## Capitolo 3 – Funzioni

In questo capitolo le funzioni vengono presentate come meccanismo centrale per strutturare il codice. Si analizza come definire nuove funzioni, come utilizzare parametri e come invocare correttamente una funzione. Il capitolo affronta il concetto di ripetizione, la località di variabili e parametri e introduce i diagrammi di stack per comprendere il flusso di esecuzione. Vengono inoltre spiegati i traceback come strumenti diagnostici e si riflette sul perché le funzioni siano fondamentali per la chiarezza, il riuso e la manutenibilità del codice.

---

## Capitolo 4 – Funzioni e interfacce

Questo capitolo esplora il rapporto tra funzioni e interfacce, utilizzando esempi grafici per mostrare come il codice possa interagire con moduli esterni. Vengono introdotti concetti come incapsulamento e generalizzazione, mostrando come migliorare progressivamente il codice attraverso il refactoring. Il capitolo propone un approccio metodico allo sviluppo, includendo la pianificazione dello sviluppo e l’uso delle docstring per documentare le funzioni. I diagrammi di stack vengono ripresi per consolidare la comprensione dell’esecuzione del programma.

---

## Capitolo 5 – Condizionali e ricorsione

In questo capitolo viene introdotta la logica decisionale nei programmi. Si parte dalla divisione intera e dall’operatore modulo, per arrivare alle espressioni booleane e agli operatori logici. Il capitolo analizza le istruzioni `if`, le clausole `else` e le diverse forme di condizionali concatenati e annidati. Una parte centrale è dedicata alla ricorsione, spiegandone il funzionamento attraverso diagrammi di stack, i rischi della ricorsione infinita e il confronto con input forniti dall’utente. Il debugging accompagna l’intero capitolo come strumento di comprensione.

---

## Capitolo 6 – Valori di ritorno

Questo capitolo approfondisce il concetto di valore di ritorno delle funzioni. Viene spiegata la differenza tra funzioni che restituiscono un valore e funzioni che non restituiscono nulla, e come i valori di ritorno interagiscono con le strutture condizionali. Il capitolo introduce lo sviluppo incrementale come strategia per costruire funzioni complesse e presenta le funzioni booleane e la ricorsione con valori di ritorno. Attraverso esempi come la sequenza di Fibonacci, si introduce il concetto di “salto di fede” nella progettazione ricorsiva e il controllo dei tipi come supporto alla correttezza del codice.

---

## Capitolo 7 – Iterazione e ricerca

Questo capitolo si concentra sull’iterazione come alternativa e complemento alla ricorsione. Viene mostrato come iterare su stringhe, aggiornare variabili all’interno dei cicli e utilizzare contatori. Il capitolo introduce l’operatore `in` e le tecniche di ricerca, mostrando come individuare elementi all’interno di sequenze. Viene inoltre presentato `doctest` come strumento per integrare test direttamente nella documentazione del codice, rafforzando il legame tra specifica e implementazione.

---

## Capitolo 8 – Stringhe ed espressioni regolari

In questo capitolo le stringhe vengono analizzate come sequenze di caratteri. Si affrontano slicing, immutabilità, confronto tra stringhe e metodi integrati. Il capitolo introduce la scrittura su file e le operazioni di ricerca e sostituzione del testo. Una parte significativa è dedicata alle espressioni regolari, mostrandone l’uso per il riconoscimento e la trasformazione di pattern testuali. Il debugging accompagna l’esplorazione di questi strumenti, spesso soggetti a errori sottili.

---

## Capitolo 9 – Liste

Questo capitolo introduce le liste come strutture dati mutabili e sequenziali. Vengono analizzate le operazioni fondamentali, lo slicing, i metodi delle liste e il rapporto tra liste e stringhe. Il capitolo esplora l’iterazione sulle liste, l’ordinamento e la distinzione tra oggetti e valori, introducendo concetti come aliasing e passaggio di liste come argomenti. Attraverso esempi pratici, viene mostrato come costruire e manipolare collezioni di dati in modo efficace.

---

## Capitolo 10 – Dizionari

In questo capitolo i dizionari vengono presentati come strutture di mappatura tra chiavi e valori. Si affrontano la creazione dei dizionari, l’uso dell’operatore `in` e le tecniche per accumulare e contare informazioni. Il capitolo esplora l’iterazione sui dizionari, l’integrazione con le liste e l’uso dei memo per ottimizzare le prestazioni. Il debugging viene nuovamente utilizzato per chiarire il comportamento di strutture dati più complesse.

---

## Capitolo 11 – Tuple

Questo capitolo introduce le tuple come strutture simili alle liste ma immutabili. Vengono spiegate l’assegnazione multipla, l’uso delle tuple come valori di ritorno e il packing degli argomenti. Il capitolo presenta la funzione `zip`, le tecniche di confronto e ordinamento e l’inversione dei dizionari. Le tuple vengono mostrate come strumento essenziale per rappresentare dati strutturati in modo sicuro ed efficiente.

---

## Capitolo 12 – Analisi e generazione del testo

Questo capitolo applica le strutture dati e le tecniche viste in precedenza all’analisi del testo. Si affrontano la gestione delle parole uniche, della punteggiatura e delle frequenze, introducendo parametri opzionali e operazioni tra dizionari. Il capitolo esplora l’uso dei numeri casuali, dei bigrammi e dell’analisi di Markov per generare testo, mostrando come semplici regole possano produrre risultati complessi e sorprendenti.

---

## Capitolo 13 – File e database

In questo capitolo viene approfondita la gestione persistente dei dati. Si analizzano nomi di file e percorsi, l’uso delle f-string, e formati di archiviazione come YAML e `shelve`. Il capitolo mostra come memorizzare strutture dati complesse, confrontare file e attraversare directory. L’attenzione è posta sulla robustezza del codice e sulla capacità di lavorare con grandi quantità di dati in modo affidabile.

---

## Capitolo 14 – Classi e funzioni

Questo capitolo introduce i tipi definiti dal programmatore e il loro rapporto con le funzioni. Vengono presentati attributi, oggetti come valori di ritorno e la mutabilità degli oggetti. Il capitolo esplora le tecniche di copia, la distinzione tra funzioni pure e impure e l’approccio “prototype and patch” allo sviluppo. Viene infine introdotta la progettazione orientata al design come metodo per strutturare programmi complessi.

---

## Capitolo 15 – Classi e metodi

In questo capitolo l’attenzione si sposta sui metodi come funzioni associate agli oggetti. Vengono spiegati i metodi statici, il confronto tra oggetti, e l’uso di metodi speciali come `__str__()` e `__init__()`. Il capitolo introduce il concetto di overloading degli operatori e mostra come definire comportamenti personalizzati per le classi, migliorando l’espressività del codice.

---

## Capitolo 16 – Classi e oggetti

Questo capitolo approfondisce la modellazione di oggetti complessi. Attraverso esempi geometrici, vengono esplorati concetti come equivalenza e identità, modifica degli oggetti, copia profonda e polimorfismo. Il capitolo mostra come progettare oggetti che collaborano tra loro e come gestire correttamente il loro stato nel tempo.

---

## Capitolo 17 – Ereditarietà

In questo capitolo viene introdotta l’ereditarietà come meccanismo per riutilizzare e specializzare il codice. Attraverso l’esempio delle carte da gioco, si analizzano attributi, metodi, confronto tra oggetti e gestione di collezioni complesse come i mazzi. Il capitolo distingue tra classi genitore e figlio e introduce il concetto di specializzazione come strumento di progettazione.

---

## Capitolo 18 – Estensioni di Python

Questo capitolo presenta una selezione di funzionalità avanzate del linguaggio. Vengono introdotti set, contatori, `defaultdict`, espressioni condizionali e list comprehension. Il capitolo esplora funzioni come `any` e `all`, le named tuple e il packing degli argomenti keyword, mostrando come questi strumenti possano rendere il codice più compatto, espressivo ed efficiente.

---

## Capitolo 19 – Considerazioni finali

Il capitolo conclusivo offre una riflessione complessiva sul percorso affrontato, collegando i concetti di programmazione, progettazione e pensiero computazionale. Più che introdurre nuovi strumenti, invita a consolidare un approccio critico e consapevole alla scrittura del codice, sottolineando l’importanza della chiarezza, della semplicità e della pratica continua.