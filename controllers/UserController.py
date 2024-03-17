from flask import flash
from typing import Dict
from models.db import db
from models.User import User
import hashlib
from flask import  session
import re

class UserController:
    def __init__(self):
        pass
    
    def login(self,email:str,password:str)->bool:
        user = User.query.filter_by(email=email).first()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if user and user.password==hashed_password:
            session['user_id'] = user.id
            return True
        
        flash("Invalid email or password", "error")
        return False
    
    def register(self,user: Dict[str, str]):
        try:
            # validate email
            if not self.is_valid_email(user['email']):
                flash("Invalid Email!", "error")
                return False
            
             # Validate name 
            if not user['name'].strip():
                flash("Name cannot be empty!", "error")
                return False
            
            # if there is already another user with same email 
            existing_user = User.query.filter_by(email=user['email']).first()
            if existing_user:
                flash("Email already exists!", "error")
                return False
            else:
                # Create a new user with MD5 hashed password
                hashed_password = hashlib.md5(user['password'].encode()).hexdigest()
                new_user = User(name=user['name'], email=user['email'], password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash("Signed up successfully! Please signin", "success")
                return True
        except Exception as e:
            print(e)
            return False
    
    def is_valid_email(self,email: str) -> bool:
        # Regular expression for email validation
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(email_regex, email))