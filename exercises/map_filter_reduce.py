from functools import reduce
import operator


def keep_truthful(iterable):
    return filter(lambda x: operator.truth(x), iterable)


def abs_sum(nums):
    # return sum(abs(nums))
    return reduce(lambda x,y: abs(x)+abs(y), nums, 0)


def walk(dic, path):
    print(reduce(operator.getitem, path, dic))


if __name__ == '__main__':
    # print(list(keep_truthful([True, False, "", "foo"])))
    # print(abs_sum([-3, 7]))
    # print(abs_sum([]))
    # print(abs_sum([450]))
    walk({'a': {7: {'b': 45}}}, ["a", 7, "b"])
    #walk({'a': {7: {'b': 45}}}, ["a", 7])

