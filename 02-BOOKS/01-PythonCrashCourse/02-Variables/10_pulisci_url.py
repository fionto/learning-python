url = "https://www.esempio.com"

#Stampa solo esempio.com, rimuovendo tutti i prefissi.

clean_url = url.removeprefix('https://').removeprefix('www.')

print(clean_url)