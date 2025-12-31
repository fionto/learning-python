# ESERCIZIO 4: Lunghezza delle stringhe in una lista
#
# Data una lista di parole 
# (ad esempio: ["gatto", "elefante", "ape", "dinosauro"]),
# usa un for loop per stampare ogni parola insieme alla sua lunghezza

animali = ["gatto", "elefante", "ape", "dinosauro"]

for animale in animali:
    lettere = len(animale)
    print(f"{animale.title()} ha {lettere} lettere")