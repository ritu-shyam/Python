# 3. Make a copy of square and change the name to polygon.
# Add another parameter named n and modify the body so it draws an n-sided regular polygon.
# The exterior angles of an n-sided regular polygon are 360/n degrees.

import turtle
def polygon(t, length, n) :

    for i in range(n) :
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()
length = int(input('Enter the length'))
n = int(input('Enter the number of sides of a polygon'))
polygon(bob, length, n)
