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
**Status**: ✅ Completati  
**Totale**: 15 esercizi (4-1 a 4-15)

### Esercizi Custom - For Loops (Set 1 + Set 2: 10+)

| Esercizio | Concetti | Difficoltà |
|-----------|----------|-----------|
| Somma dei numeri | Accumulazione, for loop | ⭐ |
| Stampa invertita stringa (4 metodi) | range() negativo, reversed(), slicing step | ⭐⭐ |
| Filtraggio lista | For loop, .append(), logica | ⭐ |
| Lunghezza stringhe | len(), f-string, .capitalize() | ⭐ |
| Tabelline nidificate | Nested loops, range() | ⭐⭐ |
| Somma ultimi tre | Slicing negativo | ⭐⭐ |
| Copia invertita | reversed(), .append() | ⭐⭐ |
| Concatenazione maiuscole | Method chaining (.capitalize()), += | ⭐⭐ |
| Caratteri alternati | Slicing con step | ⭐⭐ |
| Lista di coppie | Nested list, for loop | ⭐⭐⭐ |

**Concetti consolidati**: For loops, range objects vs liste, slicing avanzato, nested loops, iterator objects, method chaining

### Mega-Progetto: Bio-Informatic Data Parser v1.0

**Valutazione**: A (95/100)  
**Concetti applicati**: 
- Set (per O(1) membership testing)
- Tuple (per dati immutabili)
- Dictionary (strutture complesse)
- String methods (method chaining)
- Slicing (positivo, negativo, step)
- Function design (Single Responsibility)

**Highlights**:
- Primo progetto multi-funzione complesso
- Uso creativo di Set per validation senza condizionali
- Documentazione README professionale
- Gestione dati strutturati e parsing

**Link valutazione**: Code review per esercizi intermedi

---

## Capitolo 5: Istruzioni if

**Status**: ✅ Completato  
**Esercizi del Libro**: Non completati (approccio pragmatico — esercizi giudicati elementari)

**Concetti da Code Review e applicazione pratica**:
- Esercizio intermedio Parser ha richiesto approfondimento autonomo su **Shadowing** e **Keywords**
- Consolidamento attraverso analisi errori reali nel progetto

---

## Capitolo 6: Dizionari

**Status**: ✅ Completato  
**Esercizi del Libro**: Non completati (stessa strategia di Cap. 5)

**Mega-Progetto Parser consolida**:
- Strutture dati multi-livello
- Annidamento (liste di dizionari, dizionari dentro dizionari)
- Accesso e manipolazione di dati complessi

---

## Riassunto Complessivo

### Totale Esercizi per Tipo

| Tipo | Numero | Status |
|------|--------|--------|
| Esercizi Libro | 53 | ✅ Completati (Cap. 1-4) |
| Esercizi Custom | 15+ | ✅ Completati |
| Mega-Progetti | 1 | ✅ Completato (Parser A: 95/100) |
| **Totale** | **70+** | ✅ |

### Capitoli Covered

- ✅ Capitolo 1: Setup
- ✅ Capitolo 2: Stringhe + 5 custom
- ✅ Capitolo 3: Liste + 5 custom
- ✅ Capitolo 4: For Loops + 10+ custom + Mega-Progetto Parser
- ✅ Capitolo 5: If Statements (consolidamento pratico, no esercizi libro)
- ✅ Capitolo 6: Dictionaries (consolidamento pratico, no esercizi libro)

---

## Metodologia

**Per ogni capitolo:**
1. Completa esercizi dal libro
2. Crea 5 esercizi custom di difficoltà crescente
3. Documenta concetti in Markdown
4. Commit e push su GitHub

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

---

**Ultimo aggiornamento**: 01 gennaio 2026  
**Prossimo passo**: Capitolo 7 (Input dell'utente e while loops) - inizio esercizi custom