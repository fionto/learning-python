# Crea una lista di numeri fino a 1_000_000 con range()
# usa min() e max() per verificare gli estremi
# usa sum() per sommare tutto

numeri = range(0, 1_000_001, 1)

print(f"Il numero minimo è: {min(numeri):,d}")
print(f"Il numero massimo è: {max(numeri):,d}")

print(f"La somma totale è: {sum(numeri):,d}")