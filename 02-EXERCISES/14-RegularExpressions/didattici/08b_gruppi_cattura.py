import re

stringa = "20240315_093000"

# Gruppi nominati
pattern = r'(?P<data>\d{8})_(?P<ora>\d{6})'
match = re.match(pattern, stringa)

if match:
    print(match.group('data'))   # Stampa: 20240315
    print(match.group('ora'))    # Stampa: 093000
    # Oppure come dizionario:
    print(match.groupdict())     # Stampa: {'data': '20240315', 'ora': '093000'}