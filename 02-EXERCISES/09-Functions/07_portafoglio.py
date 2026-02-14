# ESERCIZIO:
# Scrivi una funzione chiamata calcola_valore_portafoglio() che calcoli
# il valore totale di un portafoglio finanziario.
#
# La funzione deve accettare un numero arbitrario di argomenti tramite *args.
# Ogni argomento rappresenta un investimento ed è una tupla nella forma:
# (nome_asset, quantita, prezzo_unitario)
#
# Esempio di investimento:
# ("AAPL", 10, 185.5)
#
# La funzione deve:
# - calcolare il valore di ogni singolo investimento (quantita × prezzo_unitario)
# - stampare un riepilogo leggibile del portafoglio
# - sommare i valori di tutti gli investimenti
# - restituire il valore totale del portafoglio come float
#
# Esempio di output:
#
# Portafoglio:
# - AAPL: 10 × 185.5 € = 1855.00 €
# - MSFT: 5 × 310.0 € = 1550.00 €
# - BTP: 20 × 98.7 € = 1974.00 €
#
# Valore totale del portafoglio: 5379.00 €
#
# Firma della funzione (obbligatoria):
# def calcola_valore_portafoglio(*investimenti) -> float:
#
# Esempi di chiamata:
#
# totale = calcola_valore_portafoglio(
#     ("AAPL", 10, 185.5),
#     ("MSFT", 5, 310.0),
#     ("BTP", 20, 98.7),
# )
#
# Oppure:
# azione = ("ENI", 100, 14.2)
# obbligazione = ("BTP", 50, 97.8)
# calcola_valore_portafoglio(azione, obbligazione)
#
# Suggerimenti:
# - usa un ciclo for per iterare sugli investimenti
# - gestisci correttamente il caso di portafoglio vuoto
# - formatta i valori monetari con due cifre decimali

def calcola_valore_portafoglio(*investimenti) -> float:
    
    valore_portafoglio = 0.0
    
    print("Portafoglio:")
    
    for nome_asset, quantita, prezzo_unitario in investimenti:
        valore_investimento = quantita * prezzo_unitario
        valore_portafoglio += valore_investimento
        print(f"- {nome_asset}: {quantita} x {prezzo_unitario:.2f} € = {valore_investimento:.2f} €")
    
    print(f"Valore totale del portafoglio: {valore_portafoglio:.2f} €")

    return valore_portafoglio

totale = calcola_valore_portafoglio(
    ("AAPL", 10, 185.5),
    ("MSFT", 5, 310.0),
    ("BTP", 20, 98.7),
)

azione = ("ENI", 100, 14.2)
obbligazione = ("BTP", 50, 97.8)
calcola_valore_portafoglio(azione, obbligazione)