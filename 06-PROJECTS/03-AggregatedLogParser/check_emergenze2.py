def check_emergenza(valore, valutazione):
    v = int(valore)

    # primo filtro: valori fuori range o priorità sconosciute.
    # Decido di dare "EMERGENZA" perché malfunzionamento
    if v not in range(0, 101) or valutazione not in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        return "EMERGENZA"

    match (v, valutazione):
        # EMERGENZE
        case (_, "CRITICAL"):
            return "EMERGENZA"
        case (v, _) if v < 60:
            return "EMERGENZA"
        # ATTENZIONI
        case (_, "HIGH"):
            return "ATTENZIONE"
        case (v, _) if v <= 79:
            return "ATTENZIONE"
        #NORMALI
        case (_, "LOW") | (_, "MEDIUM"):
            return "NORMALE" 