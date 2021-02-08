# The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong.
# For each function, describe what the function actually does (assuming that the parameter is a string).

def any_lowercase1(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False
# This is wrong because it checks only for the first character of the string s

def any_lowercase2(s):
  for c in s:
    if 'c'.islower():
      return 'True'
    else:
      return 'False'
# This is wrong because it checks for the character 'c'

def any_lowercase3(s):
  for c in s:
    flag = c.islower()
  return flag
# This is wrong because it checks only for the last character of the string s

def any_lowercase4(s):
  flag = False
  for c in s:
    flag = flag or c.islower()
  return flag
# This is correct

def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
  return True
# This is wrong because it checks only for the first character of the string s and returns the opposite of what is intended

s = "RiTu"
a = any_lowercase1(s)
b = any_lowercase2(s)
c = any_lowercase3(s)
d = any_lowercase4(s)
e = any_lowercase5(s)
print(a)
print(b)
print(c)
print(d)
print(e)
