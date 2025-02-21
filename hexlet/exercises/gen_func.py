from itertools import chain


def my_map(f, xs):
    for elem in xs:
        print ('my map = ', f(elem))
        yield f(elem)


def my_filter(f, xs):
    for elem in xs:
        if f(elem):
            print ('my filter =', elem)
            yield elem
        print ('my filter <>', elem)


def replicate_each(n, xs):
    for elem in xs:
        for _ in range(n):
            yield elem


if __name__ == '__main__':
    list(my_map(abs, [-1, 2, -3]))  # [1, 2, 3]
    list(my_filter(lambda x: x % 2 == 1, range(10)))  # [1, 3, 5, 7, 9]
    #list(replicate_each(1, [1, 'a']))  # [1, 'a']
    print(list(replicate_each(1, [1, 2, 3])))
    print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
    print(list(replicate_each(0, [1, 'a'])))  # []