from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load ticket data from JSON file
def load_ticket():
    with open("app\data.json") as f:
        ticket = json.load(f)
    print(ticket)
    return ticket

ticket = load_ticket()

# API endpoint to get all ticket
@app.route('/api/ticket', methods=['GET'])
def get_ticket():
    print("test")
    print(ticket)
    return jsonify(ticket)

if __name__ == '__main__':
    app.run(port=3000)
