#  Function to update the rating of a team


def calculate_new_rating(original_rating, k, result, expected_result):
    new_rating = original_rating + (k * (result - expected_result))
    return new_rating
