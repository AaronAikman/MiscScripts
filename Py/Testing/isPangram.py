import string


def is_pangram(str1, alphabet=string.ascii_lowercase):
    str1 = set(str1.lower())
    str1.remove(' ')
    return set(alphabet) == str1


qbf = 'The quick brown fox jumps over the lazy dog'
qbf2 = 'The quick brown fox jumps over thh lazy dog'
nap = 'This is not a pangram'
print is_pangram(qbf)
# print is_pangram(nap)
