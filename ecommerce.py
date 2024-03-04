import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

DATABASE = 'ecommerce.db'

def get_connection():
  """
  Get connection from database
  """
  try:
      conn = sqlite3.connect(DATABASE)
  except Exception as e:
    print(f"An error occurred while connecting the database from controller: {e}")
  return conn

def getDBResult(sql):
  """
  Get query result from database
  """
  # open the connection to the database
  conn = get_connection()
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute(sql)
  conn.close()
  return cur.fetchall()

@app.route('/')
def index():
    """
    Display Home page
    """
    return render_template('index.html')

@app.route('/products')
@app.route('/products/page/<int:page>')
def products(page=1, per_page=20):
    """
    Display product list
    """
    start = (page - 1) * per_page
    end = start + per_page
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Products LIMIT ?, ?", (start, per_page))
    products = cur.fetchall()
    cur = conn.cursor()
    total_products = cur.execute('SELECT COUNT(*) FROM Products').fetchone()
    total_pages = (total_products[0] + per_page - 1) // per_page  # Calculate the total number of pages
    # Calculate previous and next page numbers, ensuring they stay within bounds
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None
    conn.close()
    return render_template('products.html', 
                          rows=products, 
                          total_pages=total_pages, 
                          current_page=page, 
                          prev_page=prev_page, 
                          next_page=next_page)

@app.route('/customers')
@app.route('/customers/page/<int:page>')
def customers(page=1, per_page=20):
    """
    Display the customer list
    """
    start = (page - 1) * per_page
    end = start + per_page
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Customers LIMIT ?,?", (start, per_page))
    customers = cur.fetchall()
    cur = conn.cursor()
    total_customers = cur.execute('SELECT COUNT(*) FROM Customers').fetchone()
    total_pages = (total_customers[0] + per_page - 1) // per_page  # Calculate the total number of pages
    # Calculate previous and next page numbers, ensuring they stay within bounds
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None
    conn.close()
    return render_template('customers.html', 
                          rows=customers, 
                          total_pages=total_pages, 
                          current_page=page, 
                          prev_page=prev_page, 
                          next_page=next_page)

@app.route('/orders')
@app.route('/orders/page/<int:page>')
def orders(page=1, per_page=20):
    """
    Display order list
    """
    start = (page - 1) * per_page
    end = start + per_page
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select *"
            "from Orders o left join Customers c "
            "on o.CustomerID = c.CustomerID "
            "LIMIT ?, ?", (start, per_page))
    orders = cur.fetchall()
    cur = conn.cursor()
    total_orders = cur.execute('SELECT COUNT(*) FROM Orders').fetchone()
    total_pages = (total_orders[0] + per_page - 1) // per_page  # Calculate the total number of pages
    # Calculate previous and next page numbers, ensuring they stay within bounds
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None
    conn.close()
    return render_template('orders.html', 
                          rows=orders, 
                          total_pages=total_pages, 
                          current_page=page, 
                          prev_page=prev_page, 
                          next_page=next_page)

@app.route('/orderDetails', defaults={'OrderID': None})
@app.route('/orderDetails/<OrderID>/page/<int:page>')
def orderDetails(OrderID, page=1, per_page=20):
    """
    Display order detail list
    """
    start = (page - 1) * per_page
    end = start + per_page
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    print(OrderID)
    print(start)
    print(per_page)
    if OrderID:
      cur.execute("select * "
              "from OrderDetails o left join Products p "
              "on o.ProductID = p.ProductID "
              "where o.OrderID = ? "
              "LIMIT ?, ?", (OrderID, start, per_page))
      details = cur.fetchall()
      cur = conn.cursor()
      cur.execute("SELECT COUNT(*) FROM OrderDetails where OrderID = ?", (OrderID,))
      total_details = cur.fetchone()
    else:
      cur.execute("select * from OrderDetails LIMIT ?, ?", (start, per_page))
      details = cur.fetchall()
      cur = conn.cursor()
      total_details = cur.execute('SELECT COUNT(*) FROM OrderDetails').fetchone()
    # Calculate the total number of pages
    total_pages = (total_details[0] + per_page - 1) // per_page
    # Calculate previous and next page numbers, ensuring they stay within bounds
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None
    conn.close()
    return render_template('orderDetails.html', 
                          rows=details, 
                          total_pages=total_pages, 
                          current_page=page, 
                          prev_page=prev_page, 
                          next_page=next_page)
 