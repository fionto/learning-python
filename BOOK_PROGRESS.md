# Python Crash Course - Book Progress

Cronologia di lettura e studio del libro **"Python Crash Course"** di Eric Matthes (edizione italiana).

---

## Capitolo 1 – Per iniziare

**Status**: ✅ Completato  
**Completato il**: 28 dicembre 2024  

**Concetti studiati**:
- Configurazione ambiente di programmazione
- Versioni di Python
- Esecuzione frammenti di codice
- Editor VS Code e estensione Python
- Configurazione Python su Linux
- Hello World program
- Esecuzione programmi da terminale

**Note**: Setup iniziale completato. Ambiente pronto per lo sviluppo.

---

## Capitolo 2 – Variabili e tipi di dati semplici

**Status**: ✅ Completato  
**Completato il**: 28 dicembre 2024  

**Concetti studiati**:
- Variabili e assegnamento di nomi
- Variabili come etichette (labeled shoeboxes analogy)
- **Stringhe**: .upper(), .lower(), .title(), .strip(), .lstrip(), .rstrip(), .removeprefix()
- F-string formatting e embedding di variabili
- Whitespace management (tabs, newlines)
- **Numeri**: interi (int), float, operazioni aritmetiche
- Underscore nei numeri (es. 1_000_000)
- Assegnazione multipla
- Costanti
- Commenti in Python
- Lo Zen di Python (`import this`)

**Concetti approfonditi**:
- Immutabilità delle stringhe
- Differenza tra funzioni e metodi (distributed vs. centralized responsibility)
- Method chaining in Python vs. pipelining in bash
- Filosofia del design Python

**Esercizi completati**: 12 esercizi del capitolo (2-1 a 2-12)

**Esercizi personalizzati completati**: 5 esercizi custom su stringhe
- formatta_nome.py
- messaggio_benvenuto.py
- pulisci_url.py
- trova_e_sostituisci.py
- analizza_stringa.py

**Note**: Comprensione solida di stringhe e numeri. Acquisita consapevolezza su immutabilità vs. mutabilità che sarà cruciale nel Cap. 3.

---

## Capitolo 3 – Introduzione alle liste

**Status**: ✅ Completato  
**Completato il**: 29 dicembre 2024 

**Concetti studiati**:
- Cos'è una lista e sintassi base `[]`
- Accesso agli elementi (indexing, 0-based)
- Modifica elementi: `lista[indice] = valore`
- **Aggiunta elementi**: .append(), .insert()
- **Rimozione elementi**: del, .pop(), .remove()
- **Ordinamento**: .sort(), sorted(), .reverse()
- Lunghezza lista: len()
- Aliasing vs. copia (mutabilità delle liste)

**Concetti approfonditi**:
- Mutabilità delle liste vs. immutabilità delle stringhe
- Differenza tra assegnazione (alias) e copia
- Metodi che modificano in-place vs. metodi che restituiscono valori
- Scoperta autonoma di nuovi metodi: .count(), .clear(), .copy(), .index()

**Esercizi completati**: Esercizi del capitolo (3-1 a 3-11)

**Esercizi personalizzati completati**: 5 esercizi custom di media difficoltà
- Gestione Playlist Musicale
- Classifica Videogiochi
- Libreria Personale
- Gestione Code e Stack
- Analisi Temperature

**Note**: Comprensione profonda di mutabilità. Dimostrata capacità di ricercare autonomamente nuovi metodi. Transizione riuscita da stringhe a liste.

---

## Capitolo 4 – Lavorare con le liste

**Status**: 🔄 In Corso  
**Inizio**: 30 dicembre 2024  
**Sezioni completate**:
- ✅ Cicli su un'intera lista (for loop basics)
- ✅ Uno sguardo più approfondito ai cicli
- ✅ Fare più operazioni all'interno di un ciclo for
- 🔄 Errori di indentazione (in studio)
- 🔄 Liste numeriche (in studio)

**Concetti studiati**:
- Sintassi base del `for` loop
- Iterazione su liste, stringhe, range objects
- Differenza concettuale tra `range()` (iterator) e liste (collection)
- Iterator objects e lazy evaluation
- Indentazione e suoi errori comuni
- La funzione `range()`: range(n), range(start, stop), range(start, stop, step)
- Nested loops (loop annidati)

**Concetti approfonditi**:
- PEP8: lunghezza righe (79 caratteri), trailing commas per diffs migliori
- Implicit string concatenation su più righe
- Git diff e come trailing commas lo rendono più leggibile
- Differenza tra range objects (lazy) e liste (materialized)

**Esercizi completati**: 
- 5 esercizi custom di livello elementare
  - Somma dei numeri
  - Stampa invertita di una stringa
  - Filtraggio di una lista
  - Lunghezza delle stringhe in una lista
  - Tabellina con numeri (nested loops)

**Esercizi in corso**:
- 5 esercizi custom di difficoltà incrementale (3/5 completati)

**Note**: 
- Forte comprensione dei concetti fondamentali di iterazione
- Attento alle best practices di stile (PEP8)
- Interesse genuino nei meccanismi sottostanti (iterator vs. list materialization)
- Mantiene focus su for loops, evitando salti ai capitoli successivi per consolidamento solido

---

## Capitolo 5 – Istruzioni if

**Status**: ⏳ Non ancora iniziato  
**Note**: Verrà affrontato dopo completo consolidamento del Capitolo 4

---

## Capitolo 6 – Dizionari

**Status**: ⏳ Non ancora iniziato

---

## Capitolo 7 – Input dell'utente e cicli while

**Status**: ⏳ Non ancora iniziato

---

## Capitolo 8 – Funzioni

**Status**: ⏳ Non ancora iniziato

---

## Capitolo 9 – Classi

**Status**: ⏳ Non ancora iniziato

---

## Capitolo 10 – File ed eccezioni

**Status**: ⏳ Non ancora iniziato

---

## Capitolo 11 – Testare il codice

**Status**: ⏳ Non ancora iniziato

---

## Sommario Generale

**Capitoli completati**: 2/11 (18%)  
**Capitoli in corso**: 1/11  
**Capitoli rimanenti**: 8/11  

**Ultimo aggiornamento**: 31 dicembre 2024, 09:30 UTC

**Metodologia di studio**:
- Lettura del capitolo dal libro
- Video YouTube supplementari
- Esercizi del libro
- Esercizi custom per consolidamento
- Documentazione in Markdown per riferimento futuro
- Tempo dedicato: ~10 minuti al giorno + sessioni weekend

**Paralleli attivi**:
- Harvard CS50P course (edX)
- Bash/shell scripting (come reference per design Python)
- Git e version control (tramite learning repository)

---

## Note Metodologiche

**Approccio consolidamento**:
1. Completare capitolo nel libro
2. Svolgere esercizi del libro
3. Creare 5 esercizi custom di difficoltà crescente
4. Documentare concetti in Markdown
5. Commit e push su GitHub come traccia

**Criteri di "completamento"**:
- Tutti gli esercizi del capitolo svolti
- Comprensione dimostrata dei concetti
- Capacità di spiegare e insegnare i concetti
- Pronto a passare al capitolo successivo

---
