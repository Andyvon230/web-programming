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
def products():
    """
    Display product list
    """
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Products")
    products = cur.fetchall()
    conn.close()
    return render_template('products.html', rows=products)

@app.route('/customers')
def customers():
    """
    Display the customer list
    """
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Customers")
    customers = cur.fetchall()
    conn.close()
    return render_template('customers.html', rows=customers)

@app.route('/orders')
def orders():
    """
    Display order list
    """
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select *"
            "from Orders o left join Customers c "
            "on o.CustomerID = c.CustomerID")
    orders = cur.fetchall()
    conn.close()
    return render_template('orders.html', rows=orders)

@app.route('/orderDetails')
@app.route('/orderDetails/<OrderID>')
def orderDetails(OrderID=None):
    """
    Display order detail list
    """
      # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if OrderID:
      cur.execute("select * "
              "from OrderDetails o left join Products p "
              "on o.ProductID = p.ProductID "
              "where o.OrderID = ?", (OrderID,))
    else:
      cur.execute("select * from OrderDetails")
    details = cur.fetchall()
    conn.close()
    return render_template('orderDetails.html', rows=details)
 