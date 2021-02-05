# Fermat’s Last Theorem

import math

def check_fermat(a, b, c, n) :
    lhs = math.pow(a, n) + math.pow(b, n)
    rhs = math.pow(c, n)
    if n > 2 and (lhs == rhs) :
          print('Holy smokes, Fermat was wrong!')
    else :
          print('No, that doesn’t work.')

print('Enter values of a b c and n')
a = int(input())
b = int(input())
c = int(input())
n = int(input())
check_fermat(a, b, c, n)
