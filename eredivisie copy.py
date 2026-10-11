import requests
import json

response = requests.get('https://localhost:7224/api/eredivisie')

data = response.json()
print(data)

# standings = data['standings']
# table = standings[0]['table']

# print("## Team                 gs gw gl vl pt")

# for team in table:
#     print(f"{team['position']:>2} {team['team']['shortName']:<20} {team['playedGames']} {team['won']:>2} {team['draw']:>2} {team['lost']:>2} {team['points']:>2} {team['goalsFor']:>5} {team['goalsAgainst']:>2} {team['goalDifference']:>3}")


# for team in table:
#     print(team["team"]["shortName"], team["points"])

