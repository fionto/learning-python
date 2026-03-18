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
        livello (int): Il livello attuale del personaggio (range valido 1-100).
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
            ValueError: 
                - Se punti_vita non è compreso tra 0 e 1000.
                - Se livello non è compreso tra 1 e 100.
        """
        self.nome = nome
        # Chiamo un metodo privato (_set_punti_vita) invece di assegnare direttamente
        # self.punti_vita = punti_vita. Perché? Perché voglio che la validazione
        # avvenga anche in fase di creazione. Se tra 6 mesi modifico i range nel setter,
        # l'__init__ sarà automaticamente aggiornato senza toccare questo codice.
        self._set_punti_vita(punti_vita)
        self._set_livello(livello)

    def _set_livello(self, valore: int):
        """
        Imposta il livello di esperienza applicando le regole di validazione.

        Questo metodo è privato (prefisso underscore) perché è un dettaglio
        implementativo interno. Non dovrebbe essere chiamato dall'esterno della classe.

        Args:
            valore (int): Il nuovo valore del livello.

        Raises:
            ValueError: Se il valore non è compreso tra 1 e 100.
        """
        # Scelgo di lanciare un errore invece di correggere silenziosamente (es. max/min).
        # Perché? Perché se arrivo qui con un valore sbagliato, voglio saperlo subito
        # durante lo sviluppo. Un errore blocca il programma e mi avvisa del bug.
        # Correggere in silenzio nasconderebbe errori di logica altrove nel codice.
        if not (1 <= valore <= 100):
            raise ValueError(f"Livello {valore} non valido. Range ammesso: 1-100.")
        
        self.livello = valore  # ✅ CORRETTO: Assegno all'attributo giusto

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
    """
    Gestisce la collezione di oggetti di un personaggio.

    Questa classe implementa la composizione: un Personaggio 'ha un' Inventario.
    Ogni istanza di Inventario è indipendente e non condivide stato con altre.

    Attributes:
        capacita_massima (int): Il numero massimo di oggetti trasportabili (0-10).
        _oggetti (list): Lista privata degli oggetti attualmente nell'inventario.
    """
        # Attualmente uso una lista semplice dove ogni elemento è un oggetto unico.
        # Se volessi implementare gli 'stack' di oggetti (es. 5 Pozioni nello stesso slot),
        # dovrei trasformare self._oggetti da lista a dizionario: {nome_oggetto: quantità}.
        #
        # 1. La capacità massima non sarebbe più len(self._oggetti), ma sum(self._oggetti.values()).
        # 2. aggiungi() dovrebbe incrementare il count invece di fare append(), oppure creare nuova key.
        # 3. rimuovi() dovrebbe decrementare il count e rimuovere la key solo se arriva a 0.
        #
        # Per ora mantengo la lista per mantenere la logica semplice e lineare.

    def __init__(self, capacita_massima=3, oggetti_iniziali=None):
        """
        Inizializza un nuovo inventario.

        Args:
            capacita_massima (int): La capacità massima dell'inventario.
            oggetti_iniziali (list, optional): Lista di oggetti iniziali. 
                Default è None per evitare liste mutabili condivise.

        """
        self._set_capacita(capacita_massima) # Vedi class Personaggio
        
        # Pattern standard per argomenti mutabili di default.
        # Se oggetti_iniziali è None, creo una NUOVA lista vuota per QUESTA istanza.
        # Se è fornita, uso quella (assumendo che sia una lista valida).
        if oggetti_iniziali is None:
            self._oggetti = []
        else:
            # Eseguo una copia perché voglio che la scelta sia fissata al momento dell'istanza
            self._oggetti = oggetti_iniziali[:]
    
    def _set_capacita(self, numero_oggetti):
        """
        Imposta la capacità massima applicando validazione.

        Args:
            numero_oggetti (int): Il numero massimo di oggetti.

        Raises:
            ValueError: Se il numero non è tra 0 e 10.
        """
        if not (0 <= numero_oggetti <= 10):
            raise ValueError(f"Capacità {numero_oggetti}: non valida. Range ammesso: 0-10.")
        
        self.capacita_massima = numero_oggetti

    def aggiungi(self, oggetto: str):
        """
        Aggiunge un oggetto all'inventario.

        Args:
            oggetto (str): Il nome dell'oggetto da aggiungere.

        Returns:
            bool: True se aggiunto con successo, False se inventario pieno.
        """
        # Uso >= invece di == per sicurezza. Se per bug la lista avesse 
        # già più elementi della capacità, blocchiamo comunque l'aggiunta.
        if len(self._oggetti) >= self.capacita_massima:
            return False
        
        # Validazione base: assicuriamoci che sia una stringa
        if not isinstance(oggetto, str):
            raise TypeError("Gli oggetti devono essere stringhe.")
            
        self._oggetti.append(oggetto.strip())
        return True
    
    def rimuovi(self, oggetto: str):
        """
        Rimuove un oggetto dall'inventario.

        Nota: La ricerca è case-sensitive ("Spada" != "spada").
        Se esistono duplicati, rimuove solo la prima occorrenza.

        Args:
            oggetto (str): Il nome dell'oggetto da rimuovere.

        Returns:
            bool: True se rimosso, False se non trovato.
        """
        nome_oggetto = oggetto.strip()
        
        # Controllo l'esistenza prima di rimuovere per evitare eccezioni
        # o per poter restituire un booleano chiaro al chiamante.
        if nome_oggetto not in self._oggetti:
            return False
        
        self._oggetti.remove(nome_oggetto)
        return True

    def mostra(self):
        """
        Stampa a video l'elenco degli oggetti posseduti.
        
        Se l'inventario è vuoto, stampa un messaggio informativo.
        """
        if not self._oggetti:
            print("L'inventario è vuoto.")
            return

        print("Oggetti nell'inventario:")
        for oggetto in self._oggetti:
            print(f" - {oggetto}")

class Guerriero(Personaggio):
    """
    Rappresenta un personaggio combattente specializzato.

    Eredita da Personaggio aggiungendo attributi e metodi legati al combattimento
    fisico e alla gestione di un inventario proprietario.

    Attributes:
        forza (int): La forza fisica del guerriero (influenza il danno).
        inventario (Inventario): L'istanza di composizione per gestire gli oggetti.
    """

    def __init__(self, nome: str, punti_vita: int, livello: int, forza: int):
        """
        Inizializza un nuovo Guerriero.

        Args:
            nome (str): Il nome del guerriero.
            punti_vita (int): I punti vita iniziali.
            livello (int): Il livello iniziale.
            forza (int): La forza fisica (deve essere > 0).

        Raises:
            ValueError: Se forza non è un numero positivo.
        """
        # NOTA PER IL ME FUTURO:
        # Uso super() per delegare l'inizializzazione di nome, PV e livello.
        # Se Personaggio.__init__ cambia, questo codice rimane valido automaticamente.
        super().__init__(nome, punti_vita, livello)
        
        # NOTA PER IL ME FUTURO:
        # Chiamo _set_forza invece di assegnare direttamente self.forza = forza.
        # Perché? Per coerenza con Personaggio._set_punti_vita.
        # Centralizzo la validazione in un unico punto. Se domani cambio le regole
        # sulla forza (es. max 100), modifico solo il setter e tutto si aggiorna.
        self._set_forza(forza)
        
        # Composizione: ogni Guerriero crea il SUO inventario.
        # Nessuna condivisione di stato con altri guerrieri.
        self.inventario = Inventario()

    def _set_forza(self, valore: int):
        """
        Imposta la forza fisica applicando le regole di validazione.

        Questo metodo è privato (prefisso underscore) perché è un dettaglio
        implementativo interno. Non dovrebbe essere chiamato dall'esterno.

        Args:
            valore (int): Il nuovo valore della forza.

        Raises:
            ValueError: Se il valore non è un intero positivo.
        """
        # NOTA PER IL ME FUTURO:
        # Scelgo di lanciare un errore invece di correggere silenziosamente.
        # Perché? Perché una forza <= 0 è probabilmente un errore di logica
        # nel codice che crea il guerriero. Voglio essere avvisato subito.
        if not isinstance(valore, int):
            raise TypeError("La forza deve essere un numero intero.")
        if valore <= 0:
            raise ValueError(f"Forza {valore} non valida. Deve essere > 0.")
        
        self.forza = valore

    def descrivi(self):
        """
        Stampa le informazioni del Guerriero, inclusi i dettagli della classe base.
        """
        # NOTA PER IL ME FUTURO:
        # Chiamo super().descrivi() per evitare di duplicare le stampe di
        # Nome, Livello e PV. Se cambio il formato nella classe base,
        # si aggiorna automaticamente anche qui (Principio DRY).
        super().descrivi()
        print(f"Forza: {self.forza}")
        # Delego la stampa dell'inventario all'oggetto composto
        self.inventario.mostra()

    def attacco_pesante(self, nemico: 'Personaggio') -> bool:
        """
        Esegue un attacco speciale basato sulla forza del guerriero.

        Args:
            nemico (Personaggio): Il bersaglio dell'attacco.

        Returns:
            bool: True se l'attacco è andato a segno, False altrimenti 
                  (es. guerriero morto o nemico non valido).
        """
        # 1. Controllo se sono vivo: un morto non attacca.
        if not self.e_vivo():
            print(f"{self.nome} è troppo ferito per attaccare!")
            return False

        # 2. Controllo il tipo: evito AttributeError se passo un oggetto sbagliato.            
        if not isinstance(nemico, Personaggio):
            raise TypeError("Si può attaccare solo un'istanza di Personaggio.")

        # Delego il calcolo del danno alla logica del nemico.
        # Il guerriero non sa come il nemico gestisce i PV, sa solo infliggere danno.
        print(f"{self.nome} attacca {nemico.nome} per {self.forza} danni!")
        return nemico.subisci_danno(self.forza)