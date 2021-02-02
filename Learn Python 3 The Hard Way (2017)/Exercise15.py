from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


# 1. take the filename
# 2. open the file and store it in a variable
# 3. read the variable
print('Enter filename')
file = input()
text = open(file)
print(text.read())
