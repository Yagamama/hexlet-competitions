# Вам предоставлены последовательные элементы арифметической прогрессии. 
# Однако есть одна загвоздка: в данном вам наборе чисел не хватает ровно одного члена исходного ряда. 
# Напишите функцию, которая будет определять недостающий член прогрессии.

# Пример:

#    find_missing([1, 3, 5, 9, 11]) == 7

def find_missing(data):
    steps = {data[i] - data[i-1]: i-1 for i in range(1, len(data))}
    if len(steps) != 2:
        return 'Wrong data!'
    max_step = max(steps.keys())
    i = steps.get(max_step)
    return data[i] + max_step // 2


if __name__ == '__main__':
    print(find_missing([1, 3, 5, 9, 11]))
    print(find_missing([3, 8, 13, 23, 28, 33]))
    print(find_missing([3, 8, 13, 18, 23, 29, 33]))
