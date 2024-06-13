results = []


def enter_results(*values):
    for elem in values:
        results.append(elem)
    return results


def get_sum():
    first_sum, second_sum = 0, 0
    for i in range(len(results)):
        if i % 2 == 0:
            first_sum += results[i]
        else:
            second_sum += results[i]
    return first_sum, second_sum


def get_average():
    return (get_sum()[0] / (len(results) // 2),
            get_sum()[1] / (len(results) // 2))


