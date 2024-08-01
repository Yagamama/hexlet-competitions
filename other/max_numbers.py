# Найдите число с наибольшим количеством цифр.
# Если два числа в массиве аргументов имеют одинаковое количество цифр, 
# верните первое число в массиве.

# Пример:
#    100 1000 10 —> 1000

def max_numbers(data):
    str_data = [str(d) for d in data]
    len_max = max(len(d) for d in str_data)
    filt = filter(lambda x: len(x) == len_max, str_data)
    return int(list(filt)[0])


if __name__ == '__main__':
    print(max_numbers([4, 12, 73, 238, 100, 3]))
    print(max_numbers([100, 4, 12, 73, 238, 3]))