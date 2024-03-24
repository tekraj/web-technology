from datetime import datetime
from models.db import db

class PageImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100),  nullable=False)
    page_id=db.Column(db.Integer, db.ForeignKey("page.id"))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
       return f"<PageImage id={self.id}, name={self.image}>"


