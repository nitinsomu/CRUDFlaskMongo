from flask import Flask
from flask_pymongo import PyMongo
from routes.user_bp import create_user_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)
app.register_blueprint(create_user_bp(mongo), url_prefix="/users")

if __name__ == "__main__":
    app.run()
