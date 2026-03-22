# Capitolo 4: Sezione 1.5 — Input e Output da Console

## Introduzione: il dialogo tra programma e utente

Pensate a un chiosco automatico al bar: voi premete un pulsante (input), la macchina prepara il caffè e ve lo consegna con un bip di conferma (output). Quasi ogni programma utile funziona secondo questa stessa logica: riceve informazioni dall'esterno, le elabora, e poi comunica qualcosa di ritorno. Senza questa capacità di dialogare, un programma sarebbe come un foglio di carta stampato: fisso, silenzioso, inutilizzabile in modo interattivo.

Python mette a disposizione due strumenti fondamentali per questo dialogo con la console: la funzione `print()`, che permette al programma di "parlare" verso lo schermo, e la funzione `input()`, che permette al programma di "ascoltare" ciò che l'utente digita sulla tastiera. Queste due funzioni sono tra le prime che ogni programmatore impara, perché rendono immediatamente visibile e tangibile l'effetto di ciò che si scrive.

In questa dispensa esploreremo entrambe in profondità, compresi alcuni parametri di `print()` che spesso vengono sottovalutati: `sep` e `end`. Vedremo poi come convertire il testo proveniente da `input()` in un numero, grazie alle funzioni `int()` e `float()`, un passaggio indispensabile ogni volta che vogliamo fare calcoli con dati forniti dall'utente.

---

## La funzione `print()`: parlare verso lo schermo

La funzione `print()` è già stata incontrata nelle dispense precedenti, dove è servita a verificare il valore di variabili e letterali. Ora la esaminiamo in modo sistematico.

Nella sua forma più elementare, `print()` riceve uno o più valori separati da virgola e li stampa a schermo, uno dopo l'altro, con uno spazio tra ciascuno:

```python
# Stampa una singola stringa
print("Benvenuto nel programma!")
# Output: Benvenuto nel programma!

# Stampa più valori nella stessa chiamata
nome = "Giulia"
anni = 30
print("Nome:", nome, "Età:", anni)
# Output: Nome: Giulia Età: 30
```

Notate come Python abbia inserito automaticamente uno spazio tra ogni valore: tra `"Nome:"` e `nome`, tra `nome` e `"Età:"`, e così via. Questo comportamento è controllato dal parametro `sep`, che vedremo tra poco.

È importante capire che `print()` sa stampare qualunque tipo di dato: stringhe, interi, float, booleani. Non è necessario convertirli manualmente in stringa prima di passarli alla funzione.

```python
# print() accetta tipi misti senza conversione esplicita
temperatura = 36.6
positivo = True
print("Temperatura:", temperatura, "Febbre?", positivo)
# Output: Temperatura: 36.6 Febbre? True
```

---

## Il parametro `end`: cosa succede alla fine della riga

Per capire `end`, bisogna sapere che ogni volta che `print()` finisce di stampare, aggiunge automaticamente un carattere speciale chiamato "a capo" (in inglese *newline*), scritto come `\n`. È per questo che due istruzioni `print()` consecutive producono righe distinte invece di appicciarsi l'una all'altra.

```python
print("Prima riga")
print("Seconda riga")
# Output:
# Prima riga
# Seconda riga
```

Il parametro `end` permette di sostituire questo comportamento predefinito con qualsiasi stringa si voglia, inclusa la stringa vuota `""` se non si desidera nessun separatore finale:

```python
# Stampa due cose sulla stessa riga usando end
print("Prima parte", end=" ")
print("seconda parte sulla stessa riga")
# Output: Prima parte seconda parte sulla stessa riga

# Usa end="" per non aggiungere nulla
print("A", end="")
print("B", end="")
print("C")
# Output: ABC
```

Un caso d'uso pratico è costruire progressivamente una riga di output all'interno di un ciclo, dove si vuole che ogni elemento appaia sulla stessa riga separato da un trattino, per esempio, e non su righe distinte. Tornerà utile quando studierete i cicli nella Sezione 2.

Si può anche usare `end` per aggiungere un separatore diverso dal semplice a capo:

```python
print("Fine sezione", end="\n\n")
print("Inizio sezione successiva")
# Output:
# Fine sezione
#
# Inizio sezione successiva
```

In questo caso `\n\n` inserisce due andate a capo, lasciando una riga vuota tra le due istruzioni.

---

## Il parametro `sep`: scegliere il separatore tra i valori

Come si è visto, quando si passano più argomenti a `print()`, questi vengono separati da uno spazio per default. Il parametro `sep` (abbreviazione di *separator*) permette di cambiare questo separatore con qualsiasi stringa:

```python
# Separatore predefinito: uno spazio
print("a", "b", "c")
# Output: a b c

# Separatore personalizzato: trattino
print("a", "b", "c", sep="-")
# Output: a-b-c

# Separatore con più caratteri
print("2025", "03", "22", sep="/")
# Output: 2025/03/22

# Nessun separatore
print("a", "b", "c", sep="")
# Output: abc
```

L'esempio con la data è particolarmente eloquente: passando tre parti di una data come argomenti separati e specificando `sep="/"`, si ottiene una data formattata senza dover costruire manualmente la stringa con la concatenazione.

I parametri `sep` e `end` possono essere usati contemporaneamente nella stessa chiamata a `print()`:

```python
# Usa sep e end insieme
print("Rosso", "Verde", "Blu", sep=" | ", end=".\n")
# Output: Rosso | Verde | Blu.
```

---

## La funzione `input()`: ascoltare l'utente

La funzione `input()` sospende l'esecuzione del programma, mostra un messaggio opzionale (detto *prompt*) all'utente e attende che questi digiti qualcosa sulla tastiera e prema Invio. A quel punto, `input()` restituisce ciò che è stato digitato sotto forma di stringa.

```python
# Chiede il nome e lo saluta
nome = input("Come ti chiami? ")
print("Ciao,", nome)
# L'utente digita: Mario
# Output: Ciao, Mario
```

La stringa passata a `input()` è puramente il messaggio visualizzato prima che l'utente digiti: non ha effetto sul valore restituito. Se non si vuole nessun messaggio, si può chiamare `input()` senza argomenti, anche se raramente è una scelta utile nella pratica.

Ci sono due aspetti di `input()` che è fondamentale tenere a mente. Il primo: `input()` restituisce **sempre una stringa**, indipendentemente da cosa l'utente abbia digitato. Se l'utente scrive `42`, Python non la interpreta come il numero intero 42, ma come la stringa di testo `"42"`. Il secondo: l'esecuzione del programma rimane bloccata finché l'utente non preme Invio. Questo è il comportamento atteso, ma vale la pena sapere che non si può aggirare senza strumenti più avanzati (non trattati in questo corso).

```python
# Attenzione: input() restituisce sempre una stringa
risposta = input("Inserisci un numero: ")
print(type(risposta))
# L'utente digita: 10
# Output: <class 'str'>    ← è una stringa, non un intero!
```

---

## Convertire l'input: `int()` e `float()`

Poiché `input()` restituisce sempre una stringa, ogni volta che si vuole eseguire un'operazione aritmetica con il valore fornito dall'utente è necessario convertirlo esplicitamente nel tipo appropriato. Python mette a disposizione due funzioni di conversione: `int()` per i numeri interi e `float()` per i numeri in virgola mobile.

`int()` prende una stringa che rappresenta un numero intero (senza decimali) e la trasforma in un valore di tipo `int`:

```python
# Conversione di input a intero
testo = input("Inserisci la tua età: ")  # L'utente digita: 25
eta = int(testo)
print("Tra dieci anni avrai", eta + 10, "anni")
# Output: Tra dieci anni avrai 35 anni
```

Nella pratica, la conversione si scrive quasi sempre in una sola riga, annidando `input()` direttamente dentro `int()`:

```python
# Forma compatta, la più usata
eta = int(input("Inserisci la tua età: "))
print("Tra dieci anni avrai", eta + 10, "anni")
```

`float()` funziona in modo analogo, ma accetta anche stringhe con il punto decimale (Python usa il punto, non la virgola, come separatore decimale):

```python
# Conversione di input a float
altezza = float(input("Inserisci la tua altezza in metri (es. 1.75): "))
print("La tua altezza è", altezza, "metri")
# L'utente digita: 1.82
# Output: La tua altezza è 1.82 metri
```

Vale la pena notare che `int()` e `float()` non servono solo per convertire l'output di `input()`: si possono usare su qualsiasi valore convertibile. Per esempio, `int(3.9)` restituisce `3` (troncamento, non arrotondamento), e `float(7)` restituisce `7.0`. Queste conversioni rientrano nel concetto più generale di *type casting*, già menzionato nella sezione 1.4, che sarà approfondito man mano che si incontreranno situazioni in cui i tipi devono essere compatibili tra loro.

```python
# int() tronca, non arrotonda
print(int(3.9))   # Output: 3
print(int(-2.7))  # Output: -2

# float() converte interi in float
print(float(7))   # Output: 7.0
```

Un errore classico è passare a `int()` una stringa che non rappresenta un intero valido, per esempio perché contiene lettere o la virgola al posto del punto. In quel caso Python solleva un'eccezione di tipo `ValueError`. La gestione delle eccezioni è trattata nella Sezione 4; per ora è sufficiente sapere che il programma si interrompe con un messaggio di errore se l'utente inserisce qualcosa di inatteso.

---

## Un esempio completo: mettere tutto insieme

Vediamo un piccolo programma che usa `input()`, `int()`, `float()` e `print()` con `sep` e `end` in modo coordinato:

```python
# Programma: calcolo dell'indice di massa corporea (IMC)

nome = input("Nome: ")
peso = float(input("Peso in kg (es. 70.5): "))
altezza = float(input("Altezza in metri (es. 1.75): "))

imc = peso / (altezza ** 2)

print("\n--- Risultato ---", end="\n")
print("Nome:", nome, sep=" ", end="\n")
print("IMC:", round(imc, 2), sep=" ", end="\n")
print("-----------------")
```

In questo esempio tutti i concetti della sezione 1.5 compaiono insieme: `input()` raccoglie tre dati, `float()` li converte per permettere il calcolo, e `print()` con `end` e `sep` (qui ai loro valori predefiniti, per chiarezza) formatta l'output in modo leggibile.

---

## Conclusione: il programma che ascolta e risponde

Con `print()` e `input()` avete ora in mano gli strumenti fondamentali per costruire programmi che non siano semplici sequenze di calcoli silenziosi, ma veri dialoghi con chi li usa. Sapete come controllare ogni dettaglio dell'output grazie a `sep` e `end`, e sapete come trasformare il testo digitato dall'utente in numeri su cui poter operare con `int()` e `float()`.

Questi strumenti diventano ancora più potenti quando combinati con ciò che studierete nelle sezioni successive: le istruzioni condizionali (Sezione 2.1) permetteranno di reagire in modo diverso in base a ciò che l'utente inserisce, mentre i cicli (Sezione 2.2) consentiranno di chiedere ripetutamente un input finché non si ottiene un valore valido. Il dialogo tra programma e utente, insomma, è appena cominciato.
