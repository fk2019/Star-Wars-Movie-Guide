#!/usr/bin/python3
"""api module that registeres app_views blueprint
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
#register the app with the app_views blueprint
app.register_blueprint(app_views)
cors = CORS(app, resources={r'/api/v1/*': {'origins': '*'}})


@app.errorhandler(404)
def not_found(error):
    """Return jsonified error"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
