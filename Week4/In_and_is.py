# in operator tells us if the element we're investigating is contained in sstring
name  = "Adam"
if "a" in name:
    print("Your name contains ""a""")
else:
    print("Your name doesn't contain ""a""")

# We can check the list for the searched phrase

favourite_sports = ["basketball", "football", "hokey"]
if "basketball" in favourite_sports:
    print("Basketball is on your list")

# And we can also check the dict

person = {
    "first_name": "Adam",
    "last_name": "Sierzan"
}

if "first_name" in person:
    print(person["first_name"])

if "car" in person:
    print(person["car"])

# It also works with negation

favourite_sports = ["basketball", "football", "hokey"]
if  "golf" not in favourite_sports:
    print("Golf is not on your list")

#  Is operator

age = 35

if age:
    print("if age")

if age == True:
    print("age==True")

if age is True:
    print("if age is True")

true_value = True
if true_value is True:
    print("if true_value is True ")   

# None with is operator

nothing = None
if not nothing:
    print("if not nothing")

zero = 0
if not zero:
    print("if not zero")

if zero is None:
    print("if zero is None")

if zero is not None:
    print("if zero is not None")

if nothing is not None:
    print("if nothing is None")





