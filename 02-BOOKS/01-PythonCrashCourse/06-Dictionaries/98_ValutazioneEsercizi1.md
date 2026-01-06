# 📊 Esercizi Dizionari - Revisione Accademica del Codice

**Modello di Valutazione:** Claude Sonnet 4.5 (Anthropic)  
**Modulo:** Capitolo 6 - Dizionari  
**Data Sottomissione:** 06/01/2026  
**Esercizi Analizzati:** 10 implementazioni (8 unici + 2 refactoring)

---

## 🎯 Sintesi Esecutiva

**Voto Complessivo: A- (90/100)**

Lo studente dimostra una solida comprensione dei fondamenti dei dizionari con una notevole progressione nella qualità del codice tra le iterazioni. I punti di forza includono pattern di programmazione difensiva e consapevolezza dei meccanismi di espansione dei dizionari. Debolezza principale: sottoutilizzo degli idiomi Python specifici per i dizionari a favore di logica condizionale verbosa.

**Osservazione Chiave:** A differenza dei capitoli precedenti dove lo studente si è sfidato con vincoli complessi (parser senza-if, pattern match/case), questa sottomissione riflette un approccio conservativo e fondamentale—probabilmente intenzionale data la novità della struttura dati.

---

## 📋 Analisi Esercizi e Valutazione Tecnica

| Esercizio | Concetti Core | Qualità Codice | Evoluzione | Voto |
|:---------|:--------------|:-------------|:----------|:------|
| `01_person` | Creazione dict, assegnazione chiavi | Pulito ma elementare | N/A | **B+** |
| `02_favorite_number` | Iterazione `.items()`, f-strings | Solido, idiomatico | N/A | **A** |
| `03_rivers` | `.keys()`, `.values()`, `.items()` | Copertura completa iterazione | N/A | **A** |
| `04_frasi` (v1) | `dict.fromkeys()`, unicità custom | Inizializzazione complicata | → v2 | **B** |
| `04_frasi2` (v2) | Assegnazione diretta chiavi, `.split()` | Migliorato, più pulito | ✓ | **A-** |
| `05_frutta` (v1) | Controllo esistenza chiave condizionale | Check `.keys()` verboso | → v2 | **B+** |
| `05_frutta2` (v2) | `.get()` con default, tuple unpacking | Elegante, Pythonico | ✓✓ | **A+** |
| `06_studenti` | `.items()`, funzioni aggregazione | Corretto, diretto | N/A | **A** |
| `07_trasformazione` | Filtraggio condizionale, `continue` | Pattern guard clause applicato | N/A | **A** |
| `08_sensori` | Strutture annidate, init difensiva | Eccellente ragionamento commentato | N/A | **A+** |

---

## 🔍 Analisi Critica

### Punti di Forza

#### 1. **Maturità nella Programmazione Difensiva** (`08_sensori`)
```python
if tipo not in valori_misurati:
    valori_misurati[tipo] = []
valori_misurati[tipo].append(valore)
```
**Perché è Importante:** Il blocco di commenti dettagliato che spiega perché `.append()` diretto fallisce dimostra comprensione della meccanica lettura-prima-di-scrittura dei dizionari—un concetto che confonde gli sviluppatori per mesi. Il commento esplicito "A questo punto sono sicuro" mostra pensiero algoritmico.

**Nota Accademica:** Questo è **materiale da A+** per il Capitolo 6. La maggior parte degli studenti si sarebbe schiantata contro KeyError multiple volte prima di scoprire questo pattern empiricamente.

#### 2. **Raffinamento Iterativo** (`04_frasi` → `04_frasi2`)

**Problemi Versione 1:**
- `dict.fromkeys(frasi)` pre-inizializzazione non necessaria
- `.split(' ')` manuale invece di `.split()`
- Ciclo esplicito per unicità invece di set

**Miglioramenti Versione 2:**
- Rimossa zavorra `fromkeys()`: "Se la chiave non esiste, la crea"
- Usato `.split()` senza argomento (gestisce tutti gli whitespace)
- **Tuttavia:** Usa ancora un ciclo manuale per l'unicità invece di `len(set(parole))`

**Giustificazione Voto:** Il progresso è visibile, ma lo studente non ha ancora interiorizzato che Python fornisce `set()` per la deduplicazione. Questo suggerisce che i dizionari sono compresi, ma l'integrazione cross-concetto (set Cap3 + dict Cap6) è in sospeso.

#### 3. **Scoperta del Metodo `.get()`** (`05_frutta2`)
```python
spesa[frutto] = spesa.get(frutto, 0) + quantità
```
**Momento di Svolta:** Questa singola riga sostituisce 5 righe di logica condizionale della v1. Lo studente l'ha scoperto autonomamente (probabilmente tramite ricerca documentazione, secondo il suo pattern di apprendimento). Questa è la **riga più Pythonica** dell'intera sottomissione.

**Perché A+:** Questo pattern (accumulazione tramite `.get()` con default) è la soluzione canonica insegnata nei corsi professionali Python. Scoprirlo indipendentemente a questo stadio è eccezionale.

---

### Debolezze e Opportunità Mancate

#### 1. **Sottoutilizzo di Set** (`04_frasi`)
**Implementazione Attuale:**
```python
def uniche(lista_parole: list[str]) -> int:
    parole_uniche = []
    for parola in lista_parole:
        if parola not in parole_uniche:
            parole_uniche.append(parola)
    return len(parole_uniche)
```

**Alternativa Pythonica in Una Riga:**
```python
def uniche(lista_parole: list[str]) -> int:
    return len(set(lista_parole))
```

**Critica:** Hai passato il Capitolo 3 a imparare i set per il test di appartenenza O(1). Qui stai implementando deduplicazione manuale con lookup O(n²) (`parola not in parole_uniche` scansiona l'intera lista ogni volta). Questo è precisamente ciò che i set risolvono.

**Impatto sul Voto:** Abbassa `04_frasi2` da potenziale A+ a A-. La logica è corretta, ma stai reinventando ruote della libreria standard.

#### 2. **`.keys()` Ridondante nei Test di Appartenenza** (`05_frutta` v1)
```python
if acquisto[0] not in totale.keys():  # ❌ Verboso
```
**Dovrebbe Essere:**
```python
if acquisto[0] not in totale:  # ✅ Idiomatico
```

**Spiegazione:** L'operatore `in` sui dizionari controlla le chiavi per default. Scrivere `.keys()` esplicitamente è ridondante e segnala scarsa familiarità con gli interni dei dizionari. Hai corretto questo nella v2 omettendolo, ma l'errore iniziale suggerisce modello mentale incompleto.

#### 3. **Evitamento del Chaining dei Metodi Stringa** (`04_frasi`)
**Attuale:**
```python
frase_pulita = frase.replace(',', '').replace('.', '').replace('!', '').lower()
```

**Più Scalabile (Usando `str.translate()`):**
```python
import string
frase_pulita = frase.translate(str.maketrans('', '', string.punctuation)).lower()
```

**Contro-Argomentazione:** Per il Capitolo 6, `.replace()` concatenato è accettabile. Tuttavia, questo pattern non scala (cosa fare con `?`, `;`, `:`?). Dovresti essere consapevole che Python fornisce `string.punctuation` per la gestione esaustiva.

---

## 📈 Punti di Inflessione (Marcatori di Evoluzione)

### 🔄 Iterazione 1 → 2: L'Epifania di `.get()`
**Contesto:** `05_frutta` → `05_frutta2`

**Prima (5 righe):**
```python
if acquisto[0] not in totale.keys():
    totale[acquisto[0]] = acquisto[1]
else:
    nuova_quantita = totale[acquisto[0]] + acquisto[1]
    totale[acquisto[0]] = nuova_quantita
```

**Dopo (1 riga):**
```python
spesa[frutto] = spesa.get(frutto, 0) + quantità
```

**Analisi:** Questo è il tuo **momento "aha" del Capitolo 6**—equivalente alla tua svolta sulla mutabilità nel Capitolo 3. Hai interiorizzato che i dizionari possono fornire default durante le letture, eliminando i condizionali. Questo pattern ti servirà per anni nei problemi di aggregazione.

### 🧠 Inizializzazione Difensiva: Il Paradigma `08_sensori`

**Commento Proprio dello Studente:**
> "NOTA (errore iniziale): [...] La chiave viene creata automaticamente solo quando si assegna esplicitamente: `valori_misurati[tipo] = []`. Da lì in poi, append() funziona correttamente."

**Perché è Importante:** Hai documentato il tuo processo di debugging e corretto il modello mentale. Questa auto-correzione—catturata nei commenti del codice—è **pedagogia degna di pubblicazione**. La maggior parte degli studenti non articola mai perché il primo tentativo è fallito; tu l'hai reso esplicito.

**Abilità Meta-Apprendimento:** Stai costruendo una libreria di pattern nella tua testa: "Prima di usare un metodo lista su un valore dict, assicurati che la chiave esista e il valore sia effettivamente una lista." Questa è programmazione difensiva al suo nucleo.

---

## 🚨 Critica Onesta (Senza Edulcorazioni)

### 1. **La Decomposizione delle Funzioni è Inconsistente**
- `04_frasi`: Estrae la funzione `uniche()` ✅
- `05_frutta`: Nessuna estrazione nonostante logica di accumulazione riutilizzabile ❌
- `06_studenti`: Calcolo inline delle medie ❌

**Standard:** Se la logica supera le 3 righe o è concettualmente riutilizzabile, estraila. La tua funzione `uniche()` è buona pratica, ma non applichi questa disciplina uniformemente.

### 2. **I Type Hints Sono Decorativi, Non Validati**
```python
def uniche(lista_parole: list[str]) -> int:
```

Stai usando i type hints correttamente nelle signature, ma:
- Nessuna validazione runtime (dovresti aggiungere `assert isinstance(...)`?)
- Nessun uso di `mypy` per controllo statico

**Verifica di Realtà:** I type hints senza strumenti sono documentazione, non enforcement. Considera di aggiungere `mypy` al tuo workflow per vera sicurezza sui tipi.

### 3. **Non Stai Spingendo i Limiti dei Dizionari**
**Esperimenti Mancanti:**
- Dictionary comprehension: `{k: v for k, v in ...}`
- `collections.defaultdict` per inizializzazione automatica
- `dict.setdefault()` come alternativa a `.get()`
- Iterazione su dizionari annidati

**Osservazione:** Dopo l'esplorazione aggressiva dei Capitoli 3-4 (4 modi per invertire stringhe, loop annidati), il Capitolo 6 sembra timido. Hai risolto i problemi correttamente ma non hai stress-testato i limiti della struttura dati.

---

## 🎯 Dettaglio Rubrica di Valutazione

| Criterio | Peso | Punteggio | Giustificazione |
|:----------|:-------|:------|:--------------|
| **Correttezza** | 30% | 30/30 | Tutti gli output corrispondono al comportamento atteso |
| **Idiomi Pythonici** | 25% | 18/25 | `.get()` padroneggiato, ma set/dict-comp inutilizzati |
| **Evoluzione Codice** | 20% | 18/20 | Miglioramenti v1→v2 forti; manca polish v3 |
| **Documentazione** | 15% | 15/15 | Commenti `08_sensori` sono di qualità reference |
| **Design Pattern** | 10% | 9/10 | Guard clauses usate; estrazione funzioni irregolare |
| **TOTALE** | 100% | **90/100** | **Voto: A-** |

---

## 🔮 Prossimi Passi Prescritti

### Immediato (Padronanza Capitolo 6):
1. **Riscrivi `04_frasi` Usando Set**
   ```python
   def uniche(lista_parole):
       return len(set(lista_parole))
   ```
   Capisci perché questo è O(n) vs. il tuo ciclo O(n²).

2. **Esplora il Modulo `collections`**
   - Riscrivi `08_sensori` usando `defaultdict(list)` per eliminare completamente il check `if tipo not in ...`.
   - Ricerca `Counter` per problemi di frequenza.

3. **Esercizio Dictionary Comprehension**
   Crea una dict-comp che filtra e trasforma in una riga:
   ```python
   # Trasforma 07_trasformazione usando comprehension
   dati_elaborati = {k: v*2 if v%2==0 else v for k,v in dati.items() if v > 0}
   ```

### Strategico (Ponte verso Capitolo 7):
1. **Pratica Dizionari Annidati**
   - Costruisci una struttura `dict[str, dict[str, list]]` (es. studenti → materie → voti)
   - Naviga e modifica strutture a 3 livelli di profondità

2. **Combina Dict + Input Utente**
   - Anticipa Capitolo 7: Costruisci menu interattivo che memorizza scelte utente in un dict
   - Usa `while True` + aggiornamenti dict

3. **Consapevolezza Performance**
   - Profila la tua funzione `uniche()` con `timeit` su liste da 10.000 elementi
   - Confronta ciclo manuale vs. `set()` vs. `dict.fromkeys()`

---

## 📝 Osservazioni Finali

**Cosa Hai Fatto Bene:**
- Pattern di inizializzazione difensiva (`08_sensori`) sono di livello professionale
- La scoperta di `.get()` mostra apprendimento autonomo
- Il processo di debugging commentato è pedagogicamente prezioso

**Cosa Necessita Lavoro:**
- Smetti di reinventare `set()` per l'unicità
- Applica l'estrazione di funzioni uniformemente
- Spingi le strutture dati più forte (dict-comp, `defaultdict`, iterazioni annidate)

**Osservazione Contestuale:**  
Le tue sottomissioni del Capitolo 4 erano architettonicamente ambiziose (Bio-Parser, Batch Processor). Il Capitolo 6 sembra che tu stia consolidando i fondamenti piuttosto che esplorare i limiti. Questo è **strategicamente sensato** ma significa che non hai ancora integrato i dizionari in sistemi complessi.

**Raccomandazione:** Prima di passare al Capitolo 7, costruisci un **progetto di integrazione** che combini:
- Dizionari (annidati, 2+ livelli)
- List comprehension
- Funzioni custom con type hints
- Modellazione dati mondo reale (es. catalogo biblioteca, rete sensori, registro voti)

Questo forzerà la sintesi cross-concetto e ti preparerà per la complessità while-loop + input del Capitolo 7.

---

**Voto: A- (90/100)**  
**Status:** Pronto per Capitolo 7 con esercizi di rimedio prescritti completati.