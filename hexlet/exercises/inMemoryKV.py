import copy

class InMemoryKV:
    def __init__(self, dic):
        self.data = copy.deepcopy(dic)

    def set_(self, key, value):
        self.data.update({key: value})

    def unset_(self, key):
        self.data.pop(key)

    def get_(self, key, default=None):
        return self.data.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self.data)

def swap_key_value(data):
    tmp = data.to_dict()
    for key, value in tmp.items():
        data.set_(value, key)
    for key in data.to_dict().keys():
        if key not in tmp.values():
            data.unset_(key)


if __name__ == '__main__':
    map = InMemoryKV({'key': 10})
    map.set_('key2', 'value2')
    print(swap_key_value(map))
    
    print(map.get_('key') is None)
    print(map.get_(10) == 'key')
    print(map.get_('value2') == 'key2')

    map = InMemoryKV({'foo': 'bar', 'bar': 'zoo'})

    swap_key_value(map)
    print(map.to_dict() == {'bar': 'foo', 'zoo': 'bar'})
