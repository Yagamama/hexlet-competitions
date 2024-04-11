def mult(f):
    return lambda x: f(x * x)

def add(func):
    return lambda x: func(x + 4)

@mult
@add
def f1(x):
    return x

@add
@mult
def f2(x):
    return x

if __name__ == '__main__':
    print(f1(2))  # 8
    print(f2(2)) # 36