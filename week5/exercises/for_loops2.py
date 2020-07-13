your_phone_num  = input("Type your phone number: ")
your_phone_num = your_phone_num.replace("-", "")
new_phone_number = ""
for index, num in enumerate(your_phone_num):
    if index % 3 == 0 and index != 0:
        new_phone_number += "-"
    new_phone_number += num
print(new_phone_number)