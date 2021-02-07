# Square Root

import math
def mysqrt(a) :
    x = a/5
    while True :
        y = (x + a/x) / 2
        if y == x :
            return x
        x = y

def test_square_root() :
    a = 1.0
    print('a          mysqrt(a)         math.sqrt(a)          diff')
    print('-          --------          -----------           ----')
    
    while a < 10 :
        b = mysqrt(a)
        c = math.sqrt(a)
        d = abs(b - c)
        print("{0:.4f}".format(a), "   ", "{0:.4f}".format(b), "          ", "{0:.4f}".format(c), "              ", d)
        a = a + 1

test_square_root()
