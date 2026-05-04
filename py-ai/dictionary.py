# Dictionary

lead = {
    "title": "Dictionary",
    "description": "A dictionary is a data structure that stores key-value pairs. It allows you to associate a value with a unique key, making it easy to retrieve and manipulate data based on the key.",
    "example": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
}

print(lead["title"])  # Output: Dictionary
print(lead["description"])  # Output: A dictionary is a data structure that stores key
print(lead["example"])  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(lead["example"]["name"])  # Output: Alice
print(lead["example"]["age"])  # Output: 30
print(lead["example"]["city"])  # Output: New York

# Dictionary with mixed data types
my_dict = {
    "string": "Hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "nested_dict": {
        "key1": "value1",
        "key2": "value2"
    }
}

print(f"""My dictionary: 
      {my_dict}""")
