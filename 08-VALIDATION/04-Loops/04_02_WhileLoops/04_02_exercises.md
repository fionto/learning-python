# 04_02_WhileLoops

**Esercizi consolidati**: 9
**Generato il**: 14/01/2026 18:30
**Sorgente**: `04-Loops\04_02_WhileLoops`

---

## 4_2_01_password

```python
# ESERCIZIO 1: Validatore di Password Progressivo
#
# Crea un programma che chieda all'utente di inserire una password.
# Il programma continua a chiedere finché la password non soddisfa
# TUTTI i seguenti criteri:
# - Lunghezza minima 8 caratteri
# - Contiene almeno una lettera maiuscola
# - Contiene almeno una cifra
# - Contiene almeno uno tra questi caratteri speciali: !@#$%
#
# Dopo ogni tentativo fallito, mostra SOLO i criteri non soddisfatti.
# Quando la password è valida, mostra "Password accettata" e termina.
#
# Suggerimento tecnico: dovrai cercare metodi delle stringhe che
# verifichino presenza di lettere maiuscole e cifre.

# Creo set di confronto per velocizzare operatore in
special_characters = {'!', '@', '#', '$', '%'}

# Inizializzo le variabili su false per entrare la prima volta nel while
is_long = False
has_upper = False
has_digit = False
has_special = False
valid_password = is_long and has_upper and has_digit and has_special

# Nel primo ciclo sarà sicuramente False
while not valid_password:
    password = input("Inserisci una password valida: ")

    # Controllo dei criteri di validità
    is_long = len(password) >= 8
    # Uso funzione any() che restituisce True se almeno un suo elemento è truthy
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)
    valid_password = is_long and has_upper and has_digit and has_special
    
    # Guard Clause
    if valid_password:
        print("La password è valida.")
        continue
    
    if not is_long:
        print("La password deve contenere almeno 8 caratteri")
    if not has_upper:
        print("La password deve contenere almeno una maiuscola")
    if not has_digit:
        print("La password deve contenere almeno un numero")
    if not has_special:
        print("La password deve contenere almeno un carattere speciale (!@#$%)")
```

---

## 4_2_01_password2

```python
# ESERCIZIO 1: Validatore di Password Progressivo
#
# Crea un programma che chieda all'utente di inserire una password.
# Il programma continua a chiedere finché la password non soddisfa
# TUTTI i seguenti criteri:
# - Lunghezza minima 8 caratteri
# - Contiene almeno una lettera maiuscola
# - Contiene almeno una cifra
# - Contiene almeno uno tra questi caratteri speciali: !@#$%
#
# Dopo ogni tentativo fallito, mostra SOLO i criteri non soddisfatti.
# Quando la password è valida, mostra "Password accettata" e termina.
#
# Suggerimento tecnico: dovrai cercare metodi delle stringhe che
# verifichino presenza di lettere maiuscole e cifre.

# Creo set di confronto per velocizzare operatore in
special_characters = {'!', '@', '#', '$', '%'}

# NOTA: In Python, per i cicli di validazione, 
# si preferisce l'uso di un ciclo infinito + break.

while True:

    password = input("Inserisci una password valida: ")

    # Eseguo i controlli direttamente dentro il ciclo.
    # Non ho bisogno di dichiarare queste variabili fuori dal while.
    is_long = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)

    # Verifico se TUTTE le condizioni sono True.
    # Se lo sono, stampo il successo ed esco immediatamente dal ciclo con break.
    if is_long and has_upper and has_digit and has_special:
        print("Password accettata")
        break

    # Se il codice arriva qui, significa che almeno una condizione è False.
    # Mostro solo gli errori specifici.
    if not is_long:
        print("La password deve contenere almeno 8 caratteri")
    if not has_upper:
        print("La password deve contenere almeno una maiuscola")
    if not has_digit:
        print("La password deve contenere almeno un numero")
    if not has_special:
        print("La password deve contenere almeno un carattere speciale (!@#$%)")
    
    # Il ciclo ricomincerà automaticamente da "password = input(...)"
```

---

## 4_2_01_password3

```python
# ESERCIZIO 1: Validatore di Password Progressivo
#
# Crea un programma che chieda all'utente di inserire una password.
# Il programma continua a chiedere finché la password non soddisfa
# TUTTI i seguenti criteri:
# - Lunghezza minima 8 caratteri
# - Contiene almeno una lettera maiuscola
# - Contiene almeno una cifra
# - Contiene almeno uno tra questi caratteri speciali: !@#$%
#
# Dopo ogni tentativo fallito, mostra SOLO i criteri non soddisfatti.
# Quando la password è valida, mostra "Password accettata" e termina.
#
# Suggerimento tecnico: dovrai cercare metodi delle stringhe che
# verifichino presenza di lettere maiuscole e cifre.

# Creo set di confronto per velocizzare operatore in
special_characters = {'!', '@', '#', '$', '%'}

# NOTA: Il codice precedente aveva una lista di if in cascata.
# Ciò crea ridondanza. Bisogna invece seguire il principio
# DRY (Don't Repeat Yourself).

while True:
    password = input("Inserisci una password valida: ")

    # Definisco i risultati dei controlli come booleani
    is_long = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)

    # Creo una lista che "accoppia" il risultato al suo messaggio di errore.
    # Ogni elemento della lista è una 'tupla' (risultato, messaggio).
    requirements = [
        (is_long, "almeno 8 caratteri"),
        (has_upper, "almeno una maiuscola"),
        (has_digit, "almeno un numero"),
        (has_special, "almeno un carattere speciale (!@#$%)")
    ]

    # Controllo se sono tutti validi. 
    # Uso una variabile di supporto (flag) per decidere se uscire.
    all_valid = True

    # Ciclo attraverso la lista dei requisiti e uso un singolo if annidato
    for satisfied, message in requirements:
        if not satisfied:
            print(f"ERRORE: {message}")
            all_valid = False # Se anche solo uno fallisce, non posso accettare la password

    # Se dopo il ciclo all_valid è ancora True, significa che nessun 'if not satisfied' è scattato
    if all_valid:
        print("Password accettata")
        break

    # NOTA: in questo modo se aggiungo un nuovo controllo devo modificare solo tupla       
```

---

## 4_2_02_statistica

```python
# ESERCIZIO 2: Analizzatore di Sequenze Numeriche
#
# Scrivi un programma che:
# 1. Chieda ripetutamente all'utente di inserire numeri interi
# 2. Memorizzi i numeri in una lista
# 3. Quando l'utente inserisce 'stop', il programma termina l'input
# 4. Calcola e stampa:
#    - La mediana della sequenza
#    - Il numero che appare più frequentemente (moda)
#    - Tutti i numeri che appaiono più di una volta
#
# Se l'utente inserisce valori non validi, ignora l'input e continua.
#
# Nota: dovrai implementare la logica per trovare mediana e moda
# senza usare librerie esterne (solo metodi built-in di liste/dizionari).

def main():
    numeri = []

    print("Crea una sequenza di numeri, premendo Invio \n"
    "termina la sequenza scrivendo stop")

    while True:
        dato_ingresso = input("Nuovo numero:").strip()
        is_float = check_float(dato_ingresso)
    
        if dato_ingresso == 'stop':
            break
        elif not dato_ingresso or not is_float:
            continue
        else:
            numeri.append(float(dato_ingresso))  

    print(f"La mediana della sequenza è pari a: {mediana(numeri)}")
    print(f"La moda della sequenza è pari a: {moda(numeri)}")
    print(f"I numeri che appaiono più di una volta sono: {ripetuti(numeri)}")

def check_float(stringa):    
    stringa = stringa.strip()

    # Gestisce il segno opzionale all'inizio
    if stringa.startswith(("+", "-")):
        stringa = stringa[1:]

    # Gestisce se è vuota
    if not stringa or stringa == ".":
        return False
    
    dot_count = 0
    for char in stringa:
        if char == ".":
            dot_count += 1
            if dot_count > 1: return False # Massimo un punto permesso
        elif not ('0' <= char <= '9'): # Confronto tabella
            return False    
    return True

def mediana(numeri):
    
    if not numeri:
        return None
    
    numeri_ordinati = sorted(numeri)
    elementi = len(numeri_ordinati)

    if elementi % 2 != 0:
        mediana = numeri_ordinati[((elementi + 1) // 2) - 1]
    else:
        mediana = (numeri_ordinati[(elementi//2) - 1] + numeri_ordinati[(elementi//2)])/2

    return mediana

def moda(numeri):
    
    if not numeri:
        return None
    
    moda = numeri[0]
    contatore_massimo = 0
        
    for numero in numeri:
        contatore_corrente = numeri.count(numero)
        if(contatore_corrente > contatore_massimo):
            contatore_massimo = contatore_corrente
            moda = numero

    return moda

def ripetuti(numeri):
    if not numeri:
        return None

    conteggi = {}
    for n in numeri:
        conteggi[n] = conteggi.get(n, 0) + 1

    return [n for n, c in conteggi.items() if c > 1]

main()
```

---

## 4_2_03_gestione_clinica

```python
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
```

---

## 4_2_04_validatore_codici

```python
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
```

---

## 4_2_05_analizzatore_testo

```python
# ESERCIZIO 5
# 
# OBIETTIVO: Chiedi all'utente di inserire una frase. Usa un ciclo while per 
# contare quante volte compare ogni carattere e salva i risultati in un dizionario.
# Successivamente, chiedi all'utente quale carattere vuole eliminare dal conteggio.
# Usa un ciclo while insieme al metodo .popitem() per svuotare il dizionario
# e stampare solo le coppie chiave-valore che NON corrispondono al carattere scelto.
# REQUISITO EXTRA: Studia il funzionamento di .popitem() per i dizionari.

frase = input("Inserisci una frase: ")
caratteri = list(frase)

conteggi = {}

while caratteri:
    carattere = caratteri.pop(0)
    conteggi[carattere] = conteggi.get(carattere, 0) + 1

da_eliminare = input("Inserisci un solo carattere da eliminare: ").strip()
da_eliminare = da_eliminare[0]

while conteggi:
    char, frequenza = conteggi.popitem() # NOTA: Tupla

    if char != da_eliminare:
        print(f"La lettera '{char}' appare {frequenza} volte")
```

---

## 4_2_06_trasformatore_stringhe

```python
# ESERCIZIO 6
# 
# OBIETTIVO: Data una stringa di input contenente coppie "chiave:valore" separate
# da virgole (es: "nome:Mario,cognome:Rossi"), usa un ciclo while e i metodi 
# .find() e .partition() per estrarre i dati e inserirli in un dizionario.
# Non è consentito l'uso del metodo .split().
# REQUISITO EXTRA: Studia attentamente come .partition() restituisce una tupla
# di tre elementi e usa questa caratteristica per avanzare nel ciclo sulla stringa.

dati_grezzi = "id:001,stato:attivo,livello:esperto,punteggio:85"

dati_singoli = []
dati_puliti = {}

while True:
    i = dati_grezzi.find(',')

    if i != -1:
        grezzo = dati_grezzi[:i]
        dati_singoli.append(grezzo)
        dati_grezzi = dati_grezzi[i + 1:]
        i = dati_grezzi.find(',')
    else:
        dati_singoli.append(dati_grezzi)
        break

while dati_singoli:
    chiave, delim, valore = dati_singoli.pop(0).partition(':')
    dati_puliti[chiave] = valore

print(dati_puliti)
```

---

## 4_2_06_trasformatore_stringhe2

```python
# ESERCIZIO 6
# 
# OBIETTIVO: Data una stringa di input contenente coppie "chiave:valore" separate
# da virgole (es: "nome:Mario,cognome:Rossi"), usa un ciclo while e partition() 
# per estrarre i dati e inserirli in un dizionario.

dati_grezzi = "id:001,stato:attivo,livello:esperto,punteggio:85"
dati_puliti = {}

while dati_grezzi:
    # Estraggo la prima coppia e il resto della stringa
    coppia, virgola, resto = dati_grezzi.partition(',')
    
    # Processo la coppia trovata
    chiave, due_punti, valore = coppia.partition(':')
    dati_puliti[chiave] = valore
    
    # Aggiorniamo la stringa principale con il 'resto' per il prossimo ciclo
    dati_grezzi = resto
```

---

