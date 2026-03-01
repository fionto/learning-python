# 03_02_MatchCase

**Esercizi consolidati**: 8
**Generato il**: 01/03/2026 17:14

---

## 01_classificatore_voti

```python
# ESERCIZIO 1: Il Classificatore di Voti
# Obiettivo: Utilizzare match/case per una selezione multipla semplice.
#
# Scrivi un programma che legga la variabile 'voto_lettera'. 
# Il programma deve stampare un messaggio in base al valore:
# - "A": "Eccellente"
# - "B": "Buono"
# - "C": "Sufficiente"
# - "D": "Insufficiente"
# - "F": "Gravemente insufficiente"
# - Qualsiasi altro valore: "Valutazione non valida"

voto_lettera = "W"

match voto_lettera:
    case "A":
        print("Eccellente")
    case "B":
        print("Buono")
    case "C":
        print("Sufficiente")
    case "D":
        print("Insufficiente")
    case "F":
        print("Gravemente insufficiente")
    case _:
        print("Valutazione non valida")
```

---

## 02_calendario

```python
# ESERCIZIO 2: Analizzatore di Calendario
# Obiettivo: Utilizzare l'operatore '|' per raggruppare pattern e la keyword 'as'.
#
# Data la lista 'giorni', itera su di essa. Per ogni elemento, usa un match/case per:
# 1. Identificare se è un giorno feriale (da Lunedì a Venerdì) e stampare: "Lavoro: [nome_giorno]"
# 2. Identificare se è un giorno festivo (Sabato o Domenica) e stampare: "Relax: [nome_giorno]"
# 3. Gestire input errati (es. "Gennaio") catturando il valore e stampando: "[valore] non è un giorno!"

giorni = ["Lunedì", "Sabato", "Mercoledì", "Domenica", "Gennaio"]

for giorno in giorni:
    match giorno:
        case "Lunedì" | "Martedì" | "Mercoledì" | "Giovedì" | "Venerdì" as nome_giorno:
            print(f"Lavoro: {nome_giorno}")
        case "Sabato" | "Domenica" as nome_giorno:
            print(f"Relax: {nome_giorno}")
        case altro:
            print(f"{altro} non è un giorno")
```

---

## 03_smistamento

```python
# ESERCIZIO 3: Sistema di Smistamento Logistico
# Obiettivo: Applicare match/case all'interno di un ciclo per gestire logiche diverse.
#
# Gestisci una serie di pacchi in arrivo rappresentati dalla lista 'carico_magazzino'.
# Per ogni pacco, valuta la stringa del tipo di merce:
# - "elettronica", "informatica": assegna la variabile 'corsia' a 1 e 'fragile' a True.
# - "abbigliamento", "calzature": assegna 'corsia' a 2 e 'fragile' a False.
# - "alimentari": assegna 'corsia' a 3 e 'fragile' a True.
# - Qualsiasi altra merce: assegna 'corsia' a 0 e stampa un avviso di "merce ignota".
# Alla fine di ogni match, stampa un riepilogo: "Pacco [tipo]: Corsia [n], Fragile: [Si/No]"

carico_magazzino = ["elettronica", "abbigliamento", "alimentari", "libri", "informatica"]

for articolo in carico_magazzino:
    match articolo:
        case "elettronica" | "informatica" as tipo:
            corsia = 1
            fragile = True
            print(f"Pacco {tipo}: Corsia {corsia}, Fragile: {'Sì' if fragile else 'No'}")
        case "abbigliamento" | "calzature" as tipo:
            corsia = 2
            fragile = False
            print(f"Pacco {tipo}: Corsia {corsia}, Fragile: {'Sì' if fragile else 'No'}")
        case "alimentari" as tipo:
            corsia = 3
            fragile = True
            print(f"Pacco {tipo}: Corsia {corsia}, Fragile: {'Sì' if fragile else 'No'}")
        case altro:
            corsia = 0
            print(f"Merce ignota: Corsia {corsia}")
            
```

---

## 04_transazioni_bancarie

```python
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
```

---

## 04_transazioni_bancarie2

```python
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
```

---

## 05_ordini

```python
#
# ESERCIZIO: Gestione Ordini E-Commerce
#
# Un negozio online elabora ordini. Ogni ordine contiene:
# - id_ordine: codice univoco
# - importo_base: prezzo senza tasse
# - stato: "pending", "processing", "shipped", "delivered", "cancelled"
# - tipo_cliente: "regular", "vip", "newbie"
# - metodo_pagamento: "carta", "paypal", "bonifico"
#
# Richieste:
# 1) Per ogni ordine, usa match/case sullo STATO per determinare sconto applicato:
#    - "pending" o "processing" → sconto 0% (lock transazione non completata)
#    - "shipped" o "delivered" → sconto base 5%, modificato da tipo_cliente:
#      * se tipo_cliente == "vip": +5% aggiuntivo (totale 10%)
#      * se tipo_cliente == "newbie": -2% penalità (totale 3%)
#      * se tipo_cliente == "regular": rimane 5%
#    - "cancelled" → sconto 0% (ordine escluso da ricavo totale)
#
# 2) Calcola tasse in base al metodo_pagamento con match/case:
#    - "carta" → 2.5% sull'importo finale (dopo sconto)
#    - "paypal" → 3.5% (dopo sconto)
#    - "bonifico" → 1% (dopo sconto)
#
# 3) Aggrega in struttura dati per STATO:
#    {
#      "pending": {
#        "count": N,
#        "importo_lordo": X,    # Somma importi base (no sconto)
#        "tasse_totali": Y,
#        "ricavo_netto": Z,
#        "ordini": [lista di id_ordini]
#      },
#      "processing": {...},
#      "shipped": {...},
#      "delivered": {...},
#      "cancelled": {...}
#    }
#
# 4) Stampa rapporto formattato:
#    - Per ogni stato: count, importo lordo, tasse totali, ricavo netto
#    - Totale generale ricavo netto (escluso "cancelled")
#
# VINCOLI:
# - Usa match/case (non if/elif) per almeno stato e metodo_pagamento
# - NON usare try/except
# - Calcoli sconto e tasse vanno in funzioni separate (helper functions)
# - Lista ordini originale deve rimanere intatta
#

def client_discount(cliente: str) -> int:
    """Calcola lo sconto applicato alla categoria cliente"""
    match cliente:
        case "vip":
            return 5
        case "newbie":
            return -2
        case "regular":
            return 0
        case _:
            return 0

def determine_discount(stato: str, cliente:str) -> int:
    """Calcola sconto finale"""
    match stato:
        case 'pending' | 'processing':
            return 0
        case 'shipped' | 'delivered':
            return 5 + client_discount(cliente)
        case 'cancelled':
            return 0
        case _:
            return 0

def method_taxes(metodo: str) -> float:
    """Calcola tasse in base al metodo_pagamento"""
    match metodo:
        case 'carta':
            return 2.5
        case 'paypal':
            return 3.5
        case 'bonifico':
            return 1
        case _:
            return 0
        
def determine_taxes(stato: str, metodo: str) -> float:
    """Calcola tassa finale"""
    match stato:
        case 'pending' | 'processing':
            return 0
        case 'shipped' | 'delivered':
            return method_taxes(metodo)
        case 'cancelled':
            return 0
        case _:
            return 0
            
def aggrega_stato() -> dict:
    return {
        'count': 0,
        'importo_lordo': 0,
        'tasse_totali': 0,
        'ricavo_netto': 0,
        'IDs': [],
    }

def aggiorna_riepilogo(riepilogo: dict, importo: float, stato: str, sconto: float, tassa: float, n_id: str) -> None:
    """Aggiorna un movimento alla categoria specificata."""
    riepilogo[stato]['count'] += 1
    riepilogo[stato]['IDs'].append(n_id)
    riepilogo[stato]['importo_lordo'] += round(importo, 2)
    riepilogo[stato]['tasse_totali'] += tassa
    
    if stato == 'cancelled':
        riepilogo[stato]['ricavo_netto'] = 0
    else:
        riepilogo[stato]['ricavo_netto'] += (importo - sconto - tassa)

def formatta_rapporto(riepilogo):
    """Stampa rapporto formattato."""
    ricavo_totale = 0
    print("RAPPORTO ORDINI E-COMMERCE")
    for k, v in riepilogo.items():
        print(k.upper())
        if k != 'cancelled':
            ricavo_totale += v['ricavo_netto']
            print(
                f"\tNumero: {v['count']} | "
                f"Importo Lordo: €{v['importo_lordo']:.2f} | "
                f"Tasse: €{v['tasse_totali']:.2f} | "
                f"Ricavo Netto: €{v['ricavo_netto']:.2f}"
            )
        else:
            print(
                f"\tNumero: {v['count']} | "
                f"Importo lordo: €{v['importo_lordo']:.2f} | "
                f"(non conteggiato in ricavo)"
            )
    print(f"\n RICAVO TOTALE : {ricavo_totale:.2f}")

def main():

    # DATI DI INPUT
    ordini = [
        {"id": "ORD-001", "importo_base": 100, "stato": "delivered", "tipo_cliente": "vip", "metodo_pagamento": "carta"},
        {"id": "ORD-002", "importo_base": 75, "stato": "pending", "tipo_cliente": "regular", "metodo_pagamento": "paypal"},
        {"id": "ORD-003", "importo_base": 200, "stato": "shipped", "tipo_cliente": "newbie", "metodo_pagamento": "bonifico"},
        {"id": "ORD-004", "importo_base": 150, "stato": "delivered", "tipo_cliente": "vip", "metodo_pagamento": "carta"},
        {"id": "ORD-005", "importo_base": 50, "stato": "cancelled", "tipo_cliente": "regular", "metodo_pagamento": "paypal"},
        {"id": "ORD-006", "importo_base": 300, "stato": "processing", "tipo_cliente": "regular", "metodo_pagamento": "bonifico"},
        {"id": "ORD-007", "importo_base": 120, "stato": "delivered", "tipo_cliente": "newbie", "metodo_pagamento": "paypal"},
        {"id": "ORD-008", "importo_base": 90, "stato": "shipped", "tipo_cliente": "vip", "metodo_pagamento": "carta"},
    ]

    # - stati: "pending", "processing", "shipped", "delivered", "cancelled"
    riepilogo = {
        'pending' : aggrega_stato(),
        'processing' : aggrega_stato(),
        'shipped' : aggrega_stato(),
        'delivered' : aggrega_stato(),
        'cancelled' : aggrega_stato(),
    }

    for ordine in ordini:
        stato = ordine['stato']
        importo = float(ordine['importo_base'])
        cliente = ordine['tipo_cliente']
        metodo = ordine['metodo_pagamento']
        n_id = ordine['id']
        
        pct_sconto = determine_discount(stato, cliente)

        sconto = importo * (pct_sconto / 100)
        tassa = importo * ((100 - pct_sconto) / 100) * (determine_taxes(stato, metodo) / 100)

        aggiorna_riepilogo(riepilogo, importo, stato, sconto, tassa, n_id)
    
    formatta_rapporto(riepilogo)

if __name__ == "__main__":
    main()


# OUTPUT ATTESO (approssimativo - valori aggregati):
#
# RAPPORTO ORDINI E-COMMERCE
# ═══════════════════════════════════════════════════════════════════
#
# PENDING:
#   Ordini: 1 | Importo lordo: €75.00 | Tasse: €0.00 | Ricavo netto: €75.00
#
# PROCESSING:
#   Ordini: 1 | Importo lordo: €300.00 | Tasse: €0.00 | Ricavo netto: €300.00
#
# SHIPPED:
#   Ordini: 2 | Importo lordo: €410.00 | Tasse: €20.77 | Ricavo netto: €389.23
#
# DELIVERED:
#   Ordini: 3 | Importo lordo: €470.00 | Tasse: €21.89 | Ricavo netto: €448.11
#
# CANCELLED:
#   Ordini: 1 | Importo lordo: €50.00 | (non conteggiato in ricavo totale)
#
# ═══════════════════════════════════════════════════════════════════
# RICAVO NETTO TOTALE: €812.34
#
```

---

## 05_ordini2

```python
#
# ESERCIZIO: Gestione Ordini E-Commerce
#
# Un negozio online elabora ordini. Ogni ordine contiene:
# - id_ordine: codice univoco
# - importo_base: prezzo senza tasse
# - stato: "pending", "processing", "shipped", "delivered", "cancelled"
# - tipo_cliente: "regular", "vip", "newbie"
# - metodo_pagamento: "carta", "paypal", "bonifico"
#
# Richieste:
# 1) Per ogni ordine, usa match/case sullo STATO per determinare sconto applicato:
#    - "pending" o "processing" → sconto 0% (lock transazione non completata)
#    - "shipped" o "delivered" → sconto base 5%, modificato da tipo_cliente:
#      * se tipo_cliente == "vip": +5% aggiuntivo (totale 10%)
#      * se tipo_cliente == "newbie": -2% penalità (totale 3%)
#      * se tipo_cliente == "regular": rimane 5%
#    - "cancelled" → sconto 0% (ordine escluso da ricavo totale)
#
# 2) Calcola tasse in base al metodo_pagamento con match/case:
#    - "carta" → 2.5% sull'importo finale (dopo sconto)
#    - "paypal" → 3.5% (dopo sconto)
#    - "bonifico" → 1% (dopo sconto)
#
# 3) Aggrega in struttura dati per STATO:
#    {
#      "pending": {
#        "count": N,
#        "importo_lordo": X,    # Somma importi base (no sconto)
#        "tasse_totali": Y,
#        "ricavo_netto": Z,
#        "ordini": [lista di id_ordini]
#      },
#      "processing": {...},
#      "shipped": {...},
#      "delivered": {...},
#      "cancelled": {...}
#    }
#
# 4) Stampa rapporto formattato:
#    - Per ogni stato: count, importo lordo, tasse totali, ricavo netto
#    - Totale generale ricavo netto (escluso "cancelled")
#
# VINCOLI:
# - Usa match/case (non if/elif) per almeno stato e metodo_pagamento
# - NON usare try/except
# - Calcoli sconto e tasse vanno in funzioni separate (helper functions)
# - Lista ordini originale deve rimanere intatta
#

def client_discount(cliente: str) -> int:
    """Calcola lo sconto applicato alla categoria cliente"""
    match cliente:
        case "vip":
            return 5
        case "newbie":
            return -2
        case "regular":
            return 0
        case _:
            return 0

def method_taxes(metodo: str) -> float:
    """Calcola tasse in base al metodo_pagamento"""
    match metodo:
        case 'carta':
            return 2.5
        case 'paypal':
            return 3.5
        case 'bonifico':
            return 1
        case _:
            return 0
        
def elabora_ordine(stato: str, cliente: str, metodo: str) -> tuple:
    """Ritorna (sconto%, tasse%) in base a stato e cliente."""
    match stato:
        case 'pending' | 'processing' | 'cancelled':
            return (0, 0)
        case 'shipped' | 'delivered':
            sconto_cliente = 5 + client_discount(cliente)
            tasse = method_taxes(metodo)
            return (sconto_cliente, tasse)
        case _:
            return (0, 0)
            
def aggrega_stato() -> dict:
    return {
        'count': 0,
        'importo_lordo': 0,
        'tasse_totali': 0,
        'ricavo_netto': 0,
        'IDs': [],
    }

def aggiorna_riepilogo(riepilogo: dict, importo: float, stato: str, sconto_eur: float, tassa_eur: float, n_id: str) -> None:
    """Aggiorna un movimento alla categoria specificata."""
    riepilogo[stato]['count'] += 1
    riepilogo[stato]['IDs'].append(n_id)
    riepilogo[stato]['importo_lordo'] += round(importo, 2)
    riepilogo[stato]['tasse_totali'] += round(tassa_eur, 2)
    
    if stato != 'cancelled':
        riepilogo[stato]['ricavo_netto'] += round(importo - sconto_eur - tassa_eur, 2)

def formatta_rapporto(riepilogo):
    """Stampa rapporto formattato."""
    ricavo_totale = 0
    print("RAPPORTO ORDINI E-COMMERCE")
    for k, v in riepilogo.items():
        print(k.upper())
        if k != 'cancelled':
            ricavo_totale += v['ricavo_netto']
            print(
                f"\tNumero: {v['count']} | "
                f"Importo Lordo: €{v['importo_lordo']:.2f} | "
                f"Tasse: €{v['tasse_totali']:.2f} | "
                f"Ricavo Netto: €{v['ricavo_netto']:.2f}"
            )
        else:
            print(
                f"\tNumero: {v['count']} | "
                f"Importo lordo: €{v['importo_lordo']:.2f} | "
                f"(non conteggiato in ricavo)"
            )
    print(f"\n RICAVO TOTALE: {ricavo_totale:.2f}")

def main():

    # DATI DI INPUT
    ordini = [
        {"id": "ORD-001", "importo_base": 100, "stato": "delivered", "tipo_cliente": "vip", "metodo_pagamento": "carta"},
        {"id": "ORD-002", "importo_base": 75, "stato": "pending", "tipo_cliente": "regular", "metodo_pagamento": "paypal"},
        {"id": "ORD-003", "importo_base": 200, "stato": "shipped", "tipo_cliente": "newbie", "metodo_pagamento": "bonifico"},
        {"id": "ORD-004", "importo_base": 150, "stato": "delivered", "tipo_cliente": "vip", "metodo_pagamento": "carta"},
        {"id": "ORD-005", "importo_base": 50, "stato": "cancelled", "tipo_cliente": "regular", "metodo_pagamento": "paypal"},
        {"id": "ORD-006", "importo_base": 300, "stato": "processing", "tipo_cliente": "regular", "metodo_pagamento": "bonifico"},
        {"id": "ORD-007", "importo_base": 120, "stato": "delivered", "tipo_cliente": "newbie", "metodo_pagamento": "paypal"},
        {"id": "ORD-008", "importo_base": 90, "stato": "shipped", "tipo_cliente": "vip", "metodo_pagamento": "carta"},
    ]

    # - stati: "pending", "processing", "shipped", "delivered", "cancelled"
    riepilogo = {
        'pending' : aggrega_stato(),
        'processing' : aggrega_stato(),
        'shipped' : aggrega_stato(),
        'delivered' : aggrega_stato(),
        'cancelled' : aggrega_stato(),
    }

    for ordine in ordini:
        stato = ordine['stato']
        importo = float(ordine['importo_base'])
        cliente = ordine['tipo_cliente']
        metodo = ordine['metodo_pagamento']
        n_id = ordine['id']
        
        sconto_pct, tassa_pct= elabora_ordine(stato, cliente, metodo)

        sconto_eur = importo * (sconto_pct / 100)
        tassa_eur = importo * ((100 - sconto_pct) / 100) * (tassa_pct / 100)

        aggiorna_riepilogo(riepilogo, importo, stato, sconto_eur, tassa_eur, n_id)
    
    formatta_rapporto(riepilogo)

if __name__ == "__main__":
    main()


# OUTPUT ATTESO (approssimativo - valori aggregati):
#
# RAPPORTO ORDINI E-COMMERCE
# ═══════════════════════════════════════════════════════════════════
#
# PENDING:
#   Ordini: 1 | Importo lordo: €75.00 | Tasse: €0.00 | Ricavo netto: €75.00
#
# PROCESSING:
#   Ordini: 1 | Importo lordo: €300.00 | Tasse: €0.00 | Ricavo netto: €300.00
#
# SHIPPED:
#   Ordini: 2 | Importo lordo: €290.00 | Tasse: €3.96 | Ricavo netto: €271.03
#
# DELIVERED:
#   Ordini: 3 | Importo lordo: €370.00 | Tasse: €9.70 | Ricavo netto: €331.70
#
# CANCELLED:
#   Ordini: 1 | Importo lordo: €50.00 | (non conteggiato in ricavo totale)
#
# ═══════════════════════════════════════════════════════════════════
# RICAVO NETTO TOTALE: €812.34
#
```

---

## 06_logistica

```python
# ==============================================================================
# DESCRIZIONE DEL PROBLEMA
# Un centro logistico internazionale deve elaborare il report giornaliero delle 
# spedizioni. L'obiettivo è ripartire i costi totali basandosi sulla 
# destinazione geografica e sulla categoria di peso del pacco.
#
# STRUTTURA DATI INPUT:
# Una lista di dizionari denominata 'spedizioni_in_entrata'. Ogni elemento contiene:
# - "id_ordine": stringa univoca
# - "dest": stringa (codice nazione: "IT", "FR", "DE", "US", "UK", "CN")
# - "kg": float (peso del pacco)
# - "fragile": booleano
#
# RICHIESTE NUMERICHE E LOGICHE:
# 1. Suddividere le nazioni in 3 Zone: "Nazionale" (IT), "Europa" (FR, DE), 
#    "Extra-UE" (US, UK, CN).
# 2. Definire la Categoria Peso: "Small" (fino a 2kg inclusi), "Medium" (sopra 2 
#    fino a 10kg inclusi), "Large" (sopra 10kg).
# 3. Calcolare il costo per ogni singola spedizione seguendo queste tariffe base:
#    - Nazionale: 5.0€ base + 1.5€ per ogni kg.
#    - Europa: 12.0€ base + 2.5€ per ogni kg.
#    - Extra-UE: 25.0€ base + 5.0€ per ogni kg.
# 4. Applicare un sovrapprezzo fisso di 10.0€ se il pacco è "fragile".
# 5. Aggregare i costi totali in un dizionario annidato che organizza i dati 
#    per Zona e, all'interno, per Categoria Peso.
#
# VINCOLI TECNICI OBBLIGATORI:
# - Utilizzare lo structural pattern matching (match/case) per gestire la 
#   logica di assegnazione della Zona Geografica.
# - NON modificare i dati originali nella lista 'spedizioni_in_entrata'.
# - NO blocchi try/except.
#
# STRUTTURA OUTPUT ATTESO:
# Un dizionario finale 'report_costi' con questa gerarchia:
# {
#   "Nazionale": {"Small": totale, "Medium": totale, "Large": totale},
#   "Europa": { ... },
#   "Extra-UE": { ... }
# }
# ==============================================================================

# DATI DI INPUT
spedizioni_in_entrata = [
    {"id_ordine": "A001", "dest": "IT", "kg": 1.5, "fragile": False},
    {"id_ordine": "A002", "dest": "IT", "kg": 12.0, "fragile": True},
    {"id_ordine": "A003", "dest": "FR", "kg": 5.0, "fragile": False},
    {"id_ordine": "A004", "dest": "DE", "kg": 0.8, "fragile": False},
    {"id_ordine": "A005", "dest": "US", "kg": 15.5, "fragile": True},
    {"id_ordine": "A006", "dest": "UK", "kg": 3.2, "fragile": False},
    {"id_ordine": "A007", "dest": "CN", "kg": 0.5, "fragile": False},
    {"id_ordine": "A008", "dest": "IT", "kg": 4.5, "fragile": False},
    {"id_ordine": "A009", "dest": "DE", "kg": 11.0, "fragile": True}
]

# SVOLGIMENTO:

# Definizioni costanti per dizionario di riepilogo
# COSTANTI: Grandezze pacchi
SMALL = 'Small'
MEDIUM = 'Medium'
LARGE = 'Large'
# COSTANTI: Zone di destinazione
LOCAL = 'Nazionale'
CONTINENTAL = 'Europa'
INTERCONTINENTAL = 'Extra-UE'

# Creo set per destinazioni EUROPEAN-UNION (mia discrezione), tutto il resto è "Nazionale" o "Extra-UE"
EUROPEAN_UNION = {
    "AT",  # Austria
    "BE",  # Belgio
    "BG",  # Bulgaria
    "HR",  # Croazia
    "CY",  # Cipro
    "CZ",  # Repubblica Ceca
    "DK",  # Danimarca
    "EE",  # Estonia
    "FI",  # Finlandia
    "FR",  # Francia
    "DE",  # Germania
    "GR",  # Grecia
    "HU",  # Ungheria
    "IE",  # Irlanda
    "IT",  # Italia
    "LV",  # Lettonia
    "LT",  # Lituania
    "LU",  # Lussemburgo
    "MT",  # Malta
    "NL",  # Paesi Bassi
    "PL",  # Polonia
    "PT",  # Portogallo
    "RO",  # Romania
    "SK",  # Slovacchia
    "SI",  # Slovenia
    "ES",  # Spagna
    "SE",  # Svezia
}

def define_zone(destinazione: str) -> str:
    """
    Determina la macro-zona geografica della destinazione finale
    a partire dal codice paese ISO 3166-1 alpha-2.

    Args:
        destinazione (dict): Dizionario contenente la chiave 'dest'
            con il codice paese a due caratteri.

    Returns:
        str: Macro-zona geografica ("Nazionale", "Europa", "Extra-UE")
            oppure "ERROR" se il codice non è valido.
    """
    # Normalizzazione del codice paese (rimozione spazi, uppercase)
    destinazione = destinazione.strip().upper()

    # Validazione di base del codice ISO (2 lettere alfabetiche)
    if len(destinazione) == 2 and destinazione.isalpha():
        match destinazione:
            case "IT":
                return LOCAL
            case _ if destinazione in EUROPEAN_UNION:
                return CONTINENTAL
            case _:
                return INTERCONTINENTAL
    else:
        # TODO: Implementare gestione errori formale (attualmente non supportata).
        # non ho ancora affrontato i blocchi try/except.
        return "ERROR_dz"
    
def define_weight(peso: float) -> str:
    """
    Determina la categoria di peso di una spedizione in base al valore
    espresso in chilogrammi.

    Le categorie di peso sono:
    - "Small"  → peso ≤ 2 kg
    - "Medium" → 2 kg < peso ≤ 10 kg
    - "Large"  → peso > 10 kg

    Args:
        spedizione (dict): Dizionario contenente la chiave 'kg'
            con il peso della spedizione espresso come stringa.

    Returns:
        str: Categoria di peso assegnata ("Small", "Medium", "Large")
             oppure "ERROR" se il valore del peso non è valido.
    """
    # gestione peso negativo
    if peso < 0:
        # TODO: Implementare gestione errori formale (attualmente non supportata).
        # non ho ancora affrontato i blocchi try/except.
        return "ERROR_p"

    # Classificazione per fasce di peso
    if peso <= 2:
        return SMALL
    elif peso <= 10:
        return MEDIUM
    else:
        return LARGE
    
def calculate_shipment_cost(zona: str, peso: float, fragile: bool) -> float:
    """
    Determina il costo della spedizione a seconda della zona di destinazione
    
    Args:
        spedizione (dict): Dizionario contenente tutte le informazioni
        relative alla spedizione

    Returns:
        float: costo per ogni singola spedizione
    """

    surplus = 10 if fragile else 0

    if zona == LOCAL:
        return surplus + 5 + peso * 1.5
    elif zona == CONTINENTAL:
        return surplus + 12 + peso * 2.5
    else:
        return surplus + 25 + peso * 5

def build_weight() -> dict:
    """Inizializza un dizionario per le categorie di peso.

    Crea una struttura dati predefinita per mappare le dimensioni del pacco
    a valori numerici (es. costi o pesi), impostandoli a zero.

    Returns:
        dict: Un dizionario con chiavi SMALL, MEDIUM, LARGE e valori 0.
    """
    return {
        SMALL: 0,
        MEDIUM: 0,
        LARGE: 0,
    }

def build_zone() -> dict:
    """Costruisce la struttura gerarchica delle zone di spedizione.

    Per ogni zona geografica definita (Locale, Continentale, Intercontinentale),
    genera un sotto-dizionario contenente le categorie di peso tramite
    la funzione build_weight().

    Returns:
        dict: Un dizionario nidificato dove ogni chiave di zona punta a una
            mappa di pesi e valori.
    """
    return {
        LOCAL: build_weight(),
        CONTINENTAL: build_weight(),
        INTERCONTINENTAL: build_weight(),
    }

def main():
    riepilogo = build_zone()

    for spedizione in spedizioni_in_entrata:
        
        peso = spedizione['kg']
        fragile = spedizione['fragile']
        zona = define_zone(spedizione["dest"])
        costo = calculate_shipment_cost(zona, peso, fragile)
        grandezza = define_weight(peso)

        riepilogo[zona][grandezza] += costo

    print(riepilogo)

main()

# OUTPUT ATTESO (Valori indicativi calcolati)
# Il risultato finale dovrà essere un dizionario simile a questo:
# {
#    'Nazionale': {'Small': 7.25, 'Medium': 11.75, 'Large': 33.0},
#    'Europa': {'Small': 14.0, 'Medium': 24.5, 'Large': 49.5},
#    'Extra-UE': {'Small': 27.5, 'Medium': 41.0, 'Large': 112.5}
# }
```

---

