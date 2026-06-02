import re

filenames = [
        '20240315_093000_GaSb_P1.2E-3_T450.txt',
        '20240315_093000_GaSb_P1.2E-3torr_T450_AB.txt',
        '20240315_093000_GaSb_P1.2E-3mbar_T450_BA.txt',
    ]

# The verbose pattern with line-by-line documentation
pattern = r"""
    _P                          # Matches the literal prefix '_P'
    (?P<pressure>               # Start of named capturing group 'pressure'
        [0-9]*\.?[0-9]+         # Matches a decimal or integer (e.g., 12, 0.12, .12)
        (?:                     # Start of optional non-capturing group for scientific notation
            [Ee][+-]?\d+        # Matches 'E' or 'e', an optional sign, and digits (e.g., e-5, E+10)
        )?                      # Makes the scientific notation optional
        (?:                     # Start of optional non-capturing group for units
            [A-Za-z]+           # Matches one or more alphabetic characters (e.g., Pa, bar, psi)
        )?                      # Makes the unit optional
    )                           # End of the 'pressure' capturing group
"""
# Added re.VERBOSE flag here so Python ignores the whitespace and comments
regex_compilata = re.compile(pattern, re.VERBOSE)

for i, nome_file in enumerate(filenames, 1):
    print(f"\nAnalisi File {i}: {nome_file}")
    
    match = regex_compilata.search(nome_file)
    
    if match:
        print("  [SUCCESSO] Corrispondenza trovata!")
        pressione_estratta = match.group('pressure')
        print(f"  -> Pressure (Gruppo 'pressure'): {pressione_estratta}")

    else:
        print("  [ERRORE] Il nome del file non segue il pattern previsto.")