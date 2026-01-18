# 🚀 Projects Activity Log - Consolidation & Integration

**Repository:** learning-python  
**Last Update:** 17/01/2026  
**Environment:** Python 3.12.10, VS Code  
**Status:** 3 Major Projects Completed  
**Total Project Code:** 300+ lines  

---

## 📊 Projects Overview

| Progetto | Difficoltà | Concetti Chiave | Stato |
| :--- | :--- | :--- | :--- | :--- |
| **01 - Bio-Informatic Single Record Parser** | Elementary | Parsing, String Methods, Type Casting, Validation (No-If) | ✅ Completato |
| **02 - Batch Signal Processor** | Medium | Loops, Validation, Match-Case, Aggregation | ✅ Completato |
| **03 - Aggregated Telemetry Analyzer** | Medium/High | Nested Dicts, Sets, While Loops, State Aggregation | ✅ Completato |

---

## 📂 Progetto 01: Bio-Informatic Single Record Parser

### 📋 Descrizione
Sistema di parsing e validazione per dati scientifici grezzi provenienti da strumenti di analisi biologica. Il programma pulisce dati sporchi, calcola margini di errore e valida campioni senza usare strutture condizionali.

### 🎯 Obiettivi Didattici
- Manipolazione avanzata di stringhe (title case, sostituzione, strip)
- Conversione di tipi (casting str → float)
- Generazione di codici univoci tramite string slicing
- Validazione tramite set membership (senza if)
- Costruzione di dizionari strutturati

### 📥 Formato Input
```
" ID_Grezzo : NOME_CAMPIONE : VALORE_MISURATO : ERRORE_STRUMENTO "
Esempio: " id-2021 : mArS_sOiL-sAmPlE : 12.500 : 0.15 "
```

### 🛠️ Organizzazione Codice
```
main()
├── pulisci_stringa()        # Parsing e normalizzazione
├── genera_codice()           # Estrazione e composizione
└── calcolo_range()           # Conversione numerica
```

### 📌 Vincoli Tecnici
- ✅ NO condizionali (if/else/elif)
- ✅ NO cicli (for/while)
- ✅ Obbligatori: main() + funzioni di supporto
- ✅ Type hints facoltativi ma consigliati

### 🎓 Concetti Consolidati
- **String Methods Avanzati:** `.title()`, `.replace()`, `.strip()`, `.upper()`, string slicing
- **Type Casting:** `float()` per conversione sicura
- **Tuple:** Rappresentazione di coppie di valori (min/max)
- **Set Membership:** Validazione booleana senza if
- **Dictionary Construction:** Aggregazione dati eterogenei
- **Function Decomposition:** Separazione di responsabilità

### ✨ Aspetti Innovativi
1. **Constraint Programming:** Risolvere il problema di validazione senza condizionali
2. **Tupla per Range:** Scelta strutturale elegante per min/max
3. **Set-Based Validation:** Pattern funzionale vs. imperativo

---

## 📂 Progetto 02: Batch Signal Processor

### 📋 Descrizione
Sistema di monitoraggio per sensori perimetrali di una base spaziale. Analizza lista di segnali, scarta dati corrotti, classifica minacce e determina livello di allerta generale tramite match-case statement.

### 🎯 Obiettivi Didattici
- Iterazione su liste con `for` loop
- Validazione dati (numericità, parità)
- Pattern matching con `match-case` (Python 3.10+)
- Aggregazione statistiche
- Logica decisionale multi-criterio
- String methods per validazione (`.isdigit()`)

### 📥 Formato Input
```
" ID_SEGNALE | CODICE_ZONA | TIPO_MINACCIA | LIVELLO_INTENSITA "
Esempio: " 4420 | SEC_01 | RAD | 45.5 "
```

### 🛠️ Organizzazione Codice
```
main()
├── pulisci_segnali()        # Parsing e filtraggio
├── match_minaccia()          # Classificazione match-case
└── [logica allerta inline]   # Nel main per semplicità
```

### 📌 Vincoli Tecnici
- ✅ Uso obbligatorio di `for` loop
- ✅ Uso obbligatorio di `continue` per skip
- ✅ Uso obbligatorio di `match` statement
- ✅ Funzioni di supporto (min 1)
- ✅ Nessun vincolo su eleganza

### 🎓 Concetti Consolidati
- **For Loop Patterns:** Iterazione con guard clauses
- **Continue Statement:** Skip intelligente di elementi
- **String Validation:** `.isdigit()` per numericità
- **Match-Case:** Pattern matching vs. if-elif cascata
- **Aggregation:** Accumulo di statistiche durante iterazione
- **Set Operations:** Membership testing con `in`
- **Floating Point Arithmetic:** Accumulo di float con precisione

### ✨ Aspetti Innovativi
1. **Checksum ID:** Validazione multi-step (alfanumericità + parità)
2. **Match-Case per Semantica:** Classificazione più leggibile che if-elif
3. **Flag per Stato Complesso:** `rischio_grave` per tracciare minacce critiche

---

## 📂 Progetto 03: Aggregated Telemetry Analyzer

### 📋 Descrizione
Sistema avanzato di analisi telemetria per log di manutenzione della Stazione Spaziale Internazionale (ISS). Processa report giornalieri dai moduli, identifica anomalie critiche e genera rapporto di stato aggregato con metriche complesse.

### 🎯 Obiettivi Didattici
- Nested dictionaries per strutture dati complesse
- Set per tracciamento di valori unici
- While loops con `.pop()` per processing distruttivo
- Match-case con guard clauses (`if` dentro match)
- Calcolo medie incrementali (media mobile)
- String processing per date (inversione formato)
- Aggregazione multi-livello

### 📥 Formato Input
```
"MODULO#TIMESTAMP#SISTEMA#STATO#PRIORITA"
Esempio: "COLUMBUS#02012026-1430#Life Support#95#LOW"

Dove:
- MODULO: Codice modulo (es. "COLUMBUS", "DESTINY")
- TIMESTAMP: Formato GGMMAAAA-HHMM
- STATO: 0-100 (efficienza percentuale)
- PRIORITA: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
```

### 🛠️ Organizzazione Codice
```
main()
├── while loop con .pop()
│   ├── Validazione strutturale
│   ├── Parsing componenti
│   ├── check_emergenza()      # Classificazione match-case
│   └── Aggregazione nested dict
├── invert_date()              # Helper per date
├── check_emergenza()          # Match-case con guards
└── Stampa formattata
```

### 📌 Vincoli Tecnici
- ✅ Uso obbligatorio di `while` loop (non for)
- ✅ Uso obbligatorio di `match-case`
- ✅ Uso obbligatorio di dizionari annidati
- ✅ Uso obbligatorio di set per alerts
- ✅ NO list comprehension
- ✅ NO try-except (validazione manuale)
- ✅ Max 2 funzioni helper

### 🎓 Concetti Consolidati
- **Nested Dictionaries:** Strutture multi-livello con accesso sicuro
- **Set Operations:** Deduplicazione automatica, membership O(1)
- **While Loops Avanzati:** Iterazione distruttiva con `.pop()`
- **Match-Case Avanzato:** Guard clauses `if` dentro match
- **Media Incrementale:** Algoritmo Welford senza storing tutti i dati
- **String Manipulation:** Inversione data per comparazione lessicale
- **Aggregation Patterns:** Raggruppamento multi-criterio
- **State Management:** Tracking complesso di moduli e anomalie

### ✨ Aspetti Innovativi
1. **While + Pop Pattern:** Processamento distruttivo efficiente
2. **Media Incrementale:** Calcolo online senza list completa
3. **Set per Critical Alerts:** Deduplicazione automatica
4. **Match-Case Guard Clauses:** Syntax elegante e pattern-based
5. **Nested Dict Navigation:** Accesso sicuro senza try-except

### 🏆 Complessità Tecnica

| Aspetto | Livello | Dettagli |
| :--- | :--- | :--- |
| **Parsing** | Medium | Split multiplo, validazione strutturale |
| **Algoritmi** | Medium | Media incrementale, massimo cronologico |
| **Data Structures** | High | Nested dicts 3+ livelli, set management |
| **State Tracking** | High | Aggregazione per chiave con metriche multiple |
| **Control Flow** | Medium | Match-case con guards, while con pop |

---

## 📊 Comparazione Progetti

| Aspetto | Progetto 01 | Progetto 02 | Progetto 03 |
| :--- | :--- | :--- | :--- |
| **Linee Codice** | ~80 | ~120 | ~180 |
| **Funzioni** | 4 | 3 | 3 |
| **Difficoltà** | Easy | Medium | Medium-High |
| **Data Structures** | Dict, Tuple, Set | Dict, List, String | Dict (nested), Set, List |
| **Loops** | None | For | While |
| **Conditionals** | None | If/Elif | Match-Case + If |
| **String Methods** | High | Medium | Medium |
| **Numeric Ops** | Medium | Medium | High (media) |
| **Validation** | String-based | Numeric + String | Multi-level |
| **Output** | Simple Dict | Formatted String | Complex Nested |

---

## 🎯 Concetti Trasversali Consolidati

### Tier 1: Fondamentali
- ✅ String methods (`.strip()`, `.split()`, `.replace()`, `.title()`, `.upper()`)
- ✅ Type casting (`int()`, `float()`)
- ✅ Dictionary operations (creazione, accesso, aggiornamento)
- ✅ Set operations (membership, deduplicazione)
- ✅ Tuple unpacking e creazione

### Tier 2: Intermedi
- ✅ For loop con `continue` e `enumerate()`
- ✅ While loop con `break` e `.pop()`
- ✅ Match-case statement (Python 3.10+)
- ✅ Nested data structures
- ✅ String indexing e slicing

### Tier 3: Avanzati
- ✅ Nested dictionaries (3+ livelli)
- ✅ Set-based validation (no-if patterns)
- ✅ Media incrementale (running average)
- ✅ Match-case con guard clauses
- ✅ Distruttive iteration (`.pop()`)
- ✅ String processing for dates (chronological order)

### Tier 4: Architetturali
- ✅ Function decomposition (separation of concerns)
- ✅ Data aggregation patterns
- ✅ Multi-criteria decision logic
- ✅ State management in complex systems
- ✅ Output formatting (structured vs. formatted)

---

## 📈 Progressione Didattica

```
Progetto 01 (Easy)
├─ String manipulation
├─ Type casting
├─ No-if validation (constraint programming)
└─ Simple output

    ↓ (Complexity increases)

Progetto 02 (Medium)
├─ Loops con guard clauses
├─ String validation (.isdigit())
├─ Match-case statement
├─ Aggregation (contatori)
└─ Formatted output

    ↓ (Complexity increases)

Progetto 03 (Medium-High)
├─ Nested data structures
├─ Distruttive iteration (.pop)
├─ Match-case con guards
├─ Complex aggregation (nested)
├─ Advanced algorithms (running mean)
└─ Complex formatted output
```

---

## 🎓 Capitoli PCC Connessi

| Progetto | Capitolo PCC | Concetti Principali |
| :--- | :--- | :--- |
| **01 - Parser** | 2, 3, 6 | Stringhe, Liste, Dizionari (base) |
| **02 - Batch Processor** | 4, 5, 8 | Loops, Conditionals, Functions, Match |
| **03 - Telemetry Analyzer** | 5, 6, 7, 8 | Conditionals (avanzati), Dicts, Functions, Loops |

---

## 📋 Metriche Consolidamento

```
Stack Inventory Completato:
✅ String Methods: strip, split, replace, title, upper, find, isdigit
✅ Type Casting: str → int, str → float
✅ Data Structures: dict, list, set, tuple
✅ Loops: for (with continue), while (with pop, break)
✅ Conditionals: if/elif/else, match-case (with guards)
✅ Operators: in (set/list), %, //, **
✅ Algorithms: aggregation, running average, validation
✅ Patterns: guard clauses, set-based validation, nested dicts
```