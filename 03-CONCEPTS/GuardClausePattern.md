# Guard Clause Pattern: Guida Completa
## Matteo | Design Pattern Fondamentale
### Data: 6 gennaio 2026

---

## Introduzione

Il **guard clause pattern** (o "early return") è uno dei pattern più importanti nella programmazione moderna. È semplice da capire, ma ha un impatto enorme sulla leggibilità e manutenibilità del codice. In Python, è anche conosciuto come **"fail-fast" pattern** o **"bail-out early"**.

---

## Il Concetto Fondamentale

Una **guard clause** è una condizione che verifica se una situazione è "invalida" o "anomala", e se lo è, **esce dalla funzione immediatamente**, saltando il resto del codice.

### Esempio Base

```python
def processa_dati(dati):
    # Guard clause: se dati è None, esci subito
    if dati is None:
        return None
    
    # Se arriviamo qui, sappiamo che dati non è None
    # Possiamo procedere con la logica principale
    risultato = dati * 2
    return risultato
```

Nota l'indentazione: il codice principale **non è indentato dentro un if**. È al livello "normale". Questo è il punto cruciale.

---

## Guard Clause vs. Alternativa Negata

Molti principianti scrivono così:

```python
# ❌ BRUTTO - Non-guard clause
def processa_dati(dati):
    if dati is not None:
        risultato = dati * 2
        return risultato
    else:
        return None
```

Confronta con:

```python
# ✓ BELLO - Guard clause
def processa_dati(dati):
    if dati is None:
        return None
    
    risultato = dati * 2
    return risultato
```

**Qual è la differenza?**

Nel primo caso, il **codice logico principale** (`risultato = dati * 2`) è dentro l'if. È indentato una volta. Se aggiungi altra logica, devi aggiungerla dentro l'if.

Nel secondo caso, il **codice logico principale** è al livello di base. È chiaro e lineare.

Questa differenza diventa **massiccia** in funzioni complesse:

```python
# ❌ BRUTTO - Piramide della morte (Pyramid of Doom)
def elabora_ordine(ordine):
    if ordine is not None:
        if ordine.articoli:
            if ordine.cliente:
                if ordine.cliente.indirizzo:
                    # Infine, il vero codice
                    calcola_spese_spedizione(ordine)
                else:
                    return "Errore: indirizzo mancante"
            else:
                return "Errore: cliente mancante"
        else:
            return "Errore: ordine vuoto"
    else:
        return "Errore: ordine None"

# ✓ BELLO - Guard clauses
def elabora_ordine(ordine):
    if ordine is None:
        return "Errore: ordine None"
    
    if not ordine.articoli:
        return "Errore: ordine vuoto"
    
    if not ordine.cliente:
        return "Errore: cliente mancante"
    
    if not ordine.cliente.indirizzo:
        return "Errore: indirizzo mancante"
    
    # Infine, il vero codice, al livello di base
    calcola_spese_spedizione(ordine)
```

Leggi il secondo: lineare, chiaro, facile da capire. Ogni guard clause elimina una "via anomala", e alla fine rimane il **happy path** (il percorso felice, il caso normale).

---

## Struttura Base del Guard Clause

```python
def funzione(parametro):
    # Guard clause 1
    if condizione_anomala_1:
        return risultato_errore_1
    
    # Guard clause 2
    if condizione_anomala_2:
        return risultato_errore_2
    
    # Guard clause 3
    if condizione_anomala_3:
        return risultato_errore_3
    
    # Se arriviamo qui, tutte le guard clauses sono passate
    # Logica principale (happy path)
    risultato = calcolo(parametro)
    return risultato
```

**Pattern**: verifichi i **casi cattivi** prima, uno per uno. Se uno è vero, esci. Se tutti falliscono (cioè, tutte le guard clauses sono False), procedi con la logica principale.

---

## Caso Studio 1: Validazione di Input Utente

Immagina una funzione che crea un nuovo utente:

```python
# ❌ BRUTTO - Senza guard clauses
def crea_utente(email, password, età):
    if email and email.count("@") > 0:
        if password and len(password) >= 8:
            if età and età >= 18:
                # Crea l'utente
                db.insert({"email": email, "password": password, "età": età})
                return "Utente creato"
            else:
                return "Errore: età minima 18 anni"
        else:
            return "Errore: password minimo 8 caratteri"
    else:
        return "Errore: email non valida"

# ✓ BELLO - Con guard clauses
def crea_utente(email, password, età):
    # Guard clause 1: email non presente
    if not email:
        return "Errore: email obbligatoria"
    
    # Guard clause 2: email non valida
    if email.count("@") == 0:
        return "Errore: email deve contenere @"
    
    # Guard clause 3: password non presente
    if not password:
        return "Errore: password obbligatoria"
    
    # Guard clause 4: password troppo corta
    if len(password) < 8:
        return "Errore: password minimo 8 caratteri"
    
    # Guard clause 5: età non presente
    if età is None:
        return "Errore: età obbligatoria"
    
    # Guard clause 6: età sotto il minimo
    if età < 18:
        return "Errore: età minima 18 anni"
    
    # Happy path: se arriviamo qui, tutto è valido
    db.insert({"email": email, "password": password, "età": età})
    return "Utente creato"
```

**Vantaggi:**

1. **Lineare**: leggi il codice da cima a fondo senza "zigzag"
2. **Chiarezza**: ogni guard clause è una ragione per cui il processo fallisce
3. **Manutenibilità**: aggiungere una nuova validazione è semplice — aggiungi un'altra guard clause
4. **Testing**: è facile testare ogni guard clause separatamente

---

## Caso Studio 2: Ricerca in una Struttura Dati Complessa

Immagina di cercate un prodotto in un ordine:

```python
# ❌ BRUTTO - Senza guard clauses
def trova_prezzo_prodotto(ordine, nome_prodotto):
    if ordine:
        if "articoli" in ordine:
            for articolo in ordine["articoli"]:
                if "nome" in articolo:
                    if articolo["nome"] == nome_prodotto:
                        if "prezzo" in articolo:
                            return articolo["prezzo"]
                        else:
                            return None
    return None

# ✓ BELLO - Con guard clauses
def trova_prezzo_prodotto(ordine, nome_prodotto):
    # Guard clause 1: ordine non esiste
    if not ordine:
        return None
    
    # Guard clause 2: articoli non presenti
    if "articoli" not in ordine:
        return None
    
    # Guard clause 3: articoli è vuota
    if not ordine["articoli"]:
        return None
    
    # Happy path: cerca il prodotto
    for articolo in ordine["articoli"]:
        if articolo.get("nome") == nome_prodotto:
            return articolo.get("prezzo")
    
    # Se il prodotto non è stato trovato
    return None
```

Nota l'ultimo return: non è un guard clause per dati invalidi, è il risultato naturale della ricerca.

---

## Caso Studio 3: Il Tuo Batch Signal Processor

Ricordi il tuo codice?

```python
for segnale_str in segnali:
    # Guard clause 1: stringa vuota
    if not segnale_str:
        segnali_corrotti += 1
        continue
    
    componenti_segnale = segnale_str.split("|")
    
    # Guard clause 2: numero di componenti sbagliato
    if len(componenti_segnale) != 4:
        segnali_corrotti += 1
        continue
    
    # Guard clause 3: primo elemento non è un numero
    is_invalid_format = not componenti_segnale[0].isdigit()
    if is_invalid_format:
        segnali_corrotti += 1
        continue
    
    # Happy path: processo il segnale
    id_int = int(componenti_segnale[0])
    is_not_valid_id = id_int % 2 != 0
    if is_not_valid_id:
        segnali_invalidi += 1
    else:
        segnali_validi += 1
```

**Esattamente** quello che hai fatto! Ogni `continue` è un "bail-out" — uscire dal ciclo per questo elemento. Le guard clauses verificano i dati invalidi, e se passano tutte, procedi con la logica.

---

## Best Practices

### 1. **Ordine delle Guard Clauses**

Ordina le guard clauses dal **più semplice al più complesso**:

```python
# ✓ BENE
def processa_pagina(pagina):
    # Semplice: esiste?
    if not pagina:
        return None
    
    # Più complesso: tipo corretto?
    if not isinstance(pagina, dict):
        return None
    
    # Ancora più complesso: campo presente?
    if "contenuto" not in pagina:
        return None
    
    # Complessissimo: contenuto valido?
    if not pagina["contenuto"].strip():
        return None
    
    # Happy path
    return pagina["contenuto"]
```

Questo ha senso perché:
1. Se fallisce una guard clause semplice, non sprechi CPU su celle complesse
2. È più leggibile — la logica procede naturalmente da semplice a complesso

### 2. **Guard Clauses vs. Assert**

Non confondere guard clauses con **assert**:

```python
# ❌ SBAGLIATO - Assert per validazione input
def calcola(x):
    assert x > 0, "x deve essere positivo"
    return x ** 2

# ✓ GIUSTO - Guard clause per validazione input
def calcola(x):
    if x <= 0:
        raise ValueError("x deve essere positivo")
    return x ** 2

# ✓ ANCHE GIUSTO - Return per funzioni che non lanciano eccezioni
def valida_numero(x):
    if x <= 0:
        return False
    return True
```

**Differenza:**
- **Assert**: per errori di programmazione (bug nel tuo codice)
- **Guard clauses**: per dati invalidi (errore dell'utente)

### 3. **Messaggi di Errore Chiari**

```python
# ❌ VAGO
if not email:
    return "Errore"

# ✓ CHIARO
if not email:
    return "Errore: email obbligatoria"

# ✓ ANCORA MEGLIO (con contesto)
def registra_utente(email, password):
    if not email:
        return {"success": False, "errore": "email_obbligatoria"}
    
    if not password:
        return {"success": False, "errore": "password_obbligatoria"}
    
    # Crea l'utente
    return {"success": True, "messaggio": "Registrazione completata"}
```

### 4. **Guard Clauses con Operatori Logici**

A volte puoi combinare condizioni:

```python
# ✓ ACCETTABILE
def crea_amministratore(email, password, è_admin):
    if not email or not password:
        return "Errore: email e password obbligatorie"
    
    if not è_admin:
        return "Errore: solo admin possono creare admin"
    
    # Happy path
    return "Admin creato"
```

Ma **non** esagerare:

```python
# ❌ TROPPO COMPLESSO
if not email or not password or len(password) < 8 or not è_admin or email.count("@") == 0:
    return "Errore"

# ✓ SEPARATO
if not email:
    return "Errore: email obbligatoria"

if email.count("@") == 0:
    return "Errore: email non valida"

if not password:
    return "Errore: password obbligatoria"

if len(password) < 8:
    return "Errore: password minimo 8 caratteri"

if not è_admin:
    return "Errore: permessi insufficienti"
```

---

## Guard Clauses vs. Exception Handling

Non sono la stessa cosa:

```python
# Guard clause: prevenire il problema
def dividi(a, b):
    if b == 0:
        return None  # Preveniamo la divisione per zero
    return a / b

# Exception handling: gestire l'errore quando accade
def dividi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None  # Catturiamo l'errore che accade
```

**Quando usare cosa?**
- **Guard clauses**: per errori **prevedibili** (input utente, campi mancanti, ecc.)
- **Exception handling**: per errori **imprevisti** (file non trovato, memoria piena, ecc.)

Nel tuo Batch Signal Processor, usi guard clauses perché sai che i dati potrebbero essere malformati. Se invece stessi leggendo un file e il file non esistesse, useresti exception handling.

---

## Quando **Non** Usare Guard Clauses

Guard clauses non sono sempre la scelta giusta:

```python
# ❌ ECCESSIVO - Guard clauses per cose triviali
def saluta(nome):
    if not nome:
        return ""
    if nome == "Admin":
        return "Ciao Admin!"
    return f"Ciao {nome}"

# ✓ SEMPLICE - Usa if/elif quando la logica è semplice
def saluta(nome):
    if nome == "Admin":
        return "Ciao Admin!"
    return f"Ciao {nome}" if nome else ""
```

Guard clauses brillano quando:
1. Hai **molte condizioni di errore**
2. La **logica principale è complessa**
3. Vuoi **evitare l'indentazione profonda**

Non usarle quando la funzione è così semplice che una singola if/else è più leggibile.

---

## Riassunto: Come Riconoscere un Guard Clause

Una **guard clause** ha sempre questi elementi:

1. **Una condizione che nega il "caso normale"**: `if not valido:` or `if errore:`
2. **Un'uscita immediata**: `return`, `continue`, `break`, oppure `raise`
3. **Nessun "else" complesso**: non hai nidificazione

```python
# Questo è una guard clause:
if condizione_cattiva:
    return risultato_errore  # Uscita immediata

# Questo non è una guard clause (è un if normale):
if condizione_buona:
    # Logica principale indentata
```

---

## Conclusione

Il **guard clause pattern** è uno dei pattern più importanti che imparerai in programmazione. Non è specifico di Python — è universale, usato in ogni linguaggio.

Ricorda:
- **Guard clauses** = verificare i "casi cattivi" prima, uno per uno
- **Uscire presto** = non sprecare CPU/indentazione su casi anomali
- **Lineare** = il codice si legge da cima a fondo senza zigzag
- **Chiaro** = ogni guard clause è una ragione per cui il processo fallisce

Quando avrai scritto 100 funzioni, non potrai vivere senza questo pattern.

---

## Risorse Esterne

- **Real Python**: "Guard Clauses" (articolo)
- **Martin Fowler**: "Replace Nested Conditionals with Guard Clauses" (refactoring classico)
- **Corey Schafer**: Guarda il video su "Conditionals" — non è esplicitamente su guard clauses, ma lui le usa naturalmente

---