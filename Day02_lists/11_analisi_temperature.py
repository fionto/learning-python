# =============================================================================
# ESERCIZIO 5: ANALISI TEMPERATURE
# =============================================================================
# Crea una lista 'temperature' con 7 valori numerici
# (esempio: 18, 22, 19, 25, 21, 23, 20)
# Poi esegui le seguenti operazioni:
# - Aggiungi una temperatura anomala molto alta alla fine (es. 35)
# - Ordina le temperature
# - Scopri quale metodo permette di trovare **l'indice** di un valore 
#   specifico nella lista (ricerca!)
# - Trova l'indice della temperatura più alta
# - Crea una lista ordinata al contrario senza modificare 'temperature'
# - Calcola e stampa: "Differenza tra max e min: X gradi" 
#   (usa indicizzazione per prendere primo e ultimo elemento della lista 
#   ordinata)

# Il tuo codice qui:

temperature = [18, 22, 19, 25, 21, 23, 20]

# Registrato nuovo valore
temperature.append(35)

# Ordino da più piccolo a più grande
temperature.sort()

# controllo qual è il valore massimo e poi da quello ricavo indice
print("L'indice della temperatura più alta è:", temperature.index(max(temperature)))

# nuova lista riordinata al contrario
temperature_reversed = list(reversed(temperature))
print(temperature_reversed)

# calcolo della differenza
differenza = max(temperature) - min(temperature)
print("La differenza tra valore massimo e minimo è:", differenza)