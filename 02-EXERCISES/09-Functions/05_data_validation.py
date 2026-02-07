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

MEASURED_QUANTITIES = {'temp', 'humidity'}

def calculate_mean_std(data: list[float]) -> tuple[float, float]:
    """
    Calcola media e deviazione standard della popolazione.

    Args:
        data: Una lista di numeri (int o float).

    Returns:
        Una tupla contenente (media, deviazione_standard).
        Restituisce (0.0, 0.0) in caso di errore critico.
    """
    
    # 1. Controllo che l'input sia una lista
    if type(data) != list:
        print("Errore calcolo dev_std: l'input deve essere una lista.")
        return 0.0, 0.0

    # 2. Controllo che ci siano elementi per evitare divisioni per zero
    if len(data) == 0:
        print("Errore calcolo dev_std: la lista è vuota.")
        return 0.0, 0.0

    # --- Inizio del calcolo ---
    
    n = len(data)
    mean = sum(data) / n
    
    # Caso limite: se c'è un solo elemento, la dispersione è zero
    if n < 2:
        print("Avviso: con un solo valore la deviazione standard è 0.0.")
        return mean, 0.0
    
    # Calcolo scarti quadratici
    squared_diffs = [(x - mean) ** 2 for x in data]
    
    # Varianza e Deviazione Standard
    variance = sum(squared_diffs) / n
    std_dev = variance ** 0.5
    
    return mean, std_dev

def is_valid_float(value: str) -> bool:
    """
    Verifica se una stringa può essere convertita in un numero decimale (float).
    
    La funzione valida la stringa controllando manualmente la presenza di segni,
    punti decimali e cifre numeriche, senza l'uso di blocchi try/except.

    Args:
        value: La stringa da analizzare.

    Returns:
        True se la stringa è un formato numerico valido, False altrimenti.
    """
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

def validate_key(key: str) -> tuple[str, bool]:
    """
    Normalizza una chiave e ne verifica la validità.

    Args:
        key: La stringa che rappresenta la chiave da validare.

    Returns:
        Una tupla (chiave_pulita, stato_validazione).
        - chiave_pulita: La stringa senza spazi bianchi e in minuscolo.
        - stato_validazione: True se la chiave è valida, False altrimenti.
    """

    # 1. Pulizia della stringa (rimozione spazi e normalizzazione)
    clean_key = key.strip().lower()

    # 2. Controllo validità (esempio: non deve essere vuota)
    if not clean_key:
        return "", False
    
    # 3. Controllo che siano nel set di stringhe accettate
    if clean_key not in MEASURED_QUANTITIES:
        return "", False
    
    return clean_key, True
    
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
        print("Errore validate_and_convert: numero campi errato.")
        return None
    
    sensor_id, temp_str, humidity_str, time_str = fields
    
    # Early return: se non validi come float
    if not (is_valid_float(temp_str) and is_valid_float(humidity_str)):
        print("Errore validate_and_convert: campo temp o humidity non è un float.")
        return None
    
    temp = float(temp_str)
    humidity = float(humidity_str)

    # Early return: se fuori range
    if not (-50 <= temp <= 150 and 0 <= humidity <= 100):
        print("Errore validate_and_convert: campo temp o humidity fuori range.")
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
def calculate_statistics(data_list: list[dict], key: str) -> dict | None:
    """Calcola statistiche su dati validi.
    
    Args:
        data_list: Lista di dizionari (output da validate_and_convert)
        key: 'temp' o 'humidity'
    
    Returns:
        Dizionario con {avg, min, max, count} se dati presenti
        None se lista vuota o nessun dato valido
    """

    clean_key, valid_key = validate_key(key)

    # Early return: se key sbagliata
    if not valid_key:
        return None
    
    # Filtra None E estrai valori in una riga (list comprehension completa)
    values = [reading[clean_key] for reading in data_list if reading]

    # Early return: se nessun dato valido
    if not values:
        return None    
    
    count = len(values)

    return {
        'avg': round(sum(values) / count, 2), 
        'v_min': min(values), 
        'v_max': max(values), 
        'count': count,
        }

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
def remove_anomalies(data_list: list[dict], key: str, threshold: float = 2) -> list:
    """
    Rimuove i record i cui valori cadono fuori dall'intervallo [media ± threshold * std].

    Args:
    data_list: Lista di dizionari (output da validate_and_convert)
    key: 'temp' o 'humidity'
    threshold: numero di deviazioni standard (default=2)
    
    Returns:
        Lista filtrata di dizionari
    """

    clean_key, valid_key = validate_key(key)

    # Early return: se key sbagliata
    if not valid_key:
        return []

    valid_data = [reading for reading in data_list if reading]

    # Early return: se nessun dato valido
    if not valid_data:
        return []
    
    values = [reading[clean_key] for reading in valid_data]
    mean, std = calculate_mean_std(values)
    
    filtered_list = [reading for reading in valid_data if mean - (std * threshold) <= reading[clean_key] <= mean + (std * threshold)]

    print(f"Anomalies removed: {len(valid_data) - len(filtered_list)}")

    return filtered_list


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

def main():
    data_list = []
    for signal in test_data:
        data_list.append(validate_and_convert(signal))
    
    temp_stats = calculate_statistics(data_list, 'temp')

    if temp_stats:
        print("=== SENSOR DATA REPORT ===")
        print(f"Temperature - Avg: {temp_stats['avg']}, "
              f"Min: {temp_stats['v_min']}, "
              f"Max: {temp_stats['v_max']}, "
              f"Records: {temp_stats['count']}")    
    else:
        print("No valid data is present")
    
    filtered_list = (remove_anomalies(data_list, 'temp'))

    new_temp_stats = calculate_statistics(filtered_list, 'temp')

    if new_temp_stats:
        print("=== SENSOR DATA REPORT ===")
        print(f"Temperature - Avg: {new_temp_stats['avg']}, "
              f"Min: {new_temp_stats['v_min']}, "
              f"Max: {new_temp_stats['v_max']}, "
              f"Records: {new_temp_stats['count']}")    
    else:
        print("No valid data is present")

main()