# Il Modulo CSV di Python - Guida Completa

## Introduzione: Perché un Modulo Dedicato?

Abbiamo appena imparato a leggere e scrivere file di testo usando `open()` e i metodi `.read()`, `.readline()`, `.write()`. Se volessimo processare un file CSV (comma-separated values) usando solo questi strumenti, dovremmo farlo manualmente:

```python
# Modo manuale (senza csv module)
with open('dati.csv') as f:
    intestazione = f.readline().strip().split(',')
    for riga in f:
        valori = riga.strip().split(',')
        # Ora devo gestire manualmente i casi speciali:
        # E se un valore contiene una virgola? ("Mario, detto "il grande"")
        # E se contiene newline?
        # E se il delimitatore non è una virgola ma un punto e virgola?
```

Questo approccio diventa rapidamente fragile. Il modulo `csv` della libreria standard **risolve tutti questi problemi** per voi, gestendo i casi edge (valori con virgole, newline, delimitatori variabili, caratteri speciali) in modo robusto e testato.

---

## Importare il Modulo

È semplicissimo:

```python
import csv
```

Non dovete installare nulla. Il modulo è già parte di Python.

---

## Lettura di File CSV: Il Metodo Semplice

### Il DictReader - Leggere come Dizionari

Il modo più "pythonic" di leggere CSV è usare `csv.DictReader`, che converte ogni riga in un dizionario invece che in una lista. Questo rende il codice molto più leggibile:

```python
import csv

# Supponiamo di avere un file vendite.csv:
# prodotto,quantita,prezzo
# Mela,100,0.50
# Banana,150,0.30
# Arancia,80,0.60

with open('vendite.csv') as f:
    reader = csv.DictReader(f)
    
    for riga in reader:
        # riga è un dizionario!
        # riga = {'prodotto': 'Mela', 'quantita': '100', 'prezzo': '0.50'}
        
        print(f"{riga['prodotto']}: {riga['quantita']} unità")
```

Notate come accedete ai dati per **nome di colonna** invece che per indice. Questo rende il codice self-documenting: chiunque legga il vostro codice sa istantaneamente che state accedendo a `'prodotto'` e `'quantita'`.

### Come Funziona DictReader

`DictReader` fa due cose importanti:

1. **Legge la prima riga come header**: Assume che la prima riga contiene i nomi delle colonne.
2. **Restituisce dizionari**: Ogni riga successiva diventa un dizionario dove le chiavi sono i nomi delle colonne.

Se il vostro file CSV **non** ha un header (la prima riga è data, non nomi di colonna), potete specificare i nomi manualmente:

```python
# File senza header
# Mela,100,0.50
# Banana,150,0.30

fieldnames = ['prodotto', 'quantita', 'prezzo']

with open('vendite_no_header.csv') as f:
    reader = csv.DictReader(f, fieldnames=fieldnames)
    
    for riga in reader:
        print(f"{riga['prodotto']}: {riga['quantita']} unità")
```

### Un Esempio Più Realistico

Prendiamo un CSV di studenti e calcoliamo la media dei voti:

```python
import csv

with open('studenti.csv') as f:
    reader = csv.DictReader(f)
    
    totale_voti = 0
    numero_studenti = 0
    
    for riga in reader:
        nome = riga['nome']
        voto = float(riga['voto'])  # Convertite a float per calcoli
        
        totale_voti += voto
        numero_studenti += 1
        
        # Logica: se voto < 6, segnalate
        if voto < 6:
            print(f"⚠ {nome} ha voto insufficiente: {voto}")
    
    media = totale_voti / numero_studenti if numero_studenti > 0 else 0
    print(f"\nMedia voti: {media:.2f}")
```

---

## Lettura di File CSV: Il Metodo Tradizionale

Se preferite list invece di dict, usate `csv.reader`:

```python
import csv

with open('vendite.csv') as f:
    reader = csv.reader(f)
    
    # Saltate l'intestazione manualmente
    next(reader)
    
    for riga in reader:
        # riga è una lista: ['Mela', '100', '0.50']
        prodotto, quantita, prezzo = riga
        print(f"{prodotto}: {quantita} unità a €{prezzo}")
```

Qui `riga` è una lista, non un dizionario. Accedete con indici: `riga[0]`, `riga[1]`, etc.

**Quando usare `reader` vs `DictReader`?**
- Usate `DictReader` (il nuovo metodo) quando il CSV ha un header o quando volete codice leggibile
- Usate `reader` (il metodo tradizionale) solo per CSV semplici o quando vi piacciono le liste

La nostra raccomandazione: **usate quasi sempre `DictReader`**, è più robusto.

---

## Scrittura di File CSV

### Il DictWriter - Scrivere Dizionari

Analogamente a `DictReader`, potete usare `csv.DictWriter` per scrivere CSV in modo elegante:

```python
import csv

# Dati da scrivere
studenti = [
    {'nome': 'Alice', 'voto': 8.5},
    {'nome': 'Bob', 'voto': 7.0},
    {'nome': 'Carol', 'voto': 9.0},
]

# Scrivete il CSV
with open('risultati.csv', 'w', newline='') as f:
    fieldnames = ['nome', 'voto']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    # Scrivete l'intestazione
    writer.writeheader()
    
    # Scrivete le righe
    for studente in studenti:
        writer.writerow(studente)
```

Il file risultante sarà:
```
nome,voto
Alice,8.5
Bob,7.0
Carol,9.0
```

**Importante**: Notate il `newline=''` in `open()`. Questo è una peculiarità di CSV: Python consiglia di usare `newline=''` per evitare problemi di interpretazione dei newline su Windows. È un dettaglio tecnico ma importante.

### Il Writer - Scrivere Liste

Se preferite usare liste invece di dizionari:

```python
import csv

dati = [
    ['Alice', 8.5],
    ['Bob', 7.0],
    ['Carol', 9.0],
]

with open('risultati.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Scrivete l'intestazione manualmente
    writer.writerow(['nome', 'voto'])
    
    # Scrivete le righe
    for riga in dati:
        writer.writerow(riga)
```

---

## Delimitatori Non-Standard

Il modulo CSV è molto flessibile. Se il vostro file usa un delimitatore diverso da virgola, potete specificarlo:

```python
import csv

# File con delimitatore semicolon
# nome;età;città
# Alice;30;Roma
# Bob;25;Milano

with open('persone.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    
    for riga in reader:
        print(f"{riga['nome']} vive a {riga['città']}")
```

Delimitatori comuni:
- `','` (virgola - predefinito)
- `';'` (punto e virgola - comune in Europa per decimali)
- `'\t'` (tab - tabulation)
- `'|'` (pipe - usato raramente)

Per scrivere:

```python
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'età'], delimiter=';')
    writer.writeheader()
    writer.writerow({'nome': 'Alice', 'età': 30})
```

---

## Gestione dei Dialetti

CSV ha una variante standardizzata chiamata **Sniffer** che tenta di indovinare il dialetto (delimitatore, quoting style, etc.) di un file sconosciuto:

```python
import csv

# Leggi un file di cui non conosci il formato
with open('mistero.csv') as f:
    # Leggi i primi 1024 byte per analizzare il formato
    sample = f.read(1024)
    
    # Indovina il dialetto
    dialect = csv.Sniffer().sniff(sample)
    
    # Torna all'inizio del file
    f.seek(0)
    
    # Usa il dialetto indovinato
    reader = csv.DictReader(f, dialect=dialect)
    
    for riga in reader:
        print(riga)
```

È utile quando dovete processare file di provenienza sconosciuta.

---

## Caso di Studio Completo: Processare e Trasformare un CSV

Creiamo uno script che legge un CSV di vendite, filtra, trasforma, e scrive un nuovo CSV:

```python
import csv
from pathlib import Path

def processare_vendite(input_file, output_file):
    """
    Legge un file di vendite, filtra le righe con prezzo > 5,
    aggiunge una colonna con il totale, e scrive un nuovo CSV.
    """
    
    vendite_filtrate = []
    
    # Lettura e filtraggio
    try:
        with open(input_file, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Validate che il file abbia le colonne richieste
            if reader.fieldnames is None:
                print("Errore: File CSV vuoto")
                return False
            
            for riga in reader:
                try:
                    # Estrai e converti i dati
                    prodotto = riga['prodotto']
                    quantita = int(riga['quantita'])
                    prezzo = float(riga['prezzo'])
                    
                    # Filtra: solo vendite con prezzo > 5
                    if prezzo > 5.0:
                        # Aggiungi una colonna calcolata
                        riga['totale'] = quantita * prezzo
                        vendite_filtrate.append(riga)
                        
                except (ValueError, KeyError) as e:
                    print(f"⚠ Riga non valida: {riga}")
                    continue
    
    except FileNotFoundError:
        print(f"Errore: File '{input_file}' non trovato")
        return False
    
    # Scrittura del file filtrato
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            # Fieldnames del file output: aggiungiamo 'totale'
            fieldnames = ['prodotto', 'quantita', 'prezzo', 'totale']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            for riga in vendite_filtrate:
                writer.writerow(riga)
        
        print(f"✓ File scritto: {output_file}")
        print(f"  Righe elaborate: {len(vendite_filtrate)}")
        return True
    
    except PermissionError:
        print(f"Errore: Non hai permessi per scrivere '{output_file}'")
        return False

# Utilizzo
if __name__ == '__main__':
    successo = processare_vendite('vendite.csv', 'vendite_filtrate.csv')
    exit(0 if successo else 1)
```

---

## Quoting: Gestione dei Valori Speciali

A volte un valore CSV contiene una virgola o un newline. Il modulo CSV gestisce questo automaticamente avvolgendo il valore in doppi apici:

```python
# File CSV originale
nome,descrizione
Prodotto A,"Un grande prodotto, ottimo!"
Prodotto B,"Una descrizione
con newline"

# Quando leggete con DictReader
import csv
with open('prodotti.csv') as f:
    reader = csv.DictReader(f)
    for riga in reader:
        # riga['descrizione'] avrà automaticamente le virgole interpretate correttamente
        print(riga['descrizione'])
```

Il modulo CSV gestisce automaticamente il quoting. Se dovete scrivere tali valori, vi consiglio di lasciar fare al modulo:

```python
import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'descrizione'])
    writer.writeheader()
    
    # Scrivete valori complessi
    writer.writerow({
        'nome': 'Prodotto A',
        'descrizione': 'Un grande prodotto, ottimo!'  # La virgola sarà gestita
    })
    writer.writerow({
        'nome': 'Prodotto B',
        'descrizione': 'Una descrizione\ncon newline'  # Il newline sarà gestito
    })
```

Il file risultante avrà i valori correttamente quoted dal modulo csv.

---

## Differenza tra csv.reader e csv.DictReader

Ecco un confronto pratico con lo stesso file:

### File: vendite.csv
```
prodotto,quantita,prezzo
Mela,100,0.50
Banana,150,0.30
```

### Usando csv.reader:
```python
import csv

with open('vendite.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Saltate l'intestazione manualmente
    
    for riga in reader:
        # riga è una lista: ['Mela', '100', '0.50']
        print(riga[0], riga[1], riga[2])
```

### Usando csv.DictReader:
```python
import csv

with open('vendite.csv') as f:
    reader = csv.DictReader(f)
    
    for riga in reader:
        # riga è un dizionario
        # {'prodotto': 'Mela', 'quantita': '100', 'prezzo': '0.50'}
        print(riga['prodotto'], riga['quantita'], riga['prezzo'])
```

**Vantaggi di DictReader:**
- Non dovete ricordare l'ordine delle colonne
- Il codice è self-documenting
- Se le colonne vengono riordinate nel CSV, il vostro codice continua a funzionare
- Meno errori di indice

---

## Best Practice Quando Usate CSV

### 1. Specificate Always Encoding

```python
# Buono
with open('dati.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)

# Cattivo
with open('dati.csv') as f:
    reader = csv.DictReader(f)
```

### 2. Usate `newline=''` quando Scrivete

```python
# Buono (per scrittura)
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'età'])

# Cattivo - potrebbe causare righe vuote extra su Windows
with open('output.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'età'])
```

### 3. Convertite i Tipi di Dato

I valori da CSV arrivano sempre come stringhe. Convertiteli se necessario:

```python
# Cattivo: trattiamo tutto come stringhe
for riga in reader:
    total = riga['quantita'] * riga['prezzo']  # StringError!

# Buono: convertiamo
for riga in reader:
    quantita = int(riga['quantita'])
    prezzo = float(riga['prezzo'])
    total = quantita * prezzo  # OK
```

### 4. Gestite i Valori Mancanti

```python
# Cattivo: assume che tutte le colonne siano presenti
for riga in reader:
    print(riga['telefono'])  # KeyError se 'telefono' manca

# Buono: usate .get() con default
for riga in reader:
    telefono = riga.get('telefono', 'N/A')
    print(telefono)
```

### 5. Usate sempre `with` per Context Management

```python
# Buono
with open('dati.csv') as f:
    reader = csv.DictReader(f)
    # Il file è garantito chiuso alla fine

# Cattivo
f = open('dati.csv')
reader = csv.DictReader(f)
f.close()  # Facile dimenticare se accade un'eccezione
```

---

## Esercizio Pratico: Creare e Processare un CSV

Creiamo uno script completo che:
1. Crea un file CSV con dati di esempio
2. Lo legge e filtra
3. Scrive un nuovo CSV con i risultati

```python
import csv
from pathlib import Path

def creare_csv_esempio():
    """Crea un file CSV di esempio con dati di studenti."""
    studenti = [
        {'nome': 'Alice', 'voto_italiano': 8, 'voto_matematica': 9},
        {'nome': 'Bob', 'voto_italiano': 6, 'voto_matematica': 5},
        {'nome': 'Carol', 'voto_italiano': 9, 'voto_matematica': 8},
        {'nome': 'David', 'voto_italiano': 5, 'voto_matematica': 6},
    ]
    
    with open('studenti.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['nome', 'voto_italiano', 'voto_matematica']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(studenti)
    
    print("✓ File studenti.csv creato")

def processare_studenti():
    """Legge il CSV e crea un report con medie e stato."""
    risultati = []
    
    with open('studenti.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for riga in reader:
            nome = riga['nome']
            voto_it = int(riga['voto_italiano'])
            voto_mat = int(riga['voto_matematica'])
            
            media = (voto_it + voto_mat) / 2
            status = '✓ Promosso' if media >= 6 else '✗ Bocciato'
            
            risultati.append({
                'nome': nome,
                'media': f"{media:.1f}",
                'stato': status
            })
    
    # Scrivi il report
    with open('report_studenti.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['nome', 'media', 'stato']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(risultati)
    
    print("✓ File report_studenti.csv creato")
    
    # Stampa a schermo
    print("\n=== REPORT ===")
    for riga in risultati:
        print(f"{riga['nome']}: media {riga['media']} ({riga['stato']})")

if __name__ == '__main__':
    creare_csv_esempio()
    processare_studenti()
```

Esecuzione:
```
$ python script.py
✓ File studenti.csv creato
✓ File report_studenti.csv creato

=== REPORT ===
Alice: media 8.5 (✓ Promosso)
Bob: media 5.5 (✗ Bocciato)
Carol: media 8.5 (✓ Promosso)
David: media 5.5 (✗ Bocciato)
```

---

## Conclusione

Il modulo `csv` della libreria standard è **semplice ma potente**. Vi consiglio di:

1. **Usare `DictReader` per letture** - è più pythonic e meno prono a errori
2. **Usare `DictWriter` per scritture** - simmetrico e coerente
3. **Ricordare `newline=''` in scrittura** - dettaglio tecnico ma importante
4. **Sempre convertire i tipi** - CSV restituisce stringhe
5. **Gestire gli errori** - file non trovati, formato non valido, etc.

Con CSV padroneggiato e File I/O già appreso, siete pronti a lavorare con dati strutturati. Nel prossimo modulo, potremmo esplorare JSON, che è ancora più flessibile.

Happy CSV processing! 📊