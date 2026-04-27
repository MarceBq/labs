# Lops
favorite_fruits = ["apple", "banana", "cherry", "date"]

# Loop through the list and print each fruit
for fruit in favorite_fruits:
    print(fruit)
    
# Loop through the list with index
for index, fruit in enumerate(favorite_fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Loop through the list in reverse
for fruit in reversed(favorite_fruits):
    print(fruit)
    
# Loop through the list with a while loop
index = 0
while index < len(favorite_fruits):
    print(favorite_fruits[index])
    index += 1

# Loop through the list and print fruits that start with 'b'
for fruit in favorite_fruits:
    if fruit.startswith('b'):
        print(fruit)
        
# Loop through the list and print fruits in uppercase
for fruit in favorite_fruits:
    print(fruit.upper())
    
# Loop through the list and print the length of each fruit
for fruit in favorite_fruits:
    print(f"{fruit}: {len(fruit)} characters")

# Loop through the list and print fruits that contain the letter 'a'
for fruit in favorite_fruits:
    if 'a' in fruit:
        print(fruit)
        
# Loop through the list and print fruits that are longer than 5 characters
for fruit in favorite_fruits:
    if len(fruit) > 5:
        print(fruit)

# Loop through the list and print fruits that are shorter than 6 characters
for fruit in favorite_fruits:
    if len(fruit) < 6:
        print(fruit)

# Loop through the list and print fruits that contain the letter 'e'
for fruit in favorite_fruits:
    if 'e' in fruit:
        print(fruit)

# Loop through the list and print fruits that do not contain the letter 'a'
for fruit in favorite_fruits:
    if 'a' not in fruit:
        print(fruit)
        
# Loop through the list and print fruits that start with 'c'
for fruit in favorite_fruits:
    if fruit.startswith('c'):
        print(fruit)
