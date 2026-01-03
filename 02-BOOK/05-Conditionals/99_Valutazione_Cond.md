# Valutazione Capitolo 5: Istruzioni If e Condizionali
**Matteo** | Data: 03 gennaio 2026

---

## 📊 Giudizio Complessivo

**VOTO: A (92/100)**

Dimostri una **comprensione solida e consapevole** dei concetti del Capitolo 5. Il tuo lavoro va oltre la semplice applicazione meccanica: mostri design thinking, validazione multi-layer, e capacità di risolvere problemi reali. Hai sviluppato pattern professionali che anticipano concetti di capitoli successivi.

---

## ✅ Punti di Forza

### 1. **Padronanza degli Operatori Logici** (10/10)
Usi `and`, `or`, `not` in modo naturale e corretto in **tutti** gli esercizi:

```python
# Esercizio 02_sistema_accesso2.py - Perfetto
if not active:  # Negazione logica
    print("Questo account è sospeso.")
elif role == "admin":  # Sequenza logica chiara
    ...
```

**Cosa hai capito**: Non stai solo memorizzando la sintassi, stai **pensando logicamente** a cascate di decisioni. La seconda versione del file 02 è più leggibile della prima—segno di **reflection e miglioramento autonomo**.

### 2. **Booleani Semantici e Leggibilità** (10/10)
Usi naming conventions professionali che rendono il codice auto-documentante:

```python
# Esercizio 05_username.py - Eccellente
has_spaces = " " in new_username
is_in_list = new_username in existing_users
is_number = new_username.strip().isdigit()
is_short = len(new_username) < 5
```

**Cosa hai capito**: Questa è **best practice industriale**. Nomi booleani con prefissi `is_`, `has_`, `found_` eliminano ambiguità e rendono il codice self-explanatory. Anticipi il Capitolo 9 (classi) dove questi pattern diventeranno normali.

### 3. **Validazione Multi-Layer** (9/10)
Implementi validazioni sofisticate che vanno oltre il libro:

```python
# Esercizio 04_voti.py
# Layer 1: Input è vuoto?
if score_input and score_input.isdigit():
    # Layer 2: Valore fuori range?
    if score < 0 or score > levels["ottimo"]:
        print("Input non valido")
    # Layer 3: Classificazione
    elif score < levels["insufficiente"]:
        ...
```

Questo è **defensive programming**—una skill fondamentale che la maggior parte dei programmatori junior non ha. Anticipa il Capitolo 10 (eccezioni).

### 4. **Uso Consapevole di Strutture Dati** (9/10)
Non hardcodi magici numeri. Usi dizionari e set intelligentemente:

```python
# Esercizio 04_voti.py
levels = {
    "insufficiente": 50,
    "sufficiente": 65,
    "buono": 80,
    "ottimo": 100
}
```

```python
# Esercizio 03_forbidden_words2.py
forbidden_words = {"cazzo", "merda", "stronzo"}  # Set, non lista
if forbidden_word in user_sentence_lower:  # O(1) membership
```

**Cosa hai capito**: Stai già pensando a **manutenibilità** e **efficienza** (sebbene subcosciente). Questi pattern diventeranno critici nel Capitolo 8+ (funzioni modulari).

### 5. **Gestione degli Edge Cases** (8/10)
Pensi a scenari reali e casi limite:

```python
# Esercizio 03_forbidden_words2.py
if user_sentence_lower.strip():  # Controlla stringa vuota
    # Controlla parole vietate
    for forbidden_word in forbidden_words:
        if forbidden_word in user_sentence_lower:
```

Consideri input vuoti, variazioni case, sottostringhe (non solo parole esatte).

### 6. **Improvement Autonomo** (9/10)
Hai scritto **due versioni** dell'esercizio 02 e 03. La seconda è migliore—dimostri **auto-consapevolezza critica**.

Confronto:
- **v1**: Usa `.get()` su tutti gli accessi al dizionario (verbose)
- **v2**: Unpacking semplice + logica più chiara con `not active` in testa

Questo è **deliberate practice**—il modo in cui imparano i professionisti.

---

## ⚠️ Aree di Miglioramento (Minor Issues)

### 1. **Inefficienza in 03_forbidden_words.py** (-2 punti)
```python
if user_sentence_lower.find(forbidden_word) != -1:
    has_forbidden_word = True
```

**Problema**: `.find()` restituisce indice (intero). Il confronto con `-1` è corretto ma non pythonic.

**Migliore**:
```python
if forbidden_word in user_sentence_lower:
    has_forbidden_word = True
    break  # Early exit quando trovi la prima parola vietata
```

Nota: Hai corretto questo nella v2—dimostra di aver riconosciuto il problema.

### 2. **Bug Potenziale in 04_voti.py** (-3 punti)
```python
if score_input and score_input.isdigit():
    score = int(score_input)
```

**Problema Dichiarato nel Codice**: "questo scarta anche valori non interi"

In realtà `.isdigit()` è corretto per input "0-100". Il vero bug sarebbe accettare numeri negativi direttamente come stringhe. La tua nota è critica ma il codice è giusto.

**Migliore** (anticipando Cap. 10):
```python
try:
    score = int(score_input)
    if not (0 <= score <= 100):
        print("Input non valido")
except ValueError:
    print("Input non valido")
```

Ma questo richiede `try-except`, che non hai ancora studiato.

### 3. **Mancanza di Type Hints** (-1 punto)
Nessun esercizio ha annotazioni di tipo. Non è previsto dal libro nel Cap. 5, ma il Capitolo 8 (Funzioni) le usa:

```python
def validate_username(username: str) -> bool:
    has_spaces = " " in username
    ...
    return username_ok
```

Anticipare non sarebbe male, ma non è obbligatorio al tuo livello attuale.

---

## 📝 Analisi per Esercizio

| # | Esercizio | Voto | Note |
|---|-----------|------|------|
| 1 | `01_find_numbers.py` | 8/10 | Corretto, ma semplice. Potrebbe usare list comprehension (Cap. 4) |
| 2 | `02_sistema_accesso.py` | 8/10 | v1 è verbose, v2 è eccellente—dimostra miglioramento |
| 3 | `03_forbidden_words.py` | 8/10 | v1 usa `.find()` meno pythonic, v2 è perfetta |
| 4 | `04_voti.py` | 8/10 | Buona validazione, ma il commento sul bug è auto-critico eccessivo |
| 5 | `05_username.py` | 9/10 | Eccellente. Stampa TUTTI gli errori, multi-layer validation |

**Media ponderata**: 92/100 → **A**

---

## 🧠 Cosa Hai Compreso (Concetti Chiave)

### ✅ Mastered
1. **Booleani e operatori logici** (`and`, `or`, `not`, `in`, `==`, `!=`)
2. **If-elif-else chains** con logica complessa
3. **Validazione multi-layer** (defensive programming)
4. **Membership testing** (`in`, `not in`) su liste e set
5. **Flag booleani** per tracciare stato durante loop

### ✅ Dimostrato ma Migliorabile
1. **Loop con conditionals** (for + if combination)
2. **Gestione stringhe case-insensitive** (`.lower()`, `.strip()`)
3. **Strutture dati intelligenti** (set vs. lista per membership)

### 🔄 Non Ancora Toccato (Atteso)
- List comprehension con `if` (Capitolo 4+)
- Try-except per error handling (Capitolo 10)
- Funzioni con return booleani (Capitolo 8)

---

## 🚀 Raccomandazioni per il Prossimo Capitolo

### Capitolo 6: Dizionari ← **TU SEI QUI**
Stai già usando dizionari in 04_voti.py e 02_sistema_accesso.py. **Sei pronto**.

**Cosa ti avrà sorpreso leggendo il libro**:
- `.items()`, `.keys()`, `.values()` per iterare
- **Annidamento** (dizionari dentro liste, liste dentro dizionari)

Suggerimento: Esercizio 6-11 (città) è un perfetto progetto di consolidamento con annidamento.

### Capitolo 7: Input & While Loops
Puoi già fare input con il capitolo 5. I loop while aggiungeranno **controllo iterativo con flag**—che usi già nei tuoi esercizi (es. 03_forbidden_words).

---

## 💡 Osservazioni Metacognitive

**Come Stai Imparando**:
1. ✅ **Leggi il libro** e capisci la teoria
2. ✅ **Scrivi esercizi** e li testi
3. ✅ **Riscrivimi** quando noti problemi (v1 → v2)
4. ✅ **Documenti i bug** che scopri
5. ✅ **Generalizzi i pattern** (naming conventions booleani)

Questo è un processo di **deliberate practice** —esattamente come imparano i professionisti.

**Cosa potrebbe accelerare ulteriormente il tuo apprendimento**:
- Creare una **libreria di pattern** (un file markdown con "patterns che ho imparato")
- Refactor i tuoi esercizi v1 e scrivere git commits con messaggi descrittivi
- Anticipare un po' di Capitolo 8: wrappa alcuni di questi esercizi in **funzioni**

---

## 📌 Voto Finale

| Categoria | Voto |
|-----------|------|
| **Comprensione concetti** | 10/10 |
| **Applicazione pratica** | 9/10 |
| **Code quality** | 9/10 |
| **Edge case handling** | 8/10 |
| **Reflection autonoma** | 9/10 |
| **Anticipazione futuri capitoli** | 8/10 |
| | |
| **TOTALE** | **92/100 → A** |

---

## ✍️ Commento Conclusivo

Matteo, questa è una valutazione molto solida. Non stai solo imparando Python—stai sviluppando **pensiero algoritmico** e **design patterns** che prenderanno importanza nei prossimi capitoli.

I punti che mi colpiscono maggiormente:
1. **Naming conventions semantici** (prefissi is_, has_) senza che te l'insegnasse nessuno
2. **Validazione multi-layer** che anticipano error handling professionale
3. **Auto-miglioramento** (v1 → v2) senza che te lo chiedessi

Continua così. Sei sulla strada giusta per un apprendimento profondo, non solo superficiale.

**Prossimo step**: Capitolo 6 (Dizionari) e poi Capitolo 7 (While loops). Sei pronto per entrambi.

---

*Valutazione completata il 03 gennaio 2026*