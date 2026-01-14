# 02-Lists

**Esercizi consolidati**: 11
**Generato il**: 14/01/2026 18:30
**Sorgente**: `02-Lists`

---

## 2_01_names

```python
# Store the names of a few of your friends in a list called names.
# Print each person's name by accessing each element in the list, one at a time.

names = ['Leonardo', 'Michelangelo', 'Donatello', 'Raffaello']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
```

---

## 2_02_greetings

```python
# Start with the list used in exercise 1.
# Print a message to the names.
# each message should be the same, but personalized with the name.

names = ['Leonardo', 'Michelangelo', 'Donatello', 'Raffaello']

print(f'Ciao {names[0]}, come stai?')
print(f'Ciao {names[1]}, come stai?')
print(f'Ciao {names[2]}, come stai?')
print(f'Ciao {names[3]}, come stai?')
```

---

## 2_03_guest_list

```python
# Make a list that includes at least 3 people you'd like to invite to dinner.
# Use your list to print a message to each person, inviting them to dinner

peoples = ['Napoleone', 'Hammurabi', 'Attila', 'Garibaldi']

print(f'Caro {peoples[0]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[1]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[2]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[3]}, vuoi venire a cena questa sera?')
```

---

## 2_04_changing_guest_list

```python
# start with exercise 3 guest list.
# Add a print() call at the end of your program, stating the name of the guests 
# who can't make it
# Modify your list replacing the name of the guest who can make it.
# Print a set of invitations, one for each person who is still in  your list.

peoples = ['Napoleone', 'Hammurabi', 'Attila', 'Garibaldi']

print(f"L'invitato {peoples[3]} ha rifiutato l'invito")

peoples[3] = 'Traiano'

print(f'Caro {peoples[0]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[1]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[2]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[3]}, vuoi venire a cena questa sera?')
```

---

## 2_05_more_guests

```python
# start with the lists of previous exercise. 
# Add a print() call informing people that you found a bigger table.
# Use insert() to add one new guest at the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages

peoples = ['Napoleone', 'Hammurabi', 'Attila', 'Garibaldi']

print(f'Cari {peoples[0]}, {peoples[1]}, {peoples[2]}, {peoples[3]}, ho prenotato un tavolo più grande.\n')

# Aggiungi nuovo ospite all'inizio
peoples.insert(0, 'Cleopatra')

# Aggiungi nuovo ospite a metà lista
middle_index = len(peoples) // 2
peoples.insert(middle_index, 'Caterina')

# Aggiungi nuovo ospite alla fine della lista
peoples.append('Irene')

# Stampa inviti
print(f'Caro {peoples[0]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[1]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[2]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[3]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[4]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[5]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[6]}, vuoi venire a cena questa sera?')
```

---

## 2_06_mutabilita

```python
# ============================================================================
# DIMOSTRAZIONE: MUTABILITÀ vs IMMUTABILITÀ in Python
# ============================================================================
# Questo script dimostra la differenza fondamentale tra tipi mutabili 
# (come le liste) e tipi immutabili (come le stringhe) quando si assegnano
# variabili in Python.
#
# CONCETTO CHIAVE:
# - Tipi MUTABILI: l'assegnazione crea un ALIAS (stesso oggetto in memoria)
# - Tipi IMMUTABILI: l'assegnazione con nuovi valori crea NUOVI OGGETTI
# ============================================================================

# ----------------------------------------------------------------------------
# PARTE 1: LISTE (tipo MUTABILE)
# ----------------------------------------------------------------------------

# Creo una lista e la assegno a nazioni_uno
nazioni_uno = ['Francia', 'Spagna', 'Italia', 'Portogallo']

# ATTENZIONE: questa NON è una copia!
# nazioni_due è solo un ALIAS di nazioni_uno
# Entrambe le variabili puntano alla STESSA lista in memoria
nazioni_due = nazioni_uno

# Stampo entrambe le variabili - al momento sono identiche
print("=== STATO INIZIALE LISTE ===")
print(f"nazioni_uno: {nazioni_uno}")
print(f"nazioni_due: {nazioni_due}\n")

# ----------------------------------------------------------------------------
# PARTE 2: STRINGHE (tipo IMMUTABILE)
# ----------------------------------------------------------------------------

# Creo una stringa e la assegno a nome_uno
nome_uno = "napoleone bonaparte"

# Anche qui, inizialmente entrambe puntano alla stessa stringa
nome_due = nome_uno

# Stampo entrambe le variabili - al momento sono identiche
print("=== STATO INIZIALE STRINGHE ===")
print(f"nome_uno: {nome_uno}")
print(f"nome_due: {nome_due}\n")

# ----------------------------------------------------------------------------
# PARTE 3: MODIFICHE e DIFFERENZE di COMPORTAMENTO
# ----------------------------------------------------------------------------

# MODIFICA LA LISTA: cambio un elemento tramite indicizzazione
# Siccome nazioni_uno e nazioni_due sono ALIAS della stessa lista,
# la modifica si riflette su ENTRAMBE le variabili
nazioni_uno[1] = 'Germania'

# MODIFICA LA STRINGA: riassegno la variabile
# Le stringhe sono IMMUTABILI, quindi non posso fare nome_uno[0] = 'g'
# Posso solo creare una NUOVA stringa e farla puntare a nome_uno
# nome_due continua a puntare alla stringa originale
nome_uno = 'giulio cesare'

# ----------------------------------------------------------------------------
# PARTE 4: RISULTATI
# ----------------------------------------------------------------------------

print("=== DOPO LE MODIFICHE ===")
print("\n--- LISTE ---")
print(f"nazioni_uno: {nazioni_uno}")
print(f"nazioni_due: {nazioni_due}")  # SORPRESA: anche questa è cambiata!
print("^ Entrambe mostrano la modifica perché puntano allo stesso oggetto")

print("\n--- STRINGHE ---")
print(f"nome_uno: {nome_uno}")
print(f"nome_due: {nome_due}")  # Questa è rimasta invariata
print(
    "^ nome_due è rimasta invariata perché "
    "nome_uno ora punta a un nuovo oggetto"
)
```

---

## 2_07_playlist

```python
# =============================================================================
# ESERCIZIO 1: GESTIONE PLAYLIST MUSICALE
# =============================================================================
# Crea una lista chiamata 'playlist' con almeno 5 canzoni
# Poi esegui le seguenti operazioni:
# - Aggiungi una nuova canzone all'inizio della playlist
# - Rimuovi la terza canzone
# - Sposta l'ultima canzone in seconda posizione
# - Ordina la playlist alfabeticamente e stampala
# - Crea una seconda versione ordinata al contrario senza modificare l'originale

# Il tuo codice qui:

# Creo la playlist
playlist = [
    'Eight Days A Week', 
    'Let It Be', 
    'In My Life', 
    'Hey Jude', 
    'While My Guitar Gently Weeps',
]

# Inserisco una nuova canzone all'inizio
playlist.insert(0, 'Yesterday')

# Eliminato la terza canzone
del playlist[2]

# Sposto ultimo elemento al secondo posto
canzone_spostata = playlist.pop()
playlist.insert(1, canzone_spostata)

# Ordino alfabeticamente
playlist.sort()
print(playlist)

#Inverto
reversed_playlist = list(reversed(playlist))
print(reversed_playlist)

# Alternativa inversione: usando sorted() con reverse=True
```

---

## 2_08_classifica_videogiochi

```python
# =============================================================================
# ESERCIZIO 2: CLASSIFICA VIDEOGIOCHI
# =============================================================================
# Parti da questa lista di videogiochi in ordine casuale:

giochi = ["Zelda", "Mario", "Tetris", "Minecraft", "Fortnite"]

# Esegui le seguenti operazioni:
# - Stampa la classifica 
# - Inverti completamente l'ordine della classifica
# - Rimuovi il gioco in ultima posizione
# - Inserisci "GTA" al secondo posto
# - Stampa quanti giochi ci sono nella classifica finale

# Il tuo codice qui:

# print() può ricevere più oggetti separati da virgola
# e li stampa sulla stessa riga con uno spazio tra loro
print("Classifica iniziale:", giochi)

giochi.reverse()
print("Classifica invertita:", giochi)

giochi.pop()
print(giochi)

giochi.insert(1, 'GTA')
print(giochi)

print(len(giochi))
```

---

## 2_09_libreria_personale

```python
# =============================================================================
# ESERCIZIO 3: LIBRERIA PERSONALE
# =============================================================================
# Crea una lista 'libreria' con 5 libri
# Poi esegui le seguenti operazioni:
# - Aggiungi 2 libri alla fine
# - Elimina il primo libro usando l'indice
# - Scopri quale metodo usare per **contare quante volte appare** un certo 
#   titolo (suggerimento: cerca nei metodi delle liste)
# - Trova il metodo per **svuotare completamente** la lista (ricerca necessaria!)
# - Verifica che la lista sia vuota stampando la sua lunghezza

# Il tuo codice qui:

libri = [
    'Cuori in Atlantide', 
    'Fight Club', 
    'Huckleberry Finn', 
    'Le Rane', 
    '1984',]

# Aggiungo due libri alla fine e stampo la lista aggiornata
libri.append('Fiori per Algernon')
libri.append('Guida galattica per gli autostoppisti')
print("Lista aggiornata:", libri)

# Elimino primo libro in lista e stampo la lista
del libri[0]
print("Lista dopo eliminazione:", libri)

# Conto occorrenze
conteggio = libri.count('1984')
print("Occorrenze dell'elemento '1984':", conteggio)

# Svuoto la lista
libri.clear()

# Verifico che ci siano 0 elementi
print("Lunghezza lista:", len(libri))
```

---

## 2_10_code_stack

```python
# =============================================================================
# ESERCIZIO 4: GESTIONE CODE E STACK
# =============================================================================
# Crea una lista 'attesa' con 4 nomi di persone in coda
# Simula le seguenti situazioni:
# - L'arrivo di 2 nuove persone (aggiungi alla fine)
# - Il servizio della prima persona in coda (usando indice)
# - Una persona che abbandona la coda (rimuovi per valore)
# - Stampa: "Ci sono X persone in attesa"
# - **SFIDA**: cerca come **copiare** la lista in una nuova variabile 
#   'attesa_backup' senza che le modifiche all'una influenzino l'altra 
#   (ricerca richiesta!)

# Il tuo codice qui:

persone = ['Leonardo', 'Michelangelo', 'Raffaello', 'Donatello']

# Arrivano due persone
persone.append('Tiziano')
persone.append('Giorgione')

# Prima persona è servita
servito = persone.pop(0)
print("Persona servita:", servito)

# Rimuovo elemento con valore
persone.remove('Raffaello')

# Stampo il numero di persone in coda
print(f"Ci sono {len(persone)} persone in attesa")

# Copia della lista
attesa_backup = persone.copy()

```

---

## 2_11_analisi_temperature

```python
# =============================================================================
# ESERCIZIO 5: ANALISI TEMPERATURE
# =============================================================================
# Crea una lista 'temperature' con 7 valori numerici
# (esempio: 18, 22, 19, 25, 21, 23, 20)
# Poi esegui le seguenti operazioni:
# - Aggiungi una temperatura anomala molto alta alla fine (es. 35)
# - Ordina le temperature
# - Scopri quale metodo permette di trovare **l'indice** di un valore 
#   specifico nella lista (ricerca!)
# - Trova l'indice della temperatura più alta
# - Crea una lista ordinata al contrario senza modificare 'temperature'
# - Calcola e stampa: "Differenza tra max e min: X gradi" 
#   (usa indicizzazione per prendere primo e ultimo elemento della lista 
#   ordinata)

# Il tuo codice qui:

temperature = [18, 22, 19, 25, 21, 23, 20]

# Registrato nuovo valore
temperature.append(35)

# Ordino da più piccolo a più grande
temperature.sort()

# controllo qual è il valore massimo e poi da quello ricavo indice
print(
    "L'indice temperatura più alta è:", temperature.index(max(temperature))
)

# nuova lista riordinata al contrario
temperature_reversed = list(reversed(temperature))
print(temperature_reversed)

# calcolo della differenza
differenza = max(temperature) - min(temperature)
print("La differenza tra valore massimo e minimo è:", differenza)
```

---

