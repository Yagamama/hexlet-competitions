def fizzbuzz():
    for i in range(1, 51):
        s = ''
        if i % 3 == 0: 
            s = 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        print(s or i)

if __name__ == '__main__':
    fizzbuzz()
