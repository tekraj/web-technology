import os
from dotenv import load_dotenv
from flask import Flask, redirect,request,render_template, session, url_for
from flask_migrate import Migrate
from flask import Flask
from models.db import db,db_config
from middlewares.auth_middleware import is_authenticated
load_dotenv() # load environmental values

# create app
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = db_config
db.init_app(app) # # initialize the app with the db

# import models
from models import User,Page,Post,PageImage,PostImage
from controllers.UserController import UserController
from controllers.PageController import PageController

#setup migration
migrate = Migrate(app, db)
# controllers
userController = UserController()


# Routes
@app.route('/',methods=['GET'])
def index():
    pages = PageController.list_pages(1, 10)
    page,page_images= PageController.get_page_by_url('home-page')
    return render_template('index.html',pages=pages,page=page,page_images=page_images)

@app.route('/page/<url>',methods=['GET'])
def page(url):
    pages = PageController.list_pages(1, 10)
    page,page_images = PageController.get_page_by_url(url)
    return render_template('index.html',page=page,images=page_images,pages=pages)

# display sigin page
@app.route('/signin',methods=['GET'])
def signin():
    return render_template('auth/signin.html')

# display signup page
@app.route('/signup',methods=['GET']) 
def signup():
    return render_template('auth/signup.html')

# handle login form submit
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    valid_user = userController.login(email=email, password=password)
    if valid_user:
        return redirect(url_for('admin_dashboard'))  # Redirect to the index page
    return redirect(url_for('signin'))  # Redirect to the signin page


# handle register(signup) form submit
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    register_user = userController.register({'name': name, 'email': email, 'password': password})
    if register_user:
        return redirect(url_for('signin'))  # Redirect to the signin page
    return redirect(url_for('signup'))  # Redirect to the signup page


#only the logged in user can access this route, if not logged in redirect to signin page
# display admin dashboard page
@app.route('/admin',methods=['GET']) 
@is_authenticated # check user has logged in or not, can only see home page if logged in
def admin_dashboard():
    return render_template('admin/dashboard.html')

# display admin page management page
@app.route('/admin/user',methods=['GET']) 
@is_authenticated 
def admin_user():
    return render_template('admin/user/user.html')


# display admin page management page
@app.route('/admin/page',methods=['GET']) 
@is_authenticated 
def admin_page():
    page_number = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    pages = PageController.list_pages(page_number, per_page)
    return render_template('admin/page/page.html',pages=pages)

# display create new page form
@app.route('/admin/page/create-page',methods=['GET']) 
@is_authenticated 
def admin_page_show_create_form():
    return render_template('admin/page/create-page.html')

# display update  page form
@app.route('/admin/page/update-page/<page_id>',methods=['GET']) 
@is_authenticated 
def admin_page_show_update_form(page_id):
    page,page_images = PageController.get_page_by_id(page_id)
    return render_template('admin/page/edit-page.html',page=page)

@app.route('/admin/page/create',methods=['POST']) 
@is_authenticated 
def admin_page_create():
    name = request.form['name']
    description = request.form['description']
    images  = request.files.getlist('image')
    create_post = PageController.create_page(name=name,description=description,images=images)
    if create_post:
        return redirect(url_for('admin_page'))  
    return redirect(url_for('admin_page_create'))  

@app.route('/admin/page/update/<page_id>',methods=['POST']) 
@is_authenticated 
def admin_page_update(page_id):
    name = request.form['name']
    description = request.form['description']
    images  = request.files.getlist('image')
    create_post = PageController.update_page(page_id=page_id,name=name,description=description)
    if create_post:
        return redirect(url_for('admin_page'))  
    return redirect(url_for('admin_page_show_update_form')) 
# display admin post management page
@app.route('/admin/post',methods=['GET']) 
@is_authenticated 
def admin_post():
    return render_template('admin/post/post.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=4000) # run on port 4000, default is 5000 


# run this file and then open localhost:4000 on browser



