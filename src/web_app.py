from flask import Flask, request, jsonify
from motor_driver import MotorDriver

app = Flask(__name__)

motor_driver = MotorDriver()

# Serve the frontend directory
@app.route('/')
def serve_frontend():
    return app.send_static_file('frontend/index.html')

# Handle POST request
@app.route('/open-door', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    motor_driver.open_door()
    response = {'message': 'Door opened'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
