# Capitolo 1: Sezione 1.2 — Logica e Struttura di Python: Keyword, Istruzioni, Indentazione, Commenti

## Introduzione: Un Linguaggio con le Sue Regole

Immaginate di leggere uno spartito musicale. Le note hanno un valore fisso, le battute scandiscono il tempo e gli strumenti sono raggruppati in pentagrammi allineati. Questa disposizione non è casuale: è il modo in cui il compositore comunica l'armonia agli orchestrali. Se spostaste una nota fuori dal rigo, ignoraste le pause o cambiaste il tempo, il brano diventerebbe rumore.

Python funziona esattamente così. Ha una struttura, una logica interna, un vocabolario riservato. Nella dispensa precedente abbiamo visto la distinzione tra interprete e compilatore e abbiamo introdotto il concetto di lessico, sintassi e semantica. Ora scendiamo un livello e guardiamo come quella struttura si manifesta concretamente nel codice che scriviamo ogni giorno: le parole che Python riserva per sé, le istruzioni che compongono un programma, le regole di indentazione che danno significato alla posizione del codice, e i commenti che ci permettono di parlare al programmatore umano senza che Python si intrometta.

Questi quattro elementi, presi insieme, definiscono la forma di qualsiasi programma Python ben scritto. Non sono dettagli da memorizzare passivamente: sono la grammatica che rende possibile la comunicazione tra voi e la macchina.

## Le Keyword: Il Vocabolario Riservato di Python

In ogni lingua, ci sono parole che non si possono usare come nomi propri. In italiano non potreste chiamare vostra figlia "Se" o vostro figlio "Mentre", perché quelle parole hanno già un ruolo grammaticale preciso. Python ha la stessa convenzione, ma è molto più rigida: esiste un insieme fisso di parole, dette **keyword** (parole chiave), che appartengono esclusivamente alla grammatica del linguaggio e non possono essere usate come nomi per variabili, funzioni o qualsiasi altro oggetto che voi definiate.

Queste keyword non sono scelte arbitrarie. Ognuna di esse corrisponde a un'operazione fondamentale del linguaggio: `if` introduce una condizione, `for` avvia un ciclo, `def` definisce una funzione, `return` restituisce un valore, `import` carica un modulo esterno, e così via. Sono i mattoni sintattici della lingua.

Python 3 definisce 35 keyword. Non è necessario memorizzarle tutte ora, ma è utile sapere che esistono e riconoscere il messaggio di errore che si ottiene quando si prova a usarne una come nome di variabile. Se provaste a scrivere questo:

```python
# Tentativo di usare una keyword come nome di variabile
# QUESTO CODICE PRODUCE UN ERRORE
for = 10
```

Python risponde immediatamente con un `SyntaxError`. Non è che il valore 10 sia problematico: è il nome `for` a essere illegale in quella posizione, perché Python lo riconosce come l'inizio di un ciclo, non come un nome.

Le keyword più importanti che incontrerete nei capitoli a venire, raggruppate per funzione, sono: `if`, `elif`, `else` per le decisioni; `for`, `while`, `break`, `continue`, `pass` per i cicli; `def`, `return`, `lambda` per le funzioni; `class` per la programmazione orientata agli oggetti; `import`, `from`, `as` per i moduli; `True`, `False`, `None` per i valori speciali; `and`, `or`, `not`, `in`, `is` per gli operatori logici e di appartenenza; `try`, `except`, `finally`, `raise` per la gestione delle eccezioni.

Notate che `True`, `False` e `None` iniziano con la lettera maiuscola. Non è una coincidenza stilistica: Python distingue tra maiuscole e minuscole (è un linguaggio **case-sensitive**), quindi `True` e `true` sono cose completamente diverse. `True` è una keyword con un significato preciso; `true` sarebbe un nome di variabile qualsiasi, e Python non saprebbe cosa farne senza che voi lo definiate prima.

## Le Istruzioni: Le Unità di Lavoro del Programma

Se le keyword sono il vocabolario, le **istruzioni** sono le frasi. Un programma Python è una sequenza di istruzioni, ed è eseguendo queste istruzioni una dopo l'altra che l'interprete compie il lavoro.

Un'istruzione è, in senso generale, un'unità di codice che esprime un'azione completa. L'istruzione più semplice che abbiate già visto è l'assegnazione di un valore a una variabile:

```python
# Un'istruzione di assegnazione
numero = 42
```

Questa singola riga dice all'interprete: "crea un nome `numero` e associalo al valore intero 42". È un'istruzione completa: non richiede nulla prima né dopo per avere senso.

In Python, per convenzione e per chiarezza, ogni istruzione occupa una propria riga. Non è come in alcuni altri linguaggi dove il punto e virgola separa le istruzioni e si possono scrivere dieci cose sulla stessa riga. Python incoraggia fortemente la leggibilità: una istruzione, una riga.

Esistono tuttavia situazioni in cui un'istruzione è troppo lunga per stare comodamente su una riga. In questi casi, Python permette di spezzarla usando la barra rovesciata `\` alla fine della riga, oppure sfruttando il fatto che qualsiasi espressione racchiusa tra parentesi può estendersi su più righe senza bisogno di nessun carattere speciale:

```python
# Istruzione su più righe con barra rovesciata
somma = 1 + 2 + 3 + \
        4 + 5 + 6

# Istruzione su più righe con parentesi (stile preferito)
somma = (1 + 2 + 3 +
         4 + 5 + 6)

print(somma)
# Output: 21
```

Il secondo stile, con le parentesi, è quello raccomandato dalle convenzioni di stile Python (PEP 8) perché è più robusto: la barra rovesciata è fragile, uno spazio accidentale dopo di essa può causare un errore difficile da diagnosticare.

Esiste anche la possibilità tecnica di scrivere più istruzioni sulla stessa riga separandole con un punto e virgola, ma questa pratica è fortemente scoraggiata perché riduce la leggibilità:

```python
# Possibile ma sconsigliato
a = 1; b = 2; c = 3

# Molto meglio
a = 1
b = 2
c = 3
```

La filosofia di Python è che il codice viene scritto una volta ma letto molte volte: da voi, dai colleghi, da voi stessi tra sei mesi quando avrete dimenticato i dettagli. La leggibilità non è un lusso, è un requisito.

### Espressioni vs Istruzioni: Calcolare vs Agire

Per capire come ragiona l'interprete Python, dobbiamo distinguere tra due concetti che spesso i programmatori alle prime armi confondono: le **espressioni** e le **istruzioni**. Se il codice fosse un discorso, le espressioni sarebbero i dati e i calcoli, mentre le istruzioni sarebbero le azioni compiute.

#### L'Espressione: "Quanto fa?"
Un'**espressione** è una combinazione di valori (letterali), variabili e operatori che l'interprete **valuta** per produrre un risultato. Pensate all'espressione come a una domanda che ponete a Python: "Quanto fa questa roba?".

* `2 + 2` è un'espressione (risultato: `4`).
* `prezzo * 1.22` è un'espressione (risultato: il prezzo ivato).
* `"Ciao" + " " + nome` è un'espressione (risultato: un saluto personalizzato).

La caratteristica fondamentale di un'espressione è che **restituisce sempre un valore**. Se la scrivete nel REPL di Python, vedrete subito il risultato della valutazione.

#### L'Istruzione: "Fallo!"
Un'**istruzione** (o *statement*) è un comando completo che ordina a Python di **eseguire un'azione**. Mentre l'espressione calcola qualcosa, l'istruzione "muove" qualcosa o cambia lo stato del programma.

* `x = 10` è un'istruzione (assegnamento). Non "fa" 10, ma *ordina* a Python di memorizzare 10 in `x`.
* `print("Ciao")` è un'istruzione (chiamata di funzione). Ordina a Python di inviare del testo allo schermo.
* `if x > 0:` è l'inizio di un'istruzione composta (controllo di flusso).

#### La differenza pratica
Un'istruzione può **contenere** una o più espressioni, ma un'espressione da sola non costituisce necessariamente un'istruzione utile. In Python, quasi tutto ciò che "fa qualcosa" di visibile o permanente è un'istruzione, mentre tutto ciò che "è un valore" o "diventa un valore" è un'espressione.

## L'Indentazione: La Struttura Visiva che Dà Significato

Arriviamo ora a uno degli aspetti di Python che più sorprende chi proviene da altri linguaggi di programmazione: l'**indentazione** non è solo una questione estetica, è parte integrante della sintassi. In Python, lo spazio a sinistra del codice ha un significato preciso e obbligatorio.

Per capire perché, consideriamo una situazione quotidiana. Immaginate un ricettario scritto così:

> Fate bollire l'acqua.  
> Se l'acqua è salata:  
> &emsp;Aggiungete la pasta.  
> &emsp;Aspettate 10 minuti.  
> Scolate.

L'indentazione visiva delle due righe centrali comunica inequivocabilmente che quelle azioni appartengono alla condizione "se l'acqua è salata". "Scolate" invece è al livello principale: va fatto sempre, indipendentemente da qualsiasi condizione.

Python usa esattamente questa logica. Ogni blocco di codice che "appartiene" a qualcosa (una condizione, un ciclo, una funzione) deve essere rientrato di una quantità consistente rispetto alla riga che lo introduce. La convenzione standard, stabilita da PEP 8 e universalmente adottata, è di **quattro spazi** per ogni livello di indentazione.

Vediamo un esempio concreto. Nel codice seguente (che usa la keyword `if`, che studieremo in dettaglio nella Sezione 2.1) l'indentazione stabilisce quali righe fanno parte del ramo condizionale:

```python
temperatura = 35

if temperatura > 30:
    print("Fa caldo!")         # Questa riga è dentro il blocco if
    print("Prendi dell'acqua") # Anche questa

print("Fine del programma")    # Questa è fuori dal blocco if
```

Le prime due `print` sono indentate di quattro spazi: appartengono al blocco `if` e vengono eseguite solo se `temperatura > 30`. L'ultima `print` è al livello principale e viene eseguita sempre. Se eseguite questo codice con `temperatura = 35`, vedrete tutte e tre le righe. Se cambiate il valore a 20, vedrete solo l'ultima.

La cosa fondamentale da capire è che Python non usa parentesi graffe `{}` come molti altri linguaggi per delimitare i blocchi. Usa l'indentazione. Questo significa che se dimenticate di indentare o indentate in modo inconsistente, otterrete un errore:

```python
# QUESTO CODICE PRODUCE UN IndentationError
if temperatura > 30:
print("Fa caldo!")   # Manca l'indentazione!
```

```python
# ANCHE QUESTO È SBAGLIATO
if temperatura > 30:
    print("Fa caldo!")
      print("Errore!")  # Indentazione inconsistente (6 spazi invece di 4)
```

L'interprete Python è estremamente preciso su questo punto. Un blocco deve avere la stessa quantità di spazi per tutte le sue righe: non potete mescolare 2 spazi su una riga e 4 sull'altra.

Una regola pratica da tenere a mente: ogni riga che introduce un nuovo blocco termina con i due punti `:`. Dopo i due punti, tutte le righe successive che fanno parte di quel blocco devono essere indentate:

```python
# Schema generale: la riga con ":" introduce un blocco indentato
parola_chiave condizione:
    prima riga del blocco
    seconda riga del blocco
    ...

riga_al_livello_principale
```

Infine, un avvertimento pratico: usate sempre **spazi**, mai il tasto Tab, per l'indentazione. Alcuni editor inseriscono automaticamente 4 spazi quando premete Tab, ma altri inseriscono un carattere di tabulazione vero e proprio. Mescolare spazi e tab nello stesso file causa errori sottili e difficili da trovare. VS Code, l'editor che usate, è configurato per default per inserire spazi: potete verificarlo guardando la barra in basso a destra della finestra, dove apparirà "Spaces: 4".

## I Commenti: Parlare al Lettore Umano

Il terzo strumento strutturale di Python è il **commento**: testo inserito nel codice che l'interprete ignora completamente, destinato esclusivamente agli esseri umani che leggono il programma.

Un commento in Python inizia con il simbolo cancelletto `#`. Tutto ciò che segue il `#` sulla stessa riga viene ignorato dall'interprete:

```python
# Questo è un commento su una riga intera
temperatura = 35  # Questo è un commento a fine riga

# L'interprete esegue solo l'assegnazione qui sopra
# Il testo dei commenti non ha alcun effetto sul programma
```

I commenti possono essere posizionati su una riga da soli (commento a riga intera) oppure dopo una riga di codice (commento inline). Entrambi gli stili sono validi, ma esiste una convenzione: i commenti inline di solito si mettono dopo almeno due spazi dalla fine del codice, per tenere separati visivamente il codice e il commento.

Python non ha una sintassi dedicata per i commenti su più righe come altri linguaggi. Per commentare un blocco di testo si usa semplicemente il cancelletto su ogni riga:

```python
# Questo programma calcola la temperatura media
# di una sequenza di letture fornite dall'utente.
# Autore: nome.cognome@example.com
# Versione: 1.0
```

Esiste anche la convenzione di usare stringhe letterali triple-virgolette come "commento" di più righe, ma tecnicamente quelle sono stringhe che Python crea e poi scarta, non commenti veri. L'unico modo ufficiale per scrivere un commento è il cancelletto.

### Cosa commentare e cosa no

Un'abilità che si acquisisce con l'esperienza è capire **quando** scrivere un commento. La regola generale è questa: i commenti devono spiegare il *perché*, non il *cosa*. Il codice stesso mostra già cosa fa; un buon commento spiega la ragione di una scelta non ovvia.

Considerate questi due esempi:

```python
# Moltiplica per 1.22
prezzo_con_iva = prezzo_netto * 1.22  # Commento inutile, il codice è già chiaro

# Aggiunge l'IVA al 22%, aliquota applicabile ai beni non essenziali (DPR 633/72)
prezzo_con_iva = prezzo_netto * 1.22  # Commento utile: spiega la costante magica
```

Il primo commento è ridondante: chiunque sappia leggere Python capisce già che si sta moltiplicando per 1.22. Il secondo aggiunge informazione genuina: spiega da dove viene quel numero e perché è corretto.

Un altro uso prezioso dei commenti è temporaneo: durante lo sviluppo, a volte si "commenta" del codice per disattivarlo senza cancellarlo, magari perché si vuole testare una versione alternativa. Questa tecnica è utile come strumento di debug e di esplorazione:

```python
# Versione originale (mantenuta per confronto)
# risultato = calcolo_vecchio(dati)

# Nuova versione da testare
risultato = calcolo_nuovo(dati)
```

Tuttavia, il codice commentato che non serve più dovrebbe essere cancellato prima di consegnare o pubblicare il programma. I sistemi di version control come Git (che già usate) permettono di recuperare versioni precedenti del codice: non è necessario mantenere la storia nel file sorgente.

## Mettere Tutto Insieme: Un Programma Strutturato

Ora che abbiamo visto i quattro elementi separatamente, vale la pena osservare come interagiscono in un piccolo programma reale. Il codice seguente usa costrutti che studieremo nei capitoli successivi, ma è leggibile anche adesso:

```python
# ================================================================
# Classificatore di temperatura
# Legge un valore e stampa una descrizione qualitativa
# ================================================================

# Valore da classificare (simuliamo un input utente)
temperatura = 22

# Classificazione basata su soglie standard (in gradi Celsius)
if temperatura < 0:
    categoria = "gelido"
    consiglio = "Evitate di uscire se possibile"
elif temperatura < 10:
    categoria = "freddo"
    consiglio = "Vestirsi a strati"
elif temperatura < 20:
    categoria = "fresco"
    consiglio = "Una giacca leggera è sufficiente"
elif temperatura < 30:
    categoria = "mite"
    consiglio = "Clima ideale"
else:
    categoria = "caldo"
    consiglio = "Idratarsi spesso"

# Stampa il risultato
print("Temperatura:", temperatura, "°C")
print("Categoria:", categoria)
print("Consiglio:", consiglio)

# Output atteso (con temperatura = 22):
# Temperatura: 22 °C
# Categoria: mite
# Consiglio: Clima ideale
```

In questo programma potete vedere tutti e quattro gli elementi strutturali in azione. Le **keyword** `if`, `elif`, `else` governano il flusso del programma. Ogni **istruzione** occupa la propria riga e compie un'azione definita. L'**indentazione** a quattro spazi separa chiaramente le righe che appartengono a ciascun ramo condizionale dalle righe al livello principale. I **commenti** spiegano il contesto (cosa fa il programma, da dove vengono le costanti) senza ripetere ciò che il codice già dice.

## Conclusione: La Forma È Sostanza

In molte discipline esiste la tentazione di separare forma e contenuto: quello che dici sarebbe più importante di come lo dici. In programmazione questa distinzione non regge. La struttura di un programma Python, la sua forma visiva, il modo in cui le keyword e le istruzioni si dispongono sulla pagina con la giusta indentazione e i commenti nei posti giusti, tutto questo non è decorazione. È il contenuto stesso.

Un programma mal indentato non è un programma con un problema estetico: è un programma che fa cose diverse da quelle che il programmatore intendeva, oppure un programma che l'interprete rifiuta di eseguire. Un programma con keyword usate come nomi di variabili non compila. Un programma senza commenti in punti critici è un programma che il vostro sé futuro non riuscirà a mantenere.

Python non è stato progettato per essere scritto una volta e poi dimenticato. È stato progettato per essere scritto, riletto, modificato, esteso. La leggibilità che l'indentazione obbligatoria e le convenzioni sui commenti garantiscono è un investimento che si ripaga ogni volta che tornate su un programma scritto settimane fa.

Nel prossimo capitolo entreremo nel dettaglio di letterali, variabili e sistemi numerici: inizieremo a popolare i programmi con dati reali, dando finalmente qualcosa di concreto su cui operare con le istruzioni e la struttura che abbiamo appena imparato a riconoscere.
