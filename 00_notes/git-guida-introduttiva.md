# Guida introduttiva a Git e GitHub

## Cos'è Git

Git è un sistema di **version control** — un software che tiene traccia di tutte le modifiche ai tuoi file nel tempo. Immagina di avere un "salvataggio" automatico con la possibilità di tornare indietro a qualsiasi punto precedente.

Git funziona **localmente** sul tuo computer. Non richiede connessione internet per funzionare.

## Cos'è GitHub

GitHub è una piattaforma online che ospita repository Git. Ti permette di:

- Avere un backup remoto del tuo lavoro
- Condividere codice con altri
- Collaborare su progetti

GitHub è di proprietà di Microsoft ed è gratuito per uso personale, inclusi repository privati illimitati.

## Cos'è un Repository

Un **repository** (o "repo") è una cartella di progetto tracciata da Git. Contiene i tuoi file più tutta la storia delle modifiche.

Quando cloni un repository, Git crea una cartella nascosta `.git` che contiene:

- La storia completa del progetto
- La configurazione
- Il collegamento al repository remoto

---

## Installazione su Linux Mint

### Verifica se Git è già installato

```bash
git --version
```

### Se non è installato

```bash
sudo apt update
sudo apt install git
```

---

## Configurazione iniziale

### Imposta la tua identità

Git "firma" ogni commit con il tuo nome ed email. Questi dati servono a identificare chi ha fatto ogni modifica.

```bash
git config --global user.name "Il Tuo Nome"
git config --global user.email "tua-email@esempio.com"
```

**Spiegazione del comando:**

| Parte | Significato |
|-------|-------------|
| `git` | invoca il programma Git |
| `config` | modifica la configurazione |
| `--global` | applica a tutti i repository sul sistema |
| `user.name` | la proprietà da impostare |
| `"valore"` | il valore da assegnare |

L'email deve essere la stessa usata per registrarsi su GitHub, altrimenti i commit non vengono collegati al tuo profilo.

### Dove vengono salvate le configurazioni

Le impostazioni globali sono salvate in `~/.gitconfig`. Puoi verificarle con:

```bash
cat ~/.gitconfig
```

---

## Configurazione autenticazione SSH

### Perché serve SSH

Quando carichi codice su GitHub (operazione chiamata "push"), GitHub deve verificare la tua identità. SSH usa una coppia di chiavi crittografiche invece di una password.

### Come funziona

- **Chiave privata** → resta sul tuo computer, non la condividi mai
- **Chiave pubblica** → la dai a GitHub

Quando ti connetti, GitHub verifica che tu possieda la chiave privata corrispondente alla chiave pubblica registrata.

### Generare la coppia di chiavi

```bash
ssh-keygen -t ed25519 -C "tua-email@esempio.com"
```

| Parte | Significato |
|-------|-------------|
| `ssh-keygen` | programma che genera chiavi SSH |
| `-t ed25519` | tipo di algoritmo crittografico |
| `-C "email"` | commento per identificare la chiave |

Premi Invio per accettare il percorso predefinito (`~/.ssh/id_ed25519`). Ti verrà chiesta una **passphrase** opzionale per proteggere la chiave.

Dopo questo comando avrai due file:

- `~/.ssh/id_ed25519` → chiave privata
- `~/.ssh/id_ed25519.pub` → chiave pubblica

### Aggiungere la chiave pubblica a GitHub

Copia la chiave pubblica:

```bash
cat ~/.ssh/id_ed25519.pub
```

Poi su GitHub:

1. Clicca la tua foto profilo → Settings
2. SSH and GPG keys → New SSH key
3. Incolla la chiave e salva

### Verificare la connessione

```bash
ssh -T git@github.com
```

La prima volta ti chiederà di confermare — scrivi `yes`. Se vedi "Hi username! You've successfully authenticated" funziona tutto.

### Nota sulla passphrase

Se hai impostato una passphrase, ti verrà chiesta ad ogni operazione Git. Per evitarlo, puoi avviare l'agente SSH:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

L'agente tiene la chiave in memoria per la durata della sessione.

---

## Creare un repository

### Su GitHub

1. Clicca "+" in alto a destra → "New repository"
2. Scegli un nome
3. Seleziona Private o Public
4. Spunta "Add a README file"
5. Clicca "Create repository"

### Clonare sul computer

```bash
cd ~
git clone git@github.com:tuo-username/nome-repo.git
cd nome-repo
```

Questo scarica il repository e crea il collegamento con GitHub. Puoi verificare il collegamento con:

```bash
git remote -v
```

---

## Il ciclo di lavoro Git

### I tre passi fondamentali

1. **Modifica** → fai cambiamenti ai file
2. **Stage** → dici a Git quali cambiamenti salvare
3. **Commit + Push** → salvi in locale e carichi su GitHub

### Flusso visivo

```
[I tuoi file] → git add → [Stage] → git commit → [.git locale] → git push → [GitHub]
```

### Comandi in pratica

**Verificare lo stato:**

```bash
git status
```

Ti mostra quali file sono stati modificati, quali sono in stage, e se sei sincronizzato con GitHub.

**Aggiungere file allo stage:**

```bash
git add nome-file        # singolo file
git add nome-cartella/   # cartella e contenuto
git add .                # tutto
```

**Creare un commit:**

```bash
git commit -m "Descrizione delle modifiche"
```

Il messaggio tra virgolette descrive cosa hai fatto. Tienilo breve e chiaro.

**Caricare su GitHub:**

```bash
git push
```

**Scaricare modifiche da GitHub:**

```bash
git pull
```

Usalo sempre a inizio sessione per partire dalla versione più aggiornata.

---

## Riepilogo comandi essenziali

| Comando | Funzione |
|---------|----------|
| `git status` | Verifica stato del repository |
| `git add <file>` | Aggiunge file allo stage |
| `git commit -m "msg"` | Salva le modifiche in locale |
| `git push` | Carica su GitHub |
| `git pull` | Scarica da GitHub |
| `git clone <url>` | Clona un repository |
| `git remote -v` | Mostra repository remoti collegati |

---

## Buone pratiche

- **Inizia sempre con `git pull`** per sincronizzarti
- **Commit frequenti** con messaggi descrittivi
- **Verifica con `git status`** prima di chiudere la sessione
- Se vedi "nothing to commit, working tree clean" sei sincronizzato
