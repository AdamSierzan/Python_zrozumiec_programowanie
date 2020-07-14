# Positional arguments

def add_two_nums(first_num, second_num):
    print(f"First num is {first_num}")
    print(f"Second num is {second_num}")
    return first_num+second_num

print(add_two_nums(2,3))
print(add_two_nums(3,2))

# It's okay when we don't have to worry about okay
# But sometimes we have to keep the order

def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage /100 ) **100
    return result

initial = 1000
percentage = 5
years = 4

final_value = calculate_investment_value(percentage,years,initial)
print(f"After {years} your investement will be worth {final_value:.2f}")

# As we can see, wrongly inserted values change the output completly

# To make it more readable we can call the value like this
final_value = calculate_investment_value(initial_value = 100,percentage = 5,years = 4)
print(f"After {years} your investement will be worth {final_value:.2f}")
# While doing it, we can choose the order of them

final_value = calculate_investment_value(years = 100,initial_value = 5,percentage = 4)
print(f"After {years} your investement will be worth {final_value:.2f}") 
