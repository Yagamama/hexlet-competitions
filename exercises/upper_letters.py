def choose_upper(string):
    return [i for i, x in enumerate(string) if x.isupper()]


if __name__ == '__main__':
    print(choose_upper('SomeSTRinG'))
