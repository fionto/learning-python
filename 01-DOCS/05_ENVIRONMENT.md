# Documentazione Ambiente Python

**Creato:** 20 Gennaio 2026  
**Ultimo Aggiornamento:** 20 Gennaio 2026  
**Versione Python:** 3.12.10  
**Sistema Operativo:** Windows 11  
**Package Manager:** pip (installazione globale)  
**Totale Pacchetti:** 107

---

## 📋 Filosofia di Setup

Questo è un ambiente Python **globale** (non virtualizzato).  
Scelta motivata dalla curva di apprendimento - migrazione a venv/conda prevista in Fase 2.

**Trade-offs accettati:**
- ✅ **Semplicità:** un solo Python, sempre disponibile
- ✅ **Zero configurazione:** nessuna attivazione necessaria
- ✅ **Focalizzazione:** imparo Python, non gestione ambienti
- ❌ **Conflitti potenziali:** rischio accettato e monitorato
- ❌ **Riproducibilità limitata:** documentato tramite snapshot

**Motto operativo:** *"Prima imparo a usare gli strumenti, poi imparo a organizzarli"*

---

## 📦 Inventario Pacchetti Installati

### Stack Data Science (Core)

| Pacchetto | Versione | Scopo | Quando Serve |
|-----------|----------|-------|--------------|
| **numpy** | 2.4.1 | Calcolo numerico, array multidimensionali | Think Python Cap. 15+, futuro data analysis |
| **pandas** | 2.3.3 | Manipolazione dati, DataFrame | Fase 2-3, analisi spettri Raman |
| **matplotlib** | 3.10.8 | Visualizzazione dati, plotting | Think Python, PCC Part II (Cap. 15-17) |
| **pillow** | 12.1.0 | Gestione immagini (PIL fork) | PCC progetti grafici, image processing |

**Dipendenze automatiche:**
- `contourpy` 1.3.3 - Calcolo contorni per matplotlib
- `cycler` 0.12.1 - Gestione stili matplotlib
- `fonttools` 4.61.1 - Font rendering matplotlib
- `kiwisolver` 1.4.9 - Layout solver matplotlib
- `pyparsing` 3.3.1 - Parsing espressioni matplotlib
- `pytz` 2025.2 - Timezone per pandas
- `python-dateutil` 2.9.0.post0 - Manipolazione date pandas

---

### Ecosistema Jupyter

| Pacchetto | Versione | Ruolo |
|-----------|----------|-------|
| **jupyter** | 1.1.1 | Meta-package (installa tutto l'ecosistema) |
| **jupyterlab** | 4.5.2 | Interfaccia moderna, multi-tab, IDE-like |
| **notebook** | 7.5.2 | Interfaccia classica, single-notebook |
| **ipython** | 9.9.0 | Shell interattiva potenziata (REPL++) |
| **ipykernel** | 7.1.0 | Kernel Python per esecuzione codice |
| **jupyturtle** | 2024.4.1 | Turtle graphics in Jupyter (Think Python Cap. 4) |

**Componenti Server:**
- `jupyter_server` 2.17.0 - Backend HTTP
- `jupyter_client` 8.8.0 - Comunicazione con kernel
- `jupyter_core` 5.9.1 - Utilities core
- `jupyter-console` 6.6.3 - Terminale Jupyter
- `jupyter-events` 0.12.0 - Sistema eventi
- `jupyter-lsp` 2.3.0 - Language Server Protocol
- `jupyter_server_terminals` 0.5.4 - Terminale integrato
- `jupyterlab_server` 2.28.0 - Backend JupyterLab
- `notebook_shim` 0.2.4 - Compatibilità Notebook 7

**UI e Rendering:**
- `ipywidgets` 8.1.8 - Widget interattivi (slider, button, etc.)
- `jupyterlab_widgets` 3.0.16 - Widget JupyterLab
- `widgetsnbextension` 4.0.15 - Estensione widget
- `jupyterlab_pygments` 0.3.0 - Syntax highlighting JupyterLab
- `ipython_pygments_lexers` 1.1.1 - Lexer Python per colori
- `matplotlib-inline` 0.2.1 - Grafici inline nei notebook

**Gestione Notebook:**
- `nbformat` 5.10.4 - Parser file `.ipynb` (JSON)
- `nbconvert` 7.16.6 - Conversione notebook (HTML, PDF, Markdown)
- `nbclient` 0.10.4 - Esecuzione notebook programmatica

---

### Testing Framework

| Pacchetto | Versione | Scopo |
|-----------|----------|-------|
| **pytest** | 9.0.2 | Framework testing moderno (PCC Cap. 11) |

**Dipendenze:**
- `iniconfig` 2.3.0 - Parsing configurazione pytest
- `pluggy` 1.6.0 - Sistema plugin pytest
- `packaging` 25.0 - Versioning e requirements

**Nota:** `pytest-cov` non ancora installato (da aggiungere quando necessario per coverage).

---

### Networking e HTTP

| Categoria | Pacchetti |
|-----------|-----------|
| **HTTP Clients** | `requests` 2.32.5, `httpx` 0.28.1, `httpcore` 1.0.9 |
| **HTTP Server** | `tornado` 6.5.4 (async web server per Jupyter) |
| **WebSocket** | `websocket-client` 1.9.0 (streaming Jupyter) |
| **SSL/Certs** | `certifi` 2026.1.4 (certificati CA) |
| **URL Parsing** | `urllib3` 2.6.3, `idna` 3.11 |
| **Headers** | `h11` 0.16.0 (HTTP/1.1 parsing) |

---

### Parsing e Serializzazione

| Formato | Pacchetti |
|---------|-----------|
| **JSON** | `json5` 0.13.0 (JSON5 esteso), `jsonpointer` 3.0.0, `fastjsonschema` 2.21.2 |
| **JSON Schema** | `jsonschema` 4.26.0, `jsonschema-specifications` 2025.9.1, `referencing` 0.37.0 |
| **YAML** | `PyYAML` 6.0.3 |
| **HTML/XML** | `beautifulsoup4` 4.14.3, `soupsieve` 2.8.3, `defusedxml` 0.7.1 |
| **Markdown** | `mistune` 3.2.0 (parser veloce) |
| **Altro** | `lark` 1.3.1 (parser grammar-based) |

---

### Template e Rendering

| Pacchetto | Versione | Utilizzo |
|-----------|----------|----------|
| `Jinja2` | 3.1.6 | Template engine (export notebook HTML) |
| `MarkupSafe` | 3.0.3 | Escape HTML sicuro (Jinja2) |
| `bleach` | 6.3.0 | Sanitizzazione HTML |
| `tinycss2` | 1.4.0 | Parser CSS |
| `webencodings` | 0.5.1 | Encoding HTML |
| `webcolors` | 25.10.0 | Colori web (CSS) |
| `pandocfilters` | 1.5.1 | Filtri per Pandoc (nbconvert) |

---

### Validazione e Formattazione

| Tipo | Pacchetti |
|------|-----------|
| **RFC Validators** | `rfc3339-validator` 0.1.4 (datetime), `rfc3986-validator` 0.1.1 (URI), `rfc3987-syntax` 1.1.0 (IRI) |
| **FQDN** | `fqdn` 1.5.1 (fully qualified domain names) |
| **URI** | `uri-template` 1.3.0 (RFC 6570) |
| **ISO Duration** | `isoduration` 20.11.0 (ISO 8601) |

---

### Development e Debugging

| Pacchetto | Versione | Scopo |
|-----------|----------|-------|
| `debugpy` | 1.8.19 | Debugger (VS Code integration) |
| `ipdb` | - | ❌ Non installato (da aggiungere se serve debugger IPython) |
| `pdb` | - | ✅ Built-in Python (sempre disponibile) |

**Auto-completion e Inspection:**
- `jedi` 0.19.2 - Autocompletamento Python
- `prompt_toolkit` 3.0.52 - Input interattivo avanzato
- `parso` 0.8.5 - Parser Python (Jedi)

**Execution Introspection:**
- `executing` 2.2.1 - AST inspection durante esecuzione
- `asttokens` 3.0.1 - Token AST annotati
- `stack-data` 0.6.3 - Analisi stack frame
- `pure_eval` 0.2.3 - Valutazione espressioni sicura

---

### Configurazione e Metadata

| Pacchetto | Versione | Scopo |
|-----------|----------|-------|
| `traitlets` | 5.14.3 | Sistema configurazione Jupyter (typed attributes) |
| `attrs` | 25.4.0 | Classi dataclass-like |
| `decorator` | 5.2.1 | Helper per decoratori |
| `typing_extensions` | 4.15.0 | Type hints backport |

---

### Sistema e I/O

| Categoria | Pacchetti |
|-----------|-----------|
| **Async I/O** | `anyio` 4.12.1 (async compatibility layer), `async-lru` 2.1.0 (LRU cache async), `nest-asyncio` 1.6.0 (nested event loops) |
| **Platform** | `platformdirs` 4.5.1 (directory standard OS), `psutil` 7.2.1 (process e sistema) |
| **Terminale** | `pywinpty` 3.0.2 (pseudo-terminal Windows), `terminado` 0.18.1 (terminal in browser), `colorama` 0.4.6 (ANSI colors Windows), `wcwidth` 0.2.14 (larghezza caratteri Unicode) |
| **Messaging** | `pyzmq` 27.1.0 (ZeroMQ per kernel-server communication), `comm` 0.2.3 (IPython comm) |
| **Security** | `argon2-cffi` 25.1.0 (password hashing), `argon2-cffi-bindings` 25.1.0, `cffi` 2.0.0 (C bindings), `pycparser` 2.23 (C parser) |

---

### Utilities Varie

| Pacchetto | Versione | Scopo |
|-----------|----------|-------|
| `arrow` | 1.4.0 | Date/time user-friendly |
| `babel` | 2.17.0 | Internazionalizzazione (i18n) |
| `six` | 1.17.0 | Compatibilità Python 2/3 (legacy) |
| `Send2Trash` | 2.1.0 | Delete sicuro file (trash, non rm) |
| `prometheus_client` | 0.24.1 | Metriche (monitoring Jupyter) |
| `python-json-logger` | 4.0.0 | Logging formato JSON |
| `Pygments` | 2.19.2 | Syntax highlighting generale |
| `charset-normalizer` | 3.4.4 | Rilevamento encoding |
| `tzdata` | 2025.3 | Database timezone |
| `rpds-py` | 0.30.0 | Strutture dati persistenti (Rust-based) |

---

## 🔧 Comandi di Installazione Eseguiti

```powershell
# Setup iniziale Jupyter (durante chat)
pip install jupyter notebook --break-system-packages

# Data Science stack
pip install numpy pandas matplotlib --break-system-packages

# Jupyter extras
pip install jupyturtle --break-system-packages

# Testing framework
pip install pytest --break-system-packages
```

**Note:**
- Tutte le installazioni richiedono flag `--break-system-packages` (sistema specifico)
- Molti pacchetti installati automaticamente come dipendenze (es. numpy tira scipy deps)
- `pip` auto-aggiorna se versione outdated

---

## 📂 File Snapshot di Riferimento

- **`pip_snapshot_complete_20260120.txt`** - Output `pip freeze` (formato `package==version`)
- **`pip_list_complete_20260120.txt`** - Output `pip list` (formato tabellare)

**Utilizzo:**
```powershell
# Reinstallare ambiente identico (futuro)
pip install -r pip_snapshot_complete_20260120.txt

# Confrontare con snapshot futuro
pip freeze > new_snapshot.txt
diff pip_snapshot_complete_20260120.txt new_snapshot.txt
```

---

## 🎯 Linee Guida d'Uso

### Avvio Jupyter

```powershell
# Jupyter Notebook (interfaccia classica)
jupyter notebook

# JupyterLab (interfaccia moderna - RACCOMANDATO)
jupyter lab

# Da directory specifica
cd C:\path\to\learning-python\07-BOOKS\02-ThinkPython
jupyter lab
```

**Shortcut browser Jupyter:**
- `Shift+Enter` - Esegui cella e vai alla successiva
- `Ctrl+Enter` - Esegui cella e resta sulla stessa
- `Alt+Enter` - Esegui cella e inserisci nuova sotto
- `A` - Inserisci cella sopra (command mode)
- `B` - Inserisci cella sotto (command mode)
- `DD` - Cancella cella (command mode)
- `M` - Converti a Markdown (command mode)
- `Y` - Converti a Code (command mode)

### Testing con Pytest

```powershell
# Esegui tutti i test nella directory
pytest

# Esegui test specifico
pytest test_file.py

# Verbose output
pytest -v

# Stop al primo fallimento
pytest -x

# Coverage (richiede pytest-cov, da installare)
# pip install pytest-cov --break-system-packages
# pytest --cov=module_name
```

### Verifica Pacchetti

```powershell
# Lista tutti i pacchetti
pip list

# Cerca pacchetto specifico
pip list | Select-String "numpy"

# Info dettagliate pacchetto
pip show numpy

# Verifica versione da Python
python -c "import numpy; print(numpy.__version__)"
```

---

## 📊 Statistiche Ambiente

```
Totale Pacchetti Installati: 107
├─ Data Science Core: 4 (numpy, pandas, matplotlib, pillow)
├─ Jupyter Ecosystem: 30+ (server, kernel, UI, widgets)
├─ Testing: 1 (pytest + 3 deps)
├─ Networking: 10+
├─ Parsing/Serialization: 15+
├─ Dev Tools: 8+
└─ Utilities: 40+ (deps varie)

Dimensione Stimata: ~500-700 MB
```

---

## 🚀 Pacchetti da Aggiungere in Futuro

### Code Quality (Rinviati per Ora)

```powershell
# Formatter automatico (PEP 8)
pip install black --break-system-packages

# Linter avanzato
pip install pylint --break-system-packages

# Type checker
pip install mypy --break-system-packages
```

**Motivazione rinvio:** Priorità su apprendimento fondamenti, quality tools in Fase 2.

### Testing Extras

```powershell
# Code coverage
pip install pytest-cov --break-system-packages

# Mocking
pip install pytest-mock --break-system-packages
```

### Notebook Tools

```powershell
# Diff/merge notebook per Git
pip install nbdime --break-system-packages

# Dopo installazione, configurare Git:
nbdime config-git --enable --global
```

### Scientific Computing (Fase 2-3)

```powershell
# Algoritmi scientifici avanzati
pip install scipy --break-system-packages

# Plotting statistico elegante
pip install seaborn --break-system-packages

# Plotting interattivo (PCC Part II)
pip install plotly --break-system-packages
```

---

## 🔄 Piano Migrazione Futura

**Fase 2** introdurrà gestione ambienti isolati:

### Opzione A: Conda Environment

```powershell
# Creare ambiente
conda create -n learning_python python=3.12

# Attivare
conda activate learning_python

# Installare da file
conda env export > environment.yml
```

### Opzione B: Python venv

```powershell
# Creare venv nella root progetto
cd learning-python
python -m venv .venv

# Attivare (Windows)
.\.venv\Scripts\Activate.ps1

# Installare da requirements
pip install -r requirements.txt
```

**Documentazione migrazione:** `VIRTUAL_ENVIRONMENTS.md` (da creare in Fase 2)

---

## 📝 Note e Osservazioni

### Scelte Tecniche

1. **Ambiente globale vs virtuale:**  
   Scelta consapevole per apprendimento lineare. I rischi (conflitti versione) sono monitorati ma accettati. Migrazione pianificata quando competenze consolidate.

2. **Jupyter già presente:**  
   Installato durante sessione di apprendimento su Jupyter architecture. Setup completo con entrambe interfacce (classic + lab).

3. **Pip aggiornato a 25.3:**  
   Versione molto recente (Gennaio 2026). Garantisce compatibilità con ultime features Python 3.12.

4. **NumPy 2.4.1:**  
   Major version 2.x (breaking changes da 1.x). Compatibilità verificata con pandas 2.3.3 e matplotlib 3.10.8.

5. **Pytest 9.0.2:**  
   Ultima major version. Supporto completo Python 3.12, async testing nativo.

### Compatibilità e Warning

- **Windows specifico:** Alcuni pacchetti hanno versioni Windows-only (`pywinpty`, `colorama` esteso)
- **Flag `--break-system-packages`:** Necessario su questa installazione, probabilmente Python system-wide o protezione package manager OS
- **Pillow presente:** Installato automaticamente da matplotlib (dipendenza), utile per future image processing

### Best Practices Adottate

✅ Snapshot regolari (`pip freeze`)  
✅ Documentazione dettagliata installazioni  
✅ Versioning esplicito nei file requirements  
✅ Separazione logica pacchetti (core vs utils vs dev)  
✅ Git-friendly (`.txt` files versionabili)  

---

## ✅ Checklist Verifica Setup

Eseguire dopo ogni modifica ambiente:

```powershell
# ✅ Python disponibile
python --version

# ✅ Pip funzionante
pip --version

# ✅ Jupyter operativo
jupyter --version
jupyter lab --version

# ✅ Data Science stack
python -c "import numpy, pandas, matplotlib; print('✓ Stack OK')"

# ✅ Jupyter extras
python -c "import jupyturtle; print('✓ Jupyturtle OK')"

# ✅ Testing
pytest --version

# ✅ Git configurato (se nbdime installato)
# git config --global --get diff.tool
```

---

## 📅 Log Modifiche

| Data | Azione | Pacchetti Aggiunti | Note |
|------|--------|-------------------|------|
| 2026-01-20 | Setup iniziale | jupyter, notebook, jupyterlab | Durante sessione learning Jupyter |
| 2026-01-20 | Data science stack | numpy, pandas, matplotlib | Preparazione Think Python + PCC |
| 2026-01-20 | Jupyter extras | jupyturtle | Think Python Cap. 4 (turtle graphics) |
| 2026-01-20 | Testing | pytest | Preparazione PCC Cap. 11 |
| 2026-01-20 | Snapshot | - | Primo snapshot completo (107 pkg) |

---

## 🎓 Riferimenti e Risorse

**Documentazione Ufficiale:**
- [Python 3.12 Docs](https://docs.python.org/3.12/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Pytest Documentation](https://docs.pytest.org/)