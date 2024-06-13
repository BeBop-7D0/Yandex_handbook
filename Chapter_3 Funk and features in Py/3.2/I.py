
def secret_replace(text, **law):
    s = ''
    for i in range(len(text)):
        s += law.get(text[i], text[i])[(text[:i].count(text[i])) % len(law.get(text[i], text[i]))]
    return s

