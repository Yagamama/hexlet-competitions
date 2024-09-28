from functools import wraps


def memoizing(count):
    """В этот раз вы снова будете реализовывать мемоизирующий декоратор "memoizing". 
    Но на этот раз декоратор должен принимать аргумент, задающий максимальное количество 
    запоминаемых значений. При превышении количества запомненных значений лишние должны быть 
    отброшены, причём сначала — самые старые!

    Напоминаю, мемоизируемые функции считать численными функциями одного аргумента. 
    И не забудьте про functools.wraps!

    Подсказки
    Хоть в современном Python словарь и помнит, в каком порядке добавлялись ключи, 
    но я не рекомендую строить логику, опираясь на это свойство. Используйте вспомогательную 
    структуру для хранения порядка ключей.

    @memoizing(3)
    def f(x):
        print('Calculating...')
        return x * 10
    
    f(1)
    # => Calculating...
    # 10
    f(1)  # будет "вспомнено"
    # 10
    f(2)
    # => Calculating...
    # 20
    f(3)
    # => Calculating...
    # 30
    f(4)  # вытеснит запомненный результат для "1"
    # => Calculating...
    # 40
    f(1)  # будет перевычислено
    # => Calculating...
    # 10
    """
    def wrapper(func):
        calc = {}
        calc_keys = []

        @wraps(func)
        def inner(arg):
            nonlocal calc
            nonlocal calc_keys
            if arg in calc:
                return calc.get(arg)
            if len(calc) == count:
                calc.pop(calc_keys[0])
                calc_keys.pop(0)
            result = func(arg)
            calc[arg] = result
            calc_keys.append(arg)
            return result

        return inner
    return wrapper
