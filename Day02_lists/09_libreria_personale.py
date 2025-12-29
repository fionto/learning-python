# =============================================================================
# ESERCIZIO 3: LIBRERIA PERSONALE
# =============================================================================
# Crea una lista 'libreria' con 5 libri
# Poi esegui le seguenti operazioni:
# - Aggiungi 2 libri alla fine
# - Elimina il primo libro usando l'indice
# - Scopri quale metodo usare per **contare quante volte appare** un certo 
#   titolo (suggerimento: cerca nei metodi delle liste)
# - Trova il metodo per **svuotare completamente** la lista (ricerca necessaria!)
# - Verifica che la lista sia vuota stampando la sua lunghezza

# Il tuo codice qui:

libri = ['Cuori in Atlantide', 'Fight Club', 'Huckleberry Finn', 'Le Rane', '1984']

# Aggiungo due libri alla fine e stampo la lista aggiornata
libri.append('Fiori per Algernon')
libri.append('Guida galattica per gli autostoppisti')
print("Lista aggiornata:", libri)

# Elimino primo libro in lista e stampo la lista
del libri[0]
print("Lista dopo eliminazione:", libri)

# Conto occorrenze
conteggio = libri.count('1984')
print("Occorrenze dell'elemento '1984':", conteggio)

# Svuoto la lista
libri.clear()

# Verifico che ci siano 0 elementi
print("Lunghezza lista:", len(libri))