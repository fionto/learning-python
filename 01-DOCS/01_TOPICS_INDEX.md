# Python Learning Plan - Topics Index

**Version:** 1.0  
**Last Updated:** 08 Gennaio 2026  

---

## 📑 Indice Completo per Topic Block

### Block 0: Environment Setup & First Steps

#### Setup & Configuration
- Installazione Python su Windows
- Installazione Python su macOS
- Installazione Python su Linux
- Verifica versione Python (`python --version`)
- Gestione multiple versioni Python

#### Editor & Tools
- Visual Studio Code installation
- Python extension per VS Code
- Configurazione workspace VS Code
- Syntax highlighting e autocomplete
- Integrated terminal in VS Code

#### Esecuzione Codice
- Python REPL (Read-Eval-Print Loop)
- Esecuzione script da file `.py`
- Esecuzione da terminale (Windows: PowerShell, Mac/Linux: Terminal)
- Differenza REPL vs script mode
- Shebang line su Unix (`#!/usr/bin/env python3`)

#### Troubleshooting Iniziale
- PATH environment variable
- `python` vs `python3` command
- Errori comuni installazione
- Verificare installazione con `import sys; sys.version`

---

### Block 1: Variables, Data Types & Basic Operations

#### Variabili
- Assegnamento variabili: `x = 10`
- Naming conventions: `snake_case`, `CONSTANTS`
- Variabili come etichette (labels/references)
- Multiple assignment: `a, b, c = 1, 2, 3`
- Variabili keyword riservate (evitare `class`, `def`, `if`, etc.)

#### Stringhe
- Creazione stringhe: single quotes `'...'`, double quotes `"..."`
- Triple quotes per multiline: `"""..."""`
- String concatenation: `+` operator
- String repetition: `*` operator
- F-strings (formatted string literals): `f"Hello {name}"`
- String methods:
  - `.upper()` - Convert to uppercase
  - `.lower()` - Convert to lowercase
  - `.title()` - Title case (first letter capitalized)
  - `.strip()` - Remove whitespace (leading/trailing)
  - `.lstrip()` - Remove left whitespace
  - `.rstrip()` - Remove right whitespace
  - `.removeprefix(prefix)` - Remove prefix (Python 3.9+)
  - `.removesuffix(suffix)` - Remove suffix (Python 3.9+)
  - `.replace(old, new)` - Replace substring
  - `.find(substring)` - Find index of substring
  - `.split(delimiter)` - Split into list
  - `.join(iterable)` - Join list into string
- Escape characters: `\n`, `\t`, `\\`, `\'`, `\"`
- Raw strings: `r"C:\path\to\file"`
- String immutability

#### Numeri
- Integer (int): `42`, `-10`, `0`
- Float (floating-point): `3.14`, `-0.5`, `2.0`
- Underscore in numbers: `1_000_000`
- Operatori aritmetici:
  - `+` Addition
  - `-` Subtraction
  - `*` Multiplication
  - `/` Division (always returns float)
  - `//` Floor division (integer division)
  - `%` Modulo (remainder)
  - `**` Exponentiation
- Operatori precedenza: PEMDAS (Parentheses, Exponents, Mult/Div, Add/Sub)
- Type casting:
  - `int(x)` - Convert to integer
  - `float(x)` - Convert to float
  - `str(x)` - Convert to string
- Mixed operations: int + float → float

#### Commenti
- Single-line comments: `# comment`
- Multi-line comments: triple quotes o multiple `#`
- When to comment: why, not what
- PEP 20: The Zen of Python (`import this`)

#### Built-in Functions Base
- `print(x)` - Output to console
- `len(x)` - Length of sequence
- `type(x)` - Type of object
- `id(x)` - Memory address (identity)
- `input(prompt)` - Get user input (returns string)

---

### Block 2: Lists - Sequential Collections

#### Creazione e Accesso
- List literal: `[1, 2, 3]`
- Empty list: `[]` o `list()`
- Indexing (0-based): `lista[0]`, `lista[1]`
- Negative indexing: `lista[-1]` (last), `lista[-2]` (second to last)
- Accessing nested lists: `lista[0][1]`

#### CRUD Operations
- **Create/Add:**
  - `.append(item)` - Add to end
  - `.insert(index, item)` - Insert at position
  - `.extend(iterable)` - Add multiple items
  - `+` operator - Concatenate lists
- **Read:**
  - Indexing: `lista[i]`
  - Slicing (vedere Block 5)
- **Update:**
  - `lista[i] = new_value` - Modify element
- **Delete:**
  - `del lista[i]` - Delete by index
  - `.pop()` - Remove and return last item
  - `.pop(index)` - Remove and return item at index
  - `.remove(value)` - Remove first occurrence of value
  - `.clear()` - Remove all items

#### Organizzazione e Sorting
- `.sort()` - Sort in-place (modifica lista)
- `sorted(lista)` - Return sorted copy (lista immutata)
- `.sort(reverse=True)` - Sort descending
- `.reverse()` - Reverse in-place
- `reversed(lista)` - Return reversed iterator

#### List Methods
- `.count(value)` - Count occurrences
- `.index(value)` - Find first index of value
- `.copy()` - Shallow copy
- `len(lista)` - Number of elements
- `min(lista)` - Minimum value
- `max(lista)` - Maximum value
- `sum(lista)` - Sum of numeric elements

#### Concetti Avanzati
- Mutabilità: liste sono modificabili
- Aliasing vs Copia:
  - `lista2 = lista1` - Alias (stessa lista in memoria)
  - `lista2 = lista1.copy()` - Copia shallow
  - `lista2 = lista1[:]` - Copia tramite slicing
  - `lista2 = list(lista1)` - Copia tramite constructor
- List identity: `id(lista)` per verificare indirizzo memoria
- `is` operator: `lista1 is lista2` (identity check)

---

### Block 3: Control Flow - Conditionals

#### Espressioni Booleane
- Boolean type: `True`, `False`
- Truthiness:
  - Falsy values: `False`, `0`, `0.0`, `""`, `[]`, `{}`, `None`
  - Truthy: tutto il resto
- Boolean conversion: `bool(x)`

#### Operatori di Confronto
- `==` - Equal to
- `!=` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal
- `<=` - Less than or equal
- `is` - Identity (same object)
- `is not` - Not same object
- `in` - Membership test
- `not in` - Not in sequence

#### Operatori Logici
- `and` - Logical AND
- `or` - Logical OR
- `not` - Logical NOT
- Short-circuit evaluation:
  - `x and y` - Returns x if x is falsy, else y
  - `x or y` - Returns x if x is truthy, else y

#### If Statements
- Basic if:
  ```python
  if condition:
      # code
  ```
- If-else:
  ```python
  if condition:
      # code
  else:
      # code
  ```
- If-elif-else:
  ```python
  if condition1:
      # code
  elif condition2:
      # code
  else:
      # code
  ```
- Nested conditionals (da evitare quando possibile)
- Ternary operator: `x if condition else y`

#### Match/Case (Python 3.10+)
- Pattern matching:
  ```python
  match value:
      case pattern1:
          # code
      case pattern2:
          # code
      case _:
          # default
  ```
- Multiple patterns: `case 1 | 2 | 3:`
- Guard clauses: `case x if x > 10:`

#### Best Practices
- Guard clauses per early return
- Flat conditionals > nested
- Boolean flags per logica aggregata
- Evitare magic numbers (usa costanti)

---

### Block 4: Loops & Iterations

#### For Loops
- Basic syntax:
  ```python
  for item in iterable:
      # code
  ```
- Iterare su liste: `for x in lista:`
- Iterare su stringhe: `for char in stringa:`
- Iterare su dizionari (Block 6)
- Nested loops:
  ```python
  for i in outer:
      for j in inner:
          # code
  ```

#### Range Function
- `range(n)` - 0 to n-1
- `range(start, stop)` - start to stop-1
- `range(start, stop, step)` - with custom step
- Range è lazy (iterator, not list)
- `list(range(5))` - Convert to list

#### While Loops
- Basic syntax:
  ```python
  while condition:
      # code
  ```
- Infinite loop (evitare): `while True:`
- Flag pattern:
  ```python
  active = True
  while active:
      # code che può settare active = False
  ```

#### Loop Control
- `break` - Exit loop immediately
- `continue` - Skip to next iteration
- `pass` - Do nothing (placeholder)
- `else` clause in loops:
  ```python
  for item in lista:
      if condition:
          break
  else:
      # executed if break never called
  ```

#### Iterazione Avanzata
- `enumerate(iterable)` - Get (index, value) pairs
- `enumerate(iterable, start=1)` - Custom start index
- `zip(iter1, iter2)` - Iterate multiple sequences in parallel
- `reversed(iterable)` - Iterate in reverse

#### Indentazione
- Python usa indentazione per definire blocchi
- Standard: 4 spazi (MAI tab)
- Errori comuni:
  - `IndentationError` - Indentazione inconsistente
  - Forgetting indent dopo `:`
  - Extra indent dopo loop

---

### Block 5: Slicing & Sequence Manipulation

#### Slicing Syntax
- Basic: `sequenza[start:stop]`
- With step: `sequenza[start:stop:step]`
- Omissioni:
  - `sequenza[:stop]` - From beginning to stop
  - `sequenza[start:]` - From start to end
  - `sequenza[:]` - Full copy
  - `sequenza[::step]` - Every step-th element

#### Negative Indices
- `sequenza[-1]` - Last element
- `sequenza[-2]` - Second to last
- `sequenza[-3:]` - Last 3 elements
- `sequenza[:-1]` - All except last

#### Step Parameter
- `sequenza[::2]` - Every other element (alternati)
- `sequenza[1::2]` - Every other, starting from index 1
- `sequenza[::-1]` - Reverse sequence
- `sequenza[::-2]` - Reverse, every other

#### Slicing Strings vs Lists
- Strings: slicing returns new string (immutable)
- Lists: slicing returns new list (shallow copy)
- Tuple: slicing returns new tuple

#### Applicazioni Pratiche
- Copying sequences: `new_list = old_list[:]`
- Extracting substrings: `url[8:]` (skip "https://")
- Reversing: `reversed_list = lista[::-1]`
- Sliding window: `window = data[i:i+window_size]`

#### Slice Objects
- Create reusable slice: `s = slice(1, 5, 2)`
- Use: `lista[s]`
- Attributes: `s.start`, `s.stop`, `s.step`

---

### Block 6: Dictionaries - Key-Value Structures

#### Creazione
- Dictionary literal: `{"key": "value"}`
- Empty dict: `{}` o `dict()`
- Constructor: `dict(key1=val1, key2=val2)`
- From pairs: `dict([("k1", "v1"), ("k2", "v2")])`

#### Accesso e Modifica
- Access: `dict[key]`
- Safe access: `dict.get(key, default)`
- Add/Update: `dict[key] = value`
- Update multiple: `dict.update(other_dict)`
- Remove: `del dict[key]`
- Pop: `value = dict.pop(key, default)`
- Clear all: `dict.clear()`

#### Iterazione
- Keys: `for key in dict:` o `for key in dict.keys():`
- Values: `for value in dict.values():`
- Items: `for key, value in dict.items():`
- Sorted keys: `for key in sorted(dict):`

#### Dictionary Methods
- `.get(key, default)` - Safe access
- `.pop(key, default)` - Remove and return
- `.popitem()` - Remove and return arbitrary pair
- `.setdefault(key, default)` - Get or set default
- `.update(other)` - Merge dictionaries
- `.keys()` - View of keys
- `.values()` - View of values
- `.items()` - View of (key, value) pairs
- `.copy()` - Shallow copy

#### Nested Dictionaries
- Dict in dict: `outer[key1][key2]`
- List in dict: `dict[key] = [item1, item2]`
- Dict in list: `lista_dict = [{"k": "v"}, {"k2": "v2"}]`

#### Dictionary Comprehensions ⭐
- Basic: `{k: v for k, v in pairs}`
- With condition: `{k: v for k, v in pairs if condition}`
- From iterable: `{x: x**2 for x in range(10)}`
- Invert dict: `{v: k for k, v in original.items()}`

#### Concetti Avanzati
- Dictionary ordering (Python 3.7+): insertion order preserved
- Key requirements: immutable types only (str, int, tuple, not list)
- Hash tables: O(1) average lookup
- `defaultdict` (preview): auto-initialize missing keys
- `Counter` (preview): counting hashable objects

---

### Block 7: Tuples & Sets

#### Tuples
- Creazione: `(1, 2, 3)` o `1, 2, 3` (packing)
- Single element: `(1,)` (comma required)
- Empty tuple: `()` o `tuple()`
- Immutabilità: non possono essere modificati
- Indexing e slicing: come liste
- Tuple methods:
  - `.count(value)` - Count occurrences
  - `.index(value)` - Find first index

#### Tuple Operations
- Unpacking: `a, b, c = (1, 2, 3)`
- Extended unpacking: `a, *rest, c = (1, 2, 3, 4, 5)`
- Swap values: `a, b = b, a`
- Multiple return values:
  ```python
  def func():
      return x, y  # returns tuple
  ```
- Tuple as dict keys (lists cannot)
- Named tuples:
  ```python
  from collections import namedtuple
  Point = namedtuple('Point', ['x', 'y'])
  p = Point(1, 2)
  print(p.x, p.y)
  ```

#### Sets
- Creazione: `{1, 2, 3}` (no duplicati)
- Empty set: `set()` (NOT `{}` - that's dict)
- From list: `set([1, 2, 2, 3])` → `{1, 2, 3}`
- Add element: `.add(item)`
- Remove: `.remove(item)` (KeyError se assente)
- Discard: `.discard(item)` (no error)
- Pop: `.pop()` (remove arbitrary)
- Clear: `.clear()`

#### Set Operations
- Union: `set1 | set2` o `.union(set2)`
- Intersection: `set1 & set2` o `.intersection(set2)`
- Difference: `set1 - set2` o `.difference(set2)`
- Symmetric difference: `set1 ^ set2` o `.symmetric_difference(set2)`
- Subset: `set1 <= set2` o `.issubset(set2)`
- Superset: `set1 >= set2` o `.issuperset(set2)`

#### Set Comprehensions
- `{x for x in iterable if condition}`
- `{x**2 for x in range(10)}`

#### Quando Usare Cosa
- **List:** Sequenza ordinata, mutabile, duplicati OK
- **Tuple:** Sequenza ordinata, immutabile, hashable
- **Set:** Non ordinato, mutabile, nessun duplicato, O(1) membership

#### Frozenset
- Immutable set: `frozenset([1, 2, 3])`
- Hashable (può essere chiave dict o elemento set)

---

### Block 8: Comprehensions

#### List Comprehensions
- Basic: `[expr for item in iterable]`
- With condition: `[expr for item in iterable if condition]`
- Multiple for: `[expr for item1 in iter1 for item2 in iter2]`
- Ternary: `[x if condition else y for x in iterable]`

#### Dictionary Comprehensions
- Basic: `{key_expr: value_expr for item in iterable}`
- From pairs: `{k: v for k, v in pairs}`
- With condition: `{k: v for k, v in pairs if condition}`
- Invert dict: `{v: k for k, v in dict.items()}`
- From parallel iterables: `{k: v for k, v in zip(keys, values)}`

#### Set Comprehensions
- Basic: `{expr for item in iterable}`
- With condition: `{expr for item in iterable if condition}`
- Unique squares: `{x**2 for x in range(10)}`

#### Nested Comprehensions
- Matrix: `[[0 for _ in range(cols)] for _ in range(rows)]`
- Flatten list: `[item for sublist in lista for item in sublist]`

#### Ternary in Comprehensions
- `[x if x > 0 else 0 for x in lista]`
- Attenzione posizione: `if` dopo `for` è filtro, prima è ternary

#### Performance
- Comprehensions generalmente più veloci di loop equivalenti
- Lazy evaluation con generator expressions (Block 4 preview)
- Trade-off: conciseness vs readability

#### Best Practices
- Max 2 clausole `for` o `if` per leggibilità
- Se troppo complesso → loop esplicito
- Naming: `_` per variabili non usate: `[x for x, _ in pairs]`

---

### Block 9: Functions & Modularity

#### Definizione Funzioni
- Basic syntax:
  ```python
  def function_name(parameters):
      """Docstring"""
      # code
      return value
  ```
- Function naming: `snake_case`
- Return statement (opzionale): `return` o `return value`
- Funzioni senza return → `None` implicito

#### Parametri e Argomenti
- **Parametro:** Variabile nella definizione
- **Argomento:** Valore passato nella chiamata
- Positional arguments: `func(1, 2, 3)`
- Keyword arguments: `func(a=1, b=2)`
- Mix: positional prima, keyword dopo

#### Default Values
- Syntax: `def func(x, y=10):`
- Default deve essere dopo parametri senza default
- Mutable defaults danger:
  ```python
  def bad(x, lista=[]):  # EVITARE
      lista.append(x)    # lista persiste tra chiamate
  
  def good(x, lista=None):  # CORRETTO
      if lista is None:
          lista = []
  ```

#### *args e **kwargs
- `*args` - Tuple di argomenti posizionali arbitrari:
  ```python
  def func(*args):
      for arg in args:
          print(arg)
  ```
- `**kwargs` - Dict di keyword arguments arbitrari:
  ```python
  def func(**kwargs):
      for key, value in kwargs.items():
          print(f"{key}: {value}")
  ```
- Combined: `def func(pos, *args, kw=default, **kwargs):`

#### Scope (LEGB)
- **L**ocal: variabili definite dentro funzione
- **E**nclosing: variabili in funzioni esterne (nested)
- **G**lobal: variabili a livello modulo
- **B**uilt-in: nomi built-in Python
- `global` keyword: modificare variabile globale
- `nonlocal` keyword: modificare variabile enclosing

#### Docstrings
- Triple-quoted string dopo `def`:
  ```python
  def func(x):
      """
      Brief description.
      
      Args:
          x (type): Description
      
      Returns:
          type: Description
      """
  ```
- Stili comuni: Google, NumPy, reStructuredText
- Accesso: `func.__doc__` o `help(func)`

#### Lambda Functions
- Anonymous functions: `lambda args: expr`
- Example: `square = lambda x: x**2`
- Uso comune: sorting key, map/filter
- Limitazione: single expression, no statements

#### Type Hints ⭐
- Function signature:
  ```python
  def func(x: int, y: float = 1.0) -> str:
      return str(x + y)
  ```
- Type annotations:
  - `int`, `float`, `str`, `bool`
  - `list[int]`, `dict[str, int]`
  - `Optional[int]` (può essere None)
  - `Union[int, str]` (int OR str)
- Type checking: `mypy script.py`

#### Recursion (Preview)
- Funzione che chiama se stessa
- Caso base + caso ricorsivo
- Attenzione stack overflow

---

### Block 10: Modules & Libraries

#### Import Statements
- Import module: `import module`
- Import specific: `from module import func`
- Import multiple: `from module import func1, func2`
- Import all: `from module import *` (sconsigliato)
- Import with alias: `import module as alias`
- Function alias: `from module import func as alias`

#### Module Structure
- Module = file `.py`
- Package = directory con `__init__.py`
- Subpackages: nested directories

#### Creare Moduli Custom
- Salvare funzioni in file `.py`
- Importare in altro script: `import mymodule`
- `if __name__ == "__main__":` pattern:
  ```python
  def func():
      pass
  
  if __name__ == "__main__":
      # codice eseguito solo se script lanciato direttamente
      func()
  ```

#### Libreria Standard (Esempi)
- **random:**
  - `random.randint(a, b)` - Random integer
  - `random.choice(seq)` - Random element
  - `random.shuffle(list)` - Shuffle in-place
  - `random.sample(seq, k)` - k random elements
- **math:**
  - `math.sqrt(x)`, `math.pow(x, y)`
  - `math.pi`, `math.e`
  - `math.ceil(x)`, `math.floor(x)`
- **statistics:**
  - `statistics.mean(data)`
  - `statistics.median(data)`
  - `statistics.stdev(data)`
- **datetime:**
  - `datetime.datetime.now()`
  - `datetime.date(year, month, day)`
  - `datetime.timedelta(days=7)`
- **sys:**
  - `sys.argv` - Command-line arguments
  - `sys.exit(code)` - Exit program
  - `sys.version` - Python version

#### Package Management
- **pip:**
  - `pip install package`
  - `pip uninstall package`
  - `pip list` - Installed packages
  - `pip show package` - Package info
  - `pip freeze > requirements.txt` - Export dependencies
  - `pip install -r requirements.txt` - Install from file

#### Command-Line Arguments
- `sys.argv`:
  ```python
  import sys
  script_name = sys.argv[0]
  arg1 = sys.argv[1]
  ```
- `argparse` (preview):
  ```python
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('--name')
  args = parser.parse_args()
  ```

#### Module Search Path
- `sys.path` - List of directories Python searches
- Current directory sempre incluso
- PYTHONPATH environment variable

---

### Block 11: Object-Oriented Programming (OOP)

#### Classi Base
- Definizione:
  ```python
  class ClassName:
      """Docstring"""
      pass
  ```
- Istanza: `obj = ClassName()`
- Naming: `PascalCase` (CapWords)

#### `__init__()` Constructor
- Metodo speciale per inizializzare istanza:
  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  ```
- `self`: riferimento all'istanza corrente
- Chiamato automaticamente: `dog = Dog("Rex", 3)`

#### Attributi
- **Attributi di istanza:** specifici per ogni oggetto
  ```python
  def __init__(self):
      self.attribute = value
  ```
- **Variabili di classe:** condivisi da tutte le istanze
  ```python
  class MyClass:
      class_var = value
  ```
- Accesso: `obj.attribute` o `MyClass.class_var`

#### Metodi
- **Metodi di istanza:** operano su istanza (`self`)
  ```python
  def method(self, param):
      return self.attribute + param
  ```
- **Metodi di classe:** operano su classe (`cls`)
  ```python
  @classmethod
  def method(cls, param):
      return cls.class_var
  ```
- **Metodi statici:** non accedono istanza o classe
  ```python
  @staticmethod
  def method(param):
      return param * 2
  ```

#### Ereditarietà
- Classe child eredita da parent:
  ```python
  class Child(Parent):
      def __init__(self, param1, param2):
          super().__init__(param1)
          self.new_attr = param2
  ```
- `super()`: accede metodi parent
- Method overriding: ridefinire metodo parent in child
- Multiple inheritance (avanzato): `class C(A, B):`

#### Special Methods (Dunder)
- `__init__(self)` - Constructor
- `__str__(self)` - String representation (user-friendly)
- `__repr__(self)` - String representation (debug)
- `__len__(self)` - Len function
- `__eq__(self, other)` - Equality operator `==`
- `__lt__(self, other)` - Less than `<`
- `__add__(self, other)` - Addition `+`
- `__getitem__(self, key)` - Indexing `obj[key]`

#### Properties
- Getter/setter pythonic:
  ```python
  class Circle:
      def __init__(self, radius):
          self._radius = radius
      
      @property
      def radius(self):
          return self._radius
      
      @radius.setter
      def radius(self, value):
          if value < 0:
              raise ValueError("Negative radius")
          self._radius = value
  ```
- Accesso: `circle.radius` (no parentheses)

#### Composition
- Istanze come attributi:
  ```python
  class Car:
      def __init__(self):
          self.engine = Engine()
  ```
- "Has-a" relationship vs ereditarietà ("is-a")

#### Importare Classi
- Single class: `from module import ClassName`
- Multiple: `from module import Class1, Class2`
- Entire module: `import module; obj = module.ClassName()`

---

### Block 12: File I/O & Exception Handling

#### Leggere File
- Basic open:
  ```python
  file = open('filename.txt', 'r')
  content = file.read()
  file.close()
  ```
- Context manager (preferred):
  ```python
  with open('filename.txt') as file:
      content = file.read()
  ```
- Read methods:
  - `.read()` - Entire file as string
  - `.read(size)` - Read size bytes
  - `.readline()` - Single line
  - `.readlines()` - List of lines

#### Scrivere File
- Modes:
  - `'w'` - Write (sovrascrive)
  - `'a'` - Append
  - `'r+'` - Read + Write
- Write methods:
  - `.write(string)` - Write string
  - `.writelines(list)` - Write list of strings

#### Percorsi File
- Relative path: `'data/file.txt'`
- Absolute path: `'/home/user/file.txt'` (Unix), `'C:\\Users\\file.txt'` (Windows)
- `pathlib` module:
  ```python
  from pathlib import Path
  path = Path('folder') / 'file.txt'
  path.exists()
  path.read_text()
  path.write_text(content)
  ```

#### Context Managers
- `with` statement: garantisce chiusura file
- Syntax:
  ```python
  with open('file.txt') as file:
      # operazioni
  # file chiuso automaticamente
  ```
- Multiple files:
  ```python
  with open('in.txt') as f_in, open('out.txt', 'w') as f_out:
      content = f_in.read()
      f_out.write(content.upper())
  ```

#### Exception Handling
- Basic try-except:
  ```python
  try:
      # code che può fallire
  except ErrorType:
      # gestione errore
  ```
- Multiple exceptions:
  ```python
  except (Error1, Error2):
      # handle
  ```
- Else clause:
  ```python
  try:
      # code
  except:
      # handle
  else:
      # eseguito se NO exception
  ```
- Finally clause:
  ```python
  try:
      # code
  finally:
      # eseguito SEMPRE (cleanup)
  ```

#### Exception Types
- `FileNotFoundError` - File non esiste
- `PermissionError` - No permission
- `ValueError` - Invalid value
- `TypeError` - Wrong type
- `KeyError` - Key non in dict
- `IndexError` - Index out of range
- `ZeroDivisionError` - Division by zero
- `AttributeError` - Attribute non esiste
- `ImportError` - Import fallito

#### Raising Exceptions
- `raise ErrorType("message")`
- Re-raise: `raise` (dentro except)
- Custom exceptions:
  ```python
  class CustomError(Exception):
      pass
  ```

#### JSON
- `import json`
- Serialize (Python → JSON):
  - `json.dumps(obj)` - To string
  - `json.dump(obj, file)` - To file
- Deserialize (JSON → Python):
  - `json.loads(string)` - From string
  - `json.load(file)` - From file
- Types mapping:
  - dict ↔ object
  - list, tuple ↔ array
  - str ↔ string
  - int, float ↔ number
  - True ↔ true, False ↔ false
  - None ↔ null

#### CSV (Preview)
- `import csv`
- Reader:
  ```python
  with open('data.csv') as file:
      reader = csv.reader(file)
      for row in reader:
          print(row)  # row is list
  ```
- DictReader:
  ```python
  reader = csv.DictReader(file)
  for row in reader:
      print(row['column'])  # row is dict
  ```

---

### Block 13: Testing & Code Quality

#### Pytest Basics
- Installation: `pip install pytest`
- Test discovery: files `test_*.py` o `*_test.py`
- Test functions: `def test_*():`
- Running: `pytest` (auto-discover), `pytest file.py`

#### Assertions
- Basic: `assert condition`
- With message: `assert condition, "message"`
- Comparisons: `assert x == y`
- Membership: `assert item in lista`
- Type: `assert isinstance(obj, Type)`

#### Testing Functions
- Test structure:
  ```python
  def test_function():
      # Arrange (setup)
      input_data = ...
      # Act (execute)
      result = function(input_data)
      # Assert (verify)
      assert result == expected
  ```
- Test edge cases: 0, negative, empty, None, large values

#### Testing Classes
- Test methods:
  ```python
  def test_class_method():
      obj = MyClass()
      assert obj.method() == expected
  ```
- Test attributes:
  ```python
  def test_attributes():
      obj = MyClass(x=10)
      assert obj.x == 10
  ```

#### Fixtures
- Setup/teardown pattern:
  ```python
  @pytest.fixture
  def sample_data():
      # setup
      data = create_data()
      yield data
      # teardown (optional)
      cleanup(data)
  
  def test_with_fixture(sample_data):
      assert process(sample_data) == expected
  ```

#### Parametrized Tests
- Test multiple inputs:
  ```python
  @pytest.mark.parametrize("input,expected", [
      (1, 2),
      (2, 4),
      (3, 6),
  ])
  def test_double(input, expected):
      assert double(input) == expected
  ```

#### Testing Exceptions
- `pytest.raises()`:
  ```python
  def test_exception():
      with pytest.raises(ValueError):
          function_that_raises()
  ```
- Check message:
  ```python
  with pytest.raises(ValueError, match="invalid"):
      function()
  ```

#### Coverage
- Installation: `pip install pytest-cov`
- Run: `pytest --cov=module`
- Report: `pytest --cov=module --cov-report=html`
- Goal: >80% coverage (non ossessionarsi con 100%)

#### Test Organization
- Structure:
  ```
  project/
  ├── src/
  │   └── module.py
  └── tests/
      └── test_module.py
  ```
- Naming: match file structure

#### TDD Workflow
- **Red:** Write failing test
- **Green:** Write minimum code to pass
- **Refactor:** Improve code, tests still pass

#### Debugging
- `pdb` module:
  - `import pdb; pdb.set_trace()` - Breakpoint
  - Commands: `n` (next), `c` (continue), `p variable` (print), `q` (quit)
- `breakpoint()` (Python 3.7+) - Built-in pdb

---

### Block 14: Regular Expressions

#### Modulo `re`
- `import re`
- Main functions:
  - `re.search(pattern, string)` - Find first match
  - `re.match(pattern, string)` - Match at start
  - `re.findall(pattern, string)` - All matches (list)
  - `re.finditer(pattern, string)` - All matches (iterator)
  - `re.sub(pattern, repl, string)` - Replace
  - `re.split(pattern, string)` - Split

#### Metacaratteri Base
- `.` - Any character (except newline)
- `^` - Start of string
- `$` - End of string
- `*` - 0 or more repetitions
- `+` - 1 or more repetitions
- `?` - 0 or 1 repetition
- `|` - OR operator
- `[]` - Character class
- `()` - Group

#### Character Classes
- `[abc]` - a, b, or c
- `[a-z]` - Any lowercase letter
- `[A-Z]` - Any uppercase letter
- `[0-9]` - Any digit
- `[^abc]` - NOT a, b, or c
- Shortcuts:
  - `\d` - Digit `[0-9]`
  - `\D` - Non-digit
  - `\w` - Word char `[a-zA-Z0-9_]`
  - `\W` - Non-word char
  - `\s` - Whitespace
  - `\S` - Non-whitespace

#### Quantificatori
- `{n}` - Exactly n
- `{n,}` - n or more
- `{n,m}` - Between n and m
- `*` - `{0,}` (0 or more)
- `+` - `{1,}` (1 or more)
- `?` - `{0,1}` (0 or 1)

#### Gruppi
- Capturing: `(pattern)`
- Access: `match.group(1)`, `match.groups()`
- Non-capturing: `(?:pattern)`
- Named: `(?P<name>pattern)`
- Access named: `match.group('name')`

#### Anchors
- `^` - Start of string (or line with MULTILINE)
- `$` - End of string (or line with MULTILINE)
- `\b` - Word boundary
- `\B` - Non-word boundary

#### Flags
- `re.IGNORECASE` o `re.I` - Case-insensitive
- `re.MULTILINE` o `re.M` - `^` and `$` match line boundaries
- `re.DOTALL` o `re.S` - `.` matches newline
- `re.VERBOSE` o `re.X` - Allow comments in regex
- Usage: `re.search(pattern, string, re.I | re.M)`

#### Match Objects
- `.group()` - Matched string
- `.group(n)` - n-th group
- `.groups()` - All groups as tuple
- `.start()`, `.end()` - Match positions
- `.span()` - (start, end) tuple

#### Applicazioni Pratiche
- **Email validation:**
  ```python
  pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
  ```
- **URL parsing:**
  ```python
  pattern = r'https?://([^/]+)'  # extract domain
  ```
- **Date extraction:**
  ```python
  pattern = r'\d{2}/\d{2}/\d{4}'  # DD/MM/YYYY
  ```
- **Phone numbers:**
  ```python
  pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
  ```

#### Raw Strings
- Use `r'...'` for regex patterns
- Evita escape hell: `r'\d+'` instead of `'\\d+'`

#### Performance
- Compile pattern se riutilizzato:
  ```python
  compiled = re.compile(r'\d+')
  compiled.search(string)
  ```
- Attenzione catastrophic backtracking (nested quantifiers)