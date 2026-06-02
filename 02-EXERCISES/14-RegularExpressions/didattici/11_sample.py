import re

filenames = [
        '20240315_093000_GaSb_P1.2E-3_T450.txt',
        '20240315_093000_GaSb_P1.2E-3_T450_AB.txt'
    ]

print("--- FASE 2: ESTRARRE DATA E CAMPIONE INSIEME ---")

# 1. Definizione del Pattern Evoluto
# Abbiamo unito il vecchio pattern dei timestamp con il nuovo pattern del campione.
# Nota l'underscore letterale '_' che unisce i due gruppi nominati.
pattern_completo = r'(?P<ts>\d{8}_\d{6})_(?P<sample>[A-Za-z0-9]+)'
regex_compilata = re.compile(pattern_completo)

# 2. Ciclo di analisi sui file (Didattico per mostrare la flessibilità)
for i, nome_file in enumerate(filenames, 1):
    print(f"\nAnalisi File {i}: {nome_file}")
    
    match = regex_compilata.search(nome_file)
    
    if match:
        print("  [SUCCESSO] Corrispondenza trovata!")
        # Possiamo accedere a entrambi i gruppi catturati dallo stesso match!
        timestamp_estratto = match.group('ts')
        campione_estratto = match.group('sample')
        
        print(f"  -> Timestamp (Gruppo 'ts'): {timestamp_estratto}")
        print(f"  -> Campione  (Gruppo 'sample'): {campione_estratto}")
    else:
        print("  [ERRORE] Il nome del file non segue il pattern previsto.")