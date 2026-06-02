import re
from datetime import datetime

FILENAME_PATTERN = re.compile(
    r'^'
    # 1. timestamp YYYYMMDD_HHMMSS
    r'(?P<ts>\d{8}_\d{6})'
    # 2. nome campione
    r'_(?P<sample>[A-Za-z0-9]+)'
    # 3. pressione: numero puro nel gruppo 'pressure', unità (opzionale) nel gruppo 'press_unit'
    r'_P(?P<pressure>[0-9]*\.?[0-9]+(?:[Ee][+-]?\d+)?)(?P<press_unit>[A-Za-z]+)?'
    # 4. temperatura: numero puro nel gruppo 'temperature', unità (opzionale) nel gruppo 'temp_unit'
    r'_T(?P<temperature>\d+)(?P<temp_unit>[Cc]|[Kk])?'
    # 5. allineamento opzionale
    r'(?:_(?P<alignment>AB|BA))?'
    # 6. estensione
    r'\.txt$',
    re.IGNORECASE
)

def parse_filename(filename: str) -> dict | None:
    """Estrae i metadati da un nome file di misura.

    Args:
        filename: Nome del file da analizzare.

    Returns:
        Dizionario con i campi estratti, oppure None se il formato
        non corrisponde.
    """
    m = FILENAME_PATTERN.match(filename)
    if not m:
        return None
    
    return {
        'sample':         m.group('sample'),
        'timestamp':      datetime.strptime(m.group('ts'), '%Y%m%d_%H%M%S'),
        # Ora float() riceve solo stringhe numeriche pulite come '1.2E-3' o '5e-4'
        'pressure':       float(m.group('pressure')),
        'pressure_unit':  m.group('press_unit') if m.group('press_unit') else 'Torr', # Default a Torr se assente
        # int() riceve solo cifre pure come '450' o '300'
        'temperature':    int(m.group('temperature')),
        'temperature_unit': m.group('temp_unit').upper() if m.group('temp_unit') else 'K', # Default a K se assente
        'alignment':      m.group('alignment'),  # None se assente
    }


# --- Test ---
casi = [
    '20240315_093000_GaSb_P1.2E-3_T450.txt',
    '20240315_093000_GaSb_P1.2E-3mbar_T450C_AB.txt',  # Con unità mbar e Celsius
    '20240316_120000_InAs_P5e-4torr_T300K_BA.txt',    # Con unità torr e Kelvin
    'file_senza_formato.txt',
    '20240315_093000_GaSb_P1.2E-3_T450_CD.txt',        # Allineamento non valido
]

for nome in casi:
    risultato = parse_filename(nome)
    if risultato:
        print(f"OK  {nome}")
        print(f"    campione:     {risultato['sample']}")
        print(f"    timestamp:    {risultato['timestamp']}")
        print(f"    pressione:    {risultato['pressure']} {risultato['pressure_unit']}")
        print(f"    temperatura:  {risultato['temperature']} °{risultato['temperature_unit'] if risultato['temperature_unit'] != 'K' else 'K'}")
        print(f"    allineamento: {risultato['alignment']}")
    else:
        print(f"NO  {nome}")
    print()