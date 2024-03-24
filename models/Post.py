from datetime import datetime
from models.db import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),  nullable=False)
    url= db.Column(db.String(50), unique=True,  nullable=False)
    page_id=db.Column(db.Integer, db.ForeignKey("page.id"))
    description=db.Column(db.Text())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
       return f"<Post id={self.id}, name={self.name}>"


