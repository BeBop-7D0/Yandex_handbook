from sys import *

find = input()
files = [elem for elem in stdin.read().rstrip('\n').split('\n')]
names = []
for elem in files:
    with open(elem, encoding='UTF-8') as f_file:
        if find.replace(' ', '').replace('\n', '').lower() in f_file.read().replace(
                ' ', '').replace('\n', '').lower():
            names.append(elem)
if len(names) != 0:
    print(*[elem for elem in names], sep='\n')
else:
    print('404. Not Found')
