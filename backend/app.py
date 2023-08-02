from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
# print(os.getenv('APP_SETTINGS'))
print(os.environ)
app.config.from_object(os.getenv('APP_SETTINGS'))
# print(app.config.from_object(os.getenv('APP_SETTINGS')))
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

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