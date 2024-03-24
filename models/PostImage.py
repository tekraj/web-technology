from datetime import datetime
from models.db import db

class PostImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100),  nullable=False)
    post_id=db.Column(db.Integer, db.ForeignKey("post.id"))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
       return f"<PostImage id={self.id}, name={self.image}>"


