# Day01_strings

**Esercizi consolidati**: 13
**Generato il**: 03/01/2026 18:45

---

## 01_title_string

```python
name = "ada lovelace"
print(name.title())
```

---

## 02_full_name

```python
#Print full name

first_name = "matteo"
last_name = "mastellone"
full_name = f"{first_name} {last_name}"
print(full_name)
```

---

## 03_personal_message

```python
#Use a variable to represent a person's name, and then print a message
#to that person. Your message should be simple, such as, "Hello Eric,
#would you like to learn some Python today?

name = "Matteo"
print(f"Hello, {name}, would you like to learn some Python, today?")
```

---

## 04_name_cases

```python
#Use a variable to represent a person's name, and then print that person's name in
#lowercase, uppercase, and title case.

name = "matteo"
print(name.upper())
print(name.lower())
print(name.title())
```

---

## 05_famous_quote

```python
#Find a quote from a famous person you admire. Print the quote and the name of its author.

first_name = "albert"
last_name = "einstein"
print(f'{first_name.title()} {last_name.title()} once said, "A person who never made a mistake never tried anything new."')
```

---

## 06_famous_quote_2

```python
#Find a quote from a famous person you admire. Print the quote and the name of its author.
#Represent the famous person's name using a variable called famous_person.

famous_person = "Albert Einstein"
message = f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new.'
print(message)
```

---

## 07_formatta_nome

```python
#Stampa il nome formattato correttamente (iniziali maiuscole, senza spazi extra).

nome = "  mARIO rossi  "

nome_corretto = nome.rstrip()
nome_corretto = nome_corretto.lstrip()
nome_corretto = nome_corretto.title()

print(nome_corretto)
```

---

## 08_formatta_nome_2

```python
#Stampa il nome formattato correttamente (iniziali maiuscole, senza spazi extra).

nome = "  mARIO rossi  "

nome_corretto = nome.strip().title()

print(nome_corretto)
```

---

## 09_messaggio_benvenuto

```python
#Stampa un messaggio del tipo: Ciao Giulia! Benvenuta a Milano. 
#(formattato correttamente, usando un f-string).

nome = "giulia"
citta = "MILANO"

messaggio = f"Ciao {nome.title()}, benvenuta a {citta.title()}"

print(messaggio)
```

---

## 10_pulisci_url

```python
url = "https://www.esempio.com"

#Stampa solo esempio.com, rimuovendo tutti i prefissi.

clean_url = url.removeprefix('https://').removeprefix('www.')

print(clean_url)
```

---

## 11_trova_e_sostituisci

```python
frase = "Python è difficile, Python è noioso"

#Stampa la frase trasformata in: Python è facile, Python è divertente

frase_corretta = frase.replace('difficile', 'facile').replace('noioso', 'divertente')

print(frase_corretta)
```

---

## 12_analizza_stringa

```python
testo = "   Programmazione Python   "

#Stampa tre informazioni su righe separate:
#1 Il testo pulito (senza spazi extra)
#2 La lunghezza del testo pulito
#3 La posizione in cui si trova la parola "Python" nel testo pulito

testo_pulito = testo.strip()

print(testo_pulito)
print(len(testo_pulito))
print(testo_pulito.find('Python'))
```

---

## 13_favorite_number

```python
#Use a variable to represent your favorite number.
#Then, using that variable, create a message that reveals your favorite number.
#Print that message.

favorite_number = 14

message = f"My favorite number is {favorite_number}."

print(message)
```

---

