# ============================================================================
# DIMOSTRAZIONE: MUTABILITÀ vs IMMUTABILITÀ in Python
# ============================================================================
# Questo script dimostra la differenza fondamentale tra tipi mutabili 
# (come le liste) e tipi immutabili (come le stringhe) quando si assegnano
# variabili in Python.
#
# CONCETTO CHIAVE:
# - Tipi MUTABILI: l'assegnazione crea un ALIAS (stesso oggetto in memoria)
# - Tipi IMMUTABILI: l'assegnazione con nuovi valori crea NUOVI OGGETTI
# ============================================================================

# ----------------------------------------------------------------------------
# PARTE 1: LISTE (tipo MUTABILE)
# ----------------------------------------------------------------------------

# Creo una lista e la assegno a nazioni_uno
nazioni_uno = ['Francia', 'Spagna', 'Italia', 'Portogallo']

# ATTENZIONE: questa NON è una copia!
# nazioni_due è solo un ALIAS di nazioni_uno
# Entrambe le variabili puntano alla STESSA lista in memoria
nazioni_due = nazioni_uno

# Stampo entrambe le variabili - al momento sono identiche
print("=== STATO INIZIALE LISTE ===")
print(f"nazioni_uno: {nazioni_uno}")
print(f"nazioni_due: {nazioni_due}\n")

# ----------------------------------------------------------------------------
# PARTE 2: STRINGHE (tipo IMMUTABILE)
# ----------------------------------------------------------------------------

# Creo una stringa e la assegno a nome_uno
nome_uno = "napoleone bonaparte"

# Anche qui, inizialmente entrambe puntano alla stessa stringa
nome_due = nome_uno

# Stampo entrambe le variabili - al momento sono identiche
print("=== STATO INIZIALE STRINGHE ===")
print(f"nome_uno: {nome_uno}")
print(f"nome_due: {nome_due}\n")

# ----------------------------------------------------------------------------
# PARTE 3: MODIFICHE e DIFFERENZE di COMPORTAMENTO
# ----------------------------------------------------------------------------

# MODIFICA LA LISTA: cambio un elemento tramite indicizzazione
# Siccome nazioni_uno e nazioni_due sono ALIAS della stessa lista,
# la modifica si riflette su ENTRAMBE le variabili
nazioni_uno[1] = 'Germania'

# MODIFICA LA STRINGA: riassegno la variabile
# Le stringhe sono IMMUTABILI, quindi non posso fare nome_uno[0] = 'g'
# Posso solo creare una NUOVA stringa e farla puntare a nome_uno
# nome_due continua a puntare alla stringa originale
nome_uno = 'giulio cesare'

# ----------------------------------------------------------------------------
# PARTE 4: RISULTATI
# ----------------------------------------------------------------------------

print("=== DOPO LE MODIFICHE ===")
print("\n--- LISTE ---")
print(f"nazioni_uno: {nazioni_uno}")
print(f"nazioni_due: {nazioni_due}")  # SORPRESA: anche questa è cambiata!
print("^ Entrambe mostrano la modifica perché puntano allo stesso oggetto")

print("\n--- STRINGHE ---")
print(f"nome_uno: {nome_uno}")
print(f"nome_due: {nome_due}")  # Questa è rimasta invariata
print(
    "^ nome_due è rimasta invariata perché "
    "nome_uno ora punta a un nuovo oggetto"
)