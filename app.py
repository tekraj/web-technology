import os
from flask import Flask,request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask import Flask
from models.db import db
load_dotenv() # load environmental values

### Data base setup
# get dababase configs
DB_USERNAME=os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
DB_URL=os.getenv('DB_URL')



# create app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}:3306/{DB_NAME}"
db.init_app(app) # # initialize the app with the db

# import models
from models import User, db

migrate = Migrate(app, db)
# Routes

@app.route('/',methods=['GET']) # define route and methods
def index():
    return 'index page'

@app.route('/page/<int:page_id>')
def page(page_id):
   pageNumber = request.args.get('pageNumber') # query params
   formData = request.form # form Data
   files = request.files # files
   json = request.json()
   return f"PageId = {page_id} pageNumber={pageNumber} {formData}"

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=4000) # run on port 4000, default is 5000



