import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

DATABASE = 'ecommerce.db'

def get_connection():
  try:
      conn = sqlite3.connect(DATABASE)
  except Exception as e:
    print(f"An error occurred while connecting the database from controller: {e}")
  return conn

@app.route('/')
def index():
    # open the connection to the database
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select ProductID, ProductName, Price from Products")
    products = cur.fetchall()
    conn.close()
    return render_template('product_list.html', products=products)