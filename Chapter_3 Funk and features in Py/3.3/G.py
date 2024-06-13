def same_type(func):
    def decor(*val, **kwarg):
        for elem in val:
            for elem1 in val:
                if type(elem) is not type(elem1):
                    print("Обнаружены различные типы данных")
                    return 'Fail'
        return func(*val, **kwarg)
    return decor
