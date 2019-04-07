from datetime import datetime
from whr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # this allows to get all of the inquiries sent by an individual user:
    inquiries = db.relationship('Inquiry', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}', '{self.date_created}'"

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_inquired = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_input = db.Column(db.Text, nullable=True)
    # this is the foreign key to link to the user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Inquiry('{self.date_inquired}', '{self.user_input}'"