import os

file_name = input()

size = os.path.getsize(file_name)

scale = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
weight = 0

while size > 1024 and weight < len(scale):
    weight += 1
    size, overload = divmod(size, 1024)
    size += int(overload > 0)

print(f'{size}{scale[weight]}')
