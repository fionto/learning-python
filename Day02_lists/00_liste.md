# Liste in Python - Riepilogo Completo

## Introduzione alle Liste

Le liste sono uno dei tipi di dati più versatili e utilizzati in Python. Rappresentano collezioni ordinate di elementi, modificabili e capaci di contenere valori di qualsiasi tipo. A differenza delle stringhe, che sono immutabili, le liste possono essere modificate dopo la loro creazione, rendendole strumenti potenti per gestire insiemi di dati che cambiano durante l'esecuzione del programma.

## Concetti Fondamentali

### Creazione e Accesso

Le liste si creano usando le parentesi quadre e si può accedere ai loro elementi tramite indicizzazione. Python usa indicizzazione a base zero, quindi il primo elemento ha indice 0. È possibile anche usare indici negativi per accedere agli elementi partendo dalla fine della lista, dove -1 rappresenta l'ultimo elemento.
```python
nomi = ['Leonardo', 'Michelangelo', 'Donatello', 'Raffaello']
primo = nomi[0]      # 'Leonardo'
ultimo = nomi[-1]    # 'Raffaello'
```

### Mutabilità delle Liste

La caratteristica distintiva delle liste rispetto alle stringhe è la loro mutabilità. Quando assegni una lista esistente a una nuova variabile, non stai creando una copia ma un alias che punta allo stesso oggetto in memoria. Qualsiasi modifica effettuata tramite un alias si riflette su tutti gli altri alias della stessa lista.
```python
lista_uno = ['Francia', 'Spagna', 'Italia']
lista_due = lista_uno  # Questo è un alias, non una copia
lista_uno[0] = 'Germania'
# Ora anche lista_due[0] è 'Germania'
```

Questo comportamento contrasta con le stringhe, che essendo immutabili creano nuovi oggetti quando riassegnate. Comprendere questa differenza è cruciale per evitare bug difficili da individuare nei tuoi programmi.

## Metodi per Aggiungere Elementi

### append()

Il metodo append aggiunge un singolo elemento alla fine della lista. Questo metodo modifica la lista originale e non restituisce nulla, quindi non va assegnato a una variabile. È il modo più comune e diretto per far crescere una lista durante l'esecuzione del programma.
```python
libri = ['1984', 'Fight Club']
libri.append('Fiori per Algernon')
# libri è ora ['1984', 'Fight Club', 'Fiori per Algernon']
```

### insert()

Il metodo insert permette di aggiungere un elemento in una posizione specifica, specificando l'indice desiderato come primo argomento. Gli elementi esistenti vengono spostati verso destra per fare spazio al nuovo elemento.
```python
playlist = ['Let It Be', 'Hey Jude']
playlist.insert(0, 'Yesterday')  # Inserisce all'inizio
# playlist è ora ['Yesterday', 'Let It Be', 'Hey Jude']
```

### extend()

Sebbene non presente negli esercizi svolti, extend è utile quando devi aggiungere più elementi contemporaneamente da un'altra lista. A differenza di append, che aggiungerebbe l'intera lista come singolo elemento, extend aggiunge ogni elemento individualmente.
```python
lista = [1, 2]
lista.extend([3, 4])  # lista è ora [1, 2, 3, 4]
lista.append([5, 6])  # lista è ora [1, 2, 3, 4, [5, 6]]
```

## Metodi per Rimuovere Elementi

### del

L'istruzione del rimuove un elemento dalla lista specificando il suo indice. Questo è particolarmente utile quando conosci la posizione dell'elemento che vuoi eliminare ma non necessariamente il suo valore.
```python
libri = ['Cuori in Atlantide', 'Fight Club', 'Huckleberry Finn']
del libri[0]  # Rimuove il primo elemento
# libri è ora ['Fight Club', 'Huckleberry Finn']
```

### pop()

Il metodo pop rimuove e restituisce un elemento dalla lista. Se chiamato senza argomenti, rimuove e restituisce l'ultimo elemento. Se gli passi un indice, rimuove e restituisce l'elemento in quella posizione. Questo metodo è utile quando vuoi sia rimuovere che utilizzare l'elemento rimosso.
```python
persone = ['Leonardo', 'Michelangelo', 'Raffaello', 'Donatello']
servito = persone.pop(0)  # Rimuove e salva il primo elemento
# servito è 'Leonardo', persone è ora ['Michelangelo', 'Raffaello', 'Donatello']

ultimo = persone.pop()  # Rimuove l'ultimo elemento
# ultimo è 'Donatello'
```

### remove()

Il metodo remove elimina la prima occorrenza di un valore specifico dalla lista. A differenza di del e pop che operano per indice, remove cerca il valore specificato e lo rimuove. Se il valore non esiste nella lista, Python genera un errore.
```python
persone = ['Leonardo', 'Michelangelo', 'Raffaello', 'Donatello']
persone.remove('Raffaello')
# persone è ora ['Leonardo', 'Michelangelo', 'Donatello']
```

### clear()

Il metodo clear svuota completamente la lista, rimuovendo tutti gli elementi. La lista continua a esistere ma diventa vuota. Questo è più efficiente e leggibile rispetto a riassegnare una nuova lista vuota.
```python
libri = ['1984', 'Fight Club', 'Le Rane']
libri.clear()
# libri è ora []
```

## Metodi per Ordinare e Invertire

### sort()

Il metodo sort ordina gli elementi della lista in posizione, modificando la lista originale. Per impostazione predefinita ordina in modo crescente per numeri e alfabetico per stringhe. Accetta parametri opzionali come reverse=True per ordinamento decrescente.
```python
temperature = [22, 18, 25, 19]
temperature.sort()
# temperature è ora [18, 19, 22, 25]
```

### sorted()

La funzione sorted restituisce una nuova lista ordinata senza modificare l'originale. Questo è utile quando vuoi mantenere l'ordine originale della lista per altri scopi.
```python
giochi = ['Zelda', 'Mario', 'Tetris']
giochi_ordinati = sorted(giochi)
# giochi rimane invariato, giochi_ordinati è ['Mario', 'Tetris', 'Zelda']
```

### reverse()

Il metodo reverse inverte l'ordine degli elementi nella lista in posizione. Non ordina la lista, semplicemente ribalta la sequenza esistente.
```python
giochi = ['Zelda', 'Mario', 'Tetris']
giochi.reverse()
# giochi è ora ['Tetris', 'Mario', 'Zelda']
```

### reversed()

La funzione reversed restituisce un iteratore che attraversa la lista al contrario senza modificarla. Per ottenere una nuova lista è necessario convertire il risultato usando list().
```python
playlist = ['Yesterday', 'Let It Be', 'Hey Jude']
playlist_invertita = list(reversed(playlist))
# playlist rimane invariato, playlist_invertita è ['Hey Jude', 'Let It Be', 'Yesterday']
```

## Altri Metodi e Funzioni Utili

### len()

La funzione len restituisce il numero di elementi in una lista. Questo è fondamentale per molte operazioni, come calcolare l'indice centrale o verificare se una lista è vuota.
```python
nomi = ['Leonardo', 'Michelangelo', 'Donatello', 'Raffaello']
numero_elementi = len(nomi)  # 4
```

### count()

Il metodo count restituisce il numero di volte che un valore specifico appare nella lista. Questo è utile per verificare la presenza e la frequenza di elementi duplicati.
```python
numeri = [1, 2, 3, 2, 4, 2]
occorrenze = numeri.count(2)  # 3
```

### index()

Il metodo index restituisce l'indice della prima occorrenza di un valore specificato. Se il valore non esiste nella lista, Python genera un errore. Puoi specificare opzionalmente dove iniziare e terminare la ricerca.
```python
temperature = [18, 19, 22, 25, 35]
posizione_massima = temperature.index(35)  # 4
```

### copy()

Il metodo copy crea una copia superficiale della lista. Questa nuova lista è un oggetto separato in memoria, quindi le modifiche a una non influenzano l'altra. Questo risolve il problema dell'aliasing descritto in precedenza.
```python
originale = ['Leonardo', 'Michelangelo', 'Donatello']
copia = originale.copy()
originale.append('Raffaello')
# originale è ['Leonardo', 'Michelangelo', 'Donatello', 'Raffaello']
# copia rimane ['Leonardo', 'Michelangelo', 'Donatello']
```

### max() e min()

Le funzioni max e min restituiscono rispettivamente il valore massimo e minimo in una lista. Per numeri questo è intuitivo, per stringhe l'ordine è alfabetico.
```python
temperature = [18, 22, 19, 25, 35]
massima = max(temperature)  # 35
minima = min(temperature)   # 18
```

## Funzione print() con Multipli Argomenti

La funzione print può accettare più oggetti separati da virgola e li stamperà sulla stessa riga separandoli automaticamente con uno spazio. Questo è utile per creare output leggibili combinando testo descrittivo e valori di variabili.
```python
giochi = ['Zelda', 'Mario', 'Tetris']
print("Classifica iniziale:", giochi)
# Output: Classifica iniziale: ['Zelda', 'Mario', 'Tetris']
```

La sintassi completa di print include parametri opzionali come sep per il separatore tra oggetti ed end per il carattere finale, ma nella maggior parte dei casi i valori predefiniti sono sufficienti.

## Pattern e Best Practices

### Indicizzazione Negativa

Python permette di usare indici negativi per accedere agli elementi dalla fine della lista. L'indice -1 rappresenta l'ultimo elemento, -2 il penultimo e così via. Questo è particolarmente utile quando non conosci la lunghezza della lista o quando lavori frequentemente con gli ultimi elementi.

### Modifica in Posizione vs Creazione di Nuove Liste

Alcuni metodi come sort e reverse modificano la lista originale e non restituiscono nulla. Altri come sorted e reversed creano nuove liste lasciando l'originale intatta. Comprendere questa distinzione è fondamentale per evitare errori comuni come scrivere lista = lista.sort(), che assegnerebbe None alla variabile.

### Salvare Valori Rimossi

Quando usi pop, il valore rimosso viene restituito e può essere salvato in una variabile per uso futuro. Questo pattern è comune quando stai simulando strutture dati come code o stack.

### Calcolo dell'Indice Centrale

Per trovare l'indice centrale di una lista puoi usare la divisione intera. Il doppio slash esegue una divisione che restituisce solo la parte intera del risultato, scartando eventuali decimali.
```python
lista = [1, 2, 3, 4, 5]
indice_centrale = len(lista) // 2  # 2
```

## Differenze Chiave: Liste vs Stringhe

Sebbene liste e stringhe condividano alcune caratteristiche come l'indicizzazione e la capacità di essere iterate, differiscono fondamentalmente nella mutabilità. Le stringhe sono immutabili, quindi operazioni che sembrano modificarle in realtà creano nuove stringhe. Le liste sono mutabili e possono essere modificate direttamente. Questa differenza influenza profondamente come usi questi tipi di dati nei tuoi programmi e come gestisci le assegnazioni di variabili.

## Conclusione

Le liste rappresentano uno strumento fondamentale nella programmazione Python, offrendo flessibilità e potenza nella gestione di collezioni di dati. Comprendere la loro natura mutabile, i metodi disponibili e i pattern comuni ti permette di scrivere codice più efficiente ed espressivo. La pratica con esercizi che combinano diversi metodi e operazioni consolida queste competenze e prepara per concetti più avanzati come le comprehension e l'iterazione che incontrerai nei prossimi capitoli.