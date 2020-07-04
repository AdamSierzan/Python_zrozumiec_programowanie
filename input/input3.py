starting_value_input  = input("Wpisz wartość początkową: ")
starting_value = int(starting_value_input)

rate_input = input("Wpisz stopę oprocentowania: ")
rate = float(rate_input)

time_input  = input("Wpisz czas trwania w latach: ")
time  = int(time_input)

after_x_years = starting_value * (1 + rate) ** time

print(after_x_years)
