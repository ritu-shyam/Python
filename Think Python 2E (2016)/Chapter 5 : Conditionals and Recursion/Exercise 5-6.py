# The Koch curve

import turtle
t = turtle.Turtle()
print('Enter the length:')
x = int(input())

# 1. Write a function called koch that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.
def koch(t, x) :
  if x > 3 :
    # 1. Draw a Koch curve with length x/3.
    koch(t,x/3)
    # 2. Turn left 60 degrees.
    t.lt(60)
    # 3. Draw a Koch curve with length x/3.
    koch(t,x/3)
    # 4. Turn right 120 degrees.
    t.rt(120)
    # 5. Draw a Koch curve with length x/3.
    koch(t,x/3)
    # 6. Turn left 60 degrees.
    t.lt(60)
    # 7. Draw a Koch curve with length x/3.
    koch(t,x/3)
  else :
    t.fd(x)

koch(t, x)

# 2. Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.
def snowflake(t,x) :
  for i in range(3) :
    koch(t, x)
    t.rt(120)

snowflake()
