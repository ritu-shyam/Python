# Square Root

def mysqrt(a) :
    while True :
        y = (x + a/x) / 2
        if y == x :
            return x
        x = y

def test_square_root() :
    a = 4.0
    print('a          mysqrt(a)         math.sqrt(a)          diff')
    print('-          --------          -----------           ----')
    
    while a < 10 :
        b = mysqrt(a)
        c = math.sqrt(a)
        d = abs(mysqrt(a)-math.sqrt(a)
        print(a,"          ",b,"         ",c,"          ",d)
        a = a + 1

test_sqrt_root()
