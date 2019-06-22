# Various methods for importing the list of teams
import csv
import Team


def read_csv_data(filename, sport):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        teams = []

        for row in csv_reader:
            if line_count == 0:
                # skip the header row
                line_count += 1
            else:
                name = row[2]
                conference = row[1]
                team = Team.Team(name, sport, conference)
                teams.append(team)
                line_count += 1
    return teams
