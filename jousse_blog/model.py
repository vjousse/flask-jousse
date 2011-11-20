from flaskext.sqlalchemy import SQLAlchemy
from jousse_blog import app, db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    intro = db.Column(db.Text)
    content = db.Column(db.Text)
    published = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    image = db.Column(db.String(100))
    
    #Could be file, db, external
    content_type = db.Column(db.String(20))

    def __init__(self, title, intro, content, published, content_type, created_at=None):
        self.title = title
        self.intro = intro
        self.content = content
        self.published = published
        self.content_type = content_type

        if created_at is None:
            created_at = datetime.utcnow()

        self.content_type = content_type

    def __repr__(self):
        return '<Content %r>' % self.content
