# Capitolo 3: Sezione 3.1 - Prendere Decisioni in Python: Una Guida alla Logica Condizionale

## Introduzione: Il Dialogo tra Programma e Computer

Quando scriviamo un programma, in realtà stiamo insegnando a un computer come fare domande. Un programmatore concepisce una sequenza di interrogativi e il computer fornisce risposte secondo regole ben precise. La peculiarità affascinante dei computer è che rispondono sempre e solo in due modalità: con un sì oppure con un no. Non si sentiranno mai rispondere "Lasciami pensare", "Non so", oppure "Probabilmente sì, ma non sono sicuro". Questa semplicità apparente è in realtà la forza che rende i computer prevedibili e controllabili.

Il compito del programmatore, dunque, non è semplicemente quello di fare domande. È quello di insegnare al programma come reagire alle risposte che riceve. Se il nostro programma pone una domanda e il computer risponde "vero", allora il programma deve sapere cosa fare. Se la risposta è "falso", il programma deve sapere come comportarsi diversamente. Questo meccanismo di azione-reazione condizionata è il fondamento di ogni logica di programmazione moderna.

Per realizzare questa capacità di decisione, Python ci mette a disposizione un insieme di operatori speciali che ci permettono di formulare domande in linguaggio di programmazione e di gestire le risposte conseguenti. Esaminiamo questi operatori uno dopo l'altro, iniziando dai più semplici fino ad arrivare a costrutti più sofisticati.

## Il Linguaggio delle Domande: Gli Operatori di Confronto

### L'Operatore di Uguaglianza: "Sono Uguali?"

La domanda più elementare che possiamo fare a un computer è: "Questi due valori sono uguali?". In Python, per porre questa domanda utilizziamo l'operatore di uguaglianza, rappresentato da due segni di uguale consecutivi: `==`.

È fondamentale non confondere questo operatore con il singolo `=`, che abbiamo già incontrato e che serve per assegnare un valore a una variabile. Ecco la distinzione critica:

- L'operatore `=` è un operatore di **assegnazione**. Quando scriviamo `numero = 5`, stiamo dicendo al computer "assegna il valore 5 alla variabile numero".
- L'operatore `==` è un operatore di **confronto**. Quando scriviamo `numero == 5`, stiamo chiedendo "la variabile numero contiene il valore 5?".

Questa distinzione non è meramente grammaticale; è una delle fonti più comuni di errori per i programmatori alle prime armi, perché l'assegnazione modifica lo stato del programma mentre il confronto lo esamina senza modificarlo.

Consideriamo un esempio pratico:

```python
# Questo è un operatore di ASSEGNAZIONE
numero = 10  # La variabile 'numero' contiene ora il valore 10

# Questo è un operatore di CONFRONTO
numero == 10  # Questa domanda restituisce True, perché numero contiene 10
numero == 15  # Questa domanda restituisce False, perché numero non contiene 15
```

L'operatore `==` è un operatore binario, il che significa che ha bisogno di due operandi per funzionare: uno a sinistra e uno a destra della domanda. Inoltre, ha un'associatività sinistra, il che significa che se ci sono più operatori dello stesso tipo in una riga, vengono valutati da sinistra verso destra.

Immaginiamo uno scenario più interessante. Un programmatore insonne sta contando pecore nere e bianche, e vuole addormentarsi quando le pecore nere sono esattamente il doppio di quelle bianche. La domanda da fare al computer sarebbe:

```python
# Chiediamo: il numero di pecore nere è esattamente il doppio di quelle bianche?
pecore_nere == 2 * pecore_bianche
```

In questa espressione, il computer valuterà prima la moltiplicazione (`2 * pecore_bianche`), perché l'operatore di moltiplicazione ha una priorità più alta dell'operatore di uguaglianza. L'espressione è quindi equivalente a:

```python
pecore_nere == (2 * pecore_bianche)
```

### L'Operatore di Disuguaglianza: "Sono Diversi?"

Se vogliamo sapere il contrario—se due valori sono diversi piuttosto che uguali—utilizziamo l'operatore di disuguaglianza: `!=`. Questo operatore restituisce `True` quando i due valori non sono uguali, e `False` quando sono uguali.

```python
valore = 0
print(valore != 0)  # Restituisce False, perché valore è uguale a 0

valore = 1
print(valore != 0)  # Restituisce True, perché valore non è uguale a 0
```

Dal punto di vista logico, `valore != 0` è esattamente l'opposto di `valore == 0`. Sebbene spesso potremmo usare l'una o l'altra espressione, scegliere quella più leggibile dipende dal contesto e dalla naturale formulazione della domanda che vogliamo fare.

### Gli Operatori di Confronto Numerico

Oltre all'uguaglianza, Python ci offre una serie di operatori che permettono di confrontare la grandezza relativa di due numeri. Questi operatori sono cruciali quando lavoriamo con dati numerici e desideriamo prendere decisioni basate sul loro valore assoluto o relativo.

L'operatore **maggiore di**, rappresentato da `>`, risponde alla domanda "il primo valore è più grande del secondo?". Tornando al nostro programmatore insonne, potrebbe voler sapere se ci sono più pecore nere che bianche:

```python
pecore_nere > pecore_bianche  # True se le pecore nere superano quelle bianche
```

Se vuole consentire il caso in cui i due numeri siano uguali, userà l'operatore **maggiore o uguale a**: `>=`. La differenza tra gli operatori "stretti" (come `>`) e "non stretti" (come `>=`) è sottile ma cruciale in molte applicazioni pratiche. Ad esempio, se vogliamo determinare se è necessario indossare un cappello caldo, potremmo decidere di farlo quando la temperatura è zero gradi o inferiore:

```python
# Temperatura in gradi Celsius
temperatura_esterno >= 0.0  # True se possiamo andare fuori senza cappello
```

Allo stesso modo, gli operatori **minore di** (`<`) e **minore o uguale a** (`<=`) rispondono alle domande opposte. Se stiamo verificando il rischio di una multa da parte della polizia stradale su un'autostrada con limite di velocità a 85 mph:

```python
# Velocità attuale in miglia all'ora
velocita_attuale < 85   # Domanda stretta: siamo sotto il limite?
velocita_attuale <= 85  # Domanda non stretta: siamo al limite o sotto?
```

La scelta tra l'operatore stretto e quello non stretto dipende dalla specifica applicazione. In ambito legale, ad esempio, superare il limite di 85 mph di anche un solo miglio potrebbe già costituire una violazione, quindi il contesto è critico.

È importante notare che questi operatori di confronto hanno una priorità più alta rispetto agli operatori di uguaglianza e disuguaglianza. Questo significa che in un'espressione come `numero > 5 == True`, il computer valuterà prima `numero > 5` e poi confronterà il risultato con `True`.

## Conservare e Utilizzare le Risposte

Una volta che il computer ha risposto a una nostra domanda, abbiamo almeno due strade disponibili. La prima opzione è conservare la risposta in una variabile, così da poterla consultare successivamente. Questo è estremamente utile quando vogliamo tracciare lo stato di una condizione lungo tutta l'esecuzione del programma.

```python
# Chiediamo al computer una domanda e conserviamo la risposta
numero_leoni = 5
numero_leonesse = 3

# Memorizziamo la risposta alla domanda "ci sono più leoni che leonesse?"
ci_sono_piu_leoni = numero_leoni >= numero_leonesse

# Ora possiamo usare questa risposta later nel nostro programma
print(ci_sono_piu_leoni)  # Stampa: True
```

La seconda opzione, molto più comune e pratica, è usare la risposta immediatamente per decidere il comportamento del programma. È qui che entriamo nel territorio della **esecuzione condizionale**—il cuore della logica di programmazione.

## Le Istruzioni Condizionali: Insegnare al Programma a Scegliere

Nella vita reale, le nostre azioni dipendono spesso da condizioni. Facciamo una passeggiata se il tempo è bello. Se il tempo è brutto e freddo, restiamo a casa. Usiamo istintivamente una forma di logica condizionale nella nostra vita quotidiana, ma in programmazione dobbiamo esplicitare completamente questa logica, perché il computer non ha intuizioni né senso comune.

Python fornisce un meccanismo speciale per implementare questa logica condizionale: l'**istruzione if** (se). È la più semplice forma di controllo del flusso di esecuzione e la chiave per insegnare ai programmi come prendere decisioni.

### La Forma Più Semplice: l'Istruzione if

La forma più basilare dell'istruzione if segue una struttura predefinita e invariabile:

```python
if condizione:
    # Codice da eseguire se la condizione è vera
    istruzione1
    istruzione2
```

Analizziamo i componenti necessari di questa struttura:

1. La parola chiave `if`, che segnala al computer che stiamo introducendo una decisione.
2. Uno o più spazi vuoti (per convenzione, almeno uno).
3. Un'espressione che rappresenta la condizione—può essere una domanda diretta come `numero > 5`, oppure il valore di una variabile booleana come `il_tempo_e_bello`.
4. Due punti `:`, che segnano la fine della linea di condizione.
5. Una o più istruzioni **indentate** (rientrate) che costituiscono il blocco di codice da eseguire se la condizione è vera.

L'**indentazione** è un aspetto cruciale della sintassi di Python. Non è meramente decorativa: Python usa l'indentazione per determinare quali istruzioni appartengono al blocco if. Per convenzione, si usa un'indentazione di quattro spazi per livello di rientro. È assolutamente fondamentale che tutte le righe all'interno dello stesso blocco abbiamo la stessa quantità di indentazione.

Ecco come funziona l'esecuzione:

Se la condizione nell'if è vera (cioè il suo valore è diverso da zero, o più precisamente, rappresenta una verità logica), il computer eseguirà tutte le istruzioni indentate nel blocco. Se la condizione è falsa (zero, o una falsa verità logica), il computer salterà interamente il blocco indentato e continuerà con le istruzioni che seguono al livello di indentazione originale.

Consideriamo l'esempio del nostro programmatore insonne:

```python
# Se il conteggio di pecore raggiunge 120, è ora di dormire
conteggio_pecore = 150

if conteggio_pecore >= 120:
    # Questo blocco viene eseguito perché conteggio_pecore è 150, che è >= 120
    print("È tempo di addormentarsi...")
    dormi_e_sogna()

# Questa riga viene eseguita sempre, indipendentemente dalla condizione
print("Notte!")
```

In questo codice, poiché `conteggio_pecore` è 150, la condizione è vera, e la funzione `dormi_e_sogna()` verrà eseguita. Dopo l'esecuzione di quel blocco, il programma continuerà con il `print("Notte!")`.

Se invece `conteggio_pecore` fosse stato 50, la condizione sarebbe stata falsa, il blocco indentato sarebbe stato completamente saltato, e il programma avrebbe stampato solo "Notte!".

### Ramificazioni a Due Vie: l'Istruzione if-else

Nella vita, spesso abbiamo non solo una cosa da fare se una condizione è vera, ma anche un'alternativa se la condizione è falsa. Python prevede questa situazione con l'istruzione `else`:

```python
if condizione:
    # Blocco eseguito se condizione è vera
    fai_questo()
else:
    # Blocco eseguito se condizione è falsa
    fai_quello()

# Questo codice viene sempre eseguito dopo if/else
continua_qui()
```

L'`else` deve sempre seguire direttamente un `if` (eventualmente preceduto da `elif`, come vedremo), e contiene il codice da eseguire nel caso opposto. Esattamente uno dei due blocchi—quello dell'if o quello dell'else—verrà eseguito.

Nell'esempio del tempo:

```python
# Controllo la situazione meteorologica
if il_tempo_e_bello:
    # Se il tempo è bello, vado a fare una passeggiata
    esci_per_una_passeggiata()
else:
    # Se il tempo non è bello, rimango a casa
    rimani_a_casa()

# In entrambi i casi, dopo qualche ora, avrò fame e mangerò
mangia_pranzo()
```

Questo costrutto è molto leggibile e rispecchia naturalmente il modo in cui ragioniamo sulle decisioni.

### Cascate Decisionali: la Catena if-elif-else

Ma che cosa accade quando le nostre scelte sono più di due? Se il tempo è bello, esco. Se il tempo è mediocre ma i biglietti a teatro sono disponibili, vado a teatro. Se il tempo è pessimo ma un tavolo al ristorante è libero, vado a mangiare fuori. Se nessuna di queste condizioni è soddisfatta, rimango a casa a giocare a scacchi.

Python offre la soluzione con le istruzioni `elif` (abbreviazione di "else if", cioè "altrimenti se"). Permettono di creare cascate di decisioni:

```python
if il_tempo_e_bello:
    # Se il tempo è bello, vado a fare una passeggiata
    esci_per_una_passeggiata()
elif biglietti_disponibili:
    # Se il tempo non è bello MA i biglietti sono disponibili
    vai_a_teatro()
elif tavolo_disponibile:
    # Se nessuna delle precedenti è vera MA il tavolo è libero
    vai_al_ristorante()
else:
    # Se nessuna delle precedenti condizioni è vera
    gioca_scacchi_a_casa()
```

Questa struttura è denominata a volte una **cascata** (cascade). Osserviamo alcune regole importanti per usare correttamente questa cascata:

1. Non puoi usare `else` senza un `if` precedente. Ogni cascata deve iniziare con `if`.
2. Se includi un `else`, questo deve essere l'ultimo ramo della cascata, indipendentemente da quanti `elif` hai prima.
3. `else` è opzionale. Puoi avere una cascata con solo `if` e `elif`, senza il blocco finale `else`.
4. Se esiste un blocco `else` nella cascata, esattamente uno dei blocchi verrà eseguito.
5. Se non esiste un blocco `else`, è possibile che nessun blocco venga eseguito (se tutte le condizioni sono false).

La bellezza dell'indentazione di Python è che la struttura della cascata emerge naturalmente dal codice, rendendo molto chiaro quale sia il flusso logico.

## Analizzare Problemi Concreti: Trovare il Numero Maggiore

Ora applichiamo tutto quello che abbiamo imparato a un problema concreto: trovare il numero più grande tra una serie di numeri. Risolveremo lo stesso problema con complessità crescente.

### Primo Esempio: Due Numeri

Iniziamo con il caso più semplice: confrontare due numeri e determinare quale sia il più grande.

```python
# Leggiamo due numeri da input
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

# Confrontiamo i due numeri e determiniamo il più grande
if numero1 > numero2:
    # Se il primo è maggiore, il primo è il nostro numero più grande
    numero_maggiore = numero1
else:
    # Altrimenti, il secondo è il più grande
    numero_maggiore = numero2

# Stampiamo il risultato
print("Il numero più grande è:", numero_maggiore)
```

Questo codice è diretto e facile da seguire. Poniamo una domanda semplice, otteniamo una risposta semplice, e agiamo di conseguenza.

### Una Nota sulla Sintassi Alternativa

Python offre una possibilità interessante per il codice più compatto. Se un blocco if o else contiene solo una singola istruzione, puoi scriverla sulla stessa riga del colon:

```python
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

if numero1 > numero2: numero_maggiore = numero1
else: numero_maggiore = numero2

print("Il numero più grande è:", numero_maggiore)
```

Mentre questo è tecnicamente valido, è generalmente sconsigliato. Riduce la leggibilità del codice e può essere confuso quando il codice diventa più complesso. La convenzione di programmazione moderna favorisce l'indentazione chiara e esplicita, anche se comporta alcune righe di codice aggiuntive.

### Secondo Esempio: Tre Numeri

Passiamo ora a un problema leggermente più complesso: trovare il numero più grande tra tre.

```python
# Leggiamo tre numeri
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
numero3 = int(input("Inserisci il terzo numero: "))

# Strategia: assumiamo temporaneamente che il primo numero sia il più grande.
# Verificheremo questa ipotesi con i due numeri rimanenti.
numero_massimo = numero1

# Verifichiamo se il secondo numero è più grande del massimo attuale
# e lo aggiorniamo se necessario
if numero2 > numero_massimo:
    numero_massimo = numero2

# Verifichiamo se il terzo numero è più grande del massimo attuale
# e lo aggiorniamo se necessario
if numero3 > numero_massimo:
    numero_massimo = numero3

# Stampiamo il risultato
print("Il numero più grande è:", numero_massimo)
```

Questo approccio è significativamente più elegante di quello che potrebbe venire istintivamente—cioè confrontare tutte le possibili coppie (primo con secondo, secondo con terzo, terzo con primo). Lo schema che seguiamo qui è fondamentale: iniziamo con un'ipotesi, poi la verifichiamo e aggiorniamo progressivamente.

Questo stesso approccio scala facilmente. Se dovessimo trovare il massimo tra quattro, cinque, dieci numeri, aggiungeremmo semplicemente altri blocchi if simili. Non avremmo bisogno di una complessità esponenziale di confronti.

## Introduzione al Pensiero Algoritmico: Pseudocodice e Oltre

Finora abbiamo risolto problemi di dimensione moderata. Ma che cosa accade se ci viene chiesto di trovare il numero più grande tra duecento numeri? Immaginate un codice che richiederebbe almeno duecento variabili e centenovantanove istruzioni if. È gestibile tecnicamente, ma è inefficiente e praticamente impossibile da mantenere.

Fortunatamente, esiste un approccio migliore. Prima di scrivere il codice in Python (o in qualsiasi linguaggio di programmazione), possiamo descrivere la soluzione usando un linguaggio intermedio chiamato **pseudocodice**. Lo pseudocodice non è un vero linguaggio di programmazione—non può essere compilato né eseguito—ma è formale abbastanza da comunicare algoritmi in modo preciso, eppure abbastanza libero per permetterci di pensare senza preoccuparci della sintassi esatta di un linguaggio.

Ecco come potremmo descrivere l'algoritmo per trovare il numero massimo tra un numero indeterminato di numeri:

```
1. Inizializza numero_massimo con un valore estremamente piccolo (es. -999999999)
2. Ripeti i seguenti passi finché l'utente non decide di smettere:
   a. Leggi un numero da input
   b. Se il numero è -1 (il nostro segnale di stop), stampa numero_massimo ed esci
   c. Se il numero è maggiore di numero_massimo, aggiorna numero_massimo
3. Torna al passo 2
```

Questa descrizione contiene un concetto fondamentale che non abbiamo ancora affrontato: la **ripetizione**. Parti del codice possono essere eseguite più volte—tanto quanto necessario. Questo meccanismo è chiamato **loop** (ciclo).

Nel nostro pseudocodice, i passi 2a-2c si ripetono fino a quando l'utente non inserisce il valore di stop. Con un'interfaccia user-friendly, potremmo avere duecento iterazioni o mille, senza dover scrivere il codice duecento o mille volte.

Il concetto di loop è così potente che trasforma i problemi impossibili di dimensione grande in problemi gestibili. Senza loop, un programma che processa un milione di dati richiederebbe un milione di linee di codice. Con i loop, il codice rimane compatto e leggibile, perché esprime l'algoritmo una volta, e il computer lo esegue tante volte quanto necessario.

## Una Nota su Funzioni Incorporate Utili

Prima di concludere questa sezione, è importante sottolineare che Python fornisce molte funzioni incorporate che semplificano compiti comuni. Ad esempio, per trovare il numero massimo tra una serie di valori, Python mette a disposizione la funzione `max()`:

```python
# Leggiamo tre numeri
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
numero3 = int(input("Inserisci il terzo numero: "))

# Usiamo la funzione max() incorporata per trovare il più grande
numero_massimo = max(numero1, numero2, numero3)

# Stampiamo il risultato
print("Il numero più grande è:", numero_massimo)
```

Allo stesso modo, la funzione `min()` restituisce il numero più piccolo.

Tuttavia, il motivo per cui abbiamo affrontato il problema manualmente usando if e if-else è pedagogico. Capire *come* il computer risolve questo problema e *perché* certe soluzioni sono preferibili ad altre è il fondamento per diventare un programmatore consapevole e competente. Le scorciatoie come `max()` sono preziose, ma solo se comprendiamo cosa accade dietro le quinte. Una volta padroneggiato il ragionamento logico sottostante, potrai usare fiduciosamente le funzioni incorporate, sapendo esattamente cosa stanno facendo.

## Concludendo: Dal Pensiero al Codice

In questa sezione abbiamo trasformato la capacità umana di prendere decisioni in un insieme di costrutti programmabili. Gli operatori di confronto permettono al computer di rispondere a domande semplici. Le istruzioni if, if-else e if-elif-else permettono al programma di agire in base a quelle risposte.

Più importante ancora, abbiamo visto come questi concetti di base di logica condizionale si trasformano in algoritmi. Un algoritmo è una sequenza ben definita di passi che risolve un problema. La capacità di tradurre un problema reale in una cascata di decisioni logiche è ciò che separa i programmatori dilettanti da quelli professionisti.

Il prossimo passo naturale nel nostro percorso sarà imparare a ripetere le azioni—i loop—che affronteremo nel capitolo successivo. Con loop e decisioni condizionali, avremo gli strumenti per scrivere programmi che risolvono problemi di complessità arbitraria.
