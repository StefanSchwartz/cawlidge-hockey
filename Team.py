# Class that stores data and methods for a single team
class Team:

    def __init__(self, name, sport, conference, games=[]):
        self.name = name    # the name of the team
        self.sport = sport  # the sport the team plays
        self.conference = conference  # the conference the team plays in
        self.games = games  # list of games (Game objects)
