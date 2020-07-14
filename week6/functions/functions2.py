def put_a_brick():
    print("-", sep="", end="")

# function can call out ohter function

def build_a_wall():
    wall_lenght = 10
    for brick in range(wall_lenght):
        put_a_brick()
    print() 

build_a_wall()

def build_longer_wall():
    longer_wall_lenght = 30
    for brick in range(longer_wall_lenght):
        put_a_brick()
    print()

build_longer_wall()

# To avoid copying the code, we can use 
# function parameters(arguments). They are 
#  dispalyed as variables

# *parameters are defiended in function
# *values in function are arguments

def function_with_params(something, something_else):
    print(something)
    print(something_else)



# We can use any values with the arguments

function_with_params(1,4)
function_with_params("whatever", 4)

list_example = ["A", "list", "with", "elements"]
dict_example = {"Key": "value"}
function_with_params(list_example, dict_example)


# When the procedule of builind is the same, and we only want to 
# change one variable, we can make it as parameter


def build_a_wall_2(wall_lenght_2):
    for brick in range(wall_lenght_2):
        put_a_brick()
    print()
    
build_a_wall_2(21)