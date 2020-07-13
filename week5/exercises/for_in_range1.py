# Check the user's phone number to check many many times
# each digit apears in it

users_number = input("What's your number: ")

for digit in range(10):
    digit_times_in_num = users_number.count(str(digit))
    print(f"Number {digit} appears in your num {digit_times_in_num} times")
        