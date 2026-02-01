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
            