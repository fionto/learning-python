## 1. Preparazione della cartella locale

Per prima cosa, creiamo la directory e spostiamoci al suo interno. In PowerShell, puoi usare il comando `New-Item` o il classico `mkdir`.

```powershell
# Crea la cartella (inclusi i genitori se necessario)
New-Item -ItemType Directory -Force -Path "C:\GitRepositories\budget-bridge"

# Entra nella cartella
cd "C:\GitRepositories\budget-bridge"

```

## 2. Inizializzazione di Git

Ora trasformiamo questa cartella in una repository Git locale.

```powershell
# Inizializza il repository
git init -b main

```

> **Nota:** Usiamo `-b main` per assicurarci che il branch predefinito si chiami "main", allineandoci allo standard attuale di GitHub.

## 3. Creazione del primo file e commit

Git non può "pushare" una cartella vuota. Creiamo un file README veloce per testare il tutto.

```powershell
# Crea un file README
"## Budget Bridge`nRepository per la gestione del budget." | Out-File -FilePath README.md -Encoding utf8

# Aggiungi il file all'area di stage
git add README.md

# Crea il primo commit
git commit -m "Initial commit: setup repository"

```

---

## 4. Collegamento a GitHub tramite SSH

Ora viene la parte "social". Prima di lanciare i comandi sotto, assicurati di aver creato una repository **vuota** su GitHub (senza README, licenza o .gitignore generati dal sito) chiamata `budget-bridge`.

Una volta creata la repo su GitHub, copia l'URL SSH (quello che inizia con `git@github.com:...`) e usa questi comandi:

```powershell
# Sostituisci 'TUO_UTENTE' con il tuo vero username GitHub
$remoteUrl = "git@github.com:TUO_UTENTE/budget-bridge.git"

# Aggiungi l'origine remota
git remote add origin $remoteUrl

# Verifica che l'URL sia corretto
git remote -v

```

## 5. Push dei dati

Infine, inviamo il commit locale al server remoto.

```powershell
# Invia i dati e imposta il branch 'main' come upstream
git push -u origin main

```

---

### Pro-Tip per PowerShell 7

Se vuoi verificare velocemente lo stato della tua repo con un tocco di colore, usa:
`git status`

**Tutto chiaro fin qui?** Se vuoi, posso aiutarti a generare un file `.gitignore` specifico per il linguaggio di programmazione che userai per *budget-bridge*.