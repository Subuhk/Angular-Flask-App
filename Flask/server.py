
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from teams import Team, Teams
from players import Players

app = Flask(__name__)
api = Api(app)

CORS(app)


api.add_resource(Teams, '/teams')
api.add_resource(Team, '/teams/<team_id>')


api.add_resource(Players, '/players')


if __name__ == '__main__':
    app.run(port=5002)
