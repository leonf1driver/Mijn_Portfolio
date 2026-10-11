import requests
import json

response = requests.get('http://api.football-data.org/v4/competitions/2003/standings', headers={'X-Auth-Token': 'b0fe2f5493c44f499240b4de7b010353'})

# eventueel huiswerk: verwerk deze web api in een HTML pagina

data = response.json()

with open('eredivisie.json','w') as f:
    f.write(response.text)

standings = data['standings']
table = standings[0]['table']

print("## Team                 gs gw gl vl pt")

for team in table:
    print(f"{team['position']:>2} {team['team']['shortName']:<20} {team['playedGames']} {team['won']:>2} {team['draw']:>2} {team['lost']:>2} {team['points']:>2} {team['goalsFor']:>5} {team['goalsAgainst']:>2} {team['goalDifference']:>3}")


# for team in table:
#     print(team["team"]["shortName"], team["points"])

