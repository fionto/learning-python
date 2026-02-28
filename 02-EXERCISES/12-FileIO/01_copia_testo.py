# ==============================================================================
# ESERCIZIO 1: IL COPIA-TESTO SEMPLICE
# ==============================================================================
#
# OBIETTIVO:
# Creare uno script che legge il contenuto di un file di testo e ne scrive
# una copia modificata in un nuovo file, utilizzando le funzioni base di I/O.
#
# PREREQUISITI:
# - In una sottocartella di questo script (/files/), crea manualmente un file chiamato
#   'esempio1.txt' e scrivici dentro almeno 3 righe di testo a piacere.
#
# ISTRUZIONI:
# 1. Apri il file 'esempio1.txt' in modalità lettura.
# 2. Leggi tutto il contenuto del file e salvalo in una variabile.
# 3. Apri (o crea) un nuovo file chiamato 'copia.txt' in modalità scrittura.
# 4. Scrivi nel nuovo file il contenuto letto precedentemente, ma convertito
#    tutto in lettere maiuscole.
# 5. Assicurati che i file vengano chiusi correttamente dopo le operazioni.
#
# REQUISITI TECNICI:
# - Usa la funzione built-in open().
# - Usa lo statement 'with' per la gestione sicura dei file (context manager).
# - Non importare librerie esterne (usa solo funzioni base delle stringhe).
#
# ==============================================================================

# Se si usano i percorsi relativi, ricordarsi di spostare anche la posizione del terminale.

print("Inizio lettura del file source...")

with open('files/esempio1.txt', 'r', encoding='utf-8') as f:
    testo_completo = f.read()

print(f"Letti {len(testo_completo)} caratteri")
print("\nInizio scrittura del file copia...")

with open('files/copia.txt', 'w', encoding='utf-8') as f:
    f.write(testo_completo.upper())

print("Copia completata con successo.")