# ESERCIZIO 6
# 
# OBIETTIVO: Data una stringa di input contenente coppie "chiave:valore" separate
# da virgole (es: "nome:Mario,cognome:Rossi"), usa un ciclo while e partition() 
# per estrarre i dati e inserirli in un dizionario.

dati_grezzi = "id:001,stato:attivo,livello:esperto,punteggio:85"
dati_puliti = {}

while dati_grezzi:
    # Estraggo la prima coppia e il resto della stringa
    coppia, virgola, resto = dati_grezzi.partition(',')
    
    # Processo la coppia trovata
    chiave, due_punti, valore = coppia.partition(':')
    dati_puliti[chiave] = valore
    
    # Aggiorniamo la stringa principale con il 'resto' per il prossimo ciclo
    dati_grezzi = resto