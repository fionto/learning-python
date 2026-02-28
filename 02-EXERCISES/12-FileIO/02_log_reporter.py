# ==============================================================================
# ESERCIZIO 2: IL FILTRO INTELLIGENTE (Log Reporter)
# ==============================================================================
#
# OBIETTIVO:
# Creare uno script che legge un file di "log" simulato, filtra le righe in base
# a una parola chiave e scrive solo quelle rilevanti in un nuovo file, aggiungendo
# un numero progressivo.
#
# PREREQUISITI:
# 1. Nella cartella 'files', crea manualmente un file chiamato 'log_server.txt'.
# 2. Inserisci dentro almeno 10-15 righe di testo misto. Alcune devono contenere
#    la parola "ERRORE", altre la parola "INFO", e altre testo a caso.
#
# ISTRUZIONI:
# 1. Apri 'log_server.txt' in lettura e 'report_errori.txt' in scrittura ('w').
# 2. Leggi il file riga per riga.
# 3. Per ogni riga, controlla se contiene la stringa "ERRORE".
# 4. SE la riga contiene "ERRORE":
#    - Incrementa un contatore (che parte da 0).
#    - Scrivi la riga nel nuovo file 'report_errori.txt', ma preceduta dal numero
#      dell'errore trovato.
#      Formato output esatto: "Errore #1: [contenuto originale della riga]"
#      (Assicurati di gestire gli spazi e gli a capo correttamente con .strip()).
# 5. SE la riga NON contiene "ERRORE", ignorala completamente.
# 6. Alla fine, stampa a console quante righe di errore sono state trovate e salvate.
#
# REQUISITI TECNICI:
# - Usa un ciclo 'for' per iterare sul file.
# - Usa una variabile intera come contatore.
# - Usa condizioni 'if' per filtrare.
# - Gestione encoding 'utf-8'.
#
# BONUS (OPZIONALE):
# - Rendi lo script case-insensitive: deve trovare sia "ERRORE", "Errore", che "errore".
# - Aggiungi una riga finale nel file di report che dica: "--- Totale errori trovati: X ---".
#
# ==============================================================================

parola_filtro = 'ERRORE'
contatore = 0
errori = ""

with open('files/log_server.txt', 'r', encoding='utf-8') as sorgente:
    with open('files/errors.txt', 'w', encoding='utf-8') as destinazione:

        for riga in sorgente:

            if parola_filtro not in riga.upper():
                continue
            
            contatore += 1
            linea_processata = f"Errore #{contatore}:" + riga.strip() + '\n'
            destinazione.write(linea_processata)
            print(linea_processata, end='') 

print(f"Totale errori trovati: {contatore}")
