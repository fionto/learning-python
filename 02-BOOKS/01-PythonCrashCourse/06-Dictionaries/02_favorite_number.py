# Use a dictionary to store people's favorite numbers.
# Print each person's name and their favorite number.

# Memorizzo nome e numero preferito
amici = {
    "Leonardo": 23,
    "Michelangelo": 30,
    "Donatello": 7,
    "Raffaello": 55,
}

# Scorro le coppie trasformandole in touples
# Looping through all Key-Values pairs (vedi pagina 99 Python Crash Course)
for nome, numero in amici.items():
    print(f"Il numero preferito di {nome} è {numero}")