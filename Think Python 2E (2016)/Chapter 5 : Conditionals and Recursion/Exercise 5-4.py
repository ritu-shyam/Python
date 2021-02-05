# Exercise 5-4.
# What is the output of the following program? Draw a stack diagram that shows the state of the program when it prints the result.

def recurse(n, s):
  '''Takes in n and s , returns the value of s if n is equal to 0 otherwise it calls the function again'''
  if n == 0:
    print(s)
  else:
    recurse(n-1, n+s)
recurse(3, 0)

# output :
# 6

recurse(-1, 0)

# output :
# RecursionError: maximum recursion depth exceeded in comparison
print(recurse.__doc__)
