# Str have some methods from lists

name = "Adam"
print("First letter of my name is", name[0])
print("Last letter of my name is", name[-1])
print("My name without first letter is:", name[1:])

# We can't change the first element
# of the string by exchaning it like this:
# name[0] = "N"

# We have to do it like this
name = "N" + name[1:]
print(name)

# split method
words = "This is a whole sentence".split(" ")
print(words)
first_word