# Il Modulo `datetime` in Python: Lavorare con Date e Ora

Quando scriviamo programmi, spesso abbiamo bisogno di lavorare con date e orari. Che si tratti di registrare il momento in cui un utente ha eseguito un'azione, di calcolare quanti giorni mancano a una scadenza, o di confrontare due timestamp, il modulo `datetime` è lo strumento che Python mette a nostra disposizione. È un modulo che fa parte della libreria standard, il che significa che non dobbiamo installare nulla: ci aspetta già quando apriamo Python.

In questo capitolo impareremo come pensare al tempo dal punto di vista di un programmatore, quali sono gli strumenti disponibili, e come usarli per risolvere problemi reali. L'idea è costruire intuizione attorno ai concetti sottostanti, non solo memorizzare metodi e funzioni.

## Capire il Tempo come Dato

Prima di tuffarci nel codice, poniamoci una domanda semplice: cos'è una data? Per noi umani è una cosa naturale—"il 15 marzo 2025"—ma un computer ha bisogno di qualcosa di più preciso. Potremmo rappresentare una data come tre numeri separati: un anno, un mese, un giorno. Potremmo rappresentare l'ora come ore, minuti, secondi. E potremmo avere una combinazione delle due cose quando vogliamo sapere sia la data che l'ora precisa in cui qualcosa è accaduto.

Il modulo `datetime` di Python rispecchia esattamente questo modo di pensare: fornisce un insieme di classi che rappresentano questi diversi concetti. Come già conosci le classi e gli oggetti, scoprirai che `datetime` usa questo paradigma per organizzare il suo codice in modo elegante e intuitivo.

## Le Quattro Classi Principali

Il modulo `datetime` mette a disposizione quattro classi che coprono praticamente tutti i casi d'uso comuni. Capiamo cosa rappresenta ciascuna.

### 1. La Classe `date`: Solo la Data

Immagina di voler memorizzare la data di nascita di una persona, o la data di scadenza di un documento. In questi casi non ti interessa l'ora esatta, solo il giorno specifico. La classe `date` è fatta per questo: rappresenta una data nel calendario gregoriano, con anno, mese e giorno.

```python
from datetime import date

# Creare una data specifica
data_nascita = date(1995, 7, 23)  # anno, mese, giorno
print(data_nascita)  # Output: 1995-07-23

# Accedere ai componenti
print(f"Anno: {data_nascita.year}")      # 1995
print(f"Mese: {data_nascita.month}")     # 7
print(f"Giorno: {data_nascita.day}")     # 23

# Ottenere oggi
oggi = date.today()
print(f"Oggi è il {oggi}")

# Calcolare quanti giorni sono passati dalla nascita fino ad oggi
giorni_passati = oggi - data_nascita
print(f"Sono passati {giorni_passati.days} giorni")
```

Quando sottrai una data da un'altra, Python non ti restituisce un numero semplice: ti dà un oggetto di tipo `timedelta`, che rappresenta una durata di tempo. Parleremo più nel dettaglio di `timedelta` fra poco, ma per adesso puoi pensarlo come a "la differenza tra due momenti nel tempo".

### 2. La Classe `time`: Solo l'Ora

Se una data rappresenta il giorno, `time` rappresenta l'ora di una giornata: ore, minuti, secondi e persino i microsecondi (milionesimi di secondo). È una classe meno frequentemente usata da sola, perché solitamente vogliamo sapere sia la data che l'ora, ma in alcuni scenari è utile.

```python
from datetime import time

# Definire un orario specifico
pausa_pranzo = time(12, 30, 0)  # ore, minuti, secondi
print(pausa_pranzo)  # Output: 12:30:00

# Accedere ai componenti
print(f"Ora: {pausa_pranzo.hour}")       # 12
print(f"Minuto: {pausa_pranzo.minute}")  # 30
print(f"Secondo: {pausa_pranzo.second}") # 0

# Midnight
mezzanotte = time(0, 0, 0)
print(mezzanotte)  # Output: 00:00:00

# Con microsecondi
ora_precisa = time(14, 23, 45, 123456)  # microsecondi come quarto parametro
print(ora_precisa)  # Output: 14:23:45.123456
```

### 3. La Classe `datetime`: Data e Ora Insieme

Questa è probabilmente la classe che userai più spesso. Combinare data e ora significa rappresentare un momento esatto nel tempo. Non "il 15 marzo", ma "il 15 marzo alle 14:30:00".

```python
from datetime import datetime

# Creare un momento specifico
conferenza = datetime(2025, 3, 15, 14, 30, 0)
print(conferenza)  # Output: 2025-03-15 14:30:00

# Accedere ai componenti (tutti gli attributi di date e time)
print(f"Data: {conferenza.date()}")  # 2025-03-15
print(f"Ora: {conferenza.time()}")   # 14:30:00
print(f"Giorno della settimana: {conferenza.weekday()}")  # 5 (sabato)

# Ottenere il momento attuale (data e ora together)
adesso = datetime.now()
print(f"Adesso sono le {adesso}")

# Quanti secondi sono passati dal 1970?
# (cioè da quando i computer hanno iniziato a contare il tempo)
timestamp = adesso.timestamp()
print(f"Timestamp Unix: {timestamp}")
```

Il valore restituito da `weekday()` è un numero da 0 a 6, dove 0 è lunedì e 6 è domenica. Se preferisci una rappresentazione più leggibile, puoi usare `isoweekday()`, dove 1 è lunedì e 7 è domenica.

### 4. La Classe `timedelta`: Durate e Differenze

Se `date` e `datetime` rappresentano *momenti nel tempo*, `timedelta` rappresenta una *durata*—quanto tempo è passato tra due momenti. È quello che ottieni quando sottrai una data da un'altra, ma puoi anche crearlo direttamente per aggiungere o sottrarre periodi di tempo.

```python
from datetime import timedelta, datetime

# Creare una durata: 5 giorni e 3 ore
durata = timedelta(days=5, hours=3)
print(durata)  # Output: 5 days, 3:00:00

# Componenti di un timedelta
print(f"Giorni: {durata.days}")          # 5
print(f"Secondi: {durata.seconds}")      # 10800 (3 ore in secondi)
print(f"Microsecondi: {durata.microseconds}")  # 0

# Somma totale in secondi
print(f"Totale secondi: {durata.total_seconds()}")  # 432000.0

# Usare timedelta per fare aritmetica
adesso = datetime.now()
tra_una_settimana = adesso + timedelta(days=7)
print(f"Tra una settimana sarà il {tra_una_settimana}")

# Sottrarre per andare indietro nel tempo
l_anno_scorso = adesso - timedelta(days=365)
print(f"Un anno fa era il {l_anno_scorso}")

# Moltiplicare una durata
due_settimane = timedelta(days=7) * 2
print(f"Due settimane: {due_settimane}")

# Dividere per trovare il numero di unità
tre_giorni = timedelta(days=3)
numero_ore = tre_giorni.total_seconds() / 3600
print(f"Tre giorni contengono {numero_ore} ore")
```

Attenzione a un dettaglio: gli attributi `days`, `seconds` e `microseconds` di un `timedelta` non rappresentano il totale. Sono i componenti normalizzati. Ad esempio, se crei `timedelta(hours=25)`, non troverai 25 ore in `.seconds`: troverai invece 1 giorno e 1 ora. Per il totale universale, usa sempre `.total_seconds()`.

## Lavorare con le Stringhe: `strftime()` e `strptime()`

Presto o tardi, avrai bisogno di leggere date scritte come testo ("15/03/2025") e trasformarle in oggetti `date` o `datetime`, oppure fare il contrario: prendere un oggetto `datetime` e trasformarlo in una stringa formattata in un certo modo.

### Convertire `datetime` in Stringa: `strftime()`

Il metodo `strftime()` converte un oggetto data/ora in una stringa secondo un formato che tu specifichi. Il nome è abbreviazione di "string format time" (formatta il tempo come stringa).

```python
from datetime import datetime

# Creare un momento
festa = datetime(2025, 12, 31, 23, 59, 59)

# Formattare come stringa leggibile
formato1 = festa.strftime("%d/%m/%Y")
print(formato1)  # Output: 31/12/2025

# Formato diverso con l'ora
formato2 = festa.strftime("%d-%b-%Y %H:%M:%S")
print(formato2)  # Output: 31-Dec-2025 23:59:59

# Solo il mese per esteso e l'anno
formato3 = festa.strftime("%B %Y")
print(formato3)  # Output: December 2025

# Giorno della settimana
formato4 = festa.strftime("Capodanno cade di %A")
print(formato4)  # Output: Capodanno cade di Wednesday
```

I codici di formato come `%d`, `%m`, `%Y`, `%H`, `%M`, `%S` sono abbreviazioni standard. Eccone un piccolo elenco dei più comuni:

- `%d` : Giorno del mese come numero (01-31)
- `%m` : Mese come numero (01-12)
- `%Y` : Anno con 4 cifre (2025)
- `%y` : Anno con 2 cifre (25)
- `%H` : Ora in formato 24 ore (00-23)
- `%M` : Minuto (00-59)
- `%S` : Secondo (00-59)
- `%A` : Nome completo del giorno della settimana (Monday, Tuesday...)
- `%a` : Abbreviazione del giorno (Mon, Tue...)
- `%B` : Nome completo del mese (January, February...)
- `%b` : Abbreviazione del mese (Jan, Feb...)

### Convertire Stringa in `datetime`: `strptime()`

Il processo inverso è `strptime()` ("string parse time"—estrai il tempo da una stringa). Fornisci una stringa e il formato in cui è scritta, e Python estrae i componenti per creare un oggetto `datetime`.

```python
from datetime import datetime

# Una data scritta come testo
data_testo = "25/12/2024"

# Convertire in datetime
data_natale = datetime.strptime(data_testo, "%d/%m/%Y")
print(data_natale)  # Output: 2024-12-25 00:00:00

# Nota: se non specifichi l'ora, Python assume 00:00:00

# Con ora inclusa
data_ora_testo = "2025-03-15 14:30:00"
momento = datetime.strptime(data_ora_testo, "%Y-%m-%d %H:%M:%S")
print(momento)  # Output: 2025-03-15 14:30:00

# Accedere ai componenti
print(f"Giorno della settimana: {momento.strftime('%A')}")  # Saturday
```

Un dettaglio importante: `strptime()` restituisce sempre un `datetime` (con l'ora impostata a 00:00:00 se non la specifichi), non un semplice `date`. Se vuoi estrarre solo la data, puoi usare il metodo `.date()`:

```python
solo_data = momento.date()  # Restituisce un oggetto date
print(solo_data)  # 2025-03-15
```

## Scenario Pratico: Calcolatore di Scadenza

Mettere insieme tutto quello che abbiamo imparato è il modo migliore per consolidare la comprensione. Immagina di dover scrivere un programma che traccia scadenze di documenti. Un documento può essere sottoposto fra 30 giorni, oppure fra un certo numero di mesi. Vogliamo calcolare quando scade e dirci quanto tempo rimane.

```python
from datetime import datetime, timedelta

class Documento:
    """Rappresenta un documento con una scadenza."""
    
    def __init__(self, nome, data_creazione, giorni_validita):
        """
        Crea un documento.
        
        Args:
            nome (str): Nome del documento
            data_creazione (datetime): Quando è stato creato
            giorni_validita (int): Dopo quanti giorni scade
        """
        self.nome = nome
        self.data_creazione = data_creazione
        self.data_scadenza = data_creazione + timedelta(days=giorni_validita)
    
    def giorni_rimasti(self):
        """Calcola quanti giorni rimangono prima della scadenza."""
        adesso = datetime.now()
        differenza = self.data_scadenza - adesso
        return differenza.days
    
    def è_scaduto(self):
        """Ritorna True se il documento è scaduto."""
        return self.giorni_rimasti() < 0
    
    def descrivere(self):
        """Restituisce una descrizione leggibile dello stato."""
        giorni_rimasti = self.giorni_rimasti()
        
        if self.è_scaduto():
            giorni_trascorsi = abs(giorni_rimasti)
            return (f"🚨 {self.nome} è SCADUTO da {giorni_trascorsi} giorni. "
                   f"Scadenza era: {self.data_scadenza.strftime('%d/%m/%Y')}")
        
        if giorni_rimasti == 0:
            return f"⚠️  {self.nome} scade OGGI!"
        
        return (f"✅ {self.nome} scade fra {giorni_rimasti} giorni "
               f"({self.data_scadenza.strftime('%d/%m/%Y')})")

# Usare la classe
adesso = datetime.now()

# Documento che scade domani
passaporto = Documento("Passaporto", adesso - timedelta(days=354), 365)
print(passaporto.descrivere())

# Documento scaduto da una settimana
patente = Documento("Patente", adesso - timedelta(days=400), 365)
print(patente.descrivere())

# Documento che scade fra 6 mesi
visto = Documento("Visto", adesso - timedelta(days=30), 180)
print(visto.descrivere())
```

In questo esempio vediamo come `datetime` si integra naturalmente con il paradigma a oggetti. La classe `Documento` incapsula la logica di tracciamento delle scadenze, mentre `timedelta` fornisce l'aritmetica necessaria per i calcoli.

## Oggetti "Consapevoli" e "Ingenui"

Il modulo `datetime` distingue fra due tipi di oggetti: "aware" (consapevoli) e "naive" (ingenui). Non è una caratteristica che ti servirà subito, ma è bene conoscerla per non sorprendersene quando la incontrerai.

Un oggetto "naive" non conosce il fuso orario. Quando dici "le 14:30", non sai se è 14:30 a Roma, a Tokyo, o a New York. È un orario "ingenuo" perché non contiene informazione sulla posizione geografica.

Un oggetto "aware" include informazioni di fuso orario. Quando dici "le 14:30 CET" (Central European Time), stai specificando dove sei nel mondo, quindi il tuo orario è "consapevole".

```python
from datetime import datetime, timezone, timedelta

# Ingenuo (no timezone)
adesso_ingenuo = datetime.now()
print(adesso_ingenuo)  # Niente info di fuso

# Consapevole (con timezone)
fuso_roma = timezone(timedelta(hours=1))  # CET è UTC+1
adesso_consapevole = datetime.now(fuso_roma)
print(adesso_consapevole)

# Verificare se è consapevole
print(f"È consapevole? {adesso_consapevole.tzinfo is not None}")

# UTC (il "fuso orario neutrale" di internet)
adesso_utc = datetime.now(timezone.utc)
print(adesso_utc)
```

Per gli script semplici che scrivono oggi come studente, gli oggetti "ingenui" vanno perfettamente bene. Quando costruirai applicazioni che devono coordinarsi fra utenti in diversi paesi del mondo, allora dovrai iniziare a preoccuparti di time zones.

## Errori Comuni e Come Evitarli

Concludiamo con alcuni avvertimenti che ti salveranno dal fare sbagli frustranti.

**Errore 1: Confondere i giorni di `timedelta` con il totale**

```python
from datetime import timedelta

# SBAGLIATO
delta = timedelta(hours=50)
print(delta.days)  # Stampa 2, non 50!
print(delta.seconds)  # Stampa 3600 (1 ora)

# CORRETTO
print(delta.total_seconds() / 3600)  # 50.0 ore
```

**Errore 2: Dimenticare che `strptime()` restituisce `datetime`, non `date`**

```python
from datetime import datetime

# Se vuoi un semplice date
testo = "2025-03-15"
# SBAGLIATO: questo crea un datetime, non date
momento = datetime.strptime(testo, "%Y-%m-%d")

# CORRETTO: estrai la data
solo_data = datetime.strptime(testo, "%Y-%m-%d").date()
print(type(solo_data))  # <class 'datetime.date'>
```

**Errore 3: Usare la stessa variabile per diversi significati**

```python
from datetime import datetime

# Non fare così
data = datetime.now()
# Dopo 50 righe di codice...
data = "2025-03-15"  # Oops! Ora è una stringa, non un datetime!

# Meglio così
adesso = datetime.now()
data_testo = "2025-03-15"  # Nomi diversi, significati chiari
```

## Conclusione

Il modulo `datetime` è uno di quei piccoli strumenti che, una volta capito, rende la programmazione più semplice. Non è complicato—è solo una questione di capire quale classe usare per quale scopo: `date` se vuoi solo il giorno, `time` se vuoi solo l'ora (raro), `datetime` se vuoi entrambe, e `timedelta` per fare calcoli fra momenti diversi.

Da qui in poi, ogni volta che un tuo programma avrà a che fare con date e ore, saprai dove andare a cercare. E il bello è che tutto questo è già incluso in Python—non devi scaricare nulla, non devi imparare una libreria esterna. È uno dei tanti piccoli regali che la libreria standard di Python ti mette a disposizione, insieme a tanti altri moduli che scoprirai man mano che avanzi nel tuo percorso di apprendimento.