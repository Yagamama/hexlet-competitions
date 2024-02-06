from functools import reduce
import operator


def keep_truthful(iterable):
    return filter(lambda x: operator.truth(x), iterable)


def abs_sum(nums):
    # return sum(abs(nums))
    return reduce(lambda x,y: abs(x)+abs(y), nums, 0)


def walk(dic, path):
    #find_path(dic, path)
    #return reduce(operator.getitem(dic, path), (dic, path))
    findpath = f_path(dic)
    return map(findpath, path)
    #map(dic.get(lambda x: x.append(path)), dic)
    

def f_path(dic):
    def fp(path):
        dic = dic.get(path)
        print(path)
        return dic
    return fp

def find_path(dic, path):
    #if dic == path
    dic = dic.get(path)
    print(dic)
    return dic
    #for a in path:
    #    print('a =', a)
    #    dic = dic.get(a)
    #    print(dic)


if __name__ == '__main__':
    # print(list(keep_truthful([True, False, "", "foo"])))
    # print(abs_sum([-3, 7]))
    # print(abs_sum([]))
    # print(abs_sum([450]))
    walk({'a': {7: {'b': 45}}}, ["a", 7, "b"])
    walk({'a': {7: {'b': 45}}}, ["a", 7])

