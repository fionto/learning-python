# Guida: Configurazione di un ambiente Python per data science con `uv` su Fedora 44 KDE Plasma

## Indice

1. [Cos'è `uv` e perché usarlo](#1-cosè-uv-e-perché-usarlo)
2. [Installazione di `uv`](#2-installazione-di-uv)
3. [Concetto chiave: ambiente condiviso vs ambiente per-progetto](#3-concetto-chiave-ambiente-condiviso-vs-ambiente-per-progetto)
4. [Creazione dell'ambiente virtuale condiviso](#4-creazione-dellambiente-virtuale-condiviso)
5. [Attivazione dell'ambiente](#5-attivazione-dellambiente)
6. [Installazione dei pacchetti](#6-installazione-dei-pacchetti)
7. [Collegamento con VSCode](#7-collegamento-con-vscode)
8. [Verifica finale](#8-verifica-finale)
9. [Comandi utili da ricordare](#9-comandi-utili-da-ricordare)
10. [Prossimi passi](#10-prossimi-passi)

---

## 1. Cos'è `uv` e perché usarlo

`uv` è uno strumento per la gestione di progetti e ambienti Python, sviluppato da **Astral** (gli stessi autori di `ruff`, il famoso linter/formatter Python) e scritto in **Rust**.

Il motivo per cui sta guadagnando popolarità è che **unifica in un solo tool** diverse funzioni che tradizionalmente richiedevano strumenti separati:

| Funzione | Strumento "tradizionale" | Equivalente in `uv` |
|---|---|---|
| Creare ambienti virtuali | `venv`, `virtualenv` | `uv venv` |
| Installare pacchetti | `pip` | `uv pip install` |
| Gestire versioni di Python | `pyenv` | `uv python` |
| Gestire dipendenze di progetto | `pip` + `requirements.txt` | `uv add` + `pyproject.toml` |
| Bloccare versioni esatte (lockfile) | `pip-tools`, `poetry` | `uv lock` |

**Perché è più veloce**: `pip` è scritto in Python, `uv` è scritto in Rust. Questo si traduce in risoluzione delle dipendenze e installazioni molto più rapide (spesso 10-100 volte), oltre a una cache globale dei pacchetti condivisa tra tutti i tuoi ambienti virtuali, evitando di riscaricare gli stessi pacchetti più volte.

**Compatibilità**: `uv` non reinventa tutto da zero. Il comando `uv pip install`, ad esempio, si comporta come un `pip install` classico nell'interfaccia, ma sfrutta il motore interno di `uv` per essere più veloce. Questo lo rende facile da adottare senza dover disimparare `pip`.

---

## 2. Installazione di `uv`

Esistono due strade principali su Fedora:

- **Via `dnf`**: comoda perché si integra con gli aggiornamenti di sistema, ma la versione nei repository Fedora tende ad essere più indietro rispetto alle release ufficiali (che sono molto frequenti).
- **Via installer ufficiale**: scarica sempre l'ultima versione e si autoaggiorna con `uv self update`. È l'approccio raccomandato dalla documentazione ufficiale ed è quello che abbiamo scelto.

### Comando eseguito

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Spiegazione:**

- `curl -LsSf <url>` scarica lo script di installazione ufficiale:
  - `-L` segue eventuali redirect dell'URL
  - `-s` modalità silenziosa (niente progress bar)
  - `-S` ma mostra comunque gli errori, se presenti
  - `-f` fallisce silenziosamente su errori HTTP invece di scaricare una pagina d'errore come fosse lo script
- `| sh` passa lo script scaricato direttamente alla shell per l'esecuzione

Lo script installa il binario in `~/.local/bin/uv` e aggiunge quella cartella al `$PATH`, modificando `~/.bashrc`.

> ⚠️ **Nota di sicurezza**: il pattern `curl | sh` esegue codice scaricato da internet con i permessi del proprio utente. È buona norma farlo solo da fonti ufficiali e documentate, come in questo caso (astral.sh, sito ufficiale degli sviluppatori di `uv`).

### Ricaricare la shell

Dopo l'installazione, la shell corrente non "vede" ancora subito il nuovo `$PATH`, perché `~/.bashrc` viene letto da bash solo all'avvio di una nuova sessione:

```bash
source ~/.bashrc
```

### Verifica

```bash
uv --version
```

Output ottenuto:
```
uv 0.12.3 (x86_64-unknown-linux-gnu)
```

---

## 3. Concetto chiave: ambiente condiviso vs ambiente per-progetto

Prima di procedere, è importante distinguere due modi diversi di usare `uv`:

### Flusso "standard" (per-progetto)

Pensato per isolare completamente le dipendenze di un singolo progetto. Si usa `uv init` dentro una cartella, e `uv` crea automaticamente:
- un file `pyproject.toml` (elenco delle dipendenze del progetto)
- un file di lock (versioni esatte, per riproducibilità)
- un ambiente virtuale `.venv` dedicato *solo* a quel progetto

Questo è l'approccio più corretto quando un progetto deve essere condiviso, versionato, o deployato, perché chiunque può ricreare esattamente lo stesso ambiente.

### Flusso "ambiente condiviso" (quello che abbiamo fatto oggi)

Un unico ambiente virtuale "generalista", con i pacchetti scientifici più comuni già installati, riutilizzabile trasversalmente da più progetti/script senza dover reinstallare tutto ogni volta.

È un pattern comune soprattutto in fase di apprendimento o per piccoli script/esperimenti, ma **non traccia le dipendenze in un file di progetto**: se in futuro vorrai condividere uno script con qualcun altro, sarà necessario elencare manualmente cosa serve, oppure migrare quel progetto verso il flusso per-progetto.

Per costruire l'ambiente condiviso abbiamo usato i comandi "di basso livello" di `uv` (`uv venv` e `uv pip`), non il flusso a progetto (`uv init`).

---

## 4. Creazione dell'ambiente virtuale condiviso

Abbiamo scelto come posizione `~/venvs/data-science`, una cartella dedicata e separata dai progetti veri e propri.

### Comando eseguito

```bash
uv venv ~/venvs/data-science
```

**Spiegazione:**

`uv venv <percorso>` crea un nuovo ambiente virtuale Python in quel percorso (creando anche le cartelle intermedie mancanti). Al suo interno viene generata una struttura simile a quella di un `venv` standard di Python (cartelle `bin/`, `lib/`, file `pyvenv.cfg`), ma la creazione è molto più rapida grazie al motore Rust di `uv`.

### Output ottenuto

```
Using CPython 3.14.6 interpreter at: /usr/bin/python
Creating virtual environment at: venvs/data-science
Activate with: source venvs/data-science/bin/activate
```

`uv` ha usato automaticamente il Python di sistema di Fedora 44 (`/usr/bin/python`, versione 3.14.6), senza bisogno di scaricare un interprete separato.

---

## 5. Attivazione dell'ambiente

### Cos'è "attivare" un ambiente virtuale

Finché un ambiente virtuale non è attivato, il terminale continua a usare il Python di sistema e i suoi pacchetti globali. Attivarlo significa dire alla shell corrente: *"per questa sessione, usa il Python e i pacchetti dentro questa cartella al posto di quelli di sistema"*.

È un cambiamento **temporaneo e locale alla sessione di terminale**: se apri un nuovo terminale, quello resta "disattivato" finché non lo attivi anche lì esplicitamente.

### Comando eseguito

```bash
source ~/venvs/data-science/bin/activate
```

**Spiegazione:**

Dentro la cartella dell'ambiente virtuale esiste uno script `bin/activate`, che modifica variabili d'ambiente della shell corrente (in particolare il `$PATH`, anteponendo `~/venvs/data-science/bin`) e definisce una funzione `deactivate` per tornare indietro quando serve.

Si usa `source` (e non un'esecuzione diretta tipo `./activate`) perché lo script deve modificare la shell *corrente*: se venisse eseguito come processo separato, le modifiche andrebbero perse non appena lo script termina.

**Come si riconosce che è attivo**: il prompt del terminale cambia, mostrando `(data-science)` prima del solito prompt.

---

## 6. Installazione dei pacchetti

Con l'ambiente attivato, i pacchetti installati finiscono *dentro* quell'ambiente, senza toccare il Python di sistema.

### Comando eseguito

```bash
uv pip install pandas numpy scipy matplotlib
```

**Spiegazione dei pacchetti:**

| Pacchetto | A cosa serve |
|---|---|
| `pandas` | Manipolazione di dati tabellari tramite `DataFrame` |
| `numpy` | Calcolo numerico, array multidimensionali — è la base su cui sono costruiti pandas e scipy |
| `scipy` | Algoritmi scientifici avanzati (statistica, ottimizzazione, algebra lineare), costruiti sopra numpy |
| `matplotlib` | Visualizzazione dati e creazione di grafici |

> 📌 `jupyterlab` è stato volutamente escluso da questo ambiente: verrà valutato in futuro insieme a esperimenti con software GUI nativi di KDE Plasma per i notebook.

### Output ottenuto

```
Using Python 3.14.6 environment at: venvs/data-science
Resolved 13 packages in 685ms
Prepared 13 packages in 6.97s
Installed 13 packages in 149ms
 + contourpy==1.3.3
 + cycler==0.12.1
 + fonttools==4.63.0
 + kiwisolver==1.5.0
 + matplotlib==3.11.1
 + numpy==2.5.2
 + packaging==26.3
 + pandas==3.0.5
 + pillow==12.3.0
 + pyparsing==3.3.2
 + python-dateutil==2.9.0.post0
 + scipy==1.18.0
 + six==1.17.0
```

Oltre ai 4 pacchetti richiesti, `uv` ha risolto e installato automaticamente anche le loro **dipendenze indirette** (es. `pillow` e `fonttools`/`kiwisolver` servono a matplotlib per la gestione di immagini e font; `python-dateutil` e `six` servono a pandas per la gestione delle date).

---

## 7. Collegamento con VSCode

VSCode non individua automaticamente l'ambiente `~/venvs/data-science`: va indicato esplicitamente, a livello di cartella di progetto, quale interprete Python usare.

### Concetto

VSCode legge le impostazioni specifiche di un progetto da un file `settings.json`, posizionato in una cartella nascosta `.vscode/` dentro la cartella del progetto stesso. Specificando lì il percorso dell'interprete, VSCode lo userà automaticamente per l'editor (autocompletamento, linting) e per l'esecuzione di script dal terminale integrato.

### Comando eseguito

Per il progetto `/home/matteo/GitRepositories/test/`:

```bash
mkdir -p /home/matteo/GitRepositories/test/.vscode && cat > /home/matteo/GitRepositories/test/.vscode/settings.json << 'EOF'
{
    "python.defaultInterpreterPath": "/home/matteo/venvs/data-science/bin/python"
}
EOF
```

**Spiegazione:**

- `mkdir -p .../.vscode`: crea la cartella `.vscode` dentro il progetto (`-p` evita errori se esiste già e crea le cartelle intermedie mancanti)
- `&&`: esegue il comando successivo solo se il precedente è andato a buon fine
- `cat > file << 'EOF' ... EOF`: è un **heredoc**, scrive il testo racchiuso tra i due `EOF` dentro il file indicato. Le virgolette singole attorno al primo `EOF` dicono alla shell di non interpretare/espandere nulla nel blocco (utile qui perché il JSON contiene caratteri come `{ }` che la shell potrebbe altrimenti provare a interpretare)

Dopo aver creato il file, è stato necessario ricaricare la finestra di VSCode (`Ctrl+Shift+P` → *Reload Window*) perché l'interprete `data-science` comparisse nella barra di stato in basso a destra.

> 💡 **In alternativa**, lo stesso risultato si ottiene dall'interfaccia grafica di VSCode con `Ctrl+Shift+P` → *Python: Select Interpreter* → scegliendo manualmente il percorso. Utile per progetti futuri, senza dover passare da bash.

---

## 8. Verifica finale

File `main.py`:

```python
import pandas as pd
print(pd.__version__)
```

Eseguito dal terminale integrato di VSCode (che eredita l'interprete impostato nel workspace):

```
3.0.5
```

Corrisponde esattamente alla versione di pandas installata nell'ambiente `data-science`: conferma che VSCode, il terminale e l'ambiente virtuale sono correttamente collegati.

---

## 9. Comandi utili da ricordare

| Comando | Cosa fa |
|---|---|
| `uv --version` | Mostra la versione di `uv` installata |
| `uv self update` | Aggiorna `uv` all'ultima versione |
| `uv venv <percorso>` | Crea un nuovo ambiente virtuale in quel percorso |
| `source <percorso>/bin/activate` | Attiva un ambiente virtuale nella shell corrente |
| `deactivate` | Disattiva l'ambiente virtuale attivo (funzione creata da `activate`) |
| `uv pip install <pacchetti>` | Installa pacchetti nell'ambiente attivo |
| `uv pip list` | Elenca i pacchetti installati nell'ambiente attivo |

---

## 10. Prossimi passi

- Valutare l'installazione di `jupyterlab` in questo stesso ambiente (o in uno dedicato), abbinata a un client notebook nativo KDE Plasma
- Imparare il flusso "per-progetto" di `uv`, con `uv init`, `pyproject.toml` e lockfile, per quando un progetto avrà bisogno di dipendenze isolate e riproducibili
- Eventualmente valutare la creazione di più ambienti condivisi tematici (es. `~/venvs/networking`, `~/venvs/automation`) seguendo lo stesso schema di oggi
