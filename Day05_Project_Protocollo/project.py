def main():

    # Segnali grezzi in ingresso
    segnali_spaziali: list[str] = [
    " 2042 | ZONA_A | RAD | 45.2 ",       # Valido (Pari, Radiazioni)
    " 3311 | ZONA_B | BIO | 12.0 ",       # Corrotto (Dispari)
    " ",                                  # Da ignorare (Vuoto)
    " 1008 | ZONA_C | TEC | 8.5 ",        # Valido (Pari, Tecnico)
    " ERROR | ZONA_X | ??? | 0.0 ",       # Corrotto (ID non numerico)
    " 4096 | ZONA_D | BIO | 95.5 ",       # Valido (Pari, Biologico)
    "    ",                               # Da ignorare (Solo spazi)
    " 6000 | ZONA_E | UNK | 10.0 "        # Valido (Pari, Sconosciuto)
    ]

    # Lista di liste in input
    segnali_preprocessati = pulisci_segnali(segnali_spaziali)

    # Gestione minacce 
    MINACCE_CRITICHE = {"Rischio Biologico", "Radiazioni"}
    rischio_grave = False

    # Statistiche sui segnali
    segnali_totali = len(segnali_preprocessati)
    segnali_corrotti = 0
    segnali_validi = 0
    
    # Intensità totale dei pericoli
    intensita_totale = 0
    
    # Scorro i segnali da processare
    for componenti_segnale in segnali_preprocessati:
        
        # Check alfanumerico
        is_invalid_format = not componenti_segnale[0].isdigit()
        
        # Scarto i segnali corrotti
        if is_invalid_format:
            segnali_corrotti += 1
            continue
        
        # Check parità
        id_int = int(componenti_segnale[0]) 
        is_not_valid_id = id_int % 2 != 0

        if is_not_valid_id:
            segnali_corrotti += 1
            continue
        
        # Sto processando un segnale valido
        segnali_validi += 1

        # Calcolo livello minaccia
        intensita_minaccia = float(componenti_segnale[3])
        intensita_totale += intensita_minaccia
        
        # Flag minaccia critica
        if match_minaccia(componenti_segnale) in MINACCE_CRITICHE:
            rischio_grave = True

    # Processo decisionale stato Allerta
    if intensita_totale > 200 or segnali_corrotti > segnali_validi:
        stato_allerta = "Critico"
    elif 100 <= intensita_totale <= 200 and rischio_grave:
        stato_allerta = "Alto"
    else:
        stato_allerta = "Basso"

    dizionario_report = {
        "Segnali Totali": segnali_totali,
        "Segnali Validi": segnali_validi,
        "Segnali Corrotti": segnali_corrotti,
        "Intensita Totale": intensita_totale,
        "Stato Allerta": stato_allerta,
    }

    print("Analisi Terminata. Generazione Report...")
    print("----------------------------------------")
    print("REPORT SICUREZZA BASE ALPHA")
    print("----------------------------------------")
    print(f" Segnali rilevati: {segnali_totali}")
    print(f" \t-Validi: {segnali_validi}")
    print(f" \t-Corrotti: {segnali_corrotti}\n")
    print(f"Intensità Totale Rilevata: {intensita_totale}")
    print(f"Stato allerta calcolato: {stato_allerta}\n")
    print(f"Dettaglio dizionario: {dizionario_report}")


def pulisci_segnali(segnali_grezzi: list[str]):
    segnali_filtrati = []   # Lista filtrata dei segnali puliti in formato lista

    for segnale_str in segnali_grezzi:
        # Pulisco spazi ai margini della stringa
        segnale_str = segnale_str.strip()

        stringa_vuota = not segnale_str
    
        # Lavoro solo su segnali non-vuoti
        if stringa_vuota:                                 
            continue

        elementi_segnale = segnale_str.split('|')
        
        # Pulisco da spazi elementi dei singoli segnali usando enumerate()
        for i, elemento in enumerate(elementi_segnale):
            elementi_segnale[i] = elemento.strip()

        # Creo lista di liste    
        segnali_filtrati.append(elementi_segnale)
    
    return segnali_filtrati


def match_minaccia(segnale_da_analizzare: list):

    # Estraggo rischio
    codice_rischio = segnale_da_analizzare[2]

    match codice_rischio:
        case "RAD":
            descrizione_rischio = "Radiazioni"
        case "BIO":
            descrizione_rischio = "Rischio Biologico"
        case "TEC":
            descrizione_rischio = "Guasto Tecnico"
        case _:
            descrizione_rischio = "Sconosciuto"
    
    return descrizione_rischio

main()