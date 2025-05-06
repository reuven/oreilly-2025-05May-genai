def pl_word(text):
    if text[0] in 'aeiou':
        return text + 'way'
    else:
        return text[1:] + text[0] + 'ay'

for one_word in ['computer', 'apple', 'papaya', 'elephant']:
    print(f'{one_word}: {pl_word(one_word)}')
    