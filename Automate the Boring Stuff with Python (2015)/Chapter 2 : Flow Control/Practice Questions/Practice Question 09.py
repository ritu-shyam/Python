# 09. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

print('Enter the value of spam')
spam = int(input())
if spam == 1:
  print('Hello')
elif spam == 2:
  print('Howdy')
else:
  print('Greetings!')
