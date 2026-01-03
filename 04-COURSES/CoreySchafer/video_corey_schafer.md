# Riassunto Python Tutorial - Corey Schafer (Video 1-5)

## 1. Installazione e Configurazione
* **Verifica versione:** Usare `python --version` nel terminale.
* **Windows:** Scaricare l'installer da python.org. **Importante:** Spuntare "Add Python to PATH".
* **Mac:** Scaricare Python 3. Per usare il comando `python` invece di `python3`, creare un alias nel file di configurazione della shell (`.zshrc` o `.bash_profile`).
* **Ambiente:** Si può usare l'IDLE integrato, ma sono consigliati editor come VS Code, Sublime Text o PyCharm.

---

## 2. Stringhe (Textual Data)
* **Definizione:** Testo tra apici `' '` o `" "`. Per più righe: `''' '''`.
* **Metodi Principali:**
    * `len(str)`: Lunghezza della stringa.
    * `str[indice]`: Accesso ai caratteri (0 è il primo).
    * `str[inizio:fine]`: Slicing (il limite superiore è escluso).
    * `.lower()` / `.upper()`: Cambia il case.
    * `.count('x')`: Conta occorrenze.
    * `.find('x')`: Restituisce l'indice della prima occorrenza (o -1).
    * `.replace('vecchio', 'nuovo')`: Sostituisce il testo.
* **Formattazione (f-strings):** * `f"Ciao, {variabile}"` (Metodo moderno e preferito).

---

## 3. Numeri (Integers & Floats)
* **Tipi:** `int` (interi) e `float` (decimali).
* **Operatori:**
    * `+`, `-`, `*`, `/` (divisione classica).
    * `//` (divisione intera: scarta il resto).
    * `**` (esponente).
    * `%` (modulo: restituisce il resto della divisione).
* **Funzioni:**
    * `abs(num)`: Valore assoluto.
    * `round(num, cifre)`: Arrotondamento.
* **Comparazioni:** `==`, `!=`, `>`, `<`, `>=`, `<=` (restituiscono True o False).
* **Casting:** `int('100')` converte una stringa in numero.

---

## 4. Liste, Tuple e Set
* **Liste `[]`:** Ordinate e **mutabili**.
    * `.append(x)`: Aggiunge in fondo.
    * `.insert(i, x)`: Aggiunge in posizione specifica.
    * `.extend(lista)`: Unisce due liste.
    * `.remove(x)` / `.pop()`: Rimuove elementi.
    * `sorted(lista)`: Restituisce una copia ordinata.
* **Tuple `()`:** Ordinate ma **immutabili** (non possono essere cambiate dopo la creazione).
* **Set `{}`:** Non ordinati e **senza duplicati**.
    * Molto veloci per test di appartenenza (`x in set`).
    * Metodi: `.intersection()`, `.difference()`, `.union()`.
* **Utility:** `' - '.join(lista)` trasforma una lista in stringa.

---

## 5. Dizionari (Key-Value Pairs)
* **Struttura:** Coppie chiave-valore `{ 'chiave': 'valore' }`.
* **Operazioni:**
    * `dict.get('chiave', 'Default')`: Accesso sicuro (non crasha se la chiave manca).
    * `dict['nuova_chiave'] = 'valore'`: Aggiunta o modifica.
    * `dict.update({ ... })`: Aggiorna più valori contemporaneamente.
    * `del dict['chiave']`: Eliminazione.
* **Iterazione:**
    * `dict.keys()`: Solo le chiavi.
    * `dict.values()`: Solo i valori.
    * `dict.items()`: Ciclo su entrambi (`for k, v in dict.items():`).

---

## 6. Condizionali e Booleani (If, Else, Elif)

### 6.1. Struttura dei Condizionali
* **if:** Esegue un blocco di codice solo se la condizione è vera.
* **elif (else if):** Permette di controllare più condizioni in sequenza se quelle precedenti erano false.
* **else:** Esegue un blocco di codice se nessuna delle condizioni precedenti è stata soddisfatta.
* **Nota sulla Sintassi:** Python usa i due punti `:` alla fine della condizione e l'indentazione per definire i blocchi di codice.

### 6.2. Operatori di Comparazione
* `==`: Uguale a
* `!=`: Diverso da
* `>` / `<`: Maggiore di / Minore di
* `>=` / `<=`: Maggiore o uguale / Minore o uguale

### 6.3. Operatori Logici
* **and:** Vero solo se tutte le condizioni sono vere.
* **or:** Vero se almeno una delle condizioni è vera.
* **not:** Inverte il valore Booleano (da True a False e viceversa).

### 6.4. Identità degli Oggetti: la keyword 'is'
Esiste una differenza fondamentale tra `==` e `is`:
* **`==` (Eguaglianza):** Controlla se i **valori** degli oggetti sono uguali.
* **`is` (Identità):** Controlla se due variabili puntano allo **stesso oggetto nella memoria**.
    * Due liste `a = [1,2,3]` e `b = [1,2,3]` risulteranno `a == b` (True), ma `a is b` (False) perché sono due oggetti distinti in memoria.
    * Internamente, `is` confronta l'ID dell'oggetto ottenuto con la funzione `id()`.

### 6.5. Cosa valuta Python come False (Falsy Values)
In Python, non solo il valore Booleano `False` è considerato falso. Le seguenti condizioni valutano sempre a **False** in un contesto condizionale:

1.  **False:** Il valore booleano stesso.
2.  **None:** L'oggetto che rappresenta l'assenza di valore.
3.  **Zero di qualsiasi tipo numerico:** `0`, `0.0`, ecc.
4.  **Sequenze vuote:** Stringa vuota `''`, Lista vuota `[]`, Tupla vuota `()`.
5.  **Dizionari (Mapping) vuoti:** `{}`.

*Ogni altro valore non elencato qui sopra viene valutato come **True** da Python.*

---

## 7. Cicli e Iterazioni (For e While Loop)

I cicli permettono di scorrere collezioni di dati (liste, tuple, dizionari) o di eseguire un blocco di codice ripetutamente finché una condizione è soddisfatta.

### 7.1 Il ciclo "for"
Viene utilizzato per iterare su una sequenza di elementi (come una lista o una stringa).
* **Esempio:** `for num in nums:` esegue il codice per ogni elemento all'interno di `nums`.

### 7.2 Statements: break e continue
Questi comandi permettono di modificare il flusso normale di un ciclo.

* **break:** Viene usato per interrompere completamente il ciclo. Quando Python incontra `break`, "esce" immediatamente dal loop e passa alla prima riga di codice successiva al ciclo stesso.
* **continue:** Non interrompe il ciclo, ma "salta" solo l'iterazione corrente. Quando Python incontra `continue`, ignora tutto il codice rimanente all'interno del blocco per quell'elemento e passa immediatamente all'iterazione successiva.

### 7.3 La funzione range()
Viene utilizzata per generare una sequenza di numeri, molto utile quando si vuole eseguire un'azione per un numero specifico di volte.

**Gli argomenti di `range(start, stop, step)`:**
1.  **start (opzionale):** Il valore di inizio (default è 0).
2.  **stop (obbligatorio):** Il valore a cui fermarsi. **Nota bene:** Questo valore è *esclusivo*, il ciclo si ferma al numero precedente allo stop.
3.  **step (opzionale):** L'incremento tra un numero e l'altro (default è 1).
* **Esempio:** `range(1, 11)` produrrà i numeri da 1 a 10.

### 7.4 Il ciclo "while"
A differenza del ciclo `for`, che scorre una sequenza definita, il ciclo `while` continua a girare finché una determinata condizione rimane `True`.
* **Esempio:** `while x < 10:` esegue il codice fintanto che la condizione rimane `True`


### 7.5 While loop con break
È possibile utilizzare lo statement `break` anche all'interno di un ciclo `while` per forzarne l'uscita, indipendentemente dalla condizione iniziale.
* Una pratica comune è creare un ciclo potenzialmente infinito con `while True:` e inserire un controllo interno con un `if` che chiama il `break` quando viene raggiunto l'obiettivo desiderato.