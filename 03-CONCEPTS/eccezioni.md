# Eccezioni in Python: Gestire e Sollevare Errori

## Introduzione: Che Cosa Sono le Eccezioni

Immaginate di scrivere una funzione che legge un file. La funzione si aspetta che il file esista, che sia leggibile, che contenga dati ben formati. Ma cosa succede se il file non esiste? Se il programma non ha i permessi di lettura? Se il file è corrotto?

Senza un meccanismo per gestire questi problemi, il programma si arresta all'istante, spesso con un messaggio criptico che non vi aiuta a capire cosa sia andato storto. Con le eccezioni, invece, potete riconoscere il problema, decidere come comportarvi e continuare l'esecuzione se opportuno.

Le eccezioni sono un meccanismo fondamentale di Python per segnalare e gestire situazioni anomale. Non sono "errori nel senso di bug del programmatore"; sono situazioni previste ma indesiderate, come l'accesso a un indice inesistente, la divisione per zero, o il tentativo di aprire un file che non esiste.

Senza eccezioni, ogni funzione dovrebbe restituire un codice di errore insieme ai dati normali, complicando la logica di ogni chiamante. Le eccezioni separano il flusso "felice" (quando tutto va bene) dal flusso "triste" (quando qualcosa non funziona), rendendo il codice più leggibile e robusto.

## Il Modello: Try, Except, Finally

L'architettura delle eccezioni in Python si articola attorno a quattro parole chiave: `try`, `except`, `else` e `finally`. Vediamole in ordine di importanza.

### Try e Except: Catturare un Errore

La struttura di base è semplice: mettete il codice "rischioso" dentro un blocco `try`, e specificate come comportarvi se un errore si verifica con un blocco `except`.

```python
# Codice senza gestione delle eccezioni
numero = int("non è un numero")
# Output: ValueError: invalid literal for int() with base 10: 'non è un numero'
# Il programma si arresta.
```

Con la gestione delle eccezioni:

```python
try:
    numero = int("non è un numero")
except ValueError:
    print("Ho ricevuto un testo che non è un numero")
    numero = 0  # Valore di default

print(f"Numero: {numero}")
# Output: Ho ricevuto un testo che non è un numero
#         Numero: 0
```

Quello che accade è: Python tenta di eseguire il codice nel blocco `try`. Se un'eccezione di tipo `ValueError` viene sollevata, il resto del blocco `try` viene saltato, e il controllo passa al blocco `except ValueError`. Se nessuna eccezione si verifica, il blocco `except` viene ignorato.

L'eccezione catturata contiene informazioni: quale tipo di errore è, dove è accaduto, quale era lo stato delle variabili. Potete accedere a queste informazioni usando la parola chiave `as`.

```python
try:
    file = open("dati_inesistenti.txt", "r")
except FileNotFoundError as errore:
    print(f"Non riesco a trovare il file: {errore.filename}")
    print(f"Messaggio: {errore.strerror}")
```

### Catturare Più Tipi di Eccezioni

Una singola operazione può sollevare tipi diversi di eccezioni. Nel codice seguente, `int()` può sollevare `ValueError`, mentre `lista[indice]` può sollevare `IndexError`.

```python
try:
    testo = input("Inserisci un numero: ")
    numero = int(testo)
    lista = [10, 20, 30]
    elemento = lista[numero]  # Potrebbe sollevare IndexError
except ValueError:
    print("Non hai inserito un numero valido")
except IndexError:
    print("L'indice non esiste nella lista")
```

Potete anche catturare una categoria intera di eccezioni. Ad esempio, `ValueError` e `TypeError` ereditano entrambi da `Exception`, quindi un blocco `except Exception` le cattura tutte.

```python
try:
    risultato = 10 / 0
except Exception as e:
    print(f"Qualcosa è andato storto: {type(e).__name__}")
    print(f"Dettagli: {e}")
```

Attenzione: catturare `Exception` è una pratica ragionevole quando sapete che potrebbe verificarsi una varietà di errori. Ma catturare `BaseException` (senza specificare nulla: `except:` nudo) cattura anche eccezioni di sistema come `KeyboardInterrupt` e `SystemExit`, che normalmente volete che il programma non ignori. Evitate `except:` a meno che non abbiate una ragione molto specifica.

### Finally: Pulizia Garantita

A volte dovete eseguire del codice indipendentemente dal fatto che un'eccezione si sia verificata o meno. Ad esempio: chiudere un file, rilasciare una connessione a un database, ripristinare lo stato di una variabile globale.

```python
try:
    file = open("dati.txt", "r")
    contenuto = file.read()
except FileNotFoundError:
    print("File non trovato")
finally:
    file.close()
```

Il blocco `finally` viene eseguito sempre, sia che l'eccezione sia stata sollevata, sia che sia stata catturata, sia che nessuna eccezione si sia verificata. Nel codice sopra, il file viene chiuso comunque, indipendentemente da qualsiasi cosa accada nel `try` e nell' `except`.

(In pratica, per i file è preferibile usare `with`, che gestisce la chiusura automaticamente. Ma `finally` è fondamentale per altri tipi di risorse.)

### Else: Il Percorso Felice

Se desiderate eseguire del codice solo quando nessuna eccezione si è verificata, potete usare `else`.

```python
try:
    numero = int(input("Inserisci un numero: "))
except ValueError:
    print("Quello non è un numero")
else:
    print(f"Hai inserito il numero {numero}")
    print(f"Il suo quadrato è {numero ** 2}")
```

Questo pattern separa logicamente il codice "rischioso" (nel `try`) dal codice "di seguito" (nell' `else`), rendendo il flusso più chiaro.

## Sollevare Eccezioni: Raise

Non dovete solo catturare eccezioni; dovete anche crearle e schivarle per segnalare problemi nel vostro codice. Usate la parola chiave `raise`.

```python
def dividi(a, b):
    if b == 0:
        raise ValueError("Non puoi dividere per zero")
    return a / b

risultato = dividi(10, 0)
# Output: ValueError: Non puoi dividere per zero
```

Sollevare un'eccezione dice al codice che chiama: "Ho rilevato un problema. Non posso continuare. Tocca a te decidere cosa fare."

La gerarchia delle eccezioni in Python è importante. Le eccezioni più specifiche ereditano da quelle più generiche:

```
BaseException
├── Exception
│   ├── ValueError
│   ├── TypeError
│   ├── KeyError
│   ├── IndexError
│   └── ... (altre eccezioni specifiche)
├── KeyboardInterrupt
├── SystemExit
└── GeneratorExit
```

Se sollevate `ValueError`, chi chiama la vostra funzione può catturarla specificamente, oppure può catturarla come `Exception` se vuole un comportamento più generico.

### Preservare il Traceback Originale

Quando un'eccezione viene sollevata e volete sollevarne un'altra in risposta, usate la sintassi `from` per preservare il traceback originale. Questo aiuta il debugging perché conserva la catena di errori.

```python
import json

def carica_configurazione(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"File di configurazione non trovato: {path}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Configurazione JSON non valida in {path}") from e

carica_configurazione("config.json")
# Se il file non esiste, vedete il traceback originale di FileNotFoundError
# E poi il vostro RuntimeError con un messaggio più semantico
```

La sintassi `from e` dice a Python: "Questa nuova eccezione è stata causata da quella precedente. Tieni traccia di entrambe."

## La Gerarchia: Quale Eccezione Sollevare

Python fornisce decine di eccezioni built-in. Le più comuni:

**Errori di tipo:**
- `TypeError`: il tipo di un oggetto non è quello atteso (es. sommare un numero e una stringa)
- `ValueError`: il valore di un oggetto è fuori intervallo o malformato (es. `int("abc")`)
- `AttributeError`: si tenta di accedere a un attributo inesistente (es. `lista.push()` invece di `lista.append()`)

**Errori di accesso:**
- `KeyError`: la chiave non esiste in un dizionario
- `IndexError`: l'indice non esiste in una lista
- `KeyboardInterrupt`: l'utente ha premuto Ctrl+C

**Errori di I/O:**
- `FileNotFoundError`: il file non esiste
- `PermissionError`: non hai i permessi per accedere al file
- `IOError`: errore generico durante lettura/scrittura

**Errori aritmetici:**
- `ZeroDivisionError`: divisione per zero
- `OverflowError`: il numero è troppo grande per la rappresentazione

Quando scrivete il vostro codice, scegliete l'eccezione più specifica possibile. Non usate mai `Exception` generica quando un'eccezione più specifica esiste.

```python
# ❌ Sbagliato: generico
def estrai_eta(persona_dict):
    raise Exception("Chiave mancante")

# ✅ Corretto: specifico
def estrai_eta(persona_dict):
    if "eta" not in persona_dict:
        raise KeyError("La chiave 'eta' non esiste nel dizionario")
    return persona_dict["eta"]
```

## Eccezioni Personalizzate: Quando e Come

Fin qui abbiamo usato le eccezioni built-in fornite da Python. Ma per progetti complessi, potete definire le vostre eccezioni personalizzate che rappresentano errori specifici del vostro dominio.

Immaginate un'applicazione che gestisce prenotazioni di ristoranti. Potrebbe sollevare `ValueError` quando un numero di ospiti è negativo, ma potrebbe essere più chiaro sollevare una vostra eccezione `NumeroOspitiNonValido`. In questo modo, chi usa la vostra funzione capisce subito che il problema riguarda gli ospiti, non un generico valore sbagliato.

Definire un'eccezione personalizzata è semplice: create una classe che eredita da `Exception` (o da un'altra eccezione built-in).

```python
# Definire l'eccezione
class NumeroOspitiNonValido(Exception):
    """Sollevata quando il numero di ospiti non è valido."""
    pass

# Usarla
def prenota_tavolo(ristorante, ospiti):
    if ospiti < 1 or ospiti > 20:
        raise NumeroOspitiNonValido(f"Il numero di ospiti deve essere tra 1 e 20, ricevuto {ospiti}")
    print(f"Tavolo prenotato per {ospiti} ospiti")

# Catturarla
try:
    prenota_tavolo("Da Mario", 0)
except NumeroOspitiNonValido as e:
    print(f"Errore di prenotazione: {e}")
```

Le eccezioni personalizzate diventano ancora più potenti quando organizzate in una gerarchia. Per esempio, un'applicazione di banca potrebbe definire:

```python
class ErroreTransazione(Exception):
    """Eccezione base per tutti gli errori di transazione."""
    pass

class SaldoInsufficiente(ErroreTransazione):
    """Sollevata quando il conto non ha abbastanza fondi."""
    pass

class ContoBloccato(ErroreTransazione):
    """Sollevata quando il conto è temporaneamente bloccato."""
    pass

def trasferisci(conto_origine, conto_destinazione, importo):
    if conto_origine.saldo < importo:
        raise SaldoInsufficiente(f"Saldo insufficiente: {conto_origine.saldo}, richiesto {importo}")
    if conto_origine.bloccato:
        raise ContoBloccato("Il conto è bloccato")
    # ... trasferimento
```

Chi usa questa funzione può catturare `SaldoInsufficiente` e `ContoBloccato` separatamente per comportamenti diversi, oppure catturare `ErroreTransazione` genericamente se vuole lo stesso comportamento per tutti gli errori di transazione.

## Trabocchetto: Catturare Tutto Può Essere Pericoloso

Il trabocchetto più comune è catturare eccezioni troppo largamente, nascondendo così errori che non avevate intenzione di gestire.

```python
# ❌ Pericoloso
try:
    numero = int(input("Inserisci un numero: "))
    lista = [1, 2, 3]
    elemento = lista[numero]
except:  # Cattura TUTTO
    print("Qualcosa è andato storto")
```

Il problema: se la lista è `None` (perché assegnata per errore), il codice `lista[numero]` solleva `TypeError`, che viene catturato silenziosamente. Non scoprirete mai il bug.

Sempre catturate l'eccezione più specifica possibile:

```python
# ✅ Corretto
try:
    numero = int(input("Inserisci un numero: "))
    lista = [1, 2, 3]
    elemento = lista[numero]
except ValueError:
    print("Non hai inserito un numero valido")
except IndexError:
    print("Quell'indice non esiste nella lista")
```

Un altro trabocchetto: lanciare eccezioni durante la gestione di un'eccezione senza usare `from`.

```python
# ❌ Cattiva forma
try:
    file = open("dati.txt")
except FileNotFoundError:
    raise RuntimeError("Configurazione non trovata")
    # Perdi il traceback originale

# ✅ Buona forma
try:
    file = open("dati.txt")
except FileNotFoundError as e:
    raise RuntimeError("Configurazione non trovata") from e
    # Preservi la causa originale
```

## Dove si Incontrano le Eccezioni nel Codice Reale

Nel vostro lavoro quotidiano, incontrerete eccezioni in questi contesti:

**Input/Output:** Ogni volta che leggete da file, rete o input utente, dovete gestire `FileNotFoundError`, `IOError`, `ValueError`.

**Parsing e conversione:** Quando elaborate dati non strutturati (JSON, CSV, dati da API), dovete catturare `json.JSONDecodeError`, `ValueError` per parsing numerico, `KeyError` per chiavi mancanti.

**Operazioni sui dati:** Accesso a liste e dizionari può sollevare `IndexError` e `KeyError`.

**Librerie esterne:** Quasi ogni libreria (requests per HTTP, pandas per dati, etc.) definisce eccezioni personalizzate per segnalare errori specifici.

Un esempio realistico:

```python
import json
from pathlib import Path

def carica_e_processa_dati(file_path):
    """Carica dati JSON e estrae informazioni critiche."""
    try:
        # Passaggio 1: Leggi il file
        file_path = Path(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            contenuto = f.read()
        
        # Passaggio 2: Parse JSON
        dati = json.loads(contenuto)
        
        # Passaggio 3: Estrai dati
        nomi = [persona["nome"] for persona in dati["persone"]]
        return nomi
    
    except FileNotFoundError:
        print(f"Il file {file_path} non esiste")
        return []
    
    except json.JSONDecodeError as e:
        print(f"Il file non contiene JSON valido: {e}")
        return []
    
    except KeyError as e:
        print(f"Struttura JSON incompleta. Chiave mancante: {e}")
        return []
    
    except Exception as e:
        # Fallback per errori inaspettati
        print(f"Errore inaspettato: {type(e).__name__}: {e}")
        return []
```

Questo codice gestisce ogni tipo di errore prevedibile separatamente, con messaggi specifici, mentre cattura gli errori inaspettati al fondo per non rimanere completamente al buio.

## Conclusione

Le eccezioni sono il meccanismo mediante il quale Python comunica problemi. Non sono un trucco avanzato; sono fondamentali per scrivere codice affidabile. Tre concetti chiave:

1. **Catturare specificamente**: usate `except ValueError`, non `except Exception`, a meno che non abbiate una ragione.

2. **Sollevare appropiatamente**: quando il vostro codice rileva un problema, comunicate il tipo di problema sollevando l'eccezione giusta.

3. **Preservare il contesto**: usate `from e` per mantenere il traceback originale, e includete informazioni utili nel messaggio dell'eccezione.

Le eccezioni personalizzate diventano importanti quando il vostro progetto cresce: creano un linguaggio comune tra moduli, permettono al codice che chiama di reagire in modo intelligente agli errori specifici del vostro dominio. Ma iniziate imparando a catturare e sollevare le eccezioni built-in correttamente; il resto seguirà naturalmente.
