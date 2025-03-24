"""
Error Handling
This module demonstrates various error handling techniques in Python.
"""

import sys
import logging
from typing import Union, List, Dict
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error_handling.log'
)

class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message: str, error_code: int = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def demonstrate_basic_error_handling():
    """Demonstrate basic error handling with try-except"""
    print("\n=== Basic Error Handling ===")
    
    # Division by zero
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        logging.error(f"Division by zero error: {e}")
    
    # Type error
    try:
        text = "Hello"
        number = 42
        result = text + number
    except TypeError as e:
        print(f"Error: {e}")
        logging.error(f"Type error: {e}")
    
    # File not found
    try:
        with open('nonexistent_file.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        logging.error(f"File not found error: {e}")

def demonstrate_advanced_error_handling():
    """Demonstrate advanced error handling techniques"""
    print("\n=== Advanced Error Handling ===")
    
    def process_data(data: Union[List, Dict]) -> float:
        """Process data with type checking and error handling"""
        try:
            if isinstance(data, list):
                return sum(data) / len(data)
            elif isinstance(data, dict):
                return sum(data.values()) / len(data)
            else:
                raise CustomError("Input must be a list or dictionary", error_code=400)
        except ZeroDivisionError as e:
            raise CustomError("Cannot process empty data", error_code=400) from e
        except Exception as e:
            raise CustomError(f"Unexpected error: {str(e)}", error_code=500) from e
    
    # Test with valid data
    try:
        result = process_data([1, 2, 3, 4, 5])
        print(f"Result with list: {result}")
    except CustomError as e:
        print(f"Custom error: {e.message} (Code: {e.error_code})")
        logging.error(f"Custom error: {e.message} (Code: {e.error_code})")
    
    # Test with invalid data
    try:
        result = process_data("invalid")
    except CustomError as e:
        print(f"Custom error: {e.message} (Code: {e.error_code})")
        logging.error(f"Custom error: {e.message} (Code: {e.error_code})")

def demonstrate_context_managers():
    """Demonstrate context managers for resource handling"""
    print("\n=== Context Managers ===")
    
    class DatabaseConnection:
        """Example context manager for database connection"""
        def __init__(self, db_name: str):
            self.db_name = db_name
            self.connection = None
        
        def __enter__(self):
            print(f"Connecting to database: {self.db_name}")
            # Simulate connection
            self.connection = "Connected"
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Closing database connection")
            self.connection = None
            if exc_type is not None:
                logging.error(f"Error in database connection: {exc_val}")
                return False
            return True
    
    # Using context manager
    try:
        with DatabaseConnection("example.db") as db:
            print(f"Database connection status: {db.connection}")
            # Simulate an error
            raise Exception("Database error")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Database error: {e}")

def demonstrate_error_tracking():
    """Demonstrate error tracking and debugging"""
    print("\n=== Error Tracking ===")
    
    def complex_function():
        """Function that might raise various errors"""
        try:
            # Simulate a complex operation
            result = 1 / 0
        except Exception as e:
            # Get detailed error information
            error_type = type(e).__name__
            error_message = str(e)
            error_traceback = traceback.format_exc()
            
            # Log detailed error information
            logging.error(f"Error Type: {error_type}")
            logging.error(f"Error Message: {error_message}")
            logging.error(f"Traceback:\n{error_traceback}")
            
            # Print error information
            print(f"Error Type: {error_type}")
            print(f"Error Message: {error_message}")
            print("Traceback:")
            traceback.print_exc()
    
    # Test error tracking
    complex_function()

def demonstrate_cleanup_handling():
    """Demonstrate cleanup handling with try-finally"""
    print("\n=== Cleanup Handling ===")
    
    def process_file(filename: str):
        """Process a file with proper cleanup"""
        file = None
        try:
            file = open(filename, 'w')
            file.write("Test data")
        except IOError as e:
            print(f"Error writing to file: {e}")
            logging.error(f"IO error: {e}")
        finally:
            if file:
                file.close()
                print("File closed successfully")
    
    # Test cleanup handling
    process_file("test.txt")

if __name__ == "__main__":
    # Demonstrate various error handling techniques
    demonstrate_basic_error_handling()
    demonstrate_advanced_error_handling()
    demonstrate_context_managers()
    demonstrate_error_tracking()
    demonstrate_cleanup_handling() 