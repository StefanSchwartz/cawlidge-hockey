from get_last_rating import get_last_rating
import csv


def print_ranking(ratings):
    rankings = {}

    for team in list(ratings):
        last_rating = get_last_rating(ratings[team])
        rankings[last_rating] = team

    outfile_name = 'Rankings.csv'
    with open(outfile_name, 'w') as outfile:
        fieldnames = ['ELO Score', 'Team']
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)

        for score in sorted(rankings, reverse=True):
            row_data = [score, rankings[score]]
            writer.writerow(row_data)
