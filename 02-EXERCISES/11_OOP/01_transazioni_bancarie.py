# ============================================================
# ESERCIZIO: Creare e utilizzare una classe in Python
# Argomento: Classi (livello principiante)
# ============================================================
#
# Obiettivo:
# Creare una classe che rappresenti un conto bancario.
#
# ------------------------------------------------------------
# TESTO DELL'ESERCIZIO
# ------------------------------------------------------------
#
# 1) Crea una classe chiamata ContoBancario.
#
# 2) La classe deve avere:
#    - un attributo "intestatario" (stringa)
#    - un attributo "saldo" (numero, valore iniziale scelto dall'utente)
#
# 3) Implementa i seguenti metodi:
#
#    - deposita(importo)
#        Aggiunge l'importo al saldo.
#        Stampa un messaggio con il nuovo saldo.
#
#    - preleva(importo)
#        Se il saldo è sufficiente:
#            sottrae l'importo dal saldo
#            stampa il nuovo saldo
#        Altrimenti:
#            stampa un messaggio di errore (fondi insufficienti)
#
#    - mostra_saldo()
#        Stampa il saldo attuale dell'intestatario.
#
# 4) Nel programma principale:
#    - Crea almeno un oggetto della classe ContoBancario.
#    - Prova a fare:
#         * un deposito
#         * un prelievo valido
#         * un prelievo non valido
#    - Mostra il saldo finale.
#
# ------------------------------------------------------------
# BONUS (facoltativo)
# ------------------------------------------------------------
#
# - Impedisci il deposito o il prelievo di importi negativi.
# - Aggiungi un metodo __str__ per stampare le informazioni
#   del conto in modo leggibile.
#
# ------------------------------------------------------------
# Obiettivo didattico:
# - Capire cos'è una classe
# - Usare il metodo __init__
# - Utilizzare self
# - Creare oggetti (istanze)
# - Chiamare metodi su un oggetto
# ============================================================

class ContoBancario:
    
    def __init__(self, intestatario: str, saldo: float):
        self.intestatario = intestatario
        self.saldo = saldo

    def deposita(self, importo: float):
        if importo <= 0:
            print("Errore: l'importo deve essere positivo.")
            return # dentro un metodo (una funzione) non si usa break
        self.saldo += importo
        print(f"DEPOSITO AUTORIZZATO: Il saldo attuale è: {self.saldo}")
        return self.saldo
    
    def preleva(self, importo: float):
        if importo <= 0:
            print("Errore: l'importo deve essere positivo.")        
        elif self.saldo < importo:
            print(f"ERRORE: fondi insufficienti")
        else:
            self.saldo = self.saldo - importo
            print(f"PRELIEVO AUTORIZZATO: Il saldo attuale è: {self.saldo}")
            return self.saldo
        
    def mostra_saldo(self):
        print(f"Il saldo attuale è: {self.saldo}")

    def __str__(self):
        return f"Conto intestato a {self.intestatario} - Saldo: {self.saldo}"

def main():
    mio_conto = ContoBancario('Johnny', 1_000)
    print(mio_conto)
    mio_conto.deposita(100)
    mio_conto.preleva(970)
    mio_conto.preleva(200)
    mio_conto.mostra_saldo()

main()  