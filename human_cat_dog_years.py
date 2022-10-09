def human_years_cat_years_dog_years(human_years):
    result_human = human_years
    result_cat = 15
    result_dog = 15
    if human_years >= 2:
        result_cat += 9 + (4 * (human_years - 2))
        result_dog += 9 + (5 * (human_years - 2))
    return [result_human, result_cat, result_dog]


## fully conditional
def human_years_cat_years_dog_years(x):
    return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]
