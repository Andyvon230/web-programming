import csv
import sqlite3
from contextlib import closing

def read_csv(file_path):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row from the CSV with column headers as keys.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def create_database(db_name):
    """
    Creates a new SQLite database connection and returns a connection object.
    """
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")
        return None

def create_tables(conn):
    """
    Creates tables in the SQLite database.
    """
    try:
        # drop the data from the table so that if we rerun the file, we don't repeat values
        conn.execute('DROP TABLE IF EXISTS Customers')
        print(f"table Customers dropped successfully");
        conn.execute('DROP TABLE IF EXISTS Products')
        print(f"table Products dropped successfully");
        conn.execute('DROP TABLE IF EXISTS Orders')
        print(f"table Orders dropped successfully");
        conn.execute('DROP TABLE IF EXISTS OrderDetails')
        print(f"table OrderDetails dropped successfully");
        with closing(conn.cursor()) as cur:
            # Create Customers table
            cur.execute('''CREATE TABLE Customers (
                            CustomerID INTEGER PRIMARY KEY,
                            FirstName TEXT,
                            c TEXT,
                            Email TEXT)''')
            print(f"table Customers created successfully");

            # Create Products table
            cur.execute('''CREATE TABLE Products (
                            ProductID INTEGER PRIMARY KEY,
                            ProductName TEXT,
                            Price REAL)''')
            print(f"table Products created successfully");
            
            # Create Orders table
            cur.execute('''CREATE TABLE Orders (
                            OrderID INTEGER PRIMARY KEY,
                            CustomerID INTEGER,
                            OrderDate TEXT,
                            FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID))''')
            print(f"table Orders created successfully");

            # Create OrderDetails table
            cur.execute('''CREATE TABLE OrderDetails (
                            OrderDetailID INTEGER PRIMARY KEY,
                            OrderID INTEGER,
                            ProductID INTEGER,
                            Quantity INTEGER,
                            FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
                            FOREIGN KEY(ProductID) REFERENCES Products(ProductID))''')
            print(f"table OrderDetails created successfully");
        conn.commit()
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")

def insert_data(conn, data):
    """
    Inserts data into the database from the list of dictionaries.
    """
    try:
        with closing(conn.cursor()) as cur:
            # Insert data into each table
            for row in data:
                # Insert or ignore into Customers
                print(f"Current row: {row}")
                cur.execute('''INSERT INTO Customers (CustomerID, FirstName, LastName, Email)
                               VALUES (?, ?, ?, ?)''', 
                            (row['CustomerID'], row['CustomerFirstName'], row['CustomerLastName'], row['CustomerEmail']))
                
                # Insert or ignore into Products
                cur.execute('''INSERT INTO Products (ProductID, ProductName, Price)
                               VALUES (?, ?, ?)''', 
                            (row['ProductID'], row['ProductName'], row['ProductPrice']))
                
                # Insert or ignore into Orders
                cur.execute('''INSERT INTO Orders (OrderID, CustomerID, OrderDate)
                               VALUES (?, ?, ?)''', 
                            (row['OrderID'], row['CustomerID'], row['OrderDate']))
                
                # Insert into OrderDetails
                cur.execute('''INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
                               VALUES (?, ?, ?, ?)''', 
                            (row['OrderDetailID'], row['OrderID'], row['ProductID'], row['Quantity']))
                print(f"Current row insert finished: {row}")
            
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        return False

def main(csv_file_path, db_name='ecommerce.db'):
    """
    Main function to read CSV, create database and tables, and insert data.
    """
    data = read_csv(csv_file_path)
    if not data:
        return

    conn = create_database(db_name)
    if conn is None:
        return

    create_tables(conn)
    is_success = insert_data(conn, data)
    if is_success:
        print(f"Data imported successfully into database.")
    else:
        print(f"Error during data import.")
    conn.close()

if __name__ == "__main__":
    csv_file_path = 'order_details.csv'
    main(csv_file_path)
