# services/users/project/__init__.py

import os, sys
from flask import Flask, jsonify


# New Instance for Flask
app = Flask(__name__)

# Para teste
print(app.config, file=sys.stderr)

# Set Config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'Pong com Docker!'
    })
