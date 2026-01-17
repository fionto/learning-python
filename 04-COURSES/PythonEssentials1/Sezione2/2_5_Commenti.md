# Capitolo 2: Sezione 2.5 - Commenti: La Comunicazione Nel Codice

## Introduzione: Il Paradosso dei Commenti

Avrete sicuramente visto codice come questo:

```python
# Incrementare x di 1
x = x + 1

# Stampare il risultato
print(x)

# Controllare se y è maggiore di 5
if y > 5:
    # Se vero, stampare "Maggiore"
    print("Maggiore")
```

Se leggete questi commenti, vi accorgerete di una cosa: **dicono esattamente quello che il codice fa già**. Il commento "Incrementare x di 1" è totalmente ovvio quando vedete `x = x + 1`. È ridondante. È rumore.

Questo è il **paradosso dei commenti**: i commenti più facili da scrivere sono spesso i meno utili.

Un bravo programmatore capisce che **i commenti non dovrebbero spiegare il "come"—il codice già lo fa. I commenti dovrebbero spiegare il "perché"**.

## 2.5.1 La Filosofia dei Commenti: Cosa Scrivere e Perché

### Il Cattivo: Commenti Ovvi

I commenti ovvi aggiungono rumore senza valore:

```python
# Cattivo: commento ovvio
x = 5                          # Assegna 5 a x
y = 10                         # Assegna 10 a y
z = x + y                      # Somma x e y

# Cattivo: commento che ripete il codice
if temperatura > 30:           # Se la temperatura è maggiore di 30
    print("Fa caldo")          # Stampa "Fa caldo"
```

Perché sono cattivi? Perché il codice **già dice quello che fanno**. Leggendo il codice, capisco perfettamente che `x = 5` assegna 5 a x. Non ho bisogno di un commento.

Inoltre, i commenti ovvi creano un **costo nascosto**:
1. **Più da leggere**: Devo leggere sia il codice che il commento
2. **Rischio di disinformazione**: Se il codice cambia e il commento no, ora il commento è sbagliato
3. **Distrazione**: Il commento riduce la chiarezza visiva

### Il Buono: Commenti Significativi

I commenti significativi aggiungono valore che il codice **non può esprimere**:

```python
# Buono: spiega il PERCHÉ
if temperatura > 30:
    # Se la temperatura supera 30°C, attivare la ventilazione
    # per prevenire il surriscaldamento del sistema
    ventilazione.attiva()
```

```python
# Buono: spiega un algoritmo non ovvio
# Usiamo il metodo di ricerca binaria perché il dataset
# è ordinato e ha milioni di elementi (O(log n) vs O(n))
indice = ricerca_binaria(dati, valore)
```

```python
# Buono: spiega una scelta di design
# Arrotondiamo a 2 decimali per evitare problemi di
# precisione in virgola mobile nel calcolo delle tasse
prezzo_finale = round(prezzo * (1 + aliquota), 2)
```

Questi commenti aggiungono **contesto** che il codice da solo non può dire.

### L'Eccellente: Nessun Commento (Codice Auto-Esplicativo)

Spesso, il **miglior commento è un codice ben scritto**:

```python
# Cattivo: codice confuso + commento che spiega
x = y * 0.85           # Applica uno sconto del 15%

# Buono: codice chiaro, nessun commento necessario
SCONTO_PERCENTUALE = 15
prezzo_scontato = prezzo * (1 - SCONTO_PERCENTUALE / 100)

# Eccellente: ancora più chiaro
ALIQUOTA_SCONTO = 0.15  # 15% di sconto
prezzo_scontato = prezzo * (1 - ALIQUOTA_SCONTO)
```

Nel terzo caso, il codice è così chiaro che **un commento sarebbe ridondante**. Il nome della variabile spiega tutto.

Questo è il principio fondamentale: **Un buon nome vale più di un buon commento**.

## 2.5.2 Quando I Commenti Sono Veramente Utili

I commenti sono preziosi in situazioni specifiche. Vediamo quando:

### 1. Spiegare il "Perché", Non il "Come"

```python
# Cattivo: spiega il come (ovvio dal codice)
if ord(carattere) >= 48 and ord(carattere) <= 57:
    # Controlla se il carattere è una cifra

# Buono: spiega il perché
# Validiamo che il primo carattere sia una cifra per evitare
# codici di product che cominciano con lettere (standard ISO 8859)
if ord(carattere) >= 48 and ord(carattere) <= 57:
    codice_valido = True
```

### 2. Documentare Decisioni Non Ovvie o Contro-Intuitive

```python
# Buono: spiega perché usiamo un approccio inusuale
# Usiamo i thread al posto di asyncio perché le librerie legacy
# del progetto non sono async-compatible. Una migrazione è in corso.
thread = threading.Thread(target=process_data)

# Buono: spiega un workaround
# Aggiungiamo un delay di 100ms perché c'è un bug hardware
# nel sensore Bosch BME680 con letture troppo veloci.
# Issue: https://github.com/boschsensortec/BME680_driver/issues/12
time.sleep(0.1)
```

### 3. Documenti Assunzioni Critiche

```python
# Buono: documenta un'assunzione che potrebbe essere violata
# Assumiamo che le temperature siano sempre in Celsius.
# Se ricevi i dati in Fahrenheit, la conversione va qui!
temperatura_celsius = temperatura_input

# Buono: documenta i vincoli
# Questo algoritmo assume che N < 1.000.000. Per dataset più grandi,
# considerare una struttura dati basata su alberi (B-tree)
if len(dati) > 1_000_000:
    raise ValueError("Dataset troppo grande per questo algoritmo")
```

### 4. Fornire Contesto Storico o Riferimenti

```python
# Buono: spiega un fix a un bug specifico
# HOTFIX: Dopo l'aggiornamento a PyPy 7.3.5, il test_performance
# fallisce a causa di JIT compilation timing. Aggiunto retry.
# TODO: Rimuovere quando PyPy sarà aggiornato a 7.4.0
for _ in range(3):
    try:
        risultato = test_performance()
        break
    except TimeoutError:
        time.sleep(1)

# Buono: fornisce contesto e riferimenti
# La formula di Haversine calcola la distanza tra due punti sulla Terra.
# Vedi: https://en.wikipedia.org/wiki/Haversine_formula
# Accurate a ±0.5%
def distanza_haversine(lat1, lon1, lat2, lon2):
    # ... codice ...
```

### 5. Segnalare Intenzione Futura (TODO, FIXME, HACK)

```python
# Buono: segnala lavoro in corso
# TODO: Refactorizzare questo con la nuova libreria utils (ETA: Sprint 3)
def calcola_prezzo_vecchio():
    # implementazione temporanea
    pass

# Buono: segnala un debito tecnico
# HACK: Moltiplicazione per 1000 per evitare arrotondamento con floats
# Questo dovrebbe usare Decimal() dopo il refactor della sezione calcoli
risultato = int(valore * 1000) / 1000

# Buono: segnala un problema noto
# FIXME: Questo fallisce se la stringa contiene emoji
# Il problema è che len() conta i byte, non i caratteri Unicode
if len(stringa) > 100:
    stringa_troncata = stringa[:100]
```

### 6. Sezioni Complesse o Algoritmi Non Ovvi

```python
# Buono: spiega un algoritmo complesso
# Implementazione della ricerca binaria ricorsiva.
# Pre-condizione: l'array deve essere ordinato
# Complessità: O(log n)
# Vedi Capitolo 12 di "Introduction to Algorithms" per dettagli
def ricerca_binaria(arr, target, sinistra=0, destra=None):
    if destra is None:
        destra = len(arr) - 1
    
    if sinistra > destra:
        return -1
    
    mezzo = (sinistra + destra) // 2
    if arr[mezzo] == target:
        return mezzo
    elif arr[mezzo] < target:
        return ricerca_binaria(arr, target, mezzo + 1, destra)
    else:
        return ricerca_binaria(arr, target, sinistra, mezzo - 1)
```

## 2.5.3 La Sintassi dei Commenti: Come Scriverli

### Commenti Singoli: Il Hash `#`

Un commento che inizia con `#` si estende fino alla fine della riga:

```python
x = 5                          # Questo è un commento inline
# Questo è un commento su una riga intera
y = 10
# Commento che spiega la riga successiva
risultato = x + y
```

### Commenti Multipli: Un Hash per Riga

Se volete un commento su più righe, mettete un hash all'inizio di ogni riga:

```python
# Questo è un commento su più righe.
# Continua qui.
# E qui.
# È così che si fa in Python.
x = 5
```

### Commenti Inline vs Su Linea Propria

**Inline (sulla stessa riga del codice):**
```python
x = 5  # Assegnamento iniziale
```

**Su linea propria (sopra il codice):**
```python
# Assegnamento iniziale
x = 5
```

**Buona pratica:** I commenti su linea propria sono generalmente preferibili perché:
1. Non riducono la visibilità del codice
2. Sono più facili da leggere
3. Hanno meno probabilità di spingersi oltre lo schermo
4. Permettono commenti più lunghi

```python
# Preferito: commento su linea propria
# Inizializzziamo il contatore al numero di elementi nel dataset.
# Questo contatore traccia il numero di iterazioni completate.
contatore = len(dataset)

# Meno preferito: commento inline che riduce la leggibilità
contatore = len(dataset)  # Inizializziamo il contatore al numero di elementi nel dataset
```

### Non Usare le Stringhe Multilinea Come Commenti

```python
# Cattivo: le stringhe non sono commenti
"""
Questo potrebbe sembrare un commento
Ma è una stringa non assegnata
E costa memoria
"""

# Buono: usate gli hash
# Questo è un vero commento
# Su più righe
```

(Le stringhe multilinea sono usate per **docstring**, che impareremo nel capitolo sulle funzioni.)

## 2.5.4 La Regola d'Oro: Quando Aggiungere un Commento

Prima di scrivere un commento, chiedetevi:

### 1. "Potrei rendere il codice più chiaro cambiando nomi o struttura?"

**Cattivo:**
```python
# Calcolare l'area del rettangolo
a = 5
b = 3
result = a * b
print(result)
```

**Buono:**
```python
larghezza = 5
altezza = 3
area = larghezza * altezza
print(area)
```

Non avete bisogno di un commento se il codice è auto-esplicativo.

### 2. "Questo commento spiega il 'perché', non il 'come'?"

**Cattivo:**
```python
# Aggiungere 10 a x
x = x + 10
```

**Buono:**
```python
# Aggiungere 10 per convertire da Celsius a Kelvin
x = x + 273.15
```

Il primo commento è ovvio. Il secondo spiega il contesto.

### 3. "Un lettore futuro comprenderà questa decisione senza il commento?"

**Cattivo:**
```python
if lunghezza > 100:
    lunghezza = 100
```

**Buono:**
```python
# Limitiamo la lunghezza a 100 caratteri per compatibilità
# con il database legacy che ha un vincolo VARCHAR(100)
if lunghezza > 100:
    lunghezza = 100
```

Senza il commento, il lettore si chiede: "Perché 100? È un errore? È intenzionale?"

## 2.5.5 Commenti vs Nomi Auto-Esplicativi

La cosa più importante da capire è: **i migliori commenti sono inutili quando il codice è ben scritto**.

### Esempio 1: Valutazione di Polinomi

**Con cattivi nomi + commenti:**
```python
# Valutare il polinomio: 3x³ - 2x² + 3x - 1
x = float(input())
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
```

**Con nomi auto-esplicativi, nessun commento:**
```python
coefficiente_cubico = 3
coefficiente_quadratico = -2
coefficiente_lineare = 3
termine_costante = -1

x = float(input())
y = (coefficiente_cubico * x**3 + 
     coefficiente_quadratico * x**2 + 
     coefficiente_lineare * x + 
     termine_costante)
print("y =", y)
```

Nel secondo caso, il codice **è il commento**.

### Esempio 2: Conversione di Valute

**Cattivo:**
```python
euro = 100
# Tasso di cambio: 1 EUR = 1.10 USD
usd = euro * 1.10
```

**Buono:**
```python
euro = 100
TASSO_CAMBIO_EUR_A_USD = 1.10
usd = euro * TASSO_CAMBIO_EUR_A_USD
```

Il nome della costante è il commento.

## 2.5.6 Commenti per Disabilitare Codice (Debugging)

Durante il testing, spesso volete eseguire il codice con e senza certe righe:

```python
x = 10
y = 20
# z = x + y  # Commentato per testare se il problema è qui
print(x, y)
```

Questo è un uso legittimo dei commenti: **marcare codice che volete disabilitare temporaneamente**.

**Scorciatoia:** In VS Code o la maggior parte degli editor:
- Selezionate le righe
- Premete **Ctrl+/** (Windows/Linux) o **Cmd+/** (Mac)
- Le righe sono commentate/decommentate istantaneamente

```python
# Prima
x = 10
y = 20
z = x + y
print(x, y, z)

# Dopo (selezionare tutto e Ctrl+/)
# x = 10
# y = 20
# z = x + y
print(x, y, z)
```

**Attenzione:** Non lasciate codice commentato nel codice finale. Se non serve, eliminatelo. Se potrebbe servirvi later, usate il **version control** (Git).

## 2.5.7 Laboratorio: Valutare e Migliorare i Commenti

### Scenario

Vi viene dato questo codice con molti commenti:

```python
# Questo programma converte le ore in secondi
# È stato scritto il 15 gennaio 2026

# Variabile per le ore
a = 2

# Costante: numero di secondi in un'ora
secondi_per_ora = 3600

# Calcolo dei secondi totali
print("Ore: ", a)

# Stampare i secondi (commentato per debugging)
# print("Secondi in ore: ", a * secondi_per_ora)

# Qui dovremmo stampare "Goodbye" ma il programmatore non ha avuto tempo
```

### Il Problema

Molti commenti sono **ovvi** o **inutili**. Alcuni aggiungono informazioni non pertinenti (la data). Alcuni spiegano codice commentato senza motivo.

### La Soluzione

**Versione Migliorata:**

```python
# Converte un numero di ore in secondi totali
ore = 2
secondi_per_ora = 3600

print(f"Ore: {ore}")

# Calcolate i secondi totali e stampateli
# (Commentato durante il debugging della conversione)
# secondi_totali = ore * secondi_per_ora
# print(f"Secondi totali: {secondi_totali}")

# TODO: Aggiungere un messaggio di "Goodbye" alla fine
```

### Cosa è Migliorato

1. **Rimossi commenti ovvi**: "Variabile per le ore" è ovvio
2. **Rimossi timestamp personali**: Non pertinenti al codice
3. **Reso il codice autoesplicativo**: `ore` invece di `a`
4. **Migliorato il commento sul codice commentato**: Spiega perché è commentato
5. **Aggiunto TODO**: Indica il lavoro futuro

### Esercizio

Migliorate questo codice:

```python
# Calcolare l'area di un rettangolo
# Scritto da Mario il 16 gennaio

# Assegnare la larghezza
l = 5
# Assegnare l'altezza
a = 3
# Moltiplicare per ottenere l'area
area = l * a
# Stampare il risultato
print("Area =", area)

# Non dimenticare di aggiungere la circonferenza later
```

**Cosa fare:**
1. Eliminate commenti ovvi
2. Ringrossate i nomi di variabili
3. Aggiungete un commento significativo se ce n'è bisogno
4. Migliorate il TODO

## Conclusione: La Filosofia dei Commenti

Ricordate:

✅ **Scrivete commenti per il "perché"**
- Perché avete scelto questo approccio
- Perché questa costante ha questo valore
- Perché il codice sembra strano

❌ **Non scrivete commenti per il "come"**
- Il codice già lo dice
- Rischio di disinformazione
- Rumore ridondante

✅ **Fate in modo che il codice parli da solo**
- Nomi di variabili significativi
- Funzioni ben nominate
- Struttura logica chiara

❌ **Non usate commenti per compensare codice confuso**
- Riscrivete il codice, non commentatelo

La regola d'oro: **Se state scrivendo un commento per spiegare cosa il codice fa, probabilmente potete scrivere il codice in modo più chiaro**.

I migliori programmatori scrivono **meno commenti**, non più, perché il loro codice è così chiaro che i commenti sono inutili. Quando aggiungono commenti, aggiungono **valore reale**.

Aspirate a questo standard.