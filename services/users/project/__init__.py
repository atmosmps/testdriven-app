# services/users/project/__init__.py

import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


class Userping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Userping, '/users/ping/')
