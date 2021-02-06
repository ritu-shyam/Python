# Palindrome

word = input('Enter the word')

def first(word):
    return word[1]
def last(word):
    return word[-1]
def middle(word):
    return word[2:-1]

f = first(word)
l = last(word)
m = middle(word)
# to get the reverse of the middle string
r = m[::-1]

def is_palindrome(word):
    if f == l and m == r:
        return True
    else:
        return False

print(is_palindrome(word))
