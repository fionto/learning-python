# ==============================================================================
# DESCRIZIONE DEL PROBLEMA
# Un centro logistico internazionale deve elaborare il report giornaliero delle 
# spedizioni. L'obiettivo è ripartire i costi totali basandosi sulla 
# destinazione geografica e sulla categoria di peso del pacco.
#
# STRUTTURA DATI INPUT:
# Una lista di dizionari denominata 'spedizioni_in_entrata'. Ogni elemento contiene:
# - "id_ordine": stringa univoca
# - "dest": stringa (codice nazione: "IT", "FR", "DE", "US", "UK", "CN")
# - "kg": float (peso del pacco)
# - "fragile": booleano
#
# RICHIESTE NUMERICHE E LOGICHE:
# 1. Suddividere le nazioni in 3 Zone: "Nazionale" (IT), "Europa" (FR, DE), 
#    "Extra-UE" (US, UK, CN).
# 2. Definire la Categoria Peso: "Small" (fino a 2kg inclusi), "Medium" (sopra 2 
#    fino a 10kg inclusi), "Large" (sopra 10kg).
# 3. Calcolare il costo per ogni singola spedizione seguendo queste tariffe base:
#    - Nazionale: 5.0€ base + 1.5€ per ogni kg.
#    - Europa: 12.0€ base + 2.5€ per ogni kg.
#    - Extra-UE: 25.0€ base + 5.0€ per ogni kg.
# 4. Applicare un sovrapprezzo fisso di 10.0€ se il pacco è "fragile".
# 5. Aggregare i costi totali in un dizionario annidato che organizza i dati 
#    per Zona e, all'interno, per Categoria Peso.
#
# VINCOLI TECNICI OBBLIGATORI:
# - Utilizzare lo structural pattern matching (match/case) per gestire la 
#   logica di assegnazione della Zona Geografica.
# - NON modificare i dati originali nella lista 'spedizioni_in_entrata'.
# - NO blocchi try/except.
#
# STRUTTURA OUTPUT ATTESO:
# Un dizionario finale 'report_costi' con questa gerarchia:
# {
#   "Nazionale": {"Small": totale, "Medium": totale, "Large": totale},
#   "Europa": { ... },
#   "Extra-UE": { ... }
# }
# ==============================================================================

# DATI DI INPUT
spedizioni_in_entrata = [
    {"id_ordine": "A001", "dest": "IT", "kg": 1.5, "fragile": False},
    {"id_ordine": "A002", "dest": "IT", "kg": 12.0, "fragile": True},
    {"id_ordine": "A003", "dest": "FR", "kg": 5.0, "fragile": False},
    {"id_ordine": "A004", "dest": "DE", "kg": 0.8, "fragile": False},
    {"id_ordine": "A005", "dest": "US", "kg": 15.5, "fragile": True},
    {"id_ordine": "A006", "dest": "UK", "kg": 3.2, "fragile": False},
    {"id_ordine": "A007", "dest": "CN", "kg": 0.5, "fragile": False},
    {"id_ordine": "A008", "dest": "IT", "kg": 4.5, "fragile": False},
    {"id_ordine": "A009", "dest": "DE", "kg": 11.0, "fragile": True}
]

# SVOLGIMENTO:

EUROPA = {
    "AD",  # Andorra
    "AL",  # Albania
    "AM",  # Armenia
    "AT",  # Austria
    "AZ",  # Azerbaigian
    "BA",  # Bosnia ed Erzegovina
    "BE",  # Belgio
    "BG",  # Bulgaria
    "CH",  # Svizzera
    "CY",  # Cipro
    "CZ",  # Repubblica Ceca
    "DE",  # Germania
    "DK",  # Danimarca
    "EE",  # Estonia
    "ES",  # Spagna
    "FI",  # Finlandia
    "FR",  # Francia
    "GB",  # Regno Unito
    "GE",  # Georgia
    "GR",  # Grecia
    "HR",  # Croazia
    "HU",  # Ungheria
    "IE",  # Irlanda
    "IS",  # Islanda
    "LI",  # Liechtenstein
    "LT",  # Lituania
    "LU",  # Lussemburgo
    "LV",  # Lettonia
    "MC",  # Monaco
    "MD",  # Moldavia
    "ME",  # Montenegro
    "MK",  # Macedonia del Nord
    "MT",  # Malta
    "NL",  # Paesi Bassi
    "NO",  # Norvegia
    "PL",  # Polonia
    "PT",  # Portogallo
    "RO",  # Romania
    "RS",  # Serbia
    "SE",  # Svezia
    "SI",  # Slovenia
    "SK",  # Slovacchia
    "SM",  # San Marino
    "TR",  # Turchia
    "UA",  # Ucraina
    "UK",  # Regno Unito
}

def define_zone(spedizione: dict) -> str:
    """
    Determina la macro-zona geografica della destinazione finale
    a partire dal codice paese ISO 3166-1 alpha-2.

    Args:
        destinazione (dict): Dizionario contenente la chiave 'dest'
            con il codice paese a due caratteri.

    Returns:
        str: Macro-zona geografica ("Nazionale", "Europa", "Extra-UE")
            oppure "ERROR" se il codice non è valido.
    """
    # Normalizzazione del codice paese (rimozione spazi, uppercase)
    destinazione = spedizione["dest"].strip().upper()

    # Validazione di base del codice ISO (2 lettere alfabetiche)
    if len(destinazione) == 2 and destinazione.isalpha():
        match destinazione:
            case "IT":
                return "Nazionale"
            case _ if destinazione in EUROPA:
                return "Europa"
            case _:
                return "Extra-UE"
    else:
        # Codice paese mancante o non conforme allo standard ISO
        return "ERROR"
    
def define_weight(spedizione: dict) -> str:
    """
    Determina la categoria di peso di una spedizione in base al valore
    espresso in chilogrammi.

    Le categorie di peso sono:
    - "Small"  → peso ≤ 2 kg
    - "Medium" → 2 kg < peso ≤ 10 kg
    - "Large"  → peso > 10 kg

    Args:
        spedizione (dict): Dizionario contenente la chiave 'kg'
            con il peso della spedizione espresso come stringa.

    Returns:
        str: Categoria di peso assegnata ("Small", "Medium", "Large")
             oppure "ERROR" se il valore del peso non è valido.
    """
    # Estrazione e normalizzazione del peso
    peso = (spedizione["kg"])

    # gestione peso negativo
    if peso < 0:
        return "ERROR: peso negativo non valido"

    # Classificazione per fasce di peso
    if peso <= 2:
        return "Small"
    elif peso <= 10:
        return "Medium"
    else:
        return "Large"
    
def calculate_shipment_cost(spedizione: dict):
    """
    Determina il costo della spedizione a seconda della zona di destinazione
    
    Args:
        spedizione (dict): Dizionario contenente tutte le informazioni
        relative alla spedizione

    Returns:
        float: costo per ogni singola spedizione
    """

    pass

for spedizione in spedizioni_in_entrata:
    print(f"{define_zone(spedizione)}, {define_weight(spedizione)}")


# OUTPUT ATTESO (Valori indicativi calcolati)
# Il risultato finale dovrà essere un dizionario simile a questo:
# {
#    'Nazionale': {'Small': 7.25, 'Medium': 11.75, 'Large': 33.0},
#    'Europa': {'Small': 14.0, 'Medium': 24.5, 'Large': 49.5},
#    'Extra-UE': {'Small': 27.5, 'Medium': 41.0, 'Large': 112.5}
# }