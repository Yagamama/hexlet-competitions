def odds_from_odds(array):
    #r = list(filter(lambda x: array.index(x) % 2 == 0, array))
    k = list(map(lambda x: x[::2], array[::2]))
    print('k = ', k)
    #r = list(map(lambda y: list(filter(lambda x: y.index(x) % 2 == 0, y)), r))
    #print(r)
    return k


def keep_odds_from_odds(array):
    for i in range(len(array)-1, -1, -1):
        if i% 2 == 1:
            array.pop(i)
        else:
            for j in range(len(array[i])-1, -1, -1):
                if j % 2 == 1:
                    array[i].pop(j)
    print (array)
    return 


if __name__ == '__main__':
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10,11,12], [13,14,15]]
    #odds_from_odds(l)
    #odds_from_odds([])
    #odds_from_odds([[]])
    #keep_odds_from_odds(l)
    #keep_odds_from_odds(l)
    #keep_odds_from_odds(l)
    #keep_odds_from_odds([])
    #keep_odds_from_odds([[]])
    l = [
        [1, 2, 3, 4, 5],
        ['c', 'a', 't'],
        ['d', 'o', 'g'],
        [100, 200, 300, 400],
        [True, False],
        [],
        [],
    ]
    odds_from_odds(l)
    keep_odds_from_odds(l)
