from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import click

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    is_active = db.Column(db.Boolean(True))
    
@app.route("/")
def homepage():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def login():
    return 'login'

@app.route("/logout", methods=['POST'])
def logout():
    return 'logout'

@app.route('/register', methods=["POST"])
def register():
    return 'register'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)