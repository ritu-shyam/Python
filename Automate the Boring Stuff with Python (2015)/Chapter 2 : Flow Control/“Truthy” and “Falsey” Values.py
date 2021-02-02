# When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True.
name = ''
# If the user enters a blank string for name, then the while statement’s condition will be True, and the program continues to ask for a name.
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
# If the value for numOfGuests is not 0 , then the condition is considered to be True, and the program will print a reminder for the user
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')
