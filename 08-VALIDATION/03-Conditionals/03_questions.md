# Domande Concettuali: Condizionali e Dizionari
## Matteo | Test di Comprensione Teorica
### Data: 2 gennaio 2026

---

## ISTRUZIONI

Rispondi a queste domande **senza scrivere codice**. Le risposte devono essere brevi (1-3 frasi) ma complete. L'obiettivo è capire se comprendi il **concetto**, non se sai la sintassi.

Se una domanda ti sembra confusa, prova a riformularla per te stesso prima di rispondere.

**Tempo consigliato**: 20-30 minuti totali.

---

## SEZIONE 1: CONDIZIONALI (if/elif/else)

### Livello Fondamentale

**1.1** Spiega la differenza tra un `if` e un `if/else`. Quando useresti uno rispetto all'altro?

**1.2** Cosa succede in questo codice e perché?
```python
x = 5
if x > 3:
    print("A")
if x > 4:
    print("B")
if x > 6:
    print("C")
```
Quali print verranno eseguiti?

**1.3** Qual è la differenza concettuale tra:
- Una serie di `if` separati
- Un `if/elif/else` chain

Quando è importante usare una piuttosto che l'altra?

**1.4** Se scrivi una condizione `if x == 5:`, cosa stai confrontando? Cosa significa il `==`?

**1.5** Spiega cosa fa l'operatore `and` e quando lo useresti. Fai un esempio concettuale (non codice).

---

### Livello Intermedio

**1.6** In un'applicazione di controllo accesso, vuoi permettere l'accesso solo se:
- L'utente ha una password corretta, E
- L'utente non è stato bannato, E  
- L'ora attuale è entro l'orario di accesso permesso

Come struttureresti la logica con `and`/`or`/`not`? Spiega il ragionamento.

**1.7** Qual è la differenza tra:
```python
# Opzione A
if not error:
    process_data()
    
# Opzione B
if error:
    return
else:
    process_data()
```
Quale è più "Pythonic"? Perché?

**1.8** Considerate questa situazione:
- Devi classificare una persona in base all'età: bambino (< 13), adolescente (13-17), adulto (18-64), anziano (65+)

Useresti `if/elif/else` chain oppure `match/case` (Python 3.10+)? Perché?

**1.9** Spiega il concetto di "short-circuit evaluation" negli operatori `and` e `or`. (Suggerimento: cosa succede dopo che la prima parte di un `and` è False?)

**1.10** Quando useresti `in` vs `==` per verificare un valore? Fai un esempio concettuale.

---

### Livello Avanzato

**1.11** Immagina di avere questa logica:
```python
if age >= 18 and (has_license or has_permit):
    allow_drive = True
else:
    allow_drive = False
```

Puoi riscrivere questa logica in una riga senza `if/else`, usando solo operatori booleani? Quale versione è più leggibile?

**1.12** Quali sono gli "edge case" (casi limite) che dovresti considerare quando scrivi una condizione su un'età? (Es: che succede se l'età è None? Se è negativa? Se è un float?)

**1.13** Nel contesto del tuo Batch Signal Processor, hai usato un `match/case` statement. Spiega: quale problema stavi risolvendo con `match/case` che avresti potuto risolvere (meno elegantemente) con `if/elif/else`?

**1.14** Spiega il concetto di **boolean variable** (una variabile che contiene True o False). Quando ha senso usare una variabile booleana come "flag" rispetto a scrivere direttamente la condizione nell'if?