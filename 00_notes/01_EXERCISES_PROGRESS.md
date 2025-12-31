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

## Riassunto Complessivo

### Totale Esercizi per Tipo

| Tipo | Numero | Status |
|------|--------|--------|
| Esercizi Libro | 38 | ✅ Completati |
| Esercizi Custom | 15+ | ✅ Completati |
| **Totale** | **53+** | ✅ |

### Capitoli Covered

- ✅ Capitolo 1: Setup (completato)
- ✅ Capitolo 2: Stringhe + 5 custom (completato)
- ✅ Capitolo 3: Liste + 5 custom (completato)
- 🔄 Capitolo 4: For Loops + 10+ custom (in corso - consolidamento)

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

**Ultimo aggiornamento**: 31 dicembre 2024  
**Prossimo passo**: Completare Set 2 for loops, poi capitolo 5 (if statements)