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
# - Utilizzare lo structural pattern matching (match/case) con l'uso di "guards" 
#   (if nel case) per determinare la Categoria Peso.
# - Implementare almeno due funzioni helper separate: una per il calcolo del 
#   costo monetario e una per la determinazione della categoria/zona.
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

# OUTPUT ATTESO (Valori indicativi calcolati)
# Il risultato finale dovrà essere un dizionario simile a questo:
# {
#    'Nazionale': {'Small': 7.25, 'Medium': 11.75, 'Large': 33.0},
#    'Europa': {'Small': 14.0, 'Medium': 24.5, 'Large': 49.5},
#    'Extra-UE': {'Small': 27.5, 'Medium': 41.0, 'Large': 112.5}
# }

# SVOLGIMENTO: