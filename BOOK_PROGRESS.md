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
- Lo Zen di Python (PEP 20)

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
**Completato il**: 29 dicembre 2024 (mattina)  

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

**Status**: ✅ Completato  
**Completato il**: 31 dicembre 2024  

**Concetti studiati**:
- Sintassi base del `for` loop
- Iterazione su liste, stringhe, range objects
- Differenza concettuale tra `range()` (iterator) e liste (collection)
- Iterator objects e lazy evaluation
- Indentazione e suoi errori comuni
- La funzione `range()`: range(n), range(start, stop), range(start, stop, step)
- Nested loops (loop annidati)
- Slicing di liste e stringhe (positivo, negativo, con step)
- Tuple e loro caratteristiche

**Concetti approfonditi**:
- PEP8: lunghezza righe (79 caratteri), trailing commas per diffs migliori
- Implicit string concatenation su più righe
- Git diff e come trailing commas lo rendono più leggibile
- Differenza tra range objects (lazy) e liste (materialized)
- Reversed objects come iterator
- Aliasing vs. copia di liste (approfondimento mutabilità)

**Esercizi completati**: 
- 10+ esercizi custom (elementari + incrementali)
  - Somma dei numeri e accumulazione
  - Stampa invertita di una stringa (4 metodi diversi)
  - Filtraggio di una lista
  - Lunghezza delle stringhe in una lista con .capitalize()
  - Tabelline con loop nidificati
  - Slicing avanzato (negativo, con step)
  - Copia invertita con reversed()
  - Concatenazione stringhe con metodi
  - Estrazione caratteri alternati
  - Lista di coppie da due liste

**Mega-progetto**:
- **Bio-Informatic Data Parser v1.0** (Project Cosmic Parser)
  - Valutazione: A (95/100)
  - Concetti applicati: Set, Tuple, Dictionary, String methods, Slicing, Function design
  - Gestione dati strutturati, parsing, validazione logica
  - Documentazione professionale con analisi evolutiva
  - [Valutazione completa chat: Code review per esercizi intermedi]

**Note**: 
- Consolidamento completo del capitolo
- Approccio metodico e ordinato
- Applicazione creativa di concetti in un progetto reale
- Pronto per passare ai capitoli successivi

---

## Capitolo 5 – Istruzioni if

**Status**: ✅ Completato  
**Completato il**: 01 gennaio 2026  

**Concetti studiati** (dal libro):
- Test condizionali e booleani
- Operatori di confronto: ==, !=, >, <, >=, <=
- Operatori logici: and, or, not
- Verificare appartenenza a liste (in, not in)
- Espressioni booleane
- Istruzioni if semplici
- Istruzioni if-else
- Catena if-elif-else

**Concetti approfonditi** (supplementari):
- **Statement `is`** (Corey Schafer) — confronto di identità vs. uguaglianza
- **Type checking** — verificare il tipo di una variabile
- **Keywords e Shadowing** (ricerca autonoma) — implicazioni quando si riassegnano variabili
  - Concetto critico emerso durante sviluppo Project Parser
  - Comprensione di scope e namespace in Python

**Esercizi completati**: 
- Nessun esercizio dal libro (giudicati troppo elementari)
- Consolidamento attraverso mega-progetto Parser e riflessione autonoma

**Note**: 
- Approccio selettivo: saltare esercizi ridondanti, focus su applicazione pratica
- Approfondimento autonomo di shadowing causato da errori nel Parser
- Integrazione di fonti supplementari per completezza concettuale

---

## Capitolo 6 – Dizionari

**Status**: ✅ Completato  
**Completato il**: 01 gennaio 2026  

**Concetti studiati** (dal libro):
- Struttura dizionario: chiave-valore
- Accesso ai valori tramite chiave
- Aggiungere e modificare coppie chiave-valore
- Rimuovere coppie (del, .pop())
- Metodo .get() per accesso sicuro
- Iterazione su dizionari:
  - Ciclo su coppie chiave-valore (.items())
  - Ciclo su sole chiavi
  - Ciclo su soli valori
- **Annidamento** (dal libro):
  - Lista di dizionari
  - Dizionari dentro dizionari
  - Liste dentro dizionari

**Concetti approfonditi** (supplementari):
- **List of dictionaries** (dal libro, capitolo dedicato) — strutture dati complesse
- Unpacking di dizionari (anticipato da future refactoring)

**Esercizi completati**: 
- Nessun esercizio dal libro (stesso criterio del Cap. 5)
- **Mega-progetto Parser v1.0** consolida dizionari e annidamento:
  - Strutture dati multi-livello
  - Accesso e manipolazione di dati complessi
  - Gestione errori tramite validazione logica senza `if`

**Note**: 
- Approccio pragmatico: esercizi libro saltati, apprendimento attraverso progetti
- Fondamento solido per strutture dati complesse
- Parser dimostra mastery di dictionary operations in contesto reale

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

**Capitoli completati**: 4/11 (36%)  
**Capitoli in corso**: 0/11  
**Capitoli rimanenti**: 7/11  

**Ultimo aggiornamento**: 01 gennaio 2026, 11:16 UTC

**Metodologia di studio**:
- Lettura del capitolo dal libro (quando appropriato)
- Video YouTube supplementari (Corey Schafer)
- CS50P lectures in parallelo (Harvard)
- Esercizi del libro (quando significativi) + esercizi custom
- Mega-progetti per consolidamento pratico
- Documentazione in Markdown per riferimento futuro
- Tempo dedicato: ~10 minuti al giorno + sessioni weekend

**Paralleli attivi**:
- Harvard CS50P course (edX) - Lecture 0 e 1 completate
- Corey Schafer YouTube tutorials (video supplementari)
- Bash/shell scripting (come reference per design Python)
- Git e version control (tramite learning repository)

**Fonti integrate**:
- **Libro**: Python Crash Course (Eric Matthes, edizione italiana) — base strutturale
- **CS50P**: Funzioni, concetti avanzati
- **Corey Schafer**: Dettagli tecnici (statement is, ecc.)
- **Ricerca autonoma**: Keywords, shadowing, type checking

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