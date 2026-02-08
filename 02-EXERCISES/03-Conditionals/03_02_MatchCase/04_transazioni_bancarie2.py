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


# Definisco le categoria come COSTANTI all'inizio per rendere il codice più
# facilmente modificabile in futuro
ENTRATA = "ENTRATA"
USCITA = "USCITA"
TRASFERIMENTO = "TRASFERIMENTO"
PROBLEMA = "PROBLEMA"

# Funzioni ausiliarie, vanno posizionata prima della definizione main
def aggrega_transazione(riepilogo, categoria, transazione):
    """Aggrega una transazione alla categoria specificata."""
    riepilogo[categoria]['conteggi'] += 1
    riepilogo[categoria]['totale'] += transazione["importo"]
    riepilogo[categoria]['transazioni'].append(transazione["descrizione"])

def formatta_rapporto(riepilogo):
    """Stampa rapporto formattato."""
    print("RAPPORTO TRANSAZIONI BANCARIE")
    for k, v in riepilogo.items():
        print(f"{k} ({v['colore']})")
        print(f"\tNumero: {v['conteggi']} | Totale: €{v['totale']:.2f}")

def main():
    # Dati di input forniti dall'AI
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
        ENTRATA : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': "verde"},
        USCITA : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': "rosso"},
        TRASFERIMENTO : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': "blu"},
        PROBLEMA : {'totale': 0, 'conteggi' : 0, 'transazioni' : [], 'colore': "grigio"},
    }

    for transazione in transazioni:
        tipologia = transazione.get("tipo", "").lower()

        match tipologia:
            case "deposito" | "stipendio":
                aggrega_transazione(riepilogo, ENTRATA, transazione)
            case "prelievo" | "pagamento":
                aggrega_transazione(riepilogo, USCITA, transazione)
            case "bonifico":
                aggrega_transazione(riepilogo, TRASFERIMENTO, transazione)
            case "errore":
                aggrega_transazione(riepilogo, PROBLEMA, transazione)
            case _:  # ← Aggiungi questo!
                print(f"Tipo non riconosciuto: {tipologia}")

    formatta_rapporto(riepilogo)

# ============================================================================
# PUNTO DI INGRESSO DEL PROGRAMMA
# ============================================================================
# 
# Python assegna una variabile speciale __name__ a ogni file .py:
# 
#   - Se ESEGUI il file direttamente:   __name__ = "__main__"
#   - Se IMPORTI il file da altri:      __name__ = "nome_modulo"
# 
# Questa condizione garantisce che il codice sotto if __name__ == "__main__":
# si esegua SOLO quando lo script viene lanciato direttamente.
# 
# Vantaggio: Se qualcun altro importa funzioni da questo file, non esegue
# per sbaglio il main(). Per esempio:
#   from banca import aggrega_transazione  # Importa solo la funzione
#                                           # main() NON si esegue
# 
# È una best practice universale in Python. Usalo sempre per separare
# "codice che fa da libreria" da "codice che fa da programma standalone".
#
if __name__ == "__main__":
    main()