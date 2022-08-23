def calculate_age(year_of_birth, current_year):
    year_diff = current_year - year_of_birth
    if year_diff > 0:
        result = "You are {} year{} old."
    elif year_diff < 0:
        result = "You will be born in {} year{}."
    else:
        result = "You were born this very year!"
    
    plural_suffix = "s"
    if abs(year_diff) == 1:
        plural_suffix = ""
    return result.format(abs(year_diff), plural_suffix)


# slimmer solution
def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'
