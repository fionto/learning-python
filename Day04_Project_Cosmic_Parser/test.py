# Test cosmic parser

messaggio = "id-1123: eaRth_sTatiOn-DeLtA : 25.0001 : 0.1"

# Creo stringa vuota per il return
stringa_pulita = []

# Ricevo stringa, pulisco spazi, divido e trasformo in lista
stringa = messaggio.strip().split(':')

# Standardizzo elementi lista
stringa_pulita.append(stringa[0].strip().title().replace("-", " ").replace("_", " "))
stringa_pulita.append(stringa[1].strip().title().replace("-", " ").replace("_", " "))
stringa_pulita.append(stringa[2].strip())
stringa_pulita.append(stringa[3].strip())

valore = float(stringa_pulita[2])
errore = float(stringa_pulita[3])

print(errore, valore)

print(stringa_pulita)