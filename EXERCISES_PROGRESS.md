# Exercises Summary - Python Crash Course

Riepilogo di tutti gli esercizi completati, organizzato per capitolo.

---

## Capitolo 2: Variabili e Tipi Dati Semplici

### Esercizi del Libro
**Status**: ✅ Completati  
**Totale**: 12 esercizi (2-1 a 2-12)

### Esercizi Custom - Stringhe (5)

| Esercizio | Concetti | Note |
|-----------|----------|------|
| `formatta_nome.py` | .strip(), .title() | Method chaining su stringhe |
| `messaggio_benvenuto.py` | F-string, variabili | Embedding di variabili in f-string |
| `pulisci_url.py` | .removeprefix(), chaining | Rimozione multipli prefissi |
| `trova_e_sostituisci.py` | .replace() | Sostituzione di sottostringhe |
| `analizza_stringa.py` | .find(), len(), .strip() | Combinazione di metodi string |

**Concetti consolidati**: Method chaining, f-string formatting, immutabilità stringhe

---

## Capitolo 3: Introduzione alle Liste

### Esercizi del Libro
**Status**: ✅ Completati  
**Totale**: 11 esercizi (3-1 a 3-11)

### Esercizi Custom - Liste (5)

| Esercizio | Concetti | Note |
|-----------|----------|------|
| `gestione_playlist.py` | .insert(), .pop(), .sort(), reversed() | Aliasing vs. copia, operazioni in-place |
| `classifica_videogiochi.py` | Indexing, .reverse(), len() | Accesso e modifica elementi |
| `libreria_personale.py` | .count(), .clear(), .copy() | Scoperta autonoma nuovi metodi |
| `gestione_queue.py` | .pop(0), .remove() | FIFO/LIFO concepts con liste |
| `analisi_temperature.py` | .index(), sorting, .append() | Ricerca elementi, ordinamento |

**Concetti consolidati**: Mutabilità liste, methods in-place vs. non-in-place, aliasing vs. copia, ricerca autonoma metodi

---

## Capitolo 4: Lavorare con le Liste

### Esercizi del Libro
**Status**: ✅ Completati (sezioni principali)  
**Totale**: 15 esercizi (4-1 a 4-15)

### Esercizi Custom - For Loops (Set 1: Elementare) (5)

| Esercizio | Concetti | Output |
|-----------|----------|--------|
| `somma_numeri.py` | For loop, accumulazione | Somma elementi lista |
| `stringa_invertita.py` | range() negativo, stringhe | Stampa caratteri al contrario |
| `filtra_lista.py` | For loop, .append() | Lista filtrata con numeri pari |
| `lunghezza_stringhe.py` | len(), f-string, lista | Stampa lunghezza ogni parola |
| `tabellina_nested.py` | Nested loops, range() | Tabelline 5x5 |

**Concetti**: For loop basics, range objects, accumulazione, nested loops

---

### Esercizi Custom - For Loops (Set 2: Incrementale) (5+)

| Esercizio | Concetti | Difficoltà |
|-----------|----------|-----------|
| `somma_ultimi_tre.py` | Slicing negativo, for loop | ⭐⭐ |
| `copia_invertita.py` | For loop, .append(), reversed() | ⭐⭐ |
| `concatenazione_maiuscole.py` | .capitalize(), concatenazione stringhe | ⭐⭐ |
| `caratteri_alternati.py` | Slicing con step, stampa | ⭐⭐ |
| `lista_coppie.py` | For loop, liste annidate | ⭐⭐⭐ |

**Concetti consolidati**: Slicing positivo/negativo, range() con step, for loop avanzati, concatenazione stringhe

---

### Esercizi Completati da Chat Diretta

| Esercizio | Codice | Concetti |
|-----------|--------|----------|
| Esercizio 4: Lunghezza animali | `animali = ["gatto", "elefante", "ape", "dinosauro"]` | .capitalize() in f-string, len() |
| Esercizio 5: Tabelline | `range(1, 6)` x2 nested | Loop nidificati, `range(start, stop)` |

---

## 🚀 Progetti Intermedi

Progetti complessi che integrano concetti da più capitoli, sviluppati parallelamente agli esercizi standard.

---

### Progetto 01: Bio-Informatic Data Parser v1.0

**Data completamento**: 31 dicembre 2024  
**Capitoli coinvolti**: 2 (Stringhe), 3 (Liste), 8 (Funzioni base)

**Obiettivo**: Sistema di parsing e validazione per dati scientifici grezzi provenienti da sensori, con trasformazione in record strutturati.

#### Specifiche Tecniche
- **Input**: Stringa grezza formato `"ID : NOME : VALORE : ERRORE"`
- **Output**: Dizionario con campi puliti, codice univoco, e range calcolato
- **Vincoli**: NO condizionali, NO loop, architettura funzionale obbligatoria

#### Metriche Codice
- **Linee di codice**: ~60
- **Funzioni**: 4 (`main()`, `pulisci_stringa()`, `genera_codice()`, `calcolo_range()`)
- **Complessità ciclomatica**: 1 (nessun branching)

#### Concetti Applicati
- **String methods**: `.strip()`, `.split()`, `.title()`, `.replace()`, `.upper()`, `[:n]` slicing
- **Type conversion**: `float()`, casting esplicito
- **Data structures**: Liste, Dizionari, Tuple (per dati immutabili)
- **Set membership**: Validazione con `in` operatore su Set
- **Function design**: Separazione responsabilità, single purpose functions

#### Tecniche Avanzate Scoperte
- **Method chaining complesso**: `stringa.strip().title().replace("-", " ").replace("_", " ")`
- **Slicing combinato**: `sensore[:3].upper() + id[-2:]` per generazione codice
- **Set per lookup O(1)**: `{"MAR21", "VEN22", ...}` invece di lista

#### Aree di Miglioramento Identificate
- **Input validation**: Aggiungere controlli su lunghezza lista dopo `.split()` (richiede `if` - Cap. 5)
- **Error handling**: Gestire conversioni numeriche fallite (richiede `try-except` - Cap. 10)
- **Unpacking**: Sostituire indici numerici con unpacking `id, nome, valore, errore = lista.split()` (Cap. 6+)
- **Type hints return**: Completare signature funzioni con `-> type`

#### Documentazione
- **README professionale**: Con analisi evolutiva del processo di sviluppo
- **Commenti header**: Specifiche complete nel file sorgente
- **Tracking evolutivo**: Log delle iterazioni e debugging

---

### Progetto 02: Batch Signal Processor (Protocollo Sicurezza Base Alpha)

**Data completamento**: 2 gennaio 2025  
**Capitoli coinvolti**: 2-5 (Stringhe, Liste, For Loops, Conditionals, Match)

**Obiettivo**: Sistema di analisi batch per segnali da sensori perimetrali con validazione multi-livello, classificazione minacce e generazione report aggregato.

#### Specifiche Tecniche
- **Input**: Lista di stringhe grezze formato `"ID | ZONA | TIPO | INTENSITÀ"`
- **Output**: Report aggregato con statistiche e stato allerta calcolato
- **Logica decisionale**: Algoritmo a cascata con 3 livelli di allerta

#### Metriche Codice
- **Linee di codice**: ~95 (+58% vs Progetto 01)
- **Funzioni**: 3 (`main()`, `pulisci_segnali()`, `match_minaccia()`)
- **Complessità ciclomatica**: 8 (logica ramificata complessa)
- **Livelli di validazione**: 3 (stringhe vuote, formato ID, parità)

#### Concetti Applicati
- **Loop control**: `for` loop con `continue` per early exit
- **Conditionals**: `if/elif/else` con condizioni composite (`and`/`or`)
- **Pattern matching**: `match/case` statement con wildcard `_`
- **Boolean flags**: Gestione stato con variabili booleane (`rischio_grave`)
- **Type hints**: Annotazioni complete su parametri (`list[str]`)
- **Chained comparisons**: `100 <= x <= 200` (pythonic range check)

#### Tecniche Avanzate Scoperte
- **`.isdigit()`**: Ricerca autonoma metodo per validazione numerica
- **`enumerate()`**: Pattern per modifica in-place di liste
- **Validazione a cascata**: Fail-fast pattern con multiple early returns
- **Set per lookup critico**: `MINACCE_CRITICHE = {"Radiazioni", ...}` per O(1) membership

#### Naming Semantico Professionale
```python
is_invalid_format = not componenti_segnale[0].isdigit()
is_not_valid_id = id_int % 2 != 0
stringa_vuota = not segnale_str
```
- Prefisso `is_` per booleani
- Variabili auto-documentanti che eliminano necessità di commenti

#### Pattern Architetturali
- **Separation of Concerns**: Parsing separato da validazione separato da classificazione
- **Single Responsibility**: Ogni funzione ha uno scopo preciso
- **Data Flow Lineare**: Input → Pulizia → Validazione → Aggregazione → Decisione → Output

#### Aree di Miglioramento Identificate
- **Chiavi dizionario**: Standardizzare formato (attualmente Title Case invece di snake_case)
- **Type hints return**: Aggiungere `-> list[list[str]]` e `-> str` alle funzioni
- **List comprehension**: Refactoring loop `enumerate()` quando studiata (fine Cap. 4)
- **Docstrings**: Aggiungere documentazione funzioni in stile Google (Cap. 8+)
- **Loop optimization**: Considerare `break` quando trovata minaccia critica (Cap. 7)

#### Evoluzione Rispetto a Progetto 01

| Aspetto | Progetto 01 | Progetto 02 | Crescita |
|---------|-------------|-------------|----------|
| **Strutture controllo** | Nessuna | `for`, `if`, `continue`, `match` | Salto di livello |
| **Validazione** | Assente | Multi-layer (3 livelli) | +80% robustezza |
| **Complessità logica** | Lineare | Ramificata con decisioni composite | Pensiero algoritmico |
| **Type hints** | Assenti | Presenti su parametri | Best practice adottata |
| **Ricerca autonoma** | 0 metodi | 2 metodi (`.isdigit()`, `enumerate()`) | Crescita esplorativa |

#### Documentazione
- **Testo esercizio completo**: Specifiche dettagliate in Markdown separato
- **Test cases multipli**: 3 liste di test con scenari diversi
- **Output formattato**: Report professionale con tabellazione

---

## Riassunto Complessivo

### Totale Esercizi per Tipo

| Tipo | Numero | Status |
|------|--------|--------|
| Esercizi Libro | 38 | ✅ Completati |
| Esercizi Custom | 15+ | ✅ Completati |
| **Progetti Intermedi** | **2** | **✅ Completati** |
| **Totale** | **55+** | **✅** |

### Capitoli Covered

- ✅ Capitolo 1: Setup (completato)
- ✅ Capitolo 2: Stringhe + 5 custom (completato)
- ✅ Capitolo 3: Liste + 5 custom (completato)
- 📄 Capitolo 4: For Loops + 10+ custom (in corso - consolidamento)

---

## Metodologia

**Per ogni capitolo:**
1. Completa esercizi dal libro
2. Crea 5 esercizi custom di difficoltà crescente
3. Documenta concetti in Markdown
4. Commit e push su GitHub

**Per progetti intermedi:**
1. Integrazione concetti da multipli capitoli
2. Specifiche tecniche dettagliate in file separato
3. Documentazione evoluzione processo sviluppo
4. Code review e identificazione aree miglioramento future

**Criteri di completamento:**
- Tutti gli esercizi svolti
- Comprensione dimostrata
- Pronto al capitolo successivo

---

## Note Finali

- Gli esercizi custom includono sempre ricerca autonoma di nuovi metodi/funzioni
- Attenzione costante a PEP8 e best practices
- Focus su consolidamento prima di passare al prossimo capitolo
- Nessun salto a capitoli successivi fino a comprensione solida
- I progetti intermedi sono tracciati separatamente per future iterazioni e miglioramenti

---

**Ultimo aggiornamento**: 2 gennaio 2025  
**Prossimo passo**: Completare Set 2 for loops, poi capitolo 5 (if statements)