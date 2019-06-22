# Class that stores data and methods for a single game
class Game:

    def __init__(self, date, home_team, away_team, home_score, away_score):
        self.date = date    # the date the game was played
        self.home_team = home_team  # Team object for the home team
        self.away_team = away_team  # Team object for the away team
        self.home_score = home_score  # number of points the home team scored
        self.away_score = away_score  # number of points the away team scored
        self.season = None  # the season the game was played in
