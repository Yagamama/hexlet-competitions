from functools import reduce


def display(image):
    for line in image:
        print(line)


def enlarge(image):
    pair = lambda x: [x, x]
    dup = lambda x: x + x
    result = map(dup, image[0])
    return result


if __name__ == "__main__":
    glider = [' * ', '  *', '***']
    #enlarge(glider)
    display(enlarge(glider))