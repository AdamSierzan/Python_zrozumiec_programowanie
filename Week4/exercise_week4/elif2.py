# This program based on Cooper's test results will tell you
# if you're in good physical condition or not
# The test shows results for people in age between 20 and 29


gender = input("For women type ""W"" for men type ""M"": ")
if gender == "W":
    distance = int(input("How much meters you can run in 12 minutes? "))
    if distance <= 1500:
        print("You're in very bad condition")
    elif 1500 < distance <=1799:
        print("You're in bad condtiion") 
    elif 1800 < distance <= 2199:
        print("You're in mediocre condtition")
    elif 2200 < distance <= 2700:
        print("You're in good condition")
    else:
        print("You're in great condition")
if gender == "M":
    distance = int(input("How much meters you can run in 12 minutes? "))
    if distance <= 1600:
        print("You're in very bad condition")
    elif 1600 < distance <=2199:
        print("You're in bad condtiion") 
    elif 2200 < distance <= 2399:
        print("You're in mediocre condtition")
    elif 2400 < distance <= 2800:
        print("You're in good condition")
    else:
        print("You're in great condition")
else:
    print("Seems you did something wrong")