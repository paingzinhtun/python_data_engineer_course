"""
Data Processing with Pandas
This module demonstrates data processing operations using pandas library.
"""

import pandas as pd
import numpy as np

def create_sample_dataframe():
    """Create a sample DataFrame for demonstration"""
    data = {
        'name': ['John', 'Anna', 'Peter', 'Sarah', 'Mike'],
        'age': [28, 22, 35, 31, 27],
        'city': ['New York', 'Paris', 'London', 'Tokyo', 'Berlin'],
        'salary': [75000, 65000, 85000, 70000, 72000],
        'experience': [5, 3, 8, 6, 4]
    }
    return pd.DataFrame(data)

def demonstrate_basic_operations(df):
    """Demonstrate basic DataFrame operations"""
    print("\n=== Basic DataFrame Operations ===")
    print("\nDataFrame Info:")
    print(df.info())
    
    print("\nDataFrame Description:")
    print(df.describe())
    
    print("\nFirst 3 rows:")
    print(df.head(3))
    
    print("\nLast 2 rows:")
    print(df.tail(2))

def demonstrate_data_filtering(df):
    """Demonstrate data filtering operations"""
    print("\n=== Data Filtering ===")
    
    # Filter by age
    print("\nPeople older than 30:")
    print(df[df['age'] > 30])
    
    # Multiple conditions
    print("\nPeople from New York or Paris with salary > 70000:")
    print(df[(df['city'].isin(['New York', 'Paris'])) & (df['salary'] > 70000)])
    
    # Using query
    print("\nUsing query method:")
    print(df.query('age > 30 and salary > 75000'))

def demonstrate_data_transformation(df):
    """Demonstrate data transformation operations"""
    print("\n=== Data Transformation ===")
    
    # Adding new column
    df['bonus'] = df['salary'] * 0.1
    print("\nAdded bonus column:")
    print(df)
    
    # Applying function to column
    df['salary_category'] = df['salary'].apply(lambda x: 'High' if x > 75000 else 'Medium' if x > 70000 else 'Low')
    print("\nAdded salary category:")
    print(df)
    
    # Group by operations
    print("\nAverage salary by city:")
    print(df.groupby('city')['salary'].mean())
    
    # Pivot table
    print("\nPivot table of average salary by city and salary category:")
    print(pd.pivot_table(df, values='salary', index='city', columns='salary_category', aggfunc='mean'))

def demonstrate_data_cleaning(df):
    """Demonstrate data cleaning operations"""
    print("\n=== Data Cleaning ===")
    
    # Create a copy with some missing values
    dirty_df = df.copy()
    dirty_df.loc[0, 'age'] = np.nan
    dirty_df.loc[2, 'salary'] = np.nan
    
    print("\nDataFrame with missing values:")
    print(dirty_df)
    
    # Fill missing values
    dirty_df['age'].fillna(dirty_df['age'].mean(), inplace=True)
    dirty_df['salary'].fillna(dirty_df['salary'].median(), inplace=True)
    
    print("\nDataFrame after filling missing values:")
    print(dirty_df)

if __name__ == "__main__":
    # Create sample DataFrame
    df = create_sample_dataframe()
    
    # Demonstrate various operations
    demonstrate_basic_operations(df)
    demonstrate_data_filtering(df)
    demonstrate_data_transformation(df)
    demonstrate_data_cleaning(df) 