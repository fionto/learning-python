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
    numero_articoli = len(prezzi)
    subtotale = sum(prezzi)
    
    if 'spedizione_express' in opzioni:
        spedizione = 5.00 if opzioni['spedizione_express'] else 0.00
    else:
        spedizione = 0.00

    if 'sconto_percentuale' in opzioni:
        totale_finale = subtotale * ((100 - float(opzioni['sconto_percentuale'])) / 100) + spedizione
    else:
        totale_finale = subtotale + spedizione

    ricevuta = {
        'id_cliente' : id_cliente,
        'numero_articoli' : numero_articoli,
        'subtotale' : subtotale,
        'totale_finale' : totale_finale,
        'opzioni_extra' : opzioni,
    }

    return ricevuta

# =====================================================================
# TEST DA ESEGUIRE
# =====================================================================

# Test 1: Ordine normale, senza opzioni extra
print("--- TEST 1 ---")
risultato_1 = crea_ricevuta("CLI-001", 10.0, 20.0, 5.0)
print(risultato_1)
# Output atteso: 
# subtotale: 35.0, totale_finale: 35.0, opzioni_extra: {}

# Test 2: Ordine con solo sconto
print("\n--- TEST 2 ---")
risultato_2 = crea_ricevuta("CLI-002", 50.0, 50.0, sconto_percentuale=20)
print(risultato_2)
# Output atteso: 
# subtotale: 100.0, totale_finale: 80.0, opzioni_extra: {'sconto_percentuale': 20}


# Test 3: L'esempio completo con sconto, spedizione e un'opzione extra
print("\n--- TEST 3 ---")
risultato_3 = crea_ricevuta("CLI-003", 15.50, 24.00, 10.50, 
                            sconto_percentuale=10, 
                            spedizione_express=True, 
                            pacco_regalo=True)
print(risultato_3)
# Output atteso:
# subtotale: 50.0 (15.50+24.00+10.50)
# totale_finale: 50.0 (50.0 - 10% di sconto = 45.0. Poi + 5.0 di spedizione = 50.0)
# opzioni_extra: {'sconto_percentuale': 10, 'spedizione_express': True, 'pacco_regalo': True}


# Test 4: Nessun articolo acquistato, ma chiede la spedizione express
print("\n--- TEST 4 ---")
risultato_4 = crea_ricevuta("CLI-004", spedizione_express=True)
print(risultato_4)
# Output atteso:
# numero_articoli: 0, subtotale: 0, totale_finale: 5.0, opzioni_extra: {'spedizione_express': True}