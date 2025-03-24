"""
File Operations
This module demonstrates various file operations in Python for data engineering.
"""

import os
import csv
import json

def write_text_file(filename, content):
    """Write content to a text file"""
    with open(filename, 'w') as f:
        f.write(content)

def read_text_file(filename):
    """Read content from a text file"""
    with open(filename, 'r') as f:
        return f.read()

def write_csv_file(filename, data):
    """Write data to a CSV file"""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv_file(filename):
    """Read data from a CSV file"""
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def write_json_file(filename, data):
    """Write data to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def read_json_file(filename):
    """Read data from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)

def append_to_file(filename, content):
    """Append content to a file"""
    with open(filename, 'a') as f:
        f.write(content)

if __name__ == "__main__":
    # Test text file operations
    print("=== Text File Operations ===")
    write_text_file('example.txt', "Hello, Data Engineering!")
    content = read_text_file('example.txt')
    print(f"File content: {content}")
    
    # Append more content
    append_to_file('example.txt', "\nThis is an appended line.")
    content = read_text_file('example.txt')
    print(f"Updated content: {content}")

    # Test CSV file operations
    print("\n=== CSV File Operations ===")
    csv_data = [
        ['Name', 'Age', 'City'],
        ['John', '30', 'New York'],
        ['Anna', '25', 'Paris']
    ]
    write_csv_file('users.csv', csv_data)
    csv_content = read_csv_file('users.csv')
    print("CSV Content:")
    for row in csv_content:
        print(row)

    # Test JSON file operations
    print("\n=== JSON File Operations ===")
    json_data = {
        'users': [
            {'name': 'John', 'age': 30, 'city': 'New York'},
            {'name': 'Anna', 'age': 25, 'city': 'Paris'}
        ]
    }
    write_json_file('users.json', json_data)
    json_content = read_json_file('users.json')
    print("JSON Content:")
    print(json_content)

    # Clean up files
    files_to_remove = ['example.txt', 'users.csv', 'users.json']
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"\nRemoved {file}") 