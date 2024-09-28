from itertools import chain
def each2d(test, matrix):
    res = (test(x) for x in chain(*matrix))
    if not all(res):
        print(matrix, ' = False')
        return False
    print(matrix, ' = True')
    return True

def some2d(test, matrix):
    res = (test(x) for x in chain(*matrix))
    if any(res):
        print(matrix, ' = True')
        return True
    print(matrix, ' = False')
    return False
    

def sum2d(test, matrix):
    res = sum([x for x in chain(*matrix) if test(x)])
    print('sum 2d =', res)
    return res


def is_int(x):
    return isinstance(x, int)


if __name__ == '__main__':
    #each2d(is_int, [1, 2, 3, 4])  # True
    each2d(is_int, [[1, 2], [3, 4]])  # True
    each2d(is_int, [[1, None], [3, 4]])  # False
    # В пустой матрице нет ни одного элемента, который бы завалил тест
    each2d(is_int, [])      # True
    some2d(is_int, [[None, "foo"], [(), {}]])   # False
    some2d(is_int, [[None, "foo"], [0, {}]])    # True
    # В пустой матрице нет ни одного элемента, который бы прошел тест
    some2d(is_int, [])     # False
    sum2d(is_int, [[1, "Foo", 100], [False, 10, None]])  # 111