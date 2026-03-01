# =====================================================================
# Esercizio: Generatore di Ricevute E-commerce
# =====================================================================
#
# Scrivi una funzione chiamata 'crea_ricevuta' che calcoli il totale 
# di un ordine e restituisca un dizionario con i dettagli della ricevuta.
#
# La funzione crea_ricevuta() deve accettare i seguenti parametri:
# 1. Un argomento posizionale obbligatorio: 'id_cliente' (stringa).
# 2. Un numero arbitrario di argomenti posizionali (*args): i prezzi 
#    dei singoli articoli acquistati (float o int).
# 3. Un numero arbitrario di argomenti nominati (**kwargs): le opzioni 
#    extra dell'ordine.
#
# Logica di calcolo:
# - Calcola il 'subtotale' sommando tutti i prezzi passati in *args.
# - Controlla se nei **kwargs è presente la chiave 'sconto_percentuale'. 
#   Se c'è, sottrai quella percentuale dal subtotale.
# - Controlla se nei **kwargs è presente la chiave 'spedizione_express'. 
#   Se è True, aggiungi 5.00 al costo totale (dopo aver applicato lo sconto).
#
# La funzione deve restituire un dizionario strutturato in questo modo:
# {
#     "id_cliente": ...,
#     "numero_articoli": ..., # Quanti prezzi sono stati passati
#     "subtotale": ...,       # Somma dei prezzi base
#     "totale_finale": ...,   # Totale dopo sconti e spedizione
#     "opzioni_extra": ...    # Dizionario con tutti i **kwargs passati
# }
#
# Esempio di utilizzo previsto:
# ricevuta = crea_ricevuta("CLI-987", 15.50, 24.00, 10.50, 
#                          sconto_percentuale=10, 
#                          spedizione_express=True, 
#                          pacco_regalo=True)
#
# print(ricevuta)
# =====================================================================

def crea_ricevuta(id_cliente: str, *prezzi: float, **opzioni):
    subtotale = sum(prezzi)
    
    # Se 'sconto_percentuale' non c'è, restituisce 0
    sconto = opzioni.get('sconto_percentuale', 0) 
    
    # Se 'spedizione_express' non c'è, restituisce False
    spedizione = 5.00 if opzioni.get('spedizione_express', False) else 0.00
    
    # Calcolo compatto
    totale_scontato = subtotale * ((100 - sconto) / 100)
    totale_finale = totale_scontato + spedizione

    return {
        'id_cliente': id_cliente,
        'numero_articoli': len(prezzi),
        'subtotale': subtotale,
        'totale_finale': totale_finale,
        'opzioni_extra': opzioni,
    }