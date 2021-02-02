# The argv is the argument variable
# This variable holds the arguments you pass to your Python script when you run it.
# Use customised run and give the arguments to run this program

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
