from flask import Flask
from config import Config
from flask_sqlalchamey import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.confing.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes