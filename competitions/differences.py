def gen_diff(dfirst, dsecond):
    result = {}  # dfirst.update(dsecond)
    print(dfirst)
    print(dsecond)
    for key in dfirst.keys():
        result[key] = 'deleted'
    for key in dsecond.keys():
        if key in dfirst:
            if dfirst[key] == dsecond[key]:
                result[key] = 'unchanged'
            else:
                result[key] = 'changed'
        else:
            result[key] = 'added'
    print (result)


if __name__ == "__main__":
    df = {"one": "eon", "two": "two", "four": True}
    ds = {"two": "own", "zero": 4, "four": True}
    gen_diff(df, ds)