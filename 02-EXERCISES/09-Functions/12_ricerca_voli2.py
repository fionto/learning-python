# =====================================================================
# Esercizio Finale: Motore di Ricerca Voli (Filtro Dinamico)
# =====================================================================
#
# Scrivi una funzione 'cerca_voli' che accetti:
# 1. destinazione (str): Argomento posizionale obbligatorio.
# 2. *compagnie (str): Un numero variabile di compagnie aeree preferite 
#    dall'utente (es: "Ryanair", "ITA", "Lufthansa").
# 3. **filtri (kwargs): Filtri opzionali per la ricerca.
#
# All'interno della funzione, crea una lista di dizionari (i "voli_disponibili").
# Ogni volo deve avere: 'destinazione', 'compagnia', 'prezzo', 'scali' (bool).
# Esempio: {"destinazione": "Parigi", "compagnia": "ITA", "prezzo": 120, "scali": False}
#
# Logica richiesta:
# - Se l'utente ha indicato delle compagnie in *args, la funzione deve 
#   tenere solo i voli di quelle compagnie. Se *args è vuoto, tienili tutti.
#
# - Se nei **filtri c'è 'prezzo_max', scarta i voli che costano di più.
#
# - Se nei **filtri c'è 'solo_diretti' ed è True, scarta i voli con scali.
#
# - Se la destinazione del volo non coincide con quella passata come 
#   primo argomento, scartalo sempre.
#
# La funzione deve restituire la lista dei voli che hanno superato 
# tutti i controlli.
# =====================================================================

def cerca_voli(destinazione: str, *compagnie: str, **filtri):
    voli_database = [
        {"destinazione": "Londra", "compagnia": "Ryanair", "prezzo": 45, "scali": False},
        {"destinazione": "Londra", "compagnia": "British Airways", "prezzo": 150, "scali": False},
        {"destinazione": "Parigi", "compagnia": "Air France", "prezzo": 200, "scali": False},
        {"destinazione": "Londra", "compagnia": "Lufthansa", "prezzo": 90, "scali": True},
    ]
    
    compagnie_preferite = [c.title() for c in compagnie]
    voli_filtrati = []

    for volo in voli_database:
        # 1. Filtro Destinazione (come prima)
        if volo['destinazione'].title() != destinazione.title():
            continue

        # Passo ad una logica early-exit invece di creare variabili 
        # booleane e poi fare un if finale lunghissimo.
        # Continuo a cercare tutti i requisiti per cui scartare.
        # 2. Filtro Compagnie (*args)
        if compagnie_preferite and volo['compagnia'].title() not in compagnie_preferite:
            continue

        # 3. Filtro Prezzo (**kwargs)
        # Usiamo un valore di default infinito se prezzo_max non è specificato
        if volo['prezzo'] > filtri.get('prezzo_max', float('inf')):
            continue

        # 4. Filtro Scali (**kwargs)
        if filtri.get('solo_diretti', False) and volo['scali']:
            continue

        # Se è arrivato qui, il volo ha passato tutti i controlli!
        voli_filtrati.append(volo)
        
    return voli_filtrati

risultato = cerca_voli("Londra", prezzo_max=100, solo_diretti=False)
print(risultato) 