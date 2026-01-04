# =============================================================================
# ESERCIZIO 4: GESTIONE CODE E STACK
# =============================================================================
# Crea una lista 'attesa' con 4 nomi di persone in coda
# Simula le seguenti situazioni:
# - L'arrivo di 2 nuove persone (aggiungi alla fine)
# - Il servizio della prima persona in coda (usando indice)
# - Una persona che abbandona la coda (rimuovi per valore)
# - Stampa: "Ci sono X persone in attesa"
# - **SFIDA**: cerca come **copiare** la lista in una nuova variabile 
#   'attesa_backup' senza che le modifiche all'una influenzino l'altra 
#   (ricerca richiesta!)

# Il tuo codice qui:

persone = ['Leonardo', 'Michelangelo', 'Raffaello', 'Donatello']

# Arrivano due persone
persone.append('Tiziano')
persone.append('Giorgione')

# Prima persona è servita
servito = persone.pop(0)
print("Persona servita:", servito)

# Rimuovo elemento con valore
persone.remove('Raffaello')

# Stampo il numero di persone in coda
print(f"Ci sono {len(persone)} persone in attesa")

# Copia della lista
attesa_backup = persone.copy()
