# 1. Type this example into a script and test it.
def do_twice(f):
  f()
  f()

def print_spam():
  print('spam')

do_twice(print_spam)

# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
value = 'spam'
def do_twice2(f, value):
  f(value)
  f(value)

def print_spam2(value):
  print(value)

do_twice2(print_spam2, value)

# 3. Copy the definition of print_twice from earlier in this chapter to your script.
def print_twice(bruce):
  print(bruce)
  print(bruce)

# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
do_twice2(print_spam2, value)

# 5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
def do_four(f, value):
  f(print_spam2, value)
  f(print_spam2, value)

do_four(do_twice2, value)
