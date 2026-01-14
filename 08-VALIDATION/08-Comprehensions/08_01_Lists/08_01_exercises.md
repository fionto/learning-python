# 08_01_Lists

**Esercizi consolidati**: 8
**Generato il**: 14/01/2026 18:30
**Sorgente**: `08_Comprehensions\08_01_Lists`

---

## 8_1_01_cubes

```python
# Usa una list comprehension per generare una lista dei primi 10 cubi

cubi = [value**3 for value in range (1,11)]

print(cubi)
```

---

## 8_1_02_dispari

```python
# ESERCIZIO 2
# Data una lista di numeri interi, costruisci una nuova lista contenente
# solo i numeri dispari.
#
# Esempio:
# input  -> [10, 15, 22, 33, 40]
# output -> [15, 33]
#

numeri = [10, 15, 22, 33, 40]

dispari = [n for n in numeri if n % 2 != 0]

print(dispari)
```

---

## 8_1_03_lunghezza

```python
# ESERCIZIO 3
# Data una lista di stringhe, crea una nuova lista che contenga
# solo le stringhe con lunghezza maggiore di 5 caratteri.
#
# Esempio:
# input  -> ["python", "c", "java", "matlab", "go"]
# output -> ["python", "matlab"]
#
# Obiettivo: allenarsi all'uso delle list comprehension con stringhe.

linguaggi = ["python", "c", "java", "matlab", "go"]

linguaggi_lunghi = [linguaggio for linguaggio in linguaggi if len(linguaggio) > 5]

print(linguaggi_lunghi)
```

---

## 8_1_04_negativi

```python
# ESERCIZIO 4
# Data una lista di numeri (positivi e negativi), crea una nuova lista
# in cui ogni numero viene trasformato secondo la seguente regola:
# - se il numero è positivo, mantienilo
# - se il numero è negativo, sostituiscilo con 0
#
# Esempio:
# input  -> [3, -1, 0, -7, 5]
# output -> [3, 0, 0, 0, 5]
#

numeri = [3, -1, 0, -7, 5]

numeri_trasformati = [n if n > 0 else 0 for n in numeri]

print(numeri_trasformati)
```

---

## 8_1_05_maiuscolo

```python
# ESERCIZIO 5
# Data una lista di stringhe contenenti parole in minuscolo,
# crea una nuova lista che contenga le stesse parole ma in maiuscolo,
# escludendo però le parole vuote ("").
#
# Esempio:
# input  -> ["ciao", "", "python", "", "corso"]
# output -> ["CIAO", "PYTHON", "CORSO"]
#

parole = ["ciao", "", "python", "", "corso"]

maiuscole = [parola.upper() for parola in parole if parola]

print(maiuscole)
```

---

## 8_1_06_multipli

```python
# ESERCIZIO 6
# Data una lista di numeri interi, costruisci una nuova lista contenente
# solo i numeri che sono multipli sia di 3 che di 5.
#
# L'obiettivo è ottenere la lista finale usando una singola list comprehension.

multipli = [n for n in range(1, 100) if n % 15 == 0]

print(multipli)
```

---

## 8_1_07_lunghezze

```python
# ESERCIZIO 7
# Data una lista di stringhe, crea una nuova lista contenente la lunghezza
# di ciascuna stringa, escludendo quelle che contengono solo spazi.
#
# La lista risultante deve contenere solo numeri interi.

animali = ['cane', 'gatto', 'rinoceronte', '  ', '', 'gallina']

lunghezze = [len(animale) for animale in animali if animale.strip()]

print(lunghezze)
```

---

## 8_1_08_

```python
# ESERCIZIO 8
# Data una lista di numeri reali, costruisci una nuova lista in cui:
# - i numeri negativi vengono scartati
# - i numeri positivi vengono trasformati
#
# L'esercizio richiede l'uso combinato di più elementi tipici
# delle list comprehension in Python.

numeri = [-3, -7, 10, 250, 0, 69, -85, 45, 12, -12]

elaborati = [n ** 2 for n in numeri if n >= 0]

print(elaborati)
```

---

