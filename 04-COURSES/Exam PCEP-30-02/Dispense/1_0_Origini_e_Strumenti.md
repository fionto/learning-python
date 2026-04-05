# Sezione Bonus: Python — Origini, Evoluzione e Strumenti del Mestiere

## Introduzione: prima di scrivere la prima riga

Prima di imparare a programmare in Python, vale la pena fermarsi un momento e chiedersi: *da dove viene* questo linguaggio? Perché esistono una versione 2 e una versione 3? E quando qualcuno dice "Python" intende sempre la stessa cosa?

Queste domande non fanno parte del syllabus PCEP vero e proprio, ma rispondere aiuta a orientarsi nel panorama reale: capire la storia di uno strumento significa capire le scelte che lo hanno plasmato, e capire le scelte significa fare meno errori quando si inizia a usarlo sul serio. Pensate a come conoscere la storia di un quartiere vi aiuta a capire la disposizione delle strade: non è strettamente necessario per camminare, ma rende tutto più sensato.

---

## Come è Nato Python

Alla fine degli anni Ottanta, un informatico olandese di nome **Guido van Rossum** lavorava al Centrum Wiskunde & Informatica di Amsterdam. Il suo obiettivo non era rivoluzionario, almeno in apparenza: voleva un linguaggio di scripting che fosse più potente di Bash ma più semplice del C, qualcosa con cui fare prototipazione veloce senza perdere ore in dettagli di bassa sintassi.

Van Rossum iniziò a scrivere il primo interprete Python nel **dicembre 1989**, durante le vacanze di Natale, quasi come progetto personale. Il nome non viene dal rettile: Guido era un fan del gruppo comico britannico **Monty Python's Flying Circus** e scelse quel nome per alleggerire il tono del progetto. La scelta ha avuto conseguenze durature: ancora oggi la documentazione ufficiale abbonda di riferimenti agli sketch del gruppo, e il termine canonico per un esempio di codice è "spam" o "eggs" invece del più anonimo "foo" o "bar".

La **prima versione pubblica (Python 0.9.0)** uscì nel **febbraio 1991** su un newsgroup Usenet. Conteneva già alcune delle idee che rendono Python riconoscibile ancora oggi: l'indentazione obbligatoria come struttura del codice, le eccezioni, le funzioni come oggetti di prima classe. La versione **1.0** arrivò nel 1994, seguita dalla **2.0** nel 2000 con la Python Software Foundation a gestire lo sviluppo, e infine dalla **3.0** nel 2008.

Per oltre vent'anni van Rossum ha ricoperto il ruolo di **Benevolent Dictator For Life** (BDFL): una figura di autorità finale sulle decisioni progettuali del linguaggio, con il potere di approvare o rigettare qualsiasi proposta di modifica. Nel luglio 2018 ha annunciato il ritiro da quel ruolo; da allora Python è governato da un **Steering Council** eletto dalla comunità dei core developer.

L'eredità culturale più importante di Van Rossum è forse il **The Zen of Python**: una raccolta di diciannove aforismi che descrivono la filosofia del linguaggio. Si possono leggere direttamente nell'interprete Python digitando `import this`. Il primo aforisma è emblematico: *Beautiful is better than ugly* (il bello è meglio del brutto). Non è un capriccio estetico: è un manifesto che spiega perché Python privilegia la leggibilità rispetto alla concisione criptica.

---

## Python 2 vs. Python 3

Poche cose generano più confusione nei nuovi programmatori della coesistenza storica di due versioni incompatibili dello stesso linguaggio. Vale la pena capire cosa è successo.

Nel 2008 fu rilasciato **Python 3.0**, noto anche come "Python 3000" o "Py3K". L'obiettivo era risolvere alcune incongruenze di fondo accumulate nel corso degli anni: la gestione delle stringhe Unicode era tortuosa, alcune funzioni restituivano liste dove avrebbe avuto più senso restituire iteratori, la divisione intera tra numeri interi dava risultati controintuitivi. Tutte correzioni sensate, ma incompatibili con il codice esistente. Python 3 **non è retrocompatibile** con Python 2: un programma scritto per Python 2 non funziona necessariamente in Python 3 senza modifiche.

Questo creò una frattura nella comunità. Le grandi librerie scientifiche (NumPy, SciPy, Django e così via) avevano milioni di righe di codice scritte per Python 2; migrarle tutte richiedeva tempo, risorse, e la volontà delle organizzazioni che le mantenevano. Per anni le due versioni hanno coesistito, con i nuovi sviluppatori che si trovavano di fronte alla domanda scomoda: quale versione imparare?

La risposta oggi è semplice e definitiva: **Python 2 è morto**. Il 1° gennaio 2020 è terminato il supporto ufficiale per Python 2.7 (l'ultima versione della serie): nessuna patch di sicurezza, nessuna correzione di bug, nessun aggiornamento di qualsiasi tipo. Tutto l'ecosistema delle librerie importanti ha completato la migrazione. Se oggi iniziate a programmare in Python, imparate Python 3: non c'è ragione pratica di fare altrimenti.

Per chi è curioso, ecco le differenze più visibili tra le due versioni:

| Aspetto | Python 2 | Python 3 |
|---|---|---|
| Stampa a schermo | `print "ciao"` (istruzione) | `print("ciao")` (funzione) |
| Divisione intera | `7 / 2` restituisce `3` | `7 / 2` restituisce `3.5` |
| Stringhe Unicode | opt-in con prefisso `u"..."` | predefinito |
| `input()` vs `raw_input()` | `input()` valutava l'espressione | solo `input()`, sicuro |
| Fine supporto | 1° gennaio 2020 | attivo e in sviluppo |

A partire dalla versione **3.10** (ottobre 2021) Python ha introdotto i *match statement* (simili allo switch/case di altri linguaggi); la **3.12** ha portato miglioramenti significativi alle performance; la **3.13**, rilasciata nell'ottobre 2024, ha iniziato a includere un interprete sperimentale senza il GIL (Global Interpreter Lock), aprendo la strada a una vera esecuzione parallela. Il linguaggio è vivo e in continua evoluzione.

---

## Python, Stato dell'Arte: dove viene usato oggi

Se vi chiedete perché vale la pena imparare Python nel 2025, la risposta più onesta è: perché è diventato il linguaggio generalista più usato al mondo per una gamma di applicazioni straordinariamente ampia.

**Scienza dei dati e intelligenza artificiale** sono oggi l'uso più visibile. Librerie come NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow e PyTorch hanno fatto di Python il linguaggio nativo dell'analisi dati e del machine learning. Quando leggete di un modello di linguaggio o di una rete neurale, quasi certamente il codice di training era scritto in Python (o in un wrapper Python attorno a codice C++ per le parti critiche).

**Automazione e scripting** sono il terreno storico di Python: sostituire sequenze di operazioni manuali con uno script è il caso d'uso che Guido van Rossum aveva in mente dall'inizio. Sysadmin, ricercatori, analisti: chiunque debba fare cose ripetitive con file, reti o API trova in Python uno strumento immediato.

**Sviluppo web backend** è un altro settore consolidato. Framework come Django e Flask permettono di costruire applicazioni web complete con poche righe. Molti servizi che usate ogni giorno sono costruiti su questi strumenti.

**Applicazioni scientifiche e accademiche**: in fisica, bioinformatica, chimica computazionale, economia, psicologia sperimentale, Python ha progressivamente sostituito MATLAB e R come linguaggio di riferimento per l'analisi statistica e la simulazione.

**Embedded e microcontrollori**: con **MicroPython** e **CircuitPython** è possibile eseguire codice Python su microcontrollori come il Raspberry Pi Pico o alcune schede basate su ESP32; i vantaggi in termini di leggibilità si trasferiscono anche in quel dominio.

**Istruzione**: Python è il linguaggio più insegnato nelle università di tutto il mondo per i corsi introduttivi di programmazione, e non è un caso.

La conseguenza pratica è che imparare Python non vi rinchiude in una nicchia: vi dà accesso a un ecosistema vastissimo, a una comunità enorme, e a una quantità di materiale didattico senza pari.

---

## Implementazioni di Python

Quando si dice "installare Python", di solito si intende installare **CPython**: l'implementazione di riferimento scritta in linguaggio C, sviluppata direttamente dalla Python Software Foundation. È quella che scaricate da python.org, è quella a cui si riferisce questo corso, ed è quella che il 99% dei programmatori usa nella pratica quotidiana.

Ma CPython non è l'unica implementazione del linguaggio. Python è definito da una specifica (il *language reference*), e chiunque può scrivere un interprete che la rispetti. Alcune di queste alternative sono nate per ragioni molto concrete.

**Jython** è un'implementazione di Python scritta in Java che gira sulla **Java Virtual Machine (JVM)**. Il vantaggio è l'interoperabilità diretta con le librerie Java: un programma Jython può importare e usare classi Java come se fossero moduli Python nativi. È utile in ambienti enterprise dove l'ecosistema Java è già consolidato. Il limite è che Jython è rimasta ferma a Python 2.7 per molto tempo e il supporto a Python 3 è ancora incompleto.

**IronPython** fa per il mondo Microsoft quello che Jython fa per Java: è un'implementazione Python che gira sul **Common Language Runtime (CLR)** di .NET. Permette di usare librerie .NET direttamente da Python e viceversa. Anche qui, il supporto alla versione 3 è arrivato tardi.

**PyPy** è probabilmente l'alternativa più interessante dal punto di vista tecnico. È un'implementazione di Python scritta in Python stesso (in una variante ristretta chiamata RPython), e usa una tecnica chiamata **compilazione JIT** (Just-In-Time) per tradurre il codice in istruzioni macchina durante l'esecuzione. Il risultato è che PyPy è spesso **da 5 a 10 volte più veloce** di CPython per codice computazionalmente intensivo. I programmi Python standard girano su PyPy senza modifiche nella maggior parte dei casi. Il limite è la compatibilità con alcune estensioni C (come NumPy, storicamente), anche se negli anni la situazione è molto migliorata.

**MicroPython** è una reimplementazione compatta di Python 3 progettata per girare su microcontrollori con risorse limitate (pochi kilobyte di RAM, nessun sistema operativo tradizionale). Non include la libreria standard completa, ma supporta un sottoinsieme funzionale e aggiunge moduli specifici per l'hardware.

**Cython** è un caso a parte: non è un interprete Python alternativo ma un *compilatore* che traduce Python (con alcune estensioni di tipo opzionali) in codice C, poi compilato come estensione nativa. È lo strumento preferito quando si vuole ottimizzare parti critiche di un programma senza abbandonare Python.

Per questo corso e per i vostri primi anni di programmazione Python, CPython è tutto ciò di cui avrete bisogno. Le alternative diventano rilevanti quando si lavora in contesti specifici (ambienti Java o .NET, ottimizzazione di performance, sistemi embedded).

---

## Strumenti Essenziali: Editor, Console e Debugger

Un falegname esperto sa scegliere gli attrezzi giusti per ogni lavoro; allo stesso modo, un programmatore dovrebbe conoscere l'ecosistema di strumenti che lo circonda. Non tutti gli strumenti sono ugualmente adatti a tutti i contesti, e le preferenze personali giocano un ruolo: quello che conta è capire cosa fa ogni categoria di strumento.

### L'interprete interattivo (REPL)

Quando si installa Python e si digita `python` (o `python3` su molti sistemi Linux e macOS) in un terminale, si entra nel **REPL**: Read-Eval-Print Loop. L'interprete legge un'istruzione, la valuta, stampa il risultato, e torna ad aspettare. È lo strumento più immediato per esplorare il linguaggio: potete scrivere un'espressione e vedere immediatamente cosa restituisce, testare una funzione appena scritta, o verificare il comportamento di un modulo.

```python
>>> 7 / 2
3.5
>>> "Python"[::-1]
'nohtyP'
>>> import math
>>> math.sqrt(144)
12.0
```

Il REPL standard è funzionale ma essenziale. Un'alternativa molto più ricca è **IPython**: un REPL avanzato con completamento automatico, colorazione della sintassi, cronologia persistente, e comandi speciali (i cosiddetti "magic commands") come `%timeit` per misurare il tempo di esecuzione. IPython è la base su cui è costruito Jupyter.

### Editor di testo e IDE

Per scrivere programmi di lunghezza reale si usa un editor. La distinzione fondamentale è tra **editor di testo con supporto a Python** e **IDE** (Integrated Development Environment).

Un IDE integra in un'unica applicazione l'editor, il debugger, il gestore dei pacchetti, il terminale, e spesso strumenti di analisi statica del codice. Il principale IDE dedicato a Python è **PyCharm** di JetBrains: professionale, completo, con un'edizione Community gratuita. È la scelta più comune in ambienti di lavoro strutturati.

**Visual Studio Code** (VS Code) di Microsoft occupa una posizione intermedia: tecnicamente è un editor di testo, ma con l'estensione Python (sviluppata da Microsoft stessa) diventa quasi indistinguibile da un IDE completo, con IntelliSense (completamento intelligente), debugger integrato, supporto ai virtual environment, e molto altro. È gratuito, leggero, estremamente popolare, e funziona bene sia per Python che per decine di altri linguaggi.

**Thonny** merita una menzione speciale in un corso introduttivo: è un IDE minimalista progettato specificamente per chi impara Python per la prima volta. L'interfaccia è pulita, il debugger visuale mostra passo per passo cosa succede all'interno del codice (compreso lo stato delle variabili in ogni momento), e viene distribuito con un interprete Python integrato, il che elimina i problemi di configurazione dell'ambiente. Se siete alle prime armi e volete un ambiente che "funziona subito", Thonny è la scelta più semplice.

**IDLE** è l'ambiente incluso nell'installazione standard di Python (dal nome del membro dei Monty Python Eric Idle, ovviamente). Modesto nelle funzionalità ma sempre disponibile e sufficiente per gli esercizi del corso.

Per chi preferisce lavorare in un browser senza installare nulla localmente, piattaforme come **Replit**, **Google Colab** (particolarmente popolare in ambito data science, basato su Jupyter Notebook) e **Programiz** offrono ambienti Python online gratuiti.

### Il Debugger

Il debugger è lo strumento che vi permette di interrompere l'esecuzione di un programma in punti precisi (i cosiddetti **breakpoint**), ispezionare il valore delle variabili in quel momento, e procedere istruzione per istruzione per capire cosa sta succedendo. È l'antidoto alla tecnica di debug più rozza ma più diffusa: inserire `print()` ovunque per vedere i valori intermedi.

Python include un debugger nativo chiamato **pdb** (Python Debugger), utilizzabile direttamente da terminale. In pratica, la maggior parte dei programmatori usa il debugger integrato nel proprio IDE: quello di VS Code o PyCharm è visuale e intuitivo, con pannelli che mostrano lo stack delle chiamate, le variabili locali e globali, e permettono di modificare i valori a runtime.

Imparare a usare il debugger è una delle abilità più preziose che un programmatore possa acquisire: riduce drasticamente il tempo di risoluzione dei bug e sviluppa una comprensione più profonda del flusso di esecuzione del programma.

---

## Conclusione: il linguaggio e il suo contesto

Python non è nato per essere il linguaggio più potente o il più veloce: è nato per essere il più leggibile, il più accessibile, e il più piacevole da usare. Quella filosofia, codificata nel Zen of Python e incarnata in ogni scelta progettuale del linguaggio, è la ragione per cui trent'anni dopo Python è ovunque.

La transizione da Python 2 a Python 3 è ormai storia; sapere che è avvenuta vi aiuterà a capire certi angoli oscuri della documentazione e a non confondervi se incappate in codice datato su internet. Le implementazioni alternative esistono per risolvere problemi specifici, ma CPython è la vostra casa.

Gli strumenti cambieranno con le vostre esigenze: oggi Thonny o IDLE, domani VS Code o PyCharm, dopodomani forse Jupyter o l'interprete su un microcontrollore. Quello che non cambia è il linguaggio sotto di essi.

Con questo contesto in mente, siete pronti ad entrare nel vivo: variabili, operatori, strutture di controllo, funzioni. Il percorso PCEP vi aspetta.
