# ESERCIZIO 1: Il Classificatore di Voti
# Obiettivo: Utilizzare match/case per una selezione multipla semplice.
#
# Scrivi un programma che legga la variabile 'voto_lettera'. 
# Il programma deve stampare un messaggio in base al valore:
# - "A": "Eccellente"
# - "B": "Buono"
# - "C": "Sufficiente"
# - "D": "Insufficiente"
# - "F": "Gravemente insufficiente"
# - Qualsiasi altro valore: "Valutazione non valida"

voto_lettera = "W"

match voto_lettera:
    case "A":
        print("Eccellente")
    case "B":
        print("Buono")
    case "C":
        print("Sufficiente")
    case "D":
        print("Insufficiente")
    case "F":
        print("Gravemente insufficiente")
    case _:
        print("Valutazione non valida")