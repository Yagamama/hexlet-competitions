def length(spis):
    count = 0
    if spis == []:
        print(count)
        return count
    
    def inner(spis):
        nonlocal count
        head, *tail = spis
        count +=1
        if not tail:
            print(count)
            return count
        return inner(tail)
    inner(spis)
    return count


def reverse_range(begin, end):
    array = []

    def inner(begin, end):
        nonlocal array
        if end >= begin:
            array.append(end)
            return inner(begin, end-1)
        #print(array)
        return array
    inner(begin, end)
    return array


def filter_positive(spis):
    array = []
    if spis == []:
        return array
    
    def inner(spis):
        nonlocal array
        head, *tail = spis
        if head > 0:
            array.append(head)
        if not tail:
            #print(array)
            return array
        return inner(tail)
    inner(spis)
    return array


if __name__ == '__main__':
    length([])
    length([1])
    print('length =',length([1,2,3,4,5,8,17]))
    print('reverse = ', reverse_range(2,5))
    filter_positive([]) 
    filter_positive([-3]) 
    filter_positive([1, -2, 3])