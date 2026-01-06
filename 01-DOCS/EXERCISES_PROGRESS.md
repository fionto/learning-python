# 📂 CS50P Technical Activity Log

**Repository:** learning-python
**Last Update:** 06/01/2026
**Environment:** Python 3.x, VS Code
**Status:** In Progress (Chapters 1-6 Covered)
**Valutatore:** Gemini

---

## 🛠️ Stack Inventory
Riepilogo delle primitive e dei pattern implementati nel codebase attuale.

### Core Constructs
* **Strings:** Parsing (`split`, `strip`), Formatting (`f-strings`, `title`, `upper`), Sanitization (`removeprefix`).
* **Data Structures:**
    * `List`: Mutability, Slicing `[start:stop:step]`, Methods (`append`, `insert`, `pop`).
    * `Set`: Membership testing (`in`), Deduplication.
    * `Tuple`: Immutable data passing.
    * `Dictionary`: Key-Value storage, Data aggregation, Safe access via `.get()`.
* **Control Flow:**
    * Iterative: `for` loops, `range()`, `enumerate()`, List Comprehensions, Dict Iteration (`.items()`, `.keys()`, `.values()`).
    * Conditional: `if/elif/else`, `match/case` (Python 3.10), Ternary operators.
    * Logic: Boolean flags, Guard Clauses, Membership testing (`not in`).

---

## 📜 Change Log & Implementation Details

### 📂 Module: String Manipulation
* **Source:** `Day01_strings.md`
* **Coverage:** 13 Scripts.
* **Key Implementations:**
    * **Method Chaining:** Implementata sequenza `.strip().title()` per normalizzazione input.
    * **Prefix Handling:** Utilizzo di `removeprefix()` per pulizia URL, sostituendo slicing manuale.
    * **Search:** Utilizzo di `.find()` per localizzazione sottostringhe.

### 📂 Module: Data Structures & Loops
* **Source:** `Day02_lists.md`, `Day03_for_loops.md`, `Day07_ListComprehensions.md`
* **Coverage:** 33 Scripts.
* **Key Implementations:**
    * **Memory Management:** Dimostrazione comportamento *by reference* vs *by value* (copia) su tipi mutabili.
    * **Iteration Logic:**
        * Reverse iteration implementata tramite 3 pattern: `reversed(range())`, `reversed(iterable)`, slicing `[::-1]`.
        * Nested loops per generazione matrici/tabelline.
    * **Optimization:** Refactoring di cicli `for` standard in **List Comprehensions** per filtraggio e mappatura dati.
        * *Pattern:* `[x for x in list if condition]`
        * *Pattern:* `[x if condition else y for x in list]`

### 📂 Module: Control Flow & Logic
* **Source:** `Day06_ifStatements.md`
* **Coverage:** 7 Scripts.
* **Key Implementations:**
    * **Refactoring:** Conversione da Nested-Ifs a Flat-Ifs per migliorare leggibilità.
    * **Validation Logic:** Implementazione controlli multipli (spazi, lunghezza, tipo) aggregati in variabile booleana unica.
    * **Sanitization:** Gestione case-insensitive (`.lower()`) pre-validazione.

### 📂 Module: Dictionaries
* **Source:** `97_RaccoltaEsercizi.md`
* **Coverage:** 10 Scripts.
* **Key Implementations:**
    * **Iterazione Avanzata:** Implementazione di cicli ottimizzati su `.items()` per coppie chiave-valore e `.values()` per estrazione dati aggregati.
    * **Accesso Sicuro:** Utilizzo del metodo `.get(key, default)` per prevenire `KeyError` e gestire contatori iniziali (`05_frutta2`).
    * **Inizializzazione Dinamica:** Gestione di chiavi inesistenti tramite controllo di appartenenza (`if key not in dict`) prima di operazioni di mutazione come `.append()` (`08_sensori`).
    * **Data Parsing:** Raffinamento dello `.split()` per gestire whitespaces variabili e pulizia manuale della punteggiatura via `.replace()` (`04_frasi2`).

---

## 🏗️ Project Architecture Log

### Project: Bio-Informatic Data Parser
* **File:** `single-record-parser.py`
* **Type:** Single-file Script
* **Constraints:** No Conditional Statements (`if`), No Loops (`for/while`).
* **Features:**
    * **Input Processing:** Parsing stringa delimitata da separatori custom (`:`).
    * **Data Transformation:** Generazione ID univoco tramite slicing stringhe e casting MAIUSCOLO.
    * **Math:** Calcolo range (min/max) con arrotondamento a 3 decimali.
    * **Output:** Generazione struttura Dizionario con Tupla annidata per i limiti.

### Project: Batch Signal Processor
* **File:** `batch-signal-processor.py`
* **Type:** Data Processing Pipeline
* **Features:**
    * **Pipeline:** Input List -> Cleaning (`strip`) -> Parsing (`split`) -> Validation -> Aggregation.
    * **Pattern Matching:** Utilizzo costrutto `match/case` per mappatura codici errore (Python 3.10+).
    * **Flow Control:** Utilizzo `continue` (Guard Clauses) per skip immediato dati corrotti.
    * **State Management:** Accumulo statistiche in variabili locali e incapsulamento finale in dizionario report.
    * **Validation:** Controllo parità su interi e validazione tipo dato.

---

## 📊 Metrics Summary

| Modulo | Script/Funzioni | Stato | Note |
| :--- | :--- | :--- | :--- |
| **Strings** | 13 | Executed | Metodi built-in e sanitizzazione |
| **Lists** | 11 | Executed | Mutabilità e metodi CRUD |
| **Loops** | 14 | Executed | Iterazione classica e slicing |
| **Condizionali** | 7 | Executed | Logica booleana e refactoring |
| **Comprehensions** | 8 | Executed | Sintassi concisa per trasformazioni |
| **Dictionaries** | 10 | Executed | Gestione chiavi, `.get()` e annidamento |
| **Projects** | 2 | Completed | Rispetto vincoli architetturali |