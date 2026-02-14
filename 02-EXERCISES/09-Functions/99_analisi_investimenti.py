# ESERCIZIO: Analisi Portafoglio Investimenti
# ============================================================================
# DESCRIZIONE
# -----------
# Sei un analista finanziario che deve analizzare il portafoglio di
# investimenti di un cliente. Hai a disposizione una lista di transazioni
# (acquisti/vendite) su diversi strumenti finanziari in varie valute.
#
# Devi:
# 1. Processare le transazioni e categorizzare per tipo di strumento
# 2. Calcolare il valore totale per categoria in EUR (conversione necessaria)
# 3. Determinare il rischio complessivo del portafoglio usando una matrice
#    di regole che combina tipo di strumento + valuta + ammontare
# 4. Generare un report aggregato con statistiche per ogni categoria
#
# ============================================================================
# STRUTTURA DATI INPUT
# -----------
# Transazioni = Lista di tuple: (tipo_strumento, valuta, importo, quantita)
#
# Tipo strumento: "STOCK", "BOND", "CRYPTO", "COMMODITY"
# Valuta: "USD", "EUR", "GBP", "JPY"
# Importo: float (prezzo unitario)
# Quantita: int (numero di unità)
#
# Tassi conversione (fissi, non reali):
#   1 USD = 0.92 EUR
#   1 GBP = 1.17 EUR
#   1 JPY = 0.0067 EUR
#
# ============================================================================
# RICHIESTE NUMERICHE
# -----------
# 1. Dato un elenco di transazioni, aggregare il valore totale per categoria
#    di strumento (STOCK, BOND, CRYPTO, COMMODITY)
#
# 2. Per ogni categoria, fornire:
#    - Valore totale in EUR
#    - Numero di transazioni
#    - Importo medio per transazione
#    - Valute coinvolte (come set)
#
# 3. Classificare il rischio COMPLESSIVO del portafoglio come:
#    "CONSERVATIVO" | "MODERATO" | "AGGRESSIVO"
#    usando una funzione che applica match/case su:
#    - Percentuale CRYPTO sul totale
#    - Percentuale BOND sul totale
#    - Presenza di COMMODITY ad alto importo (>10000 EUR)
#
# 4. Per ogni categoria, determinare il rating di rischio individuale
#    ("BASSO" | "MEDIO" | "ALTO") usando match/case su:
#    - tipo_strumento
#    - numero_transazioni
#    - valore_medio_transazione
#
# ============================================================================
# VINCOLI TECNICI OBBLIGATORI
# -----------
# ✓ Implementare 3+ funzioni helper per calcoli aggregati
# ✓ Almeno 2 utilizzi di match/case (uno per rischio portafoglio, uno per
#   rating categoria)
# ✓ Almeno 1 utilizzo di *args per ricevere N transazioni variabili
# ✓ Almeno 1 utilizzo di **kwargs per customizzazione parametri di rischio
#   (es: soglia_crypto=None, soglia_bond=None, soglia_commodity=None)
# ✓ Risultato finale aggregato in dizionario annidato strutturato:
#     {
#       "categoria": {
#         "valore_eur": float,
#         "num_transazioni": int,
#         "importo_medio": float,
#         "valute": set,
#         "rating_rischio": str
#       },
#       ...
#       "portafoglio_totale": {
#         "valore_eur": float,
#         "rischio_complessivo": str
#       }
#     }
# ✓ NO try/except per gestione errori
# ✓ NO lista generata da input() - usare dati forniti
#
# ============================================================================
# OUTPUT ATTESO (approssimativo)
# -----------
# Il programma deve stampare un report strutturato che mostra:
# - Per ogni categoria: statistiche e rating di rischio
# - Totale portafoglio in EUR
# - Classificazione rischio globale
# - Percentuali di esposizione per categoria
#
# Esempio (con dati diversi):
# ┌─────────────────────────────────────────────────┐
# │ CATEGORIA: STOCK                                │
# │ Valore: 15432.50 EUR                            │
# │ Transazioni: 3                                  │
# │ Importo medio: 5144.17 EUR                      │
# │ Valute: {'USD', 'EUR'}                          │
# │ Rating rischio: MEDIO                           │
# └─────────────────────────────────────────────────┘
# ...
# PORTAFOGLIO TOTALE: 45892.30 EUR
# RISCHIO COMPLESSIVO: MODERATO
# Esposizione STOCK: 33.6%
# ...
#
# ============================================================================
# SPECIFICA DATI ORIGINALI
# -----------
# Le transazioni fornite NON devono essere modificate durante l'elaborazione.
# Tutti i calcoli devono avvenire su copie o in strutture dati separate.
# Il dizionario risultato deve essere la sola "fonte di verità" finale.
#
# ============================================================================

# Dati di input

transazioni = [
    ("STOCK", "USD", 150.50, 5),
    ("BOND", "EUR", 98.75, 10),
    ("CRYPTO", "USD", 45000.00, 1),
    ("STOCK", "GBP", 78.25, 8),
    ("COMMODITY", "JPY", 2500.00, 100),
    ("BOND", "USD", 102.30, 15),
    ("STOCK", "EUR", 125.00, 3),
    ("CRYPTO", "EUR", 32500.00, 1),
    ("COMMODITY", "USD", 8500.50, 2),
    ("BOND", "GBP", 99.50, 5),
]

# Tassi di conversione a EUR (fissi)
tassi_conversione = {
    "EUR": 1.00,
    "USD": 0.92,
    "GBP": 1.17,
    "JPY": 0.0067,
}