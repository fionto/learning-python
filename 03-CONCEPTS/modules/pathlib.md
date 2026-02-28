# Pathlib: Il Filesystem come Oggetti Python

## Il Vecchio Modo di Pensare ai Percorsi

Prima di `pathlib`, in Python gestire i percorsi (path) dei file era una fatica. Si usava il modulo `os.path`, che trattava i percorsi come semplici stringhe:

```python
import os

# Vecchio modo: stringhe concatenate
path = 'home/utente/documenti/relazione.txt'
directory = os.path.dirname(path)
filename = os.path.basename(path)
full_path = os.path.join(directory, 'backup', filename)

# Per fare operazioni semplici, dovete usare tante funzioni diverse
if os.path.exists(full_path):
    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)
```

Questo approccio funziona, ma è **frammentato e poco pythonic**. Dovete ricordare molte funzioni diverse (`dirname`, `basename`, `join`, `exists`, `isfile`, `getsize`), e il concetto di "percorso" non è veramente incapsulato. Un percorso è solo una stringa, senza alcuna struttura.

Inoltre, il vecchio approccio ha un problema critico: **differenze tra sistemi operativi**. Su Windows usate backslash (`\`), su Unix usate forward slash (`/`). Se scrivete codice su Windows e qualcuno lo esegue su Linux, i vostri percorsi potrebbero non funzionare.

## La Filosofia di Pathlib: Path come Oggetti

`pathlib` rappresenta un cambio di paradigma. Invece di trattare i percorsi come stringhe, li tratta come **oggetti veri e propri**. Un path è un oggetto che conosce di se stesso: sa come dividersi in componenti, sa come concatenarsi con altri path, sa come interrogare il filesystem.

```python
from pathlib import Path

# Nuovo modo: Path come oggetto
path = Path('home') / 'utente' / 'documenti' / 'relazione.txt'

# Operazioni naturali
directory = path.parent
filename = path.name
full_path = directory / 'backup' / filename

# Interroga il filesystem con metodi intuitivi
if path.exists():
    if path.is_file():
        size = path.stat().st_size
```

Guardate la differenza:

1. **Uso dell'operatore `/`** per concatenare path: è intuitivo e portabile. Non dovete pensare a quale sia il separatore corretto per il vostro OS.

2. **Proprietà e metodi intuitivi**: `.parent` (la directory contenente), `.name` (il nome del file), `.stat()` (informazioni del file).

3. **Una singola classe** che sa fare tutto, invece di tante funzioni sparse.

Questo è il genio di `pathlib`: cattura il concetto di "percorso nel filesystem" come un oggetto di prima classe in Python, con metodi e proprietà naturali.

---

## Pure Paths vs Concrete Paths: Una Distinzione Importante

`pathlib` distingue tra due concetti:

### Pure Paths: Logica Senza Filesystem

Un **Pure Path** rappresenta un percorso puramente dal punto di vista logico. Non accede al filesystem. Potete creare, dividere, ricombinare path senza che il file esista effettivamente sul disco.

```python
from pathlib import PurePath, PureWindowsPath, PurePosixPath

# Pure path generico (adatta al vostro OS)
pure = PurePath('home/utente/file.txt')

# Pure path specifico per Windows
win_path = PureWindowsPath('C:\\Users\\utente\\file.txt')

# Pure path specifico per Unix
unix_path = PurePosixPath('/home/utente/file.txt')

# Potete usarli per manipolazione logica, anche su un OS diverso
# Ad esempio, convertire path Windows su una macchina Unix per analizzarli
print(win_path.name)      # 'file.txt' - funziona anche su Unix!
print(win_path.parent)    # 'C:\Users\utente'
```

Perché questa distinzione? Immaginate di scrivere uno script che **analizza** file di log da computer Windows, ma lo eseguite su un server Linux. Potete usare `PureWindowsPath` per parsare e manipolare path Windows senza che il file esista effettivamente sul vostro filesystem locale.

### Concrete Paths: Con Accesso al Filesystem

Una **Concrete Path** è quello che userete il 99% delle volte. Rappresenta un percorso reale, e potete usarla per **accedere e manipolare** il filesystem: leggere file, creare directory, cancellare, etc.

```python
from pathlib import Path

# Concrete path - potete interagire col filesystem
path = Path('home/utente/file.txt')

# Queste operazioni accedono al filesystem
if path.exists():
    print(path.stat())
    path.unlink()  # Cancella il file

# Potete anche creare file e directory
new_dir = Path('home/utente/backup')
new_dir.mkdir(parents=True, exist_ok=True)
```

La regola è semplice: **usate `Path` (concrete) per lavoro reale**, `PurePath` per manipolazione astratta di percorsi.

---

## Creare Path: La Filosofia della Concatenazione

Il primo insegnamento di `pathlib` è: **dimenticatevi di concatenare stringhe con `os.path.join()`**.

### L'Operatore `/`: Concatenazione Naturale

L'operatore `/` concatena path in modo elegante e portabile:

```python
from pathlib import Path

# Iniziate con una directory
base = Path('home')

# Concatenate usando /
path = base / 'utente' / 'documenti'

# È come costruire un percorso per passi
path = path / 'sottocartella'
path = path / 'file.txt'

# Potete anche usare stringhe
path = Path('home') / 'utente' / 'my documents' / 'report.pdf'

# Tutto funziona allo stesso modo su Windows, Mac, e Linux
# Python gestisce automaticamente il separatore corretto
```

Perché è meglio? Perché è **leggibile** e **portabile**. Non dovete pensare a quale sia il separatore corretto per il vostro sistema. Python lo sa.

### Path Assoluti vs Relativi

Potete creare path assoluti (da radice) o relativi (da directory corrente):

```python
from pathlib import Path

# Relativo (da directory corrente)
relativo = Path('documenti') / 'file.txt'

# Assoluto (da radice)
assoluto = Path('/home/utente/documenti/file.txt')  # Unix
# o
assoluto = Path('C:') / 'Users' / 'utente' / 'Documents' / 'file.txt'  # Windows

# Potete convertire da relativo ad assoluto
print(relativo.resolve())  # Restituisce il percorso assoluto completo

# Home directory dell'utente (funziona su tutti gli OS)
home = Path.home()
print(home)  # /home/utente (Unix) o C:\Users\utente (Windows)
```

Nota: `Path.home()` è un metodo di classe che restituisce la home directory dell'utente corrente, indipendentemente dal sistema operativo. Molto comodo!

---

## Navigare un Path: Scomposizione in Componenti

Un path può essere scomposto in componenti logici. Questa è la logica dietro i metodi `.parent`, `.name`, `.stem`, `.suffix`.

### Analizzare un Percorso

```python
from pathlib import Path

path = Path('/home/utente/documenti/relazione_2025.pdf')

# Componenti principali
print(path.name)        # 'relazione_2025.pdf' - nome completo del file
print(path.parent)      # '/home/utente/documenti' - directory contente
print(path.stem)        # 'relazione_2025' - nome senza estensione
print(path.suffix)      # '.pdf' - estensione
print(path.suffixes)    # ['.tar', '.gz'] - se sono multiple (es: file.tar.gz)

# Navigare verso l'alto
print(path.parent)          # '/home/utente/documenti'
print(path.parent.parent)   # '/home/utente'
print(path.parent.parent.parent)  # '/home'

# Componenti del percorso come tuple
print(path.parts)  # ('/', 'home', 'utente', 'documenti', 'relazione_2025.pdf')
```

Questi metodi sono straordinariamente utili per manipolare percorsi:

```python
# Creare una copia con estensione diversa
original = Path('foto.jpg')
backup = original.with_suffix('.backup.jpg')
print(backup)  # 'foto.backup.jpg'

# Creare un percorso nella stessa directory con nome diverso
config = Path('/etc/config.txt')
backup_config = config.with_name('config.txt.bak')
print(backup_config)  # '/etc/config.txt.bak'

# Combinare operazioni
archive = Path('archive/2024/dati.tar.gz')
new_archive = archive.with_stem('dati_backup')
print(new_archive)  # 'archive/2024/dati_backup.tar.gz'
```

---

## Interrogare il Filesystem

Uno dei superpoteri di `pathlib` è interrogare il filesystem in modo intuitivo. Invece di usare un milione di funzioni `os.*`, usate metodi sull'oggetto path.

### Controllare Cosa È un Percorso

```python
from pathlib import Path

path = Path('mio_file.txt')

# Che cosa è questo percorso?
if path.exists():
    print("Il percorso esiste")
else:
    print("Il percorso non esiste")

if path.is_file():
    print("È un file regolare")

if path.is_dir():
    print("È una directory")

if path.is_symlink():
    print("È un collegamento simbolico")

if path.is_socket():
    print("È un socket")
```

Questi metodi sono veri e propri: restituiscono `True` o `False`. Sono molto più leggibili che usare `os.path.isfile()` e `os.path.isdir()`.

### Informazioni sul File

```python
from pathlib import Path
import datetime

path = Path('documento.pdf')

if path.exists():
    # Ottenere informazioni del file
    stat_info = path.stat()
    
    print(f"Dimensione: {stat_info.st_size} byte")
    print(f"Proprietario (UID): {stat_info.st_uid}")
    print(f"Modificato: {datetime.datetime.fromtimestamp(stat_info.st_mtime)}")
    print(f"Permessi: {oct(stat_info.st_mode)}")
    
    # Operazioni comuni
    print(f"È leggibile: {path.is_file() and (stat_info.st_mode & 0o400)}")
```

Il metodo `.stat()` restituisce un oggetto `os.stat_result` con tutte le informazioni che il sistema operativo conosce sul file.

---

## Leggere e Scrivere File Direttamente

`pathlib` integra file I/O direttamente nell'oggetto path. Non dovete usare `open()` separatamente se state facendo operazioni semplici:

### Lettura Semplice

```python
from pathlib import Path

path = Path('file.txt')

# Leggi l'intero file come stringa
contenuto = path.read_text(encoding='utf-8')

# Leggi il file come bytes
dati = path.read_bytes()

# Leggi come liste di righe
righe = path.read_text().splitlines()
```

Questi metodi sono comodi per operazioni semplici. Non dovete preoccuparvi di `.close()` - il file viene automaticamente chiuso.

### Scrittura Semplice

```python
from pathlib import Path

path = Path('output.txt')

# Scrivi una stringa
path.write_text('Contenuto nuovo\n', encoding='utf-8')

# Scrivi bytes
path.write_bytes(b'\x00\x01\x02')

# Aggiungi a un file
with open(path, 'a') as f:
    f.write('Riga aggiuntiva\n')
```

**Attenzione**: `.write_text()` e `.write_bytes()` **sovrascrivono** il file se esiste. Usate con cautela!

### Per Operazioni Complesse, Usate `open()`

Per letture/scritture complesse (processare riga per riga, leggere a pezzi, etc.), usate `path.open()`:

```python
from pathlib import Path

path = Path('file_grande.txt')

# Potete usare path.open() come context manager
with path.open('r', encoding='utf-8') as f:
    for riga in f:
        print(riga.strip())

# Oppure
with open(path, 'r', encoding='utf-8') as f:
    for riga in f:
        print(riga.strip())

# Entrambi funzionano! Path è compatibile con open()
```

---

## Navigare le Directory: Glob e Iterdir

### Iterare una Directory

```python
from pathlib import Path

directory = Path('documenti')

# Ottenere tutti gli elementi (file e subdirectory)
for elemento in directory.iterdir():
    print(elemento)
    print(f"  - È file: {elemento.is_file()}")
    print(f"  - È directory: {elemento.is_dir()}")
```

`.iterdir()` restituisce un iteratore (non una lista), il che è efficiente per directory grandi.

### Pattern Matching: Glob

Uno dei superpoteri di `pathlib` è il pattern matching su nomi di file:

```python
from pathlib import Path

directory = Path('documenti')

# Trovare tutti i file PDF
pdf_files = list(directory.glob('*.pdf'))

# Trovare file in subdirectory (ricorsivo)
all_txt = list(directory.glob('**/*.txt'))

# Pattern complessi
# Trovare file che iniziano con 'report'
reports = list(directory.glob('report*.doc*'))

# Trovare file in qualsiasi subdirectory con estensione .csv
all_csv = list(Path('.').glob('**/*.csv'))
```

Glob supporta pattern wildcard:
- `*` - corrisponde a qualsiasi carattere (eccetto `/`)
- `?` - corrisponde a un singolo carattere
- `**` - corrisponde a zero o più directory

```python
from pathlib import Path

base = Path('archivio')

# Esempi pratici
# Tutti i file nella directory corrente
base.glob('*')

# Tutti i file .pdf in qualsiasi subdirectory
base.glob('**/*.pdf')

# Tutti i file che iniziano con "2024"
base.glob('2024*')

# File con nome numerato (es: backup_001.zip, backup_002.zip)
base.glob('backup_[0-9][0-9][0-9].zip')
```

---

## Creare File e Directory

### Creare Directory

```python
from pathlib import Path

# Creare una singola directory
path = Path('nuova_cartella')
path.mkdir()  # Crea la directory

# Se la directory esiste già, genera FileExistsError
# Usate exist_ok=True per evitare l'errore
path.mkdir(exist_ok=True)

# Creare una gerarchia di directory
path = Path('a/b/c/d/e')
path.mkdir(parents=True, exist_ok=True)
# parents=True crea tutti i parent necessari
# Equivalente a mkdir -p su Unix
```

### Creare File

```python
from pathlib import Path

# Creare un file vuoto
path = Path('nuovo_file.txt')
path.touch()

# Se il file esiste, non fa nulla (non lo sovrascrive)
path.touch(exist_ok=True)

# Scrivere subito contenuto
path.write_text('Contenuto iniziale\n')
```

---

## Cancellare e Muovere File

### Cancellare

```python
from pathlib import Path

# Cancellare un file
path = Path('file_da_eliminare.txt')
if path.exists():
    path.unlink()  # unlink = rimuovi il link al file

# Cancellare una directory (deve essere vuota)
directory = Path('cartella_vuota')
directory.rmdir()

# Cancellare ricorsivamente una directory (Python 3.13+)
import shutil
directory = Path('cartella_con_contenuto')
shutil.rmtree(directory)  # Usa shutil per cancellare ricorsivamente
```

### Muovere e Rinominare

```python
from pathlib import Path

# Rinominare un file
original = Path('vecchio_nome.txt')
new_name = Path('nuovo_nome.txt')
original.rename(new_name)

# Muovere un file
source = Path('file.txt')
destination = Path('another_directory/file.txt')
source.rename(destination)

# Copiano un file (usate shutil, pathlib non lo fornisce)
import shutil
source = Path('file.txt')
backup = Path('file.backup.txt')
shutil.copy(source, backup)

# Copiano una directory
import shutil
original_dir = Path('original')
backup_dir = Path('backup_original')
shutil.copytree(original_dir, backup_dir)
```

---

## Casi di Studio: Applicazioni Pratiche

### Case Study 1: Organizzare File per Tipo

Immaginate di avere una directory piena di file di vari tipi e volete organizzarli in subdirectory per estensione:

```python
from pathlib import Path

def organizzare_file(directory_path):
    """Organizza i file in subdirectory per tipo di estensione."""
    directory = Path(directory_path)
    
    if not directory.is_dir():
        print(f"Errore: {directory} non è una directory")
        return
    
    # Iterare su tutti i file
    for file in directory.iterdir():
        if file.is_file():
            # Determinare la subdirectory basata sull'estensione
            if file.suffix:
                subdir_name = file.suffix[1:].upper()  # Rimuovi il punto
            else:
                subdir_name = 'NO_EXTENSION'
            
            # Creare la subdirectory se non esiste
            subdir = directory / subdir_name
            subdir.mkdir(exist_ok=True)
            
            # Muovere il file
            destination = subdir / file.name
            file.rename(destination)
            print(f"Spostato: {file.name} -> {subdir_name}/")

# Utilizzo
organizzare_file('Downloads')
```

### Case Study 2: Trovare Duplicati

Trovare file con lo stesso nome ma in directory diverse:

```python
from pathlib import Path
from collections import defaultdict

def trovare_duplicati(directory_path):
    """Trova file con lo stesso nome in subdirectory diverse."""
    directory = Path(directory_path)
    
    # Mappare nome_file -> lista di path dove esiste
    files_map = defaultdict(list)
    
    for file in directory.glob('**/*'):
        if file.is_file():
            files_map[file.name].append(file)
    
    # Stampare i duplicati
    duplicati = {name: paths for name, paths in files_map.items() if len(paths) > 1}
    
    if duplicati:
        print("File duplicati trovati:")
        for name, paths in duplicati.items():
            print(f"\n{name}:")
            for path in paths:
                size = path.stat().st_size
                print(f"  {path} ({size} byte)")
    else:
        print("Nessun duplicato trovato")
    
    return duplicati

# Utilizzo
trovare_duplicati('archivio')
```

### Case Study 3: Pulire Directory Vecchie

Trovare e cancellare file non modificati da più di N giorni:

```python
from pathlib import Path
import datetime

def pulire_vecchi_file(directory_path, giorni=30):
    """Cancella file non modificati negli ultimi N giorni."""
    directory = Path(directory_path)
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=giorni)
    
    file_cancellati = []
    
    for file in directory.glob('**/*'):
        if file.is_file():
            # Ottenere data di modifica
            mtime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            
            if mtime < cutoff_date:
                print(f"Cancello: {file} (modificato: {mtime})")
                file.unlink()  # Cancella
                file_cancellati.append(file)
    
    print(f"\nFile cancellati: {len(file_cancellati)}")
    return file_cancellati

# Utilizzo (cautela: cancella davvero!)
# pulire_vecchi_file('backup', giorni=60)
```

### Case Study 4: Strutturare Progetti

Creare la struttura di base per un nuovo progetto Python:

```python
from pathlib import Path

def creare_struttura_progetto(nome_progetto):
    """Crea la struttura di base per un progetto Python."""
    base = Path(nome_progetto)
    
    # Creare la gerarchia
    (base / 'src').mkdir(parents=True, exist_ok=True)
    (base / 'tests').mkdir(exist_ok=True)
    (base / 'docs').mkdir(exist_ok=True)
    (base / 'data').mkdir(exist_ok=True)
    
    # Creare file iniziali
    (base / 'README.md').write_text(f"# {nome_progetto}\n")
    (base / 'src' / '__init__.py').touch()
    (base / 'tests' / '__init__.py').touch()
    
    # Gitignore
    (base / '.gitignore').write_text(
        "__pycache__/\n*.pyc\n.venv/\ndist/\nbuild/\n*.egg-info/\n"
    )
    
    print(f"✓ Struttura creata in {base}")
    
    # Mostra la struttura
    for item in base.rglob('*'):
        indent = '  ' * (len(item.relative_to(base).parts) - 1)
        symbol = '📁' if item.is_dir() else '📄'
        print(f"{indent}{symbol} {item.name}")

# Utilizzo
creare_struttura_progetto('mio_progetto')
```

Output:
```
✓ Struttura creata in mio_progetto
📁 mio_progetto
  📁 src
    📄 __init__.py
  📁 tests
    📄 __init__.py
  📁 docs
  📁 data
  📄 README.md
  📄 .gitignore
```

---

## Portabilità: Il Vero Valore di Pathlib

Ecco il vero valore di `pathlib`: **scrivete una volta, funziona dappertutto**.

### Vecchio Modo (fragile):

```python
import os

# Questo funziona su Unix
path = os.path.join('home', 'utente', 'file.txt')

# Su Windows, diventava 'home\\utente\\file.txt'
# Dovevate ricordare di usare sempre join() e mai concatenare stringhe
```

### Nuovo Modo (robusto):

```python
from pathlib import Path

# Funziona su Unix, Windows, macOS
path = Path('home') / 'utente' / 'file.txt'

# Potete anche scrivere:
path = Path.home() / 'documenti' / 'file.txt'

# Per operazioni specifiche per OS, potete controllare:
import sys
if sys.platform == 'win32':
    # Codice specifico Windows
    pass
else:
    # Codice per Unix-like
    pass
```

Ogni volta che usate `/` per concatenare path, Python gestisce automaticamente i separatori corretti per il vostro sistema operativo. Questa è **portabilità vera**.

---

## Pathlib vs os.path: Un Confronto

| Operazione | os.path | pathlib |
|-----------|---------|---------|
| Concatenare percorsi | `os.path.join(a, b)` | `a / b` |
| Nome file | `os.path.basename(path)` | `path.name` |
| Directory | `os.path.dirname(path)` | `path.parent` |
| Estensione | Complicato con split | `path.suffix` |
| Esiste? | `os.path.exists(path)` | `path.exists()` |
| È file? | `os.path.isfile(path)` | `path.is_file()` |
| È directory? | `os.path.isdir(path)` | `path.is_dir()` |
| Creare directory | `os.makedirs(path)` | `path.mkdir(parents=True)` |
| Cancellare file | `os.remove(path)` | `path.unlink()` |
| Rinominare | `os.rename(old, new)` | `old.rename(new)` |
| Leggere file | `open(path); f.read()` | `path.read_text()` |
| Trovare file | `os.listdir()` + filtraggio manuale | `path.glob('*.txt')` |

Come vedete, `pathlib` è **più intuitivo e conciso** per quasi ogni operazione. È la ragione per cui è stata introdotta in Python 3.4 e continua a diventare lo standard.

---

## Best Practice con Pathlib

1. **Usate sempre `pathlib.Path` per lavoro con il filesystem**, non stringhe raw.

2. **Preferite `/` per concatenare path** - è portabile e leggibile.

3. **Usate `.resolve()` quando servono percorsi assoluti** - converte path relativi in assoluti.

4. **Controllate `.exists()` prima di operazioni critiche**:
```python
path = Path('file_importante.txt')
if not path.exists():
    print("Errore: il file non esiste")
    exit(1)
```

5. **Usate `.glob()` per trovare file**, è molto più potente di `.iterdir()`.

6. **Per operazioni complicate, combinate pathlib con other librerie**:
```python
from pathlib import Path
import shutil

source = Path('backup')
destination = Path('restore')
shutil.copytree(source, destination)  # shutil per copie ricorsive
```

7. **Specificate sempre `encoding='utf-8'` quando leggete/scrivete testo**:
```python
path = Path('file.txt')
contenuto = path.read_text(encoding='utf-8')
```

8. **Usate context manager quando fate I/O complesso**:
```python
with path.open('r', encoding='utf-8') as f:
    # Operazioni su file
    pass
```

---

## Conclusione: Pensare a Oggetti, Non a Stringhe

`pathlib` rappresenta un cambio di mentalità: **i percorsi non sono stringhe, sono oggetti con comportamento e responsabilità**.

Questa astrazione:
- **Elimina gli errori** causati da separatori incorretti
- **Rende il codice leggibile** - `.parent` è più chiaro di `os.path.dirname()`
- **Unifica le operazioni** - tutto è incapsulato nel path object
- **Favorisce la portabilità** - scrivete una volta, funziona ovunque

Una volta che iniziate a usare `pathlib`, non tornerete indietro. È uno di quei moduli che sembrano piccolini ma migliorano significativamente la qualità della vostra programmazione.

Quando lavorate con il filesystem, ricordatevi: **`pathlib` first, everything else second**.

Happy path navigation! 🗂️