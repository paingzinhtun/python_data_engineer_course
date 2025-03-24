"""
Functions and Modules
This module demonstrates Python functions, modules, and their usage in data engineering.
"""

# Basic Functions
def process_data(data):
    """Example function for data processing"""
    return [x * 2 for x in data]

def calculate_statistics(numbers):
    """Calculate basic statistics from a list of numbers"""
    if not numbers:
        return None
    return {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }

# Function with multiple arguments and default values
def create_user(name, age, city="Unknown"):
    """Create a user dictionary with optional city parameter"""
    return {
        'name': name,
        'age': age,
        'city': city
    }

# Lambda functions
square = lambda x: x**2
add = lambda x, y: x + y

# Example usage
if __name__ == "__main__":
    # Test process_data function
    numbers = [1, 2, 3, 4, 5]
    processed_numbers = process_data(numbers)
    print(f"Original numbers: {numbers}")
    print(f"Processed numbers: {processed_numbers}")

    # Test calculate_statistics function
    stats = calculate_statistics(numbers)
    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    # Test create_user function
    user1 = create_user("John", 30, "New York")
    user2 = create_user("Anna", 25)  # Using default city
    print("\nUsers:")
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")

    # Test lambda functions
    print("\nLambda functions:")
    print(f"Square of 5: {square(5)}")
    print(f"Sum of 3 and 4: {add(3, 4)}") 