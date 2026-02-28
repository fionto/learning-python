# Esempio dal libro PCC

# Definizione della classe: pensa alla classe come a uno "stampo" o un progetto.
# Usiamo la CapWords convention (iniziali maiuscole) come suggerito dal PEP 8.
class Dog:
    """Modello semplificato di un cane."""

    # Il metodo __init__ è il 'costruttore'.
    # Un metodo è una funzione che appartiene ad una classe.
    # __init__ chiamato automaticamente quando creiamo un nuovo oggetto (istanza).
    # serve a istruire Python su come gestire l'oggetto in situazioni particolari (creazione ecc.)
    # 'self' rappresenta l'istanza specifica che stiamo creando: permette
    # di distinguere i dati di un cane da quelli di un altro.
    def __init__(self, name, age):
        """Inizializza gli attributi del cane."""
        # Attributi: variabili associate a un'istanza della classe.
        self.name = name
        self.age = age

    # I metodi definiscono il comportamento: cosa può "fare" l'oggetto.
    def sit(self):
        """Simula il cane che si siede."""
        # Usiamo self.name per accedere al nome specifico di questa istanza.
        print(f"{self.name} è ora seduto.")

    def roll_over(self):
        """Simula il cane che rotola."""
        print(f"{self.name} ha rotolato!")

# --- UTILIZZO DELLA CLASSE ---

# Istanziazione: creiamo un oggetto reale (my_dog) basato sul progetto (Dog).
# "Turbo" e 10 vengono passati rispettivamente a 'name' e 'age' in __init__.
my_dog = Dog("Turbo", 10)

# Accesso agli attributi: usiamo la "dot notation" (notazione col punto)
# per leggere i dati interni dell'oggetto.
print(f"Il nome del mio cane è {my_dog.name}.")
print(f"Il mio cane ha {my_dog.age} anni.")

# Chiamata dei metodi: chiediamo all'oggetto di eseguire un'azione.
my_dog.sit()

# Si posso creare quante istanze si vogliono da una classe
your_dog = Dog('Diesel', 9)
print(f"Il nome del tuo cane è {your_dog.name}.")
print(f"Il tuo cane ha {your_dog.age} anni.")
your_dog.roll_over()