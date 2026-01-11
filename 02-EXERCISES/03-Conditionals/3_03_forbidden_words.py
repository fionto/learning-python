# ============================================
# ESERCIZIO 3 – Analisi di una frase
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
has_forbidden_word = False
empty_sentence = False

if user_sentence_lower.strip():
    
    for forbidden_word in forbidden_words:

        if user_sentence_lower.find(forbidden_word) != -1:
            has_forbidden_word = True
    
else:
    empty_sentence = True

if not empty_sentence and not has_forbidden_word:
    print("Frase accettata.")
elif has_forbidden_word:
    print("Frase non valida: parola vietata")
else:
    print("Frase non valida: frase vuota")