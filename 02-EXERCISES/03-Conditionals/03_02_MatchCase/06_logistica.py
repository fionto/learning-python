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

# Definizioni costanti per dizionario di riepilogo
# COSTANTI: Grandezze pacchi
SMALL = 'Small'
MEDIUM = 'Medium'
LARGE = 'Large'
# COSTANTI: Zone di destinazione
LOCAL = 'Nazionale'
CONTINENTAL = 'Europa'
INTERCONTINENTAL = 'Extra-UE'

# Creo set per destinazioni EUROPEAN-UNION (mia discrezione), tutto il resto è "Nazionale" o "Extra-UE"
EUROPEAN_UNION = {
    "AT",  # Austria
    "BE",  # Belgio
    "BG",  # Bulgaria
    "HR",  # Croazia
    "CY",  # Cipro
    "CZ",  # Repubblica Ceca
    "DK",  # Danimarca
    "EE",  # Estonia
    "FI",  # Finlandia
    "FR",  # Francia
    "DE",  # Germania
    "GR",  # Grecia
    "HU",  # Ungheria
    "IE",  # Irlanda
    "IT",  # Italia
    "LV",  # Lettonia
    "LT",  # Lituania
    "LU",  # Lussemburgo
    "MT",  # Malta
    "NL",  # Paesi Bassi
    "PL",  # Polonia
    "PT",  # Portogallo
    "RO",  # Romania
    "SK",  # Slovacchia
    "SI",  # Slovenia
    "ES",  # Spagna
    "SE",  # Svezia
}

def define_zone(destinazione: str) -> str:
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
    destinazione = destinazione.strip().upper()

    # Validazione di base del codice ISO (2 lettere alfabetiche)
    if len(destinazione) == 2 and destinazione.isalpha():
        match destinazione:
            case "IT":
                return LOCAL
            case _ if destinazione in EUROPEAN_UNION:
                return CONTINENTAL
            case _:
                return INTERCONTINENTAL
    else:
        # TODO: Implementare gestione errori formale (attualmente non supportata).
        # non ho ancora affrontato i blocchi try/except.
        return "ERROR_dz"
    
def define_weight(peso: float) -> str:
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
    # gestione peso negativo
    if peso < 0:
        # TODO: Implementare gestione errori formale (attualmente non supportata).
        # non ho ancora affrontato i blocchi try/except.
        return "ERROR_p"

    # Classificazione per fasce di peso
    if peso <= 2:
        return SMALL
    elif peso <= 10:
        return MEDIUM
    else:
        return LARGE
    
def calculate_shipment_cost(zona: str, peso: float, fragile: bool) -> float:
    """
    Determina il costo della spedizione a seconda della zona di destinazione
    
    Args:
        spedizione (dict): Dizionario contenente tutte le informazioni
        relative alla spedizione

    Returns:
        float: costo per ogni singola spedizione
    """

    surplus = 10 if fragile else 0

    if zona == LOCAL:
        return surplus + 5 + peso * 1.5
    elif zona == CONTINENTAL:
        return surplus + 12 + peso * 2.5
    else:
        return surplus + 25 + peso * 5

def build_weight() -> dict:
    """Inizializza un dizionario per le categorie di peso.

    Crea una struttura dati predefinita per mappare le dimensioni del pacco
    a valori numerici (es. costi o pesi), impostandoli a zero.

    Returns:
        dict: Un dizionario con chiavi SMALL, MEDIUM, LARGE e valori 0.
    """
    return {
        SMALL: 0,
        MEDIUM: 0,
        LARGE: 0,
    }

def build_zone() -> dict:
    """Costruisce la struttura gerarchica delle zone di spedizione.

    Per ogni zona geografica definita (Locale, Continentale, Intercontinentale),
    genera un sotto-dizionario contenente le categorie di peso tramite
    la funzione build_weight().

    Returns:
        dict: Un dizionario nidificato dove ogni chiave di zona punta a una
            mappa di pesi e valori.
    """
    return {
        LOCAL: build_weight(),
        CONTINENTAL: build_weight(),
        INTERCONTINENTAL: build_weight(),
    }

def main():
    riepilogo = build_zone()

    for spedizione in spedizioni_in_entrata:
        
        peso = spedizione['kg']
        fragile = spedizione['fragile']
        zona = define_zone(spedizione["dest"])
        costo = calculate_shipment_cost(zona, peso, fragile)
        grandezza = define_weight(peso)

        riepilogo[zona][grandezza] += costo

    print(riepilogo)

main()

# OUTPUT ATTESO (Valori indicativi calcolati)
# Il risultato finale dovrà essere un dizionario simile a questo:
# {
#    'Nazionale': {'Small': 7.25, 'Medium': 11.75, 'Large': 33.0},
#    'Europa': {'Small': 14.0, 'Medium': 24.5, 'Large': 49.5},
#    'Extra-UE': {'Small': 27.5, 'Medium': 41.0, 'Large': 112.5}
# }