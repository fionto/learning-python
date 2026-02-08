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