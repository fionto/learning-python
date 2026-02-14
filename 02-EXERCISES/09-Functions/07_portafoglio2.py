# ESERCIZIO:
# Gestione e analisi di un portafoglio finanziario utilizzando *args.
#
# L'obiettivo è costruire un piccolo programma che analizzi un portafoglio
# composto da un numero arbitrario di investimenti, applicando il principio
# di separazione delle responsabilità.
#
# Ogni investimento è rappresentato da una tupla nella forma:
# (nome_asset, quantita, prezzo_unitario)
#
# Esempio:
# ("AAPL", 10, 185.5)
#
# Il programma deve:
# - accettare un numero variabile di investimenti tramite *args
# - calcolare il valore economico dei singoli investimenti
# - determinare il valore totale del portafoglio
# - produrre un output leggibile con un riepilogo dei dati
#
# Requisiti di progettazione:
# - NON scrivere una sola funzione che faccia tutto
# - suddividere il problema in più funzioni, ognuna con un solo compito
# - usare *args solo dove ha senso dal punto di vista logico
#
# Suggerimenti (non vincolanti):
# - una funzione potrebbe occuparsi del calcolo del valore di un investimento
# - una funzione potrebbe calcolare il valore totale del portafoglio
# - una funzione potrebbe gestire la visualizzazione dei risultati
#
# Comportamento atteso (esempio di output):
#
# Portafoglio:
# - AAPL: 10 × 185.50 € = 1855.00 €
# - MSFT: 5 × 310.00 € = 1550.00 €
# - BTP: 20 × 98.70 € = 1974.00 €
#
# Valore totale del portafoglio: 5379.00 €
#
# Suggerimenti aggiuntivi:
# - gestire il caso di portafoglio vuoto
# - usare una formattazione coerente per i valori monetari
# - mantenere le funzioni semplici e facilmente riutilizzabili
#
# Obiettivo didattico:
# - comprendere l'uso di *args in contesti reali
# - imparare a progettare funzioni con responsabilità singola
# - evitare funzioni monolitiche difficili da mantenere
