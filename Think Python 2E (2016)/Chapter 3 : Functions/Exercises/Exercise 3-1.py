# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display:

def right_justify(s) :
    for i in range(1, 70 - len(s), 1):
      print(' ', end = '')
    print(s)

print('Enter the string:')
s = input()
right_justify(s)
