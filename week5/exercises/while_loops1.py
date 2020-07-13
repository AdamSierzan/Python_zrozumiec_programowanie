counter = 0
while counter < 10:
    user_num = int(input("Try to guess my number: "))
    
    if user_num % 2 == 0:
        counter += 10
        print("That's the number!")

    else:
        print("That's not the number")
        counter+=1
