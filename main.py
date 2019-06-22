# main script to run college hockey model
import Sport
import read_team_list
import read_game_data
from calculate_new_rating import calculate_new_rating
from calculate_expected_result import calculate_expected_result
from get_last_rating import get_last_rating
from print_ranking import print_ranking
import datetime
import csv


Hockey = Sport.Sport('hockey', 10)
k = Hockey.k
initial_rating = 1500
initial_rating_date = datetime.date(datetime.MINYEAR, 1, 1)

teamfile = 'College Hockey Teams.csv'
Teams = read_team_list.read_csv_data(teamfile, Hockey.name)

ratings = {}

for team in Teams:
    temp_dict = {}
    temp_dict[initial_rating_date] = initial_rating
    ratings[team.name] = temp_dict

game_file = 'Data/1998-1999.json'
game_data = read_game_data.read_json_data(game_file)
game_data.sort(key=lambda game: game.date)  # sort the games by date

outfile_name = game_file[:-4]+'csv'
with open(outfile_name, 'w') as outfile:
    fieldnames = ['Date', 'Home Team', 'Rating', 'Win Probability']
    fieldnames[4:7] = ['Away Team', 'Rating', 'Win Probability', 'Home Score']
    fieldnames[8:10] = ['Away Score', 'Home Rating (New)', 'Away Rating (New)']
    writer = csv.writer(outfile)
    writer.writerow(fieldnames)

    for game in game_data:
        row_data = [str(game.date)]

        h_team = game.home_team
        h_ratings = ratings[h_team]
        last_h_rating = get_last_rating(h_ratings)
        row_data.append(h_team)
        row_data.append(last_h_rating)

        a_team = game.away_team
        a_ratings = ratings[a_team]
        last_a_rating = get_last_rating(a_ratings)
        row_data.append(a_team)
        row_data.append(last_a_rating)

        dr = (last_h_rating + 100) - last_a_rating   # TODO - make home-field advantage a property of the Sport class
        h_prob = calculate_expected_result(dr)
        a_prob = calculate_expected_result(-dr)
        row_data.insert(3, h_prob)
        row_data.append(a_prob)

        h_score = game.home_score
        a_score = game.away_score
        row_data.append(h_score)
        row_data.append(a_score)

        if (h_score > a_score):
            new_h_rating = calculate_new_rating(last_h_rating, k, 1, h_prob)
            new_a_rating = calculate_new_rating(last_a_rating, k, 0, a_prob)
        elif (h_score < a_score):
            new_h_rating = calculate_new_rating(last_h_rating, k, 0, h_prob)
            new_a_rating = calculate_new_rating(last_a_rating, k, 1, a_prob)
        elif (h_score == a_score):
            new_h_rating = calculate_new_rating(last_h_rating, k, 0.5, h_prob)
            new_a_rating = calculate_new_rating(last_a_rating, k, 0.5, a_prob)

        h_ratings[game.date] = new_h_rating
        ratings[h_team] = h_ratings
        a_ratings[game.date] = new_a_rating
        ratings[a_team] = a_ratings
        row_data.append(new_h_rating)
        row_data.append(new_a_rating)
        writer.writerow(row_data)

print_ranking(ratings)
