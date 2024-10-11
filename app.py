from flask import Flask, request, jsonify
import random
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/app-test-status', methods=['GET'])
def app_test_status():
    device_id = request.args.get('deviceId')
    if not device_id:
        return "Invalid request, missing deviceId", 400

    response = random.choices([
        {"status": "GOOD", "message": ""},
        {"status": "BAD", "message": "some message"}
    ], weights=[70, 30], k=1)[0]

    logging.info(f"Request received for deviceId: {device_id}, Response: {response}")
    return jsonify(response), 200

@app.route('/', methods=['GET', 'POST'])
def invalid_route():
    return "Invalid route", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)