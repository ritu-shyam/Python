# Comma Code
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
# spam = ['apples', 'bananas', 'tofu', 'cats']
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

list1 = []
while True:
    print('Enter the element ' + str(len(list1) + 1) +' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    else:
        list1 = list1 + [name]


def convert(list1) :
  s = ''
  for i in range(len(list1)-1) :
    s = s + list1[i] + ', '
  s = s + 'and ' + list1[i+1]
  print(s)

convert(list1)
