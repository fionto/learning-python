#"RAD" -> "Radiazioni"
#"BIO" -> "Rischio Biologico"
#"TEC" -> "Guasto Tecnico"

# Lista di liste in input
segnali_preprocessati = [
    ['2042', 'ZONA_A', 'RAD', '45.2'],
    ['3311', 'ZONA_B', 'BIO', '12.0'],
    ['1008', 'ZONA_C', 'TEC', '8.5'],
    ['ERROR', 'ZONA_X', '???', '0.0'],
    ['4096', 'ZONA_D', 'BIO', '95.5'],
    ['6000', 'ZONA_E', 'UNK', '10.0'],
    ]

# Lista da analizzare
segnale = segnali_preprocessati[3]

# Estraggo rischio
codice_rischio = segnale[2]

match codice_rischio:
    case "RAD":
        descrizione_rischio = "Radiazioni"
    case "BIO":
        descrizione_rischio = "Rischio Biologico"
    case "TEC":
        descrizione_rischio = "Guasto Tecnico"
    case _:
        descrizione_rischio = "Sconosciuto"

print(descrizione_rischio)