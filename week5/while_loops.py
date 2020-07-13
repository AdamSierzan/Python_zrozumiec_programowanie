# We use while loops to tell python how many times,
# we want him to keep on repeating same action

# Keep on generating the numbers until we'll hit 30

counter = 0 
while counter <= 30:
    print(counter)
    counter+=1
    

# while True keeps the python going on and on

# while True:
    # print("I will never stop")

expected_potatoes = int(input("How many potatoes you need"))

potatoes = []

while len(potatoes) < expected_potatoes:
    print("I peel the potato")
    print("I put the potato into the pot ")
    potatoes.append("Ziemniak")
print(potatoes)





# We want the user to type number higher than 100

num = 0
while num <= 100:
    num = int(input("Type the number higher than 100"))
    if num <= 100:
        print(f"Your number {num} is not higher than 100")
print(f"Nice!")


# We want to make sure that the user typed right number

age = int(input("How old are you"))
while age <1:
    if age <1:
        print("I don't think so...\n")
        age = int(input("How old are you"))
if age < 18:
    print("You can't vote")
else:
    print("You can vote")

# While loops are very useful when we want the user to use the 
# programe few times

option = "T" 
while option == "T":
    income  = int(input("How much you earn"))
    employees_number = int(input("How many employees you hire"))
    years_on_the_market = int(input("How many years you're on the market"))
    if income < 2000:
        print("You can get a support")
    elif 5 <= employees_number <= 10:
        print("You can get an employee support")
    elif years_on_the_market < 3:
        print("You can get a new firm suport")
    else:
        print("You won't get a support")
    option = input("If you want to check data for other firms type ""T""")

# printing things from the list

favourite_sports = ["walking", "running", "swimming", "tennis"]
sport_index = 0
while sport_index < len(favourite_sports):
    print(favourite_sports[sport_index])
    sport_index +=1

