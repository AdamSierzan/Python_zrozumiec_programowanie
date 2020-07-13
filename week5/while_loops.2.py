# summing numbers

numbers = [1,4,5,12,54,12]
number_sum = 0
number_index = 0
while number_index < len(numbers):
    number_sum += numbers[number_index]
    number_index +=1
print(f"Sum of these numbers is {number_sum}")


# printing zip code number by number

zip_code = input("What's your zip code")
letter_index = 0
while letter_index < len(zip_code):

    print(f"{letter_index} ->> {zip_code[letter_index]}")
    letter_index+=1

# Changing the zip code so it's always in correct form (xx-xx-xx-xx...)

zip_code = input("What's your zip code")
zip_code = zip_code.replace("-", "")
formatted_zip_code = ""
letter_index = 0
while letter_index < len(zip_code):
    if letter_index % 2 == 0 and letter_index != 0:
        formatted_zip_code += "-"
    formatted_zip_code += zip_code[letter_index]
    letter_index += 1
print(formatted_zip_code)