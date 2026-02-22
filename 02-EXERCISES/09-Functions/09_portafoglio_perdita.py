# ESERCIZIO:
# Analisi delle performance di un insieme di investimenti usando *args.
#
# Devi costruire un piccolo sistema che analizzi un numero arbitrario
# di investimenti e determini se ciascuno è in profitto o in perdita.
#
# Ogni investimento è rappresentato da una tupla nella forma:
# (nome_asset, quantita, prezzo_acquisto, prezzo_attuale)
#
# Esempio:
# ("AAPL", 10, 150.0, 185.5)
#
# Dove:
# - nome_asset è una stringa
# - quantita è il numero di unità possedute
# - prezzo_acquisto è il prezzo unitario di acquisto
# - prezzo_attuale è il prezzo unitario corrente
#
# Il programma deve:
# - accettare un numero arbitrario di investimenti tramite *args
# - calcolare per ciascun investimento:
#     - valore iniziale (quantita × prezzo_acquisto)
#     - valore attuale (quantita × prezzo_attuale)
#     - profitto o perdita
# - determinare il profitto/perdita totale del portafoglio
# - stampare un riepilogo chiaro e formattato


investimenti_test_1 = (
    ("AAPL", 10, 150.0, 185.5),   # profitto
    ("MSFT", 5, 320.0, 300.0),   # perdita
    ("BTP", 20, 98.0, 101.7),    # profitto
)

investimenti_test_2 = (
    ("ENI", 100, 13.5, 14.2),
    ("STM", 50, 35.0, 38.5),
    ("ETF_S&P500", 15, 400.0, 420.0),
)

investimenti_test_3 = (
    ("TSLA", 8, 250.0, 220.0),
    ("AMZN", 3, 140.0, 120.0),
    ("BTC_ETF", 12, 60.0, 45.0),
)

investimenti_test_4 = (
    ("AAPL", 10, 150.0, 185.5),
    ("MSFT", 5, 320.0, 300.0),
    ("GOOGL", 7, 120.0, 140.0),
    ("TSLA", 3, 250.0, 230.0),
    ("BTP", 50, 97.0, 100.0),
    ("ETF_NASDAQ", 12, 300.0, 330.0),
)

def valuta_investimento(investimento: tuple[str, int, float, float]) -> tuple[float, float, bool]:
    """
    Analizza un investimento calcolando il valore iniziale, quello attuale e la redditività.

    La funzione riceve una tupla contenente i dettagli dell'investimento, estrae le quantità
    e i prezzi, ed esegue i calcoli finanziari di base.

    Args:
        investimento (tuple[str, int, float, float]): Una tupla contenente:
            - Nome/Ticker (str): Identificativo dell'asset (non utilizzato nel calcolo).
            - Quantità (int): Numero di unità possedute.
            - Prezzo acquisto (float): Prezzo medio di carico per unità.
            - Prezzo attuale (float): Prezzo di mercato corrente per unità.

    Returns:
        tuple[float, float, bool]: Una tupla contenente:
            - Valore iniziale (float): Capitale investito inizialmente (quantità * prezzo acquisto).
            - Valore attuale (float): Valore di mercato corrente (quantità * prezzo attuale).
            - È profittevole (bool): True se il valore attuale supera quello iniziale, False altrimenti.
    """
    _, quantita, prezzo_acquisto, prezzo_attuale = investimento

    valore_iniziale = quantita * prezzo_acquisto
    valore_attuale = quantita * prezzo_attuale
    
    # Se i valori sono uguali, restituisce False (nessun profitto netto/mia decisione)
    is_profittevole = valore_attuale > valore_iniziale

    return valore_iniziale, valore_attuale, is_profittevole


def valuta_portafoglio(*investimenti: tuple[str, int, float, float]) -> dict:
    """
    Genera un portafoglio di riepilogo sottoforma di dizionario ricevendo in
    ingresso un investimento
    """
    portafoglio = {}
        
    for investimento in investimenti:
        ticker = investimento[0]
        valore_iniziale, valore_finale, is_profittevole = valuta_investimento(investimento)
        
        # Ipotizzo che nella lista di investimenti non ci siano doppioni
        portafoglio[ticker] = {
            'profittevole': is_profittevole,
            'guadagno': valore_finale - valore_iniziale
        }

    return portafoglio

def stampa_portafoglio(portafoglio: dict):
    
    print("Analisi Portafoglio:")

    for k, v in portafoglio.items():
        print(f"{k.upper()}: {'Profitto' if v['profittevole'] else 'Perdita'} di {abs(v['guadagno']):.2f} €")

# --- CHIAMATA CORRETTA ---
# Usa l'asterisco (*) per espandere la tupla di tuple in argomenti singoli
stampa_portafoglio(valuta_portafoglio(*investimenti_test_4))



# Esempio di output:
#
# Analisi portafoglio:
# - AAPL: Profitto di 355.00 €
# - MSFT: Perdita di 120.00 €
# - BTP: Profitto di 74.00 €
#
# Profitto/Perdita totale: 309.00 €