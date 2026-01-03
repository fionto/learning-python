#Stampa il nome formattato correttamente (iniziali maiuscole, senza spazi extra).

nome = "  mARIO rossi  "

nome_corretto = nome.rstrip()
nome_corretto = nome_corretto.lstrip()
nome_corretto = nome_corretto.title()

print(nome_corretto)