# ============================================================
# ESERCIZIO: Sistema Gestione Studente
# ============================================================
# Obiettivo:
# Creare una classe che rappresenti uno studente e la gestione
# dei suoi voti.
# ------------------------------------------------------------
# TESTO DELL'ESERCIZIO
# ------------------------------------------------------------
# 1) Crea una classe chiamata Studente.
#
# 2) La classe deve avere:
#    - un attributo "nome" (stringa)
#    - un attributo "matricola" (stringa o numero)
#    - un attributo "voti" (lista inizialmente vuota)
#
# 3) Implementa i seguenti metodi:
#
#    - aggiungi_voto(voto)
#        Aggiunge un voto alla lista.
#        Il voto deve essere tra 0 e 30.
#        Se non è valido, stampa un messaggio di errore.
#
#    - media()
#        Restituisce la media dei voti.
#        Se non ci sono voti, stampa un messaggio appropriato.
#
#    - voto_massimo()
#        Restituisce il voto più alto ottenuto.
#
#    - voto_minimo()
#        Restituisce il voto più basso ottenuto.
#
#    - mostra_info()
#        Mostra:
#            Nome
#            Matricola
#            Numero di voti inseriti
#            Media attuale
#
# 4) Nel programma principale:
#    - Crea uno studente.
#    - Aggiungi almeno 4 voti (incluso uno non valido).
#    - Mostra le informazioni complete.
#
# ------------------------------------------------------------
# BONUS (facoltativo)
# ------------------------------------------------------------
#
# - Aggiungi un metodo che dica se lo studente è:
#       "Promosso" (media >= 18)
#       "Bocciato" (media < 18)
#
# - Implementa il metodo __str__ per stampare lo studente
#   in modo leggibile con print().
#
# ------------------------------------------------------------
# Obiettivo didattico:
# - Usare liste dentro una classe
# - Gestire controlli sui dati
# - Calcolare media con len() e sum()
# - Restituire valori con return
# - Rafforzare la logica nei metodi
# ============================================================

class Studente:

    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.voti = []
    
    def aggiungi_voto(self,voto):
        if 0 <= voto <= 30:
            self.voti.append(voto)
        else:
            print("ERRORE: Il voto deve essere compreso tra 0 e 30")

    def calcola_media(self):
        if self.voti:
            return sum(self.voti) / len(self.voti)
        else:
            print("ATTENZIONE: non sono presenti voti nel database")
            return None
    
    def voto_massimo(self):
        if self.voti:
            return max(self.voti)
        else:
            print("ATTENZIONE: non sono presenti voti nel database")
            return None
            
    def voto_minimo(self):
        if self.voti:
            return min(self.voti)
        else:
            print("ATTENZIONE: non sono presenti voti nel database")
            return None
            
    def mostra_info(self):
        print(f"\nNome: {self.nome}")
        print(f"Matricola: {self.matricola}")
        print(f"Numero voti inseriti: {len(self.voti)}")

        media = self.calcola_media()
        if media is not None:
            print(f"Media: {media}\n")
        else:
            print("Nessun voto disponibile.\n")
    
    def valuta_studente(self):
        media = self.calcola_media()
        
        if not media:
            print("ERRORE: Impossibile calcolare media senza voti validi")
            return
        
        if media < 18:
            print("Lo studente è bocciato.")
        else:
            print("Lo studente è promosso.")
        
    def __str__(self):
        return f"STUDENTE: {self.nome} - MATRICOLA: {self.matricola}"

def main():
    studente_uno = Studente('Jimmy', '424090')
    
    studente_uno.mostra_info()
    
    studente_uno.aggiungi_voto(18)
    studente_uno.aggiungi_voto(24)
    studente_uno.aggiungi_voto(22)

    print(f"Il voto massimo è {studente_uno.voto_massimo()}")
    print(f"Il voto minimo è {studente_uno.voto_minimo()}")

    studente_uno.mostra_info()

main()  