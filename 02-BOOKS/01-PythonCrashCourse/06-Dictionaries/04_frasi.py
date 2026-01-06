# ESERCIZIO 4
#
# Dato un elenco di frasi, scrivi un codice che restituisca un dizionario
# in cui a ogni frase è associato il numero di parole uniche (case-insensitive),
# escludendo la punteggiatura.
#

def main():
    frasi = [
        "Python è divertente, Python è potente!",
        "Scrivere codice pulito è importante.",
        "È importante leggere la documentazione."
    ]

    # Riempio le chiavi del dizionario perché nel ciclo assegno i solo valori
    dizionario = dict.fromkeys(frasi)
    
    for frase in frasi:
        frase_pulita = frase.replace(',', '').replace('.', '').replace('!', '').lower()
        parole = frase_pulita.split(' ')
        
        numero_uniche = uniche(parole)
        
        # Assegno i valori alle chiavi
        dizionario[frase] = numero_uniche

    print(dizionario)
        

# Conta parole uniche
def uniche(lista_parole: list[str]) -> int:
    
    parole_uniche = []

    for parola in lista_parole:
        if parola not in parole_uniche:
            parole_uniche.append(parola)

    return len(parole_uniche)

main()