# OBIETTIVO
# Sviluppare un prototipo di "Portfolio Analyzer" che trasformi un registro di transazioni
# finanziarie grezzo (stringhe sporche) in una struttura dati immutabile e organizzata, 
# calcolando metriche di base per ogni asset.

# SPECIFICHE INPUT
# I dati in ingresso sono forniti come una singola stringa multi-linea. 
# Ogni riga rappresenta una transazione con questo formato: 
# "DATA | TICKER | TIPO | QUANTITÀ | PREZZO_UNITARIO"
# Nota: La stringa contiene spazi extra, ticker con maiuscole/minuscole 
# inconsistenti e potenziali righe malformate.

# REQUISITI FUNZIONALI
# Elabora la stringa riga per riga. Ignora le righe vuote o che non contengono esattamente 5 campi.
# I Ticker devono essere sempre salvati in maiuscolo e senza spazi.
# Ogni transazione valida deve essere memorizzata come una Tupla composta da: (Ticker, Tipo, Quantità, Prezzo).
# Escludi dalla fase di calcolo le transazioni che presentano una quantità o un prezzo pari o inferiore a zero.
# Crea un report finale sotto forma di Dizionario. Le chiavi saranno i Ticker. I valori saranno a loro volta dizionari contenenti:
#   - 'totale_investito': La somma (Quantità * Prezzo) per tutte le operazioni 'BUY' di quel ticker.
#   - 'numero_operazioni': Il conteggio totale di transazioni (BUY e SELL) registrate per quel ticker.
# Calcola il valore totale complessivo investito nel portafoglio (solo operazioni 'BUY').

# VINCOLI TECNICI
# Utilizzo obbligatorio della funzione nativa tuple() per la conversione dei dati estratti.
# Utilizzo obbligatorio di un ciclo for per l'iterazione.
# Gestione della logica di aggregazione tramite dizionari.
# Hidden Gem: Per gestire i decimali nei report finali, dovrai consultare la documentazione 
# per utilizzare una funzione nativa che permetta di limitare la precisione numerica a due cifre decimali
#  (arrotondamento), garantendo la leggibilità finanziaria. 
# Inoltre, dovrai trovare un metodo delle stringhe per rimuovere correttamente gli spazi bianchi all'inizio 
# e alla fine di ogni segmento di testo separato.

# Dati di Test
raw_data = """
2024-01-10 | aapl | BUY | 10 | 150.25
2024-01-11 | TSLA | BUY | 5 | 240.00
2024-01-12 | aapl | SELL | 2 | 155.00
2024-01-13 |  msft  | BUY | 12 | 390.10
2024-01-14 | TSLA | BUY | 0 | 250.00
2024-01-15 | AAPL | BUY | 5 | 148.50

2024-01-16 | BTC | BUY | 1 | 42000.00
2024-01-17 | | ERROR | | 
2024-01-18 | MSFT | BUY | 8 | 405.00
"""

# Output Atteso
# --- REPORT PORTAFOGLIO ---
# AAPL: {'totale_investito': 2245.0, 'numero_operazioni': 3}
# TSLA: {'totale_investito': 1200.0, 'numero_operazioni': 1}
# MSFT: {'totale_investito': 7921.2, 'numero_operazioni': 2}
# BTC: {'totale_investito': 42000.0, 'numero_operazioni': 1}
# --------------------------
# VALORE TOTALE INVESTITO: 53366.2

lines = raw_data.splitlines()

for line in lines:
    print(line)