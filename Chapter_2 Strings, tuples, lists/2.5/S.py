alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
shift = int(input())
with open('public.txt', encoding='UTF-8') as input_file:
    s = input_file.read()

with open('private.txt', 'w', encoding='UTF-8') as out_file:
    for elem in s:
        if elem.lower() in alf:
            if elem.isupper():
                print(alf[abs((alf.index(elem.lower()) + shift) % 26)].upper(), end='', file=out_file)
            else:
                print(alf[abs((alf.index(elem.lower()) + shift) % 26)], end='', file=out_file)
        else:
            print(elem, end='', file=out_file)
