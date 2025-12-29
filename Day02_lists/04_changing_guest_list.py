#start with exercise 3 guest list.
#Add a print() call at the end of your program, stating the name of the gues who can't make it
#Modify your list replacing the name of the guest who can make it.
#Print a set of invitations, one for each person who is still in  your list.

peoples = ['Napoleone', 'Hammurabi', 'Attila', 'Garibaldi']

print(f"L'invitato {peoples[3]} ha rifiutato l'invito")

peoples[3] = 'Traiano'

print(f'Caro {peoples[0]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[1]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[2]}, vuoi venire a cena questa sera?')
print(f'Caro {peoples[3]}, vuoi venire a cena questa sera?')