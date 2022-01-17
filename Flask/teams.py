from flask_restful import Resource
import json

teams = [
    {"id": 1, "abbreviation": "ATL", "city": "Atlanta", "conference": "East", "division": "Southeast", "fullName": "Atlanta Hawks",
     "name": "Hawks", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/atl.png"},
    {"id": 2, "abbreviation": "BOS", "city": "Boston", "conference": "East", "division": "Atlantic", "fullName": "Boston Celtics",
     "name": "Celtics", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/bos.png"},
    {"id": 3, "abbreviation": "BKN", "city": "Brooklyn", "conference": "East", "division": "Atlantic", "fullName": "Brooklyn Nets",
     "name": "Nets", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/bkn.png"},
    {"id": 4, "abbreviation": "CHA", "city": "Charlotte", "conference": "East", "division": "Southeast", "fullName": "Charlotte Hornets",
     "name": "Hornets", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/cha.png"},
    {"id": 5, "abbreviation": "CHI", "city": "Chicago", "conference": "East", "division": "Central", "fullName": "Chicago Bulls",
     "name": "Bulls", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/chi.png"},
    {"id": 6, "abbreviation": "CLE", "city": "Cleveland", "conference": "East", "division": "Central", "fullName": "Cleveland Cavaliers",
     "name": "Cavaliers", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/cle.png"},
    {"id": 7, "abbreviation": "DAL", "city": "Dallas", "conference": "West", "division": "Southwest", "fullName": "Dallas Mavericks",
     "name": "Mavericks", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/dal.png"},
    {"id": 8, "abbreviation": "DEN", "city": "Denver", "conference": "West", "division": "Northwest", "fullName": "Denver Nuggets",
     "name": "Nuggets", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/den.png"},
    {"id": 9, "abbreviation": "DET", "city": "Detroit", "conference": "East", "division": "Central", "fullName": "Detroit Pistons",
     "name": "Pistons", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/det.png"},
    {"id": 10, "abbreviation": "GSW", "city": "Golden State", "conference": "West", "division": "Pacific", "fullName": "Golden State Warriors",
     "name": "Warriors", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/gsw.png"},
    {"id": 11, "abbreviation": "HOU", "city": "Houston", "conference": "West", "division": "Southwest", "fullName": "Houston Rockets",
     "name": "Rockets", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/hou.png"},
    {"id": 12, "abbreviation": "IND", "city": "Indiana", "conference": "East", "division": "Central", "fullName": "Indiana Pacers",
     "name": "Pacers", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/ind.png"},
    {"id": 13, "abbreviation": "LAC", "city": "LA", "conference": "West", "division": "Pacific", "fullName": "LA Clippers",
     "name": "Clippers", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/lac.png"},
    {"id": 14, "abbreviation": "LAL", "city": "Los Angeles", "conference": "West", "division": "Pacific", "fullName": "Los Angeles Lakers",
     "name": "Lakers", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/lal.png"},
    {"id": 15, "abbreviation": "MEM", "city": "Memphis", "conference": "West", "division": "Southwest", "fullName": "Memphis Grizzlies",
     "name": "Grizzlies", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/mem.png"},
    {"id": 16, "abbreviation": "MIA", "city": "Miami", "conference": "East", "division": "Southeast", "fullName": "Miami Heat",
     "name": "Heat", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/mia.png"},
    {"id": 17, "abbreviation": "MIL", "city": "Milwaukee", "conference": "East", "division": "Central", "fullName": "Milwaukee Bucks",
     "name": "Bucks", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/mil.png"},
    {"id": 18, "abbreviation": "MIN", "city": "Minnesota", "conference": "West", "division": "Northwest", "fullName": "Minnesota Timberwolves",
     "name": "Timberwolves", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/min.png"},
    {"id": 19, "abbreviation": "NOP", "city": "New Orleans", "conference": "West", "division": "Southwest", "fullName": "New Orleans Pelicans",
     "name": "Pelicans", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/nop.png"},
    {"id": 20, "abbreviation": "NYK", "city": "New York", "conference": "East", "division": "Atlantic", "fullName": "New York Knicks",
     "name": "Knicks", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/nyk.png"},
    {"id": 21, "abbreviation": "OKC", "city": "Oklahoma City", "conference": "West", "division": "Northwest", "fullName": "Oklahoma City Thunder",
     "name": "Thunder", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/okc.png"},
    {"id": 22, "abbreviation": "ORL", "city": "Orlando", "conference": "East", "division": "Southeast", "fullName": "Orlando Magic",
     "name": "Magic", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/orl.png"},
    {"id": 23, "abbreviation": "PHI", "city": "Philadelphia", "conference": "East", "division": "Atlantic", "fullName": "Philadelphia 76ers",
     "name": "76ers", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/phi.png"},
    {"id": 24, "abbreviation": "PHX", "city": "Phoenix", "conference": "West", "division": "Pacific", "fullName": "Phoenix Suns",
     "name": "Suns", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/phx.png"},
    {"id": 25, "abbreviation": "POR", "city": "Portland", "conference": "West", "division": "Northwest", "fullName": "Portland Trail Blazers",
     "name": "Trail Blazers", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/por.png"},
    {"id": 26, "abbreviation": "SAC", "city": "Sacramento", "conference": "West", "division": "Pacific", "fullName": "Sacramento Kings",
     "name": "Kings", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/sac.png"},
    {"id": 27, "abbreviation": "SAS", "city": "San Antonio", "conference": "West", "division": "Southwest", "fullName": "San Antonio Spurs",
     "name": "Spurs", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/sas.png"},
    {"id": 28, "abbreviation": "TOR", "city": "Toronto", "conference": "East", "division": "Atlantic", "fullName": "Toronto Raptors",
     "name": "Raptors", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/tor.png"},
    {"id": 29, "abbreviation": "UTA", "city": "Utah", "conference": "West", "division": "Northwest", "fullName": "Utah Jazz",
     "name": "Jazz", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/uta.png"},
    {"id": 30, "abbreviation": "WAS", "city": "Washington", "conference": "East", "division": "Southeast", "fullName": "Washington Wizards",
     "name": "Wizards", "logoUrl": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/was.png"}
]


class Teams(Resource):
    def get(self):
        return teams


class Team(Resource):
    def get(self, team_id):
        team = [team for team in teams if team['id'] == int(team_id)]
        return team
