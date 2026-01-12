# ESERCIZIO 4: Slicing per la copia e verifica immutabilità
# Obiettivo: Dimostrare la differenza tra copia di una lista e riferimento, 
# e osservare il comportamento delle stringhe.
# 1. Creare una copia Shallow della lista 'colori' chiamarla 'colori_copia'.
# 2. Modificare il primo elemento di 'colori' in "nero". Verificare che 'colori_copia' sia rimasta invariata.
# 3. Provare a modificare un carattere della stringa 'nome' tramite slicing (es. nome[0] = "K").
# NOTA: Osservate l'errore generato al punto 3 per confermare l'immutabilità.

colori = ["rosso", "verde", "blu"]
nome = "Python"

# Risultati attesi:
# colori: ["nero", "verde", "blu"]
# colori_copia: ["rosso", "verde", "blu"]
# Errore atteso al punto 3: TypeError: 'str' object does not support item assignment

colori_copia = colori[:]

colori[0] = 'nero'

print(f"lista originale è composta da : {colori}")
print(f"lista originale è composta da : {colori_copia}")