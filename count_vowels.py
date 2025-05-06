# I'm writing a function that, given a string, returns a dict 
# whose keys are the vowels (a, e, i, o, u) and whose values are
# integers, the number of times that each vowel appeared in 
# the string

def count_vowels(text):
    output = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for one_character in text:
        if one_character in output:
            output[one_character] += 1

    return output

    