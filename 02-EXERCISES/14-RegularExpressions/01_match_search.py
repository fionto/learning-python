import re

filename = "diamante_20240315"
sample, date = filename.split("_")

print(f"Sample: {sample} | Date: {date}")

# Pattern per data in formato YYYYMMDD 
## \d{4} = esattamente 4 cifre, \d{2} = esattamente 2 cifre
pattern_date = r'\d{4}\d{2}\d{2}'  # equivalente a r'\d{8}'

# ✅ search - cerca ovunque
# e restituisce un oggetto match al primo incontro
search1 = re.search(pattern_date, filename) 
print(search1.group())

#re.match -> vincola la ricerca all'inizio della stringa
match1 = re.match(pattern_date, date)       # ✅ match - funziona perché date inizia con 8 cifre
match2 = re.match(pattern_date, filename)   # restituisce None se non lo trova o non è all'inizio
print(match1.group())
# print(match2.group()) # ❌ AttributeError! None non ha metodo .group()

# ✅ CORRETTO - gestione dell'errore
if match2:
    print(f"match su filename: {match2.group()}")
else:
    print("match2 è None - re.match() non ha trovato il pattern all'inizio della stringa")
    print("Suggerimento: usa re.search() se non sei certo che il pattern sia all'inizio")