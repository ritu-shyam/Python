# 2. Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a second argument.
# Run the program again. Test your program with a range of values for length.

import turtle
def square(t, length) :

    for i in range(4) :
        t.fd(length)
        t.lt(90)

bob = turtle.Turtle()
length = int(input('Enter the length'))
square(bob, length)
