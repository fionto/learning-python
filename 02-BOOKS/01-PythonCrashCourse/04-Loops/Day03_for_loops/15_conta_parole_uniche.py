# Conta parole uniche
parole = ['python', 'è', 'divertente', 'python', 'è', 'potente']

parole_uniche = []

for parola in parole:
    if parola not in parole_uniche:
        parole_uniche.append(parola)

conto_uniche = len(parole_uniche)

