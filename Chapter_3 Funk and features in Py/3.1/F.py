
a = ''


def modern_print(text):
    global a
    if text not in a:
        a += text
        return print(text)


