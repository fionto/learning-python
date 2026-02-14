# =============================================================================
# ESERCIZIO: PROTOCOLLO DI CRITTOGRAFIA "BIT-SHIFTER V2"
# 
# DESCRIZIONE DEL PROBLEMA:
# Sviluppare un sistema di cifratura simmetrica semplificato che elabora messaggi 
# segreti basandosi sulla posizione dei caratteri e su chiavi bitwise.
# Il sistema deve trasformare ogni carattere in base alla sua categoria (Vocale, 
# Consonante, Altro) e applicare una rotazione di bit specifica.
#
# STRUTTURA DATI INPUT:
# - Una stringa di testo 'RAW_MESSAGE'.
# - Un intero 'MASTER_KEY' (usato per operazioni XOR).
# - Un intero 'SHIFT_AMOUNT' (usato per spostamenti di bit).
#
# RICHIESTE NUMERICHE:
# 1. Convertire ogni carattere nel suo valore Unicode (ASCII).
# 2. Se il carattere è una VOCALE: Eseguire uno shift a SINISTRA di 'SHIFT_AMOUNT'.
# 3. Se il carattere è una CONSONANTE: Eseguire uno shift a DESTRA di 'SHIFT_AMOUNT'.
# 4. Se il carattere è ALTRO (spazi, simboli): Eseguire XOR con 'MASTER_KEY'.
# 5. Calcolare la somma totale dei nuovi valori binari ottenuti.
#
# VINCOLI TECNICI OBBLIGATORI:
# - Implementare almeno 2 funzioni helper per i calcoli bitwise e la logica di analisi.
# - Utilizzare 'match/case' per distinguere tra Vocali, Consonanti e Altro.
# - Utilizzare 'match/case' per gestire almeno 2 diversi scenari di MASTER_KEY 
#   (es. se la chiave è pari o dispari).
# - Aggregare i risultati in un dizionario annidato seguendo questa struttura:
#   { 'stats': {'total_sum': int}, 'data': {'original': str, 'encoded_values': list} }
# - Vietato l'uso di try/except.
# - I dati originali non devono essere sovrascritti: crea nuove strutture dati.
#
# STRUTTURA OUTPUT ATTESO:
# Un unico dizionario contenente la somma dei valori trasformati e la lista 
# dei singoli interi risultanti dalla manipolazione bitwise.
# =============================================================================

# --- DATI DI INPUT ---
RAW_MESSAGE = "Python 3.12!"
MASTER_KEY = 42
SHIFT_AMOUNT = 2

# --- OUTPUT ATTESO (Approssimativo) ---
# Il risultato finale dovrebbe essere simile a:
# {
#   'stats': {'total_sum': 1254}, 
#   'data': {
#       'original': 'Python 3.12!', 
#       'encoded_values': [20, 484, 464, 26, 444, 28, 74, 10, 75, 72, 86]
#    }
# }
# Nota: I valori numerici sopra sono puramente indicativi del formato.

# --- SVOLGIMENTO UTENTE ---

def alterate_key(key: int) -> int:
    """Modifica la chiave master basandosi sulla sua parità.

    Args:
        key: Il valore intero della chiave originale.

    Returns:
        La chiave invariata se pari, incrementata di 1 se dispari.
    """
    match (key % 2): 
        case 0:
            return key
        case _: # Copre l'1 e qualsiasi altro valore teorico, elimina warning VSCode
            return (key + 1)

def encrypt_character(character: str, shift_amount: int, master_key: int) -> int:
    """Applica trasformazioni bitwise a un carattere in base alla sua categoria.

    La funzione utilizza match/case per smistare i caratteri. Nota: lo shift
    a destra è un'operazione distruttiva che causa perdita di dati.

    Args:
        character: Il singolo carattere da cifrare.
        shift_amount: Numero di posizioni per gli shift bitwise.
        master_key: Chiave numerica per l'operazione XOR.

    Returns:
        L'intero risultante dalla trasformazione bitwise.
    """
    match character.upper():
        case "A" | "E" | "I" | "O" | "U":
            # Shift a sinistra: moltiplica il valore Unicode (operazione reversibile)
            return ord(character) << shift_amount
        case (
            "B" | "C" | "D" | "F" | "G" | "H" | "J" | "K" | "L" |
            "M" | "N" | "P" | "Q" | "R" | "S" | "T" | "V" |
            "W" | "X" | "Y" | "Z"
        ):
            # --- NOTA TECNICA: OPERAZIONE DISTRUTTIVA ---
            # Lo shift a destra (>>) rimuove i bit meno significativi.
            # Esempio: 'B' (66) è 1000010. Con shift 2 diventa 0010000 (16).
            # I bit finali '10' vengono eliminati. Non è possibile ricostruire
            # il carattere originale partendo solo dal risultato.
            return ord(character) >> shift_amount    
        case _:
            # XOR: operazione bitwise logica (reversibile applicando nuovamente lo XOR)
            return ord(character) ^ alterate_key(master_key)

def main():
    """Esegue il ciclo di cifratura e aggrega i dati in un report strutturato."""
    
    # Inizializzazione del dizionario di riepilogo (Data Aggregation)
    recap = {
        'stats': {'total_sum': 0},
        'data': {'original': RAW_MESSAGE, 'encoded_values': []},
    }

    for char in RAW_MESSAGE:
        # Calcolo del valore cifrato tramite helper function
        encrypted_char = encrypt_character(char, SHIFT_AMOUNT, MASTER_KEY)
        
        # Aggiornamento dei dati nel dizionario annidato
        recap['stats']['total_sum'] += encrypted_char
        recap['data']['encoded_values'].append(encrypted_char)

    print(recap)

if __name__ == "__main__":
    main()