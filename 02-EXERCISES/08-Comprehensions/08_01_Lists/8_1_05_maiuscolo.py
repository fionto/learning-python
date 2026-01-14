# ESERCIZIO 5
# Data una lista di stringhe contenenti parole in minuscolo,
# crea una nuova lista che contenga le stesse parole ma in maiuscolo,
# escludendo però le parole vuote ("").
#
# Esempio:
# input  -> ["ciao", "", "python", "", "corso"]
# output -> ["CIAO", "PYTHON", "CORSO"]
#

parole = ["ciao", "", "python", "", "corso"]

maiuscole = [parola.upper() for parola in parole if parola]

print(maiuscole)