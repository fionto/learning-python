# ESERCIZIO: Analizzatore di Performance Personalizzabile
#
# Obiettivo:
# Implementare un sistema modulare che analizzi una serie di investimenti
# e permetta di applicare regole opzionali tramite **kwargs.
#
# Requisiti:
# - Separazione delle responsabilità
# - Ogni funzione deve avere un solo compito
# - Uso corretto e ragionato di **kwargs
# - Nessuna logica duplicata
# - Codice leggibile e modulare
#
# Note:
# Le opzioni opzionali devono essere completamente dinamiche e non obbligatorie.

investimenti_test = (
    ("AAPL", 10, 150.0, 185.5),
    ("MSFT", 5, 320.0, 300.0),
    ("TSLA", 3, 250.0, 310.0),
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

def valuta_investimento(investimento: tuple[str, int, float, float], **dettagli) -> tuple[float, float]:
    """
    Analizza un investimento calcolando il valore iniziale, quello attuale.

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
    """
    _, quantita, prezzo_acquisto, prezzo_attuale = investimento

    valore_iniziale = quantita * prezzo_acquisto
    valore_attuale = quantita * prezzo_attuale
    
    

    return valore_iniziale, valore_attuale