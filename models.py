
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

image = "https://images.unsplash.com/photo-1665897530498-e3c664ff42ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"

def connect_db(app):
    """connect to database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, default=image)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    is_available = db.Column(db.Boolean, nullable=False,default=True)