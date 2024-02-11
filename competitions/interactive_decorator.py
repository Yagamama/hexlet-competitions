import prompt


def interactive(text):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)
        return inner
    return wrapper


def asks(name, question):
    def wrapper(func):
        def inner(*args, **kwargs):
            nonlocal name
            name = prompt.string(question)
            #print ('name =', name)
            return func(name, *args, **kwargs)
        return inner
    return wrapper


@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
@interactive('Calculator')
def calc(x, y):
    print(int(x) + int(y))
    return int(x) + int(y)


if (__name__ == '__main__'):
    calc()
    # Calculator
    # Enter first number: 42
    # Enter second number: 57
    # 99