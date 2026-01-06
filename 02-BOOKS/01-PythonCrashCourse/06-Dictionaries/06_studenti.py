# ESERCIZIO 6
#
# Dato un dizionario che associa studenti a una lista di voti,
# scrivi una funzione che restituisca un nuovo dizionario
# contenente solo gli studenti con una media maggiore o uguale a 27.
#


registro = {
    "Anna": [28, 30, 27],
    "Luca": [24, 26, 25],
    "Marco": [30, 29, 28],
    "Sara": [27, 26, 27]
}

promossi = {}

for studente, voti in registro.items():
    media = round(sum(voti)/len(voti), 1)
    
    if media > 27:
        promossi[studente] = media

print(promossi)