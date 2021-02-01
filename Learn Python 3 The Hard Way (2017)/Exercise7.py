print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# The end parameter is used to append any string at the end of the output of the print statement in python.
# By default, the print method ends with a newline. This means there is no need to explicitly specify the parameter end as '\n'.
# Syntax : print(variable1, end = 'type whatever character you want to append to the next print statement')
print(end7 + end8 + end9 + end10 + end11 + end12)
