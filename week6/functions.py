# function is a type of instruction for a program, it tell it what should it do

# peeling the potatoes, definition of function
def peel_the_potatoes():
    expected_potatoes = int(input(("how many potatoes you want")))
    potatoes = []
    while len(potatoes) < expected_potatoes:
        print("Peeling the potatoe")
        print("Putting the potatoe to the pot")
        potatoes.append("Ziemniak")
    print(potatoes)

# callinf out the function

peel_the_potatoes()
peel_the_potatoes()
peel_the_potatoes()

def make_soup():
    print("It's soup!")

make_soup()

# We can call the function whenever we want
# without duplicating the code