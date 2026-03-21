# Sistema di Gestione Personaggi RPG

**Versione:** 1.0 (Prima implementazione)  
**Concetti Applicati:** Classi, Ereditarietà, Composizione, Incapsulamento  
**Linguaggio:** Python 3.x  

---

## 🎯 Obiettivo Generale

Questo progetto rappresenta il primo esercizio significativo di programmazione orientata agli oggetti nel mio percorso di apprendimento. L'obiettivo è c consolidare la comprensione di come le classi permettono di modellare il mondo reale in modo strutturato, come l'ereditarietà legittima il riuso di codice, e come la composizione (object nesting) permette di costruire sistemi complessi da componenti semplici. Nel contesto di un gioco di ruolo, gestire personaggi significa rappresentare entità che hanno proprietà (attributi) e comportamenti (metodi).

---

## 📚 Contesto Teorico

### Classi come Modelli di Realtà

Una classe è un blueprint, uno stampo. Proprio come uno stampo per biscotti definisce la forma che avranno tutti i biscotti prodotti, una classe definisce la struttura che avranno tutte le istanze (gli oggetti concreti) create a partire da essa.

Nella pratica, quando definisco una classe `Guerriero`, sto dicendo: "Ogni guerriero ha un nome, punti vita, un livello, e una forza. Ogni guerriero sa come descriversi, ricevere danno, e attaccare." Quando creo un'istanza (`guerriero_1 = Guerriero("Aragorn", 100, 1, 15)`), sto creando un'incarnazione concreta di quel concetto.

### Ereditarietà: Specializzazione e Riuso

L'ereditarietà risolve un problema comune nella programmazione: evitare la duplicazione di codice. Se ho una classe `Personaggio` che gestisce nome, punti vita, e livello (cose comuni a tutti i personaggi), posso far ereditare `Guerriero` da `Personaggio` piuttosto che riscrivere quegli stessi attributi e metodi.

L'ereditarietà crea una relazione di specializzazione: un `Guerriero` *è un* `Personaggio` (con proprietà aggiuntive come la forza). Una `Maga` potrebbe essere un altro `Personaggio` specializzato (con intelligenza invece che forza). Entrambi ereditano dai metodi comuni, ma ciascuno aggiunge comportamenti propri.

### Composizione: Aggregazione di Responsabilità

La composizione è diversa dall'ereditarietà. Mentre l'ereditarietà dice "è un tipo di", la composizione dice "ha un". Un `Guerriero` *ha un* `Inventario`. Questa distinzione è critica per scrivere codice manutenibile.

La composizione è il principio che preferisco quando ho dubbi. Permette di separare responsabilità: la classe `Inventario` sa come aggiungere, rimuovere e mostrare oggetti. La classe `Guerriero` sa come combattere, ricevere danno, e interagire con il suo inventario – ma non reimplementa la logica di gestione inventario (quella la delega all'oggetto `Inventario` interno).

In questo esercizio, ogni `Guerriero` ha il proprio `Inventario` indipendente. Questo è il comportamento atteso: se creo due guerrieri, ciascuno deve avere il suo zaino personale, non condividere lo stesso zaino. Il rischio di errore qui è una "trappola" comune di Python: usare liste come attributi di default della classe, che vengono condivise accidentalmente tra le istanze.

---

## 🏗️ Struttura del Progetto

### Classe Base: `Personaggio`

La classe `Personaggio` è l'astrazione comune. Rappresenta le proprietà e i comportamenti condivisi da tutti i personaggi del gioco.

**Attributi:**
- `nome` (str): Identificativo del personaggio
- `punti_vita` (int): Risorsa centrale che decresce quando il personaggio riceve danno
- `livello` (int): Rappresenta esperienza/forza complessiva

**Metodi:**
- `descrivi()`: Stampa una rappresentazione leggibile dello stato del personaggio
- `subisci_danno(quantita)`: Riduce i punti vita. Implementazione importante: i punti vita non devono mai diventare negativi. Se il danno sarebbe 50 e ho 30 vita, termino a 0, non a -20.
- `e_vivo()`: Ritorna un booleano che verifica se il personaggio è ancora in combattimento (punti_vita > 0)

La logica "difensiva" (proteggere l'invariante che vita >= 0) deve vivere dentro il metodo `subisci_danno()`. Non dovrei permettere che nessun'altra parte del codice riduca direttamente `self.punti_vita` senza controllo.

### Classe di Composizione: `Inventario`

L'`Inventario` non eredita da nulla. È una classe di utilità che gestisce una sola responsabilità: contenere e manipolare una lista di oggetti.

**Attributi:**
- `oggetti` (list): La lista degli oggetti fisici custoditi
- `capacita_massima` (int): Il limite di quanti oggetti possono essere immagazzinati

**Metodi:**
- `aggiungi(oggetto)`: Aggiunge un oggetto alla lista se c'è spazio. Ritorna `True` se l'aggiunta è riuscita, `False` se l'inventario è pieno. Questa semantica di ritorno booleano permette al chiamante di reagire al fallimento.
- `rimuovi(oggetto)`: Rimuove l'oggetto dalla lista. Cosa fare se l'oggetto non esiste? Due scelte: sollevare un'eccezione (esplicita, ma interrompe il flusso) o ritornare un booleano (permissivo, ma richiede che il chiamante verifichi il risultato). Per semplicità iniziale, consiglio ritornare booleano.
- `mostra()`: Stampa a console il contenuto dell'inventario in formato leggibile

### Classe Derivata: `Guerriero`

`Guerriero` eredita da `Personaggio`, il che significa che eredita automaticamente nome, punti_vita, livello, e tutti i metodi della classe base.

**Attributi Aggiuntivi:**
- `forza` (int): Un numero che rappresenta il potere offensivo del guerriero
- Un'istanza di `Inventario` per custodire equipaggiamento

**Metodo Speciale:**
- `attacco_pesante(nemico)`: Il guerriero attacca il nemico usando la sua forza. Il danno inflitto è una funzione della forza (esempio: `danno = forza * 1.5 + numero_casuale`). Dopo il calcolo, chiama il metodo `nemico.subisci_danno(danno)`.

La scelta di chiamare il metodo del nemico piuttosto che modificare direttamente `nemico.punti_vita` è cruciale. Permette al nemico di mantenere il controllo sulla validazione dei dati (non scendere sotto zero) senza dover fidarsi che l'attaccante lo faccia.

---

## 💻 Esecuzione e Logica Principale

Lo script deve essere **eseguibile direttamente** e **importabile senza effetti collaterali**.

Questo significa usare il pattern:

```python
if __name__ == "__main__":
    # Codice che crea guerrieri, simula battaglia, stampa risultati
    pass
```

Se qualcuno importa il modulo in un altro script, il codice di test non si esegue automaticamente. Se lancio il file direttamente, il test gira.

### Scenario Simulato

1. Creo due guerrieri distinti
2. Simulo una battaglia: a turni, uno attacca l'altro
3. Durante il combattimento, do equipaggiamento ai guerrieri via inventario
4. Stampo lo stato finale: chi è ancora vivo, che oggetti ha, quanti punti vita rimangono

---

## ✅ Checklist di Qualità

Prima di considerare il progetto completato, devo verificare:

### Documentazione

- [ ] **Docstring della classe `Personaggio`**: Descrivo lo scopo, gli attributi fondamentali, il comportamento atteso
- [ ] **Docstring della classe `Inventario`**: Spiego la responsabilità della classe e il limite di capacità
- [ ] **Docstring della classe `Guerriero`**: Descrivere come specializza `Personaggio`, il ruolo della forza
- [ ] **Docstring di ogni metodo pubblico**: Una o due righe che spiegano input, output, e comportamento collaterale importante
- [ ] **Commenti in-line dove necessario**: Particolarmente per la logica di attacco e il controllo dei punti vita

### Sicurezza Dati

- [ ] **Punti vita invariante**: Nessuna operazione può rendere `punti_vita` negativo. Test manuale: creo un personaggio, chiamo `subisci_danno(1000)`, verifico che vita sia 0, non -900
- [ ] **Inventario indipendente**: Creo due guerrieri senza argomenti, modifico l'inventario di uno, verifico che l'altro non sia stato affettato

### Leggibilità

- [ ] **Nomi significativi**: Evito `lista`, `dati`, `temp`. Uso `oggetti`, `danno_inflitto`, `nemico`
- [ ] **Coerenza di naming**: Se uso `guerriero_1` in un posto, non uso `g1` in un altro
- [ ] **Linee non troppo lunghe**: Max 88 caratteri (PEP8 soft limit)
- [ ] **Funzioni/metodi non troppo lunghi**: Se un metodo è > 20 righe, probabilmente faccio troppo in un posto solo

### Incapsulamento

- [ ] **Preferisco metodi a accesso diretto**: Se devo aggiungere un oggetto all'inventario, chiamo `guerriero.inventario.aggiungi(oggetto)`, non `guerriero.inventario.oggetti.append(oggetto)`. Questo "distanza" il codice dalla struttura interna
- [ ] **Logica di validazione centralizzata**: I controlli (non negativi, non oltre capacità) vivono dentro i metodi, non sparse nel codice client

---

## 📝 Note di Implementazione

### Evoluzione del Codice

Questa è una **prima versione**. Saranno probabilmente necessari refactoring futuri:

- **Versione 1.0 (Attuale):** Classi base, ereditarietà semplice, composizione con Inventario, battaglia turno-per-turno
- **Versione 1.1 (Possibile):** Aggiungere una classe `Oggetto` per rappresentare gli item specificamente (non solo stringhe), aggiungere effetti come "spada che aumenta danno" o "armatura che riduce danno ricevuto"
- **Versione 2.0 (Futura):** Sistema di maghi con mana, classi diverse (Paladino, Ranger), meccaniche di schivata/blocco

Per adesso, rimango semplice: gli oggetti sono stringhe ("spada", "scudo"), e l'inventario è solo contenitore.

---

## 🔄 Prossimi Passi

Dopo aver completato questo progetto con i requisiti di base, posso:

1. **Code Review Personale**: Rileggo il codice come se l'avesse scritto qualcun altro. Cerco:
   - Logica offuscata
   - Nomi ambigui
   - Duplicazione di codice
   - Edge case non gestiti (cosa succede se danno è 0? Se inventario è pieno?)

2. **Estensioni**: Aggiungo funzionalità:
   - Metodo `__str__()` per stampare il personaggio in modo naturale (`print(guerriero)` invece di `print(guerriero.descrivi())`)
   - Sistema di armatura che riduce il danno ricevuto
   - Punti energia che limitano quanti attacchi pesanti posso fare

3. **Integrazione con Progetti Precedenti**: Se ho fatto esercizi su liste/dizionari, posso salvare lo stato della battaglia su file JSON, o caricarlo.

---

## 📖 Riferimenti nei Miei Studi

Questo esercizio consolida concetti dei capitoli 8 e 9 di Python Crash Course:
- **Capitolo 8 (Funzioni):** Le funzioni come astrazione
- **Capitolo 9 (Classi):** Classi, eredità, composizione, `__init__()`, metodi di istanza

Vedi anche **Block 11 (OOP)** nel Piano di Apprendimento per approfondimenti teorici.

---

**Versione:** 1.0  
**Ultimo aggiornamento:** 18 Marzo 2026