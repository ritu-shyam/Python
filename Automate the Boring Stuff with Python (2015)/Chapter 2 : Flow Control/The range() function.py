# This is why range(5) results in five iterations through the clause, with i being set to 0, then 1, then 2, then 3, and then 4. The variable i will go up to, but will not include, the integer passed to range().
print('My name is')
for i in range(5):
  print('Ritu ' + str(i))

# The first argument will be where the for loop’s variable starts, and the second argument will be up to, but not including, the number to stop at.
for i in range(0, 5):
  print(i)

# The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.
for i in range(0, 5, 1):
  print(i)
