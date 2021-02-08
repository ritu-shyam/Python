# String Methods

# 1 str.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercased.
str = ritu
s_1 = str.capitalize()
print(s1)

# 2 str.casefold()
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string.
# For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".
str = rituß
s_2 = str.casefold()
print(s_2)
