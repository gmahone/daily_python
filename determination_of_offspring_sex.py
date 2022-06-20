def chromosome_check(sperm):
    offspring_sex = "son" if "Y" in sperm else "daughter"
    return f"Congratulations! You\'re going to have a {offspring_sex}."


# using format
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')

# using format with dictionary
def chromosome_check(sperm):
    gender = {"XY" : "son", "XX" : "daughter"}
    return "Congratulations! You\'re going to have a {}.".format(gender[sperm])
