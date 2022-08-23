def calculate_age(year_of_birth, current_year):
    year_diff = current_year - year_of_birth
    if year_diff > 0:
        result = "You are {} years old"
    elif year_diff < 0:
        result = "You will be born in {} years"
    else:
        result = "You were born this very year!"
    return result.format(abs(year_diff))
