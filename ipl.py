import pandas as pd
df = pd.read_excel(r"C:\Users\mohanraj\Downloads\Mock IPL Auction Player Rating  (1).xlsx")
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

def convert_to_int(price_str):
    if 'CR' in price_str:
        return int(float(price_str.replace('CR', '')) * 100_00_000)
    elif 'L' in price_str:
        return int(float(price_str.replace('L', '')) * 1_00_000)
    else:
        return None

while True:
    player_name = input("Enter player name (or 'q' to quit): ")
    if player_name.lower() == 'q':
        break

    price_input = input("Enter price (e.g., '1 CR' or '50L'): ")
    price = convert_to_int(price_input)
    if price is None:
        print("Invalid price format. Please use 'CR' for crores or 'L' for lakhs.")
        continue

    team = input("Enter sold team: ")

    if team not in teams:
        print("Invalid team name. Try again.")
        continue

    if teams[team] < price:
        print(f"{team} does not have enough funds to buy {player_name}.")
        continue

    teams[team] -= price
    print(f"{player_name} was bought by {team}. Remaining purse for {team}: {teams[team]}")

    print("Remaining purse for all teams:")
    for team_name, team_purse in teams.items():
        print(f"{team_name}: {team_purse}")

for team, purse in teams.items():
    print(f"{team}: {purse}")
