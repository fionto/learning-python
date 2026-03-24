# Capitolo 4: Sezione 2.1 — Decisioni e Branching: Insegnare al Computer a Scegliere

## Introduzione: Il Bivio sulla Strada

Immaginate di guidare in una città che non conoscete. A ogni incrocio, dovete prendere una decisione: svoltare a destra, a sinistra, oppure andare dritto. La scelta dipende dalla destinazione, dalle indicazioni stradali, dal traffico. Senza la capacità di prendere decisioni agli incroci, potreste solo andare dritti per sempre, incuranti di dove volete arrivare.

Un programma senza decisioni funziona esattamente così: esegue le istruzioni una dopo l'altra, dalla prima all'ultima, senza possibilità di adattarsi alle circostanze. Questo tipo di esecuzione lineare ha il suo valore, ma è fortemente limitato. Un programma che calcola l'IVA di un prezzo, per esempio, dovrebbe comportarsi diversamente a seconda che il prezzo superi o meno una certa soglia fiscale. Un programma che gestisce l'accesso a un sito deve distinguere tra chi ha inserito la password corretta e chi no.

La struttura che permette a Python di prendere decisioni si chiama **istruzione condizionale**, ed è il primo grande salto verso la programmazione reale. Con essa, il flusso di esecuzione non è più una strada dritta: diventa una rete di percorsi possibili, e il programma sceglie quale seguire in base ai dati che ha davanti.

In questa dispensa esploreremo le forme dell'istruzione condizionale in Python: dall'`if` più semplice, capace di eseguire un blocco di codice solo quando una condizione è vera, fino alle catene `if-elif-else` che gestiscono scenari con molte alternative. Impareremo anche come annidare le condizioni, cioè come costruire decisioni più sottili dentro altre decisioni, e come combinare più criteri in un'unica espressione logica.

Come prerequisiti, questa dispensa assume che conosciate gli operatori di confronto (`==`, `!=`, `<`, `>`, `<=`, `>=`) e gli operatori logici (`and`, `or`, `not`), trattati nella sezione 1.4. Se qualcosa di questi concetti non vi è chiaro, è il momento giusto per ripassarli.

---

## La Forma Base: `if`

Nella vita di tutti i giorni, diciamo spesso "se accade X, allora faccio Y". In Python questa struttura si traduce quasi parola per parola:

```python
if condizione:
    istruzione_da_eseguire
```

Se la condizione è vera (`True`), le istruzioni indentate sotto l'`if` vengono eseguite. Se è falsa (`False`), vengono saltate e il programma prosegue normalmente dopo il blocco.

Un dettaglio fondamentale: le istruzioni che appartengono all'`if` devono essere **indentate**, cioè rientrate rispetto all'`if` di un livello (convenzionalmente quattro spazi). L'indentazione non è un abbellimento estetico in Python: è la sintassi stessa. È il modo con cui Python capisce quali istruzioni fanno parte del blocco condizionale e quali no. Se dimenticate l'indentazione, otterrete un errore.

```python
# Esempio base: segnalare una temperatura anomala
temperatura = 38.5

if temperatura > 37.5:
    print("Attenzione: temperatura febbricitante")

print("Misurazione completata")
# Output:
# Attenzione: temperatura febbricitante
# Misurazione completata
```

In questo esempio, il messaggio "Attenzione" viene stampato solo perché `temperatura > 37.5` è vero. L'ultima `print`, invece, viene eseguita sempre, perché si trova fuori dal blocco indentato. Se avessimo impostato `temperatura = 36.0`, il messaggio di attenzione non sarebbe apparso, ma "Misurazione completata" sì.

---

## Aggiungere l'Alternativa: `if-else`

La struttura `if` da sola gestisce il caso "se vero, fai qualcosa; altrimenti, non fare nulla". Ma spesso ci serve anche un percorso alternativo: "se vero, fai X; altrimenti, fai Y". Questo è il ruolo di `else`.

```python
if condizione:
    # eseguito se la condizione è vera
else:
    # eseguito se la condizione è falsa
```

Esattamente uno dei due blocchi verrà eseguito: mai entrambi, mai nessuno dei due.

```python
# Controllare se un numero è pari o dispari
numero = 7

if numero % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")
# Output: Il numero è dispari
```

L'operatore `%` calcola il resto della divisione. Se il resto di `numero / 2` è zero, il numero è pari; altrimenti è dispari. Con `numero = 7`, il resto è 1 (diverso da zero), quindi la condizione è falsa e si esegue il ramo `else`.

Notate che anche il blocco `else` deve essere indentato coerentemente con l'`if`. La parola chiave `else` stessa si trova allo stesso livello dell'`if`, con i due punti (`:`) che la seguono.

---

## Condizioni Multiple: `if-elif-else`

La combinazione `if-else` funziona bene quando le alternative sono due. Ma cosa succede quando le possibilità sono tre, cinque, dieci? Potremmo immaginare di annidare tanti `if` dentro altri `if`, ma Python offre una soluzione molto più elegante: la parola chiave `elif`, contrazione di "else if".

```python
if prima_condizione:
    # eseguito se prima_condizione è vera
elif seconda_condizione:
    # eseguito se prima_condizione è falsa E seconda_condizione è vera
elif terza_condizione:
    # eseguito se le prime due sono false E terza_condizione è vera
else:
    # eseguito se TUTTE le condizioni precedenti sono false
```

Le condizioni vengono valutate nell'ordine in cui appaiono. Non appena una è vera, il relativo blocco viene eseguito e le condizioni successive vengono saltate senza essere valutate. Questo è importante: significa che l'ordine degli `elif` ha conseguenze concrete sul comportamento del programma.

Un esempio classico è la conversione di un punteggio numerico in un voto letterale:

```python
# Convertire un punteggio in un voto scolastico
punteggio = 72

if punteggio >= 90:
    voto = "A"
elif punteggio >= 80:
    voto = "B"
elif punteggio >= 70:
    voto = "C"
elif punteggio >= 60:
    voto = "D"
else:
    voto = "F"

print(f"Punteggio: {punteggio}, Voto: {voto}")
# Output: Punteggio: 72, Voto: C
```

Con `punteggio = 72`, la prima condizione (`72 >= 90`) è falsa; si valuta la seconda (`72 >= 80`), anch'essa falsa; si valuta la terza (`72 >= 70`), che è vera. Viene assegnato `voto = "C"` e il resto delle condizioni non viene nemmeno esaminato.

Potete usare quanti `elif` volete, ma solo un `if` all'inizio e al massimo un `else` alla fine. Sia l'`elif` che l'`else` sono facoltativi: un `if` da solo è perfettamente valido, così come un `if-else` senza alcun `elif`.

---

## Condizioni Multiple in un'Unica Espressione

Talvolta la condizione che ci interessa non è semplice come "questo numero è maggiore di zero", ma richiede di combinare più criteri. Possiamo farlo usando gli operatori logici `and`, `or`, e `not` direttamente all'interno dell'espressione condizionale.

Con `and`, entrambe le condizioni devono essere vere perché l'intera espressione lo sia:

```python
# Verificare se un anno è bisestile (regola semplificata)
anno = 2024

if anno % 4 == 0 and anno % 100 != 0:
    print(f"{anno} è bisestile")
else:
    print(f"{anno} non è bisestile")
# Output: 2024 è bisestile
```

Con `or`, basta che almeno una delle condizioni sia vera:

```python
# Controllare se un carattere è una vocale
carattere = "e"

if carattere == "a" or carattere == "e" or carattere == "i" or carattere == "o" or carattere == "u":
    print(f"'{carattere}' è una vocale")
else:
    print(f"'{carattere}' è una consonante")
# Output: 'e' è una vocale
```

Con `not`, invertiamo il valore logico di una condizione:

```python
# Segnalare se un campo testo è vuoto
nome_utente = ""

if not nome_utente:
    print("Errore: il campo nome non può essere vuoto")
# Output: Errore: il campo nome non può essere vuoto
```

In Python, una stringa vuota viene considerata falsa in un contesto booleano; `not ""` è quindi `True`. Questo idioma è molto comune nel codice Python reale.

Quando combinate più operatori logici nella stessa espressione, ricordate che `not` ha priorità più alta di `and`, che a sua volta ha priorità più alta di `or`. In caso di dubbio, usate le parentesi per rendere esplicita la logica:

```python
# Un controllo di accesso: admin, oppure utente attivo con permessi speciali
ruolo = "utente"
attivo = True
permesso_speciale = True

if ruolo == "admin" or (attivo and permesso_speciale):
    print("Accesso consentito")
# Output: Accesso consentito
```

---

## Nesting: Condizioni dentro Condizioni

A volte la logica del problema richiede di fare una seconda domanda solo dopo aver risposto alla prima. Pensate a come funziona un distributore automatico: prima controlla se avete inserito abbastanza monete; solo se la risposta è sì, controlla se il prodotto selezionato è disponibile. Non avrebbe senso verificare la disponibilità se il denaro inserito non basta.

Questo si traduce in Python con il **nesting** (annidamento): un'istruzione `if` all'interno di un altro blocco `if`. Ogni livello aggiuntivo richiede un ulteriore livello di indentazione.

```python
# Simulare l'accesso a un sistema con due livelli di verifica
nome_utente = "matteo"
password = "sicura123"
account_attivo = True

if nome_utente == "matteo":
    # Primo livello: utente riconosciuto
    if password == "sicura123":
        # Secondo livello: password corretta
        if account_attivo:
            print("Accesso effettuato con successo")
        else:
            print("Account disabilitato, contattare l'amministratore")
    else:
        print("Password errata")
else:
    print("Utente non trovato")
# Output: Accesso effettuato con successo
```

In questo esempio ci sono tre livelli di annidamento. Ogni blocco interno viene eseguito solo se tutte le condizioni nei blocchi esterni sono state soddisfatte. Se `nome_utente` fosse "luigi", il programma stamperebbe "Utente non trovato" e non valuterebbe mai la password.

È importante prestare attenzione all'indentazione quando si annidano le condizioni: ogni livello aggiunge quattro spazi, e un errore di rientro può cambiare completamente il significato del programma.

Un avvertimento pratico: il nesting profondo (tre, quattro, cinque livelli) rende il codice difficile da leggere e da mantenere. In molti casi, è possibile riscrivere una struttura profondamente annidata usando `and` e `or` per combinare le condizioni, oppure usando `elif`. L'esempio precedente, per molti casi d'uso, potrebbe essere semplificato così:

```python
# Versione più compatta con condizioni combinate
nome_utente = "matteo"
password = "sicura123"
account_attivo = True

if nome_utente == "matteo" and password == "sicura123" and account_attivo:
    print("Accesso effettuato con successo")
elif nome_utente != "matteo":
    print("Utente non trovato")
elif password != "sicura123":
    print("Password errata")
else:
    print("Account disabilitato, contattare l'amministratore")
# Output: Accesso effettuato con successo
```

Le due versioni non si comportano in modo identico in tutti i casi limite, ma per i percorsi principali producono lo stesso risultato. La scelta tra nesting e condizioni combinate dipende dalla chiarezza che volete dare al codice e dalla logica specifica del problema.

---

## Un Esempio Completo: Il Calcolatore di Tariffa

Per mettere insieme tutti i concetti visti, costruiamo un programma leggermente più articolato: un calcolatore di tariffa per un parcheggio che applica prezzi diversi in base all'ora di ingresso e alla durata della sosta.

```python
# Calcolo della tariffa di parcheggio
ora_ingresso = 14      # ora di ingresso (formato 24h)
durata_ore = 3         # durata della sosta in ore

# Determinare la fascia oraria
if ora_ingresso >= 8 and ora_ingresso < 13:
    fascia = "mattina"
elif ora_ingresso >= 13 and ora_ingresso < 20:
    fascia = "pomeriggio"
else:
    fascia = "notturna"

# Calcolare la tariffa in base alla fascia e alla durata
if fascia == "mattina":
    if durata_ore <= 1:
        tariffa = 2.0
    else:
        tariffa = 2.0 + (durata_ore - 1) * 1.5
elif fascia == "pomeriggio":
    if durata_ore <= 1:
        tariffa = 1.5
    else:
        tariffa = 1.5 + (durata_ore - 1) * 1.0
else:
    tariffa = durata_ore * 0.5   # tariffa ridotta in fascia notturna

print(f"Fascia: {fascia}")
print(f"Durata: {durata_ore} ore")
print(f"Tariffa totale: {tariffa:.2f} euro")
# Output:
# Fascia: pomeriggio
# Durata: 3 ore
# Tariffa totale: 3.50 euro
```

Questo programma usa prima una catena `if-elif-else` per determinare la fascia oraria, poi un secondo livello di condizionali (annidati nel primo) per calcolare la tariffa specifica. I due livelli di decisione sono logicamente separati e gestiti in modo indipendente, il che rende il codice leggibile nonostante la sua articolazione.

---

## Conclusione: Il Programma Impara a Decidere

Con le istruzioni condizionali, i nostri programmi hanno acquisito una capacità fondamentale: quella di rispondere in modo diverso a situazioni diverse. Non si tratta di una miglioria marginale: è la differenza tra uno strumento rigido e uno strumento intelligente.

Abbiamo visto come l'`if` semplice gestisca il caso "fai questo solo se vale la condizione"; come `if-else` introduca un percorso alternativo obbligatorio; come la catena `if-elif-else` permetta di discriminare tra molte alternative con piena leggibilità. Abbiamo poi visto come combinare più condizioni con `and`, `or`, e `not` in un'unica espressione compatta, e come il nesting consenta di porre domande annidate, dove la risposta alla seconda dipende dalla risposta alla prima.

Il passo successivo, nella sezione 2.2, sarà insegnare al programma non solo a scegliere, ma a **ripetere**: i cicli `while` e `for` ci daranno il potere di eseguire blocchi di codice più e più volte, con o senza un numero predefinito di iterazioni. Le condizioni che abbiamo imparato qui saranno la base di quel meccanismo: ogni ciclo, in fondo, è guidato da una decisione riformulata a ogni passo.
