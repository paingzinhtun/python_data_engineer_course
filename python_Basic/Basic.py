"""
Python for Data Engineering - Comprehensive Course
This course covers essential Python concepts and libraries needed for data engineering.
"""

# 1. Basic Python Fundamentals
print("\n=== 1. Basic Python Fundamentals ===")

# Variables and Data Types
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
print("\nControl Structures:")
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

# 2. Functions and Modules
print("\n=== 2. Functions and Modules ===")

def process_data(data):
    """Example function for data processing"""
    return [x * 2 for x in data]

# Example usage
numbers = [1, 2, 3, 4, 5]
processed_numbers = process_data(numbers)
print(f"Original numbers: {numbers}")
print(f"Processed numbers: {processed_numbers}")

# 3. File Operations
print("\n=== 3. File Operations ===")

# Writing to a file
with open('example.txt', 'w') as f:
    f.write("Hello, Data Engineering!")

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(f"File content: {content}")

# 4. Data Processing Libraries
print("\n=== 4. Data Processing Libraries ===")

# Pandas Example
import pandas as pd

# Create a sample DataFrame
data = {
    'name': ['John', 'Anna', 'Peter'],
    'age': [28, 22, 35],
    'city': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# Basic DataFrame operations
print("\nDataFrame Operations:")
print(f"Mean age: {df['age'].mean()}")
print(f"Unique cities: {df['city'].unique()}")

# 5. Data Cleaning and Transformation
print("\n=== 5. Data Cleaning and Transformation ===")

# Example of data cleaning
dirty_data = {
    'name': ['John', 'Anna', 'Peter', None],
    'age': [28, None, 35, 40],
    'city': ['New York', 'Paris', 'London', '']
}
dirty_df = pd.DataFrame(dirty_data)

# Clean the data
clean_df = dirty_df.dropna()  # Remove rows with missing values
clean_df['city'] = clean_df['city'].replace('', 'Unknown')  # Replace empty strings
print("\nCleaned DataFrame:")
print(clean_df)

# 6. Data Aggregation
print("\n=== 6. Data Aggregation ===")

# Create sample sales data
sales_data = {
    'product': ['A', 'B', 'A', 'B', 'A'],
    'amount': [100, 200, 150, 300, 250]
}
sales_df = pd.DataFrame(sales_data)

# Group by and aggregate
grouped_sales = sales_df.groupby('product')['amount'].agg(['sum', 'mean', 'count'])
print("\nAggregated Sales Data:")
print(grouped_sales)

# 7. Data Visualization
print("\n=== 7. Data Visualization ===")

import matplotlib.pyplot as plt

# Create a simple bar plot
plt.figure(figsize=(8, 6))
plt.bar(sales_df['product'], sales_df['amount'])
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Amount')
plt.savefig('sales_plot.png')
plt.close()

# 8. Working with APIs
print("\n=== 8. Working with APIs ===")

import requests

def fetch_data_from_api(url):
    """Example function to fetch data from an API"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage (commented out as it requires an actual API endpoint)
# api_url = "https://api.example.com/data"
# data = fetch_data_from_api(api_url)

# 9. Database Operations
print("\n=== 9. Database Operations ===")

import sqlite3

# Create a sample database connection
def create_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create a sample table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')
    
    # Insert sample data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 30))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Anna", 25))
    
    conn.commit()
    conn.close()

# Create the database
create_database()

# 10. Error Handling
print("\n=== 10. Error Handling ===")

def safe_divide(a, b):
    """Example of error handling"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Please provide numeric values")
        return None

# Test error handling
print(safe_divide(10, 2))  # Should work
print(safe_divide(10, 0))  # Should handle division by zero
print(safe_divide("10", 2))  # Should handle type error

"""
This course covers the essential Python concepts and libraries needed for data engineering.
Key topics covered:
1. Basic Python Fundamentals
2. Functions and Modules
3. File Operations
4. Data Processing Libraries (Pandas)
5. Data Cleaning and Transformation
6. Data Aggregation
7. Data Visualization
8. Working with APIs
9. Database Operations
10. Error Handling

To further enhance your data engineering skills, consider learning:
- Advanced SQL
- Data Warehousing concepts
- ETL/ELT processes
- Big Data technologies (Spark, Hadoop)
- Cloud platforms (AWS, GCP, Azure)
- Data modeling
- Data quality and testing
"""

