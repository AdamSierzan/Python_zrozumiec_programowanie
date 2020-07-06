# with None we can express "nothing"
# None value can be assigned to the variable

nothing = None
print(f"Nic: {nothing}")

# None has NoneType
print(f"None is a: {type(None)}")

# None can be used as a value in dict

people = [
    {
        "first_name": "Alicja",
        "car": {
            "brand": "Ford",
            "production_year": 2012
        }
    },
    {
        "first_name": "Adam",
        "car": None
    }
]

print(people)

# We can also use None as an element on the list

random_list = [1,2,3, None,5]
print(random_list)

# We cant make aritmetic operations, or join them with a str or int

# We cant change None it for int or float

# We can convert it into string
none_str = str(None)
print("abc" + none_str)