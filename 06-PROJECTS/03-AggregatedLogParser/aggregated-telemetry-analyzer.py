# ==============================================================================
# AGGREGATED TELEMETRY ANALYZER
# ==============================================================================
# Project: 03-AggregatedLogParser
# Script: aggregated-telemetry-analyzer.py
# Author: Matteo
# Date: January 2026
# 
# Description:
#   Sistema di analisi telemetria per log di manutenzione della Stazione 
#   Spaziale Internazionale (ISS). Processa report giornalieri dai moduli,
#   identifica anomalie critiche, e genera rapporto di stato aggregato.
#
# Technical Stack:
#   - Data Structures: Nested Dictionaries, Sets
#   - Control Flow: while loops, match-case (Python 3.10+)
#   - Techniques: Data validation, Parsing, Aggregation, Classification
#
# Input Format:
#   "MODULO#TIMESTAMP#SISTEMA#STATO#PRIORITA"
#   Example: "COLUMBUS#02012026-1430#Life Support#95#LOW"
#
# Output:
#   Structured report dictionary with metadata, module metrics, and alerts
# ==============================================================================

# Copia questa variabile nel tuo script
station_logs = [
    "COLUMBUS#02012026-1430#Life Support#95#LOW",
    "DESTINY#02012026-1445#Power Grid#78#HIGH",
    "KIBO#02012026-1500#Communications#45#CRITICAL",
    "   ",  # Log vuoto
    "COLUMBUS#03012026-0800#Thermal Control#88#MEDIUM",
    "DESTINY#02012026-1530#Cooling System#62#MEDIUM",
    "ZARYA#02012026-1600#Navigation",  # Malformato (4 componenti invece di 5)
    "KIBO#03012026-0900#Life Support#92#LOW",
    "COLUMBUS#02012026-1700#Power Grid#55#HIGH",
    "DESTINY#03012026-1000#Life Support#91#LOW",
    "",  # Stringa vuota
    "ZARYA#03012026-1100#Communications#70#MEDIUM",
    "KIBO#02012026-1800#Thermal Control#30#CRITICAL",
    "COLUMBUS#04012026-0700#Life Support#97#LOW",
    "TRANQUILITY#03012026-1200#Water Recovery#85#LOW"
]

# Ulteriore test
station_logs2 = [
    "NODE2#06012026-1000#Berthing#88#LOW",
    "NODE2#06012026-1015#Berthing#92#LOW",
    "NODE3#Invalid#Log",  # Malformato
    "NODE3#Another#Bad#One",  # Malformato (4 componenti)
    "",
    "NODE3",  # Malformato (1 componente)
    "PMM#06012026-1100#Storage#55#CRITICAL",
]

def main():

    # Conteggio dei segnali validi e invalidi
    num_validi = 0
    num_invalidi = 0

    # Set vuoto per nomi moduli
    moduli_unici = set()

    # Dizionario report finale
    report_finale = {
        'metadata': {}, 
        'modules': {}, 
        'critical_alerts': set() # set() mi facilita l'aggiunta di emergenze rilevate
        }

    # Creo le chiavi per il dizionario dei moduli
    keys_modules = {'reports', 'stato_medio', 'emergenze', 'ultimo_report'}

    # Come da richiesta del testo, uso un ciclo while per il processing dei log
    while station_logs:
        segnale_grezzo = station_logs.pop().strip()
        segnale_seg = segnale_grezzo.split('#')

        # Scarto alla radice (richiesta del testo) i segnali vuoti, malformati o con doppio ##
        if len(segnale_seg) != 5:
            num_invalidi +=1
            continue
        
        if len(segnale_seg) == 5:
            num_validi += 1
            provenienza, timestamp, sistema, stato, priorità = segnale_seg # Variabile sistema mai usata
            data = invert_date(timestamp[:8]) # Invertire la data mi permette di fare il confronto tra stringhe
            moduli_unici.add(provenienza)
            emergenza = check_emergenza(stato, priorità)

            if provenienza not in report_finale['modules']:
                report_finale['modules'][provenienza] = dict.fromkeys(keys_modules)
                report_finale['modules'][provenienza]['reports'] = 1
                report_finale['modules'][provenienza]['stato_medio'] = int(stato)
                report_finale['modules'][provenienza]['ultimo_report'] = data
                report_finale['modules'][provenienza]['emergenze'] = 1 if emergenza == "EMERGENZA" else 0
            else:
                # Gestione del numero dei reports
                report_finale['modules'][provenienza]['reports'] += 1
                # Gestione dello stato medio (come numero intero arrotondato)
                media = report_finale['modules'][provenienza]['stato_medio']
                media = media + (int(stato) - media) / report_finale['modules'][provenienza]['reports']
                report_finale['modules'][provenienza]['stato_medio'] = round(media)
                # Gestione data ultimo report
                ultimo_report = report_finale['modules'][provenienza]['ultimo_report']
                ultimo_report = data if data > ultimo_report else ultimo_report # Non sono sicuro che questo è ok per str
                report_finale['modules'][provenienza]['ultimo_report'] = ultimo_report
                # Gestione emergenza
                num_emergenze = report_finale['modules'][provenienza]['emergenze']
                num_emergenze += 1 if emergenza == "EMERGENZA" else 0
                report_finale['modules'][provenienza]['emergenze'] = num_emergenze
            
            if emergenza == "EMERGENZA":
                report_finale['critical_alerts'].add(provenienza)
                

    report_finale['metadata'] = {
        'total_logs': num_validi,
        'invalid_logs': num_invalidi,
        'modules_count': len(moduli_unici)
    }

    # Stampo i risultati
    title = "REPORT STATO STAZIONE SPAZIALE ISS"
    line = "=" * (len(title) + 10)

    print(line)
    print(f"    {title}")
    print(line)

    print('METADATA:')
    print(f"Totale Log Processati: {report_finale['metadata']['total_logs']}")
    print(f"Log Invalidi: {report_finale['metadata']['invalid_logs']}")
    print(f"Moduli Attivi: {report_finale['metadata']['modules_count']}\n")

    print(line)
    print('DETTAGLIO MODULI:')
    print(line)
    for titolo_modulo, dict_modulo in report_finale['modules'].items():
        print(titolo_modulo)
        print(f"Reports: {dict_modulo['reports']}")
        print(f"Stato Medio: {dict_modulo['stato_medio']}")
        print(f"Emergenze: {dict_modulo['emergenze']}")
        print(f"Ultimo Report: {dict_modulo['ultimo_report']}\n")

    print(line)
    print('ALLERTA CRITICA:')
    print(line)
    print("Moduli con emergenze attive:", end = " ")
    for nome in report_finale['critical_alerts']:
        print(nome, end = " ")
    print()

def invert_date(s):
    return s[4:8] + s[2:4] + s[0:2]

def check_emergenza(valore, valutazione):
    v = int(valore)

    # primo filtro: valori fuori range o priorità sconosciute.
    # Decido di dare "EMERGENZA" perché malfunzionamento
    if not (0 <= v <= 100) or valutazione not in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        return "EMERGENZA"

    match (v, valutazione):
        # EMERGENZE
        case (_, "CRITICAL"):
            return "EMERGENZA"
        case (v, _) if v < 60:
            return "EMERGENZA"
        # ATTENZIONI
        case (_, "HIGH"):
            return "ATTENZIONE"
        case (v, _) if v <= 79:
            return "ATTENZIONE"
        #NORMALI
        case (_, "LOW") | (_, "MEDIUM"):
            return "NORMALE" 

main()