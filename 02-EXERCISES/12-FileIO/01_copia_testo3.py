# ==============================================================================
# VERSIONE OTTIMIZZATA: Lettura/Scrittura Riga-per-Riga
# ==============================================================================
#
# COSA È MIGLIORATO RISPETTO ALLA VERSIONE PRECEDENTE?
#
# 1. EFFICIENZA DISCO (Il punto più importante!)
#    - Prima: Aprivo e chiudevo il file di scrittura 'copia2.txt' ad OGNI riga.
#    - Ora:   Apro il file di scrittura UNA SOLA volta prima del ciclo.
#
# 2. GESTIONE DEL CONTENUTO ('w' vs 'a')
#    - Prima: Usavo 'a' (append) perché aprivo il file tante volte.
#    - Ora:   Posso usare 'w' (write). Questo assicura che ogni volta che lancio lo script,
#             il file 'copia2.txt' venga pulito e riscritto da zero, evitando duplicati accidentali
#             se eseguo il codice più volte.
# ==============================================================================

# Apro ENTRAMBI i file contemporaneamente.
# 'sorgente' è in lettura ('r'), 'destinazione' è in scrittura ('w').
with open('files/esempio1.txt', 'r', encoding='utf-8') as sorgente:
    with open('files/copia3.txt', 'w', encoding='utf-8') as destinazione:
        
        # Il ciclo ora scorre solo sulla lettura. La scrittura avviene dentro, 
        # ma senza riaprire il file ogni volta.
        for riga in sorgente:
            # 1. strip() toglie il vecchio a capo
            # 2. upper() mette in maiuscolo
            # 3. + '\n' aggiunge il nuovo a capo necessario
            linea_processata = riga.strip().upper() + '\n'
            
            # Scrivo la riga già pronta nel file tenuto aperto
            destinazione.write(linea_processata)

print("Fatto! Copia efficiente completata.")