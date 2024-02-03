def rgb(red=0, green=0, blue=0):
    print(f'rgb({red}, {green}, {blue})')
    return f'rgb({red}, {green}, {blue}'


def get_colors():
    return {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255),
    }


def test_colors():
    colors = get_colors()
    assert set(colors.keys()) == {'red', 'green', 'blue'}
    assert colors['red'] == rgb(red=255)
    assert colors['green'] == rgb(green=255)
    assert colors['blue'] == rgb(blue=255)


if __name__ == '__main__':
    test_colors()