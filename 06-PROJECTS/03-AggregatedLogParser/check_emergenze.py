def check_emergenza(valore, valutazione):
    v = int(valore)

    # primo filtro: valori fuori range o priorità sconosciute. 
    # Decido di dare "EMERGENZA" perché malfunzionamento
    if v > 100 or valutazione not in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        return "EMERGENZA"

    # classificazione principale
    if v < 60 or valutazione == "CRITICAL":
        return "EMERGENZA"
    if v <= 79 or valutazione == "HIGH":
        return "ATTENZIONE"
    return "NORMALE"