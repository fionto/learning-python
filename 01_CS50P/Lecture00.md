# Riassunto Lezione 0: Funzioni e Variabili (CS50P)

## 1. Introduzione all'Ambiente di Sviluppo [00:00:41]
* **VS Code:** L'editor di testo consigliato per scrivere codice.
* **Terminale (CLI):** L'interfaccia a riga di comando per interagire con il computer.
* **File .py:** Tutti i programmi Python devono avere l'estensione `.py`.
* **Esecuzione:** Si esegue un programma digitando `python nome_file.py` nel terminale.

## 2. Prime Funzioni e Argomenti [00:05:39]
* **Funzione:** Un'azione o un "verbo" che dice al computer di fare qualcosa (es. `print()`).
* **Argomento:** L'input che passiamo a una funzione (es. il testo dentro `print("ciao")`).
* **Bug e Sintassi:** Un errore nel codice. Il computer è letterale: una parentesi mancante causerà un `SyntaxError`.

## 3. Variabili e Input [00:12:40]
* **input():** Funzione per chiedere informazioni all'utente.
* **Variabile:** Un contenitore per memorizzare dati (es. `name = input(...)`).
* **Assegnamento (=):** Il simbolo `=` non significa uguaglianza matematica, ma copia il valore da destra verso sinistra.

## 4. Commenti e Pseudocodice [00:20:16]
* **Commenti (#):** Note scritte per gli esseri umani, ignorate dal computer.
* **Pseudocodice:** Scrivere la logica del programma in linguaggio naturale prima di tradurlo in codice.

## 5. Manipolazione delle Stringhe (str) [00:25:42]
* **Parametri di print:**
    * `sep`: Definisce come separare più argomenti (default: spazio).
    * `end`: Definisce cosa stampare alla fine (default: nuova riga `\n`).
* **f-strings:** Modo moderno per inserire variabili nel testo: `f"Ciao, {name}"`.
* **Metodi delle stringhe:**
    * `.strip()`: Rimuove gli spazi bianchi all'inizio e alla fine.
    * `.title()`: Capitalizza la prima lettera di ogni parola.
    * `.split()`: Divide una stringa in più parti.

## 6. Numeri: Integers (int) e Floats [00:59:32]
* **int:** Numeri interi. Operatori: `+`, `-`, `*`, `/`, `%` (modulo/resto).
* **Casting (Conversione):** `input()` restituisce sempre testo (stringa). Bisogna usare `int()` o `float()` per fare calcoli.
* **float:** Numeri con la virgola (decimali).
* **round():** Funzione per arrotondare i numeri.
* **Formattazione:** Usare f-strings per aggiungere separatori di migliaia o limitare i decimali (es. `:.2f`).

## 7. Creare le proprie Funzioni [01:26:13]
* **def:** Parola chiave per definire una funzione personalizzata.
* **Struttura:** ```python
    def hello(to="world"):
        print("hello,", to)
    ```
* **Scope (Ambito):** Una variabile creata dentro una funzione esiste solo dentro quella funzione.
* **main():** Convenzione per raggruppare la logica principale del programma.
* **return:** Parola chiave per far sì che una funzione restituisca un valore al chiamante.

---

## 💡 Note Conclusive e Concetti Chiave

* **Il Concetto di Astrazione:** Una delle lezioni più importanti. Definire funzioni personalizzate permette di "nascondere" la complessità. Una volta scritta una funzione `hello()` o `square()`, non dobbiamo più preoccuparci di *come* funzioni internamente, ma solo di *cosa* faccia.
* **Problem Solving come Algoritmo:** La programmazione viene presentata non come studio della sintassi, ma come il processo di prendere un **Input**, rielaborarlo in una "Black Box" (il nostro codice) e produrre un **Output**.
* **Leggibilità (Clean Code):** Non basta che il codice funzioni. Deve essere leggibile per gli esseri umani. L'uso di nomi di variabili descrittivi (es. `name` invece di `n`) e una struttura pulita con la funzione `main()` sono pratiche professionali essenziali.
* **Effetti Collaterali vs Valori di Ritorno:** * Una funzione come `print()` ha un **effetto collaterale**: visualizza del testo a schermo.
    * Una funzione con `return` restituisce un **valore** che il computer può riutilizzare per altri calcoli. Capire questa distinzione è cruciale per la logica avanzata.
* **Interfaccia Utente e Robustezza:** Piccoli accorgimenti come `.strip()` o `.title()` mostrano l'importanza di rendere il programma "robusto", ovvero capace di gestire input dell'utente imprevisti (spazi extra, minuscole/maiuscole errate) senza rompersi o produrre risultati sbagliati.
* **Il Mindset del Programmatore:** I bug non sono fallimenti, ma parte integrante del processo. La lezione incoraggia un approccio iterativo: scrivi un po' di codice, testalo, correggi gli errori e procedi.
