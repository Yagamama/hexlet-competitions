def simple_input(_, prompt):
    """Just input string."""
    return input(prompt)


def asks(name, prompt, **kw):
    # BEGIN (write your solution here)

    def wrapper(func):

        def inner(*args, **kwargs):
            #f = simple_input
            kw.update({name: prompt})
            kwargs.update({name: prompt})
            print ('asks kw =', kw)
            #print (simple_input.__getattribute__())
            #interactive.__setattr__('input_function', simple_input(name, prompt))
            # return #(func(*args, **kwargs))
            return #(*args, kw)
        return inner
    return wrapper
    # END


def interactive(
    description,
    input_function=simple_input,
    output_function=print,
):
    # BEGIN (write your solution here)
    def wrapper(func):
        def inner(*args, **kwargs):
            output_function(description)
            # kw = getattr(input_function, **kwargs)
            print('kw = ', kwargs)
            for key, prompt in kwargs.items():
                value = input_function(key, prompt)
                print('value = ', value)
                kwargs[key] = value
            result = func(*kwargs)
            output_function(result)
        return inner
    return wrapper
    # END


@interactive('Calculator')  
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calc(x, y):
    return int(x) + int(y)


if __name__ == '__main__':
    calc()
