# Capitolo 2: Sezione 2.2 — Iterazioni e Cicli: Il Potere della Ripetizione

## Introduzione: La Lista della Spesa e il Calendario

Immaginate di dover avvisare ogni persona della vostra famiglia che domani c'è un pranzo importante. Potreste inviare i messaggi uno a uno, aprendo la rubrica, cercando il nome, scrivendo il testo, inviando, poi ricominciare dall'inizio per il prossimo contatto. L'operazione è tediosa ma fattibile se i destinatari sono tre o quattro. Ma se fossero trecento? O tremila?

Nella vita reale, in questi casi, adottiamo un approccio diverso: definiamo l'azione da compiere una volta sola ("inviare il messaggio a questa persona") e poi la ripetiamo sistematicamente per ogni elemento di un elenco. Non riscriviamo la procedura trecento volte: la eseguiamo trecento volte.

Questo è esattamente il problema che i **cicli** risolvono in programmazione. Senza di essi, per stampare i numeri da 1 a 100 dovreste scrivere cento istruzioni `print` separate. Con un ciclo, ne scrivete una sola e dite all'interprete quante volte ripeterla. I cicli sono uno dei costrutti più potenti di qualsiasi linguaggio di programmazione, e Python ne offre due forme principali: `while` e `for`, ciascuna adatta a situazioni diverse.

Questa dispensa assume che conosciate le variabili, gli operatori di confronto, gli operatori logici e le istruzioni condizionali della sezione 2.1. I cicli, in fondo, sono decisioni che si ripetono: a ogni giro, il programma valuta una condizione e decide se continuare oppure fermarsi.

---

## Il Ciclo `while`: Ripetere Finché Vale una Condizione

Il ciclo `while` è la forma di ripetizione più diretta. La sua logica è identica a quella di una frase della vita quotidiana: "finché il semaforo è rosso, aspetta". Si continua a eseguire il blocco di codice per tutto il tempo in cui la condizione specificata rimane vera. Non appena diventa falsa, il ciclo termina e l'esecuzione prosegue con la riga successiva.

La sintassi è la seguente:

```python
while condizione:
    # blocco di codice da ripetere
```

Come per l'`if`, la condizione viene valutata prima di ogni iterazione. Se è già falsa alla prima valutazione, il blocco non viene mai eseguito. Se rimane vera per sempre, il programma non terminerà mai: questo si chiama **ciclo infinito**, ed è uno degli errori più comuni da evitare.

Un esempio semplice: stampare i numeri da 1 a 5.

```python
# Contare da 1 a 5 con while
contatore = 1

while contatore <= 5:
    print(contatore)
    contatore += 1  # aggiornare il contatore è essenziale

# Output:
# 1
# 2
# 3
# 4
# 5
```

In questo esempio, `contatore` parte da 1 e viene incrementato di 1 a ogni iterazione. Quando raggiunge 6, la condizione `contatore <= 5` diventa falsa e il ciclo termina. Se dimenticaste la riga `contatore += 1`, il contatore non cambierebbe mai e il ciclo girerebbe all'infinito stampando "1" senza fermarsi. Ogni ciclo `while` che modifica delle variabili deve assicurarsi che prima o poi la condizione diventi falsa.

Il `while` è particolarmente adatto quando non sapete in anticipo quante volte ripetere il blocco: la ripetizione continua finché l'utente non inserisce un dato valido, finché non si raggiunge una certa soglia calcolata dinamicamente, finché un sensore non segnala una condizione.

```python
# Chiedere un numero positivo fino a ottenerne uno valido
numero = -1

while numero <= 0:
    numero = int(input("Inserisci un numero positivo: "))

print(f"Hai inserito: {numero}")
```

Questo ciclo si ripete finché l'utente non fornisce un valore maggiore di zero. Potrebbe girare una volta sola o dieci volte: dipende dall'utente, non dal programmatore.

---

## L'Istruzione `pass`: Un Blocco Volutamente Vuoto

Prima di addentrarci nel ciclo `for`, vale la pena conoscere una piccola parola chiave che compare spesso insieme ai cicli: `pass`. In Python, un blocco di codice non può essere vuoto: se scrivete un `while` o un `for` senza nessuna istruzione al suo interno, otterrete un errore di sintassi. Ma a volte, durante la scrittura di un programma, avete bisogno di definire la struttura prima di riempirla.

`pass` è un'istruzione che non fa nulla: è un segnaposto legale che soddisfa l'obbligo sintattico di avere un corpo nel blocco.

```python
# Ciclo che per ora non fa nulla (struttura da completare)
for i in range(5):
    pass  # da implementare in seguito

# Nessun output: il ciclo gira 5 volte e non fa nulla
```

Vedrete `pass` usato anche all'interno di funzioni e classi ancora da implementare. Non ha effetto sul comportamento del programma: serve solo a rendere il codice sintatticamente valido mentre lavorate sulla struttura.

---

## Il Ciclo `for` e `range()`: Ripetere un Numero Noto di Volte

Il ciclo `for` in Python funziona in modo diverso da come potreste conoscerlo in altri linguaggi. Non è un semplice contatore che va da A a B: è uno strumento per **scorrere una sequenza di valori**, uno alla volta. A ogni iterazione, la variabile di ciclo assume il valore successivo della sequenza.

La forma base è:

```python
for variabile in sequenza:
    # blocco da eseguire per ogni elemento
```

La sequenza può essere qualsiasi cosa iterabile: una lista, una stringa, oppure, nel caso più comune a questo livello, un oggetto prodotto dalla funzione `range()`.

`range()` genera una sequenza di numeri interi. Può essere usata in tre modi distinti:

`range(stop)` genera i numeri da 0 (incluso) fino a `stop` (escluso):

```python
# Stampare i numeri da 0 a 4
for i in range(5):
    print(i)
# Output: 0  1  2  3  4
```

`range(start, stop)` genera i numeri da `start` (incluso) fino a `stop` (escluso):

```python
# Stampare i numeri da 1 a 5
for i in range(1, 6):
    print(i)
# Output: 1  2  3  4  5
```

`range(start, stop, step)` genera i numeri da `start` a `stop` con un passo `step`. Il passo può anche essere negativo, per contare al contrario:

```python
# Numeri pari da 0 a 8
for i in range(0, 10, 2):
    print(i)
# Output: 0  2  4  6  8

# Conto alla rovescia da 5 a 1
for i in range(5, 0, -1):
    print(i)
# Output: 5  4  3  2  1
```

Una cosa importante da tenere a mente: `range()` non genera una lista di numeri in memoria, ma un oggetto che li produce uno alla volta su richiesta. Questo lo rende molto efficiente anche con valori grandissimi.

### Iterare su Sequenze con `in`

La parola chiave `in` nel ciclo `for` non si limita a lavorare con `range()`. Può scorrere qualsiasi sequenza: per esempio, i caratteri di una stringa, uno alla volta.

```python
# Scorrere i caratteri di una parola
parola = "Python"

for carattere in parola:
    print(carattere)
# Output:
# P
# y
# t
# h
# o
# n
```

Il ciclo assegna a `carattere` il primo carattere della stringa, esegue il blocco, poi passa al secondo, e così via fino all'ultimo. Le sequenze più ricche (liste, tuple, dizionari) verranno esplorate nelle sezioni 3.1, 3.2 e 3.3; qui è sufficiente sapere che `for` è costruito per lavorare con qualsiasi tipo di sequenza in modo naturale.

---

## `break`: Uscire dal Ciclo Prima del Tempo

A volte durante una ricerca potete trovare quello che cercate prima di aver esaminato tutti gli elementi. Continuare a cercare dopo aver trovato la risposta sarebbe uno spreco. In questi casi, `break` permette di uscire immediatamente dal ciclo, saltando tutte le iterazioni rimanenti.

```python
# Cercare il primo numero divisibile per 7 in un intervallo
for numero in range(1, 50):
    if numero % 7 == 0:
        print(f"Trovato: {numero}")
        break  # usciamo subito, non serve continuare

# Output: Trovato: 7
```

Senza il `break`, il ciclo continuerebbe e stamperebbe tutti i multipli di 7 fino a 49. Con il `break`, si ferma al primo risultato utile.

`break` funziona allo stesso modo anche nel ciclo `while`:

```python
# Leggere input finché l'utente non scrive "fine"
while True:  # ciclo potenzialmente infinito
    testo = input("Scrivi qualcosa (o 'fine' per uscire): ")
    if testo == "fine":
        break
    print(f"Hai scritto: {testo}")

print("Arrivederci!")
```

L'idioma `while True:` combinato con `break` è molto usato in Python quando la condizione di uscita dipende da qualcosa che accade all'interno del ciclo, non da una variabile valutabile prima di entrare. Il ciclo "non ha fine" in senso teorico, ma il `break` garantisce che si fermi nel momento giusto.

---

## `continue`: Saltare un'Iterazione e Proseguire

Mentre `break` interrompe completamente il ciclo, `continue` interrompe solo l'iterazione corrente e passa direttamente alla successiva, ricominciando dalla valutazione della condizione (nel `while`) o dal prossimo elemento (nel `for`).

Pensatelo come un "salta questo, vai avanti": il resto delle istruzioni nell'iterazione corrente viene ignorato, ma il ciclo non termina.

```python
# Stampare solo i numeri dispari tra 1 e 10
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # numero pari: salta questa iterazione
    print(numero)

# Output: 1  3  5  7  9
```

Quando `numero` è pari, `continue` viene eseguito e la `print` viene saltata. Quando è dispari, `continue` non viene raggiunto e la `print` viene eseguita normalmente.

Un esempio con `while`:

```python
# Sommare solo i numeri positivi inseriti dall'utente (0 per terminare)
somma = 0
valore = -1

while valore != 0:
    valore = int(input("Inserisci un numero (0 per finire): "))
    if valore < 0:
        continue  # ignoriamo i negativi e chiediamo di nuovo
    somma += valore

print(f"Somma dei valori positivi: {somma}")
```

Qui `continue` salta l'aggiornamento della somma quando il valore inserito è negativo, ma non interrompe il ciclo: si torna subito alla lettura dell'input successivo.

---

## La Clausola `else` nei Cicli

Una caratteristica di Python che sorprende spesso chi viene da altri linguaggi è la possibilità di aggiungere una clausola `else` a un ciclo `while` o `for`. La logica è questa: il blocco `else` viene eseguito quando il ciclo **termina normalmente**, cioè quando la condizione `while` diventa falsa o quando la sequenza del `for` è stata completamente esaurita. Non viene eseguito se il ciclo è stato interrotto da un `break`.

Questo meccanismo è particolarmente utile per le ricerche: potete usarlo per distinguere il caso "ho trovato quello che cercavo" (uscita con `break`) dal caso "ho esaminato tutto senza trovarlo" (uscita naturale, con `else`).

```python
# Cercare un valore in una sequenza
valori = [4, 9, 15, 22, 31]
cercato = 17

for v in valori:
    if v == cercato:
        print(f"Trovato {cercato} nella sequenza")
        break
else:
    # Questo blocco si esegue solo se il for è terminato senza break
    print(f"{cercato} non è presente nella sequenza")

# Output: 17 non è presente nella sequenza
```

Se `cercato` fosse stato 22, il ciclo avrebbe trovato il valore, eseguito il `break`, e il blocco `else` non sarebbe stato raggiunto.

La stessa logica vale per `while-else`:

```python
# Tentare di connettersi a un server, con numero massimo di tentativi
tentativi_rimasti = 3
connesso = False

while tentativi_rimasti > 0:
    # qui ci sarebbe la logica reale di connessione
    # simuliamo sempre un fallimento per l'esempio
    print(f"Tentativo... ({tentativi_rimasti} rimasti)")
    tentativi_rimasti -= 1
else:
    # Si esegue perché il while è terminato naturalmente (non con break)
    print("Impossibile connettersi: tentativi esauriti")

# Output:
# Tentativo... (3 rimasti)
# Tentativo... (2 rimasti)
# Tentativo... (1 rimasti)
# Impossibile connettersi: tentativi esauriti
```

La clausola `else` nei cicli è una delle scelte di design più originali di Python. Non è indispensabile (si può sempre ottenere lo stesso risultato con una variabile booleana di controllo), ma quando il suo uso è appropriato rende il codice più espressivo e leggibile.

---

## Cicli Annidati: Iterazioni dentro Iterazioni

Così come le condizioni possono essere annidate (sezione 2.1), anche i cicli possono contenere altri cicli. Per ogni iterazione del ciclo esterno, il ciclo interno viene eseguito per intero, dall'inizio alla fine.

Pensate alla costruzione di una tabella: per ogni riga (ciclo esterno), dovete riempire tutte le colonne (ciclo interno).

```python
# Tavola pitagorica da 1 a 5
for riga in range(1, 6):
    for colonna in range(1, 6):
        prodotto = riga * colonna
        print(f"{prodotto:4}", end="")  # stampa senza andare a capo
    print()  # va a capo alla fine di ogni riga

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
```

Il ciclo interno gira 5 volte per ogni iterazione del ciclo esterno: in totale, il blocco più interno viene eseguito 25 volte (5 × 5). Con tre livelli di annidamento sarebbero 125 esecuzioni, e così via. È importante tenere a mente questa moltiplicazione quando si lavora con cicli annidati: più sono profondi, più il programma diventa lento per input grandi.

Il `break` in un ciclo annidato interrompe solo il ciclo più interno in cui si trova, non quelli esterni:

```python
# Trovare la prima coppia (i, j) tale che i * j > 20
for i in range(1, 6):
    for j in range(1, 6):
        if i * j > 20:
            print(f"Prima coppia trovata: {i} × {j} = {i*j}")
            break  # esce solo dal ciclo interno (su j)
    # il ciclo esterno (su i) continua

# Output:
# Prima coppia trovata: 5 × 5 = 25
```

Se volessimo uscire da entrambi i cicli simultaneamente, dovremmo usare una variabile booleana di controllo oppure spostare la logica in una funzione con `return`, argomento che affronteremo nella sezione 4.1.

---

## Un Esempio Integrativo: Validazione e Ricerca

Per concludere con un esempio che metta insieme i vari strumenti della sezione, costruiamo un piccolo programma interattivo che chiede all'utente di indovinare un numero segreto, con un massimo di cinque tentativi.

```python
# Gioco "indovina il numero" con massimo 5 tentativi
numero_segreto = 42
tentativi_massimi = 5
trovato = False

for tentativo in range(1, tentativi_massimi + 1):
    risposta = int(input(f"Tentativo {tentativo}/{tentativi_massimi}: "))

    if risposta < numero_segreto:
        print("Troppo basso!")
    elif risposta > numero_segreto:
        print("Troppo alto!")
    else:
        print(f"Bravo! Hai indovinato in {tentativo} tentativo/i.")
        trovato = True
        break
else:
    # Il for è terminato senza break: i tentativi sono esauriti
    print(f"Tentativi esauriti. Il numero era {numero_segreto}.")
```

In questo programma troviamo `for` con `range()` per contare i tentativi, `if-elif-else` per confrontare il valore inserito, `break` per uscire quando il numero è trovato, e la clausola `else` del `for` per gestire il caso di fallimento. Tutti gli strumenti del capitolo lavorano insieme in modo coordinato.

---

## Conclusione: Il Ritmo della Ripetizione

Con i cicli, il vostro repertorio di strumenti per controllare il flusso di un programma è ora completo. Avete imparato a ripetere azioni finché una condizione rimane vera (`while`), a scorrere sequenze di valori uno alla volta (`for`), a generare sequenze numeriche su misura (`range()`), a interrompere un ciclo anticipatamente (`break`), a saltare un'iterazione e continuare (`continue`), e a reagire al tipo di uscita dal ciclo grazie alla clausola `else`.

Questi strumenti, combinati con le decisioni della sezione 2.1, formano la spina dorsale del controllo di flusso in Python. Quasi ogni algoritmo di interesse reale si esprime attraverso una combinazione di condizioni e cicli: ricerche, ordinamenti, calcoli iterativi, interfacce a riga di comando.

La sezione 3 ci porterà a lavorare con le strutture dati: liste, tuple, dizionari e stringhe. Scoprirete che il ciclo `for` acquista nuova potenza quando la sequenza su cui itera non è una serie di numeri generata da `range()`, ma una collezione di dati reali costruita dal programma. Il legame tra cicli e strutture dati è così stretto che molte operazioni sulle liste, ad esempio, si scrivono naturalmente come un `for` che scorre gli elementi uno alla volta.
