fav_food = input("Please type your favourite dishes")
fav_food2 = fav_food.split()
print(fav_food2)
index = 0

while index < len(fav_food2):
    print(f"{index}, {fav_food2[index]}")
    index += 1