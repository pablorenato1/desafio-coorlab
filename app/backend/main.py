from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def search_ticket_per_city(city, tickets_option):
    tickets_founded = []
    for ticket in tickets_option:
        if ticket['city'] == city:
            tickets_founded.append(ticket)
    return tickets_founded

def find_cheapest_fastest_tickets(tickets_options):
    cheapest_ticket = None
    fastest_ticket = None
    cheapest_price = float('inf')
    fastest_duration = float('inf')

    for ticket in tickets_options:
        price_confort = float(ticket["price_confort"].replace("R$ ", "").replace(",", "."))
        price_economic = float(ticket["price_econ"].replace("R$ ", "").replace(",", "."))
        duration_hours = int(ticket["duration"].replace("h", ""))

        # Check if the comfort ticket is cheaper
        if price_confort < price_economic:
            if price_confort < cheapest_price:
                cheapest_price = price_confort
                cheapest_ticket = ticket

        # Check if the economic ticket is cheaper
        else:
            if price_economic < cheapest_price:
                cheapest_price = price_economic
                cheapest_ticket = ticket

        # Check if it's faster than previous with comfort
        if price_confort < float('inf') and duration_hours < fastest_duration:
            fastest_duration = duration_hours
            fastest_ticket = ticket

    # Determine seat_code and seat_type based on the cheapest ticket
    if cheapest_ticket["price_confort"] < cheapest_ticket["price_econ"]:
        cheapest_seat_type = "Leito"
        cheapest_seat_code = cheapest_ticket["bed"]
    else:
        cheapest_seat_type = "Poltrona"
        cheapest_seat_code = cheapest_ticket["seat"]

    # Create the cheapest and fastest ticket objects
    cheapest = {
        "name": cheapest_ticket["name"],
        "price": "R$ {:.2f}".format(cheapest_price),
        "duration": cheapest_ticket["duration"],
        "seat_type": cheapest_seat_type,
        "seat_code": cheapest_seat_code,
        "ticket_code": 0  # Cheapest
    }

    fastest = {
        "name": fastest_ticket["name"],
        "price": "R$ {:.2f}".format(float(fastest_ticket["price_confort"].replace("R$ ", "").replace(",", "."))),
        "duration": fastest_ticket["duration"],
        "seat_type": "Leito",
        "seat_code": fastest_ticket["bed"],
        "ticket_code": 1  # Fastest
    }

    # If the cheapest and fastest are the same ticket
    if cheapest_ticket["id"] == fastest_ticket["id"]:
        return [fastest]
    else:
        return [cheapest, fastest]



def load_ticket():
    with open("app\data.json", encoding='utf-8') as f:
        tickets_option = json.load(f)
    return tickets_option['transport']


tickets_option = load_ticket()

@app.route('/api/locals', methods=['GET'])
def get_locations():
    temp = [transport["city"] for transport in tickets_option]
    temp = list(dict.fromkeys(temp))
    return jsonify(temp)

# API endpoint to get all ticket
@app.route('/api/ticket', methods=['POST'])
def get_ticket():
    city_requested = request.json
    _result = search_ticket_per_city(city_requested['location'], tickets_option)
    options = find_cheapest_fastest_tickets(_result)

    return jsonify(options)

if __name__ == '__main__':
    app.run(port=3000)
