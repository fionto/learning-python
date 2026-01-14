# supporto

**Esercizi consolidati**: 4
**Generato il**: 14/01/2026 18:30
**Sorgente**: `04-Loops\04_02_WhileLoops\supporto`

---

## 001_moda

```python
def moda(numeri):
    
    if not numeri:
        return None
    
    moda = numeri[0]
    contatore_massimo = 0
        
    for numero in numeri:
        contatore_corrente = numeri.count(numero)
        if(contatore_corrente > contatore_massimo):
            contatore_massimo = contatore_corrente
            moda = numero

    return moda
```

---

## 001_moda2

```python
def moda(numeri):
    
    if not numeri:
        return None
    
    # Fase 1: Creazione del dizionario delle frequenze
    conteggi = {}
    for numero in numeri:
        conteggi[numero] = conteggi.get(numero, 0) + 1

    # Fase 2: Ricerca manuale del massimo
    # Inizializziamo due variabili per "tenere traccia" del meglio che troviamo
    numero_più_frequente = None
    massima_frequenza_trovata = -1 # Partiamo da un valore bassissimo
    
    # Usiamo .items() per avere sia la 'chiave' (il numero) che il 'valore' (la frequenza)
    for numero, frequenza in conteggi.items():
        # Se la frequenza del numero che stiamo guardando ora è superiore
        # a quella massima registrata finora...
        if frequenza > massima_frequenza_trovata:
            # ...allora questo numero diventa il nostro nuovo candidato principale
            massima_frequenza_trovata = frequenza
            numero_più_frequente = numero

    return numero_più_frequente
```

---

## 002_ripetuti

```python
def ripetuti(numeri):
    
    if not numeri:
        return None
    
    numeri_ripetuti = []
        
    for numero in set(numeri):
        if(numeri.count(numero) > 1):
            numeri_ripetuti.append(numero)

    return numeri_ripetuti

serie_di_numeri = [7, 10, 6, 2, 1, 2, 2, 1, 3, 3, 3, 3, 4, 1, 1, 1, 4]
print(ripetuti(serie_di_numeri))
```

---

## 002_ripetuti2

```python
def ripetuti(numeri):
    if not numeri:
        return None

    conteggi = {}
    for n in numeri:
        conteggi[n] = conteggi.get(n, 0) + 1

    return [n for n, c in conteggi.items() if c > 1]

serie_di_numeri = [7, 10, 6, 2, 1, 2, 2, 1, 3, 3, 3, 3, 4, 1, 1, 1, 4]
print(ripetuti(serie_di_numeri))
```

---

