# Scrivi un programma Python per trovare i numeri divisibili per 7 e multipli di 5, 
# compresi tra 1500 e 2700 (entrambi inclusi).

numbers = range(1500, 2701)
multiples = []

for number in numbers:
    
    is_div_seven = number % 7 == 0
    is_div_five = number % 5 == 0

    if is_div_seven and is_div_five:
        multiples.append(number)

print(multiples)