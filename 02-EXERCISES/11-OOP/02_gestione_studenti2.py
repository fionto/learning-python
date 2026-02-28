# ============================================================
# SOLUZIONE: Sistema Gestione Studente (tutto gestito dal chiamante)
# ============================================================

class Studente:

    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.voti = []
        self.promosso = None  # True/False/None

    def aggiungi_voto(self, voto):
        """Aggiunge un voto valido. Restituisce True se valido, False altrimenti."""
        if 0 <= voto <= 30:
            self.voti.append(voto)
            return True
        return False

    def calcola_media(self):
        """Restituisce la media dei voti o None se non ci sono voti."""
        if self.voti:
            return sum(self.voti) / len(self.voti)
        return None

    def voto_massimo(self):
        return max(self.voti) if self.voti else None

    def voto_minimo(self):
        return min(self.voti) if self.voti else None

    def aggiorna_valutazione(self):
        """Aggiorna l'attributo promosso basandosi sulla media."""
        media = self.calcola_media()
        if media is None:
            self.promosso = None
        else:
            self.promosso = media >= 18

    def __str__(self):
        return f"STUDENTE: {self.nome} - MATRICOLA: {self.matricola}"


# ============================================================
# PROGRAMMA PRINCIPALE
# ============================================================

def main():
    # Creo tre studenti
    studenti = [
        Studente("Jimmy", "424090"),
        Studente("Zachariah", "424091"),
        Studente("D'Brickshaw", "424092")
    ]

    # Lista di voti da aggiungere a ciascun studente
    voti_studenti = [
        [18, 24, 22, 35],  # Jimmy
        [12, 15, 18],      # Zachariah
        [30, 28, 27, 25]   # D'Brickshaw
    ]

    # Ciclo usando enumerate su studenti
    for i, studente in enumerate(studenti):
        print(f"\n{studente}") # Ricorda, la variabile è l'oggetto Studente. In pratica uso __str__()

        # Prendo la lista dei voti corrispondente
        voti = voti_studenti[i]

        # Aggiungo voti
        for voto in voti:
            if not studente.aggiungi_voto(voto):
                print(f"Voto {voto} non valido! Deve essere tra 0 e 30.")

        # Aggiorno valutazione
        studente.aggiorna_valutazione()

        # Stampo informazioni
        num_voti = len(studente.voti)
        media = studente.calcola_media()
        voto_max = studente.voto_massimo()
        voto_min = studente.voto_minimo()

        print(f"Numero voti inseriti: {num_voti}")
        print(f"Media: {media:.2f}" if media is not None else "Nessun voto disponibile")
        print(f"Voto massimo: {voto_max}" if voto_max is not None else "Nessun voto")
        print(f"Voto minimo: {voto_min}" if voto_min is not None else "Nessun voto")

        # Stampo valutazione
        if studente.promosso is None:
            print("Impossibile valutare lo studente senza voti validi.")
        elif studente.promosso:
            print("Lo studente è promosso.")
        else:
            print("Lo studente è bocciato.")


main()