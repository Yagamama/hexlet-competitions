def greet(name, *args):
    res = 'Hello, ' + name
    if len(args) > 0: 
        res = res + ' and ' +' and '.join(args)
    res = res + "!"
    print (res)


if __name__ == '__main__':
    greet('Anna')
    greet('Bob', 'Joe', 'Tom')