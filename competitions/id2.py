def simple_input(_, prompt, name = {}, text = {}, value = {}):
    """Just input string."""
    return input(prompt)


def asks(name, prompt):
    """
    Описывает один запрос аргумента.

    Arguments:
        name - имя аргумента оборачиваемой функции,

        prompt - текст приглашения.

    Returns:
        декоратор, который и обернёт нужную функцию. Помните, после
        описания всех аргументов нужно результат обернуть в
        декоратор interactive!

    """
    # BEGIN (write your solution here)
    def wrapper(func):
        
        def inner(*args, **kwargs):
            kwargs.update({name:prompt})
            # kwargs[name] = prompt
            print('kwargs =', kwargs)
            #simple_input.__setattr__(kwargs.update({name:prompt}))
            simple_input.__setattr__('prompt', prompt)
            print('asks s_i attr: ',simple_input.__getattribute__('prompt'))
            return kwargs
        return inner()
    return wrapper
    # END


def interactive(
    description,
    input_function=simple_input,
    output_function=print,
):
    """
    Делает функцию с описанными параметрами интерактивной.

    Интерактивной может быть функция без параметров. В этом случае декоратор
    asks не потребуется.

    Arguments:
        description - описание, которое будет выведено в начале
        диалога (интерактивной сессии).

        input_function - функция, принимающая имя аргумента и приглашение,
        и возвращающая введённый пользователем текст (str).

        output_function - функция, которая будет использована для вывода
        описания и результата вызова оборачиваемой функции.

    Returns:
        декоратор, который обернёт целевую функцию.

    """
    # BEGIN (write your solution here)
    def wrapper(func):
        def inner(*args, **kwargs):
            output_function(description)
            #kwargs = getattr(input_function, **kwargs)
            print('kwargs inter =', kwargs)
            for key, prompt in kwargs:
                value = input_function(key, prompt)
                kwargs[key] = value
            print('kwargs inter2 =', kwargs)
            result = func(*kwargs.values())
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
