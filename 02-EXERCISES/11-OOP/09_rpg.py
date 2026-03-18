# ==============================================================================
# ESERCIZIO PRATICO: SISTEMA DI GESTIONE PERSONAGGI RPG
# ==============================================================================
#
# Creare un sistema software per gestire personaggi di un gioco di ruolo,
# applicando i concetti di Classi, Ereditarietà e Composizione appresi,
# ma prestando attenzione alla qualità del codice e alla robustezza.
#
# 1. CLASSE BASE: Personaggio
#    - Attributi: nome (str), punti_vita (int), livello (int).
#    - Metodi:
#      * descrivi(): Stampa le informazioni principali del personaggio.
#      * subisci_danno(quantita): Riduce i punti_vita. Non possono scendere sotto 0.
#      * e_vivo(): Restituisce True se i punti_vita sono > 0.
#
# 2. CLASSE DI COMPOSIZIONE: Inventario
#    - Questa classe non eredita da nulla, gestisce solo gli oggetti.
#    - Attributi: oggetti (lista), capacita_massima (int).
#    - Metodi:
#      * aggiungi(oggetto): Aggiunge un oggetto alla lista. 
#        - Controlla che l'inventario non sia pieno.
#        - Restituisce True se successo, False se pieno.
#      * rimuovi(oggetto): Rimuove un oggetto dalla lista.
#      * mostra(): Stampa l'elenco degli oggetti posseduti.
#    - ⚠️ ATTENZIONE: Ogni istanza di Personaggio che possiede un Inventario 
#      deve avere il PROPRIO inventario indipendente. Creare due personaggi 
#      non deve far condividere loro gli stessi oggetti di default.
#
# 3. CLASSE DERIVATA: Guerriero
#    - Eredita dalla classe Personaggio.
#    - Attributo speciale: forza (int).
#    - Durante l'inizializzazione, deve creare internamente un'istanza 
#      della classe Inventario.
#    - ⚠️ ATTENZIONE ALLA NOMENCLATURA: Scegli i nomi degli attributi in modo 
#      che sia chiaro distinguere l'oggetto "Inventario" dalla lista interna 
#      degli "oggetti". Evita confusione nella lettura del codice (es. evitare 
#      catene di accesso ambigue).
#    - Metodo speciale: attacco_pesante(nemico). Usa la forza per calcolare 
#      il danno e chiama il metodo subisci_danno del nemico.
#
# 4. ESECUZIONE SCRIPT (Main)
#    - Lo script deve essere eseguibile direttamente, ma importabile senza 
#      eseguire automaticamente il codice di test.
#    - Crea due guerrieri diversi.
#    - Simula una battaglia: uno attacca l'altro fino a quando uno non cade.
#    - Gestisci gli inventari: dai equipaggiamento ai guerrieri durante la lotta.
#    - Stampa lo stato finale dei personaggi.
#
# REQUISITI DI QUALITÀ (CODE REVIEW CHECKLIST):
# - [ ] Documentazione: Ogni classe e metodo pubblico deve avere una docstring.
# - [ ] Sicurezza Dati: I punti vita non devono mai diventare negativi.
# - [ ] Indipendenza: Modificare l'inventario del Guerriero A non deve 
#       influenzare l'inventario del Guerriero B (anche se creati senza argomenti).
# - [ ] Leggibilità: I nomi delle variabili devono descrivere il contenuto 
#       (evita nomi generici come 'lista' o 'dati').
# - [ ] Incapsulamento: Preferisci usare metodi per modificare lo stato 
#       dell'inventario piuttosto che accedere direttamente alla lista interna.
# ==============================================================================

class Personaggio:
    """
    Rappresenta un personaggio generico nel gioco.

    Questa classe funge da base per personaggi giocanti e NPC. Gestisce gli attributi
    vitali (nome, livello, punti vita) e le operazioni fondamentali di sopravvivenza.

    Attributes:
        nome (str): Il nome del personaggio.
        livello (int): Il livello attuale del personaggio.
        punti_vita (int): I punti vita attuali (range valido: 0-1000).
    """

    def __init__(self, nome: str, punti_vita: int, livello: int):
        """
        Inizializza un nuovo personaggio.

        Args:
            nome (str): Il nome del personaggio.
            punti_vita (int): I punti vita iniziali.
            livello (int): Il livello iniziale del personaggio.

        Raises:
            ValueError: Se punti_vita non è compreso tra 0 e 1000.
        """
        self.nome = nome
        self.livello = livello
        # Chiamo un metodo privato (_set_punti_vita) invece di assegnare direttamente
        # self.punti_vita = punti_vita. Perché? Perché voglio che la validazione
        # avvenga anche in fase di creazione. Se tra 6 mesi modifico i range nel setter,
        # l'__init__ sarà automaticamente aggiornato senza toccare questo codice.
        self._set_punti_vita(punti_vita)

    def _set_punti_vita(self, valore: int):
        """
        Imposta i punti vita applicando le regole di validazione.

        Questo metodo è privato (prefisso underscore) perché è un dettaglio
        implementativo interno. Non dovrebbe essere chiamato dall'esterno della classe.

        Args:
            valore (int): Il nuovo valore dei punti vita.

        Raises:
            ValueError: Se il valore non è compreso tra 0 e 1000.
        """
        # Scelgo di lanciare un errore invece di correggere silenziosamente (es. max/min).
        # Perché? Perché se arrivo qui con un valore sbagliato, voglio saperlo subito
        # durante lo sviluppo. Un errore blocca il programma e mi avvisa del bug.
        # Correggere in silenzio nasconderebbe errori di logica altrove nel codice.
        if not (0 <= valore <= 1000):
            raise ValueError(f"PV {valore} non valido. Range ammesso: 0-1000.")
        
        self.punti_vita = valore

    def descrivi(self):
        """
        Stampa le informazioni principali del personaggio a video.

        Output include nome (in formato titolo), livello e punti vita attuali.
        Utilizzato principalmente per debug o interfacce testuali semplici.
        """
        # Questo metodo stampa direttamente. In un progetto reale con interfaccia grafica,
        # sarebbe meglio restituire una stringa o un dizionario. Per ora va bene così,
        # ma se dovessi separare la logica dalla presentazione, refattorizzare qui.
        print(f"Nome personaggio: {self.nome.title()}")
        print(f"Livello: {self.livello}")
        print(f"Punti vita: {self.punti_vita}")

    def subisci_danno(self, quantita: int):
        """
        Riduce i punti vita del personaggio di una quantità specifica.

        I punti vita non possono scendere sotto zero. Se il danno è negativo,
        l'operazione viene annullata (non sono previste cure tramite questo metodo).

        Args:
            quantita (int): La quantità di danno da subire. Deve essere >= 0.

        Returns:
            bool: True se il danno è stato applicato, False se la quantita era negativa.
        """
        if quantita < 0:
            return False

        # Calcolo il nuovo valore PRIMA di passare al setter.
        # Uso max(0, ...) per garantire che non passi mai valori negativi al setter.
        # Il setter si occupa di validare il range, io mi occupo della logica di gioco
        # (il danno non può curare).
        nuovo_valore = max(0, self.punti_vita - quantita)
        self._set_punti_vita(nuovo_valore)
        return True

    def e_vivo(self):
        """
        Verifica se il personaggio è ancora in vita.

        Returns:
            bool: True se punti_vita > 0, False altrimenti.
        """
        # Restituisco direttamente l'espressione booleana.
        # Evito 'if self.punti_vita > 0: return True else: return False'
        # perché è ridondante. Il confronto restituisce già un bool.
        return self.punti_vita > 0

class Inventario:

    def __init__(self, capacita_massima=3, oggetti_iniziali=None):
        self.capacità = capacita_massima
        if oggetti_iniziali is None:
            self.oggetti = []
        else:
            self.oggetti = oggetti_iniziali
        
    def aggiungi_oggetto(self, oggetto):
        if len(self.oggetti) == self.capacità:
            return False
        else:
            self.oggetti.append(oggetto)
            return True
        
    def rimuovi_oggetto(self, oggetto):
        if oggetto not in self.oggetti:
            return False
        else:
            self.oggetti.remove(oggetto)
            return True
        
    def mostra_inventario(self):
        for oggetto in self.oggetti:
            print(f" -{oggetto}")


class Guerriero(Personaggio):

    def __init__(self, nome: str, punti_vita: int, livello: int, forza: int):
        super().__init__(nome, punti_vita, livello)
        self.forza = forza
        self.gestione_inventario = Inventario()

    def descrivi_pg(self):
        print(f"Nome Guerriero: {self.nome.title()}")
        print(f"Livello: {self.livello}")
        print(f"Forza: {self.forza}")
        print(f"Punti vita: {self.punti_vita}")

    def attacco_pesante(self, nemico):
        nemico.subisci_danno(self.forza)


def main():
    ettore = Personaggio("Ettore", 120, 5)
    ettore.descrivi()

    achille = Guerriero("Achille", 150, 7, 30)
    achille.descrivi()

if __name__ == "__main__":
    main()