# Domande Concettuali
## SEZIONE 1: CONDIZIONALI (if/elif/else)

**1.1** Il condizionale `if` è usato per decidere se una certa sezione di codice viene eseguita o no. La struttura `if/else` invece ha una ramificazione e permette di eseguire una di due diverse sezioni di codice. Se ho bisogno di scegliere tra due diverse sezioni di codici uso `if/else`.

**1.2** Assegno alla variabile `x` il valore 5 e poi eseguo tutti e tre i confronti nel codice. Vengono eseguiti solo i primi due print: "A" e "B" in quanto per il terzo la condizione è `False`.

**1.3**  La differenza è che in una serie di `if` separati controllo tutte le condizioni ed eseguo le sezioni di codice per le quali la condizione è `True`. In una `if/elif/else` chain invece eseguo solo una sezione di codice, l'unica per le quali le condizioni autoscludenti sarà `True`. Per cui uso la seconda quando ho una sola sezione di codice che voglio eseguire, quella appartenente ad una condizione che si verifica e quella di default `else`.

**1.4** Confronto il valore a cui è stata assegnata la variabile `x` con 5. Il simbolo `==` significa che confronto uguaglianza. Se sono uguali otterrò `True`.

**1.5** L'operatore `and` serve a legare due condizionali e restituirà un valore logice `True` se entrambe le condizioni sono anche esse `True`. Esempio, verifica che una persona abbia 18 anni `and` sia italiana, per poter votare in italia.

**1.6** Tutte e tre le condizioni devono essere verificate contemporaneamente, quindi le legherei con `and`. Tutte e tre devono essere `True`, quindi ad esempio avrò le variabili boleane legate così:
```python
correct_password and not_banned and access_time
```

**1.7** In entrambi i casi eseguo `process_data()` se è `error` è `False`. Il primo codice è più Pythonic perché più corto.

**1.8** Uso `if/elif/else` perché devo eseguire un condizionale logico e credo che il `match/case` è più elegante quando i case sono più corti.

**1.9** Non so cosa sia "short-circuit evaluation". Se la prima parte di un `and` è `False` il risultato è `False` in ogni caso. Se la prima parte di un `or` è `True` il risultato è `True` in ogni caso.

**1.10** Userei `in` se ad esempio devo verificare che una stringa appaia in una lista di stringhe in una singola riga di codice.

**1.11** ```python 
allow_drive = age >= 18 and (has_license or has_permit)```
Questa soluzione è più leggibile perché è una sola riga di codice, senza ramificazioni e si legge quasi come una frase in inglese.

**1.12** Devo controllare che l'età non sia negativa, che sia un numero e non una stringa, che non contenga spazi. Se non è un valore `int` o `float` non riesco ad eseguire l'operatore `>=`. Se è negativa riesco ad eseguire il programma logicamente, ma non esistono età negative.

**1.13** Ho usato un `match/case` per assegnare una etichetta di tipo `str` ad un codice per facilitare le operazioni di `print()` successive. Usare una catena `if/elif/else` avrebbe funzionato ugualmente ma in casi di assegnazione diretta, `match/case` è da preferire in quanto più pythonic.

**1.14** Una variabile booleana ci segnala se una condizione si verifica o meno. Possiamo usarla come flag se la condizione non è troppo complicata, o se non dobbiamo eseguire tante righe di codice in una possibile decisione tra due rami.