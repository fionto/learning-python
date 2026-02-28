class Studente:

    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola

    def __str__(self):
        return f"STUDENTE: {self.nome} - MATRICOLA: {self.matricola}"
    

class Registro:
    
    def __init__(self):
        self.studenti = {}
    
    def inserisci_studente(self, studente: Studente):
        self.studenti[studente.matricola] = studente

    def __str__(self):
        return f"STUDENTI: {self.studenti.keys()}"

def main():
    studente_uno = Studente('Jimmy', '424090')
    studente_due = Studente("Zachariah", "424091")
    studente_tre = Studente("D'Brickshaw", "424092")

    registro = Registro()

    registro.inserisci_studente(studente_uno)
    registro.inserisci_studente(studente_due)
    registro.inserisci_studente(studente_tre)

    print(registro)

main()  