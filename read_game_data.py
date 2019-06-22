#  Various functions for reading game data (json, txt, excel, csv)
import Game
import json
import datetime

# TODO - Look at replacing this with pandas


def read_json_data(filename):
    # read the json data
    with open(filename, "r") as read_file:
        json_data = json.load(read_file)

    games = json_data['games']
    data = []
    season = int(filename[5:9])

    for game in games:
        date_string = game['date']
        datetime_object = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        year = datetime_object.year
        month = datetime_object.month
        day = datetime_object.day
        date_object = datetime.date(year, month, day)
        h_team = game['home team']
        a_team = game['away team']
        h_score = game['home score']
        a_score = game['away score']
        gameRec = Game.Game(date_object, h_team, a_team, h_score, a_score)
        gameRec.season = season
        data.append(gameRec)

    return data
