import re

filenames = [
        '20240315_093000_GaSb_P1.2E-3_T450.txt',
        '20240315_093000_GaSb_P1.2E-3torr_T450_AB.txt',
        '20240315_093000_GaSb_P1.2E-3mbar_T450_BA.txt',
    ]

pattern = r'_P(?P<pressure>[0-9]*\.?[0-9]+(?:[Ee][+-]?\d+)?(?:[A-Za-z]+)?)'
regex_compilata = re.compile(pattern)

for i, nome_file in enumerate(filenames, 1):
    print(f"\nAnalisi File {i}: {nome_file}")
    
    match = regex_compilata.search(nome_file)
    
    if match:
        print("  [SUCCESSO] Corrispondenza trovata!")
        pressione_estratta = match.group('pressure')
        print(f"  -> Pressure (Gruppo 'pressure'): {pressione_estratta}")

    else:
        print("  [ERRORE] Il nome del file non segue il pattern previsto.")