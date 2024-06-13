
def can_eat(cor_1, cor_2):
    x1 = cor_1[0]
    y1 = cor_1[1]
    x2 = cor_2[0]
    y2 = cor_2[1]
    if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
        return True
    else:
        return False

