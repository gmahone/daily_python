def chromosome_check(sperm):
    offspring_sex = "son" if "X" in sperm else "daughter"
    return f"Congratulations, you\'re going to have a {offspring_sex}"
