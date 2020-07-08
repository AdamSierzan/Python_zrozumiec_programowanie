first_product = input("How much does the cheese cost? ")
second_product = input("How much does the onion cost? ")
third_product = input("How much does the potato cost? ")

if first_product > second_product:
    print(f"Onion is cheaper than cheese")
else:
    print(f"Onion is more expensive than cheese")
if first_product > third_product:
    print(f"Potato is cheaper than cheese")
else:
    print(f"Potato is more expensive than cheese")
if first_product == second_product:
    print(f"Onion has the same price as cheese ")
if first_product == third_product:
    print(f"Potato has the same price as cheese")
if third_product == second_product:
    print(f"Potato has the same price oniion")
