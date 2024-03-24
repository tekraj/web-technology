from datetime import datetime
from models.db import db

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),  nullable=False)
    url= db.Column(db.String(50), unique=True,  nullable=False)
    description = db.Column(db.Text(),  nullable=False) # text for storing  text - large string
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
       return f"<Page id={self.id}, name={self.name}>"


