import pytest


def test_read():
    with pytest.raises(Exception) as e:
        reading('anyfile')
    print(e.typename)

    with pytest.raises(Exception) as e:
        reading('/etc')
    print(e.typename)

def reading(path):
    f = open(path)
    data = f.read()
    f.close()
    return data

if __name__ == '__main__':
    test_read()