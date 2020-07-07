first_product = input("How much does the cheese cost? ")
second_product = input("How much does the onion cost? ")
third_product = input("How much does the potato cost? ")

print(f"Onion is cheaper than cheese {first_product > second_product}")
print(f"Potato is cheaper than cheese {first_product > third_product}")
print(f"Onion is cheaper than potato  {third_product > second_product}")

print(f"Onion has the same price as cheese {first_product == second_product}")
print(f"Potato has the same price cheese {first_product == third_product}")
print(f"Onion has the same price potato  {third_product == second_product}")



