# List Methods
fruits = ["apple", "banana", "cherry"]

# Append a new item to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Insert an item at a specific index
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

# Remove an item from the list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']

# Pop an item from the list
popped_fruit = fruits.pop(2)    
print(popped_fruit)  # Output: cherry
print(fruits)        # Output: ['apple', 'grape', 'orange']

# Clear all items from the list
fruits.clear()
print(fruits)  # Output: []

# List with mixed data types

my_list = ["Hello", 42, 3.14, True]
# Append a new item to the mixed list
my_list.append("New item")
print(my_list)  # Output: ['Hello', 42, 3.14, True, 'New item']

# List with nested lists

nested_list = [1, 2, [3, 4], 5]
# Append a new item to the nested list
nested_list.append(6)
print(nested_list)  # Output: [1, 2, [3, 4], 5, 6]
