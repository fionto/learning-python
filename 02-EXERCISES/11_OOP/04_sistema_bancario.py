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
#    - Scarta la transazione se l'importo non è un numero float positivo 
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

input_data_avanzato = [
    "VERSAMENTO:Elena:300",
    "VERSAMENTO:Marco:150",
    "PRELIEVO:Elena:300",       # Caso limite: svuotamento totale (saldo a 0)
    "PRELIEVO:Marco:200",       # Caso limite: saldo insufficiente
    "versamento:Marco:50",      # Caso sporco: minuscolo (deve essere ignorato se richiedi "VERSAMENTO")
    "VERSAMENTO:Anonimo:dieci", # Caso sporco: caratteri alfabetici nell'importo
    "PRELIEVO:Sofia:50",        # Caso logico insidioso: validazione OK, cliente nuovo, prelievo fallisce
    "VERSAMENTO:Elena:150.75",  # Caso sporco: presenza di decimali
    "BONIFICO:Elena:100",       # Caso sporco: operazione non supportata
    "VERSAMENTO:Marco:100:50",  # Caso sporco: troppi separatori
    "VERSAMENTO:Luca:-100"      # Caso sporco: numero negativo
]

class ContoCorrente:
    
    # Saldo iniziale sempre impostato a zero per l'istanziazione
    def __init__(self, nome):
        self.nome = nome
        self._saldo = 0 # Uso underscore per proteggere saldo
    
    # inserisco `return True/False` per eventuale gestione di print() nel main
    def deposita(self, importo):
        if importo < 0:
            return False

        self._saldo += importo
        return True
        
    def preleva(self, importo):
        if importo < 0:
            return False
        
        if self._saldo < importo:
            return False
        else:
            self._saldo -= importo
            return True
    
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"ContoCorrente(nome = {self.nome}, Saldo = {self._saldo})"

def is_valid_float(value: str) -> bool:
    """
    Verifica se una stringa può essere convertita in un numero decimale (float).
    
    La funzione valida la stringa controllando manualmente la presenza di segni,
    punti decimali e cifre numeriche, senza l'uso di blocchi try/except.

    Args:
        value: La stringa da analizzare.

    Returns:
        True se la stringa è un formato numerico valido, False altrimenti.
    """
    value = value.strip()

    # Gestisce il segno opzionale all'inizio
    if value.startswith(("+", "-")):
        value = value[1:]

    # Gestisce se è vuota
    if not value or value == ".":
        return False
    
    dot_count = 0
    for char in value:
        if char == ".":
            dot_count += 1
            if dot_count > 1: return False # Massimo un punto permesso
        elif not ('0' <= char <= '9'): # Confronto tabella
            return False    
    return True

def elabora_registro(movimenti):
    
    database_clienti = {}
    
    for movimento in movimenti:
        voci_movimento = movimento.strip().split(':')

        if len(voci_movimento) != 3:
            continue
        
        operazione, cliente, importo = voci_movimento

        if not is_valid_float(importo):
            continue

        importo = float(importo.strip())
        cliente = cliente.strip().title()
        operazione = operazione.strip().upper()

        if importo < 0:
            continue

        if operazione not in {"PRELIEVO", "VERSAMENTO"}: # da trasformare in set COSTANTE in futuro
            continue

        if cliente not in database_clienti:
            database_clienti[cliente] = ContoCorrente(cliente)
        
        match operazione:
            case "PRELIEVO":
                database_clienti[cliente].preleva(importo)
            case "VERSAMENTO":
                database_clienti[cliente].deposita(importo)
            case _:
                continue
    
    return database_clienti
        
def main():
    
    riepilogo = (elabora_registro(input_data_avanzato))

    for k, v in riepilogo.items():
        print(f"{k}: Saldo = {v.saldo()}")

main()