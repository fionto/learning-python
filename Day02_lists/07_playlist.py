# =============================================================================
# ESERCIZIO 1: GESTIONE PLAYLIST MUSICALE
# =============================================================================
# Crea una lista chiamata 'playlist' con almeno 5 canzoni
# Poi esegui le seguenti operazioni:
# - Aggiungi una nuova canzone all'inizio della playlist
# - Rimuovi la terza canzone
# - Sposta l'ultima canzone in seconda posizione
# - Ordina la playlist alfabeticamente e stampala
# - Crea una seconda versione ordinata al contrario senza modificare l'originale

# Il tuo codice qui:

# Creo la playlist
playlist = ['Eight Days A Week', 'Let It Be', 'In My Life', 'Hey Jude', 'While My Guitar Gently Weeps']

# Inserisco una nuova canzone all'inizio
playlist.insert(0, 'Yesterday')

# Eliminato la terza canzone
del playlist[2]

# Sposto ultimo elemento al secondo posto
canzone_spostata = playlist.pop()
playlist.insert(1, canzone_spostata)

# Ordino alfabeticamente
playlist.sort()
print(playlist)

#Inverto
reversed_playlist = list(reversed(playlist)) # Alternativa 1: usando sorted() con reverse=True
print(reversed_playlist)