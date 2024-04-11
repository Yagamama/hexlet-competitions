def calculate_probabilities(history):
    result = {num: {} for num in history}
    for num in result.keys():
        filt = [history[i+1] for i, x in enumerate(history[0:-1]) if x == num]
        it = lambda x: filt.count(x)/len(filt)
        result[num] = {value: round(it(value), 2) for value in filt }

    for elem in result.items():
        print(elem)


if __name__ == '__main__':
    calculate_probabilities([1, 3, 2, 5, 1, 2, 1, 6])