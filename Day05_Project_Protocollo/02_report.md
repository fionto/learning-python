# 📝 REPORT FINALE: PROTOCOLLO BASE ALPHA & LOGICA PYTHON
**(Focus: Manipolazione Stringhe, Validazione Dati, Logica Condizionale)**

---

## 1. IL PROGETTO: "Base Spaziale Alpha"
**Obiettivo:** Costruire un parser robusto per analizzare segnali grezzi (`" ID | ZONA | TIPO | VALORE "`), filtrare dati corrotti e determinare un livello di allerta di sicurezza.

### Concetti Chiave Utilizzati
* **Strutture Dati:** Liste (iterazione), Set (ricerca veloce `O(1)`), Dizionari (aggregazione dati).
* **Logica:** Condizionali complessi (`if/elif`), Match-Case (Python 3.10+), Operatori Logici (`and`/`or`).
* **Manipolazione:** Parsing stringhe (`split`, `strip`), Casting (`int`, `float`), Validazione (`isdigit`, parità).

---

## 2. ANALISI DEL CODICE (Evoluzione)

### A. Tecniche "Senior" Apprese (Senza Try/Except)
Abbiamo analizzato come uno sviluppatore esperto scriverebbe il codice rispettando gli stessi vincoli (no gestione errori automatica).

**1. Unpacking (Spacchettamento)**
Invece di usare indici numerici ciechi (`lista[0]`), assegniamo variabili subito:
```python
# Invece di: intensita = parti[3]
id_str, zona, tipo, val_str = riga_pulita.split('|')
# Ora il codice si legge come un libro: float(val_str)
```

**2. Dizionario "Single Source of Truth"**
Invece di avere 10 variabili sparse (`conta_validi`, `conta_corrotti`, ecc.), si usa un unico dizionario `report` che viene passato tra le funzioni.

**3. Il Flag "Latch" (Persistente)**
Per sapere se c'è *almeno* una minaccia grave:
```python
if tipo in MINACCE_CRITICHE:
    report["ha_rischio_grave"] = True
# Una volta True, non torna più False (memoria dell'evento).
```

---

## 3. APPROFONDIMENTO: Validazione Float "Manuale"
Una delle sfide maggiori è stata validare numeri decimali (es. `"10.5"` o `"-10.5"`) o scartare errori (es. `"dieci"`) usando solo `.isdigit()`.

### La Tecnica del "Replace"
Poiché `.isdigit()` restituisce `False` se trova punti o trattini, dobbiamo "pulire" la stringa temporaneamente per il controllo.

**Algoritmo per Float Positivi e Negativi:**
```python
temp_val = val_str

# 1. Gestione Segno Meno (Solo se all'inizio)
if temp_val.startswith('-'):
    temp_val = temp_val[1:] # Rimuove il primo carattere

# 2. Gestione Punto Decimale (Rimuove solo la prima occorrenza)
check_float = temp_val.replace('.', '', 1)

# 3. Controllo Finale
if check_float.isdigit():
    valore = float(val_str) # Sicuro da convertire
else:
    print("Dato non valido") # Es: "dieci", "10..5", "12-20"
```

> **Nota Didattica:** Questo processo laborioso evidenzia perché in Python si preferisce il paradigma **EAFP** (*It's Easier to Ask Forgiveness than Permission*) usando blocchi `try/except`, che vedremo nel prossimo modulo.

---

## 4. CHECKLIST COMPETENZE ACQUISITE
- [x] Saper dividere un problema in Input -> Processing -> Output.
- [x] Uso di `continue` per saltare iterazioni "sporche".
- [x] Differenza tra uguaglianza (`==`) e identità (`is`).
- [x] Validazione dati numerici manuale.
- [x] Separazione tra Dati (Codici 'RAD') e Visualizzazione (Stringhe 'Radiazioni').

**Stato Studente:** Pronto per Gestione Errori (`try/except`) e File System (I/O).