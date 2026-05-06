# Creare dizionari in Python: tutte le strade possibili

Un dizionario è una delle strutture dati più usate in Python, e si trova al centro di quasi ogni programma non banale: nei parametri di configurazione, nella rappresentazione di record JSON, nei contatori, negli indici invertiti. Chi conosce già i dizionari di solito li costruisce sempre nello stesso modo: una coppia di parentesi graffe, qualche coppia chiave-valore, fine della storia. Eppure Python offre almeno sei o sette modi diversi per creare un dizionario, e ciascuno è più adatto di altri in certi contesti.

Questa dispensa esplora tutte le forme di creazione e generazione di dizionari disponibili in Python 3.10+, dai letterali alle dict comprehension, dai costruttori ai metodi di classe. L'obiettivo non è la completezza enciclopedica, ma la capacità di scegliere la forma giusta per il problema in mano.

---

## Il punto di partenza: il letterale `{}`

La forma più immediata è il **letterale dizionario**: si scrivono le coppie chiave-valore tra parentesi graffe, separate da virgole, con i due punti a dividere chiave e valore.

```python
configurazione = {
    "host": "localhost",
    "porta": 5432,
    "debug": True,
}
```

I tipi di chiave e valore sono indipendenti: le chiavi possono essere stringhe, interi, tuple (qualunque tipo hashable), e i valori possono essere qualsiasi oggetto Python, dizionari inclusi. L'unico vincolo è che le chiavi devono essere hashable, ossia non modificabili dopo la creazione: le stringhe, gli interi e le tuple di immutabili vanno bene; le liste no.

Il letterale `{}` da solo produce un **dizionario vuoto**. Questo dettaglio è importante perché `{}` non crea un insieme vuoto: per quello serve `set()`. Il dizionario vuoto è spesso il punto di partenza per costruire strutture che crescono a runtime, e la sua forma con parentesi graffe è la più leggibile quando si prevede di popolarlo subito dopo.

```python
registro = {}  # dizionario vuoto

# popolazione esplicita
registro["Alice"] = 42
registro["Bob"] = 37

print(registro)  # Output: {'Alice': 42, 'Bob': 37}
```

---

## Il costruttore `dict()`

La funzione built-in `dict()` è il costruttore del tipo dizionario e accetta input in forme diverse. La prima è quella con **argomenti keyword**: si passano le coppie come argomenti nominali della funzione, e Python le converte automaticamente in coppie chiave-valore con chiavi di tipo stringa.

```python
persona = dict(nome="Matteo", età=34, città="Roma")

print(persona)  # Output: {'nome': 'Matteo', 'età': 34, 'città': 'Roma'}
```

Questa sintassi è comoda quando le chiavi sono identificatori validi di Python e non contengono spazi o caratteri speciali. Ha però un limite preciso: le chiavi generate sono sempre stringhe, e non è possibile usare chiavi che siano interi o tuple. Non si può scrivere `dict(42="risposta")` perché `42` non è un identificatore Python valido.

`dict()` senza argomenti produce un dizionario vuoto, alternativo a `{}`. Le due forme sono equivalenti; `dict()` è occasionalmente preferita per chiarezza espressiva in contesti in cui il tipo è rilevante.

```python
vuoto_a = {}
vuoto_b = dict()

print(vuoto_a == vuoto_b)  # Output: True
print(type(vuoto_a))       # Output: <class 'dict'>
print(type(vuoto_b))       # Output: <class 'dict'>
```

---

## Da sequenze di coppie

Il costruttore `dict()` accetta anche un **iterabile di coppie** (sequenze a due elementi) come argomento posizionale. Questa forma è molto utile quando le chiavi e i valori arrivano già come sequenze separate o come risultato di una trasformazione.

```python
coppie = [("alfa", 1), ("beta", 2), ("gamma", 3)]
d = dict(coppie)

print(d)  # Output: {'alfa': 1, 'beta': 2, 'gamma': 3}
```

Lo stesso si ottiene con una lista di liste a due elementi, oppure con qualsiasi iterabile che produca sequenze di lunghezza due. In pratica, la fonte più frequente è la funzione `zip()`, che mette in corrispondenza elemento per elemento due sequenze:

```python
chiavi = ["x", "y", "z"]
valori = [10, 20, 30]

d = dict(zip(chiavi, valori))

print(d)  # Output: {'x': 10, 'y': 20, 'z': 30}
```

Questa combinazione `dict(zip(...))` è un idioma molto diffuso: compare spesso quando si lavora con file CSV (dove intestazioni e righe sono liste separate), con risultati di query SQL, o con dati tabulari di qualsiasi tipo. È leggibile e non richiede cicli espliciti.

Cosa succede se le sequenze hanno lunghezza diversa? `zip()` si ferma alla sequenza più corta, senza errori. Questo comportamento è conveniente ma può produrre dizionari incompleti in modo silenzioso se i dati sono malformati. Quando la lunghezza uguale è un'invariante importante, è preferibile usare `zip(strict=True)` (disponibile da Python 3.10), che solleva `ValueError` in caso di disallineamento.

```python
chiavi = ["a", "b", "c"]
valori = [1, 2]  # manca un elemento

# senza strict: si ferma alla coppia ('b', 2)
d_troncato = dict(zip(chiavi, valori))
print(d_troncato)  # Output: {'a': 1, 'b': 2}

# con strict: solleva ValueError
try:
    d_stretto = dict(zip(chiavi, valori, strict=True))
except ValueError as e:
    print(f"Errore: {e}")
# Output: Errore: zip() has arguments with different lengths
```

---

## `dict.fromkeys()`: un dizionario a partire da chiavi

Il metodo di classe `dict.fromkeys()` crea un dizionario in cui tutte le chiavi sono tratte da un iterabile e tutte le chiavi mappano allo stesso valore. È utile per inizializzare strutture con un valore di default uniforme.

```python
contatori = dict.fromkeys(["alpha", "beta", "gamma"], 0)

print(contatori)
# Output: {'alpha': 0, 'beta': 0, 'gamma': 0}
```

Senza il secondo argomento, il valore predefinito è `None`.

```python
stati = dict.fromkeys(["connesso", "autenticato", "autorizzato"])

print(stati)
# Output: {'connesso': None, 'autenticato': None, 'autorizzato': None}
```

Questo metodo ha un trabocchetto importante quando il valore di default è mutabile (una lista, un altro dizionario). Tutte le chiavi condividono lo stesso identico oggetto, non copie indipendenti. La sezione "Trabocchetti" più avanti affronta questo punto in dettaglio.

---

## Dict comprehension

Le **dict comprehension** sono la forma più espressiva e flessibile per costruire dizionari in modo compatto. La sintassi rispecchia quella delle list comprehension, con la differenza che si specificano sia la chiave sia il valore, separati dai due punti.

```python
# quadrati dei numeri da 1 a 5
quadrati = {n: n**2 for n in range(1, 6)}

print(quadrati)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Come nelle list comprehension, è possibile aggiungere una condizione `if` per filtrare gli elementi:

```python
# solo i quadrati dei numeri pari
quadrati_pari = {n: n**2 for n in range(1, 11) if n % 2 == 0}

print(quadrati_pari)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

Le dict comprehension sono particolarmente potenti quando si vuole **trasformare un dizionario esistente**: invertirne le chiavi con i valori, filtrare alcune voci, o applicare una funzione ai valori.

```python
prezzi = {"mela": 0.80, "banana": 0.50, "arancia": 1.20}

# converti in centesimi
prezzi_centesimi = {frutto: int(prezzo * 100) for frutto, prezzo in prezzi.items()}
print(prezzi_centesimi)
# Output: {'mela': 80, 'banana': 50, 'arancia': 120}

# filtra solo i frutti che costano più di 0.70 €
cari = {frutto: prezzo for frutto, prezzo in prezzi.items() if prezzo > 0.70}
print(cari)
# Output: {'mela': 0.8, 'arancia': 1.2}

# inverti chiavi e valori (valido se i valori sono unici e hashable)
inverso = {v: k for k, v in prezzi.items()}
print(inverso)
# Output: {0.8: 'mela', 0.5: 'banana', 1.2: 'arancia'}
```

L'ultimo esempio (inversione) funziona correttamente solo se i valori originali sono tutti distinti. Se due chiavi mappano allo stesso valore, l'inversione sovrascrive silenziosamente la prima con la seconda.

---

## Unione di dizionari: `|` e `|=`

Da Python 3.9, è possibile **unire due dizionari** con l'operatore `|`. Il risultato è un nuovo dizionario che contiene tutte le coppie di entrambi; in caso di chiavi duplicate, vince il dizionario a destra.

```python
default = {"colore": "blu", "dimensione": "M", "materiale": "cotone"}
personalizzato = {"colore": "rosso", "taglia": "L"}

risultato = default | personalizzato

print(risultato)
# Output: {'colore': 'rosso', 'dimensione': 'M', 'materiale': 'cotone', 'taglia': 'L'}
```

Il dizionario `default` non viene modificato. Se si vuole invece aggiornare un dizionario in-place, si usa `|=`, che è equivalente alla chiamata del metodo `.update()` ma con una sintassi più compatta.

```python
opzioni = {"verbose": False, "timeout": 30}
opzioni |= {"timeout": 60, "retry": 3}

print(opzioni)
# Output: {'verbose': False, 'timeout': 60, 'retry': 3}
```

Prima di Python 3.9, l'unione si otteneva con `{**d1, **d2}`, una forma ancora valida e ancora ampiamente presente nel codice esistente.

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}

unione = {**d1, **d2}

print(unione)
# Output: {'a': 1, 'b': 99, 'c': 3}
```

L'operatore `**` (unpacking) funziona con qualsiasi numero di dizionari e si può combinare con coppie chiave-valore letterali nello stesso letterale, il che lo rende utile per "costruire" un dizionario con valori di default sovrascrivibili.

```python
def costruisci_config(**kwargs):
    base = {"debug": False, "livello_log": "INFO", "timeout": 30}
    return {**base, **kwargs}

config = costruisci_config(debug=True, timeout=60)
print(config)
# Output: {'debug': True, 'livello_log': 'INFO', 'timeout': 60}
```

---

## Nota critica: il trabocchetto di `fromkeys` con valori mutabili

`dict.fromkeys(chiavi, valore)` non crea una copia del valore per ogni chiave: tutte le chiavi puntano allo stesso oggetto. Quando il valore è un immutabile come `0` o `""`, questo non è un problema. Quando invece il valore è una lista o un dizionario, modificare la struttura attraverso una chiave la modifica per tutte le chiavi.

```python
# SBAGLIATO: tutte le chiavi condividono la stessa lista
gruppi = dict.fromkeys(["A", "B", "C"], [])

gruppi["A"].append("Mario")

print(gruppi)
# Output: {'A': ['Mario'], 'B': ['Mario'], 'C': ['Mario']}
# La lista è la stessa per tutte e tre le chiavi!
```

La soluzione è usare una dict comprehension che crea una nuova lista per ogni chiave:

```python
# CORRETTO: ogni chiave ottiene la propria lista indipendente
gruppi = {k: [] for k in ["A", "B", "C"]}

gruppi["A"].append("Mario")

print(gruppi)
# Output: {'A': ['Mario'], 'B': [], 'C': []}
```

Questo è il motivo per cui le dict comprehension sono generalmente preferibili a `fromkeys` quando il valore iniziale è mutabile. La regola è semplice: `fromkeys` va bene con valori immutabili (`None`, interi, stringhe, tuple), da evitare con liste, dizionari, o istanze di classi.

---

## Riepilogo

Python offre strade diverse per costruire un dizionario perché le sorgenti dei dati sono diverse: a volte si parte da coppie già formate, a volte da due sequenze parallele, a volte da un dizionario esistente da trasformare.

Il letterale `{"chiave": valore}` è la forma naturale quando i dati sono noti staticamente. Il costruttore `dict(chiave=valore)` semplifica la scrittura quando le chiavi sono identificatori semplici. La combinazione `dict(zip(...))` gestisce l'assemblaggio da fonti separate. `dict.fromkeys()` inizializza strutture con valori uniformi, ma solo se quei valori sono immutabili. Le dict comprehension sono lo strumento più flessibile per costruire dizionari a partire da calcoli, filtri o trasformazioni di strutture esistenti.

L'operatore `|` e il suo corrispondente `|=` completano il quadro rendendo esplicita l'operazione di fusione tra dizionari, che in precedenza richiedeva l'unpacking `**` o la chiamata esplicita a `.update()`.

Chi lavora abitualmente con dati strutturati (configurazioni, risposte JSON, pipeline di trasformazione) troverà le dict comprehension e la combinazione `dict(zip(...))` tra gli strumenti più frequentemente utili. Chi invece progetta API o funzioni con molti parametri opzionali troverà il pattern `{**base, **kwargs}` quasi indispensabile.

Un possibile passo successivo riguarda i **defaultdict** del modulo `collections`, che estendono il dizionario standard con la capacità di fornire automaticamente un valore di default per le chiavi mancanti, eliminando la necessità di verificare l'esistenza di una chiave prima di modificarne il valore.
