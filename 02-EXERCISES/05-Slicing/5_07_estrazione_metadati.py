# ESERCIZIO 7: Parsing di una stringa a formato fisso
# Obiettivo: Estrarre informazioni specifiche da una stringa che simula un log.
# Formato: "DATA:20231012|ID:9958|TEMP:22.5"
# 1. Estrarre solo la DATA (i caratteri tra l'indice 5 e il primo separatore '|').
# 2. Estrarre l'ID (4 cifre) usando indici negativi riferiti alla posizione del secondo '|'.
# 3. Creare una nuova stringa che inverta l'ordine dei componenti: "TEMP:22.5|ID:9958|DATA:20231012"
#    usando solo lo slicing e la concatenazione.

log = "DATA:20231012|ID:9958|TEMP:22.5"

# Risultati attesi:
# 1. "20231012"
# 2. "9958"
# 3. "TEMP:22.5|ID:9958|DATA:20231012"

nuova_stringa = ''

# Trovo gli indici
separatore_colon = log.find(':')
separatore_bar = log.find('|')

# Estraggo e stampo solo data
data = log[separatore_colon + 1 :separatore_bar]
print(data)

# Metto da parte stringa
nuova_stringa = log[:separatore_bar]

log_copia = log[separatore_bar + 1:]
separatore_colon = log_copia.find(':')
separatore_bar = log_copia.find('|')
id = log_copia[separatore_colon + 1 :separatore_bar]
print(id)

# Costruisco la stringa inversa
nuova_stringa = log_copia[separatore_bar + 1:] + '|' + log_copia[:separatore_bar + 1] + nuova_stringa

print(nuova_stringa)