
def order(*name):
    for napitok in name:
        k = 0
        for elem in 'coffee', 'milk', 'cream':
            if recept[napitok][elem] <= in_stock[elem]:
                k += 1
        if k == 3:
            for elem in 'coffee', 'milk', 'cream':
                in_stock[elem] -= recept[napitok][elem]
            return napitok
    return 'К сожалению, не можем предложить Вам напиток'


recept = {'Эспрессо': {"coffee": 1, "milk": 0, "cream": 0}, 'Капучино': {"coffee": 1, "milk": 3, "cream": 0},
          'Макиато': {"coffee": 2, "milk": 1, "cream": 0}, 'Кофе по-венски': {"coffee": 1, "milk": 0, "cream": 2},
          'Латте Макиато': {"coffee": 1, "milk": 2, "cream": 1}, 'Кон Панна': {"coffee": 1, "milk": 0, "cream": 1}}
