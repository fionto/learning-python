# ==============================================================================
# PROGETTO: Bio-Informatic Data Parser v1.0
# DESCRIZIONE: Pulizia, analisi e validazione di dati scientifici grezzi.
#
# REGOLE E VINCOLI:
# 1. NO condizionali (if, else, elif)
# 2. NO cicli (for, while)
# 3. Organizzazione obbligatoria: funzione main() + funzioni di supporto
#
# SPECIFICHE TRASFORMAZIONE:
# - Input: "  id-9921: mArS_rOvEr-pRoToTyPe : 12.4578 : 0.05  "
# - Nome: Title Case, senza '-' o '_', pulito da spazi.
# - Codice Univoco: Prime 3 lettere NOME (UPPER) + ultime 2 cifre ID.
# - Matematica: Limite Sup/Inf (Valore +/- Errore) arrotondati a 3 decimali.
# - Validazione: Controllo appartenenza nel Set di codici autorizzati.
#
# SET AUTORIZZATI: {"MAR21", "VEN22", "EAR23", "JUP66", "TIT50"}
# ==============================================================================

# Codice principale
def main():

    # Definisco i codici autorizzati dal ministero
    codici_autorizzati = {"MAR21", "VEN22", "EAR23", "JUP66", "TIT50"}
    
    # Ricevo stringa grezza da utente in ingresso
    stringa_grezza = input("Incolla qui la stringa: \n")
    
    # Pulisco stringa
    dati_grezzi = pulisci_stringa(stringa_grezza)
    intervallo = calcolo_range(dati_grezzi)

    # Controllo autorizzazione
    codice = genera_codice(dati_grezzi)
    autorizzazione = codice in codici_autorizzati

    # # Crea un Dizionario che contenga: id, nome_pulito, valore, limiti 
    # (i limiti devono essere una Tupla) e codice_univoco.
    dizionario =	{
        "id": dati_grezzi[0],
        "nome_pulito": dati_grezzi[1],
        "valore": float(dati_grezzi[2]),
        "limiti": intervallo,
        "codice_univoco": codice,
    }

    # Stampo rapporto
    print(f"Analisi completatata per: {dati_grezzi[1]}")
    print(f"Codice univoco: {codice}")
    print(f"Range Misurato: {intervallo}")
    print(f"Codice Autorizzato? {autorizzazione}")
    print(f"Dizionario Record: {dizionario}")
    

# Il sensore invia una singola stringa composta da 4 campi separati dal simbolo 
# dei due punti (:): " ID_Grezzo : NOME_CAMPIONE : VALORE : ERRORE "
# 1) Elimina ogni spazio bianco all'inizio e alla fine della stringa intera
# 2) Rompi la stringa nei 4 componenti originali
# 3) Il nome del campione deve essere trasformato in "Title Case". 
#    Eventuali trattini bassi (_) o medi (-) sostituiti con spazi vuoti.
def pulisci_stringa(stringa):

    # Creo lista vuota per il return
    lista_pulita = []

    # Ricevo stringa, pulisco spazi, divido e trasformo in lista
    lista_grezza = stringa.strip().split(':')

    # Standardizzo elementi lista
    lista_pulita.append(lista_grezza[0].strip())
    lista_pulita.append(lista_grezza[1].strip().title().replace("-", " ").replace("_", " "))
    lista_pulita.append(lista_grezza[2].strip())
    lista_pulita.append(lista_grezza[3].strip())

    # Ritorno
    return lista_pulita

# Generazione Codice Univoco: Crea una stringa di 5 caratteri composta da:
# Le prime 3 lettere del nome pulito (convertite in tutto MAIUSCOLO).
# Le ultime 2 cifre dell'ID (es. se l'ID è id-9921, prendi 21).
def genera_codice(lista_messaggio):
    
    # Estraggo le stringhe dalla lista
    id = lista_messaggio[0]
    sensore = lista_messaggio[1]

    # Genero il codice univoco
    codice_univoco = sensore[:3].upper() + id[-2:]

    # Ritorno
    return codice_univoco

# Converti il Valore e l'Errore in numeri float.
# Calcola il Limite Superiore (Valore + Errore) e il Limite Inferiore (Valore - Errore).
# Arrotonda entrambi i risultati a 3 cifre decimali.
def calcolo_range(lista_messaggio):

    # Calcolo minimo, massimo e arrotondo
    val_min = round(float(lista_messaggio[2]) - float(lista_messaggio[3]), 3)
    val_max = round(float(lista_messaggio[2]) + float(lista_messaggio[3]), 3)

    # Ritorno
    return (val_min, val_max)

main()