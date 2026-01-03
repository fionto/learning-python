# ESERCIZIO 7
# Data una lista di stringhe, crea una nuova lista contenente la lunghezza
# di ciascuna stringa, escludendo quelle che contengono solo spazi.
#
# La lista risultante deve contenere solo numeri interi.

animali = ['cane', 'gatto', 'rinoceronte', '  ', '', 'gallina']

lunghezze = [len(animale) for animale in animali if animale.strip()]

print(lunghezze)