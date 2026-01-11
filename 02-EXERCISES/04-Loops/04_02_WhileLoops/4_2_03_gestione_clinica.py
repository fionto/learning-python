# ESERCIZIO 3
# 
# OBIETTIVO: Gestire una coda di pazienti. Il programma deve continuare a chiedere
# il nome del paziente finché l'utente non inserisce 'esci'. 
# Se il nome del paziente inizia con la lettera 'E' (Emergenza), il paziente 
# deve essere inserito all'inizio della lista, altrimenti alla fine.
# Al termine, usa un ciclo while per rimuovere e stampare i pazienti uno ad uno
# simulando la chiamata nell'ambulatorio.
# REQUISITO EXTRA: Cerca nella documentazione il metodo delle liste per 
# inserire elementi in una posizione specifica.

pazienti = []

while True:
    chiamata = input("Qual è il tuo nome?\n").strip().lower()
    
    if not chiamata:
        print("Inserire un nome valido")
        continue
    elif chiamata == 'esci':
        break
    elif chiamata.startswith('e'):
        pazienti.insert(0, chiamata)
    else:
        pazienti.append(chiamata)

while pazienti:
    print(f"E' il turno di {pazienti.pop(0).title()}")