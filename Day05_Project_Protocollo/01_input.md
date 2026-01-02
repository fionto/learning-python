# Copia questa lista e incollala nel tuo main() come input di test

lista_segnali = [
    " 2042 | ZONA_A | RAD | 45.2 ",       # Valido (Pari, Radiazioni)
    " 3311 | ZONA_B | BIO | 12.0 ",       # Corrotto (Dispari)
    " ",                                  # Da ignorare (Vuoto)
    " 1008 | ZONA_C | TEC | 8.5 ",        # Valido (Pari, Tecnico)
    " ERROR | ZONA_X | ??? | 0.0 ",       # Corrotto (ID non numerico)
    " 4096 | ZONA_D | BIO | 95.5 ",       # Valido (Pari, Biologico)
    "    ",                               # Da ignorare (Solo spazi)
    " 6000 | ZONA_E | UNK | 10.0 "        # Valido (Pari, Sconosciuto)
]


        " 1000 | ZONA_C | TEC | 150.5 ",       # Valido
        " 2000 | ZONA_D | TEC | 60.0 ",        # Valido
        " 500  | ZONA_A | RAD | 5.0 ",         # Valido
        " 101  | ZONA_X | BIO | 10.0 "         # Corrotto (Dispari)


        " 8888 | ZONA_A | TEC | 10.0 ",        # Valido (1)
        " 9999 | ZONA_B | BIO | 50.0 ",        # Corrotto (Dispari - 1)
        " ABC  | ZONA_C | RAD | 20.0 ",        # Corrotto (Non numerico - 2)
        " 11   | ZONA_D | TEC | 5.0  "         # Corrotto (Dispari - 3)