# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b.

print('Enter 2 numbers :')
a = int(input())
b = int(input())

def is_power(a, b) :
    if a % b == 0 and ((a/b) % b == 0)  :
        return True
    else :
        return False

print(is_power(a, b))
