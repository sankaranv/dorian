from flask import Flask, jsonify
from flask_cors import CORS
from twitter_api_calls import *

# Initialize the app
app = Flask(__name__)
app.config.from_object(__name__)

# Exanble CORS - this allows us to make requests from a different protocol/IP/domain/port
CORS(app, resources = {r'/*': {'origins': '*'}})

# Sanity check route
@app.route('/ping', methods=['GET'])
def ping():
    print("ping")
    return jsonify('Ping sent to backend!')

@app.route('/public_tweets', methods=['GET'])
def public_tweets():
    screen_name = 'barackobama'
    tweets = return_tweets_and_public_metrics(screen_name)
    return jsonify({
        'status': 'success',
        'tweets': tweets
    })

if __name__ == '__main__':
    print("Starting app")
    app.run(host='0.0.0.0', port=5050, debug=True)