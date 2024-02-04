def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


def make_div(n):
    def division(x):
        return x / n
    return division


if __name__ == '__main__':
    times_2 = make_multiplier(2)
    times_3 = make_multiplier(3)
    div_2 = make_div(2)
    div_3 = make_div(3)

    print(times_2(5)) # 10
    print(times_3(5)) # 15
    print(div_2(30))
    print(div_3(30))