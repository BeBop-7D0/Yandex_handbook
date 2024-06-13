from itertools import product

nom = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
mast = ['пик', 'треф', 'бубен', 'червей']
mast.remove(input())
for val in product(nom, mast):
    print(*val)
