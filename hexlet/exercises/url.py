from urllib.parse import urlparse, parse_qs


# BEGIN (write your solution here)
class Url:
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)
        self.params = {}
        if self.parsed_url.query:
            self.params = parse_qs(self.parsed_url.query)
        # parameters = parse_qs(url)
        # self.params = {}
        # for key, value in parameters.items():
        #     if '?' in key:
        #         new_key = key[key.find('?')+1:]
        #         self.params[new_key] = value
        #     else:
        #         self.params[key] = value

    def get_scheme(self):
        return self.parsed_url.scheme

    def get_hostname(self):
        return self.parsed_url.hostname

    def get_query_params(self):
        return self.params

    def get_query_param(self, param_name, param_value=None):
        if param_name in self.params:
            return self.params.get(param_name)[0]
        return param_value

    def __eq__(self, other):
        return self.url == other
    
# END
    
URL1 = 'http://hexlet.io?key=value&key2=value2'
URL2 = 'https://google.com:80?a=b&c=d&lala=value'


def test_url1():
    url = Url(URL1)
    print('scheme ', url.get_scheme() == 'http')
    print('hostname ',url.get_hostname() == 'hexlet.io')
    print('params ', url.get_query_params() == {
        'key': ['value'],
        'key2': ['value2'],
        })
    print(' param key', url.get_query_param('key') == 'value')
    print('param key 2', url.get_query_param('key2', 'lala') == 'value2')
    print('new param', url.get_query_param('new', 'ehu') == 'ehu')
    print('eq ', url == (Url(URL1)))
    print('not eq', not url == (Url(URL2)))


def test_url2():
    url = Url(URL2)
    print('URL2 scheme ', url.get_scheme() == 'https')
    print('hostname ', url.get_hostname() == 'google.com')
    print('query params ', url.get_query_params() == {
        'a': ['b'],
        'c': ['d'],
        'lala': ['value'],
        })
    print(' param key', url.get_query_param('key') is None)
    print('param key2', url.get_query_param('key2', 'lala') == 'lala')
    print('new param', url.get_query_param('new', 'ehu') == 'ehu')
    print('eq', url == (Url(URL2)))
    print('not eq', not url == (Url(URL1)))
    print('not eq2', not url == (Url('https://google.com')))
    print('not eq3', not url == (Url(URL2.replace('80', '443'))))


if __name__ == '__main__':
    test_url1()
    test_url2()
