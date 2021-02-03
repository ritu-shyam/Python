# 5. Make a more general version of circle called arc that takes an additional parameter angle, which determines what fraction of a circle to draw.
# Angle is in units of degrees, so when angle=360, arc should draw a complete circle.

import turtle
bob=turtle.Turtle()
import math
def arc(t,radius,angle):
    circumference = 2.0*math.pi*radius
    frac = angle/360.0
    arclength = circumference*frac
    n = 50 # pick a number
    len = arclength/n;
    turnang = angle/n
    for i in range(n):
        t.fd(len)
        t.lt(turnang)
        
arc(bob, 130,60)
