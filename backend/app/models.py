from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, index=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    is_active = db.Column(db.Boolean(True))
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)