def add_name(string, tags, tag):
    string = '<' + tags[tag] + '>'
    return string


def add_closed(string, tags, tag):
    if tags[tag] == 'pair':
        string = string + '</' + tags['name'] + '>'
    return string


def add_body(string, tags, tag):
    index = string.find('>')
    string = string[:index+1] + tags[tag] + string[index+1:]
    return string


def add_others(string, tags, tag):
    index = string.find('>')
    string = f'{string[:index]} {tag}="{tags[tag]}"{string[index:]}'
    return string


attr = {
    'name': add_name,
    'body': add_body,
    'tag_type': add_closed
}


def stringify(tags):
    result = ''
    for tag in tags.keys():
        func = attr.get(tag, add_others)
        result = func(result, tags, tag)
    print('my res =', result)
    return result


if __name__ == '__main__':
    hr_tag = {
    'name': 'hr',
    'class': 'px-3',
    'id': 'myid',
    'tag_type': 'single',
    }
    stringify(hr_tag) ## <hr class="px-3" id="myid">

    div_tag = {
    'name': 'div',
    'tag_type': 'pair',
    'body': 'text2',
    'id': 'wow',
    }
    stringify(div_tag) ## <div id="wow">text2</div>

    empty_div_tag = {
    'name': 'div',
    'tag_type': 'pair',
    'body': '',
    'id': 'empty',
    }
    stringify(empty_div_tag) ## <div id="empty"></div>
