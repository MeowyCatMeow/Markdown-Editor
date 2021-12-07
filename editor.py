"""mark down editor
https://hyperskill.org/projects/162/stages/843/implement
https://imgur.com/a/GCEaUwB
"""

whole_text = []


def get_text():
    return input('Text:')


def plain():
    return get_text()


def new_line():
    return '\n'


def bold():
    return f'**{get_text()}**'


def italic():
    return f'*{get_text()}*'


def header():
    level = 0
    while level < 1 or level > 6:
        print('The level should be within the range of 1 to 6')
        level = int(input("Level: "))
    text = get_text()
    return f'{level * "#"} {text}\n'


def link():
    label = input('Label: ')
    url = input('URL:')
    return f'[{label}]({url})'


def inline_code():
    return f'`{get_text()}`'


def unordered_list(ordered=False):
    row_num = 0
    rows = []
    while row_num < 1:
        row_num = int(input('Number of rows:'))
        if row_num < 1:
            print("The number of rows should be greater than zero")
    for x in range(1, row_num + 1):
        row = input(f'Row #{x}:')
        if ordered:
            rows.append(f'{x}. {row}\n')
        else:
            rows.append(f'* {row}\n')
    return ''.join(rows)


def ordered_list():
    return unordered_list(ordered=True)


def done():
    with open('output.md', 'w') as _file:
        for x in whole_text:
            _file.write(x)


formatters = {"plain": plain,
              "bold": bold,
              "italic": italic,
              "link": link,
              "inline-code": inline_code,
              "new-line": new_line,
              "header": header,
              "unordered-list": unordered_list,
              "ordered-list": ordered_list}

while True:
    _input = input('Choose a formatter: ')
    if _input == '!done':
        done()
        break
    elif _input == '!help':
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')
    elif _input in formatters:
        whole_text.append(formatters[_input]())  # Instead of use function actions use this
        print(*whole_text, sep='')
    else:
        print('Unknown formatting type or command')
