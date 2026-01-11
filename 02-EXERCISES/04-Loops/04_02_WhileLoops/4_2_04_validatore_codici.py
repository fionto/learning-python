# ESERCIZIO 4
# 
# OBIETTIVO: Data una lista di codici seriali sporchi (fornita sotto), 
# usa un ciclo while per processarli. Un codice è valido solo se:
# 1. Non contiene spazi bianchi all'inizio o alla fine.
# 2. È composto solo da caratteri alfanumerici.
# 3. Ha una lunghezza di esattamente 8 caratteri.
# Salva i codici validi in una nuova lista e quelli errati in un dizionario
# dove la chiave è il codice e il valore è il motivo dell'errore.
# REQUISITO EXTRA: Usa i metodi .isalnum() e .strip() e gestisci l'iterazione
# con il metodo .pop() sulla lista originale.

codici_da_testare = ["  AX12345 ", "B22_99X", "12345678", "Pass1234", "Abc 1234", "9900112233"]

codici_errati = {}
codici_validi = []

while codici_da_testare:
    codice = codici_da_testare.pop(0)

    if codice.startswith(" ") or codice.endswith(" "):
        codici_errati[codice] = "Ha spazi bianchi all'inizio o alla fine"
    elif not codice.isalnum():
        codici_errati[codice] = "Contiene simboli"
    elif len(codice) != 8:
        codici_errati[codice] = "Lunghezza diversa da 8 caratteri"
    else:
        codici_validi.append(codice)

print(codici_validi)
print(codici_errati)