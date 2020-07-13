expenditures = {
    "electricity": [250],
    "water": [30.45],
    "shopping": [
        120.15,
        170.53,
        20.15
    ]
}
# keys
for expenditure_name in expenditures:
    print(expenditure_name)

# keys and values
for expenditure_name in expenditures:
    print(f"{expenditure_name} -> {expenditures[expenditure_name]}")

# Values
for expenditure in expenditures.values():
    print(expenditure)

# Keys and values alternative way, items() return tuples, with key and value
for expenditure_name, expenditure in expenditures.items():
     print(f"{expenditure_name} -> {expenditure}")

# for item in expenditures.items():
    # print(item)
    # print(f"{item[0]} -> {item[1]}")
    # print(type(item))

# tuple unpacking

bill =("electricity", "340")
name, value  = bill
print(name, value)

# Using enumarate function to write every character with an index but without using
# counter

post_code = input("What's your zip code? ")
for index, letter in enumerate(post_code):
    print(f"[{index}] -> {letter}")

# Taking every second sport
favourite_sports = ["running", "swimmming", "biking", "triathlon"]
for index, sport in enumerate(favourite_sports):
        if index % 2 == 0:
            print(sport)

# Changing the zip code so it fits the  XX-XX-XX-XX...format
post_code = input("what's your zip code? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
for index, letter in enumerate(post_code):
    if index % 2 == 0 and index != 0:
        formatted_post_code += "-"
    formatted_post_code += letter
print(formatted_post_code)