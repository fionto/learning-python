# 🚀 Esercizio: Sistema di Monitoraggio Stazione Spaziale

**Progetto:** 03-AggregatedLogParser  
**Difficulty:** Medium/High  
**Concepts:** Nested Dictionaries, Sets, While Loops, Match-Case, Data Aggregation  
**Date:** January 2026  

---

## 📋 Obiettivo

Implementare un sistema di analisi per i log di manutenzione della Stazione Spaziale Internazionale (ISS). Il sistema deve processare report giornalieri dai vari moduli, identificare anomalie critiche, e generare un rapporto di stato aggregato per il controllo missione.

---

## 📥 Specifiche Input

Riceverai una lista di stringhe grezze. Ogni stringa rappresenta un log di un modulo della ISS nel formato:

```
"MODULO#TIMESTAMP#SISTEMA#STATO#PRIORITA"
```

### Componenti

- **MODULO**: Codice alfanumerico del modulo (es. "COLUMBUS", "DESTINY", "KIBO")
- **TIMESTAMP**: Formato `GGMMAAAA-HHMM` (es. "02012026-1430")
- **SISTEMA**: Nome del sistema controllato (es. "Life Support", "Power Grid", "Communications")
- **STATO**: Valore numerico da 0 a 100 (efficienza percentuale)
- **PRIORITA**: Stringa tra "LOW", "MEDIUM", "HIGH", "CRITICAL"

### Esempio Log Valido

```python
"COLUMBUS#02012026-1430#Life Support#95#LOW"
```

---

## ✅ Requisiti Funzionali

Il tuo programma deve:

### 1. Pulizia Dati
Rimuovere spazi bianchi superflui da ogni log e scartare stringhe completamente vuote.

### 2. Validazione Strutturale
Per ogni log, verificare che contenga esattamente 5 componenti separate da `#`. I log malformati devono essere contati ma ignorati nel processing successivo.

### 3. Parsing e Conversione
Estrarre i componenti di ogni log valido e convertire lo STATO in numero intero.

### 4. Classificazione Anomalie
Ogni log deve essere classificato come:

- **NORMALE**: STATO >= 80 AND PRIORITA in ["LOW", "MEDIUM"]
- **ATTENZIONE**: STATO tra 60-79 OR PRIORITA == "HIGH"
- **EMERGENZA**: STATO < 60 OR PRIORITA == "CRITICAL"

### 5. Aggregazione per Modulo
Raggruppare tutti i log per MODULO. Per ogni modulo, calcolare:

- Numero totale di log processati
- STATO medio (come numero intero arrotondato)
- Numero di emergenze rilevate
- Data dell'ultimo report (estrarre solo `GGMMAAAA` dal timestamp più recente)

### 6. Generazione Report Finale
Creare un dizionario strutturato che contenga:

- Chiave `"metadata"`: dizionario con `"total_logs"`, `"invalid_logs"`, `"modules_count"`
- Chiave `"modules"`: dizionario dove ogni chiave è il nome del MODULO e il valore è un dizionario con le metriche aggregate
- Chiave `"critical_alerts"`: lista di stringhe con i nomi dei moduli che hanno almeno 1 emergenza

### 7. Output
Stampare il dizionario finale in modo leggibile con separatori visivi.

---

## 🔒 Vincoli Tecnici

### OBBLIGATORI

- Usare almeno un ciclo `while` per il processing dei log
- Usare `match-case` per la classificazione delle anomalie
- Usare dizionari per l'aggregazione
- Usare set per tracciare i moduli unici
- NON usare funzioni esterne (tutto nel `main()` o in max 2 funzioni helper)

### VIETATI

- List comprehension
- Librerie esterne (solo built-in Python)
- Try-except per gestione errori (validare manualmente)

---

## 📊 Dati di Input

### Test Case 1: Dataset Principale

```python
station_logs = [
    "COLUMBUS#02012026-1430#Life Support#95#LOW",
    "DESTINY#02012026-1445#Power Grid#78#HIGH",
    "KIBO#02012026-1500#Communications#45#CRITICAL",
    "   ",  # Log vuoto
    "COLUMBUS#03012026-0800#Thermal Control#88#MEDIUM",
    "DESTINY#02012026-1530#Cooling System#62#MEDIUM",
    "ZARYA#02012026-1600#Navigation",  # Malformato (4 componenti invece di 5)
    "KIBO#03012026-0900#Life Support#92#LOW",
    "COLUMBUS#02012026-1700#Power Grid#55#HIGH",
    "DESTINY#03012026-1000#Life Support#91#LOW",
    "",  # Stringa vuota
    "ZARYA#03012026-1100#Communications#70#MEDIUM",
    "KIBO#02012026-1800#Thermal Control#30#CRITICAL",
    "COLUMBUS#04012026-0700#Life Support#97#LOW",
    "TRANQUILITY#03012026-1200#Water Recovery#85#LOW"
]
```

### Test Case 2: Edge Cases Estremi

```python
station_logs_test2 = [
    "UNITY#05012026-0600#Docking Port#100#LOW",
    "UNITY#05012026-0615#Docking Port#100#LOW",
    "UNITY#05012026-0630#Docking Port#100#LOW",
    "",
    "QUEST#05012026-0700#Airlock#0#CRITICAL",  # Stato 0!
    "QUEST#05012026-0715#Airlock#0#CRITICAL",
    "   ",
    "CUPOLA#05012026-0800#Windows#79#MEDIUM",  # Limite 79 (soglia)
    "CUPOLA#05012026-0815#Windows#80#MEDIUM",  # Limite 80 (soglia)
    "CUPOLA#05012026-0830#Windows#59#LOW",     # Limite 59 (soglia)
    "CUPOLA#05012026-0845#Windows#60#LOW",     # Limite 60 (soglia)
    "LEONARDO#05012026#Cargo",  # Malformato (3 componenti)
    "LEONARDO##05012026-0900##Storage##50##HIGH",  # Doppi separatori!
]
```

### Test Case 3: Tutti Invalidi per Un Modulo

```python
station_logs_test3 = [
    "NODE2#06012026-1000#Berthing#88#LOW",
    "NODE2#06012026-1015#Berthing#92#LOW",
    "NODE3#Invalid#Log",  # Malformato
    "NODE3#Another#Bad#One",  # Malformato (4 componenti)
    "",
    "NODE3",  # Malformato (1 componente)
    "PMM#06012026-1100#Storage#55#CRITICAL",
]
```

### Test Case 4: Date Non Cronologiche

```python
station_logs_test4 = [
    "ZARYA#10012026-1200#Control#75#MEDIUM",   # 10 Gennaio
    "ZARYA#08012026-1300#Control#80#LOW",      # 08 Gennaio (torna indietro!)
    "ZARYA#12012026-0900#Control#70#MEDIUM",   # 12 Gennaio (ultimo cronologico)
    "ZARYA#09012026-1500#Control#85#LOW",      # 09 Gennaio
]
```

### Test Case 5: Tutte Emergenze

```python
station_logs_test5 = [
    "NAUKA#07012026-0800#Science#50#CRITICAL",
    "NAUKA#07012026-0830#Science#45#CRITICAL",
    "PIRS#07012026-0900#Docking#30#HIGH",
    "PIRS#07012026-0930#Docking#20#CRITICAL",
]
```

---

## 📤 Output Atteso

### Test Case 1: Output

```
==================================================
    REPORT STATO STAZIONE SPAZIALE ISS
==================================================

METADATA:
----------
Total Logs Processati: 13
Log Invalidi: 2
Moduli Attivi: 5

==================================================
DETTAGLIO MODULI:
==================================================

COLUMBUS:
  - Reports: 4
  - Stato Medio: 83%
  - Emergenze: 1
  - Ultimo Report: 04012026

DESTINY:
  - Reports: 3
  - Stato Medio: 77%
  - Emergenze: 0
  - Ultimo Report: 03012026

KIBO:
  - Reports: 3
  - Stato Medio: 55%
  - Emergenze: 2
  - Ultimo Report: 03012026

ZARYA:
  - Reports: 1
  - Stato Medio: 70%
  - Emergenze: 0
  - Ultimo Report: 03012026

TRANQUILITY:
  - Reports: 1
  - Stato Medio: 85%
  - Emergenze: 0
  - Ultimo Report: 03012026

==================================================
ALLERTA CRITICA:
==================================================
Moduli con emergenze attive: COLUMBUS, KIBO

==================================================
```

### Test Case 2: Output Atteso

```
METADATA:
Total Logs: 10
Invalid: 3
Modules: 3

UNITY:
  - Reports: 3
  - Stato Medio: 100
  - Emergenze: 0

QUEST:
  - Reports: 2
  - Stato Medio: 0
  - Emergenze: 2

CUPOLA:
  - Reports: 4
  - Stato Medio: 69
  - Emergenze: 2

Critical alerts: QUEST, CUPOLA
```

### Test Case 3: Output Atteso

```
METADATA:
Total Logs: 3
Invalid: 4
Modules: 2

NODE2:
  - Reports: 2
  - Stato Medio: 90
  - Emergenze: 0

PMM:
  - Reports: 1
  - Stato Medio: 55
  - Emergenze: 1

Critical alerts: PMM
```

### Test Case 4: Output Atteso

```
ZARYA:
  - Reports: 4
  - Stato Medio: 77
  - Emergenze: 0
  - Ultimo Report: 12012026  # La data più recente!
```

### Test Case 5: Output Atteso

```
METADATA:
Modules: 2

NAUKA:
  - Emergenze: 2

PIRS:
  - Emergenze: 2

Critical alerts: NAUKA, PIRS
```

---

## 📝 Note sull'Output

- Gli stati medi sono arrotondati all'intero più vicino
- Le date sono nel formato `GGMMAAAA` estratto dal timestamp
- I moduli nel report critico appaiono in ordine alfabetico (o ordine di inserimento)
- Il formato esatto della stampa può variare, ma i dati numerici devono coincidere

---

## 🎯 Obiettivi Didattici

Questo esercizio verifica la capacità di:

1. **Validare dati** strutturati con parsing manuale
2. **Aggregare informazioni** da fonti multiple
3. **Costruire dizionari annidati** complessi
4. **Gestire set** per tracciare valori unici
5. **Implementare logica condizionale** con `match-case`
6. **Iterare con while loops** in modo controllato
7. **Calcolare metriche** (media, conteggi, massimi)

---

**Buon lavoro, Astronauta! 🚀**