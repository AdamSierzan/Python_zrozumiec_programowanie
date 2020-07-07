shopping_list = input("Please type the products on your shopping list, separate them with coma: ")
new_list = shopping_list.split()

print(f"This is a long list: {len(new_list) > 5}")