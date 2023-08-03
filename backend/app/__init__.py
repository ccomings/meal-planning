import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from app.models import User
from app import routes
print('__name__', __name__)
if __name__ == 'app':
	app.run(host='0.0.0.0', port=8000)