# Using f strings
# F string will convert out variable into str type

python_age = 30
info = f"Python ma już prawie {python_age} lat!"

print(info)

# We can also use it like that

calculation = f"Wynik działania 3x4 to {3 * 4}"

print(calculation)

# While working with a decimal points, we can
# simply cut the decimat points we dont want

distance  = 35
time  = 3
speed = distance / time
print(f"Runner runs with the avg speed: {speed:.2f} km/h")

# Cheking the lenght of the string

your_street = input("What's the name of your street: ")

print(f"The name of your street has: {len(your_street)} letters")

# 
name = input("What's your name")
print(f"Your name is: {name.title()}")

# Replace method

phone_number_with_space  = "123 333 444"
phone_number_with_dash  = phone_number_with_space.replace(" ", "-")
print(phone_number_with_dash)

phone_num = "(58)123444"
phone_num = phone_num.replace('(', '')
phone_num = phone_num.replace(')', "")
print(phone_num)