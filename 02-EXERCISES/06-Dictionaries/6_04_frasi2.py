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

    # Non serve riempire le chiavi perché l'assegnazione dopo eseguue tutto
    dizionario = {}
    
    for frase in frasi:
        frase_pulita = frase.replace(',', '').replace('.', '').replace('!', '').lower()
        
        # Faccio split senza argomento: divido stringa su qualsiasi sequenza di whitespaces
        parole = frase_pulita.split()
        
        numero_uniche = uniche(parole)
        
        # Se la chiave non esiste, la crea. Se la chiave esiste, sovrascrivi il valore.
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