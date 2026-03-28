# Capitolo 3: Sezione 3.3 — Dizionari: Chiavi, Valori e la Potenza dell'Associazione

## Introduzione: La Rubrica Telefonica del Computer

Immaginate di voler conservare i numeri di telefono di una serie di amici. Un approccio ingenuo consiste nel tenere due liste parallele: una con i nomi, un'altra con i numeri, nella stessa sequenza. Per trovare il numero di "Giulia", dovrete prima cercare "Giulia" nella lista dei nomi (magari è al terzo posto), poi accedere al terzo elemento della lista dei numeri. Funziona, ma è scomodo: ogni volta che volete un dato, dovete passare attraverso una struttura che non lo associa esplicitamente all'altro.

I dizionari di Python nascono esattamente per risolvere questo problema. In Python, un dizionario è una struttura dati che memorizza coppie di **chiave** e **valore**: la chiave è il nome di Giulia, il valore è il suo numero di telefono. Per recuperare il numero, non cercate per posizione ma per identità: chiedete direttamente "dammi il valore associato alla chiave 'Giulia'". Il computer risponde in tempo costante, indipendentemente da quante altre coppie siano memorizzate nel dizionario.

Questa caratteristica rende i dizionari uno degli strumenti più usati in Python, presenti in quasi ogni programma reale: configurazioni software, contatori di parole, risultati di ricerche API, tabelle di traduzione. Dopo le liste e le tuple che abbiamo già incontrato nelle sezioni precedenti, i dizionari completano il nucleo delle strutture dati fondamentali del linguaggio.

---

## Costruire un Dizionario

La sintassi per creare un dizionario usa le **parentesi graffe** e separa ogni coppia chiave-valore con i due punti. Le coppie sono a loro volta separate da virgole. Ecco la forma più comune:

```python
# Un dizionario che associa nomi a numeri di telefono
rubrica = {
    "Giulia": "333-1234567",
    "Marco": "347-9876543",
    "Sara": "366-1112233"
}

print(rubrica)
# Output: {'Giulia': '333-1234567', 'Marco': '347-9876543', 'Sara': '366-1112233'}
```

Le chiavi di un dizionario devono essere **immutabili**: in pratica, potete usare stringhe, numeri interi, numeri in virgola mobile e tuple (purché non contengano elementi mutabili). Non potete usare liste come chiavi, perché le liste sono modificabili. I valori, invece, possono essere di qualsiasi tipo: stringhe, interi, altre liste, persino altri dizionari.

È possibile creare un dizionario vuoto in due modi equivalenti: con le parentesi graffe vuote `{}` oppure con la funzione `dict()`. Entrambi producono lo stesso risultato.

```python
# Due modi equivalenti per un dizionario vuoto
d1 = {}
d2 = dict()

print(type(d1))  # Output: <class 'dict'>
print(d1 == d2)  # Output: True
```

---

## Accedere, Aggiungere e Rimuovere Elementi

### Accesso tramite chiave

Per leggere il valore associato a una chiave, si usa la stessa sintassi delle liste, ma al posto dell'indice numerico si fornisce la chiave:

```python
rubrica = {"Giulia": "333-1234567", "Marco": "347-9876543"}

# Accesso diretto per chiave
numero_giulia = rubrica["Giulia"]
print(numero_giulia)  # Output: 333-1234567
```

Se la chiave non esiste, Python solleva un `KeyError`. Per evitarlo, potete usare il metodo `.get()`, che restituisce `None` (oppure un valore di default che voi specificate) se la chiave non è presente:

```python
rubrica = {"Giulia": "333-1234567"}

# Accesso con .get(): nessuna eccezione se la chiave manca
numero = rubrica.get("Luca")
print(numero)  # Output: None

# Con valore di default esplicito
numero = rubrica.get("Luca", "numero non disponibile")
print(numero)  # Output: numero non disponibile
```

### Aggiungere e modificare coppie

I dizionari sono **mutabili**: potete aggiungere nuove coppie o modificare quelle esistenti semplicemente assegnando un valore a una chiave. Se la chiave è nuova, la coppia viene creata; se esiste già, il valore viene sovrascritto.

```python
rubrica = {"Giulia": "333-1234567"}

# Aggiungere una nuova coppia
rubrica["Marco"] = "347-9876543"

# Modificare un valore esistente
rubrica["Giulia"] = "333-0000001"

print(rubrica)
# Output: {'Giulia': '333-0000001', 'Marco': '347-9876543'}
```

### Rimuovere coppie

Per rimuovere una coppia, potete usare l'istruzione `del` seguita dalla chiave, oppure il metodo `.pop()` che rimuove la coppia e restituisce il valore rimosso (utile quando lo volete usare prima di eliminarlo):

```python
rubrica = {"Giulia": "333-1234567", "Marco": "347-9876543", "Sara": "366-1112233"}

# Rimozione con del
del rubrica["Sara"]
print(rubrica)
# Output: {'Giulia': '333-1234567', 'Marco': '347-9876543'}

# Rimozione con pop(): recupera e rimuove simultaneamente
numero_rimosso = rubrica.pop("Marco")
print(numero_rimosso)  # Output: 347-9876543
print(rubrica)         # Output: {'Giulia': '333-1234567'}
```

---

## Verificare l'Esistenza di una Chiave

Prima di accedere a una chiave, spesso è utile verificare che esista. L'operatore `in`, già incontrato con le liste, funziona anche con i dizionari: controlla la presenza di una **chiave** (non di un valore) nel dizionario.

```python
rubrica = {"Giulia": "333-1234567", "Marco": "347-9876543"}

# Verifica con 'in'
if "Giulia" in rubrica:
    print("Giulia è in rubrica")       # Questa riga viene eseguita
else:
    print("Giulia non è in rubrica")

if "Luca" not in rubrica:
    print("Luca non è ancora in rubrica")  # Questa riga viene eseguita
```

Questa verifica è sicura ed efficiente: Python implementa i dizionari tramite una struttura chiamata *hash table*, per cui la ricerca di una chiave avviene in tempo quasi costante indipendentemente dalla dimensione del dizionario.

---

## I Tre Metodi di Iterazione: `keys()`, `values()`, `items()`

Quando volete scorrere l'intero contenuto di un dizionario, Python offre tre metodi dedicati che restituiscono "viste" (oggetti speciali che riflettono lo stato corrente del dizionario):

**`keys()`** restituisce tutte le chiavi; **`values()`** restituisce tutti i valori; **`items()`** restituisce coppie `(chiave, valore)` sotto forma di tuple.

```python
inventario = {
    "mele": 30,
    "pere": 12,
    "banane": 50
}

# Iterare sulle chiavi
print("Prodotti disponibili:")
for prodotto in inventario.keys():
    print(prodotto)
# Output:
# mele
# pere
# banane

# Iterare sui valori
print("Quantità in magazzino:")
for quantita in inventario.values():
    print(quantita)
# Output:
# 30
# 12
# 50

# Iterare sulle coppie chiave-valore con items()
print("Inventario completo:")
for prodotto, quantita in inventario.items():
    print(f"{prodotto}: {quantita} unità")
# Output:
# mele: 30 unità
# pere: 12 unità
# banane: 50 unità
```

Nell'ultimo esempio, notate l'**unpacking** della tupla: scrivendo `for prodotto, quantita in inventario.items()`, Python assegna automaticamente il primo elemento della coppia (la chiave) a `prodotto` e il secondo (il valore) a `quantita`. Questa tecnica rende il codice molto leggibile.

Vale la pena sapere che iterare su un dizionario senza chiamare nessuno di questi tre metodi equivale a iterare sulle sole chiavi: `for k in d` e `for k in d.keys()` sono equivalenti. Usare `.keys()` esplicitamente, tuttavia, rende l'intenzione più chiara a chi legge il codice.

```python
inventario = {"mele": 30, "pere": 12}

# Questi due cicli sono equivalenti
for k in inventario:
    print(k)

for k in inventario.keys():
    print(k)
# Entrambi stampano: mele, pere
```

---

## Dictionary Comprehension

Esattamente come le liste supportano le **list comprehension** (sezione 3.1), i dizionari supportano le **dictionary comprehension**: un modo compatto per costruire un nuovo dizionario applicando una trasformazione a una sequenza di dati, tutto in una sola espressione.

La sintassi segue lo stesso schema delle list comprehension, ma usa le parentesi graffe e separa chiave e valore con i due punti:

```python
{ chiave: valore for elemento in sequenza }
```

Un esempio semplice: costruire un dizionario che associa ogni numero intero al suo quadrato.

```python
# Modo tradizionale con ciclo for
quadrati = {}
for n in range(1, 6):
    quadrati[n] = n ** 2
print(quadrati)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Modo compatto con dictionary comprehension
quadrati = {n: n ** 2 for n in range(1, 6)}
print(quadrati)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Le comprehension possono includere anche una condizione opzionale, scritta dopo la clausola `for`, per filtrare gli elementi:

```python
# Solo i quadrati dei numeri pari
quadrati_pari = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(quadrati_pari)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

Un caso molto comune è trasformare un dizionario esistente, applicando una funzione ai valori. Supponiamo di avere i prezzi di alcuni prodotti e di volerli aumentare del 10%:

```python
prezzi = {"pane": 1.20, "latte": 0.90, "caffè": 2.50}

prezzi_aggiornati = {prodotto: round(prezzo * 1.10, 2)
                     for prodotto, prezzo in prezzi.items()}

print(prezzi_aggiornati)
# Output: {'pane': 1.32, 'latte': 0.99, 'caffè': 2.75}
```

In questo esempio, `.items()` e la dictionary comprehension lavorano in perfetta sinergia: la prima disassembla il dizionario originale in coppie, la seconda ne riassembla uno nuovo con i valori trasformati.

---

## Mettere Tutto Insieme: Un Esempio Applicato

Per consolidare tutti i concetti della sezione, costruiamo un piccolo programma che conta le occorrenze di ciascuna parola in una frase, un problema classico che i dizionari risolvono in modo naturale ed elegante.

```python
# Contare le occorrenze di ogni parola in una frase
frase = "il gatto sul tetto il tetto è caldo il gatto dorme"
parole = frase.split()  # Divide la stringa in una lista di parole

# Costruzione del contatore con un ciclo tradizionale
contatore = {}
for parola in parole:
    if parola in contatore:
        contatore[parola] += 1
    else:
        contatore[parola] = 1

print(contatore)
# Output: {'il': 3, 'gatto': 2, 'sul': 1, 'tetto': 2, 'è': 1, 'caldo': 1, 'dorme': 1}

# Stampare solo le parole che compaiono più di una volta
print("Parole ripetute:")
for parola, conteggio in contatore.items():
    if conteggio > 1:
        print(f"  '{parola}' compare {conteggio} volte")
# Output:
#   'il' compare 3 volte
#   'gatto' compare 2 volte
#   'tetto' compare 2 volte

# La stessa costruzione in forma di comprehension
contatore_comp = {p: parole.count(p) for p in set(parole)}
print(contatore_comp)
# Output (ordine può variare): {'dorme': 1, 'gatto': 2, 'il': 3, ...}
```

Si notino due cose importanti nell'ultimo snippet: `set(parole)` elimina i duplicati dalla lista, così `.count()` viene chiamato una volta sola per ogni parola distinta; il risultato è identico ma ottenuto con un'espressione singola anziché cinque righe.

---

## Conclusione: Un Nuovo Modo di Pensare ai Dati

Con i dizionari, avete acquisito una struttura dati che cambia il modo in cui si affronta la modellazione dei dati. Le liste vi chiedono di pensare in termini di posizione: il primo elemento, il quinto, l'ultimo. I dizionari vi chiedono di pensare in termini di identità e associazione: che cosa è legato a che cosa, e come accedo a un dato tramite un nome significativo piuttosto che un numero arbitrario.

I tre metodi `keys()`, `values()` e `items()` vi danno tre "finestre" diverse sullo stesso oggetto: potete vedere solo i nomi, solo i valori, oppure entrambi insieme come coppie. La dictionary comprehension vi permette di costruire o trasformare dizionari con la stessa eleganza sintattica che avete già visto per le liste.

La prossima sezione (3.4) completa il quadro delle strutture dati della Sezione 3 occupandosi delle **stringhe** in profondità: indicizzazione, slicing, immutabilità e i metodi di manipolazione più utili. Scoprirete che molti dei pattern che avete appena imparato (iterazione, accesso per chiave, comprehension) si trasferiscono con piccole variazioni anche al mondo delle stringhe, rendendo il salto concettuale molto meno ripido di quanto possa sembrare.
