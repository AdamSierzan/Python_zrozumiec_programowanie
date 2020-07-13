# For in range 
# To write numbers one by one

for number in range(12):
    print(number)

# Starting with one to 12

for number in range(1,13):
    print(number)

# from one to 12 with step of 3

for number in range(1,13,3):
    print(number)

# Let's try to use loan calculator

initial_value_input = input("Your initial value? ")
initial_value = int(initial_value_input)
percentage_input = input("What's the intrest rate (%)? ")
percentage = int(percentage_input)
years_input = input("How many years you want to keep the money to invest? ")
years = int(years_input)

for year_number in range(1, years +1):
    investment_value = initial_value * (1 + percentage / 100) ** year_number
    print(f"After {year_number} years your investment will be worth {investment_value:.2f}")

# Count method returns number of appearance of the sign in str

sentence = "Sentence with a lot of aaa - sia laa laa"
print(sentence.count("a"))



