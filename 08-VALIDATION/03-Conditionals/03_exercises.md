# 03-Conditionals

**Esercizi consolidati**: 7
**Generato il**: 14/01/2026 18:30
**Sorgente**: `03-Conditionals`

---

## 3_01_find_numbers

```python
# Scrivi un programma Python per trovare i numeri divisibili per 7 e multipli di 5, 
# compresi tra 1500 e 2700 (entrambi inclusi).

numbers = range(1500, 2701)
multiples = []

for number in numbers:
    
    is_div_seven = number % 7 == 0
    is_div_five = number % 5 == 0

    if is_div_seven and is_div_five:
        multiples.append(number)

print(multiples)
```

---

## 3_02_sistema_accesso

```python
# ESERCIZIO 2
#
# Scrivi un programma che:
# saluti ogni utente
# se l’utente non è attivo, mostri un messaggio di account sospeso
# se è attivo:
# se è admin, mostri un messaggio speciale
# se è guest, limiti l’accesso
# altrimenti, accesso standard

users = [
    {"username": "admin", "role": "admin", "active": True},
    {"username": "mario", "role": "user", "active": True},
    {"username": "lucia", "role": "user", "active": False},
    {"username": "guest", "role": "guest", "active": True},
]

for user in users:
    print(f"Ciao, {user.get('username').title()}. Benvenuto!")

    if user.get("active"):
        
        if user.get("role") == "admin":
            print("Il sistema è in modalità amministratore")

        elif user.get("role") == "guest":
            print("Il sistema è in modalità acccesso limitato")

        else:
            print("Il sistema è in modalità acccesso standard")
    
    else:
        print("Questo account è sospeso.")


```

---

## 3_02_sistema_accesso2

```python
# Scrivi un programma che:
# saluti ogni utente
# se l’utente non è attivo, mostri un messaggio di account sospeso
# se è attivo:
# se è admin, mostri un messaggio speciale
# se è guest, limiti l’accesso
# altrimenti, accesso standard

users = [
    {"username": "admin", "role": "admin", "active": True},
    {"username": "mario", "role": "user", "active": True},
    {"username": "lucia", "role": "user", "active": False},
    {"username": "guest", "role": "guest", "active": True},
]

for user in users:
    username = user["username"]
    role = user["role"]
    active = user["active"]

    print(f"Ciao, {username.title()}. Benvenuto!")

    if not active:
        print("Questo account è sospeso.")
    elif role == "admin":
        print("Il sistema è in modalità amministratore")
    elif role == "guest":
        print("Il sistema è in modalità accesso limitato")
    else:
        print("Il sistema è in modalità accesso standard")

```

---

## 3_03_forbidden_words

```python
# ============================================
# ESERCIZIO 3 – Analisi di una frase
#
# Chiedi all’utente di inserire una frase.
#
# Il programma deve:
# - verificare se la frase è vuota
# - controllare se contiene almeno una parola
#   vietata (ignorando maiuscole/minuscole)
# - stampare:
#   - "Frase accettata"
#   - oppure "Frase non valida: motivo ..."
# ============================================

forbidden_words = {"cazzo", "merda", "stronzo"}

# chiedi la frase all'utente
user_sentence = input("Inserisci una frase: ")
user_sentence_lower = user_sentence.lower()

# flag iniziali
has_forbidden_word = False
empty_sentence = False

if user_sentence_lower.strip():
    
    for forbidden_word in forbidden_words:

        if user_sentence_lower.find(forbidden_word) != -1:
            has_forbidden_word = True
    
else:
    empty_sentence = True

if not empty_sentence and not has_forbidden_word:
    print("Frase accettata.")
elif has_forbidden_word:
    print("Frase non valida: parola vietata")
else:
    print("Frase non valida: frase vuota")
```

---

## 3_03_forbidden_words2

```python
# ============================================
# ESERCIZIO 2 – Analisi di una frase
#
# Chiedi all’utente di inserire una frase.
#
# Il programma deve:
# - verificare se la frase è vuota
# - controllare se contiene almeno una parola
#   vietata (ignorando maiuscole/minuscole)
# - stampare:
#   - "Frase accettata"
#   - oppure "Frase non valida: motivo ..."
# ============================================

forbidden_words = {"cazzo", "merda", "stronzo"}

# chiedi la frase all'utente
user_sentence = input("Inserisci una frase: ")
user_sentence_lower = user_sentence.lower()

# flag iniziali
found_forbidden_word = False
empty_sentence = False

# controllo frase vuota
if user_sentence_lower.strip():
    
    # controllo parole vietate come sottostringhe
    for forbidden_word in forbidden_words:
        if forbidden_word in user_sentence_lower:
            found_forbidden_word = True
    
else:
    empty_sentence = True

# output finale
if not empty_sentence and not found_forbidden_word:
    print("Frase accettata.")
elif found_forbidden_word:
    print("Frase non valida: parola vietata")
else:
    print("Frase non valida: frase vuota")
```

---

## 3_04_voti

```python
# ============================================
# ESERCIZIO 4 – Classificazione numerica
#
# Chiedi all’utente di inserire un punteggio.
#
# Il programma deve:
# - verificare che l’input sia valido
# - classificare il punteggio in base alle soglie
#   definite in una struttura dati (non hardcoded)
# ============================================

# Soglie superiori (es. 0 a 49 insufficiente, stessa logica di range(0,50))
levels = {
    "insufficiente": 50,
    "sufficiente": 65,
    "buono": 80,
    "ottimo": 100
}

# Pulisco subito input
score_input = input("Inserisci il punteggio intero tra 0 e 100: ").strip()

# Scarto stringhe vuote, alfanumeriche e negative. Bug da risolvere, questo scarta anche valori non interi.
if score_input and score_input.isdigit():
    score = int(score_input)

    if score < 0 or score > levels["ottimo"]:
        print("Input non valido")
    elif score < levels["insufficiente"]:
        print("Il voto è insufficiente")
    elif score < levels["sufficiente"]:
        print("Il voto è sufficiente")
    elif score < levels["buono"]:
        print("Il voto è buono")
    else:
        print("Il voto è ottimo") 

else:
    print("Input non valido")
```

---

## 3_05_username

```python
# ============================================
# ESERCIZIO 5 – Verifica username intelligente
#
# Chiedi all’utente di inserire uno username.
#
# Lo username è valido solo se:
# - ha almeno 5 caratteri
# - non contiene spazi
# - non è già presente nella lista esistente
# - non è composto solo da numeri
#
# Stampa TUTTI i problemi trovati.
# ============================================

existing_users = ["admin", "mario", "lucia", "guest"]

new_username = input("Inserisci uno username: ")

# Flag di controllo. Per il numero ho inserito strip() in modo da segnalare errore solo numeri in caso di stringhe tipo "12 3"
has_spaces = " " in new_username
is_in_list = new_username in existing_users
is_number = new_username.strip().isdigit()
is_short = len(new_username) < 5

username_ok = not has_spaces and not is_in_list and not is_number and not is_short

if username_ok:
    print("L'username è valido e libero")
else:
    if has_spaces:
       print("L'username contiene spazi")
    if is_in_list:
       print("L'username è già in uso")
    if is_number:
       print("L'username è un numero") 
    if is_short:
       print("L'username è troppo corto") 
```

---

