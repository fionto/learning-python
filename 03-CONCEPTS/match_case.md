# Pattern Matching in Python: Il Costrutto match/case

## Una Nuova Aggiunta al Linguaggio

Per quasi tre decenni, Python ha funzionato perfettamente senza un costrutto dedicato alla selezione multipla. Le istruzioni `if/elif/else` e i dizionari hanno sempre fornito modi chiari ed efficaci per gestire logiche decisionali complesse. Eppure, con Python 3.10 è arrivato qualcosa di nuovo: l'istruzione `match`, accompagnata dalle clausole `case`.

Questa aggiunta rappresenta una risposta alle richieste di chi, provenendo da altri linguaggi di programmazione, sentiva la mancanza di uno statement simile a `switch/case`. Ma `match` non è semplicemente una copia di costrutti esistenti in altri linguaggi: è stato progettato per essere molto più potente, introducendo il concetto di "structural pattern matching" (corrispondenza strutturale di pattern).

In questa dispensa esploreremo `match/case` partendo dai suoi usi più semplici e intuitivi, quelli che risolvono problemi concreti senza complicazioni eccessive. La potenza completa del pattern matching strutturale è un argomento avanzato che affronteremo solo superficialmente, ma avere una solida comprensione delle basi vi permetterà di decidere quando e se questo strumento è appropriato per i vostri problemi.

## Il Problema che match Risolve

Prima di immergerci nella sintassi, riflettiamo sul tipo di situazione che `match` è progettato per gestire. Immaginate di dover scrivere codice che reagisce diversamente in base al valore di una variabile. Avete già visto come fare questo con le istruzioni condizionali:

```python
# Sistema di notifiche per diverse priorità di messaggi
priorita_messaggio = "urgente"

if priorita_messaggio == "bassa":
    colore_notifica = "verde"
    suono = "beep_leggero"
    tempo_visualizzazione = 3
elif priorita_messaggio == "normale":
    colore_notifica = "blu"
    suono = "beep_standard"
    tempo_visualizzazione = 5
elif priorita_messaggio == "alta":
    colore_notifica = "arancione"
    suono = "beep_forte"
    tempo_visualizzazione = 10
elif priorita_messaggio == "urgente":
    colore_notifica = "rosso"
    suono = "allarme"
    tempo_visualizzazione = 30
else:
    # Valore non riconosciuto, uso configurazione predefinita
    colore_notifica = "grigio"
    suono = "silenzio"
    tempo_visualizzazione = 5

print(f"Notifica {colore_notifica} con suono '{suono}' per {tempo_visualizzazione}s")
```

Questo codice funziona perfettamente, ma richiede di ripetere `priorita_messaggio ==` per ogni confronto. Un'alternativa che avete già incontrato è l'uso di un dizionario:

```python
# Stesso problema risolto con un dizionario
configurazioni = {
    "bassa": ("verde", "beep_leggero", 3),
    "normale": ("blu", "beep_standard", 5),
    "alta": ("arancione", "beep_forte", 10),
    "urgente": ("rosso", "allarme", 30)
}

# Recupera la configurazione, o usa quella predefinita se la chiave non esiste
config = configurazioni.get(priorita_messaggio, ("grigio", "silenzio", 5))
colore_notifica, suono, tempo_visualizzazione = config

print(f"Notifica {colore_notifica} con suono '{suono}' per {tempo_visualizzazione}s")
```

Anche questo approccio è valido ed elegante, ma ha un limite: tutto il comportamento deve essere rappresentabile come dati nel dizionario. Se volessimo eseguire logica più complessa per ogni caso, dovremmo ricorrere a funzioni come valori del dizionario, aumentando la complessità.

È in situazioni come queste che `match` può offrire un'alternativa chiara ed esplicita.

## La Sintassi Base di match/case

L'istruzione `match` introduce una sintassi dedicata per la selezione multipla. Ecco come riscriveremmo l'esempio delle notifiche usando `match`:

```python
priorita_messaggio = "urgente"

match priorita_messaggio:
    case "bassa":
        colore_notifica = "verde"
        suono = "beep_leggero"
        tempo_visualizzazione = 3
    
    case "normale":
        colore_notifica = "blu"
        suono = "beep_standard"
        tempo_visualizzazione = 5
    
    case "alta":
        colore_notifica = "arancione"
        suono = "beep_forte"
        tempo_visualizzazione = 10
    
    case "urgente":
        colore_notifica = "rosso"
        suono = "allarme"
        tempo_visualizzazione = 30
    
    case _:
        # Il caso predefinito: corrisponde a qualsiasi valore
        colore_notifica = "grigio"
        suono = "silenzio"
        tempo_visualizzazione = 5

print(f"Notifica {colore_notifica} con suono '{suono}' per {tempo_visualizzazione}s")
```

Analizziamo come funziona questa struttura. L'istruzione `match` inizia valutando l'espressione nell'intestazione (in questo caso `priorita_messaggio`). Poi confronta il risultato con i pattern specificati nelle clausole `case`, una dopo l'altra, dall'alto verso il basso.

Quando viene trovata la prima corrispondenza, il blocco di codice sotto quella clausola `case` viene eseguito, e l'intera istruzione `match` termina. Se nessuna clausola corrisponde, il `match` può eseguire il blocco sotto `case _` (che funge da caso predefinito, simile all'`else` delle catene `if/elif/else`), oppure semplicemente terminare silenziosamente se `case _` non è presente.

Il carattere underscore `_` ha un significato speciale: è un pattern "wildcard" che corrisponde a qualsiasi cosa. Per questo motivo deve sempre essere l'ultimo caso, fungendo da rete di sicurezza.

## Pattern con Valori Multipli: L'Operatore |

Una delle caratteristiche più utili di `match` è la possibilità di specificare più valori in un singolo `case` usando l'operatore `|` (pipe), che qui significa "oppure":

```python
# Sistema di controllo accessi per diverse aree di un edificio
codice_area = "LAB-B"

match codice_area:
    case "UFFICIO-A" | "UFFICIO-B" | "UFFICIO-C":
        livello_accesso = "standard"
        badge_richiesto = "impiegato"
        print(f"Accesso alle aree uffici: livello {livello_accesso}")
    
    case "LAB-A" | "LAB-B":
        livello_accesso = "ricerca"
        badge_richiesto = "ricercatore"
        print(f"Accesso ai laboratori: livello {livello_accesso}")
    
    case "SERVER-ROOM" | "DATACENTER":
        livello_accesso = "tecnico"
        badge_richiesto = "amministratore IT"
        print(f"Accesso alle aree tecniche: livello {livello_accesso}")
    
    case "SALA-RIUNIONI":
        livello_accesso = "pubblico"
        badge_richiesto = "nessuno"
        print("Area pubblica, nessuna restrizione")
    
    case _:
        livello_accesso = "negato"
        badge_richiesto = "non autorizzato"
        print(f"Area non riconosciuta: codice {codice_area}")
```

In questo esempio, se `codice_area` è "LAB-A" oppure "LAB-B", viene eseguito lo stesso blocco di codice. Il primo pattern che corrisponde, leggendo da sinistra a destra, determina quale caso viene selezionato.

## Catturare Valori con as: Assegnazione Durante il Matching

A volte non ci interessa solo sapere che un valore corrisponde a un certo pattern, ma vogliamo anche conservare quel valore per usarlo successivamente. La parola chiave `as` permette di catturare il valore corrispondente assegnandolo a una variabile:

```python
# Sistema di classificazione dei comandi vocali
comando = "ferma"

match comando:
    case "inizia" | "comincia" | "avvia" as azione:
        # Se corrisponde uno di questi, 'azione' conterrà il comando specifico
        print(f"Comando di avvio riconosciuto: '{azione}'")
        avvia_processo()
    
    case "ferma" | "stoppa" | "termina" as azione:
        print(f"Comando di arresto riconosciuto: '{azione}'")
        ferma_processo()
    
    case "pausa" | "sospendi" as azione:
        print(f"Comando di pausa riconosciuto: '{azione}'")
        metti_in_pausa()
    
    case altro:
        # Variabile semplice senza 'as': cattura automaticamente il valore
        print(f"Comando non riconosciuto: '{altro}'")
        print("Comandi validi: inizia, ferma, pausa")
```

Notate l'ultima clausola `case altro:` senza il simbolo `_`. Una variabile semplice in un pattern corrisponde a qualsiasi valore e lo cattura automaticamente, assegnandolo alla variabile specificata. Funziona esattamente come `case _ as altro:`, ma con una sintassi più concisa.

È importante comprendere che le variabili create dentro i `case` (come `azione` o `altro` nell'esempio) sopravvivono all'istruzione `match` stessa e possono essere usate nel codice successivo, purché quel `case` sia stato effettivamente eseguito:

```python
stato_sistema = "errore"

match stato_sistema:
    case "ok" | "running" as stato_corrente:
        print(f"Sistema operativo: {stato_corrente}")
    
    case "warning" | "errore" as problema:
        print(f"Problema rilevato: {problema}")
        registra_nel_log(problema)
    
    case altro:
        print(f"Stato sconosciuto: {altro}")

# Le variabili sono accessibili dopo il match
# (se il loro case è stato eseguito)
print(f"Dettaglio finale: {problema}")  # 'errore' in questo caso
```

## Confronto Pratico: match vs if/elif/else

Per comprendere meglio quando `match` può essere vantaggioso, confrontiamo le due approcci in un esempio realistico. Supponiamo di dover classificare diversi tipi di file in base alla loro estensione:

```python
# Approccio con if/elif/else tradizionale
estensione = ".py"

if estensione in [".py", ".pyw"]:
    tipo = "Python"
    icona = "🐍"
    editor_consigliato = "VS Code"
elif estensione in [".js", ".jsx", ".ts"]:
    tipo = "JavaScript"
    icona = "📜"
    editor_consigliato = "VS Code"
elif estensione in [".html", ".htm"]:
    tipo = "HTML"
    icona = "🌐"
    editor_consigliato = "Browser"
elif estensione in [".css", ".scss", ".sass"]:
    tipo = "Stylesheet"
    icona = "🎨"
    editor_consigliato = "VS Code"
else:
    tipo = "Sconosciuto"
    icona = "❓"
    editor_consigliato = "Editor di testo"

print(f"{icona} File {tipo} - Apri con: {editor_consigliato}")
```

Ora la stessa logica con `match`:

```python
# Approccio con match/case
estensione = ".py"

match estensione:
    case ".py" | ".pyw":
        tipo = "Python"
        icona = "🐍"
        editor_consigliato = "VS Code"
    
    case ".js" | ".jsx" | ".ts":
        tipo = "JavaScript"
        icona = "📜"
        editor_consigliato = "VS Code"
    
    case ".html" | ".htm":
        tipo = "HTML"
        icona = "🌐"
        editor_consigliato = "Browser"
    
    case ".css" | ".scss" | ".sass":
        tipo = "Stylesheet"
        icona = "🎨"
        editor_consigliato = "VS Code"
    
    case _:
        tipo = "Sconosciuto"
        icona = "❓"
        editor_consigliato = "Editor di testo"

print(f"{icona} File {tipo} - Apri con: {editor_consigliato}")
```

Entrambi gli approcci sono validi. Il `match` rende più esplicita l'intenzione di "selezionare in base al valore di una variabile", mentre l'`if/elif/else` è leggermente più conciso e richiede meno indentazione. La scelta dipende dalle vostre preferenze di stile e dalla complessità della logica coinvolta.

## Iterare sui Case: Un Esempio Pratico

Il `match` diventa particolarmente utile quando combinato con cicli per processare collezioni di dati:

```python
# Elaborazione di una serie di transazioni bancarie
transazioni = ["deposito", "prelievo", "bonifico", "prelievo", "errore"]

saldo = 1000.0

for operazione in transazioni:
    match operazione:
        case "deposito":
            importo = 200.0
            saldo += importo
            print(f"Deposito di €{importo:.2f} - Nuovo saldo: €{saldo:.2f}")
        
        case "prelievo":
            importo = 150.0
            if saldo >= importo:
                saldo -= importo
                print(f"Prelievo di €{importo:.2f} - Nuovo saldo: €{saldo:.2f}")
            else:
                print("Prelievo negato: saldo insufficiente")
        
        case "bonifico":
            importo = 300.0
            commissione = 2.0
            totale = importo + commissione
            if saldo >= totale:
                saldo -= totale
                print(f"Bonifico di €{importo:.2f} (+ €{commissione:.2f} comm.) - Nuovo saldo: €{saldo:.2f}")
            else:
                print("Bonifico negato: saldo insufficiente")
        
        case altro:
            print(f"Operazione non valida: '{altro}'")

print(f"\nSaldo finale: €{saldo:.2f}")
```

In questo esempio, ogni iterazione del ciclo valuta un tipo di transazione diverso, eseguendo la logica appropriata per ciascuna. Il pattern `case altro:` cattura qualsiasi operazione non riconosciuta, permettendoci di gestire errori con eleganza.

## Quando Usare match e Quando Evitarlo

Ora che avete visto `match` in azione, è importante capire quando è appropriato usarlo e quando altre soluzioni sono preferibili.

**Usate match quando:**
- Avete una selezione multipla basata sul valore esatto di una singola variabile
- I diversi casi richiedono blocchi di codice distinti (non solo valori di ritorno)
- Volete rendere esplicita la natura di "switch su valore" della vostra logica
- State lavorando su codice dove più valori portano alla stessa azione (sfruttando `|`)

**Preferite if/elif/else quando:**
- Le condizioni sono complesse e non si limitano a confronti di uguaglianza
- Dovete valutare espressioni booleane composite
- La logica coinvolge confronti di range (`x > 10 and x < 20`)
- State già usando questo pattern e il codice è chiaro

**Preferite dizionari quando:**
- State mappando valori a valori (non a blocchi di codice complessi)
- La mappatura potrebbe cambiare dinamicamente durante l'esecuzione
- Volete separare i dati dalla logica
- State costruendo lookup tables o dispatch tables

Considerate questo esempio dove `if` è chiaramente superiore:

```python
# Situazione dove if/elif è più appropriato
temperatura = 28
umidita = 75

# match non può gestire questo tipo di logica composta
if temperatura > 30 and umidita > 70:
    clima = "caldo e umido - disagevole"
elif temperatura > 30:
    clima = "caldo e secco - sopportabile"
elif temperatura < 10 and umidita > 70:
    clima = "freddo e umido - sgradevole"
elif temperatura < 10:
    clima = "freddo e secco - frizzante"
else:
    clima = "temperature moderate - confortevole"

print(f"Condizioni: {clima}")
```

Non esiste modo sensato di esprimere questa logica con `match`, perché stiamo valutando condizioni complesse su più variabili, non confrontando un singolo valore con alternative fisse.

## Un'Anticipazione: Pattern Matching Avanzato

Abbiamo esplorato l'uso base di `match`, che già di per sé è uno strumento utile. Tuttavia, `match` è stato progettato per essere molto più potente di un semplice "switch statement". La sua forma completa implementa il "structural pattern matching", che permette di fare matching non solo su valori letterali, ma sulla struttura stessa dei dati.

Senza entrare nei dettagli (che richiedono conoscenze che acquisirete più avanti nel vostro percorso), ecco un assaggio di cosa è possibile:

```python
# Esempio AVANZATO - non preoccupatevi se non capite tutto ora
dati = [1, 2, 3]

match dati:
    case []:
        # Corrisponde a una lista vuota
        print("Lista vuota")
    
    case [primo]:
        # Corrisponde a una lista con esattamente un elemento
        print(f"Un solo elemento: {primo}")
    
    case [primo, secondo]:
        # Corrisponde a una lista con esattamente due elementi
        print(f"Due elementi: {primo} e {secondo}")
    
    case [primo, secondo, terzo]:
        # Corrisponde a una lista con esattamente tre elementi
        print(f"Tre elementi: {primo}, {secondo} e {terzo}")
    
    case [primo, *resto]:
        # Corrisponde a una lista con almeno un elemento
        # 'resto' cattura tutti gli elementi dopo il primo
        print(f"Primo elemento: {primo}, altri: {resto}")
```

Questo esempio mostra pattern che "destrutturano" la lista, estraendo i suoi componenti. Ma questo è solo l'inizio: il pattern matching avanzato può lavorare con dizionari, oggetti personalizzati, e strutture annidate arbitrariamente complesse.

Per ora, è sufficiente sapere che questa funzionalità esiste. Quando avrete maggiore familiarità con strutture dati complesse e programmazione orientata agli oggetti, potrete esplorare questi aspetti più avanzati consultando la documentazione ufficiale di Python.

## Limiti e Considerazioni

È importante comprendere che `match` non è uno strumento universale per sostituire ogni catena `if/elif/else` nel vostro codice. Ha punti di forza specifici e limitazioni altrettanto specifiche.

Il limite principale è che `match` è progettato per confrontare pattern, non per valutare logica booleana arbitraria. Se la vostra condizione include espressioni come "maggiore di", "minore di", "contiene", o combinazioni complesse di condizioni su variabili diverse, `if/elif/else` rimane la scelta corretta.

Inoltre, `match` richiede più righe e più indentazione rispetto a soluzioni equivalenti con dizionari o `if`. Per situazioni semplici, questa verbosità potrebbe non essere giustificata:

```python
# Per una mappatura semplice, un dizionario è più conciso
giorno_settimana = 3
nome_giorno = {0: "Lunedì", 1: "Martedì", 2: "Mercoledì", 
               3: "Giovedì", 4: "Venerdì", 5: "Sabato", 6: "Domenica"}[giorno_settimana]

# Con match sarebbe più verboso senza benefici evidenti
match giorno_settimana:
    case 0:
        nome_giorno = "Lunedì"
    case 1:
        nome_giorno = "Martedì"
    # ... e così via per tutti i giorni
```

## Conclusione: Un Nuovo Strumento nella Cassetta

L'istruzione `match` è una recente aggiunta a Python che fornisce sintassi esplicita per la selezione multipla. Nel suo uso di base, offre un'alternativa chiara e leggibile alle catene `if/elif/else` quando state confrontando una variabile con un insieme di valori fissi.

Python ha funzionato magnificamente per tre decenni senza `match`, e le tecniche tradizionali (condizionali e dizionari) rimangono perfettamente valide e spesso preferibili. `Match` non rende obsolete queste tecniche, ma aggiunge un'opzione in più al vostro arsenale di strumenti.

Mentre progredite nel vostro apprendimento, incontrerete situazioni dove `match` semplificherà il vostro codice rendendolo più espressivo. In altri casi, scoprirete che gli approcci tradizionali rimangono superiori. La saggezza sta nel riconoscere quale strumento è appropriato per quale problema.

Quando sarete pronti a esplorare il pattern matching strutturale avanzato – con i suoi pattern per sequenze, mappature, e oggetti complessi – avrete già una solida base su cui costruire. Per ora, concentratevi sul padroneggiare l'uso base di `match` e, soprattutto, sul riconoscere quando è lo strumento giusto da usare.