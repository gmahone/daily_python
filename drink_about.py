def people_with_age_drink(age):
    if age < 14:
        drink = "toddy"
    elif age < 18:
        drink = "coke"
    elif age < 21:
        drink = "beer"
    else:
        drink = "whisky"
    return f"drink {drink}"

# solution using .format
def people_with_age_drink(age):
    if age < 14:
        drink = "toddy"
    elif age < 18:
        drink = "coke"
    elif age < 21:
        drink = "beer"
    else:
        drink = "whisky"
    return "drink {0}".format(drink)

# string of ifs
def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')
