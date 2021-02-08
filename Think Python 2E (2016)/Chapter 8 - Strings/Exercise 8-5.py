# Caeser cypher

def rotate_letter(letter, n) :
  if letter.isupper() :
    value = ord('A')
  elif letter.islower() :
    value = ord('a')
  else :
    return letter
  diff = ord(letter) - value
  num = (diff + n) % 26 + value
  return chr(num)

def rotate_word(s, n) :
  result = ''
  for letter in s :
    result = result + rotate_letter(letter, n)
  return result

s = input('Enter the string :\n')
n = int(input('Enter the rotation number :\n'))
print(rotate_word(s, n))
