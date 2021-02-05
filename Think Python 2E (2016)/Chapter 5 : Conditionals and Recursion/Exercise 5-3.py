# Triangle or not

def is_triangle(a, b, c) :
    if a+b > c and a+c > b and b+a > c :
        print('no')
    else :
        print('yes')

print('Enter the lengths :')
a = int(input())
b = int(input())
c = int(input())
is_triangle(a, b, c)
