from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load ticket data from JSON file
def load_ticket():
    with open("app\data.json", encoding='utf-8') as f:
        destinario = json.load(f)
    return destinario

destinario = load_ticket()

@app.route('/api/locals', methods=['GET'])
def get_locations():
    temp = [transport["city"] for transport in destinario['transport']]
    temp = list(dict.fromkeys(temp))
    return jsonify(temp)

# API endpoint to get all ticket
@app.route('/api/ticket', methods=['POST'])
def get_ticket():
    new_ticket = request.json
    print(new_ticket)
    return jsonify(destinario)

if __name__ == '__main__':
    app.run(port=3000)
