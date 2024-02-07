def memoized(func):
    calc = {}
    def inner(x):
        nonlocal calc
        if x in calc:
            print('calc.get(x) =', calc.get(x))
            return calc.get(x)
        calc[x] = func(x)
        print(calc)
        return 
    return inner


@memoized
def f(x):
    print('Calculating...')
    print(x * 10)
    return x * 10


if __name__ == '__main__':
    f(5)
    f(8)
    f(5)