def choose_upper(string):
    return [i for i, x in enumerate(string) if x.isupper()]


def for_each(data, func):
    for value in data:
        func(value)


if __name__ == '__main__':
    for_each([1, 2, 3], lambda v: print(v))
    #print(choose_upper('SomeSTRinG'))
