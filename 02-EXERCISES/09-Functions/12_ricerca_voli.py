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

def cerca_voli (destinazione: str, *compagnie: str, **filtri):

    voli_database = [
    {"destinazione": "Londra", "compagnia": "Ryanair", "prezzo": 45, "scali": False},
    {"destinazione": "Londra", "compagnia": "British Airways", "prezzo": 150, "scali": False},
    {"destinazione": "Parigi", "compagnia": "Air France", "prezzo": 200, "scali": False},
    {"destinazione": "Londra", "compagnia": "Lufthansa", "prezzo": 90, "scali": True},
    ]
    
    compagnie = [compagnia.title() for compagnia in compagnie]
    voli_disponibili = []

    for volo in voli_database:
        
        if destinazione.title() != volo['destinazione'].title():
            continue

        if compagnie:
            compagnia_filter = volo['compagnia'].title() in set(compagnie)
        else:
            compagnia_filter = True

        prezzo_filter = volo['prezzo'] < filtri.get('prezzo_max', float('inf'))
        solo_diretti = filtri.get('solo_diretti', False)

        # Se l'utente VUOLE solo diretti ed il volo HA scali, il filtro è False. Altrimenti True.
        if solo_diretti and volo['scali']:
            scali_filter = False
        else:
            scali_filter = True

        if compagnia_filter and prezzo_filter and scali_filter:
            voli_disponibili.append(volo)
        
    return voli_disponibili

risultato = cerca_voli("Londra", prezzo_max=100, solo_diretti=False)
print(risultato) 