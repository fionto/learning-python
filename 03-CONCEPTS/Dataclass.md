# Dataclass: Dalla Struttura Manuale alla Gestione Automatizzata

## Introduzione: Perché Dataclass?

Finora nei tuoi progetti hai usato dizionari per rappresentare strutture dati complesse. Un dizionario è flessibile, ma ha limitazioni evidenti non appena i dati crescono di complessità. Non hai type hints, non hai validazione automatica, e il codice diventa difficile da leggere quando navighi strutture annidate.

```python
# Approccio dizionario (quello che usi adesso)
campione = {
    "id": "id-2021",
    "nome": "mArS_sOiL-sAmPlE",
    "valore_misurato": 12.500,
    "errore": 0.15,
    "data": "2024-01-15",
    "unità": "ppm"
}

# Accesso confuso, nessuna validazione
print(campione["valore_misurato"])
```

Le classi tradizionali risolvono questi problemi, ma richiedono boilerplate:

```python
# Approccio classe tradizionale (troppo verbose)
class Campione:
    def __init__(self, id, nome, valore_misurato, errore, data, unità):
        self.id = id
        self.nome = nome
        self.valore_misurato = valore_misurato
        self.errore = errore
        self.data = data
        self.unità = unità
    
    def __repr__(self):
        return f"Campione(id={self.id!r}, nome={self.nome!r}, ...)"
```

**Dataclass** è il compromesso ideale: ottieni i benefici delle classi (type hints, validazione, leggibilità) con la sintassi concisa dei dizionari.

```python
# Approccio dataclass (il nuovo standard)
from dataclasses import dataclass

@dataclass
class Campione:
    id: str
    nome: str
    valore_misurato: float
    errore: float
    data: str
    unità: str = "ppm"  # default value

# Uso naturale
campione = Campione("id-2021", "mArS_sOiL-sAmPlE", 12.500, 0.15, "2024-01-15")
print(campione)  # Campione(id='id-2021', nome='mArS_sOiL-sAmPlE', ...)
```

---

## Parte 1: Fondamentali di Dataclass

### Struttura Base e Type Hints

Una dataclass è una classe decorata con `@dataclass` dove gli attributi sono dichiarati con type hints. Python genera automaticamente `__init__()`, `__repr__()`, e altri metodi.

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: float
    y: float
    z: float

# Creazione istanza
p = Punto(1.5, 2.0, 3.5)
print(p)  # Punto(x=1.5, y=2.0, z=3.5)
print(p.x, p.y, p.z)  # 1.5 2.0 3.5
```

I type hints non solo documentano il codice, ma permettono controllo statico con `mypy`:

```bash
$ mypy script.py  # Verifica type consistency
```

### Valori Predefiniti

Gli attributi possono avere valori di default. Gli attributi con default devono venire dopo quelli senza:

```python
@dataclass
class Misura:
    id: str
    valore: float
    unità: str = "ppm"  # default
    qualità: str = "buona"  # default

# Creazione con default
m1 = Misura("id-001", 42.5)
print(m1)  # Misura(id='id-001', valore=42.5, unità='ppm', qualità='buona')

# Sovrascrittura di default
m2 = Misura("id-002", 50.0, unità="mg/L", qualità="sospetta")
```

Se hai molti default, usa `field()` per maggiore controllo:

```python
from dataclasses import dataclass, field

@dataclass
class Esperimento:
    nome: str
    campioni: list = field(default_factory=list)  # Evita mutable default pitfall
    timestamp: str = field(default_factory=lambda: "non_inizializzato")

# Ognuna istanza avrà lista campioni DIVERSA (non condivisa)
exp1 = Esperimento("exp1")
exp1.campioni.append("A")
exp2 = Esperimento("exp2")
print(exp2.campioni)  # [] (non ["A"])
```

**Regola d'oro**: non usare mai `list`, `dict`, o `set` mutabili come default diretto. Usa sempre `field(default_factory=...)`.

### Dataclass Annidate

Le dataclass possono contenere altre dataclass. Questa è la chiave per strutturare dati complessi in modo leggibile:

```python
from dataclasses import dataclass

@dataclass
class Errore:
    valore: float
    unità: str = "percentuale"

@dataclass
class Misura:
    id: str
    risultato: float
    errore: Errore  # Annidata!

# Creazione
e = Errore(0.15, "percentuale")
m = Misura("m-001", 42.5, e)
print(m)  # Misura(id='m-001', risultato=42.5, errore=Errore(valore=0.15, unità='percentuale'))
print(m.errore.valore)  # 0.15
```

Questo è **equivalente a un dizionario annidato**, ma molto più leggibile e type-safe:

```python
# Vecchio stile (dict annidato)
misura_dict = {
    "id": "m-001",
    "risultato": 42.5,
    "errore": {
        "valore": 0.15,
        "unità": "percentuale"
    }
}
print(misura_dict["errore"]["valore"])  # Fragile: KeyError risk

# Nuovo stile (dataclass annidato)
# print(misura.errore.valore)  # Safe, type-checked
```

---

## Parte 2: Migrazione Sistematica da Dict a Dataclass

### Step 1: Identificare la Struttura

Prendi uno dei tuoi progetti (per es. il `Bio-Informatic Parser`) e identifica la struttura dict che usi:

```python
# Struttura attuale (dict)
record = {
    "id_grezzo": "id-2021",
    "nome_campione": "mArS_sOiL-sAmPlE",
    "valore_misurato": 12.500,
    "errore_strumento": 0.15,
    "codice_univoco": "m_sO",
    "range_validi": (12.35, 12.65)  # tupla min/max
}
```

### Step 2: Convertire a Dataclass

Converte il dict in una dataclass con gli stessi campi:

```python
from dataclasses import dataclass

@dataclass
class RecordBioInfoSample:
    id_grezzo: str
    nome_campione: str
    valore_misurato: float
    errore_strumento: float
    codice_univoco: str
    range_min: float  # Spezza la tupla in due field
    range_max: float

# Creazione equivalente a dict precedente
record = RecordBioInfoSample(
    id_grezzo="id-2021",
    nome_campione="mArS_sOiL-sAmPlE",
    valore_misurato=12.500,
    errore_strumento=0.15,
    codice_univoco="m_sO",
    range_min=12.35,
    range_max=12.65
)

# Accesso (identico al dict, ma type-safe)
print(record.valore_misurato)  # 12.500
```

### Step 3: Aggiungere Logica di Validazione

Una volta migrato a dataclass, puoi aggiungere metodi che in dict non sarebbero naturali:

```python
from dataclasses import dataclass

@dataclass
class RecordBioInfoSample:
    id_grezzo: str
    nome_campione: str
    valore_misurato: float
    errore_strumento: float
    codice_univoco: str
    range_min: float
    range_max: float
    
    # Metodo: Verifica se valore è in range
    def in_range(self) -> bool:
        return self.range_min <= self.valore_misurato <= self.range_max
    
    # Metodo: Calcola il range assoluto
    def calcola_range_assoluto(self) -> tuple[float, float]:
        min_possibile = self.valore_misurato - self.errore_strumento
        max_possibile = self.valore_misurato + self.errore_strumento
        return (min_possibile, max_possibile)

# Uso
record = RecordBioInfoSample(
    id_grezzo="id-2021",
    nome_campione="mArS_sOiL-sAmPlE",
    valore_misurato=12.500,
    errore_strumento=0.15,
    codice_univoco="m_sO",
    range_min=12.35,
    range_max=12.65
)

print(record.in_range())  # True
print(record.calcola_range_assoluto())  # (12.35, 12.65)
```

### Step 4: Post-Init e Validazione Automatica

Per validazione complessa al momento della creazione, usa `__post_init__()`:

```python
from dataclasses import dataclass

@dataclass
class RecordBioInfoSample:
    id_grezzo: str
    nome_campione: str
    valore_misurato: float
    errore_strumento: float
    codice_univoco: str
    range_min: float
    range_max: float
    
    def __post_init__(self):
        # Validazione eseguita DOPO __init__()
        if self.errore_strumento < 0:
            raise ValueError(f"Errore non può essere negativo: {self.errore_strumento}")
        
        if self.range_min >= self.range_max:
            raise ValueError(f"range_min ({self.range_min}) >= range_max ({self.range_max})")
        
        # Puoi anche modificare attributi
        self.nome_campione = self.nome_campione.title()

# Creazione con validazione
try:
    bad = RecordBioInfoSample(
        id_grezzo="id-2021",
        nome_campione="mArS_sOiL",
        valore_misurato=12.5,
        errore_strumento=-0.15,  # ERRORE
        codice_univoco="m_sO",
        range_min=12.0,
        range_max=13.0
    )
except ValueError as e:
    print(f"Validazione fallita: {e}")
```

---

## Parte 3: Operazioni Comuni con Dataclass

### Conversione Bidireccionale Dict ↔ Dataclass

Puoi convertire facilmente tra dict e dataclass:

```python
from dataclasses import dataclass, asdict, astuple

@dataclass
class Campione:
    id: str
    valore: float
    unità: str = "ppm"

# Dataclass → Dict
campione = Campione("id-001", 42.5)
d = asdict(campione)
print(d)  # {'id': 'id-001', 'valore': 42.5, 'unità': 'ppm'}

# Dict → Dataclass
d2 = {"id": "id-002", "valore": 50.0, "unità": "mg/L"}
campione2 = Campione(**d2)
print(campione2)  # Campione(id='id-002', valore=50.0, unità='mg/L')

# Dataclass → Tupla
t = astuple(campione)
print(t)  # ('id-001', 42.5, 'ppm')
```

### Immutabilità con `frozen=True`

Per prevenire modifiche accidentali agli attributi dopo creazione:

```python
from dataclasses import dataclass

@dataclass(frozen=True)  # Immutabile
class ConfigurazioneLaboratorio:
    nome_lab: str
    responsabile: str
    data_calibrazione: str

config = ConfigurazioneLaboratorio("Lab A", "Prof. Rossi", "2024-01-15")

# Tentativo di modifica fallisce
try:
    config.responsabile = "Prof. Bianchi"  # FrozenInstanceError
except AttributeError as e:
    print(f"Errore: {e}")
```

### Uguaglianza e Ordinamento

Dataclass implementa automaticamente `__eq__()`:

```python
from dataclasses import dataclass

@dataclass
class Misura:
    id: str
    valore: float

m1 = Misura("m-001", 42.5)
m2 = Misura("m-001", 42.5)
m3 = Misura("m-002", 42.5)

print(m1 == m2)  # True (stessi valori)
print(m1 is m2)  # False (istanze diverse)
print(m1 == m3)  # False (id diverso)
```

Per ordinamento, aggiungi `order=True`:

```python
from dataclasses import dataclass

@dataclass(order=True)
class Misura:
    data: str  # Ordinamento per primo campo
    id: str
    valore: float

m1 = Misura("2024-01-15", "m-001", 42.5)
m2 = Misura("2024-01-16", "m-002", 50.0)
m3 = Misura("2024-01-14", "m-003", 35.0)

misure = [m1, m2, m3]
misure_ordinate = sorted(misure)
for m in misure_ordinate:
    print(m)
# 2024-01-14, 2024-01-15, 2024-01-16
```

---

## Parte 4: Integrazione con NumPy

### Caricamento da Strutture NumPy

NumPy è essenziale per analisi scientifica. Le dataclass si integrano naturalmente con array NumPy:

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class SequenzaSpettrale:
    label: str
    lunghezze_d_onda: np.ndarray  # Array 1D
    intensità: np.ndarray         # Array 1D
    errori: np.ndarray            # Array 1D
    
    def __post_init__(self):
        # Validazione forme
        if not (self.lunghezze_d_onda.shape == self.intensità.shape == self.errori.shape):
            raise ValueError("Array devono avere stessa forma")
    
    def rapporto_segnale_rumore(self) -> float:
        """Calcola SNR medio"""
        return np.mean(self.intensità / np.maximum(self.errori, 1e-10))

# Uso
lambda_vals = np.array([400, 450, 500, 550, 600])  # nm
intensità = np.array([100, 150, 200, 180, 120])
errori = np.array([5, 7, 10, 9, 6])

spettro = SequenzaSpettrale("sample-001", lambda_vals, intensità, errori)
print(spettro.rapporto_segnale_rumore())  # ~25.0

# Accesso ai dati
print(spettro.intensità[2])  # 200
print(spettro.lunghezze_d_onda[-1])  # 600
```

### Conversione: Dataclass ← → NumPy Strutturato

Per dati tabulari, puoi usare NumPy structured arrays:

```python
from dataclasses import dataclass, fields, asdict
import numpy as np

@dataclass
class Campione:
    id: str
    temperatura: float
    pressione: float
    conduttività: float

# Crea lista di dataclass
campioni = [
    Campione("s1", 25.0, 1.0, 0.5),
    Campione("s2", 26.0, 1.1, 0.6),
    Campione("s3", 24.5, 0.9, 0.48),
]

# Converti a NumPy structured array
data_list = [asdict(c) for c in campioni]
dtype = [('id', 'U10'), ('temperatura', 'f8'), ('pressione', 'f8'), ('conduttività', 'f8')]
arr = np.array([(d['id'], d['temperatura'], d['pressione'], d['conduttività']) for d in data_list], dtype=dtype)

print(arr)
# [('s1', 25. , 1. , 0.5) ('s2', 26. , 1.1, 0.6) ('s3', 24.5, 0.9, 0.48)]

# Accesso colonna
print(arr['temperatura'])  # [25.  26.  24.5]
print(np.mean(arr['temperatura']))  # 25.1666...
```

---

## Parte 5: Integrazione con Pandas

### Caricamento da CSV → Dataclass

Pandas legge CSV e puoi convertire direttamente a dataclass:

```python
from dataclasses import dataclass, field
import pandas as pd
from typing import List

@dataclass
class Campione:
    id: str
    temperatura: float
    pressione: float
    conduttività: float

@dataclass
class EsperimentoDataFrame:
    nome_esperimento: str
    campioni: List[Campione] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.campioni:
            raise ValueError("Campioni non può essere vuoto")

# Leggi da CSV
df = pd.read_csv("dati_spettrometro.csv")
# id,temperatura,pressione,conduttività
# s1,25.0,1.0,0.5
# s2,26.0,1.1,0.6
# s3,24.5,0.9,0.48

# Converti righe a dataclass
campioni = [
    Campione(
        id=row['id'],
        temperatura=row['temperatura'],
        pressione=row['pressione'],
        conduttività=row['conduttività']
    )
    for idx, row in df.iterrows()
]

esperimento = EsperimentoDataFrame("Exp-2024-01-15", campioni)
print(esperimento)
```

### Dataclass → DataFrame

Converti dataclass in DataFrame per analisi:

```python
from dataclasses import dataclass, asdict
import pandas as pd

@dataclass
class Misura:
    id: str
    valore: float
    unità: str
    data: str

# Crea lista di misure
misure = [
    Misura("m-001", 42.5, "ppm", "2024-01-15"),
    Misura("m-002", 50.0, "mg/L", "2024-01-16"),
    Misura("m-003", 38.2, "ppm", "2024-01-17"),
]

# Converti a DataFrame
df = pd.DataFrame([asdict(m) for m in misure])

print(df)
#       id  valore    unità        data
# 0  m-001    42.5      ppm  2024-01-15
# 1  m-002    50.0     mg/L  2024-01-16
# 2  m-003    38.2      ppm  2024-01-17

# Operazioni pandas
print(df['valore'].mean())  # 43.566...
print(df.groupby('unità')['valore'].agg(['mean', 'std']))
#        mean  std
# unità
# mg/L   50.0  NaN
# ppm    40.35  3.03...
```

### Analisi Avanzata con Dataclass + Pandas

```python
from dataclasses import dataclass
import pandas as pd
import numpy as np

@dataclass
class TelemetriaTermale:
    timestamp: str
    temperatura_core: float
    temperatura_involucro: float
    flusso_refrigerante: float
    pressione: float

# Simula caricamento dati
np.random.seed(42)
dati = [
    TelemetriaTermale(
        timestamp=f"2024-01-15 {i:02d}:00",
        temperatura_core=70 + np.random.normal(0, 2),
        temperatura_involucro=60 + np.random.normal(0, 1.5),
        flusso_refrigerante=100 + np.random.normal(0, 5),
        pressione=1.2 + np.random.normal(0, 0.05)
    )
    for i in range(24)
]

# Converti a DataFrame
df = pd.DataFrame([vars(t) for t in dati])

# Analisi: rileva anomalie
media_core = df['temperatura_core'].mean()
std_core = df['temperatura_core'].std()
anomalie = df[df['temperatura_core'] > media_core + 2*std_core]

print(f"Media temperatura core: {media_core:.2f}°C")
print(f"Anomalie rilevate: {len(anomalie)}")
print(anomalie[['timestamp', 'temperatura_core']])
```

---

## Parte 6: Best Practices e Pattern Avanzati

### Inheritance tra Dataclass

Puoi ereditare da dataclass per estendere strutture:

```python
from dataclasses import dataclass

@dataclass
class MisuraBase:
    id: str
    valore: float
    unità: str

@dataclass
class MisuraConErrore(MisuraBase):
    errore: float  # Campo aggiuntivo
    data: str = "non-specificata"

m = MisuraConErrore("m-001", 42.5, "ppm", 0.15, "2024-01-15")
print(m)  # MisuraConErrore(id='m-001', valore=42.5, unità='ppm', errore=0.15, data='2024-01-15')
```

### Serializzazione JSON

Dataclass non serializza direttamente a JSON, ma è facile aggiungere il metodo:

```python
from dataclasses import dataclass, asdict
import json
from datetime import datetime

@dataclass
class Esperimento:
    nome: str
    data: datetime
    descrizione: str
    risultati: list

# Metodo custom per serializzazione
def dataclass_to_json(obj):
    """Serializza dataclass a JSON, gestendo datetime"""
    d = asdict(obj)
    if isinstance(obj.data, datetime):
        d['data'] = obj.data.isoformat()
    return json.dumps(d, indent=2)

exp = Esperimento(
    nome="Exp-2024-001",
    data=datetime.now(),
    descrizione="Analisi spettrale",
    risultati=[42.5, 50.0, 38.2]
)

json_str = dataclass_to_json(exp)
print(json_str)
# {
#   "nome": "Exp-2024-001",
#   "data": "2024-01-15T14:30:45.123456",
#   "descrizione": "Analisi spettrale",
#   "risultati": [42.5, 50.0, 38.2]
# }
```

### Validazione tramite Libreria `pydantic` (Preview)

Per validazione rigorosa, la libreria `pydantic` estende dataclass:

```python
# pip install pydantic

from pydantic import BaseModel, Field, validator
from typing import Optional

class Campione(BaseModel):
    id: str = Field(..., min_length=1)
    temperatura: float = Field(..., ge=-50, le=150)  # -50 <= temp <= 150
    descrizione: Optional[str] = None
    
    @validator('id')
    def id_deve_essere_alfanumerico(cls, v):
        if not v.replace('-', '').isalnum():
            raise ValueError('id deve contenere solo lettere, numeri, trattini')
        return v

# Uso
try:
    bad = Campione(id="", temperatura=200)  # Fallisce validazione
except ValueError as e:
    print(f"Errore: {e}")

good = Campione(id="s-001", temperatura=25.5)
print(good)
```

---

## Conclusione

**Dataclass è il punto di incontro ideale** tra semplicità e potenza. Ti permette di:

1. **Abbandonare gradualmente dict**, mantenendo codice ancora leggibile
2. **Aggiungere type hints** per documentazione e controllo statico
3. **Implementare validazione** tramite `__post_init__()`
4. **Integrarsi naturalmente** con NumPy e Pandas
5. **Scalare progetti** con ereditarietà e composizione

Il passo successivo, quando i dati diventano molto strutturati e la validazione diventa critica, è passare a `pydantic` o altre librerie specializzate. Ma per il 90% dei tuoi progetti scientifici, dataclass sarà lo strumento perfetto.

---

## Appendice: Quick Reference

```python
from dataclasses import dataclass, field, asdict, astuple, fields

# Base
@dataclass
class Misurazione:
    id: str
    valore: float
    unità: str = "ppm"

# Con default factory (mutable)
@dataclass
class Esperimento:
    nome: str
    campioni: list = field(default_factory=list)

# Frozen (immutabile)
@dataclass(frozen=True)
class Configurazione:
    parametro: str

# Con validazione
@dataclass
class Record:
    id: str
    valore: float
    
    def __post_init__(self):
        if self.valore < 0:
            raise ValueError("Valore non può essere negativo")

# Conversioni
obj = Misurazione("m-001", 42.5)
d = asdict(obj)  # → dict
t = astuple(obj)  # → tupla
obj2 = Misurazione(**d)  # ← from dict

# Con NumPy/Pandas
import numpy as np
import pandas as pd

@dataclass
class Spettro:
    lunghezze_onda: np.ndarray
    intensità: np.ndarray

df = pd.DataFrame([asdict(obj) for obj in lista_oggetti])
```
