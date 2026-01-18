# 📂 Exercises Activity Log

**Repository:** learning-python
**Last Update:** 17/01/2026
**Environment:** Python 3.12.10, VS Code
**Status:** In Progress (Chapters 1-7 Covered)
**Total Exercises:** 90+

---

## 🛠️ Stack Inventory
Riepilogo delle primitive e dei pattern implementati nel codebase attuale.

### Core Constructs
* **Strings:** Parsing (`split`, `strip`, `find`, `partition`), Formatting (`f-strings`, `title`, `upper`), Sanitization (`removeprefix`), Validation (`.isalnum()`).
* **Data Structures:**
    * `List`: Mutability, Slicing `[start:stop:step]`, Methods (`append`, `insert`, `pop`), Slice Assignment.
    * `Set`: Membership testing (`in`), Deduplication.
    * `Tuple`: Immutable data passing, Unpacking.
    * `Dictionary`: Key-Value storage, Data aggregation, Safe access via `.get()`, Iteration (`.items()`, `.keys()`, `.values()`), `.popitem()`.
* **Control Flow:**
    * Iterative: `for` loops, `range()`, `enumerate()`, List Comprehensions, `while` loops with `break`/`continue`.
    * Conditional: `if/elif/else`, `match/case` (Python 3.10), Ternary operators, Guard Clauses.
    * Logic: Boolean flags, Membership testing (`in`, `not in`), Early exit patterns.
* **Advanced Patterns:** Input validation loops, Statistical computing, Queue management, Fixed-format parsing, Anti-pattern refactoring (DRY principle).

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

### 📂 Module: While Loops
* **Source:** `04_02_WhileLoops`
* **Coverage:** 9 Scripts.
* **Key Implementations:**
    * **Input Validation:** Cicli while infiniti con `break` come pattern preferito per validazione iterativa. Password validator con 4 criteri (lunghezza, maiuscole, cifre, speciali). Tre varianti progressive di refactoring.
    * **Refactoring Anti-Pattern:** Eliminazione cascate di `if` ridondanti tramite strutture dati (liste di tuple). Pattern DRY per scalabilità.
    * **Statistical Computing:** Mediana (pari/dispari), moda, numeri ripetuti usando `.count()`, `sorted()`, dizionari senza librerie esterne.
    * **Queue Management:** `insert(0, elem)` per prioritization emergenze e `.pop(0)` per FIFO.
    * **String Validation:** `.isalnum()`, `.startswith()`, `.endswith()` per validazione codici seriali.
    * **Dictionary Emptying:** Pattern svuotamento controllato con `.popitem()` durante iterazione.
    * **String Parsing (Non-Standard):** `.find()` e `.partition()` per parsing senza `.split()` da stringhe strutturate.

### 📂 Module: Slicing
* **Source:** `05-Slicing`
* **Coverage:** 8 Scripts (+ 1 variante).
* **Key Implementations:**
    * **Basic Slicing:** Estrazione indici positivi/negativi (`testo[:5]`, `testo[-4:]`) e intervalli.
    * **Omitted Parameters:** Pattern abbreviati `[:4]`, `[4:]`, `[::-1]` (reverse completo).
    * **Step Parameter:** Intervalli con `[::2]`, `[1::3]`, `[::-2]` (inverso saltato).
    * **Copy vs. Reference:** Shallow copy `colori[:]` con verifica invarianza; immutabilità stringhe (TypeError atteso).
    * **Negative Indexing Advanced:** Slicing combinato con indici negativi e step negativo.
    * **Slice Assignment:** Sostituzione porzioni `dati[1:3] = [99, 88, 77]` e rimozione `del dati[-2:]`.
    * **Fixed-Format Parsing:** Estrazione da log strutturato con `.find()` e slicing; ricomposizione inversa.

    ---

## 📊 Metrics Summary

| Modulo | Script/Funzioni | Stato | Note |
| :--- | :--- | :--- | :--- |
| **Strings** | 13 | Executed | Metodi built-in e sanitizzazione |
| **Lists** | 11 | Executed | Mutabilità e metodi CRUD |
| **For Loops** | 14 | Executed | Iterazione classica e list comprehensions |
| **Condizionali** | 7 | Executed | Logica booleana e refactoring |
| **Comprehensions** | 8 | Executed | Sintassi concisa per trasformazioni |
| **Dictionaries** | 10 | Executed | Gestione chiavi, `.get()` e annidamento |
| **While Loops** | 9 | Executed | Input validation, statistics, parsing |
| **Slicing** | 9 | Executed | Indici, step, assignment, fixed-format parsing |
| **TOTAL** | **81+** | Executed | Capitoli 1-6 + approfondimenti |