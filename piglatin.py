def pl_word(text):
    if text[0] in 'aeiou':
        return text + 'way'
    else:
        return text[1:] + text[0] + 'ay'

for one_word in ['computer', 'apple', 'papaya', 'elephant']:
    print(f'{one_word}: {pl_word(one_word)}')


def pl_sentence(text):
    output = []

    for one_word in text.split():
        output.append(pl_word(one_word))

    if text[0] in 'aeiou':
        return text + 'way'
    else:
        return text[1:] + text[0] + 'ay'

for one_word in ['computer', 'apple', 'papaya', 'elephant']:
    print(f'{one_word}: {pl_word(one_word)}')
    