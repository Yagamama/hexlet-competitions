class Truncater:

    OPTIONS = {}

    def __init__(self, **kwargs):
        self.OPTIONS = {
            'separator': '...',
            'length': 200,
        }
        for key in self.OPTIONS.keys():
            if key in kwargs:
                self.OPTIONS[key] = kwargs[key]

    def truncate(self, string, **kwargs):
        options = self.OPTIONS | {}
        for key in options.keys():
            if key in kwargs:
                options[key] = kwargs[key]
        if len(string) > options['length']:
            return string[:options['length']] + options['separator']
        return string

# END

if __name__ == '__main__':
    truncater = Truncater()
    print('one two', truncater.truncate('one two') == 'one two')
    print('one two, l=6', truncater.truncate('one two', length=6) == 'one tw...')
    print('one two sep.', truncater.truncate('one two', separator='.') == 'one two')
    print('one two l=3', truncater.truncate('one two', length=3) == 'one...')

    truncater = Truncater(length=3)
    print('l=3:', truncater.truncate('one two') == 'one...')
    print('sep!', truncater.truncate('one two', separator='!') == 'one!')
    print('sep...', truncater.truncate('one two') == 'one...')

    print('l=7', truncater.truncate('one two', length=7) == 'one two')