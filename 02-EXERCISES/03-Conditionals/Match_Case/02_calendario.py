# ESERCIZIO 2: Analizzatore di Calendario
# Obiettivo: Utilizzare l'operatore '|' per raggruppare pattern e la keyword 'as'.
#
# Data la lista 'giorni', itera su di essa. Per ogni elemento, usa un match/case per:
# 1. Identificare se è un giorno feriale (da Lunedì a Venerdì) e stampare: "Lavoro: [nome_giorno]"
# 2. Identificare se è un giorno festivo (Sabato o Domenica) e stampare: "Relax: [nome_giorno]"
# 3. Gestire input errati (es. "Gennaio") catturando il valore e stampando: "[valore] non è un giorno!"

giorni = ["Lunedì", "Sabato", "Mercoledì", "Domenica", "Gennaio"]

for giorno in giorni:
    match giorno:
        case "Lunedì" | "Martedì" | "Mercoledì" | "Giovedì" | "Venerdì" as nome_giorno:
            print(f"Lavoro: {nome_giorno}")
        case "Sabato" | "Domenica" as nome_giorno:
            print(f"Relax: {nome_giorno}")
        case altro:
            print(f"{altro} non è un giorno")