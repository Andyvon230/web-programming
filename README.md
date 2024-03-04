# E-Commerce Flask Web Application

## Overview
This Flask web application has been developed as part of the CS551P assessment for web programming.
By using Python, Flask, Faker, sqlite3 and several extra library of python, this `E—Commerce` project displays several linked tables, such as customers, products and orders.

## Why was this app developed?
The application was created to demonstrate the ability to build a full-fledged web application using Flask, integrating with a database, and handling CSV data. It serves as a coursework project for educational purposes, showcasing CRUD operations, data parsing, and web server management.
Not only that, the procedure of programming exercises the ability of using Git to manage version control.

## How to run the app?
#### In Debug Mode
To deploy this project in debug mode, run command below in the Linux Terminal one by one when you are in workspace of this project:
```
pyenv install 3.7.0
pyenv local 3.7.0
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install flask
pip install Faker
export FLASK_APP=ecommerce.py
export FLASK_ENV=development
python3 -m flask run -h 0.0.0.0
```
#### Using Render

##### https://testdriven.io/blog/flask-render-deployment/

Start by creating a new account with Render (if you don't have one).

Then, navigate to your dashboard, click on the "New +" button, and select "Web Service".

Connect your Render account to your GitHub account. 

Once connected, select the repository to deploy:

Name: web-programming

Environment: Python3

Build command: $ pip install -r requirements.txt

Start command: $ gunicorn ecommerce:app

 

Click 'Create Web Service'

..... 

until build successfully

## Features
- `ecommerce.py` provides the function of queries, handling requests and pagination.
- CSV parsing capabilities provided by `parse_csv.py` for importing order details into `ecommerce.db`.
- Templated front-end design located under the `templates` directory.

## Maintenance
- Regular updates are necessary to maintain package security and compatibility.
- Database migrations should be handled carefully with backups when schema changes.
- Any changes to CSV formats should be reflected in `parse_csv.py`.

## Acknowledgments
- Thanks to the educators and contributors who provided guidance and support throughout the development of this project.
