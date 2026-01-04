# Day03_for_loops

**Esercizi consolidati**: 14
**Generato il**: 03/01/2026 18:46

---

## 01_somma

```python
# ESERCIZIO 1: Somma dei numeri
# Crea una lista di numeri
# Usa un for loop per calcolare la somma di tutti gli elementi.
# Stampa il risultato finale.

numeri = [0, 1 ,1, 2, 3, 5, 8, 13, 21]
somma = 0

for numero in numeri:
    somma = somma + numero

print(f"Il risultato finale è {somma}")
```

---

## 02_stampa_stringa

```python
# ESERCIZIO 2: Stampa invertita di una stringa
# Data una stringa (ad esempio: "python"), usa un for loop per stampare ogni 
# carattere in ordine inverso. Ricorda che le stringhe sono sequenze 
# indicizzabili, quindi puoi usare range() con indici negativi oppure iterare 
# normalmente e stampare al contrario.

# creo stringa
stringa = "python"

# calcolo lunghezza per creazione indici
num_lettere = len(stringa)

# metodo per scorrere for loop al contrario
# genero range con indici al contrario
indici = reversed(range(num_lettere))

# faccio scorrere il ciclo
for i in indici:
    lettera = stringa[i]
    print(lettera)
```

---

## 03_stampa_stringa2

```python
# ESERCIZIO 3: Stampa invertita di una stringa

# Creo una stringa
stringa = "python"

# Calcolo la lunghezza per creare gli indici
# len() ritorna un intero
num_lettere = len(stringa)

# range(num_lettere) crea un RANGE OBJECT (oggetto iterabile, non una lista)
# Un range NON memorizza tutti i numeri in memoria, ma li genera al bisogno
# range(6) è come una "ricetta" che dice "genera numeri da 0 a 5"
indici_in_avanti = range(num_lettere)

# reversed() prende un iterabile e ritorna un REVERSED OBJECT (iterabile)
# Anche reversed() NON materializza i numeri, ma li genera al bisogno, inversi
# reversed() lavora su qualsiasi sequenza (range, liste, stringhe, ecc.)
indici = reversed(indici_in_avanti)

# Il for loop può iterare su oggetti iterabili senza convertirli a lista
# Python genera un numero alla volta dal reversed object mentre il loop scorre
for i in indici:
    lettera = stringa[i]
    print(lettera)

# Se volessi materializzare l'oggetto iterabile in una lista concreta:
# indici_lista = list(reversed(range(num_lettere)))
# Allora print(indici_lista) darebbe [5, 4, 3, 2, 1, 0]
```

---

## 04_stampa_stringa3

```python
# ESERCIZIO 2: Stampa invertita di una stringa
# Data una stringa (ad esempio: "python"), usa un for loop per stampare ogni 
# carattere in ordine inverso. 

stringa = "python"
for lettera in stringa[::-1]:
    print(lettera)
# Lo slicing [::-1] inverte la sequenza direttamente
# Questo crea una nuova stringa invertita e itera su quella
```

---

## 05_stampa_stringa5

```python
# ESERCIZIO 2: Stampa invertita di una stringa
# Data una stringa (ad esempio: "python"), usa un for loop per stampare ogni 
# carattere in ordine inverso. 

# METODO 2: Usare reversed() direttamente nel for (come il tuo, ma più conciso)
stringa = "python"
for lettera in reversed(stringa):
    print(lettera)
# reversed() funziona direttamente su stringhe, non servono indici
# Genera le lettere al contrario una per una
```

---

## 06_filtra_lista

```python
# ESERCIZIO 4: Lunghezza delle stringhe in una lista
#
# Data una lista di parole 
# (ad esempio: ["gatto", "elefante", "ape", "dinosauro"]),
# usa un for loop per stampare ogni parola insieme alla sua lunghezza

animali = ["gatto", "elefante", "ape", "dinosauro"]

for animale in animali:
    lettere = len(animale)
    print(f"{animale.title()} ha {lettere} lettere")
```

---

## 07_tabelline

```python
# ESERCIZIO 5: Tabellina con numeri
#
# Stampare le tabelline da 1 a 5.
# Il risultato dovrebbe mostrare qualcosa come:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 5 x 10 = 50

moltiplicandi = range(1, 6)
moltiplicatori = range(1, 6)

for moltiplicando in moltiplicandi:
    for moltiplicatore in moltiplicatori:
        prodotto = moltiplicando * moltiplicatore
        print(f"{moltiplicando} x {moltiplicatore} = {prodotto}")
```

---

## 08_slicing1

```python
# ESERCIZIO 6: Somma degli ultimi tre numeri
# Data una lista di numeri, usa lo slicing per estrarre gli ultimi tre elementi
# e calcola la loro somma usando un for loop.

numeri = [0, 1 ,1, 2, 3, 5, 8, 13, 21]

numeri_sliced = numeri [-3:]
somma = 0

for numero in numeri_sliced:
    somma = numero + somma

print("La somma degli ultimi 3 numeri è:", somma)
```

---

## 09_somma2

```python
# Crea una lista di numeri fino a 1_000_000 con range()
# usa min() e max() per verificare gli estremi
# usa sum() per sommare tutto

numeri = range(0, 1_000_001, 1)

print(f"Il numero minimo è: {min(numeri):,d}")
print(f"Il numero massimo è: {max(numeri):,d}")

print(f"La somma totale è: {sum(numeri):,d}")
```

---

## 10_odd_numbers

```python
# Use the third argument of the range() function to make a list of the odd 
# numbers from 1 to 20. Use a for loop to print each number.

for numero in range(1, 20, 2):
    print(numero)
```

---

## 11_threes

```python
# Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the 
# numbers in your list

for numero in range(3, 31, 3):
    print(numero)
```

---

## 12_cubes

```python
# A number raised to the third power is called a cube. 
# Make a list of the first 10 cubes and use a for loop to print out the value 
# of each cube.

for numero in range (0, 11, 1):
    print(numero**3)
```

---

## 13_slices

```python
# Using one of the programs you wrote in this chapter, add several lines to the 
# end of the program that do the following:

# Print the message "The first three items in the list are:" 
# Then use a slice to print the first three items from that program’s list.
# Print the message "Three items from the middle of the list are:" 
# Then use a slice to print three items from the middle of the list.
# Print the message "The last three items in the list are:"
# Then use a slice to print the last three items in the list.

# Creo la playlist
playlist = [
    'Eight Days A Week', 
    'Let It Be', 
    'In My Life', 
    'Hey Jude', 
    'While My Guitar Gently Weeps',
    'Strawberry Fields Forever',
    'Across The Universe',
]

print(f"The first three items in the list are: {playlist[:3]}")
print(f"Three items in the middle are: {playlist[2:5]}")
print(f"The last three items in the list are: {playlist[-3:]}")
```

---

## 14_copia_lista

```python
# Genera una lista di pizze
# Copia in una nuova lista
# Aggiungi una pizza alla lista originale
# Aggiungi una pizza alla nuova lista
# Dimostra che sono due liste differenti

pizze_originali = ['Margherita', 'Capricciosa', 'Diavola']
pizze_nuove = pizze_originali[:]

pizze_originali.append('Boscaiola')
pizze_nuove.append('Hawaii')

print(pizze_originali)
print(pizze_nuove)
```

---

