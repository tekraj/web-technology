## This is Simple Flask Application 
## To Run this application install following packages
- pip install Flask
- pip install Jinja2
- pip install Flask-SQLAlchemy
- pip install pymysql
- pip install python-dotenv
- pip install Flask-Migrate

## Or simply run pip install requirements.txt 

### Copy .env-example to .env and add your env values
## Use Docker if you are familiar with Docker (otherwise skip this)
- docker-compose up -d (this will run the application)

## Run migrations 
- flask db init
- flask db migrate
- flask db upgrade