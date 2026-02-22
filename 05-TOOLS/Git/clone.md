## 💻 Guida PowerShell 7: Inizializzazione e Setup Progetto

### 1. Navigazione e Creazione (Il punto di partenza)

Apri PowerShell 7. Di default ti troverai nella tua cartella utente. Scegliamo dove far vivere il progetto (es. in `Documents`):

```powershell
# Naviga nei documenti
cd C:\GitRepositories

# Crea la cartella del progetto (se stai partendo da zero)
mkdir budget-bridge
cd budget-bridge

```

### 2. Recupero da GitHub (Clone)

Se il progetto esiste già online, usa questo comando. PowerShell gestirà il download della struttura che abbiamo definito:

```powershell
# Scarica il repository
git clone https://github.com/TUO_UTENTE/NOME_REPOSITY.git .

# Nota: il punto finale "." dice a Git di scaricare i file 
# direttamente nella cartella attuale invece di crearne una nuova.

```

---