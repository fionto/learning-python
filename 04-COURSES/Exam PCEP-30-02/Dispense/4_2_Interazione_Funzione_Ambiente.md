# Capitolo 4: Sezione 4.2 - Interazione Funzione-Ambiente: Parametri, Scope e la Parola Chiave `global`

## Introduzione: La Funzione Come Ufficio con la Sua Scrivania

Immaginate una grande azienda con decine di uffici. Ogni ufficio ha la propria scrivania, i propri cassetti, i propri documenti. Un dipendente che lavora nell'ufficio contabilità non può aprire i cassetti dell'ufficio marketing senza un permesso speciale, e viceversa. Quando un dipendente ha bisogno di qualcosa dall'esterno, qualcuno glielo porta sulla soglia della porta, lui lo usa, e poi i documenti tornano a chi li ha portati.

Questa metafora descrive quasi perfettamente come funzionano le funzioni in Python. Ogni funzione è un ufficio separato: ha il suo spazio di lavoro, le sue variabili, e una porta attraverso cui riceve ciò di cui ha bisogno (i parametri) e restituisce i risultati (il valore di ritorno). Il corridoio centrale dell'azienda, dove tutti possono passare, è il cosiddetto scope globale, cioè lo spazio del programma principale.

Capire come le funzioni interagiscono con il mondo esterno è fondamentale: vi permetterà di scrivere codice robusto, privo di effetti collaterali indesiderati, e comprensibile da chiunque lo legga. In questa dispensa esploriamo i tre pilastri di questa interazione: il meccanismo di passaggio degli argomenti, il concetto di scope, e l'uso (da maneggiare con cura) della parola chiave `global`.

Questa dispensa presuppone che abbiate già incontrato la definizione di funzione con `def`, il comando `return`, e il valore speciale `None` trattati nella sezione 4.1.

---

## Parametri e Argomenti: la Differenza che Conta

Prima di tutto, facciamo chiarezza su una distinzione terminologica che l'esame PCEP verifica esplicitamente. I termini "parametro" e "argomento" vengono spesso usati come sinonimi nel linguaggio comune, ma in Python hanno significati precisi e distinti.

Il **parametro** è il nome che compare nella definizione della funzione, tra le parentesi dopo `def`. È una variabile "segnaposto", come una casella vuota con un'etichetta: per ora la casella è vuota, ma sappiamo già come si chiama.

L'**argomento** è il valore concreto che viene passato alla funzione quando la si chiama. È il contenuto che riempie quella casella al momento dell'invocazione.

```python
# 'nome' è un PARAMETRO: compare nella definizione
def saluta(nome):
    print("Ciao,", nome)

# "Matteo" è un ARGOMENTO: viene passato al momento della chiamata
saluta("Matteo")
# Output: Ciao, Matteo
```

La distinzione diventa importante quando si parla di più parametri: ogni parametro ha la sua posizione e il suo nome, e gli argomenti devono corrispondere in modo corretto.

---

## Passaggio Posizionale, Keyword e Misto

Python offre tre modi per associare gli argomenti ai parametri. Capirli bene vi dà una flessibilità enorme nella scrittura delle chiamate a funzione.

### Passaggio posizionale

Il modo più semplice e immediato è quello **posizionale**: il primo argomento va al primo parametro, il secondo al secondo, e così via. L'ordine è tutto.

```python
def descrivi_rettangolo(larghezza, altezza):
    print(f"Larghezza: {larghezza}, Altezza: {altezza}")

# Passaggio posizionale: 10 → larghezza, 5 → altezza
descrivi_rettangolo(10, 5)
# Output: Larghezza: 10, Altezza: 5

# Invertire l'ordine cambia il risultato!
descrivi_rettangolo(5, 10)
# Output: Larghezza: 5, Altezza: 10
```

### Passaggio keyword

Nel passaggio **keyword** (o per nome), si specifica esplicitamente a quale parametro si vuole associare ciascun argomento, usando la sintassi `nome_parametro=valore`. In questo modo l'ordine non ha più importanza.

```python
def descrivi_rettangolo(larghezza, altezza):
    print(f"Larghezza: {larghezza}, Altezza: {altezza}")

# Con keyword, l'ordine non importa
descrivi_rettangolo(altezza=5, larghezza=10)
# Output: Larghezza: 10, Altezza: 5
```

Questo stile è molto utile quando una funzione ha molti parametri: rende la chiamata autoesplicativa, senza dover ricordare l'ordine preciso.

### Passaggio misto

È possibile mescolare i due stili in una stessa chiamata, ma con una regola ferrea: **gli argomenti posizionali devono sempre venire prima di quelli keyword**. Non è possibile fare il contrario.

```python
def crea_profilo(nome, eta, citta):
    print(f"{nome}, {eta} anni, vive a {citta}")

# Prima posizionale (nome), poi keyword per gli altri
crea_profilo("Luca", eta=30, citta="Roma")
# Output: Luca, 30 anni, vive a Roma

# Questo causerebbe un errore: keyword prima di posizionale
# crea_profilo(nome="Luca", 30, citta="Roma")  # SyntaxError!
```

---

## Valori di Default: Parametri Opzionali

Quando definiamo una funzione, possiamo assegnare un valore predefinito a uno o più parametri. Se chi chiama la funzione non fornisce quell'argomento, viene usato automaticamente il valore di default. Se invece lo fornisce, il valore di default viene ignorato e si usa quello passato.

Pensate a un modulo da compilare: alcuni campi sono obbligatori, altri hanno già un valore precompilato che si può lasciare o cambiare. I parametri con default sono i campi precompilati.

```python
def saluta(nome, messaggio="Ciao"):
    print(f"{messaggio}, {nome}!")

# Chiamata senza il secondo argomento: usa il default "Ciao"
saluta("Anna")
# Output: Ciao, Anna!

# Chiamata con il secondo argomento: sovrascrive il default
saluta("Anna", "Buongiorno")
# Output: Buongiorno, Anna!
```

C'è una regola importante per la posizione dei parametri con default: **devono sempre stare dopo i parametri senza default**. Il motivo è pratico: se mettessimo un parametro con default prima di uno senza, Python non saprebbe a quale parametro assegnare i valori posizionali.

```python
# Corretto: il parametro senza default (nome) viene prima
def saluta(nome, messaggio="Ciao"):
    pass

# Sbagliato: causerebbe un SyntaxError
# def saluta(messaggio="Ciao", nome):
#     pass
```

---

## Lo Scope: Il Territorio di Ogni Variabile

Lo **scope** (o ambito di visibilità) definisce dove nel codice una variabile può essere letta o modificata. È uno dei concetti più importanti di tutta la programmazione, e Python lo gestisce in modo elegante e prevedibile.

Tornando alla metafora degli uffici: ogni ufficio (ogni funzione) ha le sue variabili private, invisibili dall'esterno. Il corridoio (il programma principale) ha le sue variabili globali, visibili a tutti ma non modificabili dall'interno degli uffici, a meno di un permesso speciale.

### Variabili locali

Una variabile **locale** è una variabile creata all'interno di una funzione. Esiste solo per tutta la durata di quell'esecuzione della funzione, e poi scompare. Non è visibile dall'esterno.

```python
def calcola_area(raggio):
    pi = 3.14159          # 'pi' è una variabile locale
    area = pi * raggio ** 2   # anche 'area' è locale
    return area

risultato = calcola_area(5)
print(risultato)          # Output: 78.53975

# Tentare di accedere a 'pi' fuori dalla funzione è un errore
# print(pi)               # NameError: name 'pi' is not defined
```

`pi` e `area` nascono all'interno della funzione e muoiono quando la funzione termina. Ogni chiamata a `calcola_area` crea le sue proprie copie di queste variabili, indipendenti da tutte le altre.

### Variabili globali (visibili ma non modificabili)

Una variabile **globale** è definita nel corpo principale del programma, fuori da qualsiasi funzione. Essa è visibile (leggibile) dall'interno delle funzioni, ma, per impostazione predefinita, non può essere modificata dall'interno di una funzione. Se ci si prova, Python crea silenziosamente una nuova variabile locale con lo stesso nome, senza toccare quella globale.

```python
messaggio_globale = "Sono nel programma principale"

def leggi_globale():
    # Possiamo leggere la variabile globale senza problemi
    print(messaggio_globale)

leggi_globale()
# Output: Sono nel programma principale

def prova_a_modificare():
    # Questo NON modifica la variabile globale!
    # Crea invece una nuova variabile LOCALE con lo stesso nome.
    messaggio_globale = "Sono dentro la funzione"
    print(messaggio_globale)

prova_a_modificare()
# Output: Sono dentro la funzione

print(messaggio_globale)
# Output: Sono nel programma principale  ← invariata!
```

### Name hiding (shadowing)

Quando una variabile locale ha lo stesso nome di una variabile globale, la locale "nasconde" la globale all'interno della funzione. Questo fenomeno si chiama **name hiding** o, con termine inglese di uso comune, **shadowing** (fare ombra). Durante l'esecuzione di quella funzione, il nome si riferisce esclusivamente alla variabile locale; quella globale non è accessibile.

```python
valore = 100  # variabile globale

def mostra():
    valore = 42          # variabile locale: "nasconde" quella globale
    print(valore)        # legge la locale: 42

mostra()
# Output: 42

print(valore)
# Output: 100  ← quella globale è rimasta intatta
```

Il shadowing non è un errore, ma può essere fonte di confusione se usato senza intenzione. Scegliere nomi distinti per variabili locali e globali è una buona abitudine.

---

## La Parola Chiave `global`: Aprire la Porta con Cautela

A volte abbiamo davvero bisogno che una funzione modifichi una variabile globale, non una sua copia locale. Python lo permette, ma richiede che lo si dichiari esplicitamente con la parola chiave `global`. Questo è il "permesso speciale" di cui parlavamo prima.

Quando scriviamo `global nome_variabile` all'inizio di una funzione, stiamo dicendo a Python: "Quando incontri questo nome, non creare una variabile locale: usa direttamente quella globale".

```python
contatore = 0  # variabile globale

def incrementa():
    global contatore          # dichiarazione obbligatoria
    contatore = contatore + 1  # ora modifica davvero la globale

incrementa()
incrementa()
incrementa()
print(contatore)
# Output: 3
```

Senza la dichiarazione `global`, il tentativo di fare `contatore = contatore + 1` all'interno della funzione causerebbe un `UnboundLocalError`: Python vedrebbe `contatore` come una variabile locale (perché le viene assegnato un valore), ma nel momento in cui prova a leggere `contatore` per sommarci 1, quella variabile locale non è ancora stata inizializzata.

```python
contatore = 0

def incrementa_sbagliata():
    # Senza 'global', Python tratta 'contatore' come locale.
    # Ma come si fa a leggere una locale non ancora creata?
    contatore = contatore + 1  # UnboundLocalError!

# incrementa_sbagliata()  # Sollevrebbe un errore
```

### `global` e la creazione di nuove variabili

La dichiarazione `global` può essere usata anche per creare una variabile globale dall'interno di una funzione, anche se quella variabile non esisteva prima. Questa possibilità esiste, ma è considerata una pratica da evitare: rende il codice difficile da seguire, perché le variabili globali vengono create in posti inattesi.

```python
def crea_globale():
    global nuova_variabile
    nuova_variabile = "sono nata dentro una funzione!"

crea_globale()
print(nuova_variabile)
# Output: sono nata dentro una funzione!
```

### Quando usare `global`: un consiglio pratico

La parola chiave `global` è potente, ma va usata con parsimonia. Le funzioni che modificano variabili globali sono più difficili da testare, da riutilizzare, e da capire: per sapere cosa fa quella funzione, devo sapere anche qual è lo stato globale al momento della chiamata. In generale, è preferibile che una funzione riceva tutto ciò di cui ha bisogno tramite parametri e comunichi i risultati tramite `return`. L'uso di `global` è giustificato in pochi casi specifici, come contatori o configurazioni condivise in programmi brevi.

---

## Mettere Tutto Insieme: Un Esempio Integrato

Per consolidare i concetti visti, ecco un esempio che mostra parametri con default, passaggio keyword, scope locale e uso consapevole di `global`.

```python
# Variabile globale: tiene traccia di quante operazioni sono state fatte
operazioni_eseguite = 0

def moltiplica(a, b, stampa_risultato=True):
    """Moltiplica due numeri e, opzionalmente, stampa il risultato."""
    global operazioni_eseguite        # accesso alla variabile globale

    risultato = a * b                 # variabile locale
    operazioni_eseguite += 1          # modifica la globale

    if stampa_risultato:
        print(f"{a} x {b} = {risultato}")

    return risultato

# Chiamata con argomenti posizionali
moltiplica(3, 4)
# Output: 3 x 4 = 12

# Chiamata con argomenti keyword e default esplicito
moltiplica(b=7, a=5, stampa_risultato=False)
# (nessun output: stampa_risultato è False)

# Verifichiamo il contatore globale
print(f"Operazioni eseguite finora: {operazioni_eseguite}")
# Output: Operazioni eseguite finora: 2
```

In questo esempio, `a`, `b` e `risultato` sono tutte variabili locali: nascono con la chiamata e scompaiono con essa. `operazioni_eseguite` invece è globale e persiste tra una chiamata e l'altra, tenendo memoria dell'attività complessiva.

---

## Conclusione: Il Giusto Equilibrio tra Autonomia e Comunicazione

Abbiamo percorso un arco completo: dalla distinzione terminologica tra parametri e argomenti, ai tre modi di passarli (posizionale, keyword, misto), fino ai valori di default che rendono certi argomenti facoltativi. Poi ci siamo addentrati nel concetto di scope, scoprendo che ogni funzione vive in un proprio spazio isolato, può leggere il mondo esterno, ma non lo modifica per impostazione predefinita. Il fenomeno del name hiding ci ha mostrato cosa succede quando due mondi usano lo stesso nome. Infine, la parola chiave `global` ci ha dato la chiave per aprire quella porta, con la raccomandazione di farlo solo quando davvero necessario.

Questi meccanismi non sono capricci del linguaggio: sono stati progettati per rendere il codice prevedibile. Una funzione che non tocca nulla al di fuori di sé stessa è come un ingranaggio preciso: puoi sostituirla, testarla, spostarla senza sorprese. Più una funzione dipende e modifica lo stato globale, meno diventa affidabile come mattone riutilizzabile.

Nella prossima sezione (4.3) entreremo nel mondo delle eccezioni, scoprendo come Python classifica gli errori in una gerarchia strutturata e come possiamo intercettarli prima che facciano danni. Ma la solidità con cui avete capito lo scope vi sarà subito utile: le eccezioni, come le variabili, hanno regole precise su dove "vivono" e come si propagano attraverso i confini tra funzioni.
