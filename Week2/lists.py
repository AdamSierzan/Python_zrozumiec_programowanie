shopping_list = [
    "bread",    
    "flour",    
    "apples",   
    "naranjas"
    
]

print("Shopping list:", shopping_list)

# We can always make a list of lists and mix
# different types of variables

mixed = [
    "title",
    100,
    120.5,
    ["element", "element2"]


]

print("Mixed list", mixed)


# WE can Index the lists

print(f"Lenght of the list {len(shopping_list)}")
print(shopping_list[:2]
)
print(shopping_list[2:])
print(shopping_list[-2:])

# Adding elements to the list

shopping_list.append("tofu")
print(shopping_list)

# Adding element to the exact position
shopping_list.insert(0, "nuts")
print(shopping_list)

# deleting elements 
del shopping_list[2]
print(shopping_list)

# Draging out the element from the list
to_eat = shopping_list.pop(1)
print(to_eat)
print(shopping_list)

# deleting the element by its value
shopping_list.remove("tofu")
print(shopping_list)

# exchanging the elements 
shopping_list[-1] = "tofu"
print(shopping_list)

