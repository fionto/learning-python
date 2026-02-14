# ESERCIZIO: Analizzatore di Performance e Rischio Portafoglio (Intermediate Level)
# 
# DESCRIZIONE:
# Dato un portafoglio di asset finanziari, sviluppare un sistema di analisi che calcoli:
# 1. Il valore attuale totale e il profitto/perdita (P/L) percentuale per ogni asset.
# 2. La tassazione stimata sui guadagni in base alla tipologia di asset.
# 3. Un'aggregazione dei risultati in un dizionario annidato organizzato per SETTORE e TIPO ASSET.
# 
# STRUTTURA DATI INPUT:
# Una lista di dizionari chiamata 'transazioni_asset'. 
# Ogni dizionario contiene: 'ticker', 'tipo', 'settore', 'quantita', 'prezzo_acquisto', 'prezzo_mercato'.
# 
# RICHIESTE NUMERICHE:
# - Calcolare il valore di mercato (quantita * prezzo_mercato).
# - Calcolare la performance percentuale: ((prezzo_mercato - acquisto) / acquisto) * 100.
# - Calcolare le tasse potenziali (solo su asset in guadagno): 
#     * Azioni: 26%
#     * Obbligazioni: 12.5%
#     * Crypto: 26% (Applicare solo se il VALORE TOTALE del comparto Crypto nel portafoglio supera i 2000€).
# 
# VINCOLI TECNICI OBBLIGATORI:
# 1. Utilizzare match/case per gestire la TASSAZIONE in base al 'tipo'.
# 2. Utilizzare match/case per assegnare una 'categoria_performance' basata sul P/L %:
#    - > 20%: "Eccellente"
#    - Tra 5% e 20%: "Buona"
#    - Tra 0% e 5%: "Stabile"
#    - < 0%: "Sotto-performante"
# 3. Implementare almeno 2 'helper functions' per i calcoli atomici (es. tasse, performance).
# 4. Aggregare i dati in un dizionario annidato: {settore: {tipo_asset: valore_totale_mercato_per_quel_tipo}}.
# 5. TRATTAMENTO DATI ORIGINALI: La lista di input deve rimanere IMMUTATA.
# 6. NO try/except. NO OOP.
#
# TEMPO DI RISOLUZIONE STIMATO: 20-25 minuti.

# --- DATI DI INPUT ---
transazioni_asset = [
    {"ticker": "AAPL", "tipo": "Azione", "settore": "Tech", "quantita": 10, "prezzo_acquisto": 150.0, "prezzo_mercato": 190.0},
    {"ticker": "BTC", "tipo": "Crypto", "settore": "Tech", "quantita": 0.05, "prezzo_acquisto": 30000.0, "prezzo_mercato": 45000.0},
    {"ticker": "BTP-5Y", "tipo": "Obbligazione", "settore": "Gov", "quantita": 2000, "prezzo_acquisto": 1.0, "prezzo_mercato": 1.02},
    {"ticker": "TSLA", "tipo": "Azione", "settore": "Tech", "quantita": 5, "prezzo_acquisto": 250.0, "prezzo_mercato": 180.0},
    {"ticker": "ENI", "tipo": "Azione", "settore": "Energy", "quantita": 100, "prezzo_acquisto": 14.0, "prezzo_mercato": 15.5},
    {"ticker": "ETH", "tipo": "Crypto", "settore": "Tech", "quantita": 1.2, "prezzo_acquisto": 1800.0, "prezzo_mercato": 2400.0}
]

# --- OUTPUT ATTESO (per controllo finale) ---
# Dati Aggregati:
# {
#   'Tech': {'Azione': 2800.0, 'Crypto': 5130.0}, 
#   'Gov': {'Obbligazione': 2040.0}, 
#   'Energy': {'Azione': 1550.0}
# }
# 
# Esempi di valori singoli calcolati (per verifica funzioni):
# - AAPL: Valore 1900.0, Performance 26.67% (Eccellente), Tasse 104.0
# - TSLA: Valore 900.0, Performance -28.0% (Sotto-performante), Tasse 0.0
# - BTC: Valore 2250.0, Performance 50.0% (Eccellente), Tasse 195.0 (Soglia crypto superata)
# ---------------------------------------------

# Inizia qui la tua implementazione...