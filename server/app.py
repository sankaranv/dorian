from flask import Flask, jsonify
from flask_cors import CORS

# Config
DEBUG = True

# Initialize the app
app = Flask(__name__)
app.config.from_object(__name__)

# Exanble CORS - this allows us to make requests from a different protocol/IP/domain/port
CORS(app, resources = {r'/*': {'origins': '*'}})

# Sanity check route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('Ping received!')

if __name__ == '__main__':
    app.run()