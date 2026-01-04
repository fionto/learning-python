# ============================================
# ESERCIZIO 2 – Analisi di una frase
#
# Chiedi all’utente di inserire una frase.
#
# Il programma deve:
# - verificare se la frase è vuota
# - controllare se contiene almeno una parola
#   vietata (ignorando maiuscole/minuscole)
# - stampare:
#   - "Frase accettata"
#   - oppure "Frase non valida: motivo ..."
# ============================================

forbidden_words = {"cazzo", "merda", "stronzo"}

# chiedi la frase all'utente
user_sentence = input("Inserisci una frase: ")
user_sentence_lower = user_sentence.lower()

# flag iniziali
found_forbidden_word = False
empty_sentence = False

# controllo frase vuota
if user_sentence_lower.strip():
    
    # controllo parole vietate come sottostringhe
    for forbidden_word in forbidden_words:
        if forbidden_word in user_sentence_lower:
            found_forbidden_word = True
    
else:
    empty_sentence = True

# output finale
if not empty_sentence and not found_forbidden_word:
    print("Frase accettata.")
elif found_forbidden_word:
    print("Frase non valida: parola vietata")
else:
    print("Frase non valida: frase vuota")