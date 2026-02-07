# Pattern Matching in Python: Parte II - Guard Expressions e Pattern Avanzati

## Premessa: Oltre la Selezione Semplice

Nella prima parte abbiamo esplorato l'uso base di `match/case`, scoprendo come questo costrutto permetta di selezionare tra alternative basandoci sul valore esatto di una variabile. Tuttavia, nella programmazione reale le decisioni raramente sono così semplici. Spesso dobbiamo combinare il confronto di valori con condizioni aggiuntive: "se il valore è X *e inoltre* questa condizione è vera, allora...".

È qui che entrano in gioco le **guard expressions** (espressioni di guardia), un meccanismo potente che permette di aggiungere condizioni booleane ai nostri pattern. Questa seconda parte della dispensa esplora questo territorio più avanzato, mantenendo un approccio pratico e focalizzato su quando e perché queste tecniche sono utili.

## Il Problema delle Condizioni Combinate

Immaginate di dover classificare transazioni bancarie non solo in base al tipo di operazione, ma anche in base all'importo. Una transazione di "acquisto" sotto i 50 euro è considerata "minore", mentre sopra quella soglia richiede verifica aggiuntiva. Come gestiremmo questa situazione?

Con un approccio `if/elif/else` tradizionale, la soluzione è diretta:

```python
# Classificazione transazioni con condizioni multiple
tipo_operazione = "acquisto"
importo = 75.00

if tipo_operazione == "acquisto" and importo < 50:
    categoria = "acquisto minore"
    richiede_verifica = False
    print(f"Acquisto di piccolo importo: €{importo:.2f}")

elif tipo_operazione == "acquisto" and importo >= 50:
    categoria = "acquisto maggiore"
    richiede_verifica = True
    print(f"Acquisto significativo: €{importo:.2f} - verifica richiesta")

elif tipo_operazione == "prelievo" and importo < 100:
    categoria = "prelievo standard"
    richiede_verifica = False
    print(f"Prelievo ordinario: €{importo:.2f}")

elif tipo_operazione == "prelievo" and importo >= 100:
    categoria = "prelievo elevato"
    richiede_verifica = True
    print(f"Prelievo importante: €{importo:.2f} - verifica richiesta")

else:
    categoria = "operazione sconosciuta"
    richiede_verifica = True
    print(f"Tipo di operazione non riconosciuto: {tipo_operazione}")
```

Questo codice funziona, ma notate quanta ripetizione c'è: controlliamo `tipo_operazione` ripetutamente, e poi aggiungiamo condizioni su `importo`. Il pattern matching con guard expressions offre un modo più strutturato per esprimere questa logica.

## Le Guard Expressions: Aggiungere Condizioni ai Pattern

Una guard expression è una condizione booleana aggiuntiva che si aggiunge a un pattern usando la parola chiave `if` *dopo* il pattern stesso. La sintassi è:

```python
match variabile:
    case pattern if condizione:
        # Questo blocco viene eseguito solo se:
        # 1. Il pattern corrisponde, E
        # 2. La condizione è vera
```

È fondamentale comprendere l'ordine delle operazioni: prima Python verifica se il pattern corrisponde, e solo se corrisponde valuta la guard expression. Se la guard è falsa, Python passa al `case` successivo.

Riscriviamo l'esempio precedente usando guard expressions:

```python
# Stesso problema risolto con match e guard expressions
tipo_operazione = "acquisto"
importo = 75.00

match tipo_operazione:
    case "acquisto" if importo < 50:
        categoria = "acquisto minore"
        richiede_verifica = False
        print(f"Acquisto di piccolo importo: €{importo:.2f}")
    
    case "acquisto" if importo >= 50:
        categoria = "acquisto maggiore"
        richiede_verifica = True
        print(f"Acquisto significativo: €{importo:.2f} - verifica richiesta")
    
    case "prelievo" if importo < 100:
        categoria = "prelievo standard"
        richiede_verifica = False
        print(f"Prelievo ordinario: €{importo:.2f}")
    
    case "prelievo" if importo >= 100:
        categoria = "prelievo elevato"
        richiede_verifica = True
        print(f"Prelievo importante: €{importo:.2f} - verifica richiesta")
    
    case _:
        categoria = "operazione sconosciuta"
        richiede_verifica = True
        print(f"Tipo di operazione non riconosciuto: {tipo_operazione}")
```

Questo approccio rende più esplicita la struttura della decisione: stiamo facendo matching su `tipo_operazione`, e poi per ciascun tipo applichiamo condizioni ulteriori basate su `importo`. La logica è più stratificata e leggibile.

## Guard con Cattura di Valori

Le guard expressions diventano particolarmente potenti quando combinate con la cattura di valori tramite `as` o variabili semplici:

```python
# Sistema di classificazione messaggi con priorità dinamica
messaggio = "errore"
livello_gravita = 8  # Scala 0-10

match messaggio:
    case "info" | "debug" as tipo:
        # Questi sono sempre a bassa priorità
        priorita = "bassa"
        print(f"Messaggio {tipo}: priorità {priorita}")
    
    case "warning" as tipo if livello_gravita < 5:
        # Warning leggero
        priorita = "media"
        print(f"Attenzione {tipo} (gravità {livello_gravita}): priorità {priorita}")
    
    case "warning" as tipo if livello_gravita >= 5:
        # Warning serio
        priorita = "alta"
        print(f"Attenzione critica {tipo} (gravità {livello_gravita}): priorità {priorita}")
    
    case "errore" as tipo if livello_gravita >= 7:
        # Errore grave
        priorita = "critica"
        print(f"ERRORE CRITICO {tipo} (gravità {livello_gravita}): priorità {priorita}")
        invia_alert_amministratori()
    
    case "errore" as tipo:
        # Errore gestibile
        priorita = "alta"
        print(f"Errore {tipo} (gravità {livello_gravita}): priorità {priorita}")
    
    case altro:
        priorita = "media"
        print(f"Tipo messaggio sconosciuto: {altro}")

# La variabile 'tipo' è disponibile dopo il match se è stata assegnata
print(f"Ultimo tipo processato: {tipo}")
```

In questo esempio, catturiamo il tipo di messaggio nella variabile `tipo`, che poi usiamo sia nella guard expression che nel corpo del case. Questo elimina ripetizioni e rende il codice più manutenibile.

## Guard con Condizioni Complesse

Le guard expressions possono contenere qualsiasi espressione booleana valida, comprese condizioni multiple combinate con `and`, `or`, e `not`:

```python
# Sistema di autorizzazione per operazioni sensibili
operazione = "modifica_database"
utente_autorizzato = True
orario_lavoro = True
connessione_sicura = False

match operazione:
    case "lettura":
        # La lettura è sempre permessa
        permesso = True
        print("Operazione di lettura: accesso consentito")
    
    case "modifica_database" if utente_autorizzato and orario_lavoro and connessione_sicura:
        # Tutte le condizioni di sicurezza devono essere soddisfatte
        permesso = True
        print("Modifica database autorizzata")
        registra_audit_log(operazione, "consentita")
    
    case "modifica_database" if not connessione_sicura:
        # Caso specifico: connessione non sicura
        permesso = False
        print("ACCESSO NEGATO: richiesta connessione sicura (HTTPS/VPN)")
        registra_audit_log(operazione, "negata - connessione insicura")
    
    case "modifica_database" if not utente_autorizzato:
        # Caso specifico: utente non autorizzato
        permesso = False
        print("ACCESSO NEGATO: privilegi insufficienti")
        registra_audit_log(operazione, "negata - privilegi insufficienti")
    
    case "modifica_database":
        # Tutte le altre ragioni (es: fuori orario)
        permesso = False
        print("ACCESSO NEGATO: operazione non permessa in questo momento")
        registra_audit_log(operazione, "negata - fuori orario")
    
    case "eliminazione" if utente_autorizzato:
        # L'eliminazione richiede solo autorizzazione, ma mostra warning
        permesso = True
        print("ATTENZIONE: operazione di eliminazione - procedere con cautela")
        richiedi_conferma_esplicita()
    
    case _:
        permesso = False
        print(f"Operazione non riconosciuta: {operazione}")
```

Notate come i `case` per "modifica_database" siano ordinati strategicamente: il primo richiede tutte le condizioni, i successivi catturano specifiche ragioni di fallimento, e l'ultimo è un catch-all per qualsiasi altro caso.

## L'Ordine dei Case: Importanza Cruciale con le Guard

Quando usiamo guard expressions, l'ordine dei `case` diventa estremamente importante. Python valuta i case dall'alto verso il basso e si ferma al primo che corrisponde completamente (pattern + guard). Questo significa che dovete pensare attentamente a come ordinare i vostri case.

Considerate questo esempio problematico:

```python
# ESEMPIO PROBLEMATICO - ordine sbagliato!
temperatura = 25

match True:  # Trucco per usare match come if/elif avanzato
    case _ if temperatura > 0:
        # Questo caso cattura TUTTE le temperature positive
        clima = "sopra zero"
    
    case _ if temperatura > 15:
        # Questo non verrà MAI raggiunto!
        # Perché temperature > 15 sono già catturate dal caso precedente
        clima = "mite"
    
    case _ if temperatura > 25:
        # Anche questo non verrà mai raggiunto!
        clima = "caldo"

print(clima)  # Stamperà sempre "sopra zero" per temp > 0
```

La versione corretta ordina i case dal più specifico al più generale:

```python
# VERSIONE CORRETTA - ordine dal più specifico al più generale
temperatura = 25

match True:
    case _ if temperatura > 30:
        clima = "molto caldo"
        raccomandazione = "Evitare attività fisica intensa"
    
    case _ if temperatura > 25:
        clima = "caldo"
        raccomandazione = "Mantenersi idratati"
    
    case _ if temperatura > 15:
        clima = "mite"
        raccomandazione = "Temperatura piacevole"
    
    case _ if temperatura > 0:
        clima = "fresco"
        raccomandazione = "Portare una giacca leggera"
    
    case _ if temperatura > -10:
        clima = "freddo"
        raccomandazione = "Abbigliamento invernale necessario"
    
    case _:
        clima = "gelido"
        raccomandazione = "Evitare esposizione prolungata"

print(f"{clima}: {raccomandazione}")
```

## Il Pattern `match True`: Usare match come if/elif Potenziato

Avete notato il trucco `match True` nell'esempio precedente? Questo è un idioma interessante che permette di usare `match` essenzialmente come una catena `if/elif/else` dove ogni condizione può essere completamente diversa.

Funziona così: facciamo matching su `True`, e poi ogni guard expression diventa effettivamente la vera condizione. Il pattern `_` corrisponde sempre (anche a `True`), quindi la guard determina se quel case viene eseguito.

Ecco un esempio pratico:

```python
# Validazione complessa di dati utente
username = "alice"
password = "Secure123!"
eta = 17
accetta_termini = True

match True:
    case _ if not username:
        errore = "Username obbligatorio"
        valido = False
    
    case _ if len(username) < 3:
        errore = "Username troppo corto (minimo 3 caratteri)"
        valido = False
    
    case _ if not password:
        errore = "Password obbligatoria"
        valido = False
    
    case _ if len(password) < 8:
        errore = "Password troppo corta (minimo 8 caratteri)"
        valido = False
    
    case _ if not any(c.isupper() for c in password):
        errore = "Password deve contenere almeno una maiuscola"
        valido = False
    
    case _ if not any(c.isdigit() for c in password):
        errore = "Password deve contenere almeno un numero"
        valido = False
    
    case _ if eta < 18:
        errore = "Devi avere almeno 18 anni per registrarti"
        valido = False
    
    case _ if not accetta_termini:
        errore = "Devi accettare i termini e condizioni"
        valido = False
    
    case _:
        errore = None
        valido = True
        print("Registrazione completata con successo!")

if not valido:
    print(f"Errore di validazione: {errore}")
```

Questa tecnica è particolarmente utile quando avete una serie di controlli di validazione da eseguire in sequenza, fermandovi al primo che fallisce.

## Quando Usare Guard: Confronto con if/elif/else

Ora che conosciamo le guard expressions, quando dovremmo usarle invece del classico `if/elif/else`? Ecco alcune linee guida pratiche.

### Scenario 1: Selezione su Valore + Condizione Aggiuntiva

**Usate match con guard quando** avete una selezione basata su un valore che poi richiede condizioni aggiuntive:

```python
# BUON CASO PER MATCH/GUARD
stato_ordine = "spedito"
giorni_trascorsi = 12

match stato_ordine:
    case "spedito" if giorni_trascorsi <= 3:
        messaggio = "Ordine spedito di recente, arrivo previsto a breve"
        azione = "nessuna"
    
    case "spedito" if giorni_trascorsi <= 7:
        messaggio = "Spedizione in corso, arrivo previsto entro 2 giorni"
        azione = "nessuna"
    
    case "spedito" if giorni_trascorsi > 7:
        messaggio = "Ritardo nella spedizione"
        azione = "contatta_corriere"
    
    case "in_preparazione" if giorni_trascorsi > 3:
        messaggio = "Ordine in preparazione da troppo tempo"
        azione = "verifica_magazzino"
    
    case "annullato":
        messaggio = "Ordine annullato"
        azione = "nessuna"
    
    case _:
        messaggio = f"Stato sconosciuto: {stato_ordine}"
        azione = "contatta_supporto"
```

**Preferite if/elif/else quando** non c'è una variabile centrale su cui fate matching:

```python
# MEGLIO CON IF/ELIF - non c'è una variabile "centrale"
temperatura = 28
umidita = 75
vento = 15

if temperatura > 30 and umidita > 70:
    comfort = "molto disagevole"
elif temperatura > 25 and vento < 10:
    comfort = "caldo e stagnante"
elif temperatura < 15 and vento > 20:
    comfort = "freddo e ventoso"
elif 18 <= temperatura <= 24 and umidita < 60:
    comfort = "ideale"
else:
    comfort = "accettabile"
```

### Scenario 2: Validazione a Cascata

**Match con guard può essere elegante per validazioni sequenziali:**

```python
# Validazione configurazione sistema
config = {"debug": True, "port": 8080, "max_connections": 500}

match True:
    case _ if "port" not in config:
        errore = "Porta non specificata"
        
    case _ if config["port"] < 1024:
        errore = "Porta riservata (< 1024) - richiede privilegi amministratore"
    
    case _ if config["port"] > 65535:
        errore = "Porta non valida (> 65535)"
    
    case _ if "max_connections" not in config:
        errore = "Numero massimo connessioni non specificato"
    
    case _ if config["max_connections"] < 1:
        errore = "Il numero di connessioni deve essere positivo"
    
    case _ if config["max_connections"] > 10000:
        errore = "Troppo connessioni configurate (max 10000)"
    
    case _:
        errore = None
        print("Configurazione valida")

if errore:
    print(f"Errore configurazione: {errore}")
    usa_configurazione_predefinita()
```

**Ma if/elif è spesso più chiaro per validazioni semplici:**

```python
# Validazione semplice - if/elif è più diretto
valore = 150

if valore < 0:
    print("Errore: valore negativo non ammesso")
elif valore > 100:
    print("Errore: valore massimo 100")
else:
    print("Valore valido")
    elabora(valore)
```

### Scenario 3: Combinazione Tipo + Proprietà

**Match eccelle quando combinate tipo di dato con sue proprietà:**

```python
# Gestione risposte API che possono essere di tipi diversi
risposta = {"status": "error", "code": 404, "message": "Not found"}

match risposta:
    case {"status": "success", "data": dati}:
        print(f"Operazione riuscita, dati: {dati}")
        elabora_dati(dati)
    
    case {"status": "error", "code": codice} if codice < 500:
        print(f"Errore client (codice {codice}): {risposta.get('message', 'Errore sconosciuto')}")
        gestisci_errore_client(codice)
    
    case {"status": "error", "code": codice} if codice >= 500:
        print(f"Errore server (codice {codice}): {risposta.get('message', 'Errore sconosciuto')}")
        riprova_richiesta()
    
    case _:
        print(f"Formato risposta non riconosciuto: {risposta}")
```

## Pattern Avanzati con Guard: Un Assaggio

Anche se lo structural pattern matching completo richiede conoscenze che acquisirete più avanti, vale la pena vedere un esempio di come le guard si combinano con pattern più complessi:

```python
# Analisi comandi con parametri
comando = ["copia", "documento.txt", "/backup/"]

match comando:
    case ["copia", sorgente, destinazione] if sorgente.endswith(".txt"):
        print(f"Copia file di testo {sorgente} in {destinazione}")
        tipo_copia = "testo"
    
    case ["copia", sorgente, destinazione] if sorgente.endswith((".jpg", ".png")):
        print(f"Copia immagine {sorgente} in {destinazione}")
        tipo_copia = "immagine"
    
    case ["copia", sorgente, destinazione]:
        print(f"Copia generica di {sorgente} in {destinazione}")
        tipo_copia = "generico"
    
    case ["elimina", file] if file.startswith("/backup/"):
        print(f"Eliminazione da backup: {file}")
        richiedi_conferma = True
    
    case ["elimina", file]:
        print(f"Eliminazione: {file}")
        richiedi_conferma = False
    
    case [operazione, *argomenti]:
        print(f"Comando '{operazione}' con {len(argomenti)} argomenti")
        print(f"Argomenti: {argomenti}")
    
    case _:
        print("Comando non riconosciuto")
```

Questo esempio mostra come le guard permettono di raffinare pattern che già destrutturano dati complessi. Il pattern `["copia", sorgente, destinazione]` estrae i componenti del comando, e la guard verifica ulteriori proprietà di quegli elementi.

## Limitazioni e Insidie delle Guard

Le guard expressions, per quanto potenti, hanno alcune limitazioni che è importante conoscere:

### 1. Le Guard Non Possono Modificare Stato

Le guard devono essere espressioni pure che valutano a vero o falso. Non dovrebbero avere effetti collaterali:

```python
# ANTI-PATTERN - non fare questo!
contatore = 0

match valore:
    case x if (contatore := contatore + 1) > 3:  # Brutto!
        # Modificare stato nella guard è confuso e propenso a errori
        pass
```

### 2. Ordine dei Case Critico

Come abbiamo visto, l'ordine conta. Guard più specifiche devono venire prima di quelle più generali.

### 3. Prestazioni con Guard Complesse

Guard vengono valutate in sequenza fino a trovare corrispondenza. Se avete molti case con guard computazionalmente costose, potreste avere problemi di performance:

```python
# Potenzialmente lento se la lista è lunga
match True:
    case _ if elemento in lista_lunghissima:  # Ricerca O(n)
        # Se questo è il primo case, viene sempre eseguita
        pass
```

### 4. Debugging Più Complesso

Quando un match con guard non si comporta come previsto, può essere più difficile capire perché rispetto a un semplice `if`:

```python
# Quale case corrisponde? Dipende da stato_sistema E dalle guard!
match stato_sistema:
    case "attivo" if condizione_complessa_1():
        pass
    case "attivo" if condizione_complessa_2():
        pass
    case "attivo":
        pass
```

## Conclusione: Quando le Guard Hanno Senso

Le guard expressions aggiungono flessibilità al pattern matching, permettendovi di combinare la selezione basata su pattern con condizioni booleane arbitrarie. Sono particolarmente utili quando:

1. **State facendo matching su un valore centrale** ma avete bisogno di condizioni aggiuntive basate su altre variabili
2. **Volete esprimere validazioni a cascata** in modo strutturato
3. **State combinando pattern destrutturanti con verifiche sulle parti estratte**

Tuttavia, non sono sempre la soluzione migliore:

1. **Per logica completamente condizionale** (nessun valore centrale), `if/elif/else` rimane più chiaro
2. **Per validazioni semplici**, `if/elif/else` è più conciso
3. **Quando l'ordine dei case diventa confuso**, probabilmente `if/elif/else` è più manutenibile

Il pattern `match True` con guard è un idioma interessante che trasforma `match` in una specie di `if/elif/else` potenziato, utile per validazioni sequenziali dove volete fermarvi alla prima condizione che fallisce.

Come sempre in programmazione, il miglior strumento dipende dal contesto specifico. Le guard sono un'opzione in più nel vostro arsenale, non una sostituzione universale per tecniche esistenti. Usatele quando rendono il vostro codice più chiaro e manutenibile, non semplicemente perché sono disponibili.

Quando progredite e iniziate a lavorare con strutture dati più complesse, scoprirete che le guard diventano ancora più potenti in combinazione con il pattern matching strutturale completo. Ma questa è una storia per un altro capitolo del vostro percorso di apprendimento.