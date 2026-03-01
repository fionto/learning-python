# =====================================================================
# Esercizio: Simulatore di Investimento Avanzato
# =====================================================================
#
# Scrivi una funzione 'analizza_investimento' che valuti il rendimento 
# di un portafoglio considerando costi variabili e tasse.
#
# La funzione deve accettare:
# 1. capitale_iniziale (float): La somma versata all'inizio.
# 2. *rendimenti (float): Una serie di percentuali di rendimento annuo 
#    (es: 0.05 per il 5%, -0.02 per il -2%). Ogni argomento è un anno.
# 3. **parametri (kwargs): Opzioni aggiuntive per la simulazione.
#
# Logica richiesta:
# - Calcola il capitale finale applicando i rendimenti anno dopo anno 
#   (capitalizzazione composta: cap = cap * (1 + rendimento)).
#
# - Se tra i kwargs esiste 'commissione_annua' (float), sottrai 
#   quella percentuale dal capitale alla fine di OGNI anno.
#
# - Se tra i kwargs esiste 'tassa_plusvalenza' (float), applicala 
#   SOLO ALLA FINE e SOLO sul guadagno netto (Capitale Finale - Iniziale).
#   Esempio: se guadagni 100€ e la tassa è 0.26, sottrai 26€.
#
# - Se tra i kwargs esiste 'inflazione_media' (float), calcola un 
#   secondo valore chiamato "potere_acquisto" che svaluta il capitale 
#   finale (capitale_finale / (1 + inflazione_media)^numero_anni).
#
# La funzione deve restituire un dizionario con:
# {
#     "capitale_nominale": ...,  # Arrotondato a 2 decimali
#     "guadagno_netto": ...,      # Capitale finale - iniziale (post tasse)
#     "potere_acquisto": ...,    # Se calcolato, altrimenti None
#     "dettagli_simulazione": ... # Il dizionario kwargs originale
# }
# =====================================================================

def analizza_investimento(capitale_iniziale: float, *rendimenti: float, **parametri):
    capitale_attuale = capitale_iniziale
    comm_percentuale = parametri.get('commissione_annua', 0)

    for r in rendimenti:
        capitale_attuale *= (1 + r)
        capitale_attuale *= (1 - comm_percentuale)
    
    guadagno_lordo = capitale_attuale - capitale_iniziale
    
    # Tasse (solo se c'è guadagno)
    aliquota = parametri.get('tassa_plusvalenza', 0)
    tasse = (guadagno_lordo * aliquota) if guadagno_lordo > 0 else 0
    
    capitale_netto = capitale_attuale - tasse

    # Gestione potere d'acquisto (con ritorno None se manca inflazione)
    inflazione = parametri.get('inflazione_media')
    potere_acquisto = None
    if inflazione is not None:
        potere_acquisto = round(capitale_netto / ((1 + inflazione) ** len(rendimenti)), 2)

    return {
        'capitale_nominale': round(capitale_netto, 2),
        'guadagno_netto': round(guadagno_lordo - tasse, 2),
        'potere_acquisto': potere_acquisto,
        'dettagli_simulazione': parametri,
    }

# Test 2: Rendimenti con commissioni e tasse (Modello Italiano)
# Spiegazione: Ogni anno togli l'1% di commissione, alla fine togli il 26% sul profitto.
print(analizza_investimento(5000, 0.05, 0.08, -0.02, 0.12, commissione_annua=0.01, tassa_plusvalenza=0.26))