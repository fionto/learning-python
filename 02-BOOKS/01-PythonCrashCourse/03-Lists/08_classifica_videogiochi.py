# =============================================================================
# ESERCIZIO 2: CLASSIFICA VIDEOGIOCHI
# =============================================================================
# Parti da questa lista di videogiochi in ordine casuale:

giochi = ["Zelda", "Mario", "Tetris", "Minecraft", "Fortnite"]

# Esegui le seguenti operazioni:
# - Stampa la classifica 
# - Inverti completamente l'ordine della classifica
# - Rimuovi il gioco in ultima posizione
# - Inserisci "GTA" al secondo posto
# - Stampa quanti giochi ci sono nella classifica finale

# Il tuo codice qui:

# print() può ricevere più oggetti separati da virgola
# e li stampa sulla stessa riga con uno spazio tra loro
print("Classifica iniziale:", giochi)

giochi.reverse()
print("Classifica invertita:", giochi)

giochi.pop()
print(giochi)

giochi.insert(1, 'GTA')
print(giochi)

print(len(giochi))