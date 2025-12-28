# Stringhe in Python — Guida di Riferimento

## Cos'è una stringa?

Una stringa è una **sequenza ordinata di caratteri**. In Python, le stringhe sono **oggetti immutabili**: una volta create, non possono essere modificate. Ogni metodo che "modifica" una stringa in realtà restituisce una **nuova stringa**.

```python
nome = "python"
nome.upper()      # restituisce "PYTHON", ma nome resta "python"
nome = nome.upper()  # ora nome diventa "PYTHON"
```

## Creare stringhe

```python
# Apici singoli o doppi (equivalenti)
messaggio = 'Ciao mondo'
messaggio = "Ciao mondo"

# Stringhe multilinea con tripli apici
testo = """Questa è una stringa
su più righe"""

# Stringa vuota
vuota = ""
```

## f-string (formatted string literals)

Le f-string permettono di inserire espressioni Python direttamente dentro una stringa:

```python
nome = "giulia"
citta = "milano"

# Sintassi base
saluto = f"Ciao {nome}"

# Con espressioni e metodi
saluto = f"Ciao {nome.title()}, benvenuta a {citta.title()}"
```

Tutto ciò che sta dentro le graffe `{}` viene valutato come codice Python.

---

## Metodi usati negli esercizi

### Formattazione maiuscole/minuscole

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.lower()` | Tutto minuscolo | `"CIAO".lower()` → `"ciao"` |
| `.upper()` | Tutto maiuscolo | `"ciao".upper()` → `"CIAO"` |
| `.title()` | Prima lettera di ogni parola maiuscola | `"ciao mondo".title()` → `"Ciao Mondo"` |

### Rimozione spazi e caratteri

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.strip()` | Rimuove spazi da entrambi i lati | `"  ciao  ".strip()` → `"ciao"` |
| `.lstrip()` | Rimuove spazi a sinistra | `"  ciao  ".lstrip()` → `"ciao  "` |
| `.rstrip()` | Rimuove spazi a destra | `"  ciao  ".rstrip()` → `"  ciao"` |

Questi metodi accettano anche un argomento per specificare quali caratteri rimuovere:
```python
"###ciao###".strip("#")  # → "ciao"
```

### Rimozione prefissi e suffissi

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.removeprefix()` | Rimuove un prefisso specifico | `"https://sito.com".removeprefix("https://")` → `"sito.com"` |
| `.removesuffix()` | Rimuove un suffisso specifico | `"file.txt".removesuffix(".txt")` → `"file"` |

Se il prefisso/suffisso non è presente, la stringa viene restituita invariata (nessun errore).

### Ricerca

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.find()` | Restituisce l'indice della prima occorrenza, -1 se non trovato | `"ciao mondo".find("mondo")` → `5` |

### Sostituzione

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.replace(old, new)` | Sostituisce tutte le occorrenze | `"ciao ciao".replace("ciao", "hello")` → `"hello hello"` |

Si può limitare il numero di sostituzioni con un terzo argomento:
```python
"a-b-c-d".replace("-", "_", 2)  # → "a_b_c-d"
```

---

## Funzioni usate negli esercizi

| Funzione | Descrizione | Esempio |
|----------|-------------|---------|
| `len()` | Restituisce la lunghezza della stringa | `len("ciao")` → `4` |
| `print()` | Stampa a schermo | `print("ciao")` |

**Nota**: `len()` è una **funzione**, non un metodo. Si usa `len(stringa)` e non `stringa.len()`.

---

## Method chaining

I metodi possono essere concatenati in catena, perché ogni metodo restituisce una nuova stringa:

```python
nome = "  mARIO rossi  "
nome_pulito = nome.strip().title()  # → "Mario Rossi"
```

È equivalente a:
```python
temp = nome.strip()
nome_pulito = temp.title()
```

---

## Altri metodi utili

### Controllo del contenuto

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.startswith()` | Verifica se inizia con... | `"ciao".startswith("ci")` → `True` |
| `.endswith()` | Verifica se finisce con... | `"file.py".endswith(".py")` → `True` |
| `.isdigit()` | Verifica se contiene solo cifre | `"123".isdigit()` → `True` |
| `.isalpha()` | Verifica se contiene solo lettere | `"ciao".isalpha()` → `True` |
| `.isalnum()` | Verifica se contiene solo lettere e cifre | `"abc123".isalnum()` → `True` |
| `.isspace()` | Verifica se contiene solo spazi | `"   ".isspace()` → `True` |
| `.isupper()` | Verifica se tutto maiuscolo | `"CIAO".isupper()` → `True` |
| `.islower()` | Verifica se tutto minuscolo | `"ciao".islower()` → `True` |

### Divisione e unione

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.split()` | Divide la stringa in una lista | `"a,b,c".split(",")` → `["a", "b", "c"]` |
| `.join()` | Unisce una lista in una stringa | `"-".join(["a", "b", "c"])` → `"a-b-c"` |

```python
# split senza argomento divide per spazi
"ciao mondo".split()  # → ["ciao", "mondo"]

# splitlines divide per righe
"riga1\nriga2".splitlines()  # → ["riga1", "riga2"]
```

### Conteggio e ricerca avanzata

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.count()` | Conta le occorrenze | `"banana".count("a")` → `3` |
| `.index()` | Come find(), ma solleva errore se non trovato | `"ciao".index("a")` → `2` |
| `.rfind()` | Trova l'ultima occorrenza | `"abab".rfind("b")` → `3` |

### Allineamento e padding

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.center(n)` | Centra in n caratteri | `"ciao".center(10)` → `"   ciao   "` |
| `.ljust(n)` | Allinea a sinistra | `"ciao".ljust(10)` → `"ciao      "` |
| `.rjust(n)` | Allinea a destra | `"ciao".rjust(10)` → `"      ciao"` |
| `.zfill(n)` | Riempie con zeri a sinistra | `"42".zfill(5)` → `"00042"` |

### Altre trasformazioni

| Metodo | Descrizione | Esempio |
|--------|-------------|---------|
| `.capitalize()` | Solo prima lettera maiuscola | `"ciao MONDO".capitalize()` → `"Ciao mondo"` |
| `.swapcase()` | Inverte maiuscole/minuscole | `"Ciao".swapcase()` → `"cIAO"` |

---

## Indicizzazione e slicing

Le stringhe sono sequenze, quindi supportano l'accesso per indice:

```python
testo = "Python"

# Indicizzazione (parte da 0)
testo[0]   # → "P"
testo[1]   # → "y"
testo[-1]  # → "n" (ultimo carattere)
testo[-2]  # → "o" (penultimo)

# Slicing [start:end:step]
testo[0:3]   # → "Pyt" (da 0 a 2, il 3 è escluso)
testo[2:]    # → "thon" (da 2 alla fine)
testo[:3]    # → "Pyt" (dall'inizio a 2)
testo[::2]   # → "Pto" (un carattere ogni 2)
testo[::-1]  # → "nohtyP" (stringa invertita)
```

---

## Operatore `in`

Verifica se una sottostringa è contenuta:

```python
"mondo" in "ciao mondo"  # → True
"xyz" in "ciao mondo"    # → False
```

---

## Escape characters

| Sequenza | Significato |
|----------|-------------|
| `\n` | A capo |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Apice singolo |
| `\"` | Apice doppio |

```python
print("Prima riga\nSeconda riga")
print("Colonna1\tColonna2")
```
