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
    cheapest_price_confort = float('inf')
    cheapest_price_economic = float('inf')
    shortest_duration = float('inf')

    for ticket in tickets_options:
        price_confort = float(ticket["price_confort"].replace("R$ ", "").replace(",", "."))
        price_economic = float(ticket["price_econ"].replace("R$ ", "").replace(",", "."))
        duration_hours = int(ticket["duration"].replace("h", ""))

        # Check if it's cheaper than previous
        if price_confort < cheapest_price_confort:
            cheapest_price_confort = price_confort
            cheapest_ticket = ticket

        if price_economic < cheapest_price_economic:
            cheapest_price_economic = price_economic
            cheapest_ticket = ticket

        # Check if it's faster than previous
        if duration_hours < shortest_duration:
            shortest_duration = duration_hours
            fastest_ticket = ticket

    # If the cheapest is also the fastest, return only one ticket
    if cheapest_ticket["id"] == fastest_ticket["id"]:
        print(cheapest_price_economic)
        print(cheapest_price_confort)
        if cheapest_price_confort < cheapest_price_economic:
            price_range = "R$ {:.2f} - R$ {:.2f}".format(cheapest_price_confort, cheapest_price_economic)
        else:
            price_range = "R$ {:.2f} - R$ {:.2f}".format(cheapest_price_economic, cheapest_price_confort)
        ticket = {
            "name": cheapest_ticket["name"],
            "price":price_range,
            "duration": fastest_ticket["duration"],
            "seat_type": "",
            "seat_code": cheapest_ticket["bed"],
            "ticket_code": 2  # Both cheapest and fastest
        }
        return [ticket]

    # Otherwise, return both tickets
    cheapest = {
        "name": cheapest_ticket["name"],
        "price": "R$ {:.2f}".format(cheapest_price_economic),
        "duration": cheapest_ticket["duration"],
        "seat_type": "Poltrona",
        "seat_code": cheapest_ticket["bed"],
        "ticket_code": 0  # Cheapest
    }

    fastest = {
            "name": fastest_ticket["name"],
            "price": fastest_ticket["price_confort"],
            "duration": fastest_ticket["duration"],
            "seat_type": "Leito",
            "seat_code": fastest_ticket["bed"],
            "ticket_code": 1  # Fastest
        }

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
    _restult = search_ticket_per_city(city_requested, tickets_option)
    options = find_cheapest_fastest_tickets(_restult)
    print("cheapest:", options)

    test = {
        # "option1": option1,
        # "option2": option2
    }
    return jsonify(test)

if __name__ == '__main__':
    app.run(port=3000)
