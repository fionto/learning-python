def ripetuti(numeri):
    if not numeri:
        return None

    conteggi = {}
    for n in numeri:
        conteggi[n] = conteggi.get(n, 0) + 1

    return [n for n, c in conteggi.items() if c > 1]

serie_di_numeri = [7, 10, 6, 2, 1, 2, 2, 1, 3, 3, 3, 3, 4, 1, 1, 1, 4]
print(ripetuti(serie_di_numeri))