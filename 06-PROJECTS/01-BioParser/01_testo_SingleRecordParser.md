# 🧬 PROGETTO 01: Bio-Informatic Single Record Parser

## Obiettivo
Sviluppare un parser in Python per elaborare una **singola stringa grezza** proveniente da uno strumento di analisi biologica. Il programma deve pulire i dati, calcolare margini di errore e validare il campione, senza utilizzare strutture di controllo di flusso.

## Specifiche di Input
Il programma riceve una stringa singola in questo formato "sporco":
`" ID_Grezzo : NOME_CAMPIONE : VALORE_MISURATO : ERRORE_STRUMENTO "`

Esempio: `" id-2021 : mArS_sOiL-sAmPlE : 12.500 : 0.15 "`

## Requisiti Funzionali

### 1. Parsing e Pulizia Stringhe
- Separare la stringa in 4 campi usando il delimitatore `:`.
- **Nome Campione:**
    - Deve essere convertito in *Title Case* (es. "Mars Soil Sample").
    - Rimuovere spazi extra agli estremi.
    - Sostituire eventuali trattini `-` o underscore `_` con spazi vuoti.
- **ID:** Rimuovere spazi bianchi.

### 2. Generazione Codice Univoco
Generare un codice identificativo combinando:
- Le prime **3 lettere** del Nome pulito (tutto in MAIUSCOLO).
- Le ultime **2 cifre** dell'ID grezzo.
- *Esempio:* "Mars Soil..." + "...21" -> `MAR21`.

### 3. Calcolo Matematico (Casting e Float)
- Convertire Valore ed Errore in numeri decimali (`float`).
- Calcolare i limiti di confidenza:
    - `Minimo = Valore - Errore`
    - `Massimo = Valore + Errore`
- Arrotondare i risultati matematici a **3 cifre decimali**.
- Salvare questi due valori in una **Tupla**.

### 4. Validazione (Senza If)
Verificare se il "Codice Univoco" generato appartiene al database dei campioni attesi.
- Database (Set): `{"MAR21", "VEN22", "JUP01"}`.
- Il risultato deve essere un valore Booleano (`True`/`False`) salvato nel dizionario.

### 5. Output Strutturato
Costruire e stampare un dizionario finale con le seguenti chiavi:
- `id_originale`
- `nome_pulito`
- `valore_misurato`
- `range_confidenza` (la tupla min/max)
- `codice_generato`
- `is_valid` (booleano)

## Vincoli Tecnici (Hardcore Mode)
- **VIETATO** l'uso di `if`, `else`, `elif`.
- **VIETATO** l'uso di cicli `for` o `while`.
- Obbligo di definire una funzione `main()` e almeno una funzione di supporto per il parsing.
- Uso corretto del casting (`str` -> `float`).

---

## Dati di Test (Input)

Copia questa variabile nel tuo `main()`:

```python
# Stringa "sporca" simulata
raw_data = " id-9821 :  aLieN_DN-a_pRoBe  : 84.2399 : 0.0012 "
    
# Set di autorizzazione
AUTHORIZED_CODES = {"MAR21", "ALI21", "JUP99"}
```

---

## Output Atteso

Il terminale deve mostrare esattamente questo dizionario (l'ordine delle chiavi può variare):

```python
{
    'id_originale': 'id-9821', 
    'nome_pulito': 'Alien Dn A Probe', 
    'valore_misurato': 84.24, 
    'range_confidenza': (84.239, 84.241), 
    'codice_generato': 'ALI21', 
    'is_valid': True
}
```