import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import AppConfigData


db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object(AppConfigData)
db.init_app(app)
from db_models import *
from sessioninfo import *
from views import *
from ehandlers import *

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True, port=5010)
