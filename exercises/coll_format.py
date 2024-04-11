from collection import Collection


# BEGIN (write your solution here)
# def format(coll):
#     data = Collection(coll)
#     data = Collection.map_(data, lambda x: {
#                             'name': x['name'].lower().strip(),
#                             'country': x['country'].lower().strip()})
#     data = data.unique()
#     data = data.group_by(lambda x: (x['country'], x['name'])) 
#     data = data.sort_by(lambda x: list(x.values()))
#     data = data.sort_by(lambda x: list(x.keys()))
#     #data = Collection.map_(data, lambda x: {x.keys(): sorted(x.values())})
#     Collection.print(data)
#     # Collection.print(data)
# END

def format(data):
    c = Collection(data)
    return c.map_(_normalise) \
        .unique() \
        .group_by(lambda row: (row['country'], row['name'])) \
        .map_(lambda row: {key: sorted(values) for key, values in row.items()}) \
        .sort_by(lambda row: list(row.keys())) \
        .all()


def _normalise(row):
    return {'name': row['name'].lower().strip(), 'country': row['country'].lower().strip()}
# END
    

if __name__ == '__main__':
    raw = [{'name': 'istambul', 'country': 'turkey'},
        {'name': 'Moscow ', 'country': ' Russia'},
        {'name': 'iStambul', 'country': 'tUrkey'},
        {'name': 'antalia', 'country': 'turkeY '},
        {'name': 'samarA', 'country': '  ruSsiA'}]

    expected = [{'russia': ['moscow', 'samara']},
                {'turkey': ['antalia', 'istambul']}]

    format(raw)