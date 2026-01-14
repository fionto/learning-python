# 06-Dictionaries

**Esercizi consolidati**: 10
**Generato il**: 06/01/2026 18:19

---

## 01_person

```python
# Use a dictionary to store information about a person
# Print the dictionary

persona = {}

persona["first_name"] = "Napoleone"
persona["last_name"] = "Bonaparte"
persona["age"] = 51
persona["city"] = "Paris"

print(persona)
```

---

## 02_favorite_number

```python
# Use a dictionary to store people's favorite numbers.
# Print each person's name and their favorite number.

# Memorizzo nome e numero preferito
amici = {
    "Leonardo": 23,
    "Michelangelo": 30,
    "Donatello": 7,
    "Raffaello": 55,
}

# Scorro le coppie trasformandole in touples
# Looping through all Key-Values pairs (vedi pagina 99 Python Crash Course)
for nome, numero in amici.items():
    print(f"Il numero preferito di {nome} Ã¨ {numero}")
```

---

## 03_rivers

```python
# Make a dictionary containing three major rivers and the
# capital each river runs through.
# Use a loop to print a sentence avout each river
# Use a loop to print each river name
# Use a loop to print each nation

# Memorizzo nome e numero preferito
fiumi = {
    "Tevere": "Roma",
    "Senna": "Parigi",
    "Manzanarre": "Madrid",
    "Moldava": "Praga",
}

for fiume, cittÃ  in fiumi.items():
    print(f"Il fiume {fiume} scorre in {cittÃ }")

for fiume in fiumi.keys():
    print(fiume)

for capitale in fiumi.values():
    print(capitale)
```

---

## 04_frasi

```python
# ESERCIZIO 4
#
# Dato un elenco di frasi, scrivi un codice che restituisca un dizionario
# in cui a ogni frase Ã¨ associato il numero di parole uniche (case-insensitive),
# escludendo la punteggiatura.
#

def main():
    frasi = [
        "Python Ã¨ divertente, Python Ã¨ potente!",
        "Scrivere codice pulito Ã¨ importante.",
        "Ãˆ importante leggere la documentazione."
    ]

    # Riempio le chiavi del dizionario perchÃ© nel ciclo assegno i solo valori
    dizionario = dict.fromkeys(frasi)
    
    for frase in frasi:
        frase_pulita = frase.replace(',', '').replace('.', '').replace('!', '').lower()
        parole = frase_pulita.split(' ')
        
        numero_uniche = uniche(parole)
        
        # Assegno i valori alle chiavi
        dizionario[frase] = numero_uniche

    print(dizionario)
        

# Conta parole uniche
def uniche(lista_parole: list[str]) -> int:
    
    parole_uniche = []

    for parola in lista_parole:
        if parola not in parole_uniche:
            parole_uniche.append(parola)

    return len(parole_uniche)

main()
```

---

## 04_frasi2

```python
# ESERCIZIO 4
#
# Dato un elenco di frasi, scrivi un codice che restituisca un dizionario
# in cui a ogni frase Ã¨ associato il numero di parole uniche (case-insensitive),
# escludendo la punteggiatura.
#

def main():
    frasi = [
        "Python Ã¨ divertente, Python Ã¨ potente!",
        "Scrivere codice pulito Ã¨ importante.",
        "Ãˆ importante leggere la documentazione."
    ]

    # Non serve riempire le chiavi perchÃ© l'assegnazione dopo eseguue tutto
    dizionario = {}
    
    for frase in frasi:
        frase_pulita = frase.replace(',', '').replace('.', '').replace('!', '').lower()
        
        # Faccio split senza argomento: divido stringa su qualsiasi sequenza di whitespaces
        parole = frase_pulita.split()
        
        numero_uniche = uniche(parole)
        
        # Se la chiave non esiste, la crea. Se la chiave esiste, sovrascrivi il valore.
        dizionario[frase] = numero_uniche

    print(dizionario)
        

# Conta parole uniche
def uniche(lista_parole: list[str]) -> int:
    
    parole_uniche = []

    for parola in lista_parole:
        if parola not in parole_uniche:
            parole_uniche.append(parola)

    return len(parole_uniche)

main()
```

---

## 05_frutta

```python
# ESERCIZIO 5
#
# Data una lista di tuple (prodotto, quantitÃ ),
# scrivi un codice che costruisca un dizionario
# con il totale delle quantitÃ  per ciascun prodotto.
#

# Lista di tuples
acquisti = [
    ("mele", 3),
    ("pere", 5),
    ("mele", 2),
    ("banane", 4),
    ("pere", 1)
]

totale = {}
articoli = []

for acquisto in acquisti:
    
    if acquisto[0] not in totale.keys():
        totale[acquisto[0]] = acquisto[1]
    else:
        nuova_quantita = totale[acquisto[0]] + acquisto[1]
        totale[acquisto[0]] = nuova_quantita

print(totale)
```

---

## 05_frutta2

```python
# ESERCIZIO 5
#
# Data una lista di tuple (prodotto, quantitÃ ),
# scrivi un codice che costruisca un dizionario
# con il totale delle quantitÃ  per ciascun prodotto.
#

# Lista di tuples
acquisti = [
    ("mele", 3),
    ("pere", 5),
    ("mele", 2),
    ("banane", 4),
    ("pere", 1)
]

spesa = {}

# Tuple unpacking: direttamente nella riga del for
for frutto, quantitÃ  in acquisti:
    
    # metodo .get(key, value) per accedere al valore conoscendo la chiave
    # key Ã¨ un valore richiesto
    # value Ã¨ opzionale, in questo caso restituisce 0 se la chiave non esiste.
    spesa[frutto] = spesa.get(frutto, 0) + quantitÃ 

print (spesa)
```

---

## 06_studenti

```python
# ESERCIZIO 6
#
# Dato un dizionario che associa studenti a una lista di voti,
# scrivi una funzione che restituisca un nuovo dizionario
# contenente solo gli studenti con una media maggiore o uguale a 27.
#


registro = {
    "Anna": [28, 30, 27],
    "Luca": [24, 26, 25],
    "Marco": [30, 29, 28],
    "Sara": [27, 26, 27]
}

promossi = {}

for studente, voti in registro.items():
    media = round(sum(voti)/len(voti), 1)
    
    if media > 27:
        promossi[studente] = media

print(promossi)
```

---

## 07_trasformazione

```python
# ESERCIZIO 7
# Dato un dizionario che associa parole a numeri interi,
# scrivi un codice che restituisca una nuova versione del dizionario
# in cui:
# - le chiavi con valore negativo vengono rimosse
# - i valori pari vengono raddoppiati
# - i valori dispari rimangono invariati
#
# INPUT:

dati = {
    "a": 4,
    "b": -3,
    "c": 7,
    "d": 10,
    "e": -1
}

dati_elaborati = {}

for nome, dato in dati.items():
    valore = int(dato)
    if valore < 0:
       continue 
    if valore % 2 == 0:
        dati_elaborati[nome] = valore * 2
    else:
        dati_elaborati[nome] = valore

print(dati_elaborati)
```

---

## 08_sensori

```python
# ESERCIZIO 8
# Data una lista di dizionari, ciascuno contenente informazioni
# su un sensore (id, tipo, valore),
# scrivi una funzione che restituisca un dizionario
# che associa a ogni tipo di sensore la lista dei valori misurati.
#
# INPUT:

sensori = [
    {"id": 1, "tipo": "temperatura", "valore": 22.5},
    {"id": 2, "tipo": "pressione", "valore": 1.01},
    {"id": 3, "tipo": "temperatura", "valore": 23.1},
    {"id": 4, "tipo": "umiditÃ ", "valore": 45},
    {"id": 5, "tipo": "pressione", "valore": 0.99}
]

# All'inizio il dizionario Ã¨ vuoto.
# devo costruire le chiavi man mano che scorro la lista.
valori_misurati = {}

for sensore in sensori:
    # Estraggo le informazioni che mi servono.
    # Meglio farlo subito, cosÃ¬ il codice Ã¨ piÃ¹ leggibile
    # e non devo rileggere ogni volta il dizionario.
    tipo = sensore["tipo"]
    valore = sensore["valore"]
    
    # Creazione della chiave: prima controllo condizionale se esiste
    # l'operatore `in` che punta a dizionario esegue controllo sulle chiavi
    if tipo not in valori_misurati:
        # Se la chiave non esiste, devo crearla io.
        # E siccome poi voglio usare append(),
        # il valore associato deve essere una lista vuota.        
        valori_misurati[tipo] = []
    
    # A questo punto sono sicuro di una cosa fondamentale:
    # - la chiave esiste
    # - il valore associato Ã¨ una lista
    # quindi posso tranquillamente usare append()    
    valori_misurati[tipo].append(valore)
        
print(valori_misurati)

# NOTA (errore iniziale):
# In una versione precedente del codice cercavo di fare direttamente:
# valori_misurati[tipo].append(valore)
# dando per scontato che la chiave 'tipo' esistesse giÃ  nel dizionario.
# In realtÃ , usando .append() stavo prima LEGGENDO il valore associato alla chiave,
# e solo dopo cercavo di modificarlo.
# Se la chiave non esiste, la lettura fallisce e il dizionario NON si espande da solo.
# La chiave viene creata automaticamente solo quando si assegna esplicitamente:
# valori_misurati[tipo] = []
# Da lÃ¬ in poi, append() funziona correttamente.
```

---

