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


def test_check_emergenza():
    # Struttura: (valore, valutazione, risultato_atteso, descrizione)
    test_cases = [
        # --- Casi NORMALE ---
        (80, "LOW", "NORMALE", "Limite inferiore NORMALE (80, LOW)"),
        (100, "MEDIUM", "NORMALE", "Valore massimo con priorità media"),
        (85, "LOW", "NORMALE", "Valore alto, priorità bassa"),

        # --- Casi ATTENZIONE ---
        (79, "LOW", "ATTENZIONE", "Limite superiore ATTENZIONE (79)"),
        (60, "LOW", "ATTENZIONE", "Limite inferiore ATTENZIONE (60)"),
        (85, "HIGH", "ATTENZIONE", "Priorità HIGH scavalca STATO >= 80"),
        (65, "MEDIUM", "ATTENZIONE", "Valore nel range 60-79"),

        # --- Casi EMERGENZA (Regolari) ---
        (59, "LOW", "EMERGENZA", "Appena sotto il limite di attenzione (< 60)"),
        (0, "LOW", "EMERGENZA", "Valore minimo possibile"),
        (85, "CRITICAL", "EMERGENZA", "CRITICAL scavalca STATO alto"),
        (20, "CRITICAL", "EMERGENZA", "Entrambe le condizioni critiche"),

        # --- Casi EMERGENZA (Errori/Input sporchi) ---
        (101, "LOW", "EMERGENZA", "Fuori range massimo (> 100)"),
        (-1, "LOW", "EMERGENZA", "Fuori range minimo (< 0)"),
        (80, "SCONOSCIUTA", "EMERGENZA", "Priorità non valida"),

    ]

    print(f"{'DESCRIZIONE':<40} | {'INPUT':<15} | {'ATTESO':<12} | {'RISULTATO'}")
    print("-" * 85)

    for valore, valutazione, atteso, desc in test_cases:
        risultato = check_emergenza(valore, valutazione)
        status = "✅" if risultato == atteso else "❌"
        
        input_str = f"{valore}, {valutazione}"
        print(f"{desc:<40} | {input_str:<15} | {atteso:<12} | {status} ({risultato})")

# Esegui i test
if __name__ == "__main__":
    test_check_emergenza()