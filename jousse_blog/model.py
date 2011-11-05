from flaskext.sqlalchemy import SQLAlchemy
from jousse_blog import app, db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, unique=False)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Content %r>' % self.content
