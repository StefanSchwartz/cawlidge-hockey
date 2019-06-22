#  Function to calculate the expected result (win probability)


def calculate_expected_result(dr):
    exp = - dr / 400
    expected_result = 1 / (pow(10, exp) + 1)
    return expected_result
