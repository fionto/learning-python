"""
entities.py - Modulo per la gestione di personaggi e inventario in un gioco RPG.

Questo modulo fornisce le classi base per creare personaggi, guerrieri e gestire
gli inventari. Include validazione dei dati e protezione contro errori comuni.

Classes:
    Personaggio: Classe base per tutti i personaggi.
    Inventario: Classe di composizione per gestire gli oggetti.
    Guerriero: Classe derivata con abilità di combattimento.
"""

# =============================================================================
# COSTANTI DI CONFIGURAZIONE
# =============================================================================
# Modificare questi valori per bilanciare il gioco senza toccare le classi.

MIN_LIVELLO = 1
MAX_LIVELLO = 100

MIN_PUNTI_VITA = 0
MAX_PUNTI_VITA = 1000

MIN_INVENTARIO = 0
MAX_INVENTARIO = 10

MIN_FORZA = 1

# =============================================================================
# CLASSI
# =============================================================================

class Personaggio:
    """
    Rappresenta un personaggio generico nel gioco.

    Questa classe funge da base per personaggi giocanti e NPC. Gestisce gli attributi
    vitali (nome, livello, punti vita) e le operazioni fondamentali di sopravvivenza.

    Attributes:
        nome (str): Il nome del personaggio.
        livello (int): Il livello attuale del personaggio.
        punti_vita (int): I punti vita attuali.
    """

    def __init__(self, nome: str, punti_vita: int, livello: int):
        """
        Inizializza un nuovo personaggio.

        Args:
            nome (str): Il nome del personaggio.
            punti_vita (int): I punti vita iniziali.
            livello (int): Il livello iniziale del personaggio.

        Raises:
            ValueError: Se i valori non rientrano nei range ammessi.
        """
        self.nome = nome
        # Uso i setter privati per centralizzare la validazione.
        # Se le costanti cambiano, questo codice non richiede modifiche.
        self._set_punti_vita(punti_vita)
        self._set_livello(livello)

    def _set_livello(self, valore: int):
        """
        Imposta il livello di esperienza applicando le regole di validazione.
        """
        if not (MIN_LIVELLO <= valore <= MAX_LIVELLO):
            raise ValueError(f"Livello {valore} non valido. Range: {MIN_LIVELLO}-{MAX_LIVELLO}.")
        
        self.livello = valore

    def _set_punti_vita(self, valore: int):
        """
        Imposta i punti vita applicando le regole di validazione.
        """
        if not (MIN_PUNTI_VITA <= valore <= MAX_PUNTI_VITA):
            raise ValueError(f"PV {valore} non valido. Range: {MIN_PUNTI_VITA}-{MAX_PUNTI_VITA}.")
        
        self.punti_vita = valore

    def descrivi(self):
        """
        Stampa le informazioni principali del personaggio a video.
        """
        # In un progetto reale, separare logica e presentazione restituendo una stringa.
        print(f"Nome personaggio: {self.nome.title()}")
        print(f"Livello: {self.livello}")
        print(f"Punti vita: {self.punti_vita}")

    def subisci_danno(self, quantita: int):
        """
        Riduce i punti vita del personaggio di una quantità specifica.

        Args:
            quantita (int): La quantità di danno da subire. Deve essere >= 0.

        Returns:
            bool: True se il danno è stato applicato, False se negativo.
        """
        if quantita < 0:
            return False

        # Calcolo preventivo per non passare valori negativi al setter.
        nuovo_valore = max(MIN_PUNTI_VITA, self.punti_vita - quantita)
        self._set_punti_vita(nuovo_valore)
        return True

    def e_vivo(self):
        """
        Verifica se il personaggio è ancora in vita.

        Returns:
            bool: True se punti_vita > 0.
        """
        return self.punti_vita > MIN_PUNTI_VITA


class Inventario:
    """
    Gestisce la collezione di oggetti di un personaggio.

    Questa classe implementa la composizione: un Personaggio 'ha un' Inventario.
    Ogni istanza di Inventario è indipendente e non condivide stato con altre.

    Attributes:
        capacita_massima (int): Il numero massimo di oggetti trasportabili.
        _oggetti (list): Lista privata degli oggetti attualmente nell'inventario.
    """
    # IDEA PER REFACTORING FUTURO:
    # Attualmente uso una lista semplice. Per implementare gli 'stack' (es. 5 Pozioni),
    # trasformare self._oggetti in dizionario: {nome_oggetto: quantità}.
    # La capacità si calcolerebbe su sum(self._oggetti.values()).

    def __init__(self, capacita_massima=3, oggetti_iniziali=None):
        """
        Inizializza un nuovo inventario.

        Args:
            capacita_massima (int): La capacità massima dell'inventario.
            oggetti_iniziali (list, optional): Lista di oggetti iniziali.
        """
        self._set_capacita(capacita_massima)
        
        # Pattern standard per argomenti mutabili di default.
        if oggetti_iniziali is None:
            self._oggetti = []
        else:
            # Copia la lista per evitare riferimenti esterni condivisi
            self._oggetti = oggetti_iniziali[:]
    
    def _set_capacita(self, numero_oggetti):
        """
        Imposta la capacità massima applicando validazione.
        """
        if not (MIN_INVENTARIO <= numero_oggetti <= MAX_INVENTARIO):
            raise ValueError(f"Capacità {numero_oggetti} non valida. Range: {MIN_INVENTARIO}-{MAX_INVENTARIO}.")
        
        self.capacita_massima = numero_oggetti

    def aggiungi(self, oggetto: str):
        """
        Aggiunge un oggetto all'inventario.

        Returns:
            bool: True se aggiunto, False se pieno.
        """
        if len(self._oggetti) >= self.capacita_massima:
            return False
        
        if not isinstance(oggetto, str):
            raise TypeError("Gli oggetti devono essere stringhe.")
            
        self._oggetti.append(oggetto.strip())
        return True
    
    def rimuovi(self, oggetto: str):
        """
        Rimuove un oggetto dall'inventario (case-sensitive).

        Returns:
            bool: True se rimosso, False se non trovato.
        """
        nome_oggetto = oggetto.strip()
        
        if nome_oggetto not in self._oggetti:
            return False
        
        self._oggetti.remove(nome_oggetto)
        return True

    def mostra(self):
        """
        Stampa a video l'elenco degli oggetti posseduti.
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
        forza (int): La forza fisica del guerriero.
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
        """
        super().__init__(nome, punti_vita, livello)
        # Uso il setter per coerenza con Personaggio e validazione centralizzata.
        self._set_forza(forza)
        # Composizione: ogni Guerriero ha il proprio inventario indipendente.
        self.inventario = Inventario()

    def _set_forza(self, valore: int):
        """
        Imposta la forza fisica applicando le regole di validazione.
        """
        if not isinstance(valore, int):
            raise TypeError("La forza deve essere un numero intero.")
        if valore <= MIN_FORZA:
            raise ValueError(f"Forza {valore} non valida. Deve essere > {MIN_FORZA}.")
        
        self.forza = valore

    def descrivi(self):
        """
        Stampa le informazioni del Guerriero, inclusi i dettagli della classe base.
        """
        # Chiamo super() per evitare duplicazione (Principio DRY).
        super().descrivi()
        print(f"Forza: {self.forza}")
        self.inventario.mostra()

    def attacco_pesante(self, nemico: 'Personaggio') -> bool:
        """
        Esegue un attacco speciale basato sulla forza del guerriero.

        Args:
            nemico (Personaggio): Il bersaglio dell'attacco.

        Returns:
            bool: True se l'attacco è andato a segno.
        """
        if not self.e_vivo():
            print(f"{self.nome} è troppo ferito per attaccare!")
            return False
            
        if not isinstance(nemico, Personaggio):
            raise TypeError("Si può attaccare solo un'istanza di Personaggio.")

        print(f"{self.nome} attacca {nemico.nome} per {self.forza} danni!")
        return nemico.subisci_danno(self.forza)


# =============================================================================
# CONTROLLO EXPORT
# =============================================================================
# Definisce cosa viene importato con "from rpg_classes import *"
__all__ = ['Personaggio', 'Inventario', 'Guerriero']