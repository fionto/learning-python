# =============================================================================
# ESERCIZIO: Tuple - Livello medio/basso
# Argomenti: creazione, indicizzazione, unpacking, metodi .count() e .index()
# =============================================================================
#
# Una piccola stazione meteorologica ha registrato le temperature massime
# (in gradi Celsius) di una settimana di luglio in questa tupla:
#
#   temperature = (31, 34, 34, 29, 27, 33, 34)
#
# I giorni corrispondono nell'ordine a: lunedì, martedì, mercoledì,
# giovedì, venerdì, sabato, domenica.
#
# Completate i punti seguenti usando SOLO gli strumenti studiati sulle tuple
# (nessuna lista, nessun ciclo for, a meno che non sia esplicitamente richiesto).
#
# -----------------------------------------------------------------------------
# PUNTO 1
# Assegnate la tupla alla variabile "temperature".
# Stampate quanti giorni sono stati registrati.
#
# Output atteso:
#   Giorni registrati: 7
#
# -----------------------------------------------------------------------------
# PUNTO 2
# Usando l'indicizzazione, stampate la temperatura di lunedì e quella
# di domenica (rispettivamente primo e ultimo elemento).
#
# Output atteso:
#   Temperatura lunedì: 31 °C
#   Temperatura domenica: 34 °C
#
# -----------------------------------------------------------------------------
# PUNTO 3
# Estraete con lo slicing le temperature del fine settimana
# (sabato e domenica) e assegnatele a una variabile "weekend".
# Stampate il risultato.
#
# Output atteso:
#   Temperature weekend: (33, 34)
#
# -----------------------------------------------------------------------------
# PUNTO 4
# Usando l'unpacking, assegnate le sette temperature a sette variabili:
# lun, mar, mer, gio, ven, sab, dom.
# Stampate la temperatura di giovedì usando la variabile corrispondente.
#
# Output atteso:
#   Giovedì: 29 °C
#
# -----------------------------------------------------------------------------
# PUNTO 5
# Quante volte compare 34 gradi nella settimana?
# Usate il metodo appropriato della tupla.
#
# Output atteso:
#   Giorni a 34 °C: 3
#
# -----------------------------------------------------------------------------
# PUNTO 6
# In quale posizione (indice) appare per la prima volta la temperatura 34?
# Usate il metodo appropriato della tupla.
# Ricordate: l'indice 0 corrisponde a lunedì.
#
# Output atteso:
#   Prima occorrenza di 34 °C all'indice: 1
#
# -----------------------------------------------------------------------------
# PUNTO 7 (piccola sfida)
# Provate ad assegnare il valore 99 alla posizione 0 della tupla.
# Non eseguite la riga: lasciatela commentata e scrivete sotto,
# sempre come commento, cosa succede e perché.
#
# =============================================================================

temperature = (31, 34, 34, 29, 27, 33, 34)

print("===REPORT===")
# PASSO 1
print(f"Giorni totali registrati: {len(temperature)}")

# PASSO 2
print(f"Temperatura lunedì: {temperature[0]} °C")
print(f"Temperatura domenica: {temperature[6]} °C")

# PASSO 3
temperature_weekend = temperature[-2:]
print(f"Temperature del finesettimana: {temperature_weekend}")

# PASSO 4
lun, mar, mer, gio, ven, sab, dom = temperature
print(f"Temperatura giovedì: {gio} °C")

# PASSO 5
print(f"Giorni a 34 °C: {temperature.count(34)}")

# PASSO 6
print(f"Primo giorno a 34 °C, index n.: {temperature.index(34)}")