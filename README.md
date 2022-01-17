
The NBA Directory is a simple web app built In Angular 8 alongwith Python Flask RESTful API-

1. Lists All NBA Teams
2. Provides a detaisled view of team including Players table

### Run the Angular App
In the root directory, run:

- `npm install`
- `npm start`

You can validate the app is up and running by navigating to `http://localhost:4200/#/`.

### Run the FLask API

In the Flask directory, run:

- `pip install Flask`
- `pip install flask_cors`
- `python server.py`

There are three Flask RESTful api endpoints available to you:

- `GET` : `http://127.0.0.1:5002/teams` - Lists a high level detail of all the teams.
- `GET` : `http://127.0.0.1:5002/teams/<team_id>` - Details of team of specific id
- `GET` : `http://127.0.0.1:5002/players` - Lists all the players in the league.

 
