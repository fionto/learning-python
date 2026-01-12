# ESERCIZIO 3: Selezione a intervalli (Step)
# Obiettivo: Selezionare elementi non contigui da una lista di stringhe.
# 1. Estrarre ogni secondo elemento della lista (elementi in posizione pari: 0, 2, 4...).
# 2. Estrarre ogni terzo elemento partendo dal secondo (indice 1).
# 3. Estrarre gli elementi in ordine inverso, ma saltandone uno (uno sì e uno no).

frutti = ["mela", "banana", "ciliegia", "durian", "uva", "fico", "guava"]

# Risultati attesi:
# 1. ['mela', 'ciliegia', 'uva', 'guava']
# 2. ['banana', 'uva']
# 3. ['guava', 'uva', 'ciliegia', 'mela']

risultato_uno = frutti[::2]
print(risultato_uno)

risultato_due = frutti[1::3]
print(risultato_due)

risultato_tre = frutti[::-2]
print(risultato_tre)