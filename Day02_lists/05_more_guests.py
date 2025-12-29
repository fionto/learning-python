#start with the lists of previous exercise. 
#Add a print() call to the end of your program, informing people that you found a bigger table.
#Use insert() to add one new guest at the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages

peoples = ['Napoleone', 'Hammurabi', 'Attila', 'Garibaldi']

print(f'Cari {peoples[0]}, {peoples[1]}, {peoples[2]}, {peoples[3]}, ho prenotato un tavolo più grande.\n')

#Aggiungi nuovo ospite all'inizio
peoples.insert(0, 'Cleopatra')

#Aggiungi nuovo ospite a metà lista
middle_index = len(peoples) // 2
peoples.insert(middle_index, 'Caterina')

#Aggiungi nuovo ospite alla fine della lista
peoples.append('Irene')

#Stampa inviti
print(f'Caro {peoples[0]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[1]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[2]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[3]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[4]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[5]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[6]}, vuoi venire a cena questa sera?')