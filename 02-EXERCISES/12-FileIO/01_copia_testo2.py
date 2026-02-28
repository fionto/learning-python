# ==============================================================================
# ESERCIZIO 1: IL COPIA-TESTO SEMPLICE
# ==============================================================================
#
# OBIETTIVO:
# Creare uno script che legge il contenuto di un file di testo e ne scrive
# una copia modificata in un nuovo file, utilizzando le funzioni base di I/O.
#
# BONUS (OPZIONALE):
# - Invece di scrivere tutto il contenuto in una volta, prova a leggere e scrivere
#   il file riga per riga.
# - Stampa a console un messaggio di conferma quando l'operazione è completata.
#

with open('files/esempio1.txt', 'r', encoding='utf-8') as f:
    for riga in f:
        with open('files/copia2.txt', 'a', encoding='utf-8') as scrivente:
            scrivente.write(riga.strip().upper())
            scrivente.write('\n')