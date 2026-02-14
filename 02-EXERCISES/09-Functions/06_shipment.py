# ESERCIZIO:
# Scrivi una funzione chiamata calcola_spedizione() che calcoli il costo totale
# di una spedizione in base ad alcune informazioni fornite.
#
# La funzione deve accettare i seguenti parametri:
# - peso_kg (obbligatorio): peso del pacco in chilogrammi
# - destinazione (obbligatorio): paese di destinazione
# - assicurazione (opzionale): indica se la spedizione è assicurata
#   (valore di default: False)
# - spedizione_rapida (opzionale): indica se la spedizione è rapida
#   (valore di default: False)
#
# Regole per il calcolo del costo:
# - Il costo base della spedizione è 5 €
# - Ogni chilogrammo costa 2 €
# - Se la destinazione NON è "Italia", aggiungi 10 €
# - Se assicurazione è True, aggiungi 5 €
# - Se spedizione_rapida è True, aggiungi 8 €
#
# La funzione deve calcolare il costo totale e stampare un messaggio
# riassuntivo, ad esempio:
#
# Spedizione verso Francia (3 kg):
# - Assicurazione: sì
# - Spedizione rapida: no
# Costo totale: 29 €
#
# Esempi di chiamata:
# calcola_spedizione(2, "Italia")
# calcola_spedizione(2, "Germania", assicurazione=True, spedizione_rapida=True)

# Costanti per il calcolo prezzi
COSTO_BASE = 5
COSTO_KG = 2

def calcola_spedizione(peso_kg: float, destinazione: str, assicurazione: bool = False, spedizione_rapida: bool = False) -> float:
    """
    Calcola il costo della spedizione in base ai parametri forniti.

    Questa funzione determina il costo totale della spedizione aggiungendo
    al costo base i supplementi per il peso, la destinazione, l'assicurazione
    e il servizio di spedizione rapida. Stampa inoltre un riepilogo dei dettagli.

    Args:
        peso_kg: Peso della spedizione in chilogrammi.
        destinazione: Paese o regione di destinazione della spedizione.
        assicurazione: Se True, aggiunge il costo dell'assicurazione.
            Defaults to False.
        spedizione_rapida: Se True, aggiunge il costo della spedizione rapida.
            Defaults to False.

    Returns:
        Il costo totale della spedizione in euro (float).

    Example:
        >>> costo = calcola_spedizione(5.0, "Italia", assicurazione=True)
        >>> print(costo)
    """
    destinazione = destinazione.strip().lower()
    surplus_estero = 10 if destinazione != "italia" else 0
    surplus_assicurazione = 5 if assicurazione else 0
    surplus_rapida = 8 if spedizione_rapida else 0

    costo_totale = COSTO_BASE + COSTO_KG * peso_kg + surplus_estero + surplus_assicurazione + surplus_rapida

    print(f"Spedizione verso {destinazione.title()} ({peso_kg} kg)")
    print(f"\t- Assicurazione: {'Sì' if assicurazione else 'No'}")
    print(f"\t- Spedizione rapida: {'Sì' if spedizione_rapida else 'No'}")
    print(f"Costo totale: {costo_totale} €")

    return costo_totale

costo_totale = calcola_spedizione(4, "Germania", assicurazione=True)