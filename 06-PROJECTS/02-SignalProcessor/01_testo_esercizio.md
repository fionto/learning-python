# 🛡️ PROGETTO 02: Protocollo di Sicurezza Base Alpha - Batch Signal Processor

## Obiettivo
Scrivere un programma Python che analizzi una **lista** di segnali in arrivo dai sensori perimetrali della base, scarti i dati corrotti, cataloghi le minacce e determini il livello di allerta generale.

## Specifiche di Input
Il programma riceverà una lista di stringhe. Ogni stringa rappresenta un segnale e ha questo formato grezzo:
`" ID_SEGNALE | CODICE_ZONA | TIPO_MINACCIA | LIVELLO_INTENSITÀ "`

Esempio: `" 4420 | SEC_01 | RAD | 45.5 "`

## Requisiti Funzionali

### 1. Iterazione e Pulizia
Il programma deve scorrere la lista dei segnali.
- Se un segnale è una stringa vuota o contiene solo spazi, deve essere ignorato immediatamente (uso di `continue`).
- La stringa deve essere pulita da spazi bianchi iniziali/finali e separata nei 4 campi usando il separatore `|`.

### 2. Validazione ID (Il Checksum)
Prima di processare il segnale, devi validare l'`ID_SEGNALE` (il primo campo):
- **Step A (Ricerca):** Devi verificare se la stringa dell'ID è composta **solamente da cifre numeriche**. (Cerca nella documentazione Python un metodo delle stringhe che restituisca True se la stringa contiene solo numeri). Se non lo è, il segnale è invalido.
- **Step B (Logica):** Se è numerico, convertilo in intero. Un ID è valido **solo se è un numero PARI**. Se è dispari, il segnale è corrotto.

### 3. Classificazione (Match-Case)
Se l'ID è valido, analizza il `TIPO_MINACCIA`:
- Usa un costrutto `match` per mappare i codici brevi in descrizioni estese:
    - "RAD" -> "Radiazioni"
    - "BIO" -> "Rischio Biologico"
    - "TEC" -> "Guasto Tecnico"
    - Qualsiasi altro codice -> "Sconosciuto"

### 4. Aggregazione Dati
Devi costruire un **Dizionario Report** che tenga traccia di:
- `segnali_totali`: Numero di stringhe processate (escluse quelle vuote).
- `segnali_validi`: Numero di segnali con ID corretto (numerico e pari).
- `segnali_corrotti`: Numero di segnali scartati (ID non numerico o dispari).
- `intensita_totale`: Somma dei valori di `LIVELLO_INTENSITÀ` (convertiti in float) di tutti i segnali **validi**.
- `stato_allerta`: (Vedi punto 5).

### 5. Logica Decisionale Finale (Stato Allerta)
Alla fine del ciclo, determina lo stato di allerta basandoti sui dati aggregati:
- **"CRITICO"**: Se `intensita_totale` > 200 **OPPURE** ci sono più segnali corrotti che validi.
- **"ALTO"**: Se `intensita_totale` è tra 100 e 200 (inclusi) **E** c'è almeno 1 segnale valido di tipo "Rischio Biologico" o "Radiazioni".
- **"NORMALE"**: In tutti gli altri casi.

## Vincoli Tecnici
- Uso obbligatorio di `def main()` e almeno una funzione di supporto (es. per il parsing o la validazione).
- Uso di cicli (`for`) per scorrere la lista.
- Uso di `continue` per saltare iterazioni inutili.
- Uso del `match` statement.
- Nessun suggerimento sull'eleganza: risolvilo come preferisci, purché funzioni.

# Copia queste lista e incollala nel tuo `main()` come input di test
```python
lista_segnali = [
    " 2042 | ZONA_A | RAD | 45.2 ",       # Valido (Pari, Radiazioni)
    " 3311 | ZONA_B | BIO | 12.0 ",       # Corrotto (Dispari)
    " ",                                  # Da ignorare (Vuoto)
    " 1008 | ZONA_C | TEC | 8.5 ",        # Valido (Pari, Tecnico)
    " ERROR | ZONA_X | ??? | 0.0 ",       # Corrotto (ID non numerico)
    " 4096 | ZONA_D | BIO | 95.5 ",       # Valido (Pari, Biologico)
    "    ",                               # Da ignorare (Solo spazi)
    " 6000 | ZONA_E | UNK | 10.0 "        # Valido (Pari, Sconosciuto)
]
```

```python
lista_segnali = [
        " 1000 | ZONA_C | TEC | 150.5 ",       # Valido
        " 2000 | ZONA_D | TEC | 60.0 ",        # Valido
        " 500  | ZONA_A | RAD | 5.0 ",         # Valido
        " 101  | ZONA_X | BIO | 10.0 "         # Corrotto (Dispari)
]
```

```python
lista_segnali = [
        " 8888 | ZONA_A | TEC | 10.0 ",        # Valido (1)
        " 9999 | ZONA_B | BIO | 50.0 ",        # Corrotto (Dispari - 1)
        " ABC  | ZONA_C | RAD | 20.0 ",        # Corrotto (Non numerico - 2)
        " 11   | ZONA_D | TEC | 5.0  "         # Corrotto (Dispari - 3)
]
```

## Esempio di output
```
Analisi Terminata. Generazione Report...
----------------------------------------
REPORT SICUREZZA BASE ALPHA
----------------------------------------
Segnali Rilevati: 6
 - Validi:   4
 - Corrotti: 2

Intensità Totale Rilevata: 159.2
Stato Allerta Calcolato:   ALTO

Dettaglio Dizionario:
{
  'segnali_totali': 6, 
  'segnali_validi': 4, 
  'segnali_corrotti': 2, 
  'intensita_totale': 159.2, 
  'stato_allerta': 'ALTO'
}
```