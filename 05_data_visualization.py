"""
Data Visualization
This module demonstrates various data visualization techniques using matplotlib and seaborn.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_sample_data():
    """Create sample data for visualization"""
    data = {
        'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'sales': [1200, 1900, 1500, 2100, 1800, 2400],
        'expenses': [1000, 1600, 1400, 1800, 1600, 2000],
        'category': ['A', 'B', 'A', 'C', 'B', 'A']
    }
    return pd.DataFrame(data)

def demonstrate_line_plot(df):
    """Demonstrate line plot"""
    plt.figure(figsize=(10, 6))
    plt.plot(df['month'], df['sales'], marker='o', label='Sales')
    plt.plot(df['month'], df['expenses'], marker='s', label='Expenses')
    plt.title('Sales and Expenses Over Time')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.grid(True)
    plt.savefig('line_plot.png')
    plt.close()

def demonstrate_bar_plot(df):
    """Demonstrate bar plot"""
    plt.figure(figsize=(10, 6))
    x = range(len(df))
    width = 0.35
    
    plt.bar([i - width/2 for i in x], df['sales'], width, label='Sales')
    plt.bar([i + width/2 for i in x], df['expenses'], width, label='Expenses')
    
    plt.title('Sales and Expenses by Month')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.xticks(x, df['month'])
    plt.legend()
    plt.grid(True)
    plt.savefig('bar_plot.png')
    plt.close()

def demonstrate_pie_chart(df):
    """Demonstrate pie chart"""
    plt.figure(figsize=(8, 8))
    category_sales = df.groupby('category')['sales'].sum()
    plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%')
    plt.title('Sales Distribution by Category')
    plt.savefig('pie_chart.png')
    plt.close()

def demonstrate_scatter_plot(df):
    """Demonstrate scatter plot"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['sales'], df['expenses'])
    plt.title('Sales vs Expenses')
    plt.xlabel('Sales ($)')
    plt.ylabel('Expenses ($)')
    plt.grid(True)
    plt.savefig('scatter_plot.png')
    plt.close()

def demonstrate_seaborn_plots(df):
    """Demonstrate various seaborn plots"""
    # Set the style
    sns.set_style("whitegrid")
    
    # Box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='category', y='sales', data=df)
    plt.title('Sales Distribution by Category')
    plt.savefig('box_plot.png')
    plt.close()
    
    # Violin plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='category', y='sales', data=df)
    plt.title('Sales Distribution by Category (Violin Plot)')
    plt.savefig('violin_plot.png')
    plt.close()

def demonstrate_advanced_visualizations(df):
    """Demonstrate advanced visualization techniques"""
    # Create a figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Line plot
    ax1.plot(df['month'], df['sales'], marker='o')
    ax1.set_title('Sales Trend')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Sales ($)')
    ax1.grid(True)
    
    # Bar plot
    ax2.bar(df['month'], df['expenses'])
    ax2.set_title('Expenses by Month')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Expenses ($)')
    ax2.grid(True)
    
    # Scatter plot
    ax3.scatter(df['sales'], df['expenses'])
    ax3.set_title('Sales vs Expenses')
    ax3.set_xlabel('Sales ($)')
    ax3.set_ylabel('Expenses ($)')
    ax3.grid(True)
    
    # Pie chart
    category_sales = df.groupby('category')['sales'].sum()
    ax4.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%')
    ax4.set_title('Sales by Category')
    
    plt.tight_layout()
    plt.savefig('advanced_visualizations.png')
    plt.close()

if __name__ == "__main__":
    # Create sample data
    df = create_sample_data()
    
    # Demonstrate various visualization techniques
    demonstrate_line_plot(df)
    demonstrate_bar_plot(df)
    demonstrate_pie_chart(df)
    demonstrate_scatter_plot(df)
    demonstrate_seaborn_plots(df)
    demonstrate_advanced_visualizations(df)
    
    print("All visualization plots have been saved as PNG files.") 