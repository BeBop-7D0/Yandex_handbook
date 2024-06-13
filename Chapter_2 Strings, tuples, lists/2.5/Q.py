with open('secret.txt', encoding='UTF- 8') as in_file:
    text = in_file.read()
word = [ord(elem) for elem in text]
for val in word:
    if val > 128:
        cod = []
        new_val, j = 0, 7
        cod.append(val % 2)
        while val >= 2:
            val = val // 2
            cod.append(val % 2)
        for i in range(7, -1, - 1):
            new_val += cod[i] * (2 ** j)
            j -= 1
        print(chr(new_val), end='')
    else:
        print(chr(val), end='')
