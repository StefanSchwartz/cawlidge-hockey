# Function to get the most recent rating from a dictionary of dates and ratings
def get_last_rating(r):
    dates = sorted(r)
    last_date = dates[len(dates)-1]
    last_rating = r[last_date]
    return last_rating
