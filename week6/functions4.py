# Instead of creating another funcition, as in previos lesson, it's better to return 
# the value from the funcion, and then create two variables, which will be 
#  used to solve the problem

def calculate_investment_value(initial_value, percentage, years):

    return initial_value * (1 + percentage / 100) ** years


print("Investment calculator")

initial_value_input = input("What's the initial value? ")
initial_value = int(initial_value_input)
percentage_input = input("What's the percentage rate (%)? ")
percentage = int(percentage_input)
years_input = input("How many years will be be investing? ")
years = int(years_input)


final_value = calculate_investment_value(initial_value, percentage, years)
print(f"After {years} years your investment will be equal to {final_value:.2f}")

longer_term = years * 2
alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
print(f"Consider leaving the investment for {years} years - it will be worth {alternative_value:.2f}")


def say_hello():
    print("Hello World!")


hello_result = say_hello()
print(hello_result)