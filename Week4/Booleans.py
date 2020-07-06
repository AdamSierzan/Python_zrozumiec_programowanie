apple_price = 3
bananas_price = 4.5
pears_price = 3

print(f"Are bananas more expensive than pears {bananas_price > pears_price}")

# Booleans can have "true" or "false" value

print(f"{True} is a type {type(True)}")

# We can also change variables into booleans

result = bool(7)
print(f"bool(7) -> {result}")

result = bool(0)
print(f"bool(0) -> {result}")

result = bool("")
print(f"bool('') -> {result}")

result = bool(None)
print(f"bool(None) -> {result}")

result = bool([])
print(f"bool([]) -> {result}")

# numbers are True, except for 0
# None, empty lists, empty string are False

# We can compare two strings
name = "Adam"
result = name == "Adam"
print(f"name == 'Adam' --> {result}")

your_name  = input("Type your name: ")
are_you_Adam = your_name == "Adam"
print(f"Are you Adam? {are_you_Adam}")

# When you compare two strings, python will check the alphabetical order of them,
# and mark the one with the letters from the beggining of the alphabet as
# smaller

# You cant compare integers with strings etc