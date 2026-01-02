# Pulisco liste e filtro segnali vuoti

segnali_grezzi = [
    " 2042 | ZONA_A | RAD | 45.2 ",       # Valido (Pari, Radiazioni)
    " 3311 | ZONA_B | BIO | 12.0 ",       # Corrotto (Dispari)
    " ",                                  # Da ignorare (Vuoto)
    " 1008 | ZONA_C | TEC | 8.5 ",        # Valido (Pari, Tecnico)
    " ERROR | ZONA_X | ??? | 0.0 ",       # Corrotto (ID non numerico)
    " 4096 | ZONA_D | BIO | 95.5 ",       # Valido (Pari, Biologico)
    "    ",                               # Da ignorare (Solo spazi)
    " 6000 | ZONA_E | UNK | 10.0 "        # Valido (Pari, Sconosciuto)
]

elementi_segnale = []   # Segnale pulito in formato lista
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

print(segnali_filtrati)