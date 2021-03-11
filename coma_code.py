def list_thing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])


lit = ['banana', 'apple', 'oragne']
print(list_thing(lit))