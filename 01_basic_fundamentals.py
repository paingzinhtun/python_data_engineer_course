"""
Basic Python Fundamentals
This module covers essential Python concepts including variables, data types, and control structures.
"""

# Variables and Data Types
print("\n=== Variables and Data Types ===")

integer_var = 42
float_var = 3.14
string_var = "Data Engineering"
boolean_var = True
list_var = [1, 2, 3, 4, 5]
dict_var = {"name": "John", "age": 30}

print(f"Integer: {integer_var}, Type: {type(integer_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"String: {string_var}, Type: {type(string_var)}")
print(f"Boolean: {boolean_var}, Type: {type(boolean_var)}")
print(f"List: {list_var}, Type: {type(list_var)}")
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")

# Control Structures
print("\n=== Control Structures ===")

# If-else
age = 25
if age >= 18:
    print("Adult")
else:
    print("Minor")

# For loop
print("\nFor Loop:")
for i in range(3):
    print(f"Count: {i}")

# While loop
print("\nWhile Loop:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# List Comprehension
print("\nList Comprehension:")
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Dictionary Comprehension
print("\nDictionary Comprehension:")
square_dict = {x: x**2 for x in range(5)}
print(f"Square Dictionary: {square_dict}")

if __name__ == "__main__":
    print("\nRunning basic fundamentals examples...") 