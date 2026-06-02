import re

stringa = "20240315_093000"

# Due gruppi: data e ora
match = re.match(r'(\d{8})_(\d{6})', stringa)

if match:
    print(match.group(0))   # Stampa: 20240315_093000
    print(match.group(1))   # Stampa: 20240315
    print(match.group(2))   # Stampa: 093000
    print(match.groups())   # Stampa: ('20240315', '093000')