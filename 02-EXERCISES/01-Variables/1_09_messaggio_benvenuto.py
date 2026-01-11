#Stampa un messaggio del tipo: Ciao Giulia! Benvenuta a Milano. 
#(formattato correttamente, usando un f-string).

nome = "giulia"
citta = "MILANO"

messaggio = f"Ciao {nome.title()}, benvenuta a {citta.title()}"

print(messaggio)