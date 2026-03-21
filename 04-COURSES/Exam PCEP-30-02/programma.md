## Syllabus di riferimento (PCEP-30-02)

### Sezione 1 - Computer Programming and Python Fundamentals (18%)

**1.1** Termini fondamentali:
interprete vs. compilatore; lessico, sintassi, semantica.

**1.2** Logica e struttura di Python:
keyword; istruzioni; indentazione; commenti.

**1.3** Letterali, variabili, sistemi numerici:
booleani, interi, float; notazione scientifica; stringhe;
sistemi binario/ottale/decimale/esadecimale; variabili; convenzioni di naming; PEP-8.

**1.4** Operatori e tipi di dati:
operatori numerici (`** * / % // + -`); operatori su stringhe (`* +`);
operatori di assegnazione e shortcut; operatori unari e binari; priorita' e binding;
operatori bitwise (`~ & ^ | << >>`); operatori booleani (`not, and, or`);
espressioni booleane; operatori relazionali (`== != > >= < <=`);
accuratezza dei float; type casting.

**1.5** Input/Output da console:
`print()` e `input()`; parametri `sep=` e `end=`; `int()` e `float()`.

### Sezione 2 - Control Flow (29%)

**2.1** Decisioni e branching:
`if`, `if-else`, `if-elif`, `if-elif-else`; condizioni multiple; nesting.

**2.2** Iterazioni:
`pass`; `while`, `for`, `range()`, `in`; iterare su sequenze;
`while-else` e `for-else`; nesting; `break` e `continue`.

### Sezione 3 - Data Collections (25%)

**3.1** Liste:
costruzione di vettori; indicizzazione e slicing; `len()`; metodi (`append()`,
`insert()`, `index()`, ecc.); `sorted()`; `del`; iterazione con `for`;
`in` e `not in`; list comprehension; copia e clonazione; matrici e cubi.

**3.2** Tuple:
indicizzazione, slicing, costruzione, immutabilita'; tuple vs. liste;
liste dentro tuple e tuple dentro liste.

**3.3** Dizionari:
costruzione, indicizzazione, aggiunta e rimozione di chiavi;
iterazione su dizionari, chiavi e valori; verifica esistenza chiavi;
metodi `keys()`, `items()`, `values()`.

**3.4** Stringhe:
costruzione; indicizzazione, slicing, immutabilita'; escape con `\`;
virgolette e apostrofi; stringhe multi-linea; funzioni e metodi di base.

### Sezione 4 - Functions and Exceptions (28%)

**4.1** Funzioni:
definizione e invocazione; generatori; `return`; `None`; ricorsione.

**4.2** Interazione funzione-ambiente:
parametri vs. argomenti; passaggio posizionale, keyword, misto;
valori di default; scope, name hiding (shadowing), `global`.

**4.3** Gerarchia delle eccezioni built-in:
`BaseException`; `Exception`; `SystemExit`; `KeyboardInterrupt`;
eccezioni astratte; `ArithmeticError`; `LookupError`; `IndexError`;
`KeyError`; `TypeError`; `ValueError`.

**4.4** Gestione delle eccezioni:
`try-except`; `try-except Exception`; ordine dei rami `except`;
propagazione attraverso i confini di funzione; delega della responsabilita'.