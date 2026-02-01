# ============================================================================
# EXERCISE 8.1: Sensor Data Validator and Processor
# ============================================================================
# 
# Contesto:
# Stai sviluppando un sistema di monitoraggio per una rete di sensori di 
# temperatura distribuiti in una struttura. I dati grezzi arrivano in 
# formato stringa e devono essere validati, processati e aggregati.
#
# Requisiti:
# 1. Crea una funzione che valida e converte letture di sensore
# 2. Crea una funzione che calcola statistiche su più letture
# 3. Crea una funzione che filtra anomalie dai dati
# 4. Integra le tre funzioni in un programma principale
#
# ============================================================================

# Input fornito:
# Una lista di stringhe nel formato: "SENSOR_ID|TEMPERATURA|UMIDITA|TIMESTAMP"
# Esempio: "SENS_01|22.5|45.3|14:30"

# FUNZIONE 3: remove_anomalies()
# --------------------------------
# Parametri:
#   - data_list: lista di dizionari
#   - key: quale metrica controllare ('temp' o 'humidity')
#   - threshold: numero di deviazioni standard (default=2)
#
# Comportamento:
#   - Calcolare media e deviazione standard dei dati validi
#   - Rimuovere record dove il valore è oltre threshold deviazioni std dalla media
#   - Restituire lista filtrata
#   - Stampare numero di anomalie rimosse
#
# Formula deviazione standard:
#   1. Calcola media
#   2. Per ogni valore: (valore - media)^2
#   3. Fai media dei quadrati
#   4. Prendi radice quadrata
#
# Suggerimento: 
#   - Puoi usare math.sqrt() oppure x ** 0.5


# FUNZIONE 4: main()
# ------------------
# Coordina il flusso:
#   1. Ricevi lista di stringhe di sensori
#   2. Valida e converte ogni stringa
#   3. Calcola statistiche su temperatura PRIMA delle anomalie
#   4. Rimuovi anomalie da temperatura
#   5. Calcola statistiche su temperatura DOPO le anomalie
#   6. Stampa report con confronti
#
# Output atteso (formato):
#   """
#   === SENSOR DATA REPORT ===
#   
#   STATISTICS BEFORE ANOMALY REMOVAL:
#   Temperature - Avg: XX.X°C, Min: XX.X°C, Max: XX.X°C, Records: N
#   
#   Anomalies removed: N
#   
#   STATISTICS AFTER ANOMALY REMOVAL:
#   Temperature - Avg: XX.X°C, Min: XX.X°C, Max: XX.X°C, Records: N
#   """


# ============================================================================
# DATI DI TEST (copia-incolla per testare)
# ============================================================================

test_data = [
    "SENS_01|22.5|45.3|14:30",
    "SENS_02|23.1|46.2|14:30",
    "SENS_03|22.8|44.9|14:30",
    "SENS_04|150.5|50.0|14:30",      # Anomalia: temperatura troppo alta
    "SENS_05|21.9|47.1|14:30",
    "SENS_06|-5.3|43.2|14:30",        # Anomalia: temperatura troppo bassa (ma valida)
    "SENS_07|23.2|45.8|14:30",
    "SENS_08|INVALID|50.0|14:30",     # Formato errato
    "SENS_09|22.7|101.5|14:30",       # Anomalia: umidità sopra 100%
    "SENS_10|24.1|44.5|14:30",
]

def is_valid_float(value: str) -> bool:    
    value = value.strip()

    # Gestisce il segno opzionale all'inizio
    if value.startswith(("+", "-")):
        value = value[1:]

    # Gestisce se è vuota
    if not value or value == ".":
        return False
    
    dot_count = 0
    for char in value:
        if char == ".":
            dot_count += 1
            if dot_count > 1: return False # Massimo un punto permesso
        elif not ('0' <= char <= '9'): # Confronto tabella
            return False    
    return True

# FUNZIONE 1: validate_and_convert()
# ------------------------------------
# Parametri:
#   - sensor_string: stringa nel formato "ID|TEMP|UMID|TIME"
# 
# Comportamento:
#   - Dividere la stringa nei componenti
#   - Convertire temperatura e umidità in float
#   - Validare che temperatura sia tra -50 e 150 °C
#   - Validare che umidità sia tra 0 e 100 %
#   - Se valido: restituire dizionario con chiavi sensor_id, temp, humidity, time
#   - Se invalido: restituire None e stampare motivo dell'errore
#
# Cosa deve gestire:
#   - Spazi extra (usare .strip())
#   - Valori fuori range
#   - Formato non corretto
def validate_and_convert(sensor_string: str) -> dict | None:
    """Valida e converte letture di sensore.
    
    PATTERN: Early Return
    Invece di annidare if/else (nested hell), usa 'return None' subito
    quando una condizione fallisce.

    Args:
        sensor_string: Stringa nel formato "ID|TEMP|HUMIDITY|TIME"
    
    Returns:
        Dizionario con chiavi sensor_id, temp, humidity, time se valido, None altrimenti
    """

    fields = sensor_string.strip().split("|")
    
    # Early return: se numero campi errato, non continuare
    if len(fields) != 4:
        return None
    
    sensor_id, temp_str, humidity_str, time_str = fields
    
    # Early return: se non validi come float
    if not (is_valid_float(temp_str) and is_valid_float(humidity_str)):
        return None
    
    temp = float(temp_str)
    humidity = float(humidity_str)

    # Early return: se fuori range
    if not (-50 <= temp <= 150 and 0 <= humidity <= 100):
        return None
    
    # Solo qui, al fondo, il caso di successo
    return {
        'sensor_id': sensor_id.strip(),
        'temp': temp,
        'humidity': humidity,
        'time': time_str.strip()
    }

# FUNZIONE 2: calculate_statistics()
# -----------------------------------
# Parametri:
#   - data_list: lista di dizionari (output dalla funzione 1)
#   - key: stringa per specificare quale valore aggregare ('temp' o 'humidity')
#
# Comportamento:
#   - Estrarre solo i record validi (non None)
#   - Calcolare: media, min, max, numero record validi
#   - Restituire dizionario con chiavi: avg, min, max, count
#
# Vincoli:
#   - Usare funzioni built-in (sum, min, max, len)
#   - Gestire lista vuota (restituire None)
    
for data in test_data:
    print(validate_and_convert(data))