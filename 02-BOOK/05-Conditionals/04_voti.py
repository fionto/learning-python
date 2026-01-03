# ============================================
# ESERCIZIO 4 – Classificazione numerica
#
# Chiedi all’utente di inserire un punteggio.
#
# Il programma deve:
# - verificare che l’input sia valido
# - classificare il punteggio in base alle soglie
#   definite in una struttura dati (non hardcoded)
# ============================================

# Soglie superiori (es. 0 a 49 insufficiente, stessa logica di range(0,50))
levels = {
    "insufficiente": 50,
    "sufficiente": 65,
    "buono": 80,
    "ottimo": 100
}

# Pulisco subito input
score_input = input("Inserisci il punteggio intero tra 0 e 100: ").strip()

# Scarto stringhe vuote, alfanumeriche e negative. Bug da risolvere, questo scarta anche valori non interi.
if score_input and score_input.isdigit():
    score = int(score_input)

    if score < 0 or score > levels["ottimo"]:
        print("Input non valido")
    elif score < levels["insufficiente"]:
        print("Il voto è insufficiente")
    elif score < levels["sufficiente"]:
        print("Il voto è sufficiente")
    elif score < levels["buono"]:
        print("Il voto è buono")
    else:
        print("Il voto è ottimo") 

else:
    print("Input non valido")