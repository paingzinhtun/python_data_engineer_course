# Module 2: Python Basics

## **2.1 Variables & Data Types**
Before working with Python for Data Engineering, it's essential to understand Python's fundamental data types and how to use them.

### **Common Data Types in Python**
- **Integers (`int`)**: Whole numbers (e.g., `10`, `-3`)
- **Floats (`float`)**: Decimal numbers (e.g., `3.14`, `-0.5`)
- **Strings (`str`)**: Text data (e.g., `'Hello'`, `"World"`)
- **Booleans (`bool`)**: True/False values (e.g., `True`, `False`)
- **Lists (`list`)**: Ordered, mutable collection (e.g., `[1, 2, 3]`)
- **Tuples (`tuple`)**: Ordered, immutable collection (e.g., `(1, 2, 3)`) 
- **Dictionaries (`dict`)**: Key-value pairs (e.g., `{'name': 'Alice', 'age': 25}`)
- **Sets (`set`)**: Unordered collection of unique elements (e.g., `{1, 2, 3}`)

### **Example Code:**
```python
# Defining variables
name = "Alice"  # String
age = 25        # Integer
height = 5.7    # Float
is_student = True  # Boolean

# Type conversion
age_str = str(age)  # Convert int to string
height_int = int(height)  # Convert float to int

print(type(age_str))   # Output: <class 'str'>
print(type(height_int))  # Output: <class 'int'>
```

---
## **2.2 Operators & Expressions**
### **Types of Operators**
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `and`, `or`, `not`
- **Assignment Operators**: `=`, `+=`, `-=`, `*=`, etc.

### **Example Code:**
```python
a = 10
b = 3

# Arithmetic operations
print(a + b)  # Addition: 13
print(a / b)  # Division: 3.3333
print(a // b) # Floor division: 3
print(a ** b) # Exponentiation: 1000

# Logical operations
print(a > 5 and b < 5)  # Output: True
print(not (a == b))     # Output: True
```

---
## **2.3 Control Flow (if-else, loops)**
### **Conditional Statements**
```python
x = 15
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")
```

### **Looping through a list**
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

### **While Loop**
```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

---
## **2.4 Functions & Modules**
### **Defining Functions**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### **Importing Modules**
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

---
## **2.5 Exception Handling**
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution completed.")
```

---
## **Project: Building a Simple Data Processor**
### **Requirements:**
- Read user input
- Perform basic calculations
- Handle exceptions
- Print formatted output

```python
def data_processor():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    finally:
        print("Program execution completed.")

# Run the function
data_processor()
