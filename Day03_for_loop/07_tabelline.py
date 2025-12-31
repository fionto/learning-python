# ESERCIZIO 5: Tabellina con numeri
#
# Stampare le tabelline da 1 a 5.
# Il risultato dovrebbe mostrare qualcosa come:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 5 x 10 = 50

moltiplicandi = range(1, 6)
moltiplicatori = range(1, 6)

for moltiplicando in moltiplicandi:
    for moltiplicatore in moltiplicatori:
        prodotto = moltiplicando * moltiplicatore
        print(f"{moltiplicando} x {moltiplicatore} = {prodotto}")