# pi

import math
def estimate_pi() :
    b = 0
    k = 0
    a = (2*math.sqrt(2))/9801
    while k < 1e-15 :
        b = b + (math.factorial(4*k) * (1103+ (26390*k)))/(math.pow(math.factorial(k),4) * math.pow(396,4*k))
        k = k + 1
    est = a*b
    res = 1/math.pi
    print('Estimated value : ', est)
    print('Actual value :', res)

estimate_pi()
