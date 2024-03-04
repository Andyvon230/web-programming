### About this Project
By using Python, Flask, Faker, sqlite3 and several extra library of python, this `E—Commerce` project displays several linked tables, such as customers, products and orders.

### Deploy
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

Start command: $ gunicorn web-programming:app

 

Click 'Create Web Service'

..... 

until build successfully