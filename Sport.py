# Class that stores data and methods for a sport
class Sport:

    def __init__(self, name, k, team_list=[]):
        self.name = name    # the name of the sport
        self.team_list = team_list  # list of teams (Team objects)
        self.k = k  # ELO model parameter
