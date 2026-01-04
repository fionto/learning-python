testo = "   Programmazione Python   "

#Stampa tre informazioni su righe separate:
#1 Il testo pulito (senza spazi extra)
#2 La lunghezza del testo pulito
#3 La posizione in cui si trova la parola "Python" nel testo pulito

testo_pulito = testo.strip()

print(testo_pulito)
print(len(testo_pulito))
print(testo_pulito.find('Python'))