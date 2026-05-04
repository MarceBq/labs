# Functions

# Count - counts the number of items in a collection or the number of characters in a string

print(len("Hello, World!"))  # Output: 13

# Round - rounds a number to a specified number of decimal places

print(round(3.14159, 2))  # Output: 3.14

# Type - returns the type of an object

string_length = "Hello, World!"
print(len(string_length))  # Output: <class 'str'>

# Function definition

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Function with default parameter
def greet(name="World"):
    return f"Hello, {name}!"    

print(greet())  # Output: Hello, World!
print(greet("Bob"))  # Output: Hello, Bob!

