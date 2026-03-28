# Capitolo 3: Sezione 3.2 — Le Tuple: Dati che Non Si Toccano

## Introduzione: Quando Immutabilità è una Virtù

Immaginate di acquistare un biglietto del treno. Sulla carta sono stampati la città di partenza, la destinazione, l'orario e il numero del posto. Una volta emesso, nessuno può cambiare quei dati: il biglietto è un documento fisso, che racconta qualcosa di definitivo. Se l'orario cambia, la compagnia ferroviaria non vi modifica il biglietto in mano; vi emette uno nuovo. Il vecchio rimane immutato nella vostra tasca.

Le **tuple** in Python funzionano esattamente così. Sono sequenze ordinate di valori, molto simili alle liste che abbiamo incontrato nella sezione precedente, ma con una differenza fondamentale: una volta creata una tupla, non la si può modificare. Non si possono aggiungere elementi, non si possono rimuovere, non si possono sostituire. È un contenitore sigillato.

Questa proprietà, che di primo acchito potrebbe sembrare una limitazione, si rivela invece uno strumento potente e preciso. Come vedremo nel corso di questo capitolo, ci sono molte situazioni in cui voler garantire che certi dati rimangano intatti non è un vincolo, ma una scelta di progetto deliberata e saggia. Capire quando preferire una tupla a una lista è uno dei primi passi verso un codice Python più pulito e corretto.

## Costruire una Tupla

La sintassi di costruzione di una tupla è simile a quella delle liste, con una differenza immediata: si usano le parentesi tonde `()` al posto delle parentesi quadre `[]`.

```python
# Una tupla con tre elementi
coordinate = (48.8566, 2.3522, "Parigi")

# Una tupla di nomi
giorni_lavoro = ("lunedì", "martedì", "mercoledì", "giovedì", "venerdì")

# Stampiamo per verificare
print(coordinate)     # Output: (48.8566, 2.3522, 'Parigi')
print(giorni_lavoro)  # Output: ('lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì')
```

Come si vede, una tupla può contenere elementi di tipo diverso mescolati insieme: numeri interi, numeri in virgola mobile, stringhe. Esattamente come una lista.

Esiste anche una forma alternativa di costruzione, senza parentesi, in cui gli elementi sono semplicemente separati da virgole. Python riconosce la virgola come il vero segnale che si sta costruendo una tupla, non le parentesi in sé:

```python
# Tupla senza parentesi esplicite (la virgola è il segnale)
punto = 3, 7
print(punto)        # Output: (3, 7)
print(type(punto))  # Output: <class 'tuple'>
```

Questo comportamento può sorprendere chi viene da altri linguaggi, quindi è bene tenerlo a mente. Scrivere `x = 1, 2, 3` in Python non è un errore: crea una tupla `(1, 2, 3)` e la assegna a `x`.

C'è però un caso speciale che merita attenzione: la tupla con un solo elemento. Intuitivamente si potrebbe scrivere `(42)`, ma questo non crea una tupla: Python lo interpreta semplicemente come il numero `42` racchiuso in parentesi, esattamente come in matematica. Per creare una tupla da un solo elemento, la virgola finale è obbligatoria:

```python
# Questo NON è una tupla: è solo il numero 42
non_tupla = (42)
print(type(non_tupla))  # Output: <class 'int'>

# Questo È una tupla con un solo elemento
tupla_singola = (42,)
print(type(tupla_singola))  # Output: <class 'tuple'>
print(tupla_singola)        # Output: (42,)
```

È possibile costruire anche una tupla vuota, scrivendo semplicemente `()`, ma nella pratica le tuple vuote sono rare: una sequenza vuota che non può essere modificata ha scarsa utilità.

## Indicizzazione e Slicing

Per accedere agli elementi di una tupla si usa la stessa notazione a indice delle liste, con le parentesi quadre e un numero che indica la posizione. Gli indici partono da zero, e Python supporta anche gli indici negativi per contare dalla fine:

```python
colori = ("rosso", "verde", "blu", "giallo")

# Accesso tramite indice positivo
print(colori[0])   # Output: rosso
print(colori[2])   # Output: blu

# Accesso tramite indice negativo (dalla fine)
print(colori[-1])  # Output: giallo
print(colori[-2])  # Output: blu

# Lunghezza della tupla
print(len(colori)) # Output: 4
```

Lo slicing funziona esattamente come per le liste: si specifica un intervallo con la sintassi `tupla[inizio:fine]`, dove `inizio` è incluso e `fine` è escluso. Il risultato di uno slice su una tupla è ancora una tupla.

```python
numeri = (10, 20, 30, 40, 50, 60)

# Prendere i primi tre elementi
print(numeri[0:3])  # Output: (10, 20, 30)

# Prendere dalla terza posizione in poi
print(numeri[2:])   # Output: (30, 40, 50, 60)

# Prendere gli ultimi due elementi
print(numeri[-2:])  # Output: (50, 60)

# Invertire la tupla con lo step -1
print(numeri[::-1]) # Output: (60, 50, 40, 30, 20, 10)
```

L'operatore `in` funziona anche con le tuple e permette di verificare se un valore è presente nella sequenza:

```python
stagioni = ("primavera", "estate", "autunno", "inverno")

print("estate" in stagioni)    # Output: True
print("ottobre" in stagioni)   # Output: False
```

## L'Immutabilità: La Caratteristica Fondamentale

Torniamo al concetto che più distingue le tuple. Una volta costruita una tupla, nessuna operazione può modificarne il contenuto. Questo significa che non esiste alcun metodo per aggiungere, rimuovere o sostituire elementi. Se si tenta di farlo, Python segnala un errore:

```python
punto = (10, 20, 30)

# Tentativo di modificare un elemento: genera TypeError
# punto[0] = 99  # Errore: 'tuple' object does not support item assignment

# Tentativo di cancellare un elemento: genera TypeError
# del punto[1]   # Errore: 'tuple' object doesn't support item deletion
```

Questo errore, il `TypeError`, è Python che ci ricorda che stiamo violando il contratto implicito della tupla: il dato è immutabile, punto. Non esiste un workaround per modificarla direttamente; l'unica operazione consentita è crearne una nuova con i valori desiderati.

Vale la pena sottolineare una sottigliezza importante: l'immutabilità si applica alla struttura della tupla, cioè agli elementi che essa contiene direttamente. Se uno di quegli elementi è un oggetto mutabile, come una lista, l'oggetto in sé può essere modificato:

```python
# Una tupla che contiene una lista
dati = (1, 2, [10, 20, 30])

# Non possiamo sostituire la lista con qualcos'altro
# dati[2] = [99, 88]  # Errore: 'tuple' object does not support item assignment

# Ma possiamo modificare il contenuto della lista interna
dati[2].append(40)
print(dati)  # Output: (1, 2, [10, 20, 30, 40])
```

Questo comportamento può sembrare contraddittorio, ma è perfettamente coerente: la tupla non può cambiare i suoi "slot", cioè i riferimenti agli oggetti che contiene. Il fatto che quell'oggetto al suo interno muti è un'altra questione. L'identità dell'elemento (il riferimento in memoria) rimane la stessa; è il contenuto dell'oggetto puntato a cambiare.

## Tuple vs. Liste: Quando Usare L'Una o L'Altra

Sapere che le tuple esistono non basta: bisogna capire in quali situazioni preferirle alle liste. Non si tratta di una preferenza estetica, ma di una scelta che riflette l'intenzione del programmatore e che ha conseguenze concrete sulla correttezza e sulla chiarezza del codice.

### I Dati Concettualmente Fissi

La regola d'oro è semplice: se la raccolta di valori che state rappresentando ha un significato naturalmente fisso, usate una tupla. Pensate a coordinate geografiche (latitudine e longitudine), a una data (giorno, mese, anno), a una dimensione (larghezza e altezza), ai colori RGB di un punto. In tutti questi casi, non ha senso "aggiungere" o "rimuovere" valori: una coordinata è composta esattamente da due valori, e un colore RGB da tre. Una lista sarebbe semanticamente fuorviante, perché suggerisce una struttura aperta alla modifica.

```python
# Una tupla è la scelta giusta per una coordinata: non si "aggiungono" latitudini
origine = (41.9028, 12.4964)  # Roma

# Un colore RGB ha esattamente tre componenti: tupla perfetta
rosso_puro = (255, 0, 0)
```

### La Protezione contro Modifiche Accidentali

In un programma complesso, con molte funzioni e molti moduli, è facile che un dato venga passato da un punto all'altro. Se quel dato è una lista, chiunque può modificarla senza volerlo. Se è una tupla, Python garantisce che il suo contenuto arrivi intatto a destinazione. Usare una tupla è un modo per dire al lettore del codice (e a Python stesso): "questi valori non devono cambiare".

```python
# Passare una lista: nulla impedisce alla funzione di modificarla
# Passare una tupla: il contratto di immutabilità è garantito dal linguaggio
def stampa_punto(p):
    print(f"x={p[0]}, y={p[1]}")

punto = (5, 8)
stampa_punto(punto)  # Output: x=5, y=8
# La funzione non può modificare 'punto', anche se volesse
```

### Il Vantaggio di Prestazioni e Memoria

Le tuple sono leggermente più efficienti delle liste, sia in termini di memoria occupata che di velocità di alcune operazioni. Python riesce a ottimizzare meglio le tuple proprio perché sa che non cambieranno mai. La differenza è spesso trascurabile in programmi piccoli, ma diventa rilevante quando si lavora con milioni di sequenze in cicli intensivi.

```python
import sys

# Le tuple occupano meno memoria delle liste equivalenti
lista  = [1, 2, 3, 4, 5]
tupla  = (1, 2, 3, 4, 5)

print(sys.getsizeof(lista))   # Output: tipicamente 120 byte
print(sys.getsizeof(tupla))   # Output: tipicamente 80 byte
```

### Le Tuple come Chiavi dei Dizionari

C'è un caso d'uso in cui le tuple sono l'unica scelta possibile: le chiavi dei dizionari. I dizionari Python richiedono che le chiavi siano **hashable**, cioè immutabili e con un valore di hash calcolabile. Le liste non lo sono, quindi non possono essere usate come chiavi. Le tuple sì.

```python
# Usare coordinate come chiave di un dizionario: solo le tuple lo consentono
mappa_citta = {
    (41.9028, 12.4964): "Roma",
    (45.4654, 9.1859):  "Milano",
    (40.8518, 14.2681): "Napoli"
}

# Ricerca tramite tupla-chiave
print(mappa_citta[(41.9028, 12.4964)])  # Output: Roma

# Tentativo con lista: genera TypeError
# mappa_errata = {[41.9028, 12.4964]: "Roma"}  # Errore: unhashable type: 'list'
```

In sintesi: scegliete la lista quando lavorate con una collezione che può crescere, ridursi o variare nel tempo. Scegliete la tupla quando i valori rappresentano un'entità concettualmente atomica e fissa, o quando volete proteggere i dati da modifiche accidentali.

## Nesting: Tuple dentro Liste, Liste dentro Tuple

Python permette di annidare qualsiasi tipo di sequenza all'interno di un'altra. Una tupla può contenere liste, e una lista può contenere tuple. Queste strutture composite sono molto utili per rappresentare dati del mondo reale con una gerarchia naturale.

### Tuple dentro Liste

Immaginate di voler memorizzare i risultati di una gara podistica: per ogni partecipante avete nome, cognome e tempo. I dati di ciascun partecipante sono fissi (un'entità discreta), quindi una tupla è la scelta giusta. Ma l'insieme dei partecipanti può variare, quindi si usa una lista:

```python
# Una lista di tuple: ogni tupla è un record immutabile
risultati = [
    ("Rossi",    "Marco",  "00:42:15"),
    ("Bianchi",  "Sara",   "00:43:08"),
    ("Verdi",    "Luca",   "00:45:30"),
    ("Ferrara",  "Elena",  "00:47:55"),
]

# Iterare sulla lista e accedere agli elementi di ogni tupla
for cognome, nome, tempo in risultati:
    print(f"{nome} {cognome}: {tempo}")

# Output:
# Marco Rossi: 00:42:15
# Sara Bianchi: 00:43:08
# Luca Verdi: 00:45:30
# Elena Ferrara: 00:47:55
```

La notazione `for cognome, nome, tempo in risultati` è particolarmente elegante: Python smonta automaticamente ciascuna tupla assegnando ogni valore alla variabile corrispondente. Questo meccanismo si chiama **tuple unpacking** (scompattamento) ed è uno degli strumenti più espressivi della sintassi Python.

L'unpacking si può usare anche al di fuori dei cicli:

```python
punto = (10, 20, 30)

# Scompattamento in tre variabili
x, y, z = punto

print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30
```

### Liste dentro Tuple

Il caso inverso, una lista all'interno di una tupla, è utile quando si vuole che la struttura contenitore sia fissa, ma alcuni dei suoi "slot" debbano poter accogliere contenuti variabili:

```python
# Una tupla che descrive un corso: titolo fisso, studenti variabili
corso_python = ("Introduzione a Python", ["Alice", "Bruno", "Carla"])

# Il titolo non cambia
titolo   = corso_python[0]
studenti = corso_python[1]

print(titolo)     # Output: Introduzione a Python
print(studenti)   # Output: ['Alice', 'Bruno', 'Carla']

# Possiamo aggiungere uno studente alla lista interna
studenti.append("Davide")
print(corso_python)
# Output: ('Introduzione a Python', ['Alice', 'Bruno', 'Carla', 'Davide'])
```

Come si vede, la lista degli studenti è modificabile perché è un oggetto di tipo lista, e l'immutabilità della tupla non si estende al contenuto degli oggetti mutabili che essa ospita. Questo è il comportamento coerente che abbiamo già discusso nella sezione sull'immutabilità.

### Tuple di Tuple: Una Griglia di Dati

È possibile costruire anche strutture interamente composte da tuple annidate, utili quando si vogliono rappresentare matrici o tabelle di dati che non devono essere modificati:

```python
# Una tabella immutabile di dati climatici (mese, temp_media, precipitazioni_mm)
dati_climatici = (
    ("Gennaio",  3.5,  72),
    ("Febbraio", 5.1,  60),
    ("Marzo",    9.8,  65),
    ("Aprile",  14.2,  78),
)

# Accesso a un elemento specifico: prima riga, secondo campo (temp_media)
print(dati_climatici[0][1])  # Output: 3.5

# Iterazione sull'intera struttura
for mese, temp, pioggia in dati_climatici:
    print(f"{mese}: {temp}°C, {pioggia} mm")

# Output:
# Gennaio: 3.5°C, 72 mm
# Febbraio: 5.1°C, 60 mm
# Marzo: 9.8°C, 65 mm
# Aprile: 14.2°C, 78 mm
```

La sintassi `tupla[i][j]` accede all'elemento in posizione `j` della riga `i`, esattamente come per le liste bidimensionali. Il concetto di indicizzazione multipla è universale in Python per le strutture annidate.

## Conclusione: Scegliere il Contenitore Giusto

Abbiamo percorso l'intero territorio delle tuple: come si costruiscono, come si accede ai loro elementi, perché sono immutabili e in quali circostanze questa immutabilità è un vantaggio, non uno svantaggio.

La distinzione tra tuple e liste non è tecnica ma semantica: riflette la differenza tra dati che rappresentano un'entità definita e stabile (la tupla) e dati che rappresentano una collezione aperta e in evoluzione (la lista). Scegliere il tipo giusto per ogni situazione è un segno di codice ben pensato; chi legge il vostro programma capisce immediatamente, dalla scelta del contenitore, se quella sequenza è destinata a cambiare o no.

Le tuple torneranno utili anche nei capitoli successivi, in particolare quando studieremo i dizionari: come abbiamo visto, le tuple sono l'unico tipo di sequenza che può fungere da chiave, grazie alla loro natura hashable. Questo le rende insostituibili in certi contesti, non semplicemente una variante delle liste.

Nel prossimo capitolo affronteremo i **dizionari**: strutture dati che associano una chiave a un valore, aprendo la strada a modelli di dati ancora più espressivi e flessibili.
