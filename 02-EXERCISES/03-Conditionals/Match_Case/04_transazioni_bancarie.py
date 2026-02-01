#
# ESERCIZIO: Classificatore di Transazioni Bancarie
#
# Una banca registra transazioni quotidiane. Ogni transazione ha:
# - tipo: "deposito", "prelievo", "bonifico", "stipendio", "pagamento", "errore"
# - importo: valore numerico
# - descrizione: stringa con dettagli
#
# Richieste:
# 1) Leggi una lista di transazioni (fornita sotto)
# 2) Per ogni transazione, classifica usando match/case:
#    - "deposito", "stipendio" → categoria "ENTRATA" con colore "verde"
#    - "prelievo", "pagamento" → categoria "USCITA" con colore "rosso"
#    - "bonifico" → categoria "TRASFERIMENTO" con colore "blu"
#    - "errore" → categoria "PROBLEMA" con colore "grigio"
# 3) Costruisci un dizionario di riepilogo con struttura:
#    {
#      "ENTRATA": {"totale": X, "count": Y, "transazioni": [...]},
#      "USCITA": {"totale": X, "count": Y, "transazioni": [...]},
#      ...
#    }
# 4) Stampa un rapporto formattato (vedi output atteso sotto)
#
# VINCOLI:
# - Usa match/case (non if/elif)
# - Usa dizionari annidati per aggregazione
# - Calcola totale e numero transazioni per categoria
# - Non usare try/except
#

# DATI DI INPUT (lista di transazioni)
transazioni = [
    {"tipo": "deposito", "importo": 500, "descrizione": "Deposito iniziale"},
    {"tipo": "stipendio", "importo": 2500, "descrizione": "Stipendio febbraio"},
    {"tipo": "prelievo", "importo": 100, "descrizione": "Prelievo ATM"},
    {"tipo": "pagamento", "importo": 80, "descrizione": "Bolletta luce"},
    {"tipo": "bonifico", "importo": 300, "descrizione": "Trasferimento amico"},
    {"tipo": "deposito", "importo": 250, "descrizione": "Rimborso"},
    {"tipo": "errore", "importo": 0, "descrizione": "Operazione fallita"},
    {"tipo": "prelievo", "importo": 50, "descrizione": "Prelievo ATM"},
    {"tipo": "stipendio", "importo": 2500, "descrizione": "Stipendio marzo"},
    {"tipo": "pagamento", "importo": 150, "descrizione": "Abbonamento internet"},
]

riepilogo = {
    "ENTRATA" : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': ""},
    "USCITA" : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': ""},
    "TRASFERIMENTO" : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': ""},
    "PROBLEMA" : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': ""},
}

for transazione in transazioni:
    # dict.get("tipo") può restituire None, Pylant si lamenta
    # None non ha il metodo .lower()
    tipologia = transazione.get("tipo", "").lower() # se manca "tipo", usi ""

    match tipologia:
        case "deposito" | "stipendio":
            riepilogo['ENTRATA']['conteggi'] += 1
            riepilogo['ENTRATA']['totale'] += transazione["importo"]
            riepilogo['ENTRATA']['transazioni'].append(transazione["descrizione"])
            riepilogo['ENTRATA']['colore'] = "verde"
        case "prelievo" | "pagamento":
            riepilogo['USCITA']['conteggi'] += 1
            riepilogo['USCITA']['totale'] += transazione["importo"]
            riepilogo['USCITA']['transazioni'].append(transazione["descrizione"])
            riepilogo['USCITA']['colore'] = "rosso"
        case "bonifico":
            riepilogo['TRASFERIMENTO']['conteggi'] += 1
            riepilogo['TRASFERIMENTO']['totale'] += transazione["importo"]
            riepilogo['TRASFERIMENTO']['transazioni'].append(transazione["descrizione"])
            riepilogo['TRASFERIMENTO']['colore'] =  "blu"
        case "errore":
            riepilogo['PROBLEMA']['conteggi'] += 1
            riepilogo['PROBLEMA']['totale'] += transazione["importo"]
            riepilogo['PROBLEMA']['transazioni'].append(transazione["descrizione"])
            riepilogo['PROBLEMA']['colore'] = "grigio"


print("RAPPORTO TRANSAZIONI BANCARIE")

for k, v in riepilogo.items():
    print(f"{k} ({v['colore']})")
    print(f"\tNumero: {v['conteggi']} | Totale: €{v['totale']}")


# OUTPUT ATTESO (approssimativo - valori aggregati):
# ┌─────────────────────────────────────────┐
# │ RAPPORTO TRANSAZIONI BANCARIE           │
# ├─────────────────────────────────────────┤
# │ ENTRATA (verde)                         │
# │   Numero: 3 | Totale: €5750.00         │
# │ USCITA (rosso)                          │
# │   Numero: 3 | Totale: €380.00          │
# │ TRASFERIMENTO (blu)                     │
# │   Numero: 1 | Totale: €300.00          │
# │ PROBLEMA (grigio)                       │
# │   Numero: 1 | Totale: €0.00            │
# └─────────────────────────────────────────┘
#