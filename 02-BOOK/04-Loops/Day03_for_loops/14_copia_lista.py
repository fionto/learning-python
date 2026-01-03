# Genera una lista di pizze
# Copia in una nuova lista
# Aggiungi una pizza alla lista originale
# Aggiungi una pizza alla nuova lista
# Dimostra che sono due liste differenti

pizze_originali = ['Margherita', 'Capricciosa', 'Diavola']
pizze_nuove = pizze_originali[:]

pizze_originali.append('Boscaiola')
pizze_nuove.append('Hawaii')

print(pizze_originali)
print(pizze_nuove)