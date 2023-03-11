def anagram(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False


def capitalize_anagram(first_word, second_word):
    result = anagram(first_word, second_word)
    if result is True:
        return first_word.upper(), second_word.upper()
    else:
        return first_word, second_word


a ="oow"
b ="woo"
c = "hello"
d = "ehlol"
print(anagram(a, b))
print(capitalize_anagram(c, d))
