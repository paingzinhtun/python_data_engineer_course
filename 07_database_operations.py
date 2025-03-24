"""
Database Operations
This module demonstrates database operations in Python using SQLite and SQLAlchemy.
"""

import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from datetime import datetime

# SQLite Operations
def demonstrate_sqlite_operations():
    """Demonstrate basic SQLite operations"""
    print("\n=== SQLite Operations ===")
    
    # Create a connection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        order_date DATETIME,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    # Insert data
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                  ("John Doe", 30, "john@example.com"))
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                  ("Jane Smith", 25, "jane@example.com"))
    
    cursor.execute("INSERT INTO orders (user_id, amount, order_date) VALUES (?, ?, ?)",
                  (1, 100.50, datetime.now()))
    cursor.execute("INSERT INTO orders (user_id, amount, order_date) VALUES (?, ?, ?)",
                  (1, 75.25, datetime.now()))
    
    # Commit changes
    conn.commit()
    
    # Query data
    print("\nUsers:")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    
    print("\nOrders:")
    cursor.execute("SELECT * FROM orders")
    for row in cursor.fetchall():
        print(row)
    
    # Join query
    print("\nOrders with User Information:")
    cursor.execute('''
    SELECT orders.id, users.name, orders.amount, orders.order_date
    FROM orders
    JOIN users ON orders.user_id = users.id
    ''')
    for row in cursor.fetchall():
        print(row)
    
    # Close connection
    conn.close()

# SQLAlchemy Operations
Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))
    
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, email='{self.email}')>"

class Order(Base):
    """Order model"""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    order_date = Column(DateTime)
    
    def __repr__(self):
        return f"<Order(user_id={self.user_id}, amount={self.amount}, order_date='{self.order_date}')>"

def demonstrate_sqlalchemy_operations():
    """Demonstrate SQLAlchemy operations"""
    print("\n=== SQLAlchemy Operations ===")
    
    # Create engine and tables
    engine = create_engine('sqlite:///example_sqlalchemy.db')
    Base.metadata.create_all(engine)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create users
    user1 = User(name="John Doe", age=30, email="john@example.com")
    user2 = User(name="Jane Smith", age=25, email="jane@example.com")
    
    session.add(user1)
    session.add(user2)
    session.commit()
    
    # Create orders
    order1 = Order(user_id=1, amount=100.50, order_date=datetime.now())
    order2 = Order(user_id=1, amount=75.25, order_date=datetime.now())
    
    session.add(order1)
    session.add(order2)
    session.commit()
    
    # Query data
    print("\nUsers:")
    users = session.query(User).all()
    for user in users:
        print(user)
    
    print("\nOrders:")
    orders = session.query(Order).all()
    for order in orders:
        print(order)
    
    # Close session
    session.close()

def demonstrate_pandas_sql():
    """Demonstrate pandas SQL operations"""
    print("\n=== Pandas SQL Operations ===")
    
    # Create engine
    engine = create_engine('sqlite:///example.db')
    
    # Read data into pandas DataFrame
    users_df = pd.read_sql_query("SELECT * FROM users", engine)
    orders_df = pd.read_sql_query("SELECT * FROM orders", engine)
    
    print("\nUsers DataFrame:")
    print(users_df)
    
    print("\nOrders DataFrame:")
    print(orders_df)
    
    # Perform join operation
    merged_df = pd.merge(orders_df, users_df, left_on='user_id', right_on='id')
    print("\nMerged DataFrame:")
    print(merged_df)
    
    # Write DataFrame back to database
    merged_df.to_sql('merged_data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    # Demonstrate various database operations
    demonstrate_sqlite_operations()
    demonstrate_sqlalchemy_operations()
    demonstrate_pandas_sql() 