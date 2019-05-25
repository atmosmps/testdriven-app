# services/users/project/__init__.py

import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


# model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullabe=False)
    email = db.Column(db.String(128), nullabe=False)
    active = db.Column(db.Boolean(), default=True, nullabe=False)


class Userping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Userping, '/users/ping/')
