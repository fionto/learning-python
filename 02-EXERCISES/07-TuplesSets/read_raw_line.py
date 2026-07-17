line = '2024-01-10 | aapl | BUY | 10 | 150.25'
line_2 = '2024-01-17 | | ERROR | | '

def elaborate_raw_line(line: str) -> tuple:
    
    if not line.strip():
        raise ValueError(f"Line is empty.")

    elements = line.split('|')
    if len(elements) != 5:
        raise ValueError(f"Inconsistent number of elements: expected 5")
    
    elements = elements[1:]

    clean_elements = []

    for element in elements:

        element = element.strip().upper()

        if not element:
            raise ValueError(f"Malformed line. Value missing.")
        
        clean_elements.append(element)

    return tuple(clean_elements)


def elabora_riga_grezza(riga: str) -> tuple:
    """
    Riceve una riga nel formato:
    DATA | TITOLO | OPERAZIONE | QUANTITA | PREZZO

    Restituisce una tupla contenente:
    (titolo, operazione, quantita, prezzo)

    La data viene ignorata.
    """

    # Verifica che la riga non sia vuota
    if not riga.strip():
        raise ValueError("La riga è vuota.")

    try:
        # Divide la riga nei campi, rimuove gli spazi
        # e converte tutto in maiuscolo
        _, titolo, operazione, quantita, prezzo = (
            campo.strip().upper()
            for campo in riga.split("|")
        )

    except ValueError:
        # L'unpacking fallisce se i campi non sono esattamente 5
        raise ValueError(
            "Numero di campi non valido: attesi 5 campi separati da '|'."
        )

    risultato = (titolo, operazione, quantita, prezzo)

    # Verifica che nessun campo richiesto sia vuoto
    if any(not campo for campo in risultato):
        raise ValueError(
            "Riga malformata: uno o più valori obbligatori sono mancanti."
        )

    return risultato

result = elabora_riga_grezza(line_2)

print(result)