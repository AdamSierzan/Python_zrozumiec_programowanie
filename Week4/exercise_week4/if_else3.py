history = float(input("Type your history mark: "))
physics = float(input("Type your physics mark: "))
math = float(input("Type your math mark: "))


number_of_failures = 0

if history < 2:
    number_of_failures+=1
if physics < 2:
    number_of_failures+=1
if math < 2:
    number_of_failures+=1

if number_of_failures == 0:
    print("You've passed ")

if number_of_failures == 1:
    if (history+physics+math)/3 > 3.5:
        print("You've passed")
    else:
        print("You've failed")
if number_of_failures > 1:
    print("You've failed")