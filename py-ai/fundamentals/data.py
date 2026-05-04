# Strings 

print("'Hello, World!'")

# String Concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# String Formatting
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)

# Numbers
x = 10
y = 5

# Arithmetic Operations
sum_result = x + y
difference = x - y
product = x * y
quotient = x / y
elevation = x ** y
raised_to_power = pow(x, y)
getting_remainder = x % y

# Truncating the quotient to an integer using int()
quotient_int = int(quotient)

# Truncating the quotient to an integer using floor division
quotient_floor = x // y

# Truncanting using f strings
quotient_f_string = f"{quotient:.0f}"

print(f"Sum: {sum_result}, Difference: {difference}, Product: {product}, Quotient: {quotient}, Elevation: {elevation}, Raised to Power: {raised_to_power}")
print(f"Quotient as Integer: {quotient_int}, Quotient using Floor Division: {quotient_floor}, Remainder: {getting_remainder}")
print(f"Quotient formatted as Integer using f-string: {quotient_f_string}")