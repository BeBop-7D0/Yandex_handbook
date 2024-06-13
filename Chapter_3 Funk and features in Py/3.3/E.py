def result_accumulator(func):
    accum = []

    def acc(*val, **kwargs):
        method = kwargs.get('method', 'accumulate')
        accum.append(func(*val))
        if method == 'accumulate':
            return
        else:
            vivod = str(accum)
            accum.clear()
            return vivod
    return acc

