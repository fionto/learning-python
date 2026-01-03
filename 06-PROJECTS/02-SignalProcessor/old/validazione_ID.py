# Elaborazione validazione ID

# Lista di liste in input
segnali_preprocessed = [
    ['2042', 'ZONA_A', 'RAD', '45.2'],
    ['3311', 'ZONA_B', 'BIO', '12.0'],
    ['1008', 'ZONA_C', 'TEC', '8.5'],
    ['ERROR', 'ZONA_X', '???', '0.0'],
    ['4096', 'ZONA_D', 'BIO', '95.5'],
    ['6000', 'ZONA_E', 'UNK', '10.0'],
    ]

# Creo lista che contiene i dizionari
segnali_processati = []

# Scorro i segnali da processare
for componenti_segnale in segnali_preprocessed:
    
    # Check alfanumerico
    is_invalid_format = not componenti_segnale[0].isdigit()
    
    # Scarto i segnali corrotti
    if is_invalid_format:
       continue
    
    # Check parità
    id_int = int(componenti_segnale[0]) 
    is_not_valid_id = id_int % 2 != 0

    if is_not_valid_id:
        continue

    # Creo oggetto dizionario ad ogni ciclo
    dizionario = {
        "id": id_int,
        "zona": componenti_segnale[1],
        "rischio": componenti_segnale[2],
        "intensita": float(componenti_segnale[3]),
    }

    segnali_processati.append(dizionario)

print(segnali_processati)