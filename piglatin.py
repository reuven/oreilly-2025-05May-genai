def pl_word(text):
    if text[0] in 'aeiou':
        return text + 'way'
    else:
        return text[1:] + text[0] + 'ay'

        