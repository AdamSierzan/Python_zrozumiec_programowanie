your_phone_num  = input("Type your phone number")
your_phone_num = your_phone_num.replace("-", "")
new_phone_number = ""
index = 0
while index < len(your_phone_num):
    if index % 3 == 0 and index != 0:
        new_phone_number += "-"
    new_phone_number += your_phone_num[index]
    index += 1
print(new_phone_number)