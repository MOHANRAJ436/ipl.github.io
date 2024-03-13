from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__, static_url_path='')

teams = {
    'CSK': 45_00_00_000,
    'MI': 45_00_00_000,
    'RCB': 45_00_00_000,
    'SRH': 45_00_00_000,
    'KKR': 45_00_00_000,
    'GT': 45_00_00_000,
    'DC': 45_00_00_000,
    'PBKS': 45_00_00_000,
    'RR': 45_00_00_000,
    'LSG': 45_00_00_000,
}

players_sold = []

def convert_to_int(price_str):
    try:
        if 'CR' in price_str:
            return int(float(price_str.replace('CR', '')) * 100_00_000)
        elif 'L' in price_str:
            return int(float(price_str.replace('L', '')) * 1_00_000)
        else:
            return None
    except ValueError:
        return None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit-bid', methods=['POST'])
def submit_bid():
    player_name = request.json.get('playerName')
    price_input = request.json.get('price')
    team = request.json.get('team')

    if not player_name or not price_input or not team:
        return jsonify({'message': 'Missing player name, price, or team.'}), 400

    price = convert_to_int(price_input)
    if price is None:
        return jsonify({'message': 'Invalid price format. Please use "CR" for crores or "L" for lakhs.'}), 400

    if team not in teams:
        return jsonify({'message': 'Invalid team name. Try again.'}), 400

    if teams[team] < price:
        return jsonify({'message': f"{team} does not have enough funds to buy {player_name}."}), 400

    if player_name in [player['playerName'] for player in players_sold]:
        return jsonify({'message': f"{player_name} has already been sold."}), 400

    teams[team] -= price
    players_sold.append({'playerName': player_name, 'price': price, 'team': team})
    return jsonify({
    'message': f"{player_name} was bought by {team}. Remaining purse for all teams",
    'teams': dict(sorted(teams.items(), key=lambda x: x[1], reverse=True)),
    'playersSold': players_sold,
    'price': price_input 
})

if __name__ == '__main__':
    app.run(debug=True)
