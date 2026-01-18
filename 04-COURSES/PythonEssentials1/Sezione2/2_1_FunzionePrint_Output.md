# Capitolo 2: Sezione 2.1 - La Funzione print() e le Operazioni di Output

## Introduzione: Il Primo Programma e la Comunicazione col Mondo

Finora abbiamo parlato di teorie e concetti astratti. Ma la vera programmazione inizia quando cominciate a scrivere codice che il computer possa eseguire. E il primo compito che affrontiamo è sempre lo stesso: comunicare qualcosa all'utente.

Il codice che scrivete vive in una specie di vuoto se nessuno può vederlo o interagire con esso. Un programma deve poter parlare: deve poter dire "il risultato è 42", oppure "errore: numero non valido", o semplicemente "ciao!". Per fare questo, utilizziamo funzioni di output—il modo più comune è la funzione `print()`.

### 2.1.1 Il Vostro Primo Programma

Consideriamo il programma più semplice possibile:

```python
print("Ciao, mondo!")
```

Questo è tutto. Una sola riga. Quando eseguite questo programma, vedete:

```
Ciao, mondo!
```

Questo semplice esempio racchiude già diversi concetti importanti che dovremo approfondire. Ma innanzitutto, congratulatevi con voi stessi. Avete appena scritto un programma che comunica. È piccolo, ma è un inizio. Ogni programma, dai più semplici ai più complessi, inizia con la capacità di produrre output.

## 2.1.2 La Funzione print(): Fondamenti

La **funzione** `print()` è uno degli strumenti più fondamentali di Python. Il suo scopo è semplice: prendere le informazioni che le passate e visualizzarle sullo schermo (precisamente, mandarle al flusso di output standard, che solitamente è il vostro terminale o console).

Una funzione in programmazione è come una scatola nera che contiene un insieme di istruzioni già scritte. Voi non dovete sapere come funziona internamente; dovete solo sapere come usarla e cosa aspettarvi come risultato. Nel caso di `print()`, la "scatola nera" contiene tutte le istruzioni necessarie per prendere un valore e mostrarlo sullo schermo. Senza `print()`, avreste bisogno di scrivere centinaia di righe di codice complesso per ottenere lo stesso risultato.

### Come Funziona print()

Quando scrivete:

```python
print("Ciao, mondo!")
```

State essenzialmente dicendo al programma: "Prendi il testo 'Ciao, mondo!' e visualizzalo sullo schermo". Python capisce questo comando, lo esegue, e il testo appare. Notate che `print` è seguita da parentesi tonde: `()`. Queste parentesi sono essenziali. Indicano che `print` è una funzione, non una variabile. Se scrivete semplicemente `print` senza parentesi, il computer vi mostrerà informazioni sulla funzione stessa, non eseguirà la funzione.

## 2.1.3 Argomenti della Funzione: Cosa Passate al Contenitore

Quando utilizzate una funzione come `print()`, dovete fornirle le informazioni di cui ha bisogno per fare il suo lavoro. Queste informazioni si chiamano **argomenti** (o **parametri**, sebbene i termini siano tecnicalmente distinti). Nel nostro esempio:

```python
print("Ciao, mondo!")
```

L'argomento è la stringa `"Ciao, mondo!"`. Gli argomenti si passano inserendo i dati tra le parentesi, separati da virgole se ce ne sono più di uno. Pensate agli argomenti come istruzioni dettagliate. Se `print()` è una funzione che visualizza testo, gli argomenti dicono **quale** testo visualizzare. La funzione `print()` è molto flessibile. Potete passarle un numero:

```python
print(42)
```

Output:
```
42
```

Potete passarle una variabile:

```python
numero = 100
print(numero)
```

Output:
```
100
```

Potete persino passarle un'espressione matematica:

```python
print(5 + 3)
```

Output:
```
8
```

In ogni caso, `print()` prende ciò che gli passate, lo converte in una rappresentazione testuale, e lo visualizza.

## 2.1.4 Invocazione della Funzione: Esecuzione dell'Istruzione

Quando scrivete `print("qualcosa")`, state **invocando** la funzione. L'invocazione di una funzione significa: "Esegui le istruzioni all'interno di questa funzione, utilizzando gli argomenti che ho fornito". Ogni volta che invocate una funzione, il computer:

1. Sospende l'esecuzione del resto del programma
2. Salta al codice della funzione
3. Esegue le istruzioni della funzione con gli argomenti forniti
4. Ritorna al punto in cui era stata invocata la funzione
5. Continua l'esecuzione dal punto di interruzione

Questo accade così velocemente che non lo notate, ma è importante capire che una invocazione di funzione è un "salto" nel flusso di esecuzione del programma.

Considerate questo programma:

```python
print("Prima")
print("Seconda")
print("Terza")
```

Output:
```
Prima
Seconda
Terza
```

Il programma esegue la prima invocazione di `print()`, che visualizza "Prima". Poi esegue la seconda, che visualizza "Seconda". Poi la terza. Semplichiamo, ma è esattamente così che funziona.

## 2.1.5 Laboratorio: Lavorare con la Funzione print()

Prima di approfondire gli argomenti avanzati, è un buon momento per fare esperienza pratica con `print()`.

### Esercizio 1: Il Vostro Nome

Scrivete un programma che stampa il vostro nome:

```python
print("Alice")
```

### Esercizio 2: Numeri

Scrivete un programma che stampa alcuni numeri:

```python
print(1)
print(2)
print(3)
print(42)
print(-5)
```

### Esercizio 3: Operazioni Aritmetiche

Scrivete un programma che stampa il risultato di operazioni aritmetiche:

```python
print(2 + 2)      # Stampa: 4
print(10 - 3)     # Stampa: 7
print(4 * 5)      # Stampa: 20
print(100 / 4)    # Stampa: 25.0
```

### Esercizio 4: Variabili

Scrivete un programma che crea variabili e le stampa:

```python
nome = "Bob"
eta = 25
salario = 50000.0

print(nome)
print(eta)
print(salario)
```

## 2.1.6 La Funzione print(): Effetti, Argomenti e Valori Restituiti

Ora approfondiremo come `print()` funziona a un livello più sofisticato.

### L'Effetto Secondario di print()

Una caratteristica importante di `print()` è che ha un **effetto secondario**. Un effetto secondario è qualcosa che una funzione fa oltre a restituire un valore. Nel caso di `print()`, l'effetto secondario è visualizzare il testo sullo schermo. Molte funzioni restituiscono un valore ma non hanno effetti secondari. Ad esempio, la funzione `len()` restituisce la lunghezza di una stringa, ma non fa nulla sullo schermo. `print()`, d'altra parte, ha un effetto secondario visibile ma restituisce anche un valore—anche se quel valore è `None`.

```python
# len() restituisce un valore senza effetti secondari
lunghezza = len("ciao")
print(lunghezza)  # Stampa: 4

# print() ha un effetto secondario (visualizza il testo)
# e restituisce None (un valore speciale che significa "niente")
risultato = print("Ciao")
print(risultato)  # Stampa: None
```

### Il Valore Restituito di print()

Sebbene `print()` visualizzi il testo sullo schermo, non restituisce il testo stesso come valore. Restituisce `None`, che è un valore speciale in Python che significa "niente" o "assenza di valore". Questo è importante perché significa che non potete fare qualcosa come:

```python
# Questo NON funziona come potreste sperare
testo = print("Ciao")  # testo conterrà None, non "Ciao"
```

Se volete immagazzinare una stringa e stamparla, dovete farlo esplicitamente:

```python
testo = "Ciao"
print(testo)  # Stampa: Ciao
```

## 2.1.7 Istruzioni: Le Linee di Codice che Python Esegue

Un'**istruzione** è una linea di codice che il Python esegue. Ogni istruzione fa qualcosa: assegna un valore, invoca una funzione, modifica una variabile, ecc.

```python
print("Ciao")        # Istruzione 1: invoca print()
x = 5                # Istruzione 2: assegna 5 a x
print(x)             # Istruzione 3: invoca print() con il valore di x
```

In Python, le istruzioni sono generalmente separate da interruzioni di riga. Una interruzione di riga segna la fine di un'istruzione e l'inizio della successiva. Tuttavia, potete anche mettere più istruzioni sulla stessa riga separandole con un punto e virgola:

```python
x = 5; y = 10; print(x + y)  # Tre istruzioni sulla stessa riga
```

Ma questa pratica è generalmente sconsigliata perché riduce la leggibilità. Python favorisce il codice leggibile e ben formattato, come abbiamo visto nel capitolo precedente quando abbiamo discusso dello Zen di Python: "La leggibilità conta".

## 2.1.8 Caratteri di Escape e Newline di Python

Uno dei concetti più importanti quando lavorate con `print()` è come gestire caratteri speciali e formattazione. A volte, volete che il vostro output contenga cose che non potete digitare facilmente sulla tastiera, come un'interruzione di riga (newline) o una tabulazione. Python utilizza il sistema dei **caratteri di escape**. Un carattere di escape è una sequenza di due caratteri che comincia con una barra rovesciata `\` e rappresenta un carattere speciale.

### L'Escape Newline: \n

Il più comune carattere di escape è `\n`, che rappresenta un'interruzione di riga (newline). Quando Python vede `\n` in una stringa, crea una nuova riga:

```python
print("Riga 1\nRiga 2\nRiga 3")
```

Output:
```
Riga 1
Riga 2
Riga 3
```

Senza `\n`, tutto sarebbe su una sola riga:

```python
print("Riga 1 Riga 2 Riga 3")
```

Output:
```
Riga 1 Riga 2 Riga 3
```

### Il Comportamento Predefinito di print(): Newline Automatico

Ecco un fatto importante: ogni volta che invocate `print()`, Python aggiunge automaticamente una newline al termine dell'output. Quindi:

```python
print("Riga 1")
print("Riga 2")
```

Output:
```
Riga 1
Riga 2
```

Anche se non avete digitato `\n`, le due linee rimangono separate. Questo accade perché `print()` aggiunge una newline alla fine di ogni output per impostazione predefinita. Questo comportamento predefinito può essere modificato, come vedremo più avanti.

### L'Escape Tab: \t

Un altro carattere di escape utile è `\t`, che rappresenta una tabulazione:

```python
print("Nome\tEta\tCittà")
print("Alice\t25\tMilano")
print("Bob\t30\tRoma")
```

Output:
```
Nome    Eta     Città
Alice   25      Milano
Bob     30      Roma
```

Questo è utile per creare output in colonne.

### Escape della Barra Rovesciata: \\

Se volete visualizzare una barra rovesciata letterale, dovete scappare la barra rovesciata stessa con un'altra barra rovesciata:

```python
print("Questo è un percorso: C:\\Utenti\\Alice")
```

Output:
```
Questo è un percorso: C:\Utenti\Alice
```

### Escape della Virgoletta: \" e \'

Se volete includere una virgoletta dentro una stringa delimitata da virgolette, potete scappare la virgoletta interna:

```python
print("Mi ha detto: \"Ciao!\"")
```

Output:
```
Mi ha detto: "Ciao!"
```

Oppure potete usare virgolette singole intorno alla stringa:

```python
print('Mi ha detto: "Ciao!"')
```

Output:
```
Mi ha detto: "Ciao!"
```

## 2.1.9 Utilizzo di Più Argomenti

Finora abbiamo passato un solo argomento a `print()`. Ma `print()` è molto più potente quando usata con più argomenti. Potete passare più argomenti a `print()` separandoli con virgole:

```python
print("Ciao", "mondo", "!")
```

Output:
```
Ciao mondo !
```

Notate che `print()` ha automaticamente inserito uno spazio tra gli argomenti. Per impostazione predefinita, `print()` separa gli argomenti con uno spazio. Potete stampare numeri, stringhe, variabili, tutto insieme:

```python
nome = "Alice"
eta = 25
print("Nome:", nome)
print("Età:", eta)
print("Età tra 5 anni:", eta + 5)
```

Output:
```
Nome: Alice
Età: 25
Età tra 5 anni: 30
```

Questo è enormemente utile per creare output formattato e leggibile.

## 2.1.10 Argomenti Posizionali

Gli argomenti che abbiamo visto finora sono **argomenti posizionali**. Il loro significato dipende dalla loro posizione (ordine) all'interno della lista di argomenti. In `print("Ciao", "mondo")`, il primo argomento è "Ciao" e il secondo è "mondo". Se invertite l'ordine:

```python
print("mondo", "Ciao")
```

Output:
```
mondo Ciao
```

L'ordine cambia il risultato. Questo è il significato di "posizionale": la posizione dell'argomento conta.

La funzione `print()` interpreta i suoi argomenti posizionali in questo modo:
- Il primo argomento è il valore principale da stampare
- Il secondo argomento è un ulteriore valore da stampare (separato dal primo da uno spazio)
- E così via per quanti argomenti fornite

```python
print(1, 2, 3, 4, 5)  # Stampa: 1 2 3 4 5
```

## 2.1.11 Argomenti Nominati (Keyword Arguments)

Oltre agli argomenti posizionali, `print()` accetta anche **argomenti nominati** (keyword arguments). Un argomento nominato viene specificato usando il nome del parametro seguito da un segno di uguale e il valore. I due argomenti nominati più utili di `print()` sono:

### sep: Il Separatore

Per impostazione predefinita, `print()` separa gli argomenti con uno spazio. Potete cambiare questo comportamento usando l'argomento nominato `sep`:

```python
print("A", "B", "C")  # Output: A B C (separatore predefinito: spazio)
print("A", "B", "C", sep="-")  # Output: A-B-C (separatore personalizzato: trattino)
print("A", "B", "C", sep="")  # Output: ABC (senza separatore)
print("A", "B", "C", sep="||")  # Output: A||B||C
```

Questo è utile quando volete creare output in formati specifici:

```python
# Creare un formato CSV
print("Nome", "Cognome", "Età", sep=",")
print("Alice", "Rossi", 25, sep=",")
```

Output:
```
Nome,Cognome,Età
Alice,Rossi,25
```

### end: La Fine della Riga

Per impostazione predefinita, `print()` termina con una newline (`\n`). Potete cambiare questo usando l'argomento nominato `end`:

```python
print("A", end="")
print("B", end="")
print("C")
```

Output:
```
ABC
```

Senza `end=""`, ogni invocazione di `print()` creerebbe una nuova riga. Cambiando `end`, potete controllare esattamente come termina l'output. Un altro esempio:

```python
print("Inserisci il tuo nome:", end=" ")  # Stampa il prompt senza newline
# L'utente può digitare sulla stessa riga
```

Potete combinare `sep` e `end`:

```python
print("A", "B", "C", sep="-", end="!\n")  # Output: A-B-C!
```

## 2.1.12 Laboratorio: La Funzione print() e i Suoi Argomenti

Ora è il momento di fare pratica con le tecniche che abbiamo imparato.

### Esercizio 1: Output Formattato Semplice

Scrivete un programma che stampa tre numeri su linee separate:

```python
print(10)
print(20)
print(30)
```

Risultato atteso:
```
10
20
30
```

### Esercizio 2: Usando sep

Scrivete un programma che stampa una data nel formato GG/MM/AAAA:

```python
print(25, 12, 2024, sep="/")
```

Risultato atteso:
```
25/12/2024
```

### Esercizio 3: Usando end

Scrivete un programma che stampa i numeri da 1 a 5 sulla stessa riga:

```python
print(1, end=" ")
print(2, end=" ")
print(3, end=" ")
print(4, end=" ")
print(5)
```

Risultato atteso:
```
1 2 3 4 5
```

### Esercizio 4: Combinare Argomenti

Scrivete un programma che stampa informazioni su una persona:

```python
nome = "Alice"
cognome = "Rossi"
eta = 25
print(nome, cognome, eta, sep=" - ")
```

Risultato atteso:
```
Alice - Rossi - 25
```

### Esercizio 5: Escape Characters

Scrivete un programma che utilizza caratteri di escape:

```python
print("Riga 1\nRiga 2\nRiga 3")
print("Colonna1\tColonna2\tColonna3")
print("Percorso: C:\\Utenti\\Alice")
```

Risultato atteso:
```
Riga 1
Riga 2
Riga 3
Colonna1    Colonna2    Colonna3
Percorso: C:\Utenti\Alice
```

## 2.1.13 Laboratorio: Formattare l'Output

La formattazione dell'output è cruciale per rendere i programmi user-friendly. Esaminiamo come creare output attraente e ben organizzato.

### Concetto 1: Allineamento Visivo

Quando stampate elenchi o tabelle, volete che i dati siano allineati:

```python
# Output non formattato
print("Nome:", "Alice")
print("Città:", "Milano")
print("Paese:", "Italia")
```

Output:
```
Nome: Alice
Città: Milano
Paese: Italia
```

Questo va bene, ma potete renderlo più leggibile con una tabulazione.

### Tecnica 1: Usare Tab per l'Allineamento

```python
print("Nome:\tAlice")
print("Città:\tMilano")
print("Paese:\tItalia")
```

Output:
```
Nome:   Alice
Città:  Milano
Paese:  Italia
```

### Tecnica 2: Usare sep per Creare Tabelle

```python
# Intestazione
print("Nome", "Età", "Città", sep=" | ")
print("-" * 30)
# Dati
print("Alice", 25, "Milano", sep=" | ")
print("Bob", 30, "Roma", sep=" | ")
print("Charlie", 28, "Napoli", sep=" | ")
```

Output:
```
Nome | Età | Città
------------------------------
Alice | 25 | Milano
Bob | 30 | Roma
Charlie | 28 | Napoli
```

### Tecnica 3: Usare newline per Struttura

```python
print("=== INFORMAZIONI PERSONALI ===")
print()  # Riga vuota
print("Nome: Alice")
print("Cognome: Rossi")
print("Età: 25")
print()  # Riga vuota
print("=== CONTATTO ===")
print("Email: alice@example.com")
print("Telefono: +39 123 456 7890")
```

Output:
```
=== INFORMAZIONI PERSONALI ===

Nome: Alice
Cognome: Rossi
Età: 25

=== CONTATTO ===
Email: alice@example.com
Telefono: +39 123 456 7890
```

### Tecnica 4: Combinare Tutto

Creiamo un programma più complesso che combina tutte le tecniche:

```python
# Dati della persona
nome = "Alice"
cognome = "Rossi"
eta = 25
salario = 50000.0

# Intestazione
print("╔" + "═" * 48 + "╗")
print("║" + " " * 15 + "PROFILO DIPENDENTE" + " " * 15 + "║")
print("╚" + "═" * 48 + "╝")
print()

# Informazioni
print("Nome Completo:\t" + nome + " " + cognome)
print("Età:\t\t" + str(eta) + " anni")
print("Salario Annuo:\t€" + str(salario))
print()

# Dettagli
print("─" * 50)
print("Informazioni aggiornate al:", end=" ")
print("2024")
```

Output:
```
╔════════════════════════════════════════════════╗
║           PROFILO DIPENDENTE                  ║
╚════════════════════════════════════════════════╝

Nome Completo:  Alice Rossi
Età:            25 anni
Salario Annuo:  €50000.0

──────────────────────────────────────────────────
Informazioni aggiornate al: 2024
```

### Esercizi di Formattazione

**Esercizio 1: Piramide di Numeri**

Scrivete un programma che stampa una piramide:

```python
print("*")
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)
```

**Esercizio 2: Tabella di Moltiplicazione**

Scrivete un programma che stampa una piccola tabella di moltiplicazione:

```python
print("X", "2", "4", "6", sep="\t")
print("2", "4", "8", "12", sep="\t")
print("3", "6", "12", "18", sep="\t")
print("4", "8", "16", "24", sep="\t")
```

**Esercizio 3: Banner Decorato**

Scrivete un programma che crea un banner decorato:

```python
print("╔" + "═" * 30 + "╗")
print("║" + " BENVENUTO AL MIO PROGRAMMA ".center(30) + "║")
print("╚" + "═" * 30 + "╝")
```

**Esercizio 4: Poesia Formattata**

Scrivete un programma che stampa una poesia con una corretta formattazione:

```python
print("La programmazione è un'arte")
print("Dove la logica danza con la creatività")
print()
print("Ogni riga di codice è una pennellata")
print("Su una tela infinita di possibilità")
print()
print("Python sussurra con eleganza")
print("Insegnandoci il potere della semplicità")
```

## Conclusione: Il Potere dell'Output

La funzione `print()` è molto più che uno strumento semplice per visualizzare il testo. È il vostro canale di comunicazione con l'utente del programma. Imparare a usarla bene significa imparare a creare programmi che sono non solo funzionali, ma anche user-friendly e piacevoli da usare.

Abbiamo visto come `print()` può adattarsi a vostri bisogni attraverso argomenti posizionali e nominati. Abbiamo imparato come controllare la separazione tra elementi e come terminare l'output. Abbiamo esplorato i caratteri di escape che permettono di formattare il testo con newline, tab, e altri simboli speciali.

La capacità di formattare bene l'output è una competenza spesso sottovalutata dai principianti. Ma quando userete programmi con interfacce belle e ben organizzate, apprezzerete quanto sia importante. Nel vostro prossimo programma, prendetevi un momento per pensare a come il vostro utente vedrà l'output. La differenza tra un programma che stampa semplicemente i risultati e uno che li presenta in modo chiaro e attraente è fondamentale.

Nei prossimi capitoli, scoprirete altre funzioni incorporate (built-in) di Python, imparerete a prendere input dall'utente, e lavorerete con dati di diversi tipi. Ma `print()` rimane il vostro strumento più importante per comprendere cosa il vostro programma sta facendo e per comunicare i risultati al mondo.