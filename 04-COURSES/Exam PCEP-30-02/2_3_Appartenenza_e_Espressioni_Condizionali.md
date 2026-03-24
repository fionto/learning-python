# Capitolo 2: Sezione 2.3 — Appartenenza e Concisione: Due Strumenti per un Codice più Espressivo

## Introduzione: Domande Rapide, Risposte Dirette

Nella sezione 2.1 abbiamo imparato a prendere decisioni con `if`, `elif` ed `else`. Nella 2.2 abbiamo visto come il ciclo `for` usi la parola chiave `in` per scorrere una sequenza elemento per elemento. In questa sezione torniamo su entrambi questi strumenti per affinarne l'uso in due situazioni molto concrete.

La prima riguarda una domanda che capita spessissimo nella programmazione reale: "questo elemento è presente in questa collezione?" Non vogliamo scorrere la collezione con un ciclo, non vogliamo contare le occorrenze; vogliamo semplicemente una risposta sì o no, da usare direttamente in una condizione. Gli **operatori di appartenenza** `in` e `not in` fanno esattamente questo, e funzionano su molti più tipi di dati di quanto il solo ciclo `for` possa suggerire.

La seconda riguarda una situazione familiare: avete bisogno di assegnare un valore a una variabile scegliendo tra due alternative in base a una condizione. Scritta come un blocco `if-else` standard, questa operazione occupa quattro righe. Python offre una forma compatta, l'**espressione condizionale** (chiamata a volte operatore ternario), che la esprime in una sola. Capire quando usarla, e quando invece è meglio resistere alla tentazione, è parte dell'arte di scrivere codice leggibile.

---

## Operatori di Appartenenza: `in` e `not in`

Quando nella sezione 2.2 avete scritto `for carattere in parola:`, la parola chiave `in` svolgeva il ruolo di connettore sintattico del ciclo: "per ogni elemento nella sequenza, fai questo". Ma `in` ha una seconda vita, completamente indipendente dal `for`: può essere usato come **operatore binario** che restituisce un valore booleano.

La sintassi è semplicissima:

```python
elemento in sequenza      # True se elemento è presente, False altrimenti
elemento not in sequenza  # True se elemento è assente, False altrimenti
```

Il risultato è sempre `True` o `False`, il che significa che potete usare queste espressioni direttamente come condizione di un `if`, oppure assegnarle a una variabile booleana.

### Appartenenza nelle Stringhe

Applicato a una stringa, `in` verifica se una sottostringa è contenuta nella stringa più grande. Non si limita ai singoli caratteri: funziona con sequenze di caratteri di qualsiasi lunghezza.

```python
# Verificare la presenza di un carattere
vocali = "aeiouAEIOU"
carattere = "e"

if carattere in vocali:
    print(f"'{carattere}' è una vocale")
else:
    print(f"'{carattere}' è una consonante")
# Output: 'e' è una vocale
```

```python
# Verificare la presenza di una sottostringa
indirizzo_email = "mario.rossi@esempio.it"

if "@" in indirizzo_email:
    print("Formato email plausibile: contiene la chiocciola")
else:
    print("Formato email non valido: manca la chiocciola")
# Output: Formato email plausibile: contiene la chiocciola
```

```python
# not in: verificare l'assenza
password = "Gatto99"

if " " not in password:
    print("La password non contiene spazi: bene")
else:
    print("Attenzione: la password contiene spazi")
# Output: La password non contiene spazi: bene
```

La ricerca è **case-sensitive**: `"python" in "Python è bello"` restituisce `False`, perché la lettera maiuscola "P" e la minuscola "p" sono caratteri diversi. Se volete una ricerca insensibile alle maiuscole, dovrete prima convertire entrambe le stringhe allo stesso caso con `.lower()` o `.upper()`, strumenti che incontrerete nella sezione 3.4.

### Appartenenza nelle Liste (Anteprima)

Anche se le liste verranno trattate in dettaglio nella sezione 3.1, vale la pena sapere fin da ora che `in` e `not in` funzionano su di esse con la stessa sintassi. Questa coerenza è una delle qualità più apprezzate di Python: lo stesso operatore funziona su tipi di dati diversi senza bisogno di imparare strumenti distinti.

```python
# Verificare se un valore è in una lista di valori ammessi
colori_validi = ["rosso", "verde", "blu", "giallo"]
scelta = "verde"

if scelta in colori_validi:
    print(f"'{scelta}' è un colore valido")
else:
    print(f"'{scelta}' non è riconosciuto")
# Output: 'verde' è un colore valido
```

```python
# not in per escludere valori indesiderati
voti_insufficienti = [3, 4, 5]
voto = 7

if voto not in voti_insufficienti:
    print(f"Voto {voto}: sufficiente, si passa")
else:
    print(f"Voto {voto}: insufficiente")
# Output: Voto 7: sufficiente, si passa
```

### `in` come Espressione Booleana Autonoma

Poiché `in` e `not in` restituiscono un valore booleano, potete assegnarli direttamente a una variabile, esattamente come fareste con qualsiasi altra espressione `True`/`False`:

```python
# Salvare il risultato del test di appartenenza in una variabile
testo = "La festa è confermata"
parola_chiave = "confermata"

evento_confermato = parola_chiave in testo

print(evento_confermato)          # Output: True
print(type(evento_confermato))    # Output: <class 'bool'>

if evento_confermato:
    print("Prepara i festeggiamenti!")
# Output: Prepara i festeggiamenti!
```

Questo pattern, in cui il risultato di un test viene memorizzato in una variabile con un nome descrittivo, rende il codice più leggibile soprattutto quando la stessa verifica deve essere usata in più punti del programma.

---

## Espressioni Condizionali: l'Operatore Ternario

Considerate questo schema, che avrete già scritto molte volte:

```python
if condizione:
    variabile = valore_se_vera
else:
    variabile = valore_se_falsa
```

Quattro righe per assegnare un valore a una variabile in base a una condizione. Il blocco è chiaro, ma occupa spazio e introduce un'interruzione nel flusso della lettura per qualcosa di concettualmente semplice. Python offre una sintassi alternativa, l'**espressione condizionale**, che comprime tutto questo in una sola riga:

```python
variabile = valore_se_vera if condizione else valore_se_falsa
```

L'ordine può sembrare insolito all'inizio: prima il valore che si vuole assegnare se la condizione è vera, poi la condizione, poi il valore alternativo. Leggendola ad alta voce diventa naturale: "assegna *questo* se *tale condizione è vera*, altrimenti assegna *quest'altro*".

### Esempi Pratici

Un caso classico è la scelta tra due etichette testuali:

```python
# Forma estesa
eta = 20
if eta >= 18:
    categoria = "adulto"
else:
    categoria = "minore"

# Forma compatta con espressione condizionale
eta = 20
categoria = "adulto" if eta >= 18 else "minore"

print(categoria)  # Output: adulto
```

Entrambe le versioni producono esattamente lo stesso risultato. La seconda è più breve e, per chi conosce la sintassi, altrettanto leggibile.

Un altro uso frequente è il calcolo di un valore assoluto o di un minimo/massimo senza usare funzioni dedicate:

```python
# Valore assoluto di un numero
numero = -7
assoluto = numero if numero >= 0 else -numero
print(assoluto)  # Output: 7
```

```python
# Il maggiore tra due numeri
a = 15
b = 23
massimo = a if a > b else b
print(massimo)  # Output: 23
```

L'espressione condizionale può anche comparire direttamente all'interno di una `print()` o di qualsiasi altra espressione, senza bisogno di assegnarla prima a una variabile:

```python
# Usarla direttamente in una print
punteggio = 55
print("Promosso" if punteggio >= 60 else "Bocciato")
# Output: Bocciato
```

### Quando Usarla e Quando Evitarla

L'espressione condizionale è uno strumento di **leggibilità**, non di risparmio di righe fine a se stesso. Va usata quando la condizione è semplice, i due valori sono concisi e l'intera espressione si legge agevolmente in una riga. In questi casi, la forma compatta comunica l'intenzione più direttamente di un blocco `if-else` di quattro righe.

Diventa invece controproducente quando la condizione è complessa, quando i valori da assegnare sono essi stessi espressioni lunghe, o quando si è tentati di annidare più espressioni condizionali una dentro l'altra. Un'espressione condizionale annidata come la seguente è tecnicamente valida, ma quasi impossibile da leggere:

```python
# Da evitare: espressione condizionale annidata
# (difficile da leggere, meglio usare if-elif-else)
x = 10
etichetta = "positivo" if x > 0 else ("zero" if x == 0 else "negativo")
```

Per questo tipo di logica a tre o più rami, il blocco `if-elif-else` della sezione 2.1 rimane la scelta giusta. La regola pratica è semplice: se dovete leggere l'espressione due volte per capire cosa fa, usate la forma estesa.

---

## Mettere Tutto Insieme: Un Esempio di Validazione

Per chiudere con un esempio che unisca i due strumenti presentati in questa sezione, immaginiamo una funzione di validazione elementare per un codice prodotto: deve contenere solo caratteri alfanumerici, non contenere spazi, e iniziare con una lettera maiuscola.

```python
# Validazione di un codice prodotto
codice = "A4732X"

caratteri_validi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
maiuscole = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Controllo 1: nessuno spazio
niente_spazi = " " not in codice

# Controllo 2: primo carattere maiuscolo
primo_maiuscolo = codice[0] in maiuscole if len(codice) > 0 else False

# Messaggio finale con espressione condizionale
esito = "valido" if niente_spazi and primo_maiuscolo else "non valido"
print(f"Codice '{codice}': {esito}")
# Output: Codice 'A4732X': valido
```

In questo esempio, `not in` e `in` eseguono i controlli di appartenenza e restituiscono valori booleani memorizzati in variabili descrittive. L'espressione condizionale nella riga finale combina quei booleani in un messaggio conciso. Ogni parte del codice fa una cosa sola e la fa in modo leggibile.

---

## Conclusione: Chiarezza Prima di Tutto

Gli operatori di appartenenza e le espressioni condizionali non aggiungono capacità che prima mancavano: tutto ciò che fanno potrebbe essere scritto con un ciclo `for` e un blocco `if-else` standard. Quello che offrono è **espressività**: la possibilità di dire la stessa cosa in un modo più diretto e vicino al linguaggio naturale.

`in` e `not in` trasformano una domanda ("questo elemento è presente?") in un'espressione booleana che si legge quasi come una frase italiana. L'espressione condizionale trasforma un'assegnazione con alternativa in una singola riga che dichiara l'intenzione senza cerimonie. Usati con giudizio, rendono il codice più facile da scrivere, da leggere e da mantenere.

Con questa sezione si chiude il blocco dedicato al controllo di flusso. La sezione 3 ci porterà a esplorare le strutture dati di Python: liste, tuple, dizionari e stringhe. Scoprirete che `in` e `not in` tornano protagonisti anche lì, con la stessa sintassi ma applicati a collezioni molto più ricche di una semplice stringa.
