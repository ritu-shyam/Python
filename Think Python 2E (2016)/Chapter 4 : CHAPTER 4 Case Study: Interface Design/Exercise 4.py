# 4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle by calling polygon with an appropriate length and number of sides.
# Test your function with a range of values of r.
# Figure out the circumference of the circle and make sure that length * n = circumference.

import turtle
bob = turtle.Turtle()

def circle(t, length, n) :
    for i in range(n) :
        t.fd(length)
        t.lt(360/n)

import math
def calculate(t, r):
        circum = 2*math.pi*r
        n = int(circum/10)+1
        length = circum/n
        circle(t, length, n)

r = int(input('Enter the value of radius'))
calculate(bob, r)

