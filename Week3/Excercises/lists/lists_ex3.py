your_num = input("Please type your number")
your_num.replace("-","")
print(your_num)
public_digits  = your_num[:6]
number_of_private_digits = len(your_num ) - 6 
private_digits = "-" * number_of_private_digits
coded_number = f"{public_digits}{private_digits}"

print("YOUR CODED NUMBER IS:", coded_number)