# Il Modulo `collections`: `defaultdict` e la Gestione Intelligente dei Dizionari

## Introduzione: Il Problema del Dizionario Vuoto

Supponiamo di scrivere un programma che analizza il testo di una canzone per contare quante volte appare ogni parola. Un approccio naturale sarebbe usare un dizionario, dove le chiavi sono le parole e i valori sono i conteggi:

```python
testo = "ciao mondo ciao python python python"
parole = testo.split()

conteggi = {}
for parola in parole:
    conteggi[parola] = conteggi[parola] + 1

print(conteggi)
```

Se eseguite questo codice, otterrete un errore: `KeyError: 'ciao'`. Perché? Perché quando cercate di accedere a `conteggi[parola]` per la prima volta, la chiave non esiste ancora nel dizionario, e Python non sa come gestire l'accesso a una chiave inesistente.

La soluzione tradizionale è controllare se la chiave esiste prima di accedervi:

```python
testo = "ciao mondo ciao python python python"
parole = testo.split()

conteggi = {}
for parola in parole:
    if parola in conteggi:
        conteggi[parola] = conteggi[parola] + 1
    else:
        conteggi[parola] = 1

print(conteggi)  # {'ciao': 2, 'mondo': 1, 'python': 3}
```

Questo funziona, ma il codice è verboso. Ogni volta che accedete a una chiave potenzialmente inesistente, dovete controllare se esiste. Immaginate di dover fare questo in dieci posti diversi nel vostro codice—diventa rapidamente tedioso e propenso a errori.

Il modulo `collections` di Python offre una soluzione elegante: `defaultdict`.

## Che cos'è `defaultdict`?

`defaultdict` è una sottoclasse di `dict` che fornisce un valore predefinito per qualsiasi chiave che non esiste ancora nel dizionario. Quando accedete a una chiave inesistente, invece di ricevere un `KeyError`, `defaultdict` crea automaticamente una voce con un valore predefinito.

La sintassi è:

```python
from collections import defaultdict

d = defaultdict(tipo_o_funzione_predefinita)
```

### Parametro: La Funzione Predefinita

La cosa cruciale da capire è che `defaultdict` accetta una **funzione** (o più precisamente, un **callable**—qualcosa che può essere chiamato come una funzione) che genera il valore predefinito. Non passa il valore direttamente.

Considerate questi esempi:

```python
# Sbagliato: passate il valore
d = defaultdict([])  # Errore!

# Corretto: passate una funzione che restituisce il valore
d = defaultdict(list)  # La funzione è 'list'
```

Quando `defaultdict` ha bisogno di un valore predefinito, chiama questa funzione senza argomenti: `list()`, che restituisce una lista vuota `[]`.

Ecco alcuni callable comuni:

| Callable | Cosa crea | Quando usare |
|----------|-----------|-------------|
| `list` | `[]` | Quando volete raccogliere più valori per chiave |
| `int` | `0` | Per conteggi e somme |
| `str` | `''` (stringa vuota) | Per concatenazioni di stringhe |
| `set` | `set()` | Quando volete valori unici per chiave |
| `dict` | `{}` | Per dizionari annidati |
| `lambda: 0` | `0` | Alternativa personalizzata a `int` |
| `lambda: "N/A"` | `"N/A"` | Valore predefinito personalizzato |

## Il Nostro Primo Esempio: Contare le Parole

Torniamo al nostro esempio di conteggio delle parole, ma questa volta usiamo `defaultdict`:

```python
from collections import defaultdict

testo = "ciao mondo ciao python python python"
parole = testo.split()

# Creiamo un defaultdict con int come predefinito
conteggi = defaultdict(int)

for parola in parole:
    conteggi[parola] += 1

print(dict(conteggi))  # {'ciao': 2, 'mondo': 1, 'python': 3}
```

Notate come il codice sia molto più semplice. Quando accedete a `conteggi[parola]` per la prima volta:

1. `defaultdict` controlla se la chiave esiste
2. Se non esiste, chiama `int()` che restituisce `0`
3. Voi aggiungete 1 a questo 0, ottenendo 1
4. Il valore 1 viene memorizzato nella chiave

Alla seconda e alle volte successive che incontrate la stessa parola, la chiave esiste già, quindi recuperate direttamente il valore esistente e incrementate.

**Nota importante:** Quando stampate un `defaultdict`, potete convertirlo a un dizionario normale con `dict()` se volete che assomigli a un dizionario standard. Altrimenti, `print(conteggi)` mostrerà `defaultdict(int, {...})`.

## Raggruppare Dati: Usando `defaultdict(list)`

Un altro scenario comune è raggruppare dati. Supponiamo di avere un elenco di studenti con i loro voti in diverse materie:

```python
risultati = [
    ("Alice", "Matematica", 95),
    ("Bob", "Matematica", 87),
    ("Alice", "Italiano", 92),
    ("Bob", "Italiano", 89),
    ("Charlie", "Matematica", 91),
]
```

Volete creare un dizionario che raggruppi gli studenti per materia:

```python
from collections import defaultdict

risultati = [
    ("Alice", "Matematica", 95),
    ("Bob", "Matematica", 87),
    ("Alice", "Italiano", 92),
    ("Bob", "Italiano", 89),
    ("Charlie", "Matematica", 91),
]

# Senza defaultdict (metodo tradizionale)
per_materia_tradizionale = {}
for studente, materia, voto in risultati:
    if materia not in per_materia_tradizionale:
        per_materia_tradizionale[materia] = []
    per_materia_tradizionale[materia].append((studente, voto))

# Con defaultdict (molto più pulito)
per_materia = defaultdict(list)
for studente, materia, voto in risultati:
    per_materia[materia].append((studente, voto))

print(dict(per_materia))
# Output:
# {
#   'Matematica': [('Alice', 95), ('Bob', 87), ('Charlie', 91)],
#   'Italiano': [('Alice', 92), ('Bob', 89)]
# }
```

Notate come con `defaultdict(list)`, la prima volta che incontrate una nuova materia, `defaultdict` crea automaticamente una lista vuota, e poi voi potete semplicemente appendere il dato.

## Valori Unici: Usando `defaultdict(set)`

A volte volete raccogliere valori unici. Ad esempio, volete sapere quali città visitano i vostri clienti:

```python
from collections import defaultdict

viaggi = [
    ("Marco", "Roma"),
    ("Marco", "Milano"),
    ("Marco", "Roma"),  # Roma di nuovo
    ("Lucia", "Firenze"),
    ("Lucia", "Milano"),
]

# Con defaultdict(set), i duplicati vengono eliminati automaticamente
clienti_città = defaultdict(set)
for cliente, città in viaggi:
    clienti_città[cliente].add(città)

print(dict(clienti_città))
# Output:
# {
#   'Marco': {'Roma', 'Milano'},
#   'Lucia': {'Firenze', 'Milano'}
# }
```

Notate come Roma appare solo una volta per Marco, anche se è stata aggiunta due volte. Questo è il comportamento naturale dei set—non permettono duplicati.

## Dizionari Annidati: Usando `defaultdict(dict)`

Talvolta volete strutture più complesse. Supponiamo di voler memorizzare informazioni su clienti, organizzate per città:

```python
from collections import defaultdict

dati_clienti = [
    ("Roma", "Marco", "marco@email.com"),
    ("Roma", "Luigi", "luigi@email.com"),
    ("Milano", "Federica", "federica@email.com"),
]

# Struttura: città -> nome -> email
clienti_per_città = defaultdict(dict)

for città, nome, email in dati_clienti:
    clienti_per_città[città][nome] = email

print(dict(clienti_per_città))
# Output:
# {
#   'Roma': {'Marco': 'marco@email.com', 'Luigi': 'luigi@email.com'},
#   'Milano': {'Federica': 'federica@email.com'}
# }
```

Con `defaultdict(dict)`, ogni volta che accedete a una nuova città, viene creato automaticamente un dizionario vuoto, e poi potete aggiungere i dati del cliente.

## Valori Predefiniti Personalizzati: Usando `lambda`

Talvolta il valore predefinito che volete non è fornito da un callable built-in. Potete usare una **lambda function** (funzione anonima):

```python
from collections import defaultdict

# Volete che il valore predefinito sia la stringa "Sconosciuto"
nomi = defaultdict(lambda: "Sconosciuto")

nomi["Marco"] = "Marco Rossi"

print(nomi["Marco"])      # Marco Rossi
print(nomi["Lucia"])      # Sconosciuto
```

Una lambda è una piccola funzione anonima. La sintassi è `lambda: valore_desiderato`. Quando `defaultdict` ha bisogno di un valore predefinito, chiama questa lambda.

Potete anche usare lambda per creare strutture più complesse:

```python
from collections import defaultdict

# Volete che ogni nuovo cliente abbia di default una lista vuota di ordini
# e un credito di 0
clienti = defaultdict(lambda: {"ordini": [], "credito": 0})

clienti["Marco"]["ordini"].append("Ordine 1")
clienti["Lucia"]["credito"] = 100

print(dict(clienti))
# Output:
# {
#   'Marco': {'ordini': ['Ordine 1'], 'credito': 0},
#   'Lucia': {'ordini': [], 'credito': 100}
# }
```

## Un Caso Reale Più Complesso: Analisi di Log

Immaginate di avere un log di accessi a un sito web e volete analizzare quante volte ogni IP ha visitato una determinata pagina:

```python
from collections import defaultdict

log_accessi = [
    ("192.168.1.1", "/home"),
    ("192.168.1.1", "/about"),
    ("192.168.1.2", "/home"),
    ("192.168.1.1", "/home"),
    ("192.168.1.2", "/contact"),
    ("192.168.1.1", "/about"),
]

# Struttura: IP -> pagina -> conteggi
accessi = defaultdict(lambda: defaultdict(int))

for ip, pagina in log_accessi:
    accessi[ip][pagina] += 1

# Convertire a dizionario per la stampa
print(dict(accessi))
# Output:
# {
#   '192.168.1.1': {'home': 2, 'about': 2},
#   '192.168.1.2': {'/home': 1, '/contact': 1}
# }
```

Notate come usiamo `defaultdict(lambda: defaultdict(int))`. Questo crea una struttura a due livelli:
- Il primo livello (per IP) è un `defaultdict(int)`
- Quando accedete a un nuovo IP, il primo livello crea automaticamente un nuovo `defaultdict(int)` per memorizzare il conteggio delle pagine

## Differenze tra `defaultdict` e `dict.get()`

C'è un altro modo per gestire le chiavi inesistenti nei dizionari normali: il metodo `.get()`:

```python
d = {"a": 1}

# Con .get()
valore = d.get("b", 0)  # Restituisce 0 se "b" non esiste
print(valore)           # 0

# Ma non modifica il dizionario
print("b" in d)         # False
```

Quindi qual è la differenza?

| Aspetto | `dict.get()` | `defaultdict` |
|---------|-------------|---------------|
| **Aggiunge la chiave?** | No | Sì (al primo accesso) |
| **Modifica il dizionario?** | No | Sì |
| **Leggibilità** | Buona per accessi singoli | Migliore per cicli frequenti |
| **Overhead** | Basso | Minimo se usato correttamente |

Quando usare `dict.get()`:
- Volete verificare una chiave senza aggiungerla al dizionario
- Accedete raramente a chiavi inesistenti
- Volete codice esplicito

Quando usare `defaultdict`:
- Iterate spesso su chiavi che potrebbero non esistere
- Volete che le chiavi vengano aggiunte automaticamente
- Volete codice più conciso

## Un Avvertimento Importante: Il Comportamento di Accesso

Ricordate che `defaultdict` crea una voce **solo quando accedete direttamente alla chiave**:

```python
from collections import defaultdict

d = defaultdict(int)

# Questo NON crea una voce per "a"
print("a" in d)  # False

# Questo CREA una voce per "a" e la imposta a 0
print(d["a"])    # 0
print("a" in d)  # True (ora esiste!)
```

Questo comportamento può essere utile, ma è importante esserne consapevoli. Se iterate su un `defaultdict` senza accedere alle chiavi, non vengono create nuove voci:

```python
from collections import defaultdict

d = defaultdict(int)
d["b"] = 5

# Iterare non crea nuove chiavi
for chiave in ["a", "b", "c"]:
    print(d[chiave])

# Stampa:
# 0 (per "a" - nuova chiave creata)
# 5 (per "b" - esistente)
# 0 (per "c" - nuova chiave creata)

print(dict(d))
# {'b': 5, 'a': 0, 'c': 0}
```

## Conclusione: Quando Usare `defaultdict`

`defaultdict` è uno strumento potentissimo che riduce drasticamente il boilerplate code quando lavorate con dizionari. È particolarmente utile quando:

1. Contate occorrenze di elementi
2. Raggruppate dati
3. Create strutture di dati annidate
4. Volete codice più leggibile e manutenibile

Tuttavia, non è sempre la scelta giusta. Se state leggendo un dizionario esistente e non volete modificarlo, un dizionario normale con `.get()` potrebbe essere più appropriato.

Con `defaultdict` nel vostro arsenale, scoprirete che molti problemi comuni di manipolazione dati diventano significativamente più semplici da risolvere.
