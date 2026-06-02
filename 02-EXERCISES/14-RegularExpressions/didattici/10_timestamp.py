import re

# Stringhe di esempio (nomi di file tipici da output di laboratorio)
filename1 = '20240315_093000_GaSb_P1.2E-3_T450.txt'
filename2 = '20240315_093000_GaSb_P1.2E-3_T450_AB.txt'

# 1. Definizione del Pattern (Regex)
# Usiamo un "Named Capturing Group" (?P<nome>...) per dare un nome al gruppo catturato.
# \d{8} cerca esattamente 8 cifre (la data YYYYMMDD)
# _ cerca il carattere underscore
# \d{6} cerca esattamente 6 cifre (l'ora HHMMSS)
ts_pattern = r'(?P<ts>\d{8}_\d{6})'

print("--- 1. APPROCCIO DIRETTO (re.search) ---")
# Questo approccio va bene per operazioni "una tantum".
# Passiamo il pattern testuale direttamente alla funzione di modulo.
match_diretto = re.search(ts_pattern, filename1)

if match_diretto:
    print(f"Tipo del match object: {type(match_diretto)}")
    print(f"Timestamp estratto (tramite nome 'ts'): {match_diretto.group('ts')}")
    print(f"Timestamp estratto (tramite indice 1): {match_diretto.group(1)}")
print()


print("--- 2. APPROCCIO COMPILATO (re.compile) ---")
# Questo approccio è ideale se devi usare lo stesso pattern molte volte (es. in un ciclo su mille file).
# Compilando la regex, Python la traduce in bytecode riutilizzabile, ottimizzando le prestazioni.
ts_compilato = re.compile(ts_pattern)

print(f"Tipo di 'ts_compilato': {type(ts_compilato)}")

# Ora usiamo il metodo .search() direttamente sull'oggetto regex compilato
match_compilato = ts_compilato.search(filename2)

if match_compilato:
    print(f"Timestamp estratto dal secondo file: {match_compilato.group('ts')}")