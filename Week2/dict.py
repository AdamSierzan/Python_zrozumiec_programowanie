polish_to_english = {
    "amnezja": "amnesia",
    "aktywista": "activist",
    "burza": "storm"
}

# We get the acces to the dict, by its key
print(polish_to_english)
print(f"Po polsku 'burza' to po angielsku '{polish_to_english['burza']}'")


# Empty dict

empty = {}
print("Pusty słownik", empty)

# Values can be with of different types\
# It's good to make one-element-type lists, so if we make
# a dictionarie with a list inside it, we should put all the 
# values in lists
 
expenditures = {
     "electricity": [205],
     "water": [30.3],
     "shopping": [120.5, 304, 20.13
     ]
 }

print(expenditures)

# Int and float can be a key as well

expenditures_2 = {
    240: "water",
    100: "electricity",
    120: "shopping",
    203: "shopping"
}

print(expenditures_2)

# We have to remember that keys have to be unique


# Dictionaries can contain other dictionaries inside 


employee = {
    "first name": "Jan",
    "last name": "Kowalski",
    "age": 32,
    "contract": {
        "sign_date": "23-11-2019",
        "salary": 2500
    }
}

print(employee)

# Dictionarie can contain a list, and a list can contain a dictionarie.

students = [
    {
        "first_name": "Patryk",
        "last_name":  "Nowak",
    },
    {
        "first_name": "Alicja",
        "last_name":  "Kowalska"
    }
]
 
print(students)
print(students[0])
print(students[1])
print(students[1]['first_name'])

# We can always modify the dictionaries

employee_2 = {
    "first name": "Jan",
    "last name": "Kowalski",
    "age": 32,
    "contract": {
        "sign_date": "23-11-2019",
        "salary": 2500
    }
}
print(employee_2)

employee_2["first name"] = "Albert"

print(employee_2)

# We can add new key to the dict

employee_2["city"] = "Gdańsk"
print(employee_2)

# We can delete the key

del employee_2["last name"]
print(employee_2)


# dragging out the element out of the dict.
age = employee_2.pop("age")
print(age)
print(employee_2)

# Keys and values methods to return special types objects

print(employee_2.keys())
print(employee_2.values()
)

# We can always change then into list type ojects
keys = list(employee_2.keys())
print(keys)

value = list(employee_2.values())
print(value)

# Len function returs a num of elements (keys) in the dict
print(len(employee_2))
