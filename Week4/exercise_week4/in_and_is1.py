shopping_list = input("Please type the products on your shopping list, separate them with coma: ")
new_list = shopping_list.split()

if len(new_list) > 5:
    print(f"This is a long list")
else:
    print(f"This is not a long list")

if "buns" in shopping_list:
    print("buns are on your list") 

if "bread" in shopping_list:
    print("buns are on your list") 