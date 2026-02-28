"""
CAPITOLO 9 - CLASSI
Esercizio: Creare una classe Dog (Cane) e istanziare oggetti

CONCETTI CHIAVE INTRODUTTI:
- Definizione di classi come "blueprint" (progetti) per creare oggetti
- Metodo __init__() per inizializzazione (costruttore)
- Attributi di istanza: dati specifici per ogni oggetto
- Metodi di istanza: comportamenti (azioni) dell'oggetto
- Creazione di istanze (oggetti) e accesso ai loro dati
- La keyword 'self': riferimento all'istanza corrente

NOTA FILOSOFICA:
Una classe è un modello concettuale di una "cosa" del mondo reale. Il cane
reale è un'istanza di quella classe. Due cani diversi condividono lo stesso
"tipo" (classe Dog) ma hanno attributi diversi (nome, età).
"""

# ============================================================================
# 1. DEFINIZIONE DELLA CLASSE DOG
# ============================================================================

class Dog:
    """
    Modello di un cane.
    
    Una classe è come uno "stampo" o "progetto" che descrive:
    - Che dati (attributi) avrà ogni cane
    - Che azioni (metodi) ogni cane può compiere
    
    In Python, i nomi delle classi seguono la convention CapWords (PascalCase):
    prima lettera maiuscola, senza underscore.
    """

    # ========================================================================
    # METODO __init__(): IL COSTRUTTORE
    # ========================================================================
    
    def __init__(self, name, age):
        """
        Inizializza gli attributi di un'istanza di Dog.
        
        Il metodo __init__ (dunder method, special method) è il COSTRUTTORE:
        viene chiamato AUTOMATICAMENTE quando creiamo una nuova istanza.
        
        Parametri:
            self: Riferimento all'istanza che stiamo creando. Python lo passa
                  automaticamente, non lo specifichiamo nella chiamata.
            name: Il nome del cane (str).
            age: L'età del cane in anni (int).
        
        COSA SUCCEDE:
        Dog("Turbo", 10) → __init__ riceve self=<istanza>, name="Turbo", age=10
        
        IMPORTANTE - Attributi di istanza:
        Assegniamo i parametri a self.<attributo> per "incollare" i dati
        all'istanza specifica. Ogni cane avrà il suo name e age indipendenti.
        """
        # self.name = "Turbo" per questa istanza, self.name = "Diesel" per altra
        self.name = name
        self.age = age
    
    # ========================================================================
    # METODI DI ISTANZA: COMPORTAMENTI
    # ========================================================================
    
    def sit(self):
        """
        Simula il comportamento del cane che si siede.
        
        Un metodo è una funzione "incollata" a una classe.
        Come __init__, riceve sempre 'self' come primo parametro (implicito).
        
        Usiamo self.name per accedere all'attributo specifico di questa istanza.
        Se avessimo 100 cani, ogni uno conoscerebbe il suo nome.
        """
        # f-string con accesso all'attributo tramite self.name
        print(f"{self.name} è ora seduto.")
    
    def roll_over(self):
        """
        Simula il comportamento del cane che rotola.
        
        Questo metodo non prende parametri oltre a self, perché l'azione
        (rotolare) non ha bisogno di ulteriori informazioni.
        """
        print(f"{self.name} ha rotolato!")


# ============================================================================
# 2. UTILIZZO DELLA CLASSE: ISTANZIAZIONE
# ============================================================================

# --- Creazione della prima istanza ---

# Istanziazione: creiamo un oggetto CONCRETO basato sul progetto (classe Dog).
# 
# Cosa accade:
# 1. Python crea un nuovo oggetto in memoria
# 2. Chiama __init__ passando i parametri: name="Turbo", age=10
# 3. self viene impostato automaticamente a questo nuovo oggetto
# 4. Gli attributi vengono assegnati: my_dog.name = "Turbo", my_dog.age = 10
# 5. L'oggetto finito viene restituito e assegnato a my_dog

my_dog = Dog("Turbo", 10)

# --- Accesso agli attributi (Dot Notation) ---

# La "dot notation" (notazione col punto) permette di accedere ai dati
# incollati all'istanza. Leggiamo gli attributi specifici di my_dog.

print(f"Il nome del mio cane è {my_dog.name}.")
# Output: Il nome del mio cane è Turbo.

print(f"Il mio cane ha {my_dog.age} anni.")
# Output: Il mio cane ha 10 anni.

# --- Invocazione di metodi ---

# Metodi vengono invocati con la dot notation seguito da parentesi.
# self viene passato AUTOMATICAMENTE (non lo scriviamo):
# my_dog.sit() → equivale a sit(self=my_dog)

my_dog.sit()
# Output: Turbo è ora seduto.

# Quale altro metodo potremmo invocare? Vediamo...
my_dog.roll_over()
# Output: Turbo ha rotolato!


# ============================================================================
# 3. ISTANZE MULTIPLE: INDIPENDENZA DEI DATI
# ============================================================================

# La potenza delle classi: possiamo creare MOLTI oggetti dallo stesso modello.
# Ogni istanza ha i SUOI attributi indipendenti.

# Creiamo un secondo cane con dati diversi
your_dog = Dog("Diesel", 9)

# your_dog ha il SUO name e age, completamente separato da my_dog
# (vivono in indirizzi di memoria diversi)

print(f"Il nome del tuo cane è {your_dog.name}.")
# Output: Il nome del tuo cane è Diesel.

print(f"Il tuo cane ha {your_dog.age} anni.")
# Output: Il tuo cane ha 9 anni.

# Invochiamo metodi su your_dog - userà i SUOI attributi
your_dog.roll_over()
# Output: Diesel ha rotolato!


# ============================================================================
# 4. OSSERVAZIONI DIDATTICHE
# ============================================================================

"""
COSA ABBIAMO IMPARATO:

1. CLASSI COME BLUEPRINT:
   - La classe Dog è un progetto astratto
   - Descrive COSA è un cane (attributi) e COSA PUÒ FARE (metodi)

2. ISTANZE COME OGGETTI CONCRETI:
   - my_dog e your_dog sono istanze reali della classe Dog
   - Sono oggetti diversi con dati diversi
   - Vivono in locazioni di memoria diverse

3. ATTRIBUTI DI ISTANZA:
   - self.name e self.age sono legati a ogni istanza
   - Cambiar my_dog.name non influenza your_dog.name

4. METODI E SELF:
   - I metodi ricevono self automaticamente
   - self permette di accedere ai dati dell'istanza
   - sit() conosce quale cane l'ha chiamato (tramite self)

5. INCAPSULAMENTO:
   - Abbiamo "incapsulato" dati (attributi) e comportamenti (metodi)
     nella stessa entità concettuale (la classe)
   - Questo rende il codice organizzato e intuitivo

DIFFERENZA CHIAVE:
my_dog.sit() → Turbo è ora seduto.
your_dog.sit() → Diesel è ora seduto.

Stesso metodo, risultati diversi perché self è diverso!
"""

# ============================================================================
# 5. VERIFICHE DI IDENTITÀ (BONUS)
# ============================================================================

# Due istanze sono due OGGETTI diversi in memoria?
print(f"\nmy_dog è your_dog? {my_dog is your_dog}")
# Output: False (sono oggetti diversi)

print(f"my_dog è un'istanza di Dog? {isinstance(my_dog, Dog)}")
# Output: True (my_dog è stato creato dalla classe Dog)

# Che tipo di oggetto è my_dog?
print(f"Tipo di my_dog: {type(my_dog)}")
# Output: Tipo di my_dog: <class '__main__.Dog'>

# Indirizzi di memoria (identità dell'oggetto)
print(f"\nIdentità di my_dog: {id(my_dog)}")
print(f"Identità di your_dog: {id(your_dog)}")
# Output: due numeri diversi = due oggetti diversi in memoria