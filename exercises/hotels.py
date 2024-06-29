KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75

# BEGIN (write your solution here)
def find_all_matching(data, *args):
    min_cost = -float('inf')
    max_cost = float('inf')
    for arg in args:
        min_cost = arg.get('min', -float('inf'))
        max_cost = arg.get('max', float('inf'))
    result = []
    for item in data:
        for hotel in item['hotels']:
            cost = calculate_cost(item['service'], hotel['cost'])
            if cost > min_cost and cost < max_cost:
                normalized = {'service': item['service']}
                normalized['hotel'] = {}
                normalized['hotel']['name'] = hotel['name']
                normalized['hotel']['cost'] = cost
                result.append(normalized)
    for item in result:
        print(item)
    return result


def calculate_cost(service, price):
    match service:
        case 'kostrovok':
            return round(price * (1 + KOSTROVOK_FEE), 2)
        case 'book-king':
            return price * BOOKKING_CONVERT_RATE
        case _ :
            return price
# END


def find_the_cheapest_service(data, predicates=None):
    array = find_all_matching(data, predicates)
    array.sort(key=lambda x: x.get('hotel').get('cost'))
    print('sorted:')
    for item in array:
        print(item)
    return array[0]



if __name__ == '__main__':
    data = [
        {
            "service": "kostrovok",
            "hotels": [
            { "name": "$phpInn", "cost": 600 },
            { "name": "JSInn", "cost": 620 },
            { "name": "python_inn", "cost": 550 },
            { "name": "JavaInn", "cost": 810 }
            ]
        },
        {
            "service": "book-king",
            "hotels": [
            { "name": "$phpInn", "cost": 15 },
            { "name": "JSInn", "cost": 11 },
            { "name": "python_inn", "cost": 9 },
            { "name": "JavaInn", "cost": 10.7 }
            ]
        },
        {
            "service": "airdnb",
            "hotels": [
            { "name": "$phpInn", "cost": 680 },
            { "name": "JSInn", "cost": 750 },
            { "name": "python_inn", "cost": 500 },
            { "name": "JavaInn", "cost": 810 }
            ]
        }
        ]
    
    # print('all: ')
    # find_all_matching(data)
    # print('700 - 900: ')
    # find_all_matching(data, {'min': 700, 'max': 900})
    # print('max 900:')
    # find_all_matching(data, {'max': 900})
    # print('min 700: ')
    # find_all_matching(data, {'min': 700})

    find_the_cheapest_service(data, {'min': 700, 'max': 900})
