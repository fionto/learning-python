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