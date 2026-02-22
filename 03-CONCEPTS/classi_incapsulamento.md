# L’Incapsulamento in Python  
## Capire cosa significa davvero proteggere un oggetto

Quando si inizia a programmare con le classi, è naturale pensare che servano semplicemente a organizzare meglio il codice. In realtà le classi nascono per rappresentare entità dotate di responsabilità proprie. Un oggetto non è solo un contenitore di dati: è qualcosa che dovrebbe gestire quei dati secondo regole precise.  

Uno dei principi fondamentali della programmazione orientata agli oggetti è l’incapsulamento. Non è soltanto una tecnica, ma un modo di pensare. Significa racchiudere i dati e le regole che li governano all’interno di un confine chiaro, lasciando all’esterno solo ciò che è davvero necessario.

Immagina un oggetto come una piccola macchina. Dall’esterno puoi premere pulsanti e osservare risultati, ma non puoi infilare le mani nel motore per spostare pezzi a caso. Se fosse possibile farlo, la macchina smetterebbe di funzionare correttamente. L’incapsulamento nasce proprio per evitare che questo accada.

Prendiamo un esempio semplice. Supponiamo di avere una classe che rappresenta uno studente.

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []
```

Se creiamo un oggetto:

```python
s = Studente("Marco")
```

possiamo accedere direttamente alla lista dei voti:

```python
s.voti.append(200)
```

Il problema è evidente. Il valore 200 non è un voto valido, ma l’oggetto lo accetta senza alcun controllo. Lo stato interno dell’oggetto è ora incoerente. Abbiamo rotto la sua logica semplicemente perché abbiamo avuto accesso diretto ai suoi dati. Questo accade perché l’attributo è completamente esposto. L’oggetto non ha alcun potere di difendersi.

L’incapsulamento propone un’idea diversa: i dati interni non dovrebbero essere modificati direttamente. Dovrebbero passare attraverso metodi che applicano regole.

In Python non esistono attributi privati nel senso rigido di altri linguaggi, ma esiste una convenzione importante. Se un attributo inizia con un trattino basso, significa che è destinato all’uso interno. Possiamo riscrivere la classe così:

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome
        self._voti = [] # ATTENZIONE all'underscore

    def aggiungi_voto(self, voto):
        if 0 <= voto <= 30:
            self._voti.append(voto)
        else:
            print("Voto non valido")
```

Ora i voti vengono aggiunti solo tramite il metodo previsto. L’oggetto controlla cosa può entrare nel proprio stato interno. Anche se tecnicamente è ancora possibile accedere a `_voti` dall’esterno, la convenzione comunica chiaramente che non dovrebbe essere fatto. È un patto tra programmatori.

Esiste però un problema più sottile. Anche se proteggiamo la modifica, potremmo voler permettere la lettura dei voti senza esporre direttamente la lista originale. Se restituiamo la lista interna così com’è, chi la riceve potrebbe comunque modificarla.

Per questo Python offre lo strumento delle proprietà. Una proprietà permette di leggere un attributo come se fosse pubblico, ma mantenendo il controllo su ciò che viene restituito.

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome
        self._voti = []

    def aggiungi_voto(self, voto):
        if 0 <= voto <= 30:
            self._voti.append(voto)

    @property
    def voti(self):
        return self._voti.copy()
```

In questo modo possiamo scrivere:

```python
print(s.voti)
```

ma non possiamo alterare lo stato interno senza passare dai metodi previsti. Restituendo una copia, l’oggetto mantiene il controllo completo dei propri dati.

Un esempio ancora più concreto è quello di un conto bancario. Se il saldo fosse liberamente modificabile, qualcuno potrebbe assegnargli un valore negativo o arbitrario, compromettendo l’intero sistema.

```python
class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo

    def preleva(self, importo):
        if 0 < importo <= self._saldo:
            self._saldo -= importo

    @property
    def saldo(self):
        return self._saldo
```

Qui il saldo può cambiare solo passando attraverso le regole stabilite dai metodi. L’oggetto è responsabile della propria coerenza interna.

Questo è il cuore dell’incapsulamento. Non si tratta semplicemente di nascondere dati, ma di garantire che l’oggetto rimanga sempre in uno stato valido. Chi utilizza l’oggetto non deve preoccuparsi di come funziona internamente. Deve solo sapere quali operazioni sono consentite.

Quando progetti una classe, dovresti chiederti se stai permettendo modifiche che potrebbero rendere l’oggetto incoerente. Se la risposta è sì, probabilmente hai bisogno di più incapsulamento.

In definitiva, l’incapsulamento separa il cosa dal come. L’utente dell’oggetto vede le funzionalità offerte, non l’implementazione interna. Questa separazione rende il codice più robusto, più leggibile e più facile da mantenere nel tempo.

Un oggetto ben progettato non è solo un insieme di dati. È un’entità che custodisce e governa il proprio stato. Ed è proprio questa autonomia che rende potente la programmazione orientata agli oggetti.
