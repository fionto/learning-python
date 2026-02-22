################################################################################
# 🔐 ESERCIZIO INTERMEDIO: Analisi di Ciframento XOR con Pattern Binari
################################################################################
#
# INPUT:
# messaggi_cifrati = [
#     {"id": "MSG_001", "valore": 245, "chiave": 17},
#     {"id": "MSG_002", "valore": 189, "chiave": 42},
#     {"id": "MSG_003", "valore": 134, "chiave": 15},
#     {"id": "MSG_004", "valore": 210, "chiave": 61},
#     {"id": "MSG_005", "valore": 98,  "chiave": 33},
# ]
#
# parametri = {
#     "bit_count_threshold": 4,
#     "parity_check": True,
#     "pattern_xor": 0b11110000,
# }
#
# RICHIESTE:
# 1. Decifrare ogni messaggio con XOR (valore XOR chiave)
# 2. Contare bit accesi nel messaggio decifrato
# 3. Classificare densità: "alta" se >= threshold, "bassa" altrimenti (match/case)
# 4. Verificare parità: "PARI" se bit_accesi % 2 == 0, "DISPARI" altrimenti (match/case)
# 5. Calcolare Hamming distance: XOR messaggio decifrato con pattern_xor
# 6. Aggregare in dizionario annidato con per_messaggio + statistiche_globali
# 7. Generare report formattato
#
# VINCOLI:
# • 2+ match/case (densità e parità)
# • Funzioni helper: decifra_xor, converti_binario, conta_bit_accesi,
#   calcola_hamming_distance, classifica_messaggio
# • NO try/except
# • NO librerie esterne
#
################################################################################

messaggi_cifrati = [
    {"id": "MSG_001", "valore": 245, "chiave": 17},
    {"id": "MSG_002", "valore": 189, "chiave": 42},
    {"id": "MSG_003", "valore": 134, "chiave": 15},
    {"id": "MSG_004", "valore": 210, "chiave": 61},
    {"id": "MSG_005", "valore": 98,  "chiave": 33},
]

def decifra_xor(valore: int, chiave: int) -> int:
    return valore ^ chiave

def convert_to_binary(number: int) -> str:
    """
    Converte un numero intero positivo nella sua rappresentazione binaria.

    Args:
        number (int): Numero intero positivo da convertire.

    Returns:
        str: Rappresentazione binaria del numero come stringa.

    """

    # Caso speciale: se il numero è 0
    if number == 0:
        return "0"

    binary_string = ""

    # Continua finché il numero è maggiore di 0
    while number > 0:
        remainder = number % 2
        number = number // 2
        binary_string = str(remainder) + binary_string

    return binary_string

print(convert_to_binary(123))