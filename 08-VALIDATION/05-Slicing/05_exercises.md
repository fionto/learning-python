# 05-Slicing

**Esercizi consolidati**: 8
**Generato il**: 14/01/2026 18:30
**Sorgente**: `05-Slicing`

---

## 5_01_estrazione

```python
# ESERCIZIO 1: Estrazione tramite indici positivi e negativi
# Obiettivo: Estrarre sottostringhe specifiche dalla variabile 'testo'.
# 1. Estrarre i primi 5 caratteri.
# 2. Estrarre gli ultimi 4 caratteri usando indici negativi.
# 3. Estrarre la parola "corso".

testo = "Benvenuti al corso di Python"

# Risultati attesi:
# 1. "Benve"
# 2. "thon"
# 3. "corso"

risultato_uno = testo[:5]
print(risultato_uno)

risultato_due = testo[-4:]
print(risultato_due)

risultato_tre = testo[13:18]
print(risultato_tre)
```

---

## 5_02_sequenze

```python
# ESERCIZIO 2: Lavorare con le omissioni e l'inversione
# Obiettivo: Utilizzare la sintassi abbreviata per gestire una lista di numeri.
# 1. Creare una sottolista che contenga i primi 4 elementi.
# 2. Creare una sottolista che contenga tutti gli elementi dal quinto in poi.
# 3. Creare una versione invertita della lista originale.

numeri = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Risultati attesi:
# 1. [0, 10, 20, 30]
# 2. [40, 50, 60, 70, 80, 90]
# 3. [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

risultato_uno = numeri[:4]
risultato_due = numeri[4:]
risultato_tre = numeri[::-1] # start, stop, step = -1

print(risultato_uno)
print(risultato_due)
print(risultato_tre)
```

---

## 5_03_step_parameter

```python
# ESERCIZIO 3: Selezione a intervalli (Step)
# Obiettivo: Selezionare elementi non contigui da una lista di stringhe.
# 1. Estrarre ogni secondo elemento della lista (elementi in posizione pari: 0, 2, 4...).
# 2. Estrarre ogni terzo elemento partendo dal secondo (indice 1).
# 3. Estrarre gli elementi in ordine inverso, ma saltandone uno (uno sì e uno no).

frutti = ["mela", "banana", "ciliegia", "durian", "uva", "fico", "guava"]

# Risultati attesi:
# 1. ['mela', 'ciliegia', 'uva', 'guava']
# 2. ['banana', 'uva']
# 3. ['guava', 'uva', 'ciliegia', 'mela']

risultato_uno = frutti[::2]
print(risultato_uno)

risultato_due = frutti[1::3]
print(risultato_due)

risultato_tre = frutti[::-2]
print(risultato_tre)
```

---

## 5_04_copie

```python
# ESERCIZIO 4: Slicing per la copia e verifica immutabilità
# Obiettivo: Dimostrare la differenza tra copia di una lista e riferimento, 
# e osservare il comportamento delle stringhe.
# 1. Creare una copia Shallow della lista 'colori' chiamarla 'colori_copia'.
# 2. Modificare il primo elemento di 'colori' in "nero". Verificare che 'colori_copia' sia rimasta invariata.
# 3. Provare a modificare un carattere della stringa 'nome' tramite slicing (es. nome[0] = "K").
# NOTA: Osservate l'errore generato al punto 3 per confermare l'immutabilità.

colori = ["rosso", "verde", "blu"]
nome = "Python"

# Risultati attesi:
# colori: ["nero", "verde", "blu"]
# colori_copia: ["rosso", "verde", "blu"]
# Errore atteso al punto 3: TypeError: 'str' object does not support item assignment

colori_copia = colori[:]

colori[0] = 'nero'

print(f"lista originale è composta da : {colori}")
print(f"lista originale è composta da : {colori_copia}")
```

---

## 5_05_slicing_combinato

```python
# ESERCIZIO 5: Slicing combinato su liste e stringhe
# Obiettivo: Estrarre dati complessi combinando start, stop e step negativi.
# 1. Data la stringa 'alfabeto', estrarre la sequenza "zyx" usando solo indici negativi e step.
# 2. Dalla lista 'misto', estrarre gli elementi dall'indice 1 all'indice 5, ma restituiti al contrario.

alfabeto = "abcdefghijklmnopqrstuvwxyz"
misto = [10, "A", 20, "B", 30, "C", 40, "D"]

# Risultati attesi:
# 1. "zyx"
# 2. ["C", 30, "B", 20, "A"]

risultato_uno = alfabeto[-1:-4:-1]
print(risultato_uno)

risultato_due = misto[5:0:-1]
print(risultato_due)
```

---

## 5_06_slicing_assignement

```python
# ESERCIZIO 6: Modifica di una sequenza tramite slicing assignment
# Obiettivo: Sostituire una porzione di una lista con una nuova sequenza.
# Nota bene: La lunghezza della nuova sequenza non deve necessariamente 
# coincidere con quella della fetta sostituita.
# 1. Nella lista 'dati', sostituire gli elementi dall'indice 1 all'indice 3 (escluso)
#    con la lista [99, 88, 77].
# 2. Rimuovere gli ultimi due elementi della lista risultante usando lo slicing e l'operatore 'del' 
#    oppure assegnando una lista vuota [].

dati = [10, 20, 30, 40, 50]

# Risultati attesi:
# 1. Dopo la sostituzione: [10, 99, 88, 77, 40, 50]
# 2. Dopo la rimozione finale: [10, 99, 88, 77]

sequenza_nuova = [99, 88, 77]

dati = dati[0:1] + sequenza_nuova + dati[3:]
print(dati)

del dati[-2:]
print(dati)
```

---

## 5_06_slicing_assignement2

```python
# Nota bene: La lunghezza della nuova sequenza non deve necessariamente 
# coincidere con quella della fetta sostituita.
# 1. Nella lista 'dati', sostituire gli elementi dall'indice 1 all'indice 3 (escluso)
#    con la lista [99, 88, 77].
# 2. Rimuovere gli ultimi due elementi della lista risultante usando lo slicing e l'operatore 'del' 
#    oppure assegnando una lista vuota [].

dati = [10, 20, 30, 40, 50]

# Risultati attesi:
# 1. Dopo la sostituzione: [10, 99, 88, 77, 40, 50]
# 2. Dopo la rimozione finale: [10, 99, 88, 77]

# Python "apre" la lista originale tra l'indice 1 e 3 e 
# ci inserisce dentro i nuovi elementi, 
# adattando la lunghezza della lista automaticamente
dati[1:3] = [99, 88, 77] 
print(dati)

del dati[-2:]
print(dati)
```

---

## 5_07_estrazione_metadati

```python
# ESERCIZIO 7: Parsing di una stringa a formato fisso
# Obiettivo: Estrarre informazioni specifiche da una stringa che simula un log.
# Formato: "DATA:20231012|ID:9958|TEMP:22.5"
# 1. Estrarre solo la DATA (i caratteri tra l'indice 5 e il primo separatore '|').
# 2. Estrarre l'ID (4 cifre) usando indici negativi riferiti alla posizione del secondo '|'.
# 3. Creare una nuova stringa che inverta l'ordine dei componenti: "TEMP:22.5|ID:9958|DATA:20231012"
#    usando solo lo slicing e la concatenazione.

log = "DATA:20231012|ID:9958|TEMP:22.5"

# Risultati attesi:
# 1. "20231012"
# 2. "9958"
# 3. "TEMP:22.5|ID:9958|DATA:20231012"

nuova_stringa = ''

# Trovo gli indici
separatore_colon = log.find(':')
separatore_bar = log.find('|')

# Estraggo e stampo solo data
data = log[separatore_colon + 1 :separatore_bar]
print(data)

# Metto da parte stringa
nuova_stringa = log[:separatore_bar]

log_copia = log[separatore_bar + 1:]
separatore_colon = log_copia.find(':')
separatore_bar = log_copia.find('|')
id = log_copia[separatore_colon + 1 :separatore_bar]
print(id)

# Costruisco la stringa inversa
nuova_stringa = log_copia[separatore_bar + 1:] + '|' + log_copia[:separatore_bar + 1] + nuova_stringa

print(nuova_stringa)
```

---

