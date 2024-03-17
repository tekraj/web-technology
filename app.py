import os
from flask import Flask, redirect,request,render_template, session, url_for
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask import Flask
from models.db import db
from middlewares.auth_middleware import is_authenticated
load_dotenv() # load environmental values

### Data base setup
# get dababase configs
DB_USERNAME=os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
DB_URL=os.getenv('DB_URL')

# create app
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}:3306/{DB_NAME}"
db.init_app(app) # # initialize the app with the db

# import models
from models.db import  db
from models import User
from controllers.UserController import UserController
migrate = Migrate(app, db)
# controllers
userController = UserController()

# Routes

@app.route('/signin',methods=['GET'])
def signin():
    return render_template('auth/signin.html')

@app.route('/signup',methods=['GET']) 
def signup():
    return render_template('auth/signup.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    valid_user = userController.login(email=email, password=password)
    if valid_user:
        return redirect(url_for('index'))  # Redirect to the index page
    return redirect(url_for('signin'))  # Redirect to the signin page

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    register_user = userController.register({'name': name, 'email': email, 'password': password})
    if register_user:
        return redirect(url_for('signin'))  # Redirect to the signin page
    return redirect(url_for('signup'))  # Redirect to the signup page

@app.route('/',methods=['GET']) 
@is_authenticated
def index():
    return 'index page'


if __name__ == "__main__":
   app.run(host='0.0.0.0',port=4000) # run on port 4000, default is 5000



