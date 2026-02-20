# ==========================================
# CODING CHALLENGE: SISTEMA BANCARIO DI BASE
# ==========================================
#
# OBIETTIVO:
# Scrivere un programma che simuli l'elaborazione di un registro giornaliero
# di transazioni bancarie. Il sistema deve leggere un elenco di operazioni, 
# creare dinamicamente i conti correnti necessari, aggiornare i saldi 
# e ignorare le registrazioni malformate.
#
# SPECIFICHE INPUT:
# Riceverai una lista di stringhe. Ogni stringa corretta è formattata come:
# "TIPO_OPERAZIONE:NOME_CLIENTE:IMPORTO"
#
# REQUISITI FUNZIONALI:
# 1. Definisci una classe 'ContoCorrente'. Al momento della creazione, 
#    deve richiedere il nome del titolare e impostare un saldo iniziale a 0.
# 2. La classe 'ContoCorrente' deve avere i seguenti metodi di istanza:
#    - Un metodo per depositare un importo.
#    - Un metodo per prelevare un importo (se il saldo disponibile è sufficiente, 
#      altrimenti l'operazione viene annullata/ignorata).
#    - Un metodo che restituisca una stringa con il riepilogo del conto.
# 3. Definisci una funzione principale chiamata 'elabora_registro' che accetta 
#    la lista dei dati di input.
# 4. All'interno della funzione, crea un Dizionario vuoto. Questo dizionario 
#    ti servirà da "database": le chiavi saranno i nomi dei clienti e 
#    i valori saranno le istanze degli oggetti 'ContoCorrente'.
# 5. Elabora la lista di stringhe passo dopo passo:
#    - Dividi ogni stringa nei suoi componenti.
#    - Scarta la transazione se non è divisa esattamente in 3 parti.
#    - Scarta la transazione se l'importo non è un numero intero positivo 
#    - Se il cliente menzionato non esiste ancora nel tuo Dizionario, 
#      crea una nuova istanza di 'ContoCorrente' e salvala nel dizionario.
#    - Esegui l'azione richiesta ("VERSAMENTO" o "PRELIEVO") chiamando 
#      il metodo corrispondente sull'oggetto del cliente.
#    - Se l'azione non è né "VERSAMENTO" né "PRELIEVO", scarta la transazione.
# 6. Al termine dell'elaborazione, il programma deve scorrere il dizionario 
#    e stampare a schermo il riepilogo di tutti i conti attivi.
#
# VINCOLI TECNICI:
# - È obbligatorio definire e istanziare la classe 'ContoCorrente'.
# - È obbligatorio usare un dizionario per memorizzare e recuperare gli oggetti.
# - L'estrazione dei dati dalle stringhe deve usare il metodo .split().
# - Usa costrutti condizionali (if/elif/else) per filtrare i dati sporchi 
#   senza far crashare il programma.

input_data = [
    "VERSAMENTO:Mario:500",
    "VERSAMENTO:Luigi:200",
    "PRELIEVO:Mario:150",
    "PRELIEVO:Luigi:300",     # Caso limite: deve fallire (saldo insufficiente, non scende sotto zero)
    "VERSAMENTO:Mario:-50",   # Caso sporco: importo negativo, deve essere ignorato
    "SCAMBIO:Mario:100",      # Caso sporco: operazione inesistente, da ignorare
    "VERSAMENTO:Anna:1000",
    "VERSAMENTO:Anna:ERR",    # Caso sporco: importo non numerico, deve essere ignorato
    "PRELIEVOMario100",       # Caso sporco: formato errato (mancano i separatori)
    "",                       # Caso limite: riga vuota
    "VERSAMENTO:Luigi:50",
    "VERSAMENTO:Mario:0"      # Operazione valida, ma impatto nullo sul saldo
]