# ==============================================================================
# ESERCIZIO PRATICO: SISTEMA DI GESTIONE PERSONAGGI RPG
# ==============================================================================
#
# OBIETTIVO:
# Creare un sistema software per gestire personaggi di un gioco di ruolo,
# applicando i concetti di Classi, Ereditarietà e Composizione appresi,
# ma prestando attenzione alla qualità del codice e alla robustezza.
#
# REQUISITI FUNZIONALI:
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
#    - Ereda dalla classe Personaggio.
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