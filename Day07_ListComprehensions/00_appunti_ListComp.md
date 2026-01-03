# List Comprehension in Python

Nel percorso di apprendimento di Python, le *list comprehension* rappresentano uno di quei passaggi in cui il linguaggio inizia a “mostrare i muscoli”: permettono di scrivere codice più compatto, più leggibile e spesso più espressivo. Sono un modo *idiomatico* di pensare alle liste in Python.

In questa dispensa vedremo **cosa sono**, **come funzionano**, **quando usarle** e **quando evitarle**, con esempi progressivi e piccoli casi di studio realistici.

---

## Il problema di partenza

Partiamo da una situazione molto comune: costruire una lista a partire da un’altra.

```python
numeri = [1, 2, 3, 4, 5]

quadrati = []
for n in numeri:
    quadrati.append(n**2)
```

Questo codice è corretto, leggibile e perfettamente Python.  
Ma Python ci offre un modo più diretto per esprimere la stessa idea:

> “Voglio una lista che contenga il quadrato di ogni numero in `numeri`.”

Ed è qui che entrano in gioco le list comprehension.

---

## La forma base di una list comprehension

La versione equivalente con list comprehension è:

```python
numeri = [1, 2, 3, 4, 5]

quadrati = [n**2 for n in numeri]
```

Leggetela quasi come una frase in inglese:
> “`n**2` **for** ogni `n` in `numeri`”

La struttura generale è:

```python
[espressione for variabile in iterabile]
```

Non stiamo “scrivendo un for più corto”, ma **dichiarando direttamente il risultato** che vogliamo ottenere.

---

## Aggiungere una condizione

Spesso non vogliamo trasformare *tutti* gli elementi, ma solo quelli che soddisfano una condizione.

Esempio: calcolare il quadrato solo dei numeri pari. Versione classica:

```python
numeri = [1, 2, 3, 4, 5]

quadrati_pari = []
for n in numeri:
    if n % 2 == 0:
        quadrati_pari.append(n**2)
```

Con list comprehension:

```python
quadrati_pari = [n**2 for n in numeri if n % 2 == 0]
```

La condizione viene messa **alla fine**, dopo il `for`.  
Questo è un punto chiave: *non è un if “normale”*, ma un **filtro**.

---

## Espressioni più complesse

L’espressione iniziale può essere qualunque cosa produca un valore.

```python
nomi = ["anna", "Luca", "mArCo"]

normalizzati = [nome.capitalize() for nome in nomi]
```

Qui la list comprehension non fa solo selezione, ma anche **trasformazione semantica** dei dati.

Si può anche usare un `if-else` *nell’espressione* (attenzione alla differenza):

```python
etichette = ["pari" if n % 2 == 0 else "dispari" for n in numeri]
```

Da notare la posizione:
- `if ... else ...` **prima** del `for` → scelta tra due valori
- `if ...` **dopo** il `for` → filtro

Confondere le due cose è uno degli errori più comuni.

---

## Casi studio

### Caso studio 1: pulizia dei dati

Supponiamo di avere dati grezzi da un sensore:

```python
misure = [" 23.4", "errore", "19.8", "  ", "21.0"]
```

Vogliamo:
1. eliminare i valori non numerici
2. convertire il resto in `float`

```python
valori = [float(m.strip()) for m in misure if m.strip().replace(".", "", 1).isdigit()]
```

Qui la list comprehension condensa un’intera pipeline di pulizia dati in una singola espressione.  
È potente, ma già al limite della leggibilità — torneremo su questo punto.

---

### Caso studio 2: elaborazione scientifica semplice

Immaginiamo una lista di energie (in eV) e vogliamo selezionare solo quelle sopra una soglia:

```python
energie = [0.8, 1.2, 0.5, 2.1, 1.8]

energie_rilevanti = [E for E in energie if E > 1.0]
```

Oppure normalizzarle rispetto al valore massimo:

```python
Emax = max(energie)
energie_norm = [E / Emax for E in energie]
```

In contesti scientifici, questo stile rende il codice **molto vicino alla formula matematica** che stiamo implementando.

---

## Best practices

Le list comprehension sono eleganti, ma **non sono sempre la scelta migliore**.

Usatele quando:
- l’operazione è concettualmente *una trasformazione di lista*
- l’espressione è leggibile a colpo d’occhio
- non ci sono troppi livelli di annidamento

Evitatele quando:
- la logica diventa opaca
- servono più `if` annidati
- state facendo debugging passo-passo

Un buon criterio empirico:
> se dovete andare a capo più volte per capirla, forse è troppo.

Confronto illuminante:

```python
# Poco leggibile
risultato = [f(x) for x in dati if cond1(x) and (cond2(x) or cond3(x))]
```

Versus:

```python
risultato = []
for x in dati:
    if cond1(x) and (cond2(x) or cond3(x)):
        risultato.append(f(x))
```

La seconda è più lunga, ma **più chiara**. E la chiarezza vince quasi sempre.

---

## Un ultimo punto concettuale importante

Le list comprehension **creano una nuova lista**.  
Non modificano quella esistente.

Questo le rende:
- sicure
- prevedibili
- ideali per uno stile funzionale leggero

Se vi accorgete che state usando una list comprehension solo per *effetti collaterali*, state andando contro la filosofia di Python.

---

## Conclusione

Le list comprehension non sono solo una scorciatoia sintattica: sono un modo diverso di pensare al codice, più dichiarativo e meno procedurale.

Imparare a usarle bene significa:
- scrivere codice più Pythonico
- esprimere meglio le intenzioni
- ridurre il rumore senza perdere significato

E come sempre: **prima la leggibilità, poi la furbizia**.