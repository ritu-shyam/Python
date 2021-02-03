# The collatz sequence function
def collatz(number) :
  
  # if the number is even
  if number % 2 == 0 :
    return number // 2
  
  # if the number is odd
  else :
    return 3 * number + 1

try :
    print('Enter number:')
    number = int(input())
    if number == 1 :
        print(number)
    while number != 1 :
        number = collatz(number)
        print(number)
       
except :
    print('Enter an integer value for number.')
