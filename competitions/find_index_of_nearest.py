from functools import reduce


def find_index_of_nearest(number, array):
    if array == []:
        print('None')
        return None
    result = list(map(lambda x: abs(number - x), array))
    min = (reduce(lambda x,y: x if x<y else y, result))
    print(result.index(min))
    return result.index(min)


if __name__ == "__main__":
    find_index_of_nearest(2, []) is None
    # True
    find_index_of_nearest(0, [15, 10, 3, 4])
    # 2
    find_index_of_nearest(4, [7, 5, 3, 2])
    # 1
    find_index_of_nearest(4, [7, 5, 4, 4, 3])
    # 2)