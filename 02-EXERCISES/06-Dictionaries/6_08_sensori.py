# ESERCIZIO 8
# Data una lista di dizionari, ciascuno contenente informazioni
# su un sensore (id, tipo, valore),
# scrivi una funzione che restituisca un dizionario
# che associa a ogni tipo di sensore la lista dei valori misurati.
#
# INPUT:

sensori = [
    {"id": 1, "tipo": "temperatura", "valore": 22.5},
    {"id": 2, "tipo": "pressione", "valore": 1.01},
    {"id": 3, "tipo": "temperatura", "valore": 23.1},
    {"id": 4, "tipo": "umidità", "valore": 45},
    {"id": 5, "tipo": "pressione", "valore": 0.99}
]

# All'inizio il dizionario è vuoto.
# devo costruire le chiavi man mano che scorro la lista.
valori_misurati = {}

for sensore in sensori:
    # Estraggo le informazioni che mi servono.
    # Meglio farlo subito, così il codice è più leggibile
    # e non devo rileggere ogni volta il dizionario.
    tipo = sensore["tipo"]
    valore = sensore["valore"]
    
    # Creazione della chiave: prima controllo condizionale se esiste
    # l'operatore `in` che punta a dizionario esegue controllo sulle chiavi
    if tipo not in valori_misurati:
        # Se la chiave non esiste, devo crearla io.
        # E siccome poi voglio usare append(),
        # il valore associato deve essere una lista vuota.        
        valori_misurati[tipo] = []
    
    # A questo punto sono sicuro di una cosa fondamentale:
    # - la chiave esiste
    # - il valore associato è una lista
    # quindi posso tranquillamente usare append()    
    valori_misurati[tipo].append(valore)
        
print(valori_misurati)

# NOTA (errore iniziale):
# In una versione precedente del codice cercavo di fare direttamente:
# valori_misurati[tipo].append(valore)
# dando per scontato che la chiave 'tipo' esistesse già nel dizionario.
# In realtà, usando .append() stavo prima LEGGENDO il valore associato alla chiave,
# e solo dopo cercavo di modificarlo.
# Se la chiave non esiste, la lettura fallisce e il dizionario NON si espande da solo.
# La chiave viene creata automaticamente solo quando si assegna esplicitamente:
# valori_misurati[tipo] = []
# Da lì in poi, append() funziona correttamente.