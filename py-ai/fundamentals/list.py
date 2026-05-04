# List 

favorite_foods = ["pizza", "sushi", "ice cream", "tacos"]

print(favorite_foods[0])  # Output: pizza
print(favorite_foods[1])  # Output: sushi
print(favorite_foods[2])  # Output: ice cream

# List with mixed data types
my_list = ["Hello", 42, 3.14, True]
print(my_list[0])  # Output: Hello
print(my_list[1])  # Output: 42
print(my_list[2])  # Output: 3.14

# List with nested lists
nested_list = [1, 2, [3, 4], 5]
print(nested_list[2])  # Output: [3, 4]
print(nested_list[2][0])  # Output: 3
print(nested_list[2][1])  # Output: 4

# List slicing
print(favorite_foods[1:3])  # Output: ['sushi', 'ice cream']
print(favorite_foods[:2])   # Output: ['pizza', 'sushi']
print(favorite_foods[2:4])  # Output: ['ice cream', 'tacos']
