# Git e GitHub: Guida Completa per Principianti

## Introduzione: Il Problema che Git Risolve

Immagina di stare lavorando a un progetto importante. Modifichi un file, poi un altro. Dopo un'ora ti rendi conto di aver commesso un errore grave e vorresti tornare indietro. Ma come? Il pulsante "annulla" di Windows va solo indietro di pochi passi. Se hai spento il computer e riaperto il progetto il giorno dopo, il danno è fatto.

Oppure immagina di lavorare con altre persone. Tutti modificano gli stessi file. Come farete a sapere chi ha fatto cosa? Come eviterete che le modifiche di una persona sovrascrivano quelle di un'altra? Come terrete traccia delle versioni diverse del progetto?

Questi problemi sono esattamente quello che **Git** risolve. Git è un sistema di **version control**: un software che tiene traccia di tutte le modifiche ai tuoi file nel tempo, permettendoti di tornare a qualsiasi versione precedente del tuo lavoro, e facilitando la collaborazione tra più persone su progetti condivisi.

La bellezza di Git è che funziona completamente **localmente** sul tuo computer. Non richiede una connessione internet per registrare la storia del tuo lavoro. Puoi continuare a lavorare anche offline, e sincronizzarti con i tuoi collaboratori quando la connessione ritorna disponibile.

## GitHub: Il Cloud per il Tuo Codice

Mentre Git è uno strumento che vive sul tuo computer, **GitHub** è una piattaforma online che completa l'ecosistema. GitHub è un servizio web dove puoi ospitare i tuoi repository Git nel cloud. Se Git è il motore, GitHub è la stazione di servizio.

GitHub appartiene a Microsoft (acquisita nel 2018) ed è diventata la piattaforma standard dell'industria per lo sviluppo di software. È gratuita per uso personale, anche se opti per repository privati che solo tu puoi vedere. Milioni di sviluppatori usano GitHub non solo per collaborare, ma anche come portfolio pubblico del proprio lavoro.

La piattaforma offre molto più di un semplice spazio di storage. Ti permette di esplorare il codice di altri sviluppatori, di contribuire a progetti open source, di ricevere feedback sul tuo lavoro attraverso le "pull request": un meccanismo formale di revisione del codice. Per un principiante, GitHub può sembrare un "GitHub che host il tuo codice", ma col tempo comprenderai che è un ecosistema completo di sviluppo collaborativo.

## Repository: Il Cuore di Git

Un **repository** è il concetto centrale di Git. Un repository è semplicemente una cartella di progetto che Git sta tracciando. Contiene i tuoi file attuali, plus una cartella nascosta `.git` che Git usa per archiviare tutta la storia del progetto.

Quando crei un repository su GitHub e poi lo "cloni" (scaricare una copia) sul tuo computer, Git crea questa cartella `.git`. Dentro questa cartella trovate:

- L'intera storia di tutte le modifiche fatte al progetto
- I metadati su chi ha fatto cosa e quando
- Le configurazioni specifiche per il repository
- Il collegamento al repository remoto su GitHub

Un aspetto importante da comprendere è che il repository locale (quello sul tuo computer) e il repository remoto (quello su GitHub) sono sincronizzati, ma indipendenti. Puoi lavorare completamente offline e poi "spingere" il tuo lavoro (push) su GitHub quando sei pronto. E puoi "tirare" il lavoro degli altri (pull) da GitHub quando vuoi sincronizzarti con le loro modifiche.

## Installazione di Git su Windows 11

Git non viene preinstallato su Windows, quindi dobbiamo installarlo. Il processo è semplice ma merita una spiegazione attenta per evitare passi falsi.

### Scaricare l'Installer

Visita il sito ufficiale di Git all'indirizzo https://git-scm.com. Noterai che il sito automaticamente riconosce che stai usando Windows e ti mostra il link per scaricare l'installer per Windows. Clicca il pulsante di download.

Verrà scaricato un file `.exe` (in questo momento probabilmente `Git-for-Windows-2.x.x.exe`, ma il numero di versione cambierà nel tempo).

### Eseguire l'Installer

Una volta scaricato, fai doppio click sul file `.exe`. Windows potrebbe chiederti se consenti a questo programma di modificare il tuo computer — clicca "Sì" per procedere.

L'installer vi guidera attraverso una serie di opzioni. Per la stragrande maggioranza dei principianti, le scelte predefinite sono perfette. Lasciate tutto com'è e continuate a cliccare "Next" fino alla fine. Un'eccezione: nella schermata che domanda quale editor usare, assicuratevi che sia selezionato un editor riconoscibile (come Notepad o Visual Studio Code, se l'avete installato). Se foste avventurosi e installaste Git prima di conoscere questi editor, semplicemente ignorate — potete cambiare l'editor predefinito di Git in qualsiasi momento.

### Verificare l'Installazione

Una volta completato l'installer, apri PowerShell. In Windows 11, il metodo più veloce è premere il tasto Windows e digitare "PowerShell", poi premere Enter.

Una volta aperto PowerShell, digita il seguente comando:

```powershell
git --version
```

Se vedi una risposta che dice qualcosa come `git version 2.42.0.windows.1`, significa che Git è stato installato correttamente. Se vedete un errore che dice "git is not recognized", potrebbe significare che PowerShell non ha aggiornato il percorso del sistema dopo l'installazione. In questo caso, chiudete PowerShell completamente e riaprilo — Windows aggiornerà automaticamente il percorso.

## Il Concetto di Identità in Git: Perché è Fondamentale

Questo è il punto che causa più confusione nei principianti, quindi merita una spiegazione dettagliata. Quando usate Git, ogni modifica che farete (ogni "commit", di cui parleremo) sarà firmata con un'identità. Questa identità serve a rispondere a domande cruciali: chi ha fatto questa modifica? Quando? Perché?

### Perché Git Vuole Sapere Chi Sei

Git è stato creato nel 2005 da Linus Torvalds per gestire il codice del kernel Linux — un progetto con migliaia di sviluppatori in tutto il mondo che contribuivano cambiamenti. Era essenziale sapere, per ogni singola riga di codice, chi l'aveva scritta e quando.

Pensateci: se voi e un vostro collega state modificando lo stesso file, e trovate un bug più tardi, chi l'ha introdotto? Se Git non sapesse chi ha fatto cosa, sarebbe impossibile risalire responsabilità. Ma se Git sa che il collega ha aggiunto una certa riga il 15 gennaio alle 14:30, potete contattarlo e dire "ehi, il codice che hai aggiunto così causa un problema".

Allo stesso modo, in un progetto open source pubblico, quando qualcuno pubblica codice su GitHub, il suo nome appare come autore di quel codice. È una forma di attribuzione. È come firmare una lettera, solo digitale.

### Il Nome vs L'Email

Quando configurate Git, gli darete due informazioni: un nome e un'email. Potrebbe sembrare strano che Git voglia un'email — dopotutto, non la usa per inviarvi messaggi. L'email serve per un'altra ragione.

L'email è l'identificativo **globale** di una persona in git. Se voi usate il nome "Andrea", potrebbe esserci un'altra persona nel mondo chiamata Andrea che usa Git. Ma la probabilità che due persone abbiano esattamente la stessa email è molto bassa. L'email garantisce unicità.

Inoltre, se un giorno pubblicate il vostro codice su GitHub, GitHub vuole collegare il codice al vostro account GitHub, e fa ciò matchando l'email che usate nel vostro Git locale con l'email registrata sul vostro profilo GitHub. Se le email non corrispondo, GitHub non sa che siete voi. Il vostro commit apparirà come firmato da "Andrea (andrea@example.com)" anziché mostrare il vostro avatar e il vostro profilo GitHub.

### Quale Email Usare?

Qui arriviamo al punto che probabilmente state chiedendovi. Dovreste usare l'email registrata su GitHub — la stessa email con cui vi siete iscritti alla piattaforma.

Perché? Perché quando spingete il vostro codice su GitHub (operazione che faremo più tardi), GitHub esamina l'email nel vostro commit e la confronta con le email associate al vostro account. Se corrispondo, GitHub sa che il commit viene da voi e mostra il vostro profilo, il vostro avatar, la vostra storia di contributi. Se non corrispondo, il commit apparirà come fatto da un utente sconosciuto.

Questo è particolarmente importante per il vostro "GitHub contributions graph" — quella griglia colorata sul vostro profilo che mostra quando avete lavorato. Se l'email non corrisponde, il contributo non conta verso la vostra statistica.

### Come Sapere Quale Email È Registrata su GitHub

Se non siete sicuri quale email usate su GitHub, potete scoprirlo facilmente. Andate su GitHub.com e cliccate la vostra immagine profilo in alto a destra. Cliccate "Settings". Nel menu a sinistra, cliccate "Emails". Vedrete l'email primaria associata al vostro account. Usate quella.

## Configurazione Iniziale di Git su Windows

Ora che sapete perché Git vuole conoscere la vostra identità, configuriamola. Aprite PowerShell (Windows + digitate "PowerShell" + Enter).

### Impostare il Nome

Digitate il seguente comando, sostituendo "Il Vostro Nome" con il vostro nome reale (può essere il vostro nome completo, o un nickname, non importa):

```powershell
git config --global user.name "Il Vostro Nome"
```

Premete Enter. Non vedrete alcun messaggio di conferma — se non vedete errori, significa che il comando ha funzionato.

### Impostare l'Email

Ora digitate:

```powershell
git config --global user.email "tua-email@github.com"
```

Ancora una volta, sostituite `tua-email@github.com` con l'email del vostro account GitHub. Questo è critico.

### Verificare la Configurazione

Per verificare che la configurazione sia stata salvata, digitate:

```powershell
git config --list
```

Vi verrà mostrato un lungo elenco di impostazioni di Git. Cercate le righe che dicono:

```
user.name=Il Vostro Nome
user.email=tua-email@github.com
```

Se vedete queste due righe con i valori che avete appena inserito, tutto è configurato correttamente.

### Dove Vengono Salvate Queste Configurazioni

Una nota tecnica che potrebbe interessare i curiosi: Git salva queste impostazioni globali in un file nascosto nella vostra home directory di Windows. Il percorso è:

```
C:\Users\VostroUsername\.gitconfig
```

Se foste interessati a vedere il file, potete aprirlo con il Blocco note. Non dovreste mai modificare manualmente questo file — il comando `git config` è il modo corretto di gestire queste impostazioni — ma sapere dov'è potrebbe essere utile per troubleshooting.

### La Differenza Tra --global e --local

Quando abbiamo usato `--global`, abbiamo detto a Git di usare questa identità per tutti i repository su questo computer. Alternativamente, potreste usare `--local` (o non specificare nulla e stare dentro una cartella repository) per impostare un'identità diversa per un singolo progetto.

Per esempio, se lavorate sia su progetti personali che per un'azienda, potreste volere usare un'email personale per i progetti personali e un'email aziendale per i progetti dell'azienda. In quel caso, configurereste globalmente il valore predefinito, ma poi cambiereste la configurazione locale per i progetti dell'azienda. Ma per un principiante, `--global` è la scelta giusta.

## Configurazione SSH: L'Handshake Sicuro con GitHub

Finora abbiamo configurato come Git vi identifica. Ma c'è un secondo livello di sicurezza: come GitHub vi identifica quando caricate codice sulla piattaforma. Questo porta a SSH.

### Il Problema: Come GitHub Sa Che Siete Voi

Immaginate un'analogia del mondo reale. Voi volete inviare un pacco a GitHub (il vostro codice) dal vostro ufficio postale locale (il vostro computer). L'ufficio postale che riceve il pacco (GitHub) vuole assicurarsi che il pacco viene realmente da voi e non da qualcuno che finge di essere voi.

Nel mondo analogico, potrebbe chiedere la vostra firma o un documento d'identità. Nel mondo digitale, GitHub chiede una prova crittografica — un meccanismo che usa la matematica per provare che voi siete chi dite di essere.

Storicamente, il metodo era usar le password. Ma le password hanno un problema: sono facili da rubare se digitati su un computer che non è vostro, o se il sito web è hackerato. Per questo motivo, gli sviluppatori hanno adottato SSH.

### Come Funziona SSH

SSH sta per "Secure Shell". È un protocollo che usa la **crittografia a chiave pubblica** per provare la vostra identità senza mai inviare una password.

Il concetto è questo: voi create una coppia di chiavi. Una è la vostra **chiave privata** — che tiene rigorosamente sul vostro computer e che non condividete mai con nessuno. L'altra è la vostra **chiave pubblica** — che potete dare a GitHub, al vostro datore di lavoro, a chiunque.

Quando volete connettervi a GitHub, GitHub usa la vostra chiave pubblica per creare una sfida crittografica. Voi risolvete la sfida usando la vostra chiave privata. Se la soluzione è corretta, GitHub sa che siete voi perché solo il possessore della chiave privata potrebbe risolvere quella sfida.

Il vantaggio di questo sistema è che GitHub non ha mai accesso alla vostra chiave privata. Anche se GitHub fosse hackerato, i vostri segreti rimarrebbero al sicuro perché sono solo sul vostro computer.

### Generare la Coppia di Chiavi SSH

Su Windows 11, aprite PowerShell. Digitate il seguente comando:

```powershell
ssh-keygen -t ed25519 -C "tua-email@github.com"
```

Spieghiamo i componenti:

- `ssh-keygen` è il programma che genera le chiavi
- `-t ed25519` specifica l'algoritmo di crittografia. Ed25519 è una scelta moderna e sicura, più veloce di RSA che era lo standard precedente
- `-C "commento"` aggiunge un commento alle vostra chiave — generalmente l'email per ricordarvi quale chiave è quale se ne generate molte

Premete Enter. Il sistema vi chiederà dove salvare la chiave. Vedrete un messaggio come:

```
Enter file in which to save the key (/c/Users/YourUsername/.ssh/id_ed25519):
```

Il percorso predefinito è perfetto. Premete Enter per accettarlo.

Successivamente, vi chiederà una **passphrase**. Una passphrase è una password aggiuntiva che protegge la vostra chiave privata. Se qualcuno riuscisse fisicamente ad accedere al vostro computer e a rubare il file della chiave privata, avrebbe comunque bisogno della passphrase per usarla.

Potete lasciarlo vuoto (premete Enter due volte) se volete semplicità, o potete inserire una passphrase sicura. Se scegliete di inserire una passphrase, dovrete digitar la ogni volta che usate Git — potete automatizzare questo processo in seguito, ma per ora keepit simple.

Supponendo abbiate premuto Enter due volte, il processo è completato. Vedrete un output che mostra un "fingerprint" della vostra chiave — è una rappresentazione breve della vostra chiave. Non è importante capire esattamente cosa sia, l'importante è che il comando ha funzionato.

### Dove Sono Salvate le Chiavi

Le chiavi sono state salvate nella cartella `.ssh` dentro la vostra home directory. Su Windows, il percorso è:

```
C:\Users\VostroUsername\.ssh\
```

Dentro questa cartella troverete due file:

- `id_ed25519` — la vostra chiave privata (segreta!)
- `id_ed25519.pub` — la vostra chiave pubblica (ok da condividere)

### Aggiungere la Chiave Pubblica a GitHub

Ora dovete dire a GitHub quale sia la vostra chiave pubblica, così che possa usarla per verificare la vostra identità in futuro.

Per prima cosa, copiate il contenuto della vostra chiave pubblica. Su PowerShell, digitate:

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

Questo comando legge il file della chiave pubblica e lo copia negli appunti. (Se non funziona, potete aprire il file con il Blocco note e copiare manualmente: aprite `C:\Users\VostroUsername\.ssh\id_ed25519.pub`, selezionate tutto, e copiate.)

Ora andate su GitHub. Se siete loggati, cliccate la vostra immagine profilo in alto a destra e cliccate "Settings". Nel menu a sinistra, cercate "SSH and GPG keys" e cliccate.

Cliccate il pulsante verde "New SSH key". Vi apparirà un form con due campi: "Title" e "Key".

Nel campo "Title", inserite qualcosa di descrittivo come "Windows PC" o "Home Laptop" — questo è solo per voi, così che ricordiate quale chiave è quale se ne avete molte.

Nel campo "Key", incollate il contenuto della vostra chiave pubblica (che avete copiato negli appunti).

Cliccate "Add SSH key". GitHub vi potrebbe chiedere di confermare la password del vostro account come ulteriore misura di sicurezza. Fatelo.

### Verificare che SSH Funziona

Torniamo su PowerShell e verifichiamo che tutto sia configurato correttamente. Digitate:

```powershell
ssh -T git@github.com
```

Questo comando tenta di connettersi a GitHub via SSH e poi immediatamente chiude la connessione — serve solo per testare.

La prima volta che vi connettete, GitHub vi chiederà se volete aggiungere il fingerprint di GitHub alla vostra lista di host conosciuti. Digitate `yes` e premete Enter.

Se vedete un messaggio che dice qualcosa come `Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access.`, significa che tutto funziona perfettamente. Se vedete un errore, controllate che abbiate copiato correttamente la chiave pubblica su GitHub.

### Note Sulla Passphrase SSH (Avanzato)

Se avete impostato una passphrase SSH, vi verrà chiesta ogni volta che usate Git per connettervi a GitHub. Se trovate questo fastidioso, potete configurare un "agente SSH" che memorizza la passphrase in memoria per il resto della sessione.

Su PowerShell, digitate:

```powershell
$env:GIT_SSH_COMMAND = "ssh -i $env:USERPROFILE\.ssh\id_ed25519"
```

In realtà, per Windows è un po' più complicato. Un approccio più semplice è usare Windows built-in OpenSSH agent. Ma per principianti, semplicemente lasciate in pace la passphrase — il disagio di digitar la è minore della complessità di configurare l'agente SSH.

## Creare un Repository su GitHub

Ora che avete Git installato e SSH configurato, è il momento di creare il vostro primo repository remoto su GitHub.

### Creare il Repository

Andate su GitHub.com e assicuratevi di essere loggati. In alto a destra, cliccate il segno "+" e poi "New repository" dal menu.

Vi apparirà un form. Il primo campo chiede il nome del repository. Usate un nome descrittivo — per esempio, `learning-python` se state imparando Python, o `my-first-project`.

Il secondo campo è la descrizione — opzionale ma utile. Mettete qualcosa che spiega brevemente cosa è il progetto.

Più in basso, vedrete un'opzione per rendere il repository "Public" o "Private". Public significa che chiunque su internet può vedere il vostro codice. Private significa che solo voi potete vederlo (per ora; potete aggiungere collaboratori in seguito). Per il vostro primo progetto, "Private" è una scelta ragionevole.

C'è anche un'opzione "Add a README file" — spuntate questa. Un README è un file di testo che spiega il vostro progetto. È una buona abitudine creare fin dall'inizio.

Cliccate "Create repository". GitHub creerà il vostro repository remoto.

## Clonare il Repository sul Vostro Computer

Adesso avete un repository su GitHub, ma non ancora sul vostro computer. Dobbiamo "clonare" il repository — scaricare una copia sul vostro computer che è collegata a quella su GitHub.

Sulla pagina GitHub del vostro repository, cliccate il pulsante verde "<> Code". Vi apparirà un menu. Assicuratevi che sia selezionato il tab "SSH" (non "HTTPS"). Vedrete un URL che assomiglia a `git@github.com:yourusername/repo-name.git`.

Cliccate l'icona di copia per copiare questo URL negli appunti.

Ora aprite PowerShell. Navigatevi nella directory dove volete salvare il repository. Per esempio, se volete que sia in `C:\Users\VostroUsername\Projects\`, digitate:

```powershell
cd C:\Users\VostroUsername\Projects
```

Se la cartella `Projects` non esiste, createla prima:

```powershell
mkdir C:\Users\VostroUsername\Projects
```

Ora clonate il repository:

```powershell
git clone git@github.com:yourusername/repo-name.git
```

(Incollate l'URL che avete copiato da GitHub al posto di `git@github.com:yourusername/repo-name.git`.)

Git scaricherà il repository e creerà una cartella con lo stesso nome del repository. Navigatevi dentro:

```powershell
cd repo-name
```

Potete verificare che il collegamento a GitHub è stato creato correttamente digitando:

```powershell
git remote -v
```

Dovreste vedere due linee che dicono `origin` (il nome predefinito per il repository remoto) con l'URL SSH che avete usato per clonare. Se le vedete, congratulazioni — il vostro repository locale è collegato a GitHub.

## Il Ciclo di Lavoro di Git: Add, Commit, Push

Ora arriviamo al cuore di come usare Git nel quotidiano. Ogni volta che farete dei cambiamenti al vostro progetto, seguirete un ciclo di tre passi:

1. **Modify** — Modificate i file
2. **Stage** — Dite a Git quali modifiche volete salvare
3. **Commit** — Salvate le modifiche in locale
4. **Push** — Inviate le modifiche a GitHub (opzionale ma consigliato)

### Il Concetto di Staging

Il concetto di "staging" (o "index") è quello che confonde di più i principianti. Perché non potete semplicemente salvare tutto?

La ragione è il controllo. Immaginate di avere modificato 5 file, ma solo 2 di questi sono pronti per essere salvati come una "unità logica". Forse gli altri 3 file contengono esperimenti che non volete includere nel commit. Git vi permette di scegliere esattamente quali file includere in questo commit e quali lasciar fuori (magari per includerli in un commit successivo).

È come se steste preparando una spedizione. Avete una pila di cose sulla vostra scrivania, ma per questa spedizione volete mandare solo alcune di queste cose. Lo "staging area" è il tavolo dove mettete le cose che volete spedire. Solo dopo aver deciso esattamente cosa spedire create la scatola (il commit) e la inviate (il push).

### Verificare lo Stato

Ogni volta che volete sapere qual è la situazione del vostro repository, digitate:

```powershell
git status
```

Questo comando vi dirà:

- Quali file sono stati modificati ma non ancora staggiati
- Quali file sono staggiati in attesa di essere committati
- Se siete sincronizzati con GitHub o se avete modifiche locali che GitHub non conosce ancora

L'output di `git status` è amichevole per i principianti e vi suggerisce anche i comandi successivi da usare.

### Aggiungere File allo Staging Area

Una volta che avete fatto modifiche ai file, dovete dire a Git di includerle nel prossimo commit. Digitate:

```powershell
git add nome-file.py
```

Se volete aggiungere più file contemporaneamente, potete lasciarli tutti in una volta:

```powershell
git add file1.py file2.py file3.py
```

O, se volete aggiungere tutti i file modificati in una directory:

```powershell
git add .\
```

Il `.\` significa "la directory corrente e tutto al suo interno". In genere, fate attenzione quando usate `git add` su tutto — preferibilmente sapete quali file stanno per essere inclusi.

Se volete aggiungere tutti i file modificati nel repository (non consigliato se siete sicuri di cosa state facendo), digitate:

```powershell
git add .
```

Dopo aver usato `git add`, potete verificare cosa avete staggiato digitando di nuovo `git status`. Vedrete i file elencati sotto "Changes to be committed".

### Creare un Commit

Una volta che avete staggiato i file che volete, createte un "commit" — un salvataggio con un messaggio che spiega cosa avete fatto:

```powershell
git commit -m "Descrizione delle modifiche"
```

Il messaggio tra virgolette dovrebbe essere breve e descrittivo. Per esempio:

- `git commit -m "Aggiungi funzione di login"`
- `git commit -m "Correggi bug nel parsing JSON"`
- `git commit -m "Refactor codice di validazione"`

Una buona pratica è scrivere il messaggio di commit in imperativo, come se state dicendo a qualcuno "fai questo": "Aggiungi feature" anziché "Ho aggiunto feature" o "Aggiunto feature".

Dopo il commit, Git vi mostrerà un riepilogo di quanti file sono stati modificati e quante linee di codice sono state aggiunte o rimosse.

### Spingere le Modifiche a GitHub

Finora, il vostro commit esiste solo sul vostro computer. Per sincronizzare con GitHub, dovete "spingere" il vostro lavoro:

```powershell
git push
```

Questo comando invia tutti i commit locali che GitHub non conosce ancora al repository remoto. Dopo questo comando, se andate su GitHub e visualizzate il vostro repository, vedrete i file aggiornati e il vostro commit apparirà nella storia.

### Tirare le Modifiche da GitHub

Se state lavorando in team, o se state lavorando da più computer, gli altri potrebbero aver spinto modifiche a GitHub. Per sincronizzare il vostro computer con le loro modifiche, digitate:

```powershell
git pull
```

Una buona abitudine è sempre iniziare una sessione di lavoro con `git pull`, assicurandovi che avete le versioni più recenti di tutti i file. E finire la sessione con `git push`, assicurandovi che il vostro lavoro sia salvato su GitHub.

## Riepilogo dei Comandi Essenziali

| Comando | Funzione |
|---------|----------|
| `git status` | Verifica lo stato del repository e cosa è cambiato |
| `git add <file>` | Aggiunge file allo staging area |
| `git add .` | Aggiunge tutti i file modificati allo staging area |
| `git commit -m "msg"` | Crea un commit con il messaggio specificato |
| `git push` | Invia i commit locali a GitHub |
| `git pull` | Scarica le modifiche da GitHub |
| `git log` | Mostra la storia dei commit |
| `git clone <url>` | Clona un repository da GitHub |
| `git remote -v` | Mostra il repository remoto collegato |

## Buone Pratiche e Etichetta di Git

Anche se tecnicamente potete usare Git in qualsiasi modo, seguire alcune convenzioni vi renderà la vita più facile e farete bella figura se collaborerete con altri.

**Commit frequenti**: Non aspettate di fare due ore di lavoro e poi committare tutto in una volta. Committate ogni volta che completate una piccola unità logica di lavoro. Se potete descrivere il commit in una sola frase senza usare "e", probabilmente è della giusta grandezza.

**Messaggi descrittivi**: Il messaggio del commit è principalmente per voi stessi nel futuro. Immaginate di leggere il vostro commit tra sei mesi — il messaggio dovrebbe spiegare chiaramente cosa è stato fatto e perché.

**Sempre pullare prima di lavorare**: Se state collaborando, iniziate sempre la vostra sessione di lavoro con `git pull`. Questo assicura che avete le ultime modifiche e riduce la possibilità di conflitti.

**Sempre pushare quando finite**: Finire la vostra sessione con `git push` assicura che il vostro lavoro non vada perso se il vostro computer ha un problema.

**Verifica prima di chiudere**: Prima di chiudere il vostro editor o spegnere il computer, digitate `git status`. Se vedete il messaggio "nothing to commit, working tree clean", siete sincronizzati. Se vedete file modified o in staging, siete in una situazione incoerente — commitateli e spingeli.

## Conclusione: Il Vostro Nuovo Superpotere

Una volta che capite Git, cambierà il modo in cui approcciate la programmazione. Non dovrete più temere di fare modifiche perché potete sempre tornare indietro. Potete sperimentare liberamente perché ogni fase è salvata.

Col tempo, Git diventerà così automatico che non penserete nemmeno a usarlo — sarà semplice come salvare un file. E quando collaborerete con altri sviluppatori, avrete un linguaggio comune per discutere il lavoro e la storia del codice.

Benvenuti nel mondo dello sviluppo moderno.